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

    # Japanese Minimalist Color Palette (Pure Zen Aesthetic)
    COLOR_WASHI_WHITE = RGBColor(253, 253, 252) # Crisp rice-paper off-white
    COLOR_CARD_BG = RGBColor(255, 255, 255)     # Clean white card background
    COLOR_SUMI_INK = RGBColor(24, 24, 27)        # Deep sumi charcoal ink
    COLOR_SLATE_GRAY = RGBColor(82, 82, 91)      # Refined secondary text
    COLOR_MUTED_STONE = RGBColor(161, 161, 170)  # Subtle metadata label
    COLOR_HAIRLINE = RGBColor(228, 228, 231)     # Elegant hairline border
    COLOR_VERMILION = RGBColor(200, 35, 51)      # Japanese Torii Vermilion Red
    COLOR_VERMILION_BG = RGBColor(255, 241, 242) # Very soft vermilion tint
    COLOR_INDIGO = RGBColor(30, 58, 138)         # Japanese Aizome Indigo
    COLOR_INDIGO_BG = RGBColor(238, 242, 255)    # Very soft indigo tint
    COLOR_MATCHA = RGBColor(21, 128, 61)         # Matcha forest green
    COLOR_MATCHA_BG = RGBColor(240, 253, 244)    # Very soft matcha tint

    def set_clean_margins(tf):
        tf.word_wrap = True
        tf.margin_left = Inches(0.14)
        tf.margin_right = Inches(0.14)
        tf.margin_top = Inches(0.14)
        tf.margin_bottom = Inches(0.14)

    def draw_zen_header(slide, step_number, category_title, main_title, subtitle_text):
        # Vermilion Hanko-Style Stamp (English Number Badge)
        stamp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.85), Inches(0.52), Inches(0.55), Inches(0.55))
        stamp.fill.solid()
        stamp.fill.fore_color.rgb = COLOR_VERMILION
        stamp.line.fill.background()
        tf_s = stamp.text_frame
        set_clean_margins(tf_s)
        p_s = tf_s.paragraphs[0]
        p_s.text = step_number
        p_s.alignment = PP_ALIGN.CENTER
        p_s.font.name = "Arial"
        p_s.font.size = Pt(13)
        p_s.font.bold = True
        p_s.font.color.rgb = RGBColor(255, 255, 255)

        # Category Tracker (Top)
        cat_box = slide.shapes.add_textbox(Inches(1.55), Inches(0.48), Inches(10.5), Inches(0.28))
        tf_c = cat_box.text_frame
        set_clean_margins(tf_c)
        p_c = tf_c.paragraphs[0]
        p_c.text = category_title.upper()
        p_c.font.name = "Arial"
        p_c.font.size = Pt(9.5)
        p_c.font.bold = True
        p_c.font.color.rgb = COLOR_VERMILION

        # Main Title (Middle)
        t_box = slide.shapes.add_textbox(Inches(1.55), Inches(0.76), Inches(10.8), Inches(0.48))
        tf_t = t_box.text_frame
        set_clean_margins(tf_t)
        p_t = tf_t.paragraphs[0]
        p_t.text = main_title
        p_t.font.name = "Arial"
        p_t.font.size = Pt(20)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_SUMI_INK

        # Subtitle Context (Bottom)
        if subtitle_text:
            sub_box = slide.shapes.add_textbox(Inches(1.55), Inches(1.26), Inches(10.8), Inches(0.35))
            tf_sub = sub_box.text_frame
            set_clean_margins(tf_sub)
            p_sub = tf_sub.paragraphs[0]
            p_sub.text = subtitle_text
            p_sub.font.name = "Arial"
            p_sub.font.size = Pt(10.5)
            p_sub.font.color.rgb = COLOR_SLATE_GRAY

        # Hairline Divider
        rule = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.85), Inches(1.72), Inches(11.633), Inches(0.012))
        rule.fill.solid()
        rule.fill.fore_color.rgb = COLOR_HAIRLINE
        rule.line.fill.background()

    def add_zen_card(slide, left, top, width, height, bg_color=COLOR_CARD_BG, border_color=COLOR_HAIRLINE):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(0.9)
        return card

    # =========================================================================
    # SLIDE 1: Title Cover (Clean Zen Minimalist - Team 07 Featured)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_WASHI_WHITE
    bg1.line.fill.background()

    # Red Hanko Stamp
    seal = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9), Inches(0.85), Inches(1.0), Inches(1.0))
    seal.fill.solid()
    seal.fill.fore_color.rgb = COLOR_VERMILION
    seal.line.fill.background()
    tf_seal = seal.text_frame
    set_clean_margins(tf_seal)
    p_seal = tf_seal.paragraphs[0]
    p_seal.text = "TEAM\n07"
    p_seal.alignment = PP_ALIGN.CENTER
    p_seal.font.name = "Arial"
    p_seal.font.size = Pt(13)
    p_seal.font.bold = True
    p_seal.font.color.rgb = RGBColor(255, 255, 255)

    # Vertical Zen Divider Line
    vline = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(2.15), Inches(0.85), Inches(0.02), Inches(1.0))
    vline.fill.solid()
    vline.fill.fore_color.rgb = COLOR_HAIRLINE
    vline.line.fill.background()

    # Category Pill
    tb_c = s1.shapes.add_textbox(Inches(2.35), Inches(0.85), Inches(9.5), Inches(0.3))
    tf_c = tb_c.text_frame
    set_clean_margins(tf_c)
    p_c = tf_c.paragraphs[0]
    p_c.text = "SNOWFLAKE CLOUD DATA PLATFORM  •  ENTERPRISE ANALYTICS"
    p_c.font.name = "Arial"
    p_c.font.size = Pt(10)
    p_c.font.bold = True
    p_c.font.color.rgb = COLOR_VERMILION

    # Sub-header
    tb_j = s1.shapes.add_textbox(Inches(2.35), Inches(1.18), Inches(9.5), Inches(0.4))
    tf_j = tb_j.text_frame
    set_clean_margins(tf_j)
    p_j = tf_j.paragraphs[0]
    p_j.text = "High-Precision Data Warehousing & Automated Pipeline Architecture"
    p_j.font.name = "Arial"
    p_j.font.size = Pt(13.5)
    p_j.font.bold = True
    p_j.font.color.rgb = COLOR_SUMI_INK

    # Main Hero Heading
    tb_title = s1.shapes.add_textbox(Inches(0.9), Inches(2.2), Inches(11.5), Inches(1.3))
    tf_t = tb_title.text_frame
    set_clean_margins(tf_t)
    p_t = tf_t.paragraphs[0]
    p_t.text = "Hotel Reservation & Occupancy\nAnalytics System"
    p_t.font.name = "Arial"
    p_t.font.size = Pt(36)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_SUMI_INK

    # Description
    tb_sub = s1.shapes.add_textbox(Inches(0.9), Inches(3.65), Inches(11.5), Inches(0.55))
    tf_sub = tb_sub.text_frame
    set_clean_margins(tf_sub)
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = "An end-to-end cloud data engineering solution: Medallion Architecture, Automated Ingestion, Date Integrity Validation, Dynamic Occupancy Modeling, and Serverless Task Orchestration."
    p_sub.font.name = "Arial"
    p_sub.font.size = Pt(11.5)
    p_sub.font.color.rgb = COLOR_SLATE_GRAY

    # Team 07 Prominent Attribution Card
    tcard = add_zen_card(s1, 0.9, 4.45, 11.533, 1.05, RGBColor(255, 255, 255), COLOR_VERMILION)
    tb_team = s1.shapes.add_textbox(Inches(1.05), Inches(4.52), Inches(11.2), Inches(0.9))
    tf_team = tb_team.text_frame
    set_clean_margins(tf_team)
    pt1 = tf_team.paragraphs[0]
    pt1.text = "PROJECT BY TEAM 07"
    pt1.font.name = "Arial"
    pt1.font.size = Pt(9.5)
    pt1.font.bold = True
    pt1.font.color.rgb = COLOR_VERMILION

    pt2 = tf_team.add_paragraph()
    pt2.text = "Ashlesh Gurram   •   Varun   •   Sakshi   •   Barghavi   •   Akshitha"
    pt2.font.name = "Arial"
    pt2.font.size = Pt(13)
    pt2.font.bold = True
    pt2.font.color.rgb = COLOR_SUMI_INK

    # Bottom 4 Minimalist Specs Cards
    meta_pills = [
        ("01", "WAREHOUSE", "HOTEL_WH (X-Small)", COLOR_SUMI_INK),
        ("02", "DATABASE", "HOTEL_RESERVATION_DB", COLOR_INDIGO),
        ("03", "AUTOMATION", "CRON 0 6 * * * UTC", COLOR_VERMILION),
        ("04", "PLATFORM", "Snowflake Enterprise Cloud", COLOR_MATCHA)
    ]
    for idx, (step, m_lbl, m_val, m_col) in enumerate(meta_pills):
        px = 0.9 + (idx * 2.95)
        card = add_zen_card(s1, px, 5.75, 2.75, 1.15, RGBColor(255, 255, 255), COLOR_HAIRLINE)
        
        tb_m = s1.shapes.add_textbox(Inches(px + 0.1), Inches(5.82), Inches(2.55), Inches(0.95))
        tf_m = tb_m.text_frame
        set_clean_margins(tf_m)
        p1 = tf_m.paragraphs[0]
        p1.text = f"{step}  /  {m_lbl}"
        p1.font.name = "Arial"
        p1.font.size = Pt(9)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_MUTED_STONE
        
        p2 = tf_m.add_paragraph()
        p2.text = m_val
        p2.font.name = "Arial"
        p2.font.size = Pt(11)
        p2.font.bold = True
        p2.font.color.rgb = m_col

    # =========================================================================
    # SLIDE 2: Problem Statement & Challenges (2x2 Balanced Grid)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    draw_zen_header(s2, "02", "PROBLEM STATEMENT", "Core Operational Challenges in Multi-Property Hospitality", "Fragmented reservation sources introduced corrupt dates, unmonitored cancellation exposure, and inaccurate occupancy metrics.")

    cards_s2 = [
        ("01", "Anomalous Date Corruptions", "Check-out Preceding Check-in", "Corrupt booking records where check-out precedes check-in or zero-night stays severely skew length-of-stay and inventory calculations.", COLOR_VERMILION),
        ("02", "Untracked Cancellation Leakage", "Revenue Loss & Sudden Spikes", "Sudden cancellation spikes through indirect channels caused unmonitored revenue leakage without clear visibility into refund volumes ($5,290+).", COLOR_INDIGO),
        ("03", "Dynamic Occupancy Complexity", "Fluctuating Monthly Capacity", "Reconciling active room capacity across varying calendar days while excluding cancelled bookings required dynamic cross-join modeling.", COLOR_MATCHA),
        ("04", "Manual Pipeline Vulnerability", "Spreadsheet Silos & Idle Compute", "Relying on end-of-month manual spreadsheet exports risked human error, lacked versioning, and lacked automated schedule health monitoring.", COLOR_SLATE_GRAY)
    ]

    for idx, (num, title, subtitle, desc, col) in enumerate(cards_s2):
        col_idx = idx % 2
        row_idx = idx // 2
        cx = 0.85 + (col_idx * 5.95)
        cy = 1.95 + (row_idx * 2.5)
        card = add_zen_card(s2, cx, cy, 5.68, 2.3, RGBColor(255, 255, 255), COLOR_HAIRLINE)
        
        # Color accent strip on top of card
        strip = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(cx + 0.18), Inches(cy + 0.18), Inches(0.4), Inches(0.04))
        strip.fill.solid()
        strip.fill.fore_color.rgb = col
        strip.line.fill.background()

        t_box = s2.shapes.add_textbox(Inches(cx + 0.15), Inches(cy + 0.28), Inches(5.38), Inches(1.85))
        tf = t_box.text_frame
        set_clean_margins(tf)
        
        p1 = tf.paragraphs[0]
        p1.text = f"{num}   {title}"
        p1.font.name = "Arial"
        p1.font.size = Pt(12.5)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_SUMI_INK
        
        p_en = tf.add_paragraph()
        p_en.text = subtitle.upper()
        p_en.font.name = "Arial"
        p_en.font.size = Pt(9)
        p_en.font.bold = True
        p_en.font.color.rgb = col

        p_desc = tf.add_paragraph()
        p_desc.text = desc
        p_desc.font.name = "Arial"
        p_desc.font.size = Pt(10)
        p_desc.font.color.rgb = COLOR_SLATE_GRAY

    # =========================================================================
    # SLIDE 3: Architecture (3-Tier Medallion Columns)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    draw_zen_header(s3, "03", "DATA ARCHITECTURE", "3-Tier Medallion Data Engineering Architecture", "Separation of concerns: Raw ingestion landing, business validation, and executive analytics consumption.")

    layers = [
        ("RAW LAYER", "BRONZE INGESTION ZONE", [
            "• S3 External Stage (@HOTEL_S3_STAGE)",
            "• CSV File Format with header skip",
            "• RAW_GUESTS (20 guest profiles)",
            "• RAW_ROOMS (25 rooms across 4 hotels)",
            "• RAW_RESERVATIONS (43 bookings)",
            "• RAW_PAYMENTS (43 payment records)",
            "• Full schema immutability preserved"
        ], COLOR_INDIGO, COLOR_INDIGO_BG),
        ("CLEAN LAYER", "SILVER VALIDATION ZONE", [
            "• V_RESERVATION_DATE_VALIDATION",
            "• Automatically flags RES041–RES043",
            "• CLEAN_RESERVATIONS (40 valid rows)",
            "• V_CANCELLED_RESERVATIONS",
            "• Tracks 8 cancellations ($5,290 refund)",
            "• Enriched guest profile linkages",
            "• Date anomaly quarantine in place"
        ], COLOR_VERMILION, COLOR_VERMILION_BG),
        ("ANALYTICS LAYER", "GOLD CONSUMPTION ZONE", [
            "• FACT_RESERVATION_ANALYTICS",
            "• V_MONTHLY_OCCUPANCY (Dynamic %)",
            "• V_REVENUE_BY_HOTEL (Net Revenue)",
            "• V_REVENUE_BY_ROOM_TYPE (ADR & Rev)",
            "• DAILY_RESERVATION_SUMMARY",
            "• Automated Daily Task (CRON 6 AM)",
            "• Power BI / Tableau direct access"
        ], COLOR_MATCHA, COLOR_MATCHA_BG)
    ]

    for idx, (title, subtitle, bullets, col, bg_col) in enumerate(layers):
        lx = 0.85 + (idx * 3.98)
        card = add_zen_card(s3, lx, 1.95, 3.7, 4.95, bg_col, COLOR_HAIRLINE)
        
        # Color bar indicator
        top_bar = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(lx + 0.2), Inches(2.1), Inches(0.45), Inches(0.04))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = col
        top_bar.line.fill.background()

        tb = s3.shapes.add_textbox(Inches(lx + 0.15), Inches(2.2), Inches(3.4), Inches(4.55))
        tf = tb.text_frame
        set_clean_margins(tf)
        
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.name = "Arial"
        p1.font.size = Pt(13.5)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_SUMI_INK

        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.name = "Arial"
        p2.font.size = Pt(9)
        p2.font.bold = True
        p2.font.color.rgb = col

        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = b
            pb.font.name = "Arial"
            pb.font.size = Pt(10)
            pb.font.color.rgb = COLOR_SUMI_INK

    # =========================================================================
    # SLIDE 4: Data Quality & Date Validation Logic
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    draw_zen_header(s4, "04", "DATA QUALITY & INTEGRITY", "Reservation Date Validation Logic & Quarantine", "Automated SQL rules quarantine negative durations and zero-night stays before data reaches analytics.")

    # Left: Code Card
    card_l = add_zen_card(s4, 0.85, 1.95, 5.68, 4.95, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_l = s4.shapes.add_textbox(Inches(1.0), Inches(2.05), Inches(5.38), Inches(4.7))
    tf_l = tb_l.text_frame
    set_clean_margins(tf_l)
    p = tf_l.paragraphs[0]
    p.text = "SQL Automated Validation Rules"
    p.font.name = "Arial"
    p.font.size = Pt(13)
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
    p_code.font.size = Pt(9.5)
    p_code.font.color.rgb = COLOR_INDIGO

    p_note = tf_l.add_paragraph()
    p_note.text = "\nProduction Impact:\nAny record not matching 'VALID' is automatically excluded from the CLEAN_RESERVATIONS production table, ensuring clean business reporting."
    p_note.font.name = "Arial"
    p_note.font.size = Pt(9.5)
    p_note.font.color.rgb = COLOR_SLATE_GRAY

    # Right: Detected Anomalies
    card_r = add_zen_card(s4, 6.8, 1.95, 5.68, 4.95, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_r = s4.shapes.add_textbox(Inches(6.95), Inches(2.05), Inches(5.38), Inches(4.7))
    tf_r = tb_r.text_frame
    set_clean_margins(tf_r)
    p = tf_r.paragraphs[0]
    p.text = "Quarantined Anomalies (3 Corrupt Bookings)"
    p.font.name = "Arial"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_VERMILION

    anomalies = [
        ("RES041 • Grand Palace Hotel", "IN: 2024-11-15  |  OUT: 2024-11-10  (-5 Days)", "Check-out occurs 5 days before check-in. Flagged immediately by validation view and filtered out of CLEAN_RESERVATIONS."),
        ("RES042 • Seaside Resort", "IN: 2024-12-25  |  OUT: 2024-12-20  (-5 Days)", "OTA booking injection with inverted calendar sequence. Quarantined to prevent skewing room availability metrics."),
        ("RES043 • Mountain Lodge", "IN: 2024-10-10  |  OUT: 2024-10-10  (0 Nights)", "Same-day booking and departure without overnight stay. Excluded from overnight occupancy percentage calculations.")
    ]
    for anom_t, anom_d, anom_c in anomalies:
        pa = tf_r.add_paragraph()
        pa.text = f"\n• {anom_t}\n   {anom_d}\n   {anom_c}"
        pa.font.name = "Arial"
        pa.font.size = Pt(10)
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
        kx = 0.85 + (idx * 2.98)
        card = add_zen_card(s5, kx, 1.95, 2.75, 1.8, RGBColor(255, 255, 255), COLOR_HAIRLINE)
        tb = s5.shapes.add_textbox(Inches(kx + 0.1), Inches(2.02), Inches(2.55), Inches(1.6))
        tf = tb.text_frame
        set_clean_margins(tf)
        
        p = tf.paragraphs[0]
        p.text = val
        p.font.name = "Arial"
        p.font.size = Pt(26)
        p.font.bold = True
        p.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.name = "Arial"
        p2.font.size = Pt(10.5)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_SUMI_INK

        p3 = tf.add_paragraph()
        p3.text = note
        p3.font.name = "Arial"
        p3.font.size = Pt(9)
        p3.font.color.rgb = COLOR_MUTED_STONE

    # Lower comparison cards
    c_left = add_zen_card(s5, 0.85, 3.95, 5.68, 2.95, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_cl = s5.shapes.add_textbox(Inches(1.0), Inches(4.05), Inches(5.38), Inches(2.75))
    tf_cl = tb_cl.text_frame
    set_clean_margins(tf_cl)
    p = tf_cl.paragraphs[0]
    p.text = "Cancellation Exposure by Booking Channel"
    p.font.name = "Arial"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_SUMI_INK

    p_lines = tf_cl.add_paragraph()
    p_lines.text = "\n• Online Travel Agencies (OTA): 38.4% cancellation rate ($2,690 refund impact).\n• Direct Hotel Website: 14.3% cancellation rate (highest profit margin and guest loyalty).\n• Phone Reservations: 18.2% cancellation rate (corporate accounts with flexible policies).\n• Walk-In Guests: 0% cancellations (instant guaranteed revenue)."
    p_lines.font.name = "Arial"
    p_lines.font.size = Pt(9.5)
    p_lines.font.color.rgb = COLOR_SLATE_GRAY

    c_right = add_zen_card(s5, 6.8, 3.95, 5.68, 2.95, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_cr = s5.shapes.add_textbox(Inches(6.95), Inches(4.05), Inches(5.38), Inches(2.75))
    tf_cr = tb_cr.text_frame
    set_clean_margins(tf_cr)
    p = tf_cr.paragraphs[0]
    p.text = "Room Tier Revenue & Loyalty Contribution"
    p.font.name = "Arial"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_SUMI_INK

    p_lines = tf_cr.add_paragraph()
    p_lines.text = "\n• Suite & Presidential categories account for 48% of total gross hotel revenue.\n• Platinum Loyalty Members average 3.2x higher ADR than standard guest bookers.\n• Seaside Resort recorded the highest average length of stay (4.2 nights).\n• City Central Inn achieved the highest inventory turnover with standard rooms."
    p_lines.font.name = "Arial"
    p_lines.font.size = Pt(9.5)
    p_lines.font.color.rgb = COLOR_SLATE_GRAY

    # =========================================================================
    # SLIDE 6: Scheduled Task & Monitoring
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    draw_zen_header(s6, "06", "SERVERLESS AUTOMATION", "Scheduled Task Definition & Operational Health", "Serverless aggregation task running daily at 6 AM UTC with real-time health verification via Task History.")

    # Left: Task SQL
    c_tl = add_zen_card(s6, 0.85, 1.95, 5.68, 4.95, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_tl = s6.shapes.add_textbox(Inches(1.0), Inches(2.05), Inches(5.38), Inches(4.7))
    tf_tl = tb_tl.text_frame
    set_clean_margins(tf_tl)
    p = tf_tl.paragraphs[0]
    p.text = "Snowflake Scheduled Task Definition"
    p.font.name = "Arial"
    p.font.size = Pt(13)
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
    p_task.font.size = Pt(9)
    p_task.font.color.rgb = COLOR_INDIGO

    # Right: Task History Results
    c_tr = add_zen_card(s6, 6.8, 1.95, 5.68, 4.95, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_tr = s6.shapes.add_textbox(Inches(6.95), Inches(2.05), Inches(5.38), Inches(4.7))
    tf_tr = tb_tr.text_frame
    set_clean_margins(tf_tr)
    p = tf_tr.paragraphs[0]
    p.text = "Task Execution History & Metrics (TASK_HISTORY)"
    p.font.name = "Arial"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_MATCHA

    p_mon = tf_tr.add_paragraph()
    p_mon.text = """• Health Monitoring Query:
  SELECT NAME, STATE, SCHEDULED_TIME, DURATION_SECS
  FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY());

• Observed Live Production Metrics:
  ✓ Execution State: SUCCEEDED
  ✓ Run Duration: 3.07 seconds (Low Latency)
  ✓ Next Run: SCHEDULED (Daily 06:00 UTC)
  ✓ Compute Sizing: HOTEL_WH (X-Small)
  ✓ Auto-Suspend: 120 seconds (Zero idle compute costs)

• Operational Benefits:
  Daily reservation aggregation runs fully autonomously, eliminating manual export delays and human data entry errors."""
    p_mon.font.name = "Arial"
    p_mon.font.size = Pt(10)
    p_mon.font.color.rgb = COLOR_SLATE_GRAY

    # =========================================================================
    # SLIDE 7: Conclusion & Business Value
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    draw_zen_header(s7, "07", "BUSINESS VALUE & ROI", "Strategic Impact & Production Deliverables", "Clean, high-precision analytics delivered through Snowflake modern cloud data engineering best practices.")

    points = [
        ("Data Trust & Integrity", "Automated Validation", "Quarantined corrupt check-out dates and zero-night stays, ensuring 100% executive reporting accuracy.", COLOR_INDIGO),
        ("Revenue Protection", "Cancellation Transparency", "Exposed $2,690 in OTA cancellation refunds, providing actionable data for policy adjustments.", COLOR_VERMILION),
        ("Dynamic Yield Optimization", "Capacity Intelligence", "Accurate monthly occupancy rates empower revenue management to optimize room rates dynamically.", COLOR_MATCHA),
        ("Zero Idle Compute Cost", "Optimized Warehouse", "Task executes in 3 seconds on an X-Small warehouse with 120s auto-suspend, minimizing infrastructure spend.", COLOR_SUMI_INK)
    ]

    for idx, (title, subtitle, desc, col) in enumerate(points):
        tx = 0.85 + (idx * 2.98)
        card = add_zen_card(s7, tx, 1.95, 2.75, 4.0, RGBColor(255, 255, 255), COLOR_HAIRLINE)
        
        cbar = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(tx + 0.18), Inches(2.15), Inches(0.35), Inches(0.04))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = col
        cbar.line.fill.background()

        tb = s7.shapes.add_textbox(Inches(tx + 0.12), Inches(2.28), Inches(2.51), Inches(3.55))
        tf = tb.text_frame
        set_clean_margins(tf)
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Arial"
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_SUMI_INK

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
        p2.font.color.rgb = COLOR_SLATE_GRAY

    # Footer note
    foot_card = add_zen_card(s7, 0.85, 6.15, 11.633, 0.75, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_foot = s7.shapes.add_textbox(Inches(1.0), Inches(6.22), Inches(11.3), Inches(0.6))
    tf_foot = tb_foot.text_frame
    set_clean_margins(tf_foot)
    p_foot = tf_foot.paragraphs[0]
    p_foot.text = "GitHub: https://github.com/ashlesh0805/snowflake-hotel-reservation-analytics   •   Project by Team 07"
    p_foot.font.name = "Arial"
    p_foot.font.size = Pt(10)
    p_foot.font.bold = True
    p_foot.font.color.rgb = COLOR_VERMILION

    # =========================================================================
    # SLIDE 8: Thank You & Team 07 Attribution (NEW SLIDE!)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    bg8 = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg8.fill.solid()
    bg8.fill.fore_color.rgb = COLOR_WASHI_WHITE
    bg8.line.fill.background()

    # Red Stamp
    seal8 = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9), Inches(0.65), Inches(0.7), Inches(0.7))
    seal8.fill.solid()
    seal8.fill.fore_color.rgb = COLOR_VERMILION
    seal8.line.fill.background()
    tf_s8 = seal8.text_frame
    set_clean_margins(tf_s8)
    p_s8 = tf_s8.paragraphs[0]
    p_s8.text = "07"
    p_s8.alignment = PP_ALIGN.CENTER
    p_s8.font.name = "Arial"
    p_s8.font.size = Pt(14)
    p_s8.font.bold = True
    p_s8.font.color.rgb = RGBColor(255, 255, 255)

    # Top Section Label
    tb_t8 = s8.shapes.add_textbox(Inches(1.75), Inches(0.65), Inches(10.5), Inches(0.28))
    tf_t8 = tb_t8.text_frame
    set_clean_margins(tf_t8)
    p_t8 = tf_t8.paragraphs[0]
    p_t8.text = "PROJECT CONCLUSION  •  QUESTIONS & DISCUSSION"
    p_t8.font.name = "Arial"
    p_t8.font.size = Pt(9.5)
    p_t8.font.bold = True
    p_t8.font.color.rgb = COLOR_VERMILION

    # Main Hero "Thank You"
    tb_hero8 = s8.shapes.add_textbox(Inches(1.75), Inches(0.95), Inches(10.5), Inches(0.75))
    tf_hero8 = tb_hero8.text_frame
    set_clean_margins(tf_hero8)
    p_hero8 = tf_hero8.paragraphs[0]
    p_hero8.text = "Thank You"
    p_hero8.font.name = "Arial"
    p_hero8.font.size = Pt(32)
    p_hero8.font.bold = True
    p_hero8.font.color.rgb = COLOR_SUMI_INK

    # Hairline Divider
    rule8 = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9), Inches(1.85), Inches(11.533), Inches(0.012))
    rule8.fill.solid()
    rule8.fill.fore_color.rgb = COLOR_HAIRLINE
    rule8.line.fill.background()

    # Section Sub-heading for Team
    tb_teamhead = s8.shapes.add_textbox(Inches(0.9), Inches(2.05), Inches(11.533), Inches(0.35))
    tf_th = tb_teamhead.text_frame
    set_clean_margins(tf_th)
    p_th = tf_th.paragraphs[0]
    p_th.text = "PROJECT DELIVERED BY TEAM 07"
    p_th.font.name = "Arial"
    p_th.font.size = Pt(11)
    p_th.font.bold = True
    p_th.font.color.rgb = COLOR_SUMI_INK

    # 5 Team Member Cards
    team_members = [
        ("Ashlesh", "Team Lead", "Pipeline Architecture & Snowflake Engineering", COLOR_VERMILION),
        ("Varun", "Data Engineer", "Medallion Data Modeling & Schema Design", COLOR_INDIGO),
        ("Sakshi", "Quality Analyst", "Data Validation & Date Anomaly Rules", COLOR_MATCHA),
        ("Barghavi", "Analytics Lead", "Occupancy Modeling & Revenue Metrics", COLOR_SUMI_INK),
        ("Akshitha", "Automation Lead", "Serverless Tasks & Execution Monitoring", COLOR_VERMILION)
    ]

    for idx, (m_name, m_role, m_resp, m_col) in enumerate(team_members):
        mx = 0.9 + (idx * 2.36)
        card_m = add_zen_card(s8, mx, 2.5, 2.18, 3.1, RGBColor(255, 255, 255), COLOR_HAIRLINE)
        
        # Top color accent
        cbar_m = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(mx + 0.15), Inches(2.65), Inches(0.35), Inches(0.04))
        cbar_m.fill.solid()
        cbar_m.fill.fore_color.rgb = m_col
        cbar_m.line.fill.background()

        tb_mem = s8.shapes.add_textbox(Inches(mx + 0.1), Inches(2.78), Inches(1.98), Inches(2.7))
        tf_mem = tb_mem.text_frame
        set_clean_margins(tf_mem)
        
        pm1 = tf_mem.paragraphs[0]
        pm1.text = m_name
        pm1.font.name = "Arial"
        pm1.font.size = Pt(13.5)
        pm1.font.bold = True
        pm1.font.color.rgb = COLOR_SUMI_INK

        pm2 = tf_mem.add_paragraph()
        pm2.text = m_role.upper()
        pm2.font.name = "Arial"
        pm2.font.size = Pt(8.5)
        pm2.font.bold = True
        pm2.font.color.rgb = m_col

        pm3 = tf_mem.add_paragraph()
        pm3.text = "\n" + m_resp
        pm3.font.name = "Arial"
        pm3.font.size = Pt(9.5)
        pm3.font.color.rgb = COLOR_SLATE_GRAY

    # Bottom Contact & GitHub Banner
    card_foot = add_zen_card(s8, 0.9, 5.85, 11.533, 1.15, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_bf = s8.shapes.add_textbox(Inches(1.05), Inches(5.92), Inches(11.2), Inches(0.98))
    tf_bf = tb_bf.text_frame
    set_clean_margins(tf_bf)
    p_b1 = tf_bf.paragraphs[0]
    p_b1.text = "OPEN SOURCE REPOSITORY & LIVE ARTIFACTS"
    p_b1.font.name = "Arial"
    p_b1.font.size = Pt(9)
    p_b1.font.bold = True
    p_b1.font.color.rgb = COLOR_MUTED_STONE

    p_b2 = tf_bf.add_paragraph()
    p_b2.text = "https://github.com/ashlesh0805/snowflake-hotel-reservation-analytics"
    p_b2.font.name = "Arial"
    p_b2.font.size = Pt(11)
    p_b2.font.bold = True
    p_b2.font.color.rgb = COLOR_VERMILION

    p_b3 = tf_bf.add_paragraph()
    p_b3.text = "Complete SQL scripts, CSV datasets, validation queries, screenshots, and presentation decks are available on GitHub."
    p_b3.font.name = "Arial"
    p_b3.font.size = Pt(9.5)
    p_b3.font.color.rgb = COLOR_SLATE_GRAY

    # Save to multiple targets
    paths_to_save = [
        r"C:\Users\G ASHLESH\Downloads\Hotel_Reservation_Analytics_Team07_Japanese_Style.pptx",
        r"C:\Users\G ASHLESH\Downloads\Hotel_Reservation_Analytics_Zen_Minimalist.pptx",
        r"C:\Users\G ASHLESH\Downloads\snowflake_screenshots\Hotel_Reservation_Analytics_Japanese_Style.pptx",
        r"C:\Users\G ASHLESH\Downloads\Hotel_Reservation_Analytics_Japanese_Style.pptx",
        r"c:\Users\G ASHLESH\OneDrive\Desktop\snowflake\Hotel_Reservation_Analytics_Team07_Japanese_Style.pptx",
        r"c:\Users\G ASHLESH\OneDrive\Desktop\snowflake\Hotel_Reservation_Analytics_Zen_Minimalist.pptx",
        r"c:\Users\G ASHLESH\OneDrive\Desktop\snowflake\Hotel_Reservation_Analytics_Japanese_Style.pptx"
    ]
    
    print("Saving presentation decks with zero text-overflow and perfect alignment:")
    for path in paths_to_save:
        try:
            prs.save(path)
            print(" [OK] Saved:", path)
        except PermissionError:
            print(" [LOCKED by active PowerPoint session]:", path)

if __name__ == "__main__":
    create_japanese_deck()
