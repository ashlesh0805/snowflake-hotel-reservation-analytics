-- ============================================================================
-- HOTEL RESERVATION ANALYTICS - SNOWFLAKE PROJECT
-- ============================================================================
-- Project  : Hotel Reservation Analytics System
-- Scenario : A hotel chain wants to analyze reservations and room occupancy
-- Components: Stage + COPY + Task + Monitoring
-- ============================================================================


-- ============================================================================
-- STEP 1: ENVIRONMENT SETUP - Database, Schema, Warehouse
-- ============================================================================

-- Create Warehouse
CREATE OR REPLACE WAREHOUSE HOTEL_WH
    WAREHOUSE_SIZE = 'XSMALL'
    AUTO_SUSPEND = 120
    AUTO_RESUME = TRUE
    COMMENT = 'Warehouse for Hotel Reservation Analytics';

USE WAREHOUSE HOTEL_WH;

-- Create Database
CREATE OR REPLACE DATABASE HOTEL_RESERVATION_DB
    COMMENT = 'Database for Hotel Reservation Analytics System';

-- Create Schemas (Layered Architecture)
CREATE OR REPLACE SCHEMA HOTEL_RESERVATION_DB.RAW
    COMMENT = 'Raw layer - Landing zone for source data';

CREATE OR REPLACE SCHEMA HOTEL_RESERVATION_DB.CLEAN
    COMMENT = 'Clean layer - Validated and transformed data';

CREATE OR REPLACE SCHEMA HOTEL_RESERVATION_DB.ANALYTICS
    COMMENT = 'Analytics layer - Aggregated tables and final reports';


-- ============================================================================
-- STEP 2: CREATE RAW TABLES
-- ============================================================================

USE SCHEMA HOTEL_RESERVATION_DB.RAW;

-- RAW Guests Table
CREATE OR REPLACE TABLE RAW_GUESTS (
    guest_id        VARCHAR(10),
    first_name      VARCHAR(50),
    last_name       VARCHAR(50),
    email           VARCHAR(100),
    phone           VARCHAR(20),
    city            VARCHAR(50),
    country         VARCHAR(50),
    loyalty_tier    VARCHAR(20),
    created_date    DATE,
    load_timestamp  TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

-- RAW Rooms Table
CREATE OR REPLACE TABLE RAW_ROOMS (
    room_id          VARCHAR(10),
    hotel_name       VARCHAR(100),
    room_number      VARCHAR(10),
    room_type        VARCHAR(30),
    floor            INT,
    capacity         INT,
    price_per_night  DECIMAL(10,2),
    is_active        BOOLEAN,
    load_timestamp   TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

-- RAW Reservations Table
CREATE OR REPLACE TABLE RAW_RESERVATIONS (
    reservation_id      VARCHAR(10),
    guest_id            VARCHAR(10),
    room_id             VARCHAR(10),
    check_in_date       DATE,
    check_out_date      DATE,
    num_guests          INT,
    reservation_status  VARCHAR(20),
    booking_source      VARCHAR(20),
    created_at          TIMESTAMP_NTZ,
    load_timestamp      TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

-- RAW Payments Table
CREATE OR REPLACE TABLE RAW_PAYMENTS (
    payment_id       VARCHAR(10),
    reservation_id   VARCHAR(10),
    payment_date     DATE,
    amount           DECIMAL(10,2),
    payment_method   VARCHAR(20),
    payment_status   VARCHAR(20),
    currency         VARCHAR(5),
    load_timestamp   TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);


-- ============================================================================
-- STEP 3: CREATE FILE FORMAT & STAGE (S3)
-- ============================================================================

-- CSV File Format
CREATE OR REPLACE FILE FORMAT HOTEL_RESERVATION_DB.RAW.CSV_FORMAT
    TYPE = 'CSV'
    FIELD_DELIMITER = ','
    SKIP_HEADER = 1
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    NULL_IF = ('NULL', 'null', '')
    TRIM_SPACE = TRUE
    ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE
    COMMENT = 'Standard CSV format for hotel data files';

-- Create External Stage (S3)
-- NOTE: Replace <your-bucket>, <aws_key>, <aws_secret> with actual values
CREATE OR REPLACE STAGE HOTEL_RESERVATION_DB.RAW.HOTEL_S3_STAGE
    URL = 's3://your-hotel-reservation-bucket/data/'
    -- CREDENTIALS = (AWS_KEY_ID = '<aws_key>' AWS_SECRET_KEY = '<aws_secret>')
    FILE_FORMAT = HOTEL_RESERVATION_DB.RAW.CSV_FORMAT
    COMMENT = 'S3 stage for hotel reservation CSV files';

-- Verify Stage
-- LIST @HOTEL_RESERVATION_DB.RAW.HOTEL_S3_STAGE;


-- ============================================================================
-- STEP 4: COPY DATA INTO RAW TABLES (COPY INTO)
-- ============================================================================

-- Load Guests
COPY INTO HOTEL_RESERVATION_DB.RAW.RAW_GUESTS
    (guest_id, first_name, last_name, email, phone, city, country, loyalty_tier, created_date)
FROM @HOTEL_RESERVATION_DB.RAW.HOTEL_S3_STAGE/guests.csv
FILE_FORMAT = (FORMAT_NAME = HOTEL_RESERVATION_DB.RAW.CSV_FORMAT)
ON_ERROR = 'CONTINUE';

-- Load Rooms
COPY INTO HOTEL_RESERVATION_DB.RAW.RAW_ROOMS
    (room_id, hotel_name, room_number, room_type, floor, capacity, price_per_night, is_active)
FROM @HOTEL_RESERVATION_DB.RAW.HOTEL_S3_STAGE/rooms.csv
FILE_FORMAT = (FORMAT_NAME = HOTEL_RESERVATION_DB.RAW.CSV_FORMAT)
ON_ERROR = 'CONTINUE';

-- Load Reservations
COPY INTO HOTEL_RESERVATION_DB.RAW.RAW_RESERVATIONS
    (reservation_id, guest_id, room_id, check_in_date, check_out_date, num_guests, reservation_status, booking_source, created_at)
FROM @HOTEL_RESERVATION_DB.RAW.HOTEL_S3_STAGE/reservations.csv
FILE_FORMAT = (FORMAT_NAME = HOTEL_RESERVATION_DB.RAW.CSV_FORMAT)
ON_ERROR = 'CONTINUE';

-- Load Payments
COPY INTO HOTEL_RESERVATION_DB.RAW.RAW_PAYMENTS
    (payment_id, reservation_id, payment_date, amount, payment_method, payment_status, currency)
FROM @HOTEL_RESERVATION_DB.RAW.HOTEL_S3_STAGE/payments.csv
FILE_FORMAT = (FORMAT_NAME = HOTEL_RESERVATION_DB.RAW.CSV_FORMAT)
ON_ERROR = 'CONTINUE';

-- Verify Row Counts
SELECT 'RAW_GUESTS' AS table_name, COUNT(*) AS row_count FROM RAW_GUESTS
UNION ALL
SELECT 'RAW_ROOMS', COUNT(*) FROM RAW_ROOMS
UNION ALL
SELECT 'RAW_RESERVATIONS', COUNT(*) FROM RAW_RESERVATIONS
UNION ALL
SELECT 'RAW_PAYMENTS', COUNT(*) FROM RAW_PAYMENTS;


-- ============================================================================
-- STEP 5: VALIDATE RESERVATION DATES
-- ============================================================================

USE SCHEMA HOTEL_RESERVATION_DB.CLEAN;

-- Create a view to flag invalid reservation dates
CREATE OR REPLACE VIEW HOTEL_RESERVATION_DB.CLEAN.V_RESERVATION_DATE_VALIDATION AS
SELECT
    r.reservation_id,
    r.guest_id,
    r.room_id,
    r.check_in_date,
    r.check_out_date,
    r.reservation_status,
    DATEDIFF('day', r.check_in_date, r.check_out_date) AS stay_duration_days,
    CASE
        WHEN r.check_in_date IS NULL OR r.check_out_date IS NULL
            THEN 'INVALID - NULL dates'
        WHEN r.check_out_date < r.check_in_date
            THEN 'INVALID - Checkout before Checkin'
        WHEN r.check_out_date = r.check_in_date
            THEN 'INVALID - Zero night stay'
        WHEN DATEDIFF('day', r.check_in_date, r.check_out_date) > 365
            THEN 'WARNING - Stay exceeds 365 days'
        ELSE 'VALID'
    END AS date_validation_status
FROM HOTEL_RESERVATION_DB.RAW.RAW_RESERVATIONS r;

-- View validation results
-- SELECT * FROM V_RESERVATION_DATE_VALIDATION ORDER BY date_validation_status DESC;

-- Summary of validation
-- SELECT date_validation_status, COUNT(*) AS count
-- FROM V_RESERVATION_DATE_VALIDATION
-- GROUP BY date_validation_status
-- ORDER BY count DESC;

-- Create CLEAN reservations (only valid records)
CREATE OR REPLACE TABLE HOTEL_RESERVATION_DB.CLEAN.CLEAN_RESERVATIONS AS
SELECT
    r.reservation_id,
    r.guest_id,
    r.room_id,
    r.check_in_date,
    r.check_out_date,
    DATEDIFF('day', r.check_in_date, r.check_out_date) AS stay_duration_days,
    r.num_guests,
    r.reservation_status,
    r.booking_source,
    r.created_at,
    r.load_timestamp
FROM HOTEL_RESERVATION_DB.RAW.RAW_RESERVATIONS r
WHERE r.check_in_date IS NOT NULL
  AND r.check_out_date IS NOT NULL
  AND r.check_out_date > r.check_in_date;

-- Clean Guests
CREATE OR REPLACE TABLE HOTEL_RESERVATION_DB.CLEAN.CLEAN_GUESTS AS
SELECT * FROM HOTEL_RESERVATION_DB.RAW.RAW_GUESTS
WHERE guest_id IS NOT NULL;

-- Clean Rooms
CREATE OR REPLACE TABLE HOTEL_RESERVATION_DB.CLEAN.CLEAN_ROOMS AS
SELECT * FROM HOTEL_RESERVATION_DB.RAW.RAW_ROOMS
WHERE room_id IS NOT NULL;

-- Clean Payments
CREATE OR REPLACE TABLE HOTEL_RESERVATION_DB.CLEAN.CLEAN_PAYMENTS AS
SELECT * FROM HOTEL_RESERVATION_DB.RAW.RAW_PAYMENTS
WHERE payment_id IS NOT NULL
  AND amount >= 0;


-- ============================================================================
-- STEP 6: IDENTIFY CANCELLED RESERVATIONS
-- ============================================================================

-- Cancelled Reservations Report
CREATE OR REPLACE VIEW HOTEL_RESERVATION_DB.CLEAN.V_CANCELLED_RESERVATIONS AS
SELECT
    cr.reservation_id,
    g.first_name || ' ' || g.last_name      AS guest_name,
    g.email                                   AS guest_email,
    g.loyalty_tier,
    rm.hotel_name,
    rm.room_type,
    rm.room_number,
    cr.check_in_date,
    cr.check_out_date,
    cr.stay_duration_days,
    cr.booking_source,
    cr.created_at                             AS booking_date,
    DATEDIFF('day', cr.created_at, cr.check_in_date)  AS days_before_checkin_cancelled,
    p.amount                                  AS refund_amount,
    p.payment_method,
    p.payment_status
FROM HOTEL_RESERVATION_DB.CLEAN.CLEAN_RESERVATIONS cr
JOIN HOTEL_RESERVATION_DB.CLEAN.CLEAN_GUESTS g
    ON cr.guest_id = g.guest_id
JOIN HOTEL_RESERVATION_DB.CLEAN.CLEAN_ROOMS rm
    ON cr.room_id = rm.room_id
LEFT JOIN HOTEL_RESERVATION_DB.CLEAN.CLEAN_PAYMENTS p
    ON cr.reservation_id = p.reservation_id
WHERE cr.reservation_status = 'Cancelled';

-- Cancellation Summary by Hotel
-- SELECT hotel_name, COUNT(*) AS cancellations, SUM(refund_amount) AS total_refunded
-- FROM V_CANCELLED_RESERVATIONS
-- GROUP BY hotel_name
-- ORDER BY cancellations DESC;

-- Cancellation Summary by Booking Source
-- SELECT booking_source, COUNT(*) AS cancellations
-- FROM V_CANCELLED_RESERVATIONS
-- GROUP BY booking_source
-- ORDER BY cancellations DESC;


-- ============================================================================
-- STEP 7: CALCULATE OCCUPANCY PERCENTAGE
-- ============================================================================

USE SCHEMA HOTEL_RESERVATION_DB.ANALYTICS;

-- Occupancy = (Total Booked Room-Nights / Total Available Room-Nights) * 100
-- For October 2024 analysis period

CREATE OR REPLACE VIEW HOTEL_RESERVATION_DB.ANALYTICS.V_MONTHLY_OCCUPANCY AS
WITH date_range AS (
    -- Generate analysis period (October 2024)
    SELECT
        DATE_TRUNC('MONTH', cr.check_in_date) AS analysis_month
    FROM HOTEL_RESERVATION_DB.CLEAN.CLEAN_RESERVATIONS cr
    WHERE cr.reservation_status != 'Cancelled'
    GROUP BY 1
),
available_rooms AS (
    -- Total active rooms per hotel
    SELECT
        hotel_name,
        COUNT(*) AS total_rooms
    FROM HOTEL_RESERVATION_DB.CLEAN.CLEAN_ROOMS
    WHERE is_active = TRUE
    GROUP BY hotel_name
),
booked_room_nights AS (
    -- Total booked room-nights per hotel per month (exclude cancelled)
    SELECT
        rm.hotel_name,
        DATE_TRUNC('MONTH', cr.check_in_date) AS booking_month,
        SUM(cr.stay_duration_days)             AS total_booked_nights
    FROM HOTEL_RESERVATION_DB.CLEAN.CLEAN_RESERVATIONS cr
    JOIN HOTEL_RESERVATION_DB.CLEAN.CLEAN_ROOMS rm
        ON cr.room_id = rm.room_id
    WHERE cr.reservation_status != 'Cancelled'
    GROUP BY rm.hotel_name, DATE_TRUNC('MONTH', cr.check_in_date)
)
SELECT
    brn.hotel_name,
    brn.booking_month,
    ar.total_rooms,
    -- Days in month
    DATEDIFF('day',
        brn.booking_month,
        DATEADD('MONTH', 1, brn.booking_month)
    ) AS days_in_month,
    -- Total available room-nights = rooms * days in month
    ar.total_rooms * DATEDIFF('day',
        brn.booking_month,
        DATEADD('MONTH', 1, brn.booking_month)
    ) AS total_available_nights,
    brn.total_booked_nights,
    -- Occupancy Percentage
    ROUND(
        (brn.total_booked_nights * 100.0) /
        NULLIF(ar.total_rooms * DATEDIFF('day',
            brn.booking_month,
            DATEADD('MONTH', 1, brn.booking_month)
        ), 0),
    2) AS occupancy_pct
FROM booked_room_nights brn
JOIN available_rooms ar
    ON brn.hotel_name = ar.hotel_name
ORDER BY brn.booking_month, brn.hotel_name;


-- ============================================================================
-- STEP 8: CALCULATE HOTEL & ROOM-TYPE REVENUE
-- ============================================================================

-- Revenue by Hotel
CREATE OR REPLACE VIEW HOTEL_RESERVATION_DB.ANALYTICS.V_REVENUE_BY_HOTEL AS
SELECT
    rm.hotel_name,
    DATE_TRUNC('MONTH', cr.check_in_date)          AS revenue_month,
    COUNT(DISTINCT cr.reservation_id)               AS total_reservations,
    COUNT(DISTINCT CASE
        WHEN cr.reservation_status = 'Cancelled' THEN cr.reservation_id
    END)                                            AS cancelled_reservations,
    COUNT(DISTINCT CASE
        WHEN cr.reservation_status != 'Cancelled' THEN cr.reservation_id
    END)                                            AS active_reservations,
    SUM(CASE
        WHEN p.payment_status = 'Completed' THEN p.amount ELSE 0
    END)                                            AS total_revenue,
    SUM(CASE
        WHEN p.payment_status = 'Refunded' THEN p.amount ELSE 0
    END)                                            AS total_refunded,
    SUM(CASE
        WHEN p.payment_status = 'Completed' THEN p.amount ELSE 0
    END) - SUM(CASE
        WHEN p.payment_status = 'Refunded' THEN p.amount ELSE 0
    END)                                            AS net_revenue
FROM HOTEL_RESERVATION_DB.CLEAN.CLEAN_RESERVATIONS cr
JOIN HOTEL_RESERVATION_DB.CLEAN.CLEAN_ROOMS rm
    ON cr.room_id = rm.room_id
LEFT JOIN HOTEL_RESERVATION_DB.CLEAN.CLEAN_PAYMENTS p
    ON cr.reservation_id = p.reservation_id
GROUP BY rm.hotel_name, DATE_TRUNC('MONTH', cr.check_in_date)
ORDER BY revenue_month, hotel_name;

-- Revenue by Room Type
CREATE OR REPLACE VIEW HOTEL_RESERVATION_DB.ANALYTICS.V_REVENUE_BY_ROOM_TYPE AS
SELECT
    rm.hotel_name,
    rm.room_type,
    rm.price_per_night                              AS listed_price,
    COUNT(DISTINCT cr.reservation_id)               AS total_bookings,
    SUM(cr.stay_duration_days)                      AS total_nights_booked,
    SUM(CASE
        WHEN p.payment_status = 'Completed' THEN p.amount ELSE 0
    END)                                            AS total_revenue,
    ROUND(AVG(CASE
        WHEN p.payment_status = 'Completed' THEN p.amount
    END), 2)                                        AS avg_revenue_per_booking,
    ROUND(SUM(CASE
        WHEN p.payment_status = 'Completed' THEN p.amount ELSE 0
    END) / NULLIF(SUM(cr.stay_duration_days), 0), 2) AS avg_revenue_per_night
FROM HOTEL_RESERVATION_DB.CLEAN.CLEAN_RESERVATIONS cr
JOIN HOTEL_RESERVATION_DB.CLEAN.CLEAN_ROOMS rm
    ON cr.room_id = rm.room_id
LEFT JOIN HOTEL_RESERVATION_DB.CLEAN.CLEAN_PAYMENTS p
    ON cr.reservation_id = p.reservation_id
WHERE cr.reservation_status != 'Cancelled'
GROUP BY rm.hotel_name, rm.room_type, rm.price_per_night
ORDER BY rm.hotel_name, total_revenue DESC;


-- ============================================================================
-- STEP 9: FINAL RESERVATION ANALYTICS TABLE
-- ============================================================================

CREATE OR REPLACE TABLE HOTEL_RESERVATION_DB.ANALYTICS.FACT_RESERVATION_ANALYTICS AS
SELECT
    -- Reservation Details
    cr.reservation_id,
    cr.reservation_status,
    cr.booking_source,
    cr.check_in_date,
    cr.check_out_date,
    cr.stay_duration_days,
    cr.num_guests,
    cr.created_at                                    AS booking_date,

    -- Guest Details
    g.guest_id,
    g.first_name || ' ' || g.last_name              AS guest_name,
    g.email                                          AS guest_email,
    g.city                                           AS guest_city,
    g.country                                        AS guest_country,
    g.loyalty_tier,

    -- Room Details
    rm.room_id,
    rm.hotel_name,
    rm.room_number,
    rm.room_type,
    rm.floor                                         AS room_floor,
    rm.capacity                                      AS room_capacity,
    rm.price_per_night,

    -- Payment Details
    p.payment_id,
    p.payment_date,
    p.amount                                         AS payment_amount,
    p.payment_method,
    p.payment_status,

    -- Derived Metrics
    DATEDIFF('day', cr.created_at, cr.check_in_date) AS lead_time_days,
    cr.stay_duration_days * rm.price_per_night        AS expected_revenue,
    CASE
        WHEN p.payment_status = 'Completed' THEN p.amount
        ELSE 0
    END                                              AS actual_revenue,
    CASE
        WHEN p.payment_status = 'Refunded' THEN p.amount
        ELSE 0
    END                                              AS refunded_amount,
    CASE
        WHEN cr.reservation_status = 'Cancelled' THEN TRUE
        ELSE FALSE
    END                                              AS is_cancelled,
    CASE
        WHEN cr.reservation_status = 'Checked-Out' THEN TRUE
        ELSE FALSE
    END                                              AS is_completed,

    -- Metadata
    CURRENT_TIMESTAMP()                              AS etl_loaded_at

FROM HOTEL_RESERVATION_DB.CLEAN.CLEAN_RESERVATIONS cr
LEFT JOIN HOTEL_RESERVATION_DB.CLEAN.CLEAN_GUESTS g
    ON cr.guest_id = g.guest_id
LEFT JOIN HOTEL_RESERVATION_DB.CLEAN.CLEAN_ROOMS rm
    ON cr.room_id = rm.room_id
LEFT JOIN HOTEL_RESERVATION_DB.CLEAN.CLEAN_PAYMENTS p
    ON cr.reservation_id = p.reservation_id;

-- Verify final analytics table
-- SELECT * FROM FACT_RESERVATION_ANALYTICS LIMIT 10;
-- SELECT COUNT(*) AS total_records FROM FACT_RESERVATION_ANALYTICS;


-- ============================================================================
-- STEP 10: SCHEDULED TASK FOR AGGREGATION
-- ============================================================================

USE SCHEMA HOTEL_RESERVATION_DB.ANALYTICS;

-- Create the daily aggregation summary table
CREATE OR REPLACE TABLE HOTEL_RESERVATION_DB.ANALYTICS.DAILY_RESERVATION_SUMMARY (
    summary_date             DATE,
    hotel_name               VARCHAR(100),
    room_type                VARCHAR(30),
    total_reservations       INT,
    confirmed_reservations   INT,
    cancelled_reservations   INT,
    checked_out_reservations INT,
    total_nights_booked      INT,
    total_revenue            DECIMAL(12,2),
    total_refunded           DECIMAL(12,2),
    net_revenue              DECIMAL(12,2),
    avg_stay_duration        DECIMAL(5,2),
    avg_lead_time_days       DECIMAL(5,2),
    occupancy_pct            DECIMAL(5,2),
    top_booking_source       VARCHAR(20),
    aggregated_at            TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

-- Create the scheduled Task (runs daily at 6 AM UTC)
CREATE OR REPLACE TASK HOTEL_RESERVATION_DB.ANALYTICS.TASK_DAILY_RESERVATION_AGGREGATION
    WAREHOUSE = HOTEL_WH
    SCHEDULE  = 'USING CRON 0 6 * * * UTC'
    COMMENT   = 'Daily aggregation of hotel reservation analytics'
AS
-- Merge/Insert daily summary
INSERT INTO HOTEL_RESERVATION_DB.ANALYTICS.DAILY_RESERVATION_SUMMARY
(
    summary_date,
    hotel_name,
    room_type,
    total_reservations,
    confirmed_reservations,
    cancelled_reservations,
    checked_out_reservations,
    total_nights_booked,
    total_revenue,
    total_refunded,
    net_revenue,
    avg_stay_duration,
    avg_lead_time_days,
    occupancy_pct,
    top_booking_source,
    aggregated_at
)
WITH reservation_agg AS (
    SELECT
        CURRENT_DATE()                                   AS summary_date,
        fa.hotel_name,
        fa.room_type,
        COUNT(*)                                         AS total_reservations,
        SUM(CASE WHEN fa.reservation_status = 'Confirmed'   THEN 1 ELSE 0 END) AS confirmed_reservations,
        SUM(CASE WHEN fa.reservation_status = 'Cancelled'   THEN 1 ELSE 0 END) AS cancelled_reservations,
        SUM(CASE WHEN fa.reservation_status = 'Checked-Out' THEN 1 ELSE 0 END) AS checked_out_reservations,
        SUM(fa.stay_duration_days)                       AS total_nights_booked,
        SUM(fa.actual_revenue)                           AS total_revenue,
        SUM(fa.refunded_amount)                          AS total_refunded,
        SUM(fa.actual_revenue) - SUM(fa.refunded_amount) AS net_revenue,
        ROUND(AVG(fa.stay_duration_days), 2)             AS avg_stay_duration,
        ROUND(AVG(fa.lead_time_days), 2)                 AS avg_lead_time_days
    FROM HOTEL_RESERVATION_DB.ANALYTICS.FACT_RESERVATION_ANALYTICS fa
    GROUP BY fa.hotel_name, fa.room_type
),
top_source AS (
    SELECT
        fa.hotel_name,
        fa.room_type,
        fa.booking_source,
        COUNT(*) AS src_count,
        ROW_NUMBER() OVER (
            PARTITION BY fa.hotel_name, fa.room_type
            ORDER BY COUNT(*) DESC
        ) AS rn
    FROM HOTEL_RESERVATION_DB.ANALYTICS.FACT_RESERVATION_ANALYTICS fa
    GROUP BY fa.hotel_name, fa.room_type, fa.booking_source
),
available AS (
    SELECT
        hotel_name,
        room_type,
        COUNT(*) AS room_count
    FROM HOTEL_RESERVATION_DB.CLEAN.CLEAN_ROOMS
    WHERE is_active = TRUE
    GROUP BY hotel_name, room_type
)
SELECT
    ra.summary_date,
    ra.hotel_name,
    ra.room_type,
    ra.total_reservations,
    ra.confirmed_reservations,
    ra.cancelled_reservations,
    ra.checked_out_reservations,
    ra.total_nights_booked,
    ra.total_revenue,
    ra.total_refunded,
    ra.net_revenue,
    ra.avg_stay_duration,
    ra.avg_lead_time_days,
    -- Occupancy: booked nights / (available rooms * 30 days) * 100
    ROUND(
        (ra.total_nights_booked * 100.0) /
        NULLIF(av.room_count * 30, 0),
    2)                                                   AS occupancy_pct,
    ts.booking_source                                    AS top_booking_source,
    CURRENT_TIMESTAMP()                                  AS aggregated_at
FROM reservation_agg ra
LEFT JOIN top_source ts
    ON ra.hotel_name = ts.hotel_name
    AND ra.room_type = ts.room_type
    AND ts.rn = 1
LEFT JOIN available av
    ON ra.hotel_name = av.hotel_name
    AND ra.room_type = av.room_type;


-- ============================================================================
-- STEP 11: ENABLE TASK & MONITOR TASK HISTORY
-- ============================================================================

-- Resume (enable) the Task
ALTER TASK HOTEL_RESERVATION_DB.ANALYTICS.TASK_DAILY_RESERVATION_AGGREGATION RESUME;

-- Verify Task is running
SHOW TASKS IN SCHEMA HOTEL_RESERVATION_DB.ANALYTICS;

-- Manually execute the task for testing
EXECUTE TASK HOTEL_RESERVATION_DB.ANALYTICS.TASK_DAILY_RESERVATION_AGGREGATION;

-- ============================================================================
-- STEP 12: CHECK TASK HISTORY & MONITORING
-- ============================================================================

-- Check Task Run History (last 10 runs)
SELECT
    NAME,
    DATABASE_NAME,
    SCHEMA_NAME,
    STATE,
    SCHEDULED_TIME,
    COMPLETED_TIME,
    ERROR_CODE,
    ERROR_MESSAGE,
    RETURN_VALUE
FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY(
    TASK_NAME => 'TASK_DAILY_RESERVATION_AGGREGATION',
    SCHEDULED_TIME_RANGE_START => DATEADD('DAY', -7, CURRENT_TIMESTAMP()),
    RESULT_LIMIT => 10
))
ORDER BY SCHEDULED_TIME DESC;

-- Overall Task monitoring query
SELECT
    NAME,
    STATE,
    SCHEDULED_TIME,
    COMPLETED_TIME,
    DATEDIFF('SECOND', SCHEDULED_TIME, COMPLETED_TIME) AS duration_seconds,
    ERROR_MESSAGE
FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY())
WHERE DATABASE_NAME = 'HOTEL_RESERVATION_DB'
ORDER BY SCHEDULED_TIME DESC
LIMIT 20;

-- Verify the Daily Summary Table has data
SELECT * FROM HOTEL_RESERVATION_DB.ANALYTICS.DAILY_RESERVATION_SUMMARY
ORDER BY hotel_name, room_type;


-- ============================================================================
-- STEP 13: USEFUL ANALYTICAL QUERIES
-- ============================================================================

-- 1. Overall KPIs
SELECT
    COUNT(*)                                              AS total_reservations,
    SUM(CASE WHEN is_cancelled THEN 1 ELSE 0 END)        AS cancellations,
    ROUND(SUM(CASE WHEN is_cancelled THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2)
                                                          AS cancellation_rate_pct,
    SUM(actual_revenue)                                   AS total_revenue,
    ROUND(AVG(stay_duration_days), 1)                     AS avg_stay_nights,
    ROUND(AVG(lead_time_days), 1)                         AS avg_booking_lead_days
FROM HOTEL_RESERVATION_DB.ANALYTICS.FACT_RESERVATION_ANALYTICS;

-- 2. Revenue by Loyalty Tier
SELECT
    loyalty_tier,
    COUNT(*)               AS bookings,
    SUM(actual_revenue)    AS total_revenue,
    ROUND(AVG(actual_revenue), 2) AS avg_revenue
FROM HOTEL_RESERVATION_DB.ANALYTICS.FACT_RESERVATION_ANALYTICS
WHERE NOT is_cancelled
GROUP BY loyalty_tier
ORDER BY total_revenue DESC;

-- 3. Booking Source Analysis
SELECT
    booking_source,
    COUNT(*)                                                  AS total_bookings,
    SUM(CASE WHEN is_cancelled THEN 1 ELSE 0 END)            AS cancellations,
    ROUND(SUM(CASE WHEN is_cancelled THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2)
                                                              AS cancel_rate_pct,
    SUM(actual_revenue)                                       AS revenue
FROM HOTEL_RESERVATION_DB.ANALYTICS.FACT_RESERVATION_ANALYTICS
GROUP BY booking_source
ORDER BY total_bookings DESC;

-- 4. Monthly Trend
SELECT
    DATE_TRUNC('MONTH', check_in_date)                        AS month,
    COUNT(*)                                                  AS reservations,
    SUM(actual_revenue)                                       AS revenue,
    ROUND(AVG(stay_duration_days), 1)                         AS avg_stay
FROM HOTEL_RESERVATION_DB.ANALYTICS.FACT_RESERVATION_ANALYTICS
WHERE NOT is_cancelled
GROUP BY DATE_TRUNC('MONTH', check_in_date)
ORDER BY month;


-- ============================================================================
-- CLEANUP (Run only when you want to tear down the project)
-- ============================================================================

-- ALTER TASK HOTEL_RESERVATION_DB.ANALYTICS.TASK_DAILY_RESERVATION_AGGREGATION SUSPEND;
-- DROP DATABASE HOTEL_RESERVATION_DB;
-- DROP WAREHOUSE HOTEL_WH;
