import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_japanese_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Japanese Minimalist Color Palette (Wabi-Sabi / Modern Zen)
    COLOR_WASHI_WHITE = RGBColor(253, 253, 252) # Crisp rice paper white
    COLOR_CARD_BG = RGBColor(255, 255, 255)
    COLOR_SUMI_INK = RGBColor(24, 24, 27) # Deep sumi ink charcoal black
    COLOR_SLATE_GRAY = RGBColor(82, 82, 91) # Soft charcoal
    COLOR_MUTED_STONE = RGBColor(161, 161, 170) # Stone gray
    COLOR_HAIRLINE = RGBColor(228, 228, 231) # Delicate hairline border
    COLOR_VERMILION = RGBColor(200, 35, 51) # Japanese Vermilion / Torii Red (Hanko Seal)
    COLOR_VERMILION_LIGHT = RGBColor(255, 241, 242)
    COLOR_INDIGO = RGBColor(30, 58, 138) # Japanese Indigo (Aizome)
    COLOR_INDIGO_LIGHT = RGBColor(238, 242, 255)
    COLOR_MATCHA = RGBColor(21, 128, 61) # Deep matcha forest green
    COLOR_MATCHA_LIGHT = RGBColor(240, 253, 244)

    def draw_zen_header(slide, step_number, category_title, main_title, subtitle_text):
        # Vermilion Hanko-Style Square Stamp (English Number / Badge)
        stamp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.85), Inches(0.6), Inches(0.65), Inches(0.65))
        stamp.fill.solid()
        stamp.fill.fore_color.rgb = COLOR_VERMILION
        stamp.line.fill.background()
        tf_s = stamp.text_frame
        p_s = tf_s.paragraphs[0]
        p_s.text = step_number
        p_s.alignment = PP_ALIGN.CENTER
        p_s.font.name = "Arial"
        p_s.font.size = Pt(13)
        p_s.font.bold = True
        p_s.font.color.rgb = RGBColor(255, 255, 255)

        # Category Tracker (All English)
        cat_box = slide.shapes.add_textbox(Inches(1.65), Inches(0.55), Inches(10), Inches(0.35))
        tf_c = cat_box.text_frame
        p_c = tf_c.paragraphs[0]
        p_c.text = category_title.upper()
        p_c.font.name = "Arial"
        p_c.font.size = Pt(10)
        p_c.font.bold = True
        p_c.font.color.rgb = COLOR_VERMILION

        # Main Title (All English)
        t_box = slide.shapes.add_textbox(Inches(1.65), Inches(0.85), Inches(10.8), Inches(0.65))
        tf_t = t_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = main_title
        p_t.font.name = "Arial"
        p_t.font.size = Pt(22)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_SUMI_INK

        # Subtitle Context
        if subtitle_text:
            sub_box = slide.shapes.add_textbox(Inches(1.65), Inches(1.5), Inches(10.8), Inches(0.45))
            tf_sub = sub_box.text_frame
            tf_sub.word_wrap = True
            p_sub = tf_sub.paragraphs[0]
            p_sub.text = subtitle_text
            p_sub.font.name = "Arial"
            p_sub.font.size = Pt(11)
            p_sub.font.color.rgb = COLOR_SLATE_GRAY

        # Delicate horizontal hairline divider (Minimalist Zen element)
        rule = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.85), Inches(2.05), Inches(11.633), Inches(0.015))
        rule.fill.solid()
        rule.fill.fore_color.rgb = COLOR_HAIRLINE
        rule.line.fill.background()

    def add_zen_card(slide, left, top, width, height, bg_color=COLOR_CARD_BG, border_color=COLOR_HAIRLINE):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(0.8)
        return card

    # =========================================================================
    # SLIDE 1: Title Cover (Japanese Minimalist Style & Colors - English Language)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_WASHI_WHITE
    bg1.line.fill.background()

    # Red Vermilion Hanko Seal (Square)
    seal = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.2), Inches(1.2), Inches(1.1), Inches(1.1))
    seal.fill.solid()
    seal.fill.fore_color.rgb = COLOR_VERMILION
    seal.line.fill.background()
    tf_seal = seal.text_frame
    p_seal = tf_seal.paragraphs[0]
    p_seal.text = "SF\nDATA"
    p_seal.alignment = PP_ALIGN.CENTER
    p_seal.font.name = "Arial"
    p_seal.font.size = Pt(13)
    p_seal.font.bold = True
    p_seal.font.color.rgb = RGBColor(255, 255, 255)

    # Vertical Zen Line
    vline = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(2.6), Inches(1.2), Inches(0.03), Inches(1.1))
    vline.fill.solid()
    vline.fill.fore_color.rgb = COLOR_HAIRLINE
    vline.line.fill.background()

    # Category Pill
    tb_c = s1.shapes.add_textbox(Inches(2.8), Inches(1.2), Inches(9.0), Inches(0.35))
    tf_c = tb_c.text_frame
    p_c = tf_c.paragraphs[0]
    p_c.text = "SNOWFLAKE CLOUD DATA PLATFORM  •  ENTERPRISE ANALYTICS"
    p_c.font.name = "Arial"
    p_c.font.size = Pt(10.5)
    p_c.font.bold = True
    p_c.font.color.rgb = COLOR_VERMILION

    # Sub-header
    tb_j = s1.shapes.add_textbox(Inches(2.8), Inches(1.55), Inches(9.0), Inches(0.45))
    tf_j = tb_j.text_frame
    p_j = tf_j.paragraphs[0]
    p_j.text = "Modern Data Warehousing, Occupancy Modeling & Pipeline Automation"
    p_j.font.name = "Arial"
    p_j.font.size = Pt(14)
    p_j.font.bold = True
    p_j.font.color.rgb = COLOR_SUMI_INK

    # Main Hero Heading
    tb_title = s1.shapes.add_textbox(Inches(1.15), Inches(2.7), Inches(11.0), Inches(1.6))
    tf_t = tb_title.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "Hotel Reservation & Occupancy\nAnalytics System"
    p_t.font.name = "Arial"
    p_t.font.size = Pt(38)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_SUMI_INK

    # Sub-caption
    tb_sub = s1.shapes.add_textbox(Inches(1.2), Inches(4.5), Inches(10.5), Inches(0.8))
    tf_sub = tb_sub.text_frame
    tf_sub.word_wrap = True
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = "A minimalist, high-precision cloud architecture designed for multi-property hospitality chains: Medallion Architecture • Automated Ingestion • Date Integrity • Dynamic Occupancy • Serverless Tasks."
    p_sub.font.name = "Arial"
    p_sub.font.size = Pt(12)
    p_sub.font.color.rgb = COLOR_SLATE_GRAY

    # Bottom 4 Minimalist Metadata Cards
    meta_pills = [
        ("01", "WAREHOUSE", "HOTEL_WH (X-Small)", COLOR_SUMI_INK),
        ("02", "DATABASE", "HOTEL_RESERVATION_DB", COLOR_INDIGO),
        ("03", "AUTOMATION", "CRON 0 6 * * * UTC", COLOR_VERMILION),
        ("04", "AUTHOR", "Ashlesh Gurram", COLOR_SLATE_GRAY)
    ]
    for idx, (step, m_lbl, m_val, m_col) in enumerate(meta_pills):
        px = 1.2 + (idx * 2.75)
        card = add_zen_card(s1, px, 5.5, 2.55, 1.2, RGBColor(255, 255, 255), COLOR_HAIRLINE)
        
        tb_m = s1.shapes.add_textbox(Inches(px + 0.15), Inches(5.6), Inches(2.25), Inches(1.0))
        tf_m = tb_m.text_frame
        p1 = tf_m.paragraphs[0]
        p1.text = f"{step}  /  {m_lbl}"
        p1.font.name = "Arial"
        p1.font.size = Pt(9.5)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_MUTED_STONE
        
        p2 = tf_m.add_paragraph()
        p2.text = m_val
        p2.font.name = "Arial"
        p2.font.size = Pt(11)
        p2.font.bold = True
        p2.font.color.rgb = m_col

    # =========================================================================
    # SLIDE 2: Problem Statement & Challenges
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    draw_zen_header(s2, "02", "PROBLEM STATEMENT", "Core Operational Challenges in Multi-Property Hospitality", "Fragmented reservation sources introduced corrupt dates, unmonitored cancellation exposure, and inaccurate occupancy metrics.")

    cards_s2 = [
        ("01", "Anomalous Date Corruptions", "Check-out Dates Preceding Check-in", "Guests and third-party OTAs frequently inject check-out dates earlier than check-in or zero-day stays, severely contaminating average stay and capacity metrics.", COLOR_VERMILION),
        ("02", "Untracked Cancellation Leakage", "Revenue Loss & Sudden Spikes", "Sudden cancellation spikes through indirect channels caused unmonitored revenue leakage without clear visibility into refund volumes ($5,290+).", COLOR_INDIGO),
        ("03", "Dynamic Occupancy Modeling", "Fluctuating Monthly Capacity", "Reconciling active room capacity against fluctuating days in calendar months while isolating cancelled bookings required dynamic cross-join modeling.", COLOR_SLATE_GRAY),
        ("04", "Manual Pipeline Vulnerability", "Spreadsheet Silos & Idle Compute", "Relying on end-of-month manual spreadsheet exports lacked automated scheduling, versioned time-travel, and automated health monitoring.", COLOR_MATCHA)
    ]

    for idx, (num, title, subtitle, desc, col) in enumerate(cards_s2):
        col_idx = idx % 2
        row_idx = idx // 2
        cx = 0.85 + (col_idx * 5.9)
        cy = 2.3 + (row_idx * 2.35)
        card = add_zen_card(s2, cx, cy, 5.7, 2.15, RGBColor(255, 255, 255), COLOR_HAIRLINE)
        
        t_box = s2.shapes.add_textbox(Inches(cx + 0.2), Inches(cy + 0.15), Inches(5.3), Inches(1.85))
        tf = t_box.text_frame
        tf.word_wrap = True
        
        p1 = tf.paragraphs[0]
        p1.text = f"{num}   {title}"
        p1.font.name = "Arial"
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_SUMI_INK
        
        p_en = tf.add_paragraph()
        p_en.text = subtitle.upper()
        p_en.font.name = "Arial"
        p_en.font.size = Pt(9.5)
        p_en.font.bold = True
        p_en.font.color.rgb = col

        p_desc = tf.add_paragraph()
        p_desc.text = "\n" + desc
        p_desc.font.name = "Arial"
        p_desc.font.size = Pt(10.5)
        p_desc.font.color.rgb = COLOR_SLATE_GRAY

    # =========================================================================
    # SLIDE 3: Architecture
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    draw_zen_header(s3, "03", "DATA ARCHITECTURE", "3-Tier Medallion Data Engineering Architecture", "Separation of concerns: Raw ingestion landing, business validation, and executive analytics consumption.")

    layers = [
        ("RAW LAYER", "BRONZE INGESTION ZONE", "• External Stage (@HOTEL_S3_STAGE)\n• CSV File Format with header skip\n• RAW_GUESTS (20 guest profiles)\n• RAW_ROOMS (25 rooms across 4 hotels)\n• RAW_RESERVATIONS (43 bookings)\n• RAW_PAYMENTS (43 payment records)", COLOR_INDIGO, COLOR_INDIGO_LIGHT),
        ("CLEAN LAYER", "SILVER VALIDATION ZONE", "• V_RESERVATION_DATE_VALIDATION\n• Automatically identifies RES041-043\n• CLEAN_RESERVATIONS (40 valid rows)\n• V_CANCELLED_RESERVATIONS\n• Tracks 8 cancellations ($5,290 refund)\n• Enriched guest profile linkages", COLOR_VERMILION, COLOR_VERMILION_LIGHT),
        ("ANALYTICS LAYER", "GOLD CONSUMPTION ZONE", "• FACT_RESERVATION_ANALYTICS\n• V_MONTHLY_OCCUPANCY (Dynamic %)\n• V_REVENUE_BY_HOTEL (Net Revenue)\n• V_REVENUE_BY_ROOM_TYPE (ADR & Rev)\n• DAILY_RESERVATION_SUMMARY (Summary)\n• Serverless Daily Task (CRON 6 AM)", COLOR_MATCHA, COLOR_MATCHA_LIGHT)
    ]

    for idx, (title, subtitle, desc, col, bg_col) in enumerate(layers):
        lx = 0.85 + (idx * 3.9)
        card = add_zen_card(s3, lx, 2.3, 3.8, 4.6, bg_col, COLOR_HAIRLINE)
        
        tb = s3.shapes.add_textbox(Inches(lx + 0.2), Inches(2.5), Inches(3.4), Inches(4.2))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.name = "Arial"
        p1.font.size = Pt(14)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_SUMI_INK

        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.name = "Arial"
        p2.font.size = Pt(9.5)
        p2.font.bold = True
        p2.font.color.rgb = col

        p3 = tf.add_paragraph()
        p3.text = "\n" + desc
        p3.font.name = "Arial"
        p3.font.size = Pt(11)
        p3.font.color.rgb = COLOR_SUMI_INK

    # =========================================================================
    # SLIDE 4: Data Quality & Date Validation Logic
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    draw_zen_header(s4, "04", "DATA QUALITY & INTEGRITY", "Reservation Date Validation Logic & Quarantine", "Automated SQL rules quarantine negative durations and zero-night stays before data reaches analytics.")

    # Left: Code Card
    card_l = add_zen_card(s4, 0.85, 2.3, 5.7, 4.6, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_l = s4.shapes.add_textbox(Inches(1.05), Inches(2.45), Inches(5.3), Inches(4.3))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    p.text = "SQL Validation Rules"
    p.font.name = "Arial"
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_SUMI_INK

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
    p_code.font.color.rgb = COLOR_INDIGO

    # Right: Detected Anomalies
    card_r = add_zen_card(s4, 6.75, 2.3, 5.733, 4.6, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_r = s4.shapes.add_textbox(Inches(6.95), Inches(2.45), Inches(5.33), Inches(4.3))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "Quarantined Anomalies (3 Corrupt Bookings)"
    p.font.name = "Arial"
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_VERMILION

    anomalies = [
        ("RES041 • Grand Palace Hotel", "IN: 2024-11-15  |  OUT: 2024-11-10  (-5 Days)", "Check-out occurs 5 days prior to check-in. Flagged immediately by validation view and filtered out of CLEAN_RESERVATIONS."),
        ("RES042 • Seaside Resort", "IN: 2024-12-25  |  OUT: 2024-12-20  (-5 Days)", "OTA booking injection with inverted calendar sequence. Quarantined to prevent skewing room availability metrics."),
        ("RES043 • Mountain Lodge", "IN: 2024-10-10  |  OUT: 2024-10-10  (0 Nights)", "Same-day booking and departure without overnight stay. Excluded from overnight occupancy percentage calculations.")
    ]
    for anom_t, anom_d, anom_c in anomalies:
        pa = tf_r.add_paragraph()
        pa.text = f"\n• {anom_t}\n   {anom_d}\n   {anom_c}"
        pa.font.name = "Arial"
        pa.font.size = Pt(10.5)
        pa.font.color.rgb = COLOR_SLATE_GRAY

    # =========================================================================
    # SLIDE 5: Executive Metrics & Findings
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    draw_zen_header(s5, "05", "EXECUTIVE METRICS", "Key Analytical Findings & Financial Performance", "Verified metrics computed from FACT_RESERVATION_ANALYTICS across 4 hotel properties.")

    kpis = [
        ("40", "Valid Bookings", "3 corrupt bookings filtered out", COLOR_INDIGO),
        ("$46,880", "Net Realized Revenue", "Gross revenue less $5,290 refunds", COLOR_MATCHA),
        ("20.0%", "Cancellation Rate", "8 cancelled bookings tracked", COLOR_VERMILION),
        ("58.1%", "Peak Occupancy Rate", "Seaside Resort led October demand", COLOR_SUMI_INK)
    ]

    for idx, (val, title, note, col) in enumerate(kpis):
        kx = 0.85 + (idx * 2.9)
        card = add_zen_card(s5, kx, 2.3, 2.8, 1.85, RGBColor(255, 255, 255), COLOR_HAIRLINE)
        tb = s5.shapes.add_textbox(Inches(kx + 0.15), Inches(2.4), Inches(2.5), Inches(1.6))
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
        p2.font.color.rgb = COLOR_SUMI_INK

        p3 = tf.add_paragraph()
        p3.text = note
        p3.font.name = "Arial"
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = COLOR_MUTED_STONE

    # Lower comparison cards
    c_left = add_zen_card(s5, 0.85, 4.35, 5.7, 2.5, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_cl = s5.shapes.add_textbox(Inches(1.05), Inches(4.45), Inches(5.3), Inches(2.2))
    tf_cl = tb_cl.text_frame
    tf_cl.word_wrap = True
    p = tf_cl.paragraphs[0]
    p.text = "Cancellation Exposure by Booking Channel"
    p.font.name = "Arial"
    p.font.size = Pt(12.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_SUMI_INK

    p_lines = tf_cl.add_paragraph()
    p_lines.text = "• Online Travel Agencies (OTA): 38.4% cancellation rate ($2,690 refund impact).\n• Direct Hotel Website: 14.3% cancellation rate (highest profit margin and guest loyalty).\n• Phone Reservations: 18.2% cancellation rate (corporate accounts with flexible policies).\n• Walk-In Guests: 0% cancellations (instant guaranteed revenue)."
    p_lines.font.name = "Arial"
    p_lines.font.size = Pt(10)
    p_lines.font.color.rgb = COLOR_SLATE_GRAY

    c_right = add_zen_card(s5, 6.75, 4.35, 5.733, 2.5, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_cr = s5.shapes.add_textbox(Inches(6.95), Inches(4.45), Inches(5.33), Inches(2.2))
    tf_cr = tb_cr.text_frame
    tf_cr.word_wrap = True
    p = tf_cr.paragraphs[0]
    p.text = "Room Tier Revenue & Loyalty Contribution"
    p.font.name = "Arial"
    p.font.size = Pt(12.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_SUMI_INK

    p_lines = tf_cr.add_paragraph()
    p_lines.text = "• Suite & Presidential categories account for 48% of total gross hotel revenue.\n• Platinum Loyalty Members average 3.2x higher ADR than guest bookers.\n• Seaside Resort recorded the highest average length of stay (4.2 nights).\n• City Central Inn achieved the highest inventory turnover with standard rooms."
    p_lines.font.name = "Arial"
    p_lines.font.size = Pt(10)
    p_lines.font.color.rgb = COLOR_SLATE_GRAY

    # =========================================================================
    # SLIDE 6: Scheduled Task & Monitoring
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    draw_zen_header(s6, "06", "SERVERLESS AUTOMATION", "Scheduled Task Definition & Operational Health", "Serverless aggregation task running daily at 6 AM UTC with real-time health verification via Task History.")

    # Left: Task SQL
    c_tl = add_zen_card(s6, 0.85, 2.3, 5.7, 4.6, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_tl = s6.shapes.add_textbox(Inches(1.05), Inches(2.45), Inches(5.3), Inches(4.3))
    tf_tl = tb_tl.text_frame
    tf_tl.word_wrap = True
    p = tf_tl.paragraphs[0]
    p.text = "Snowflake Scheduled Task Definition"
    p.font.name = "Arial"
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_SUMI_INK

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
    p_task.font.size = Pt(9.5)
    p_task.font.color.rgb = COLOR_INDIGO

    # Right: Task History Results
    c_tr = add_zen_card(s6, 6.75, 2.3, 5.733, 4.6, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_tr = s6.shapes.add_textbox(Inches(6.95), Inches(2.45), Inches(5.33), Inches(4.3))
    tf_tr = tb_tr.text_frame
    tf_tr.word_wrap = True
    p = tf_tr.paragraphs[0]
    p.text = "Task Execution History & Metrics (TASK_HISTORY)"
    p.font.name = "Arial"
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_MATCHA

    p_mon = tf_tr.add_paragraph()
    p_mon.text = """• Health Monitoring Query:
  SELECT NAME, STATE, SCHEDULED_TIME, DURATION_SECS
  FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY());

• Observed Live Metrics:
  ✓ Execution State: SUCCEEDED
  ✓ Run Duration: 3.07 seconds (Low Latency)
  ✓ Next Run: SCHEDULED (Daily 06:00 UTC)
  ✓ Compute Sizing: HOTEL_WH (X-Small)
  ✓ Auto-Suspend: 120 seconds (Zero idle compute costs)

• Operational Benefits:
  Daily reservation aggregation runs fully autonomously, eliminating manual export delays and human data entry errors."""
    p_mon.font.name = "Arial"
    p_mon.font.size = Pt(10.5)
    p_mon.font.color.rgb = COLOR_SLATE_GRAY

    # =========================================================================
    # SLIDE 7: Conclusion & Business Impact
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    draw_zen_header(s7, "07", "BUSINESS VALUE & ROI", "Strategic Impact & Production Deliverables", "Clean, high-precision analytics delivered through Snowflake modern cloud data engineering best practices.")

    points = [
        ("Data Trust & Integrity", "Automated Validation", "Quarantined corrupt check-out dates and zero-night stays, ensuring executive reporting accuracy.", COLOR_INDIGO),
        ("Revenue Protection", "Cancellation Transparency", "Exposed $2,690 in OTA cancellation refunds, providing actionable data for policy adjustments.", COLOR_VERMILION),
        ("Dynamic Yield Optimization", "Capacity Intelligence", "Accurate monthly occupancy rates empower revenue management to optimize room rates dynamically.", COLOR_MATCHA),
        ("Zero Idle Compute Cost", "Optimized Warehouse", "Task executes in 3 seconds on an X-Small warehouse with 120s auto-suspend, minimizing infrastructure spend.", COLOR_SUMI_INK)
    ]

    for idx, (title, subtitle, desc, col) in enumerate(points):
        tx = 0.85 + (idx * 2.9)
        card = add_zen_card(s7, tx, 2.3, 2.8, 3.7, RGBColor(255, 255, 255), COLOR_HAIRLINE)
        
        cbar = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(tx + 0.2), Inches(2.5), Inches(0.35), Inches(0.04))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = col
        cbar.line.fill.background()

        tb = s7.shapes.add_textbox(Inches(tx + 0.15), Inches(2.65), Inches(2.5), Inches(3.1))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Arial"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = COLOR_SUMI_INK

        p_sub = tf.add_paragraph()
        p_sub.text = subtitle.upper()
        p_sub.font.name = "Arial"
        p_sub.font.size = Pt(9)
        p_sub.font.bold = True
        p_sub.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = "\n" + desc
        p2.font.name = "Arial"
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = COLOR_SLATE_GRAY

    # Footer note
    foot_card = add_zen_card(s7, 0.85, 6.25, 11.633, 0.65, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_foot = s7.shapes.add_textbox(Inches(1.05), Inches(6.3), Inches(11.2), Inches(0.5))
    tf_foot = tb_foot.text_frame
    p_foot = tf_foot.paragraphs[0]
    p_foot.text = "GitHub: https://github.com/ashlesh0805/snowflake-hotel-reservation-analytics  •  Author: Ashlesh Gurram"
    p_foot.font.name = "Arial"
    p_foot.font.size = Pt(10)
    p_foot.font.bold = True
    p_foot.font.color.rgb = COLOR_VERMILION

    paths_to_save = [
        r"C:\Users\G ASHLESH\Downloads\snowflake_screenshots\Hotel_Reservation_Analytics_Japanese_Style.pptx",
        r"C:\Users\G ASHLESH\Downloads\Hotel_Reservation_Analytics_Japanese_Style.pptx",
        r"C:\Users\G ASHLESH\Downloads\Hotel_Reservation_Analytics_Japanese_Style_v2.pptx",
        r"C:\Users\G ASHLESH\Downloads\Hotel_Reservation_Analytics_Zen_Minimalist.pptx",
        r"c:\Users\G ASHLESH\OneDrive\Desktop\snowflake\Hotel_Reservation_Analytics_Japanese_Style.pptx",
        r"c:\Users\G ASHLESH\OneDrive\Desktop\snowflake\Hotel_Reservation_Analytics_Zen_Minimalist.pptx"
    ]
    
    print("Clean English Japanese-Style Presentation saving to:")
    for path in paths_to_save:
        try:
            prs.save(path)
            print(" [OK] Saved:", path)
        except PermissionError:
            print(" [LOCKED by active PowerPoint session]:", path)

if __name__ == "__main__":
    create_japanese_deck()
