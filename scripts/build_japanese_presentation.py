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

    # Japanese Minimalist Palette
    COLOR_WASHI_WHITE = RGBColor(254, 254, 253) # Rice paper white
    COLOR_CARD_BG = RGBColor(255, 255, 255)
    COLOR_SUMI_INK = RGBColor(24, 24, 27) # Deep sumi ink black
    COLOR_SLATE_GRAY = RGBColor(82, 82, 91) # Soft charcoal
    COLOR_MUTED_STONE = RGBColor(161, 161, 170)
    COLOR_HAIRLINE = RGBColor(228, 228, 231) # Delicate divider
    COLOR_VERMILION = RGBColor(200, 35, 51) # Japanese Cinnabar / Torii Red (朱色)
    COLOR_VERMILION_LIGHT = RGBColor(255, 241, 242)
    COLOR_INDIGO = RGBColor(30, 58, 138) # Aizome Indigo (藍色)
    COLOR_INDIGO_LIGHT = RGBColor(238, 242, 255)
    COLOR_MATCHA = RGBColor(21, 128, 61) # Matcha green
    COLOR_MATCHA_LIGHT = RGBColor(240, 253, 244)

    def draw_japanese_header(slide, kanji_num, category_en, title_ja_en, subtitle_text):
        # Hanko Red Stamp / Seal Box
        stamp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.85), Inches(0.6), Inches(0.65), Inches(0.65))
        stamp.fill.solid()
        stamp.fill.fore_color.rgb = COLOR_VERMILION
        stamp.line.fill.background()
        tf_s = stamp.text_frame
        p_s = tf_s.paragraphs[0]
        p_s.text = kanji_num
        p_s.alignment = PP_ALIGN.CENTER
        p_s.font.name = "Arial"
        p_s.font.size = Pt(14)
        p_s.font.bold = True
        p_s.font.color.rgb = RGBColor(255, 255, 255)

        # Section Category English
        cat_box = slide.shapes.add_textbox(Inches(1.65), Inches(0.55), Inches(10), Inches(0.35))
        tf_c = cat_box.text_frame
        p_c = tf_c.paragraphs[0]
        p_c.text = category_en.upper()
        p_c.font.name = "Arial"
        p_c.font.size = Pt(10)
        p_c.font.bold = True
        p_c.font.color.rgb = COLOR_VERMILION

        # Main Title
        t_box = slide.shapes.add_textbox(Inches(1.65), Inches(0.85), Inches(10.8), Inches(0.65))
        tf_t = t_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title_ja_en
        p_t.font.name = "Arial"
        p_t.font.size = Pt(23)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_SUMI_INK

        # Subtitle
        if subtitle_text:
            sub_box = slide.shapes.add_textbox(Inches(1.65), Inches(1.5), Inches(10.8), Inches(0.45))
            tf_sub = sub_box.text_frame
            tf_sub.word_wrap = True
            p_sub = tf_sub.paragraphs[0]
            p_sub.text = subtitle_text
            p_sub.font.name = "Arial"
            p_sub.font.size = Pt(11.5)
            p_sub.font.color.rgb = COLOR_SLATE_GRAY

        # Delicate horizontal hairline rule
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
    # SLIDE 1: 序 — Title Cover (Japanese Wabi-Sabi & Modern Zen Minimalist)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    
    # Outer elegant framing
    bg = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = COLOR_WASHI_WHITE
    bg.line.fill.background()

    # Red Hanko Seal (Square)
    seal = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.2), Inches(1.2), Inches(1.1), Inches(1.1))
    seal.fill.solid()
    seal.fill.fore_color.rgb = COLOR_VERMILION
    seal.line.fill.background()
    tf_seal = seal.text_frame
    p_seal = tf_seal.paragraphs[0]
    p_seal.text = "雪花\n分析" # "Snowflake Analytics" in Kanji
    p_seal.alignment = PP_ALIGN.CENTER
    p_seal.font.name = "Arial"
    p_seal.font.size = Pt(13)
    p_seal.font.bold = True
    p_seal.font.color.rgb = RGBColor(255, 255, 255)

    # Vertical Zen Line next to title
    vline = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(2.6), Inches(1.2), Inches(0.03), Inches(1.1))
    vline.fill.solid()
    vline.fill.fore_color.rgb = COLOR_HAIRLINE
    vline.line.fill.background()

    # English Category
    tb_c = s1.shapes.add_textbox(Inches(2.8), Inches(1.15), Inches(9.0), Inches(0.35))
    tf_c = tb_c.text_frame
    p_c = tf_c.paragraphs[0]
    p_c.text = "SNOWFLAKE CLOUD DATA WAREHOUSE • ホテル分析"
    p_c.font.name = "Arial"
    p_c.font.size = Pt(11)
    p_c.font.bold = True
    p_c.font.color.rgb = COLOR_VERMILION

    # Main Japanese Sub-header
    tb_j = s1.shapes.add_textbox(Inches(2.8), Inches(1.5), Inches(9.0), Inches(0.45))
    tf_j = tb_j.text_frame
    p_j = tf_j.paragraphs[0]
    p_j.text = "ホテル予約・客室稼働率データ分析基盤"
    p_j.font.name = "Arial"
    p_j.font.size = Pt(16)
    p_j.font.bold = True
    p_j.font.color.rgb = COLOR_SUMI_INK

    # Main Hero Heading (Clean Sumi Black)
    tb_title = s1.shapes.add_textbox(Inches(1.15), Inches(2.7), Inches(11.0), Inches(1.6))
    tf_t = tb_title.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "Hotel Reservation & Occupancy\nAnalytics System"
    p_t.font.name = "Arial"
    p_t.font.size = Pt(38)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_SUMI_INK

    # Philosophy Sub-caption
    tb_sub = s1.shapes.add_textbox(Inches(1.2), Inches(4.5), Inches(10.5), Inches(0.8))
    tf_sub = tb_sub.text_frame
    tf_sub.word_wrap = True
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = "A minimalist, high-precision cloud analytics architecture designed for multi-property hotel chains: Automated Ingestion • Date Integrity • Dynamic Occupancy • Serverless Tasks."
    p_sub.font.name = "Arial"
    p_sub.font.size = Pt(13)
    p_sub.font.color.rgb = COLOR_SLATE_GRAY

    # Bottom 4 Minimalist Data Pills
    meta_pills = [
        ("一", "WAREHOUSE", "HOTEL_WH (X-Small)", COLOR_SUMI_INK),
        ("二", "DATABASE", "HOTEL_RESERVATION_DB", COLOR_INDIGO),
        ("三", "PIPELINE", "Tasks • CRON 6 AM UTC", COLOR_VERMILION),
        ("四", "AUTHOR", "Ashlesh Gurram", COLOR_SLATE_GRAY)
    ]
    for idx, (kanji, m_lbl, m_val, m_col) in enumerate(meta_pills):
        px = 1.2 + (idx * 2.75)
        card = add_zen_card(s1, px, 5.5, 2.55, 1.2, RGBColor(255, 255, 255), COLOR_HAIRLINE)
        
        tb_m = s1.shapes.add_textbox(Inches(px + 0.15), Inches(5.6), Inches(2.25), Inches(1.0))
        tf_m = tb_m.text_frame
        p1 = tf_m.paragraphs[0]
        p1.text = f"{kanji} • {m_lbl}"
        p1.font.name = "Arial"
        p1.font.size = Pt(9.5)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_MUTED_STONE
        
        p2 = tf_m.add_paragraph()
        p2.text = m_val
        p2.font.name = "Arial"
        p2.font.size = Pt(11.5)
        p2.font.bold = True
        p2.font.color.rgb = m_col

    # =========================================================================
    # SLIDE 2: 課題 — Challenges & Business Problem
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    draw_japanese_header(s2, "課題", "PROBLEM STATEMENT", "Core Operational Challenges / 主要な事業課題", "Fragmented booking sources introduced corrupt dates, unmonitored cancellation exposure, and inaccurate occupancy metrics.")

    cards_s2 = [
        ("01", "不正な予約日程の混入", "Anomalous Date Corruptions", "Guests and third-party OTAs frequently feed checkout dates prior to checkin or zero-day stays, contaminating length-of-stay metrics.", COLOR_VERMILION),
        ("02", "キャンセル損失の不可視化", "Untracked Cancellation Exposure", "Sudden cancellation spikes through indirect channels caused unmonitored revenue leakage without clear visibility into refund volumes.", COLOR_INDIGO),
        ("03", "稼働率算出の複雑性", "Dynamic Occupancy Modeling", "Reconciling active room capacity against fluctuating days in calendar months while excluding cancelled bookings required dynamic modeling.", COLOR_SLATE_GRAY),
        ("04", "手作業による集計の限界", "Manual Batch Vulnerability", "Relying on end-of-month manual spreadsheet exports lacked automated scheduling, versioned time-travel, and operational health monitoring.", COLOR_MATCHA)
    ]

    for idx, (num, title_ja, title_en, desc, col) in enumerate(cards_s2):
        col_idx = idx % 2
        row_idx = idx // 2
        cx = 0.85 + (col_idx * 5.9)
        cy = 2.3 + (row_idx * 2.35)
        card = add_zen_card(s2, cx, cy, 5.7, 2.15, RGBColor(255, 255, 255), COLOR_HAIRLINE)
        
        # Red subtle number tag
        t_box = s2.shapes.add_textbox(Inches(cx + 0.2), Inches(cy + 0.15), Inches(5.3), Inches(1.8))
        tf = t_box.text_frame
        tf.word_wrap = True
        
        p1 = tf.paragraphs[0]
        p1.text = f"{num}  {title_ja}"
        p1.font.name = "Arial"
        p1.font.size = Pt(13.5)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_SUMI_INK
        
        p_en = tf.add_paragraph()
        p_en.text = title_en.upper()
        p_en.font.name = "Arial"
        p_en.font.size = Pt(9.5)
        p_en.font.bold = True
        p_en.font.color.rgb = col

        p_desc = tf.add_paragraph()
        p_desc.text = "\n" + desc
        p_desc.font.name = "Arial"
        p_desc.font.size = Pt(11)
        p_desc.font.color.rgb = COLOR_SLATE_GRAY

    # =========================================================================
    # SLIDE 3: 構造 — Medallion Architecture
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    draw_japanese_header(s3, "構造", "DATA ARCHITECTURE", "Layered Medallion Architecture / 3層データ基盤設計", "Separation of raw landing files, business validation, and executive analytics consumption.")

    layers = [
        ("RAW (生データ層)", "BRONZE LANDING ZONE", "• S3 External Stage (@HOTEL_S3_STAGE)\n• CSV_FORMAT with header skip\n• RAW_GUESTS (20 rows)\n• RAW_ROOMS (25 rooms)\n• RAW_RESERVATIONS (43 rows)\n• RAW_PAYMENTS (43 transactions)", COLOR_INDIGO, COLOR_INDIGO_LIGHT),
        ("CLEAN (検証・洗練層)", "SILVER VALIDATION LAYER", "• V_RESERVATION_DATE_VALIDATION\n• Automatically isolates RES041-043\n• CLEAN_RESERVATIONS (40 rows)\n• V_CANCELLED_RESERVATIONS\n• Tracks 8 cancellations ($5,290 refund)\n• Cleaned guest profiles", COLOR_VERMILION, COLOR_VERMILION_LIGHT),
        ("ANALYTICS (分析・集計層)", "GOLD CONSUMPTION LAYER", "• FACT_RESERVATION_ANALYTICS\n• V_MONTHLY_OCCUPANCY (%)\n• V_REVENUE_BY_HOTEL (Net Rev)\n• V_REVENUE_BY_ROOM_TYPE (ADR)\n• DAILY_RESERVATION_SUMMARY\n• Automated Daily Task (CRON 6 AM)", COLOR_MATCHA, COLOR_MATCHA_LIGHT)
    ]

    for idx, (title_ja, title_en, desc, col, bg_col) in enumerate(layers):
        lx = 0.85 + (idx * 3.9)
        card = add_zen_card(s3, lx, 2.3, 3.8, 4.6, bg_col, COLOR_HAIRLINE)
        
        # Red/Indigo accent pill
        tb = s3.shapes.add_textbox(Inches(lx + 0.2), Inches(2.5), Inches(3.4), Inches(4.2))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p1 = tf.paragraphs[0]
        p1.text = title_ja
        p1.font.name = "Arial"
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_SUMI_INK

        p2 = tf.add_paragraph()
        p2.text = title_en
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
    # SLIDE 4: 品質 — Date Validation Logic
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    draw_japanese_header(s4, "品質", "DATA QUALITY & VALIDATION", "Reservation Date Validation Logic / 日付検証と異常検知", "Automated rules detect negative stay durations and zero-night anomalies before loading to production.")

    # Left: Code Card
    card_l = add_zen_card(s4, 0.85, 2.3, 5.7, 4.6, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_l = s4.shapes.add_textbox(Inches(1.05), Inches(2.45), Inches(5.3), Inches(4.3))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    p.text = "検証ロジック (Validation SQL Rules)"
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
    p.text = "検知された異常データ (3件除外)"
    p.font.name = "Arial"
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_VERMILION

    anomalies = [
        ("RES041 • グランドパレスホテル", "IN: 2024-11-15 / OUT: 2024-11-10 (-5日)", "チェックアウトがチェックインより5日前の異常レコード。検証ビューで即時検知しCLEAN層から除外。"),
        ("RES042 • シーサイドリゾート", "IN: 2024-12-25 / OUT: 2024-12-20 (-5日)", "OTA経由の不正日程予約。客室供給日数および売上集計への汚染を防止。"),
        ("RES043 • マウンテンロッジ", "IN: 2024-10-10 / OUT: 2024-10-10 (0泊)", "同日チェックイン・アウトの宿泊日数ゼロ。宿泊稼働率の計算対象から除外。")
    ]
    for anom_t, anom_d, anom_c in anomalies:
        pa = tf_r.add_paragraph()
        pa.text = f"\n• {anom_t}\n   {anom_d}\n   {anom_c}"
        pa.font.name = "Arial"
        pa.font.size = Pt(10.5)
        pa.font.color.rgb = COLOR_SLATE_GRAY

    # =========================================================================
    # SLIDE 5: 実績 — Executive Metrics & Findings
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    draw_japanese_header(s5, "実績", "EXECUTIVE METRICS", "Key Analytical Findings / 主要分析実績", "Verified metrics from FACT_RESERVATION_ANALYTICS: Revenue, Occupancy, and Channel Conversion.")

    kpis = [
        ("40件", "有効予約数 (Valid Bookings)", "43件の生データから3件の異常を除外", COLOR_INDIGO),
        ("$46,880", "純売上実績 (Net Revenue)", "完了支払総額より返金$5,290を控除", COLOR_MATCHA),
        ("8件 (20%)", "キャンセル率 (Cancellation Rate)", "OTA経由が最多($2,690の返金インパクト)", COLOR_VERMILION),
        ("58.1%", "最高稼働率 (Peak Occupancy)", "シーサイドリゾートが秋季稼働率を牽引", COLOR_SUMI_INK)
    ]

    for idx, (val, title_ja, note, col) in enumerate(kpis):
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
        p2.text = title_ja
        p2.font.name = "Arial"
        p2.font.size = Pt(10.5)
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
    p.text = "予約チャネル別キャンセル率の傾向"
    p.font.name = "Arial"
    p.font.size = Pt(12.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_SUMI_INK

    p_lines = tf_cl.add_paragraph()
    p_lines.text = "• オンライン旅行会社 (OTA): キャンセル率38.4% (事前決済・キャンセル料規約の導入が必要)\n• 公式Web予約: キャンセル率14.3% (最も高い利益率と安定的転換率)\n• 電話予約: キャンセル率18.2% (法人リピート顧客が中心)\n• 当日来店 (Walk-In): キャンセル率0% (確実な売上確保)"
    p_lines.font.name = "Arial"
    p_lines.font.size = Pt(10)
    p_lines.font.color.rgb = COLOR_SLATE_GRAY

    c_right = add_zen_card(s5, 6.75, 4.35, 5.733, 2.5, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_cr = s5.shapes.add_textbox(Inches(6.95), Inches(4.45), Inches(5.33), Inches(2.2))
    tf_cr = tb_cr.text_frame
    tf_cr.word_wrap = True
    p = tf_cr.paragraphs[0]
    p.text = "客室タイプとロイヤルティ会員の貢献"
    p.font.name = "Arial"
    p.font.size = Pt(12.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_SUMI_INK

    p_lines = tf_cr.add_paragraph()
    p_lines.text = "• スイート・プレジデンシャル客室がホテル総売上の48%を創出。\n• プラチナ会員の平均客室単価(ADR)は一般顧客の3.2倍。\n• シーサイドリゾート: 最長の平均滞在日数 (4.2泊) を達成。\n• シティセントラルイン: スタンダード客室の回転率が最も高い。"
    p_lines.font.name = "Arial"
    p_lines.font.size = Pt(10)
    p_lines.font.color.rgb = COLOR_SLATE_GRAY

    # =========================================================================
    # SLIDE 6: 自動化 — Scheduled Task & Monitoring
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    draw_japanese_header(s6, "自動化", "SERVERLESS AUTOMATION", "Scheduled Task & Operational Health / 自動集計タスク", "Serverless aggregation task running daily at 6 AM UTC with real-time health verification via Task History.")

    # Left: Task SQL
    c_tl = add_zen_card(s6, 0.85, 2.3, 5.7, 4.6, RGBColor(255, 255, 255), COLOR_HAIRLINE)
    tb_tl = s6.shapes.add_textbox(Inches(1.05), Inches(2.45), Inches(5.3), Inches(4.3))
    tf_tl = tb_tl.text_frame
    tf_tl.word_wrap = True
    p = tf_tl.paragraphs[0]
    p.text = "定期集計タスク定義 (Scheduled Task)"
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
    p.text = "タスク履歴と稼働実績 (TASK_HISTORY)"
    p.font.name = "Arial"
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_MATCHA

    p_mon = tf_tr.add_paragraph()
    p_mon.text = """• 監視クエリ (Monitoring Query):
  SELECT NAME, STATE, SCHEDULED_TIME, DURATION_SECS
  FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY());

• 実測稼働実績 (Observed Metrics):
  ✓ 実行ステータス: SUCCEEDED (正常完了)
  ✓ 実行所要時間: 3.07秒 (低レイテンシ)
  ✓ 次回スケジュール: SCHEDULED (毎日UTC 06:00)
  ✓ コンピュート: HOTEL_WH (X-Small)
  ✓ 自動サスペンド: 120秒 (アイドルコスト完全排除)

• 運用上のメリット:
  日次集計が完全自動化され、手動トリガーの負担と人為的ミスをゼロに削減。"""
    p_mon.font.name = "Arial"
    p_mon.font.size = Pt(10.5)
    p_mon.font.color.rgb = COLOR_SLATE_GRAY

    # =========================================================================
    # SLIDE 7: 結び — Conclusion & ROI
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    draw_japanese_header(s7, "結び", "BUSINESS VALUE & ROI", "Summary, Business Impact & Next Steps / まとめと事業価値", "Clean, high-precision analytics delivered through Snowflake modern data cloud best practices.")

    points = [
        ("完全なデータ信頼性", "Data Trust", "チェックアウト異常日程やゼロ泊の混入を即時遮断し、財務レポートの完全性を保証。", COLOR_INDIGO),
        ("キャンセル損失の抑制", "Refund Control", "OTA経由の返金インパクト($2,690)を可視化し、返金不可プラン等の規約改定を支援。", COLOR_VERMILION),
        ("客室稼働の最適化", "Dynamic Yield", "各ホテルの余剰客室および高収益スイートルームの稼働実態をリアルタイムに把握。", COLOR_MATCHA),
        ("クラウド費用の極小化", "Zero Idle Cost", "タスク実行時間3秒、ウェアハウス自動停止により、月額インフラ費用を最小限に抑制。", COLOR_SUMI_INK)
    ]

    for idx, (t_ja, t_en, t_desc, col) in enumerate(points):
        tx = 0.85 + (idx * 2.9)
        card = add_zen_card(s7, tx, 2.3, 2.8, 3.7, RGBColor(255, 255, 255), COLOR_HAIRLINE)
        
        # Red/Color accent line
        cbar = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(tx + 0.2), Inches(2.5), Inches(0.35), Inches(0.04))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = col
        cbar.line.fill.background()

        tb = s7.shapes.add_textbox(Inches(tx + 0.15), Inches(2.65), Inches(2.5), Inches(3.1))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = t_ja
        p.font.name = "Arial"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = COLOR_SUMI_INK

        p_sub = tf.add_paragraph()
        p_sub.text = t_en.upper()
        p_sub.font.name = "Arial"
        p_sub.font.size = Pt(9)
        p_sub.font.bold = True
        p_sub.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = "\n" + t_desc
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

    out_downloads = r"C:\Users\G ASHLESH\Downloads\snowflake_screenshots\Hotel_Reservation_Analytics_Japanese_Style.pptx"
    out_repo = r"c:\Users\G ASHLESH\OneDrive\Desktop\snowflake\Hotel_Reservation_Analytics_Japanese_Style.pptx"
    prs.save(out_downloads)
    prs.save(out_repo)
    print("Japanese Style Presentation saved to:")
    print(" -", out_downloads)
    print(" -", out_repo)

if __name__ == "__main__":
    create_japanese_deck()
