import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_perfect_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Minimalist Japanese Color Palette (Zen / Editorial)
    C_BG = RGBColor(252, 252, 250)         # Warm rice-paper white
    C_WHITE = RGBColor(255, 255, 255)      # Pure white
    C_SUMI = RGBColor(24, 24, 27)          # Sumi charcoal black
    C_SLATE = RGBColor(82, 82, 91)         # Soft slate
    C_MUTED = RGBColor(161, 161, 170)      # Muted gray
    C_BORDER = RGBColor(228, 228, 231)     # Hairline border
    C_RED = RGBColor(200, 35, 51)          # Japanese Vermilion / Torii Red
    C_INDIGO = RGBColor(30, 58, 138)       # Indigo
    C_MATCHA = RGBColor(21, 128, 61)       # Matcha green

    def add_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG
        bg.line.fill.background()
        return bg

    def add_header(slide, number_str, category_str, title_str, subtitle_str=""):
        # Vermilion Hanko Square Badge
        stamp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.85), Inches(0.55), Inches(0.55), Inches(0.55))
        stamp.fill.solid()
        stamp.fill.fore_color.rgb = C_RED
        stamp.line.fill.background()
        tf = stamp.text_frame
        tf.word_wrap = False
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = number_str
        p.alignment = PP_ALIGN.CENTER
        p.font.name = "Arial"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = C_WHITE

        # Header Text Box
        tbox = slide.shapes.add_textbox(Inches(1.55), Inches(0.5), Inches(10.8), Inches(1.1))
        tf_h = tbox.text_frame
        tf_h.word_wrap = True
        tf_h.margin_left = tf_h.margin_right = tf_h.margin_top = tf_h.margin_bottom = 0

        p_cat = tf_h.paragraphs[0]
        p_cat.text = category_str.upper()
        p_cat.font.name = "Arial"
        p_cat.font.size = Pt(9.5)
        p_cat.font.bold = True
        p_cat.font.color.rgb = C_RED

        p_title = tf_h.add_paragraph()
        p_title.text = title_str
        p_title.font.name = "Arial"
        p_title.font.size = Pt(20)
        p_title.font.bold = True
        p_title.font.color.rgb = C_SUMI

        if subtitle_str:
            p_sub = tf_h.add_paragraph()
            p_sub.text = subtitle_str
            p_sub.font.name = "Arial"
            p_sub.font.size = Pt(10.5)
            p_sub.font.color.rgb = C_SLATE

        # Hairline divider
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.85), Inches(1.7), Inches(11.633), Inches(0.012))
        line.fill.solid()
        line.fill.fore_color.rgb = C_BORDER
        line.line.fill.background()

    # =========================================================================
    # SLIDE 1: Cover Slide
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1)

    stamp1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(0.9), Inches(1.0), Inches(1.0))
    stamp1.fill.solid()
    stamp1.fill.fore_color.rgb = C_RED
    stamp1.line.fill.background()
    tf1 = stamp1.text_frame
    tf1.margin_left = tf1.margin_right = tf1.margin_top = tf1.margin_bottom = 0
    p = tf1.paragraphs[0]
    p.text = "TEAM\n07"
    p.alignment = PP_ALIGN.CENTER
    p.font.name = "Arial"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    tb_top = s1.shapes.add_textbox(Inches(2.25), Inches(0.9), Inches(9.5), Inches(0.9))
    tf_top = tb_top.text_frame
    tf_top.margin_left = tf_top.margin_right = tf_top.margin_top = tf_top.margin_bottom = 0
    p1 = tf_top.paragraphs[0]
    p1.text = "SNOWFLAKE CLOUD DATA WAREHOUSE  •  ENTERPRISE ANALYTICS"
    p1.font.name = "Arial"
    p1.font.size = Pt(10)
    p1.font.bold = True
    p1.font.color.rgb = C_RED

    p2 = tf_top.add_paragraph()
    p2.text = "End-to-End Hotel Reservation, Occupancy & Revenue Intelligence"
    p2.font.name = "Arial"
    p2.font.size = Pt(13)
    p2.font.bold = True
    p2.font.color.rgb = C_SUMI

    tb_main = s1.shapes.add_textbox(Inches(1.0), Inches(2.25), Inches(11.3), Inches(1.5))
    tf_main = tb_main.text_frame
    tf_main.word_wrap = True
    tf_main.margin_left = tf_main.margin_right = tf_main.margin_top = tf_main.margin_bottom = 0
    p_hero = tf_main.paragraphs[0]
    p_hero.text = "Hotel Reservation & Occupancy\nAnalytics System"
    p_hero.font.name = "Arial"
    p_hero.font.size = Pt(36)
    p_hero.font.bold = True
    p_hero.font.color.rgb = C_SUMI

    p_desc = tf_main.add_paragraph()
    p_desc.text = "Automated CSV Ingestion • 3-Tier Medallion Architecture • Date Integrity Quarantine • Serverless Tasks"
    p_desc.font.name = "Arial"
    p_desc.font.size = Pt(12)
    p_desc.font.color.rgb = C_SLATE

    # Team 07 Card (ONLY NAMES - NO WORK NAMES)
    team_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(4.1), Inches(11.333), Inches(1.3))
    team_card.fill.solid()
    team_card.fill.fore_color.rgb = C_WHITE
    team_card.line.color.rgb = C_RED
    team_card.line.width = Pt(1.5)
    
    tb_team = s1.shapes.add_textbox(Inches(1.3), Inches(4.25), Inches(10.7), Inches(1.0))
    tf_team = tb_team.text_frame
    tf_team.margin_left = tf_team.margin_right = tf_team.margin_top = tf_team.margin_bottom = 0
    pt1 = tf_team.paragraphs[0]
    pt1.text = "PROJECT BY TEAM 07"
    pt1.font.name = "Arial"
    pt1.font.size = Pt(10)
    pt1.font.bold = True
    pt1.font.color.rgb = C_RED

    pt2 = tf_team.add_paragraph()
    pt2.text = "Ashlesh   •   Varun   •   Sakshi   •   Barghavi   •   Akshitha"
    pt2.font.name = "Arial"
    pt2.font.size = Pt(18)
    pt2.font.bold = True
    pt2.font.color.rgb = C_SUMI

    specs = [
        ("WAREHOUSE", "HOTEL_WH (X-Small)"),
        ("DATABASE", "HOTEL_RESERVATION_DB"),
        ("SCHEDULER", "Daily 06:00 UTC (Task)"),
        ("PLATFORM", "Snowflake Enterprise")
    ]
    for idx, (label, val) in enumerate(specs):
        sx = 1.0 + (idx * 2.92)
        scard = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(sx), Inches(5.65), Inches(2.7), Inches(1.1))
        scard.fill.solid()
        scard.fill.fore_color.rgb = C_WHITE
        scard.line.color.rgb = C_BORDER
        scard.line.width = Pt(1.0)
        
        stb = s1.shapes.add_textbox(Inches(sx + 0.15), Inches(5.75), Inches(2.4), Inches(0.85))
        stf = stb.text_frame
        stf.margin_left = stf.margin_right = stf.margin_top = stf.margin_bottom = 0
        sp1 = stf.paragraphs[0]
        sp1.text = label
        sp1.font.name = "Arial"
        sp1.font.size = Pt(9)
        sp1.font.bold = True
        sp1.font.color.rgb = C_MUTED
        
        sp2 = stf.add_paragraph()
        sp2.text = val
        sp2.font.name = "Arial"
        sp2.font.size = Pt(11)
        sp2.font.bold = True
        sp2.font.color.rgb = C_SUMI

    # =========================================================================
    # SLIDE 2: Business Challenges
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "02", "PROBLEM STATEMENT", "Core Operational Challenges in Multi-Property Hospitality", "Fragmented reservation sources introduced corrupt dates, unmonitored cancellation exposure, and inaccurate occupancy metrics.")

    challenges = [
        ("01", "Anomalous Date Corruptions", "Check-out Dates Preceding Check-in", "Corrupt booking records where check-out precedes check-in or zero-night stays severely skew length-of-stay and inventory calculations.", C_RED),
        ("02", "Untracked Cancellation Leakage", "Revenue Loss & Sudden Spikes", "Sudden cancellation spikes through indirect channels caused unmonitored revenue leakage without clear visibility into refund volumes ($5,290+).", C_INDIGO),
        ("03", "Dynamic Occupancy Complexity", "Fluctuating Monthly Capacity", "Reconciling active room capacity across varying calendar days while excluding cancelled bookings required dynamic cross-join modeling.", C_MATCHA),
        ("04", "Manual Pipeline Vulnerability", "Spreadsheet Silos & Idle Compute", "Relying on end-of-month manual spreadsheet exports risked human error, lacked versioning, and lacked automated schedule health monitoring.", C_SLATE)
    ]

    for idx, (num, title, subtitle, desc, col) in enumerate(challenges):
        col_idx = idx % 2
        row_idx = idx // 2
        cx = 0.85 + (col_idx * 5.95)
        cy = 2.05 + (row_idx * 2.45)
        
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(cx), Inches(cy), Inches(5.68), Inches(2.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_WHITE
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1.0)
        
        bar = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(cx + 0.25), Inches(cy + 0.25), Inches(0.4), Inches(0.04))
        bar.fill.solid()
        bar.fill.fore_color.rgb = col
        bar.line.fill.background()

        tb = s2.shapes.add_textbox(Inches(cx + 0.25), Inches(cy + 0.38), Inches(5.18), Inches(1.65))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        
        p1 = tf.paragraphs[0]
        p1.text = f"{num}   {title}"
        p1.font.name = "Arial"
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = C_SUMI

        p2 = tf.add_paragraph()
        p2.text = subtitle.upper()
        p2.font.name = "Arial"
        p2.font.size = Pt(8.5)
        p2.font.bold = True
        p2.font.color.rgb = col

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.name = "Arial"
        p3.font.size = Pt(10.5)
        p3.font.color.rgb = C_SLATE

    # =========================================================================
    # SLIDE 3: Architecture
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "03", "DATA ARCHITECTURE", "3-Tier Medallion Data Engineering Architecture", "Structured separation of concerns: Raw landing, business validation, and executive analytics consumption.")

    layers = [
        ("RAW LAYER", "BRONZE INGESTION ZONE", [
            "• S3 External Stage (@HOTEL_S3_STAGE)",
            "• CSV File Format with header skip = 1",
            "• RAW_GUESTS: 20 guest profiles",
            "• RAW_ROOMS: 25 rooms across 4 properties",
            "• RAW_RESERVATIONS: 43 raw booking rows",
            "• RAW_PAYMENTS: 43 financial transactions",
            "• Preserves complete raw data lineage"
        ], C_INDIGO),
        ("CLEAN LAYER", "SILVER VALIDATION ZONE", [
            "• V_RESERVATION_DATE_VALIDATION",
            "• Automatically isolates corrupt bookings",
            "• CLEAN_RESERVATIONS: 40 validated records",
            "• V_CANCELLED_RESERVATIONS tracking",
            "• Identifies 8 cancellations ($5,290 refunded)",
            "• Enriched guest profile linkages",
            "• Strict quality gate before production"
        ], C_RED),
        ("ANALYTICS LAYER", "GOLD CONSUMPTION ZONE", [
            "• FACT_RESERVATION_ANALYTICS wide fact",
            "• V_MONTHLY_OCCUPANCY: dynamic monthly %",
            "• V_REVENUE_BY_HOTEL: property-level yield",
            "• V_REVENUE_BY_ROOM_TYPE: ADR metrics",
            "• DAILY_RESERVATION_SUMMARY aggregation",
            "• Automated Daily Task (CRON 6 AM UTC)",
            "• BI-ready views for executive dashboards"
        ], C_MATCHA)
    ]

    for idx, (title, subtitle, bullets, col) in enumerate(layers):
        lx = 0.85 + (idx * 3.98)
        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(lx), Inches(2.05), Inches(3.7), Inches(4.85))
        card.fill.solid()
        card.fill.fore_color.rgb = C_WHITE
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1.0)
        
        bar = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(lx + 0.3), Inches(2.3), Inches(0.5), Inches(0.04))
        bar.fill.solid()
        bar.fill.fore_color.rgb = col
        bar.line.fill.background()

        tb = s3.shapes.add_textbox(Inches(lx + 0.3), Inches(2.45), Inches(3.1), Inches(4.3))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.name = "Arial"
        p1.font.size = Pt(14)
        p1.font.bold = True
        p1.font.color.rgb = C_SUMI

        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.name = "Arial"
        p2.font.size = Pt(8.5)
        p2.font.bold = True
        p2.font.color.rgb = col

        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = b
            pb.font.name = "Arial"
            pb.font.size = Pt(10.5)
            pb.font.color.rgb = C_SUMI

    # =========================================================================
    # SLIDE 4: Data Quality & Date Validation Logic (PERFECT FIT)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "04", "DATA QUALITY & INTEGRITY", "Reservation Date Validation Logic & Quarantine", "Automated SQL rules quarantine negative durations and zero-night stays before data reaches analytics.")

    card_l = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.85), Inches(2.05), Inches(5.68), Inches(4.85))
    card_l.fill.solid()
    card_l.fill.fore_color.rgb = C_WHITE
    card_l.line.color.rgb = C_BORDER
    card_l.line.width = Pt(1.0)

    tb_l = s4.shapes.add_textbox(Inches(1.1), Inches(2.2), Inches(5.18), Inches(4.5))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = tf_l.margin_bottom = 0

    p_lt = tf_l.paragraphs[0]
    p_lt.text = "SQL Automated Validation Rules"
    p_lt.font.name = "Arial"
    p_lt.font.size = Pt(13)
    p_lt.font.bold = True
    p_lt.font.color.rgb = C_SUMI

    p_code = tf_l.add_paragraph()
    p_code.text = """CASE
  WHEN check_in_date IS NULL 
    THEN 'INVALID - NULL dates'

  WHEN check_out_date < check_in_date
    THEN 'INVALID - Checkout before Checkin'

  WHEN check_out_date = check_in_date
    THEN 'INVALID - Zero night stay'

  WHEN DATEDIFF('day', check_in, check_out) > 365
    THEN 'WARNING - Stay exceeds 365 days'

  ELSE 'VALID'
END AS date_validation_status;"""
    p_code.font.name = "Consolas"
    p_code.font.size = Pt(9.5)
    p_code.font.color.rgb = C_INDIGO

    p_ln = tf_l.add_paragraph()
    p_ln.text = "\nEnforcement: Records evaluated as 'VALID' load into CLEAN_RESERVATIONS (40 rows). Corrupt records are quarantined in view V_RESERVATION_DATE_VALIDATION."
    p_ln.font.name = "Arial"
    p_ln.font.size = Pt(9.5)
    p_ln.font.color.rgb = C_SLATE

    anomalies_s4 = [
        ("RES041 • Grand Palace Hotel", "IN: 2024-11-15  |  OUT: 2024-11-10  (-5 Days)", "Check-out occurs 5 days before check-in. Flagged immediately and excluded from production clean tables."),
        ("RES042 • Seaside Resort", "IN: 2024-12-25  |  OUT: 2024-12-20  (-5 Days)", "OTA booking injection with inverted calendar sequence. Quarantined to prevent skewing room availability metrics."),
        ("RES043 • Mountain Lodge", "IN: 2024-10-10  |  OUT: 2024-10-10  (0 Nights)", "Same-day booking and departure without overnight stay. Excluded from overnight occupancy percentage calculations.")
    ]

    for idx, (head, subh, exp) in enumerate(anomalies_s4):
        ay = 2.05 + (idx * 1.66)
        acard = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(ay), Inches(5.68), Inches(1.52))
        acard.fill.solid()
        acard.fill.fore_color.rgb = C_WHITE
        acard.line.color.rgb = C_BORDER
        acard.line.width = Pt(1.0)
        
        atb = s4.shapes.add_textbox(Inches(7.05), Inches(ay + 0.15), Inches(5.18), Inches(1.22))
        atf = atb.text_frame
        atf.word_wrap = True
        atf.margin_left = atf.margin_right = atf.margin_top = atf.margin_bottom = 0
        
        ap1 = atf.paragraphs[0]
        ap1.text = head
        ap1.font.name = "Arial"
        ap1.font.size = Pt(11)
        ap1.font.bold = True
        ap1.font.color.rgb = C_RED

        ap2 = atf.add_paragraph()
        ap2.text = subh
        ap2.font.name = "Arial"
        ap2.font.size = Pt(9)
        ap2.font.bold = True
        ap2.font.color.rgb = C_SUMI

        ap3 = atf.add_paragraph()
        ap3.text = exp
        ap3.font.name = "Arial"
        ap3.font.size = Pt(9.5)
        ap3.font.color.rgb = C_SLATE

    # =========================================================================
    # SLIDE 5: Metrics & Commercial Impact (CLEAN FIT)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "05", "EXECUTIVE METRICS", "Key Analytical Findings & Financial Performance", "Verified metrics computed from FACT_RESERVATION_ANALYTICS across 4 hotel properties.")

    kpis = [
        ("40", "Valid Bookings", "3 corrupt bookings filtered out", C_INDIGO),
        ("$46,880", "Net Realized Revenue", "Gross revenue less $5,290 refunds", C_MATCHA),
        ("20.0%", "Cancellation Rate", "8 cancelled bookings tracked", C_RED),
        ("58.1%", "Peak Occupancy Rate", "Seaside Resort led October demand", C_SUMI)
    ]

    for idx, (val, title, note, col) in enumerate(kpis):
        kx = 0.85 + (idx * 2.98)
        card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(kx), Inches(2.05), Inches(2.75), Inches(1.5))
        card.fill.solid()
        card.fill.fore_color.rgb = C_WHITE
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1.0)
        
        tb = s5.shapes.add_textbox(Inches(kx + 0.15), Inches(2.18), Inches(2.45), Inches(1.25))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        
        p = tf.paragraphs[0]
        p.text = val
        p.font.name = "Arial"
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.name = "Arial"
        p2.font.size = Pt(10)
        p2.font.bold = True
        p2.font.color.rgb = C_SUMI

        p3 = tf.add_paragraph()
        p3.text = note
        p3.font.name = "Arial"
        p3.font.size = Pt(8.5)
        p3.font.color.rgb = C_MUTED

    bot_cards = [
        (0.85, "Cancellation Exposure by Channel", [
            ("Online Travel Agencies (OTA):", "38.4% cancel rate ($2,690 refund impact)."),
            ("Direct Hotel Website:", "14.3% cancel rate (highest retention & profit margin)."),
            ("Phone Reservations:", "18.2% cancel rate (corporate account bookings)."),
            ("Walk-In Guests:", "0.0% cancel rate (guaranteed realized revenue).")
        ], C_RED),
        (6.8, "Room Tier & Loyalty Performance", [
            ("Suite & Presidential Tiers:", "Generate 48% of gross realized revenue."),
            ("Platinum Loyalty Members:", "Average 3.2x higher ADR than standard guests."),
            ("Seaside Resort:", "Longest average length of stay (4.2 nights)."),
            ("City Central Inn:", "Highest room inventory turnover rate.")
        ], C_INDIGO)
    ]

    for bx, btitle, items, bcol in bot_cards:
        bcard = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(bx), Inches(3.75), Inches(5.68), Inches(3.15))
        bcard.fill.solid()
        bcard.fill.fore_color.rgb = C_WHITE
        bcard.line.color.rgb = C_BORDER
        bcard.line.width = Pt(1.0)
        
        bar = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(bx + 0.25), Inches(3.95), Inches(0.4), Inches(0.04))
        bar.fill.solid()
        bar.fill.fore_color.rgb = bcol
        bar.line.fill.background()

        tb = s5.shapes.add_textbox(Inches(bx + 0.25), Inches(4.08), Inches(5.18), Inches(2.7))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = btitle
        p.font.name = "Arial"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = C_SUMI

        for label_i, text_i in items:
            pi = tf.add_paragraph()
            pi.text = f"• {label_i} {text_i}"
            pi.font.name = "Arial"
            pi.font.size = Pt(9.5)
            pi.font.color.rgb = C_SLATE

    # =========================================================================
    # SLIDE 6: Serverless Scheduled Task (CLEAN GRID)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "06", "SERVERLESS AUTOMATION", "Scheduled Task Definition & Operational Health", "Serverless aggregation task running daily at 6 AM UTC with real-time health verification via Task History.")

    c_tl = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.85), Inches(2.05), Inches(5.68), Inches(4.85))
    c_tl.fill.solid()
    c_tl.fill.fore_color.rgb = C_WHITE
    c_tl.line.color.rgb = C_BORDER
    c_tl.line.width = Pt(1.0)

    tb_tl = s6.shapes.add_textbox(Inches(1.1), Inches(2.25), Inches(5.18), Inches(4.45))
    tf_tl = tb_tl.text_frame
    tf_tl.word_wrap = True
    tf_tl.margin_left = tf_tl.margin_right = tf_tl.margin_top = tf_tl.margin_bottom = 0

    p_tt = tf_tl.paragraphs[0]
    p_tt.text = "Snowflake Scheduled Task Definition"
    p_tt.font.name = "Arial"
    p_tt.font.size = Pt(13)
    p_tt.font.bold = True
    p_tt.font.color.rgb = C_SUMI

    p_task = tf_tl.add_paragraph()
    p_task.text = """CREATE OR REPLACE TASK 
  TASK_DAILY_RESERVATION_AGGREGATION
  WAREHOUSE = HOTEL_WH
  SCHEDULE  = 'USING CRON 0 6 * * * UTC'
AS
INSERT INTO DAILY_RESERVATION_SUMMARY
(
  summary_date, hotel_name, room_type,
  total_reservations, net_revenue,
  occupancy_pct, top_booking_source...
)
SELECT ... FROM FACT_RESERVATION_ANALYTICS;

ALTER TASK ... RESUME;"""
    p_task.font.name = "Consolas"
    p_task.font.size = Pt(9)
    p_task.font.color.rgb = C_INDIGO

    p_tn = tf_tl.add_paragraph()
    p_tn.text = "\nAutonomous Pipeline Execution:\nRuns daily without external orchestrators (Airflow/dbt not required). Computes daily aggregates into DAILY_RESERVATION_SUMMARY table directly in Snowflake."
    p_tn.font.name = "Arial"
    p_tn.font.size = Pt(9.5)
    p_tn.font.color.rgb = C_SLATE

    c_tr = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.05), Inches(5.68), Inches(4.85))
    c_tr.fill.solid()
    c_tr.fill.fore_color.rgb = C_WHITE
    c_tr.line.color.rgb = C_BORDER
    c_tr.line.width = Pt(1.0)

    tb_tr = s6.shapes.add_textbox(Inches(7.05), Inches(2.25), Inches(5.18), Inches(4.45))
    tf_tr = tb_tr.text_frame
    tf_tr.word_wrap = True
    tf_tr.margin_left = tf_tr.margin_right = tf_tr.margin_top = tf_tr.margin_bottom = 0

    p_rt = tf_tr.paragraphs[0]
    p_rt.text = "Task Execution History (TASK_HISTORY)"
    p_rt.font.name = "Arial"
    p_rt.font.size = Pt(13)
    p_rt.font.bold = True
    p_rt.font.color.rgb = C_MATCHA

    task_stats = [
        ("Execution State", "SUCCEEDED (Verified live in Snowflake worksheet)"),
        ("Run Duration", "3.07 seconds (Low compute latency)"),
        ("Schedule Cadence", "CRON 0 6 * * * UTC (Daily at 6 AM)"),
        ("Compute Warehouse", "HOTEL_WH (X-Small) with 120s Auto-Suspend"),
        ("Zero Idle Spend", "Warehouse shuts down immediately after task finishes")
    ]

    for label_s, val_s in task_stats:
        ps = tf_tr.add_paragraph()
        ps.text = f"• {label_s}: {val_s}"
        ps.font.name = "Arial"
        ps.font.size = Pt(9.5)
        ps.font.color.rgb = C_SLATE

    # =========================================================================
    # SLIDE 7: Business Value & ROI
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "07", "BUSINESS VALUE & ROI", "Strategic Impact & Production Deliverables", "Clean, high-precision analytics delivered through Snowflake modern cloud data engineering best practices.")

    points = [
        ("Data Trust & Integrity", "Automated Validation", "Quarantined corrupt check-out dates and zero-night stays, ensuring 100% executive reporting accuracy.", C_INDIGO),
        ("Revenue Protection", "Cancellation Transparency", "Exposed $2,690 in OTA cancellation refunds, providing actionable data for policy adjustments.", C_RED),
        ("Dynamic Yield Optimization", "Capacity Intelligence", "Accurate monthly occupancy rates empower revenue management to optimize room rates dynamically.", C_MATCHA),
        ("Zero Idle Compute Cost", "Optimized Warehouse", "Task executes in 3 seconds on an X-Small warehouse with 120s auto-suspend, minimizing infrastructure spend.", C_SUMI)
    ]

    for idx, (title, subtitle, desc, col) in enumerate(points):
        tx = 0.85 + (idx * 2.98)
        card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(tx), Inches(2.05), Inches(2.75), Inches(3.75))
        card.fill.solid()
        card.fill.fore_color.rgb = C_WHITE
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1.0)
        
        cbar = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(tx + 0.2), Inches(2.25), Inches(0.4), Inches(0.04))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = col
        cbar.line.fill.background()

        tb = s7.shapes.add_textbox(Inches(tx + 0.2), Inches(2.38), Inches(2.35), Inches(3.3))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Arial"
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = C_SUMI

        p_sub = tf.add_paragraph()
        p_sub.text = subtitle.upper()
        p_sub.font.name = "Arial"
        p_sub.font.size = Pt(8.5)
        p_sub.font.bold = True
        p_sub.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = "\n" + desc
        p2.font.name = "Arial"
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_SLATE

    foot_card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.85), Inches(6.05), Inches(11.633), Inches(0.75))
    foot_card.fill.solid()
    foot_card.fill.fore_color.rgb = C_WHITE
    foot_card.line.color.rgb = C_BORDER
    foot_card.line.width = Pt(1.0)

    tb_foot = s7.shapes.add_textbox(Inches(1.1), Inches(6.15), Inches(11.1), Inches(0.55))
    tf_foot = tb_foot.text_frame
    tf_foot.margin_left = tf_foot.margin_right = tf_foot.margin_top = tf_foot.margin_bottom = 0
    p_foot = tf_foot.paragraphs[0]
    p_foot.text = "GitHub: https://github.com/ashlesh0805/snowflake-hotel-reservation-analytics   •   Project by Team 07"
    p_foot.font.name = "Arial"
    p_foot.font.size = Pt(10.5)
    p_foot.font.bold = True
    p_foot.font.color.rgb = C_RED

    # =========================================================================
    # SLIDE 8: Thank You & Team 07 (ONLY NAMES - NO WORK NAMES!)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8)

    stamp8 = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(0.9), Inches(1.0), Inches(1.0))
    stamp8.fill.solid()
    stamp8.fill.fore_color.rgb = C_RED
    stamp8.line.fill.background()
    tf8 = stamp8.text_frame
    tf8.margin_left = tf8.margin_right = tf8.margin_top = tf8.margin_bottom = 0
    p = tf8.paragraphs[0]
    p.text = "TEAM\n07"
    p.alignment = PP_ALIGN.CENTER
    p.font.name = "Arial"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    tb_t8 = s8.shapes.add_textbox(Inches(2.25), Inches(0.9), Inches(9.5), Inches(0.9))
    tf_t8 = tb_t8.text_frame
    tf_t8.margin_left = tf_t8.margin_right = tf_t8.margin_top = tf_t8.margin_bottom = 0
    p1 = tf_t8.paragraphs[0]
    p1.text = "PROJECT CONCLUSION  •  QUESTIONS & DISCUSSION"
    p1.font.name = "Arial"
    p1.font.size = Pt(10)
    p1.font.bold = True
    p1.font.color.rgb = C_RED

    p2 = tf_t8.add_paragraph()
    p2.text = "Thank You"
    p2.font.name = "Arial"
    p2.font.size = Pt(32)
    p2.font.bold = True
    p2.font.color.rgb = C_SUMI

    line8 = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(2.2), Inches(11.333), Inches(0.012))
    line8.fill.solid()
    line8.fill.fore_color.rgb = C_BORDER
    line8.line.fill.background()

    tb_head8 = s8.shapes.add_textbox(Inches(1.0), Inches(2.45), Inches(11.333), Inches(0.4))
    tf_h8 = tb_head8.text_frame
    tf_h8.margin_left = tf_h8.margin_right = tf_h8.margin_top = tf_h8.margin_bottom = 0
    ph8 = tf_h8.paragraphs[0]
    ph8.text = "PRESENTED BY TEAM 07"
    ph8.font.name = "Arial"
    ph8.font.size = Pt(11)
    ph8.font.bold = True
    ph8.font.color.rgb = C_SUMI

    # 5 Big Beautiful Name Cards (ONLY NAMES - NO WORK NAMES!)
    names = ["Ashlesh", "Varun", "Sakshi", "Barghavi", "Akshitha"]
    
    for idx, name_i in enumerate(names):
        nx = 1.0 + (idx * 2.32)
        ncard = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(nx), Inches(2.95), Inches(2.15), Inches(2.2))
        ncard.fill.solid()
        ncard.fill.fore_color.rgb = C_WHITE
        ncard.line.color.rgb = C_BORDER
        ncard.line.width = Pt(1.2)
        
        nbar = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(nx + 0.3), Inches(3.2), Inches(0.4), Inches(0.04))
        nbar.fill.solid()
        nbar.fill.fore_color.rgb = C_RED if idx == 0 else C_SUMI
        nbar.line.fill.background()

        ntb = s8.shapes.add_textbox(Inches(nx + 0.15), Inches(3.6), Inches(1.85), Inches(1.2))
        ntf = ntb.text_frame
        ntf.margin_left = ntf.margin_right = ntf.margin_top = ntf.margin_bottom = 0
        
        pn = ntf.paragraphs[0]
        pn.text = name_i
        pn.alignment = PP_ALIGN.CENTER
        pn.font.name = "Arial"
        pn.font.size = Pt(20)
        pn.font.bold = True
        pn.font.color.rgb = C_SUMI

    bcard8 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(5.45), Inches(11.333), Inches(1.3))
    bcard8.fill.solid()
    bcard8.fill.fore_color.rgb = C_WHITE
    bcard8.line.color.rgb = C_BORDER
    bcard8.line.width = Pt(1.0)

    tb_b8 = s8.shapes.add_textbox(Inches(1.3), Inches(5.6), Inches(10.7), Inches(1.0))
    tf_b8 = tb_b8.text_frame
    tf_b8.margin_left = tf_b8.margin_right = tf_b8.margin_top = tf_b8.margin_bottom = 0
    
    pb1 = tf_b8.paragraphs[0]
    pb1.text = "PROJECT REPOSITORY & CODEBASE"
    pb1.font.name = "Arial"
    pb1.font.size = Pt(9.5)
    pb1.font.bold = True
    pb1.font.color.rgb = C_RED

    pb2 = tf_b8.add_paragraph()
    pb2.text = "https://github.com/ashlesh0805/snowflake-hotel-reservation-analytics"
    pb2.font.name = "Arial"
    pb2.font.size = Pt(13)
    pb2.font.bold = True
    pb2.font.color.rgb = C_SUMI

    pb3 = tf_b8.add_paragraph()
    pb3.text = "Includes full SQL pipeline scripts, CSV datasets, date validation tests, task history logs, and screenshots."
    pb3.font.name = "Arial"
    pb3.font.size = Pt(9.5)
    pb3.font.color.rgb = C_SLATE

    save_targets = [
        r"C:\Users\G ASHLESH\Downloads\Hotel_Reservation_Analytics_Team07_Japanese_Style.pptx",
        r"C:\Users\G ASHLESH\Downloads\Hotel_Reservation_Analytics_Zen_Minimalist.pptx",
        r"C:\Users\G ASHLESH\Downloads\snowflake_screenshots\Hotel_Reservation_Analytics_Japanese_Style.pptx",
        r"C:\Users\G ASHLESH\Downloads\Hotel_Reservation_Analytics_Japanese_Style.pptx",
        r"c:\Users\G ASHLESH\OneDrive\Desktop\snowflake\Hotel_Reservation_Analytics_Team07_Japanese_Style.pptx",
        r"c:\Users\G ASHLESH\OneDrive\Desktop\snowflake\Hotel_Reservation_Analytics_Zen_Minimalist.pptx",
        r"c:\Users\G ASHLESH\OneDrive\Desktop\snowflake\Hotel_Reservation_Analytics_Japanese_Style.pptx"
    ]

    print("Building and saving clean presentation:")
    for target in save_targets:
        try:
            prs.save(target)
            print(" [OK] Saved:", target)
        except PermissionError:
            print(" [LOCKED]:", target)

if __name__ == "__main__":
    build_perfect_presentation()
