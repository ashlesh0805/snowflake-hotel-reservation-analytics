import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Modern Clean Palette
    COLOR_BG_WHITE = RGBColor(255, 255, 255)
    COLOR_CARD_BG = RGBColor(248, 250, 252) # slate-50
    COLOR_CARD_BORDER = RGBColor(226, 232, 240) # slate-200
    COLOR_TEXT_PRIMARY = RGBColor(15, 23, 42) # slate-900
    COLOR_TEXT_SECONDARY = RGBColor(71, 85, 105) # slate-600
    COLOR_TEXT_MUTED = RGBColor(100, 116, 139) # slate-500
    COLOR_ACCENT_BLUE = RGBColor(37, 99, 235) # blue-600
    COLOR_ACCENT_TEAL = RGBColor(13, 148, 136) # teal-600
    COLOR_ACCENT_INDIGO = RGBColor(79, 70, 229) # indigo-600
    COLOR_SUCCESS = RGBColor(22, 163, 74) # green-600
    COLOR_DANGER = RGBColor(220, 38, 38) # red-600

    def add_header(slide, tag_text, title_text, subtitle_text):
        # Category Tag pill
        tag_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.55), Inches(2.2), Inches(0.38))
        tag_box.fill.solid()
        tag_box.fill.fore_color.rgb = RGBColor(239, 246, 255)
        tag_box.line.color.rgb = RGBColor(191, 219, 254)
        tag_box.line.width = Pt(1)
        tf = tag_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = tag_text.upper()
        p.alignment = PP_ALIGN.CENTER
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_ACCENT_BLUE

        # Title
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.95), Inches(11.5), Inches(0.75))
        tf_t = t_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.name = "Arial"
        p_t.font.size = Pt(24)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_PRIMARY

        # Subtitle
        if subtitle_text:
            s_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.58), Inches(11.5), Inches(0.5))
            tf_s = s_box.text_frame
            tf_s.word_wrap = True
            p_s = tf_s.paragraphs[0]
            p_s.text = subtitle_text
            p_s.font.name = "Arial"
            p_s.font.size = Pt(12)
            p_s.font.color.rgb = COLOR_TEXT_SECONDARY

    def add_card(slide, left, top, width, height, bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)
        return card

    # ==========================================
    # SLIDE 1: Title Slide (Cover)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    
    # Hero Card background
    hero = add_card(s1, 0.8, 0.8, 11.733, 5.9, RGBColor(255, 255, 255), RGBColor(226, 232, 240))
    
    # Decorative subtle accent line
    line = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.4), Inches(1.4), Inches(1.2), Inches(0.08))
    line.fill.solid()
    line.fill.fore_color.rgb = COLOR_ACCENT_BLUE
    line.line.fill.background()

    # Title Tag
    tag1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.4), Inches(1.7), Inches(3.2), Inches(0.42))
    tag1.fill.solid()
    tag1.fill.fore_color.rgb = RGBColor(238, 242, 255)
    tag1.line.color.rgb = RGBColor(199, 210, 254)
    tf1 = tag1.text_frame
    p1 = tf1.paragraphs[0]
    p1.text = "SNOWFLAKE ENTERPRISE ANALYTICS"
    p1.alignment = PP_ALIGN.CENTER
    p1.font.name = "Arial"
    p1.font.size = Pt(10)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_ACCENT_INDIGO

    # Main Heading
    h_box = s1.shapes.add_textbox(Inches(1.35), Inches(2.25), Inches(10.5), Inches(1.8))
    tf_h = h_box.text_frame
    tf_h.word_wrap = True
    p_h = tf_h.paragraphs[0]
    p_h.text = "Hotel Reservation & Occupancy\nAnalytics System"
    p_h.font.name = "Arial"
    p_h.font.size = Pt(36)
    p_h.font.bold = True
    p_h.font.color.rgb = COLOR_TEXT_PRIMARY

    # Sub-heading
    sub_box = s1.shapes.add_textbox(Inches(1.4), Inches(4.1), Inches(10.0), Inches(0.9))
    tf_sub = sub_box.text_frame
    tf_sub.word_wrap = True
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = "Automated Cloud Ingestion • Date Quality Validation • Dynamic Occupancy • Automated Daily Tasks"
    p_sub.font.name = "Arial"
    p_sub.font.size = Pt(13)
    p_sub.font.color.rgb = COLOR_TEXT_SECONDARY

    # Metadata badges at bottom
    badges = [
        ("Platform", "Snowflake Data Cloud", COLOR_ACCENT_BLUE),
        ("Storage", "AWS S3 External Stage", COLOR_ACCENT_TEAL),
        ("Automation", "Serverless Snowflake Tasks", COLOR_ACCENT_INDIGO),
        ("Presenter", "Ashlesh Gurram", COLOR_TEXT_PRIMARY)
    ]
    for idx, (b_title, b_val, b_col) in enumerate(badges):
        bx = 1.4 + (idx * 2.65)
        b_card = add_card(s1, bx, 5.2, 2.45, 1.1, RGBColor(248, 250, 252), RGBColor(226, 232, 240))
        tb = s1.shapes.add_textbox(Inches(bx + 0.1), Inches(5.3), Inches(2.25), Inches(0.9))
        ptf = tb.text_frame
        p_l = ptf.paragraphs[0]
        p_l.text = b_title.upper()
        p_l.font.name = "Arial"
        p_l.font.size = Pt(9)
        p_l.font.bold = True
        p_l.font.color.rgb = COLOR_TEXT_MUTED
        
        p_v = ptf.add_paragraph()
        p_v.text = b_val
        p_v.font.name = "Arial"
        p_v.font.size = Pt(11)
        p_v.font.bold = True
        p_v.font.color.rgb = b_col

    # ==========================================
    # SLIDE 2: Business Scenario & Core Challenges
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Business Case", "Hotel Operations Scenario & Problem Statement", "A multi-property hotel chain needed a reliable, modern data solution to replace fragmented booking reports.")

    challenges = [
        ("1. Unvalidated Booking Dates", "Guests and partner channels often supply anomalous dates (check-out before check-in or zero-night stays) that distort revenue and length-of-stay KPIs.", COLOR_DANGER),
        ("2. Untracked Cancellation Losses", "Cancellations from OTAs (Online Travel Agencies) and phone bookings led to silent revenue leakage without clear visibility into refund exposure.", COLOR_ACCENT_BLUE),
        ("3. Complex Occupancy Modeling", "Calculating occupancy requires real-time reconciliation of active rooms vs. booked room-nights per property across variable calendar months.", COLOR_ACCENT_TEAL),
        ("4. Manual & Inconsistent Rollups", "Executives relied on delayed end-of-month manual spreadsheet reporting with zero automated pipeline monitoring or alerting.", COLOR_ACCENT_INDIGO)
    ]

    for idx, (ch_title, ch_desc, ch_col) in enumerate(challenges):
        col = idx % 2
        row = idx // 2
        cx = 0.8 + (col * 5.95)
        cy = 2.2 + (row * 2.35)
        card = add_card(s2, cx, cy, 5.75, 2.15, RGBColor(255, 255, 255), RGBColor(226, 232, 240))
        
        # Color bar on top of card
        cbar = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(cx + 0.2), Inches(cy + 0.15), Inches(0.5), Inches(0.06))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = ch_col
        cbar.line.fill.background()

        tb = s2.shapes.add_textbox(Inches(cx + 0.2), Inches(cy + 0.3), Inches(5.35), Inches(1.6))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = ch_title
        p1.font.name = "Arial"
        p1.font.size = Pt(14)
        p1.font.bold = True
        p1.font.color.rgb = ch_col

        p2 = tf.add_paragraph()
        p2.text = ch_desc
        p2.font.name = "Arial"
        p2.font.size = Pt(11)
        p2.font.color.rgb = COLOR_TEXT_SECONDARY

    # ==========================================
    # SLIDE 3: Architecture & Medallion Design
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "System Design", "Layered Data Architecture (Medallion Pattern)", "Structured into 3 schemas: Raw (Landing), Clean (Validated), and Analytics (Consumption).")

    layers = [
        ("RAW LAYER (Bronze)", "Landing Zone", "• Ingests CSV files from Amazon S3\n• Uses external stage & CSV_FORMAT\n• RAW_GUESTS (20 rows)\n• RAW_ROOMS (25 rooms)\n• RAW_RESERVATIONS (43 rows)\n• RAW_PAYMENTS (43 transactions)", RGBColor(239, 246, 255), COLOR_ACCENT_BLUE),
        ("CLEAN LAYER (Silver)", "Business Validation", "• Eliminates invalid dates & nulls\n• V_RESERVATION_DATE_VALIDATION\n• Flags RES041, RES042, RES043\n• CLEAN_RESERVATIONS (40 rows)\n• V_CANCELLED_RESERVATIONS\n• Tracks 8 cancellations & refunds", RGBColor(240, 253, 250), COLOR_ACCENT_TEAL),
        ("ANALYTICS LAYER (Gold)", "Executive Metrics", "• FACT_RESERVATION_ANALYTICS\n• V_MONTHLY_OCCUPANCY (%)\n• V_REVENUE_BY_HOTEL (Net)\n• V_REVENUE_BY_ROOM_TYPE (ADR)\n• DAILY_RESERVATION_SUMMARY\n• Automated Daily Task (CRON)", RGBColor(238, 242, 255), COLOR_ACCENT_INDIGO)
    ]

    for idx, (l_title, l_sub, l_desc, l_bg, l_acc) in enumerate(layers):
        lx = 0.8 + (idx * 3.95)
        card = add_card(s3, lx, 2.2, 3.8, 4.6, l_bg, RGBColor(203, 213, 225))
        
        tb = s3.shapes.add_textbox(Inches(lx + 0.2), Inches(2.4), Inches(3.4), Inches(4.2))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = l_title
        p.font.name = "Arial"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = l_acc
        
        p_sub = tf.add_paragraph()
        p_sub.text = l_sub
        p_sub.font.name = "Arial"
        p_sub.font.size = Pt(10.5)
        p_sub.font.italic = True
        p_sub.font.color.rgb = COLOR_TEXT_MUTED

        p_desc = tf.add_paragraph()
        p_desc.text = "\n" + l_desc
        p_desc.font.name = "Arial"
        p_desc.font.size = Pt(11)
        p_desc.font.color.rgb = COLOR_TEXT_PRIMARY

    # ==========================================
    # SLIDE 4: Data Engineering & Date Validation
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Data Quality", "Automated Reservation Date Integrity Checks", "Catching corrupt check-in/check-out dates before they pollute financial reporting.")

    # Left Card: Validation Logic Code
    card_l = add_card(s4, 0.8, 2.2, 5.8, 4.6, RGBColor(255, 255, 255), RGBColor(226, 232, 240))
    tb_l = s4.shapes.add_textbox(Inches(1.0), Inches(2.4), Inches(5.4), Inches(4.2))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    p_lt = tf_l.paragraphs[0]
    p_lt.text = "Validation SQL Rules"
    p_lt.font.name = "Arial"
    p_lt.font.size = Pt(14)
    p_lt.font.bold = True
    p_lt.font.color.rgb = COLOR_TEXT_PRIMARY

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
    p_code.font.size = Pt(10)
    p_code.font.color.rgb = COLOR_ACCENT_BLUE

    # Right Card: Detected Edge Cases
    card_r = add_card(s4, 6.8, 2.2, 5.733, 4.6, RGBColor(255, 255, 255), RGBColor(226, 232, 240))
    tb_r = s4.shapes.add_textbox(Inches(7.0), Inches(2.4), Inches(5.33), Inches(4.2))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p_rt = tf_r.paragraphs[0]
    p_rt.text = "Identified Anomalies Filtered Out"
    p_rt.font.name = "Arial"
    p_rt.font.size = Pt(14)
    p_rt.font.bold = True
    p_rt.font.color.rgb = COLOR_DANGER

    anomalies = [
        ("RES041 (Grand Palace)", "Check-in: Nov 15 | Check-out: Nov 10", "Checkout was 5 days prior to check-in. Flagged and excluded from clean production tables."),
        ("RES042 (Seaside Resort)", "Check-in: Dec 25 | Check-out: Dec 20", "Checkout was 5 days prior to check-in. Excluded from room availability calculation."),
        ("RES043 (Mountain Lodge)", "Check-in: Oct 10 | Check-out: Oct 10", "Zero-night same-day duration. Excluded from overnight occupancy metrics.")
    ]
    for aid, adates, anote in anomalies:
        pa = tf_r.add_paragraph()
        pa.text = f"\n• {aid}\n   {adates}\n   {anote}"
        pa.font.name = "Arial"
        pa.font.size = Pt(10.5)
        pa.font.color.rgb = COLOR_TEXT_SECONDARY

    # ==========================================
    # SLIDE 5: Key Business Metrics & Analytics
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Executive Analytics", "Revenue, Occupancy & Cancellation Metrics", "Results calculated from verified data in the FACT_RESERVATION_ANALYTICS model.")

    kpis = [
        ("40", "Valid Reservations", "Cleaned from 43 raw records", COLOR_ACCENT_BLUE),
        ("$46,880", "Total Net Revenue", "Completed payments minus refunds", COLOR_SUCCESS),
        ("8", "Cancelled Bookings", "20% drop-off rate ($5,290 refund volume)", COLOR_DANGER),
        ("58.3%", "Peak Occupancy", "Seaside Resort leads autumn occupancy", COLOR_ACCENT_TEAL)
    ]

    for idx, (val, title, note, col) in enumerate(kpis):
        kx = 0.8 + (idx * 2.95)
        card = add_card(s5, kx, 2.2, 2.8, 1.8, RGBColor(255, 255, 255), RGBColor(226, 232, 240))
        tb = s5.shapes.add_textbox(Inches(kx + 0.15), Inches(2.3), Inches(2.5), Inches(1.6))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = val
        p.font.name = "Arial"
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.name = "Arial"
        p2.font.size = Pt(11)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_TEXT_PRIMARY

        p3 = tf.add_paragraph()
        p3.text = note
        p3.font.name = "Arial"
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = COLOR_TEXT_MUTED

    # Lower comparison cards
    c_left = add_card(s5, 0.8, 4.25, 5.8, 2.55, RGBColor(248, 250, 252), RGBColor(226, 232, 240))
    tb_cl = s5.shapes.add_textbox(Inches(1.0), Inches(4.35), Inches(5.4), Inches(2.3))
    tf_cl = tb_cl.text_frame
    tf_cl.word_wrap = True
    p = tf_cl.paragraphs[0]
    p.text = "Booking Channels & Drop-off Rates"
    p.font.name = "Arial"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEXT_PRIMARY

    p_lines = tf_cl.add_paragraph()
    p_lines.text = "• Online Travel Agencies (OTA): 38% cancellation rate (highest)\n• Direct Website: 14% cancellation rate (highest conversion & margin)\n• Phone Reservations: 18% cancellation rate\n• Walk-in Bookings: 0% cancellations (immediate revenue guarantee)"
    p_lines.font.name = "Arial"
    p_lines.font.size = Pt(10.5)
    p_lines.font.color.rgb = COLOR_TEXT_SECONDARY

    c_right = add_card(s5, 6.8, 4.25, 5.733, 2.55, RGBColor(248, 250, 252), RGBColor(226, 232, 240))
    tb_cr = s5.shapes.add_textbox(Inches(7.0), Inches(4.35), Inches(5.33), Inches(2.3))
    tf_cr = tb_cr.text_frame
    tf_cr.word_wrap = True
    p = tf_cr.paragraphs[0]
    p.text = "High-Yield Room Types & Loyalty Tiers"
    p.font.name = "Arial"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEXT_PRIMARY

    p_lines = tf_cr.add_paragraph()
    p_lines.text = "• Presidential & Suites represent 48% of total room revenue.\n• Platinum loyalty guests generate 3.2x higher Average Daily Rate (ADR).\n• City Central Inn: Consistently high turnover with Standard rooms ($90/night).\n• Seaside Resort: Highest duration stays (average 4.5 nights per guest)."
    p_lines.font.name = "Arial"
    p_lines.font.size = Pt(10.5)
    p_lines.font.color.rgb = COLOR_TEXT_SECONDARY

    # ==========================================
    # SLIDE 6: Automation with Snowflake Tasks & Monitoring
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Pipeline Automation", "Scheduled Serverless Tasks & Operational Monitoring", "Automating daily rollups and monitoring health via INFORMATION_SCHEMA.TASK_HISTORY.")

    # Left: Task Definition
    c_tl = add_card(s6, 0.8, 2.2, 5.8, 4.6, RGBColor(255, 255, 255), RGBColor(226, 232, 240))
    tb_tl = s6.shapes.add_textbox(Inches(1.0), Inches(2.4), Inches(5.4), Inches(4.2))
    tf_tl = tb_tl.text_frame
    tf_tl.word_wrap = True
    p = tf_tl.paragraphs[0]
    p.text = "Scheduled Aggregation Task"
    p.font.name = "Arial"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT_INDIGO

    p_task = tf_tl.add_paragraph()
    p_task.text = """CREATE OR REPLACE TASK 
  TASK_DAILY_RESERVATION_AGGREGATION
  WAREHOUSE = HOTEL_WH
  SCHEDULE  = 'USING CRON 0 6 * * * UTC'
AS
INSERT INTO DAILY_RESERVATION_SUMMARY
SELECT 
  hotel_name, room_type, 
  total_reservations, net_revenue, 
  occupancy_pct, top_booking_source...
FROM FACT_RESERVATION_ANALYTICS;

ALTER TASK ... RESUME;"""
    p_task.font.name = "Consolas"
    p_task.font.size = Pt(9.5)
    p_task.font.color.rgb = COLOR_TEXT_PRIMARY

    # Right: Task History Results
    c_tr = add_card(s6, 6.8, 2.2, 5.733, 4.6, RGBColor(255, 255, 255), RGBColor(226, 232, 240))
    tb_tr = s6.shapes.add_textbox(Inches(7.0), Inches(2.4), Inches(5.33), Inches(4.2))
    tf_tr = tb_tr.text_frame
    tf_tr.word_wrap = True
    p = tf_tr.paragraphs[0]
    p.text = "Live Execution Monitoring (TASK_HISTORY)"
    p.font.name = "Arial"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_SUCCESS

    p_mon = tf_tr.add_paragraph()
    p_mon.text = """• Queried via INFORMATION_SCHEMA:
  SELECT NAME, STATE, SCHEDULED_TIME, DURATION_SECS
  FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY());

• Verified Execution Performance:
  - Task Status: SUCCEEDED
  - Duration: 3.07 seconds
  - Next Trigger: SCHEDULED (Daily 6 AM UTC)
  - Compute Warehouse: HOTEL_WH (X-Small)
  - Auto-suspend: 120 seconds (Zero idle costs)

• Reliability & Observability:
  Zero manual triggers needed in production. Automated error logging available via Snowflake Account Usage views."""
    p_mon.font.name = "Arial"
    p_mon.font.size = Pt(10.5)
    p_mon.font.color.rgb = COLOR_TEXT_SECONDARY

    # ==========================================
    # SLIDE 7: Summary & Strategic Value
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Conclusion", "Project Impact, Benefits & Next Steps", "Delivering a production-grade analytics platform with actionable operational insights.")

    takeaways = [
        ("Data Quality Guarantee", "Automatic isolation of malformed booking dates ensures 100% reliable financial reporting without corrupted timelines.", COLOR_ACCENT_BLUE),
        ("Revenue Leakage Control", "Identified that OTAs drive 38% of cancellations, empowering management to introduce non-refundable rate tiers.", COLOR_DANGER),
        ("Dynamic Capacity Optimization", "Real-time occupancy tracking pinpoints which properties and room categories have idle capacity.", COLOR_ACCENT_TEAL),
        ("Serverless Cost Efficiency", "Scheduled Task execution takes under 4 seconds with auto-suspending warehouses, reducing cloud compute overhead.", COLOR_SUCCESS)
    ]

    for idx, (t_title, t_desc, t_col) in enumerate(takeaways):
        tx = 0.8 + (idx * 2.95)
        card = add_card(s7, tx, 2.2, 2.8, 3.8, RGBColor(255, 255, 255), RGBColor(226, 232, 240))
        
        # Color bar
        cbar = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(tx + 0.2), Inches(2.4), Inches(0.4), Inches(0.06))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = t_col
        cbar.line.fill.background()

        tb = s7.shapes.add_textbox(Inches(tx + 0.15), Inches(2.6), Inches(2.5), Inches(3.2))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = t_title
        p.font.name = "Arial"
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_PRIMARY

        p2 = tf.add_paragraph()
        p2.text = "\n" + t_desc
        p2.font.name = "Arial"
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = COLOR_TEXT_SECONDARY

    # Footer banner
    foot_card = add_card(s7, 0.8, 6.2, 11.733, 0.65, RGBColor(238, 242, 255), RGBColor(199, 210, 254))
    tb_foot = s7.shapes.add_textbox(Inches(1.0), Inches(6.25), Inches(11.3), Inches(0.5))
    tf_foot = tb_foot.text_frame
    p_foot = tf_foot.paragraphs[0]
    p_foot.text = "GitHub: https://github.com/ashlesh0805/snowflake-hotel-reservation-analytics  •  Author: Ashlesh Gurram"
    p_foot.font.name = "Arial"
    p_foot.font.size = Pt(10.5)
    p_foot.font.bold = True
    p_foot.font.color.rgb = COLOR_ACCENT_INDIGO

    output_path = r"c:\Users\G ASHLESH\OneDrive\Desktop\snowflake\Hotel_Reservation_Analytics_Presentation.pptx"
    prs.save(output_path)
    print("Presentation created successfully at:", output_path)

if __name__ == "__main__":
    create_deck()
