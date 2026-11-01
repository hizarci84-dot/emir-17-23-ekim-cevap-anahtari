# -*- coding: utf-8 -*-
"""
EMİR 1-7 KASIM TARİHLERİ ÜSLÜ SAYILAR ÖDEVLENDİRME
- Maarif_Video_Ders_Kitabi Üslü İfadeler (Sayfa 7-23, özellikle Sayfa 14-16 ve yeni kurgular)
- Günlük 10 soru (her bir test 10 soru) olacak şekilde toplam 6 adet çoktan seçmeli test (60 soru).
- Her soru altında Emir'in rahatça işlem yapabilmesi için geniş çözüm alanı bırakılmıştır.
- Cevap anahtarı PDF sonunda yer almaz (günlük saat 18:00'de e-posta olarak gönderilir).
"""

import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    PageTemplate,
    Frame,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
    NextPageTemplate,
    PageBreak,
    Flowable,
)

from questions_kasim_1_7_data import QUESTIONS_KASIM_1_7, TEST_INFO


def register_turkish_fonts():
    font_dir = "C:/Windows/Fonts"
    candidates = [
        ("Calibri", "calibri.ttf", "calibrib.ttf", "calibrii.ttf"),
        ("Arial", "arial.ttf", "arialbd.ttf", "ariali.ttf"),
        ("SegoeUI", "segoeui.ttf", "segoeuib.ttf", "segoeuii.ttf"),
    ]
    for family, reg, bold, ital in candidates:
        reg_p = os.path.join(font_dir, reg)
        bold_p = os.path.join(font_dir, bold)
        ital_p = os.path.join(font_dir, ital)
        if os.path.exists(reg_p) and os.path.exists(bold_p):
            pdfmetrics.registerFont(TTFont("TRFont", reg_p))
            pdfmetrics.registerFont(TTFont("TRFont-Bold", bold_p))
            if os.path.exists(ital_p):
                pdfmetrics.registerFont(TTFont("TRFont-Italic", ital_p))
            else:
                pdfmetrics.registerFont(TTFont("TRFont-Italic", reg_p))
            return family
    raise RuntimeError("Türkçe destekli TrueType font bulunamadı!")


class DividerLine(Flowable):
    def __init__(self, width, color=colors.HexColor("#CBD5E1")):
        super().__init__()
        self.width = width
        self.height = 4
        self.color = color

    def draw(self):
        self.canv.saveState()
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(0.7)
        self.canv.line(0, 2, self.width, 2)
        self.canv.restoreState()


class WorkspaceLabel(Flowable):
    """Subtle label at the top of the blank student solution workspace."""
    def __init__(self, width):
        super().__init__()
        self.width = width
        self.height = 10

    def draw(self):
        self.canv.saveState()
        self.canv.setFont("TRFont-Italic", 7.3)
        self.canv.setFillColor(colors.HexColor("#94A3B8"))
        self.canv.drawString(2, 2, "Çözüm / İşlem:")
        self.canv.restoreState()


def build_question_flowable(q, styles, col_w):
    q_no = q["no"]
    q_text = q["text"]
    opts = q["options"]

    elements = []

    if q.get("table_data"):
        tdata = q["table_data"]
        n_cols = len(tdata[0])
        cw = (col_w - 10) / n_cols
        formatted_rows = []
        for r_idx, row in enumerate(tdata):
            frow = []
            for cell in row:
                st = styles["TableCellHeader"] if r_idx == 0 else styles["TableCell"]
                frow.append(Paragraph(cell, st))
            formatted_rows.append(frow)
        data_tbl = Table(formatted_rows, colWidths=[cw] * n_cols)
        data_tbl.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E0E7FF")),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F8FAFC")),
                    ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#94A3B8")),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 4),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                    ("TOPPADDING", (0, 0), (-1, -1), 2.5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
                ]
            )
        )
        elements.append(data_tbl)
        elements.append(Spacer(1, 4))

    badge_tag = f"<font color='#1E3A8A'><b>{q_no}.</b></font> "
    q_para = Paragraph(badge_tag + q_text, styles["Question"])
    elements.append(q_para)
    elements.append(Spacer(1, 4))

    max_opt_len = max(len(o[1]) for o in opts)
    if q.get("options_vertical") or max_opt_len > 28:
        opt_rows = [
            [Paragraph(f"<b>{o[0]})</b> {o[1]}", styles["OptionLong"])]
            for o in opts
        ]
        opt_table = Table(opt_rows, colWidths=[col_w - 6])
    else:
        row1 = [
            Paragraph(f"<b>{opts[0][0]})</b> {opts[0][1]}", styles["Option"]),
            Paragraph(f"<b>{opts[1][0]})</b> {opts[1][1]}", styles["Option"]),
            Paragraph(f"<b>{opts[2][0]})</b> {opts[2][1]}", styles["Option"]),
        ]
        row2 = [
            Paragraph(f"<b>{opts[3][0]})</b> {opts[3][1]}", styles["Option"]),
            Paragraph(f"<b>{opts[4][0]})</b> {opts[4][1]}", styles["Option"]),
            Paragraph("", styles["Option"]),
        ]
        c_w = (col_w - 6) / 3.0
        opt_table = Table([row1, row2], colWidths=[c_w, c_w, c_w])

    opt_table.setStyle(
        TableStyle(
            [
                ("LEFTPADDING", (0, 0), (-1, -1), 1),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                ("TOPPADDING", (0, 0), (-1, -1), 1.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    elements.append(opt_table)
    elements.append(Spacer(1, 5))
    elements.append(WorkspaceLabel(col_w - 4))
    # Generous blank workspace for Emir to solve each problem comfortably
    elements.append(Spacer(1, 78))
    elements.append(DividerLine(col_w - 4))
    elements.append(Spacer(1, 8))

    return KeepTogether(elements)


def create_pdf_for_questions(output_path, questions_subset, subtitle_text):
    page_w, page_h = A4
    left_m = 11 * mm
    right_m = 11 * mm
    top_m = 22 * mm
    bottom_m = 13 * mm
    col_gap = 7 * mm

    usable_w = page_w - left_m - right_m
    col_w = (usable_w - col_gap) / 2.0

    first_top_offset = 30 * mm
    first_frame_h = page_h - first_top_offset - bottom_m
    later_frame_h = page_h - top_m - bottom_m

    frame_p1_left = Frame(
        left_m, bottom_m, col_w, first_frame_h, id="F1_L",
        leftPadding=2, rightPadding=2, topPadding=2, bottomPadding=2
    )
    frame_p1_right = Frame(
        left_m + col_w + col_gap, bottom_m, col_w, first_frame_h, id="F1_R",
        leftPadding=2, rightPadding=2, topPadding=2, bottomPadding=2
    )

    frame_pN_left = Frame(
        left_m, bottom_m, col_w, later_frame_h, id="FN_L",
        leftPadding=2, rightPadding=2, topPadding=2, bottomPadding=2
    )
    frame_pN_right = Frame(
        left_m + col_w + col_gap, bottom_m, col_w, later_frame_h, id="FN_R",
        leftPadding=2, rightPadding=2, topPadding=2, bottomPadding=2
    )

    MAIN_TITLE = "EMİR 1-7 KASIM TARİHLERİ ÜSLÜ SAYILAR ÖDEVLENDİRME"

    def draw_first_page(canvas, doc):
        canvas.saveState()
        banner_h = 18 * mm
        banner_y = page_h - 25 * mm
        canvas.setFillColor(colors.HexColor("#1E3A8A"))
        canvas.roundRect(left_m, banner_y, usable_w, banner_h, 5, fill=1, stroke=0)

        canvas.setFillColor(colors.white)
        canvas.setFont("TRFont-Bold", 11.8)
        canvas.drawCentredString(
            page_w / 2.0,
            banner_y + 10.5 * mm,
            MAIN_TITLE,
        )
        canvas.setFont("TRFont", 9.0)
        canvas.setFillColor(colors.HexColor("#DBEAFE"))
        canvas.drawCentredString(
            page_w / 2.0,
            banner_y + 4.0 * mm,
            subtitle_text,
        )

        mid_x = page_w / 2.0
        canvas.setStrokeColor(colors.HexColor("#94A3B8"))
        canvas.setLineWidth(0.6)
        canvas.setDash(3, 3)
        canvas.line(mid_x, bottom_m, mid_x, banner_y - 3 * mm)

        canvas.setDash()
        canvas.setStrokeColor(colors.HexColor("#CBD5E1"))
        canvas.setLineWidth(0.6)
        canvas.line(left_m, bottom_m - 2 * mm, page_w - right_m, bottom_m - 2 * mm)
        canvas.setFillColor(colors.HexColor("#475569"))
        canvas.setFont("TRFont", 8)
        canvas.drawString(left_m, 6 * mm, MAIN_TITLE)
        canvas.setFont("TRFont-Bold", 8.5)
        canvas.drawRightString(page_w - right_m, 6 * mm, f"Sayfa {doc.page}")
        canvas.restoreState()

    def draw_later_page(canvas, doc):
        canvas.saveState()
        header_y = page_h - 15 * mm
        canvas.setFillColor(colors.HexColor("#1E3A8A"))
        canvas.rect(left_m, header_y, usable_w, 7.5 * mm, fill=1, stroke=0)
        canvas.setFillColor(colors.white)
        canvas.setFont("TRFont-Bold", 8.5)
        canvas.drawString(left_m + 3 * mm, header_y + 2.2 * mm, MAIN_TITLE)
        canvas.setFont("TRFont", 8.0)
        canvas.drawRightString(page_w - right_m - 3 * mm, header_y + 2.2 * mm, subtitle_text)

        mid_x = page_w / 2.0
        canvas.setStrokeColor(colors.HexColor("#94A3B8"))
        canvas.setLineWidth(0.6)
        canvas.setDash(3, 3)
        canvas.line(mid_x, bottom_m, mid_x, header_y - 3 * mm)

        canvas.setDash()
        canvas.setStrokeColor(colors.HexColor("#CBD5E1"))
        canvas.setLineWidth(0.6)
        canvas.line(left_m, bottom_m - 2 * mm, page_w - right_m, bottom_m - 2 * mm)
        canvas.setFillColor(colors.HexColor("#475569"))
        canvas.setFont("TRFont", 8)
        canvas.drawString(left_m, 6 * mm, MAIN_TITLE)
        canvas.setFont("TRFont-Bold", 8.5)
        canvas.drawRightString(page_w - right_m, 6 * mm, f"Sayfa {doc.page}")
        canvas.restoreState()

    doc = BaseDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=left_m,
        rightMargin=right_m,
        topMargin=top_m,
        bottomMargin=bottom_m,
        title=MAIN_TITLE,
        author="Antigravity",
    )

    doc.addPageTemplates(
        [
            PageTemplate(
                id="FirstPage",
                frames=[frame_p1_left, frame_p1_right],
                onPage=draw_first_page,
            ),
            PageTemplate(
                id="LaterPages",
                frames=[frame_pN_left, frame_pN_right],
                onPage=draw_later_page,
            ),
        ]
    )

    styles = getSampleStyleSheet()
    q_style = ParagraphStyle(
        "Question",
        parent=styles["Normal"],
        fontName="TRFont",
        fontSize=9.2,
        leading=12.6,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=2,
    )
    opt_style = ParagraphStyle(
        "Option",
        parent=styles["Normal"],
        fontName="TRFont",
        fontSize=8.8,
        leading=11.6,
        textColor=colors.HexColor("#1E293B"),
    )
    opt_long_style = ParagraphStyle(
        "OptionLong",
        parent=styles["Normal"],
        fontName="TRFont",
        fontSize=8.3,
        leading=10.8,
        textColor=colors.HexColor("#1E293B"),
    )
    tbl_hdr_style = ParagraphStyle(
        "TableCellHeader",
        parent=styles["Normal"],
        fontName="TRFont-Bold",
        fontSize=8.0,
        leading=10.2,
        alignment=1,
        textColor=colors.HexColor("#1E3A8A"),
    )
    tbl_cell_style = ParagraphStyle(
        "TableCell",
        parent=styles["Normal"],
        fontName="TRFont",
        fontSize=8.0,
        leading=10.2,
        alignment=1,
        textColor=colors.HexColor("#0F172A"),
    )
    day_banner_style = ParagraphStyle(
        "DayBanner",
        parent=styles["Normal"],
        fontName="TRFont-Bold",
        fontSize=8.8,
        leading=11.5,
        alignment=1,
        textColor=colors.white,
    )

    style_map = {
        "Question": q_style,
        "Option": opt_style,
        "OptionLong": opt_long_style,
        "TableCellHeader": tbl_hdr_style,
        "TableCell": tbl_cell_style,
        "DayBanner": day_banner_style,
    }

    story = [NextPageTemplate("LaterPages")]

    current_day = None
    for idx, q in enumerate(questions_subset):
        if len(questions_subset) > 10 and q["day"] != current_day:
            current_day = q["day"]
            day_title, day_desc = TEST_INFO[current_day]
            if idx > 0:
                story.append(PageBreak())
            banner_p = Paragraph(f"<b>{day_title} — {day_desc}</b>", day_banner_style)
            banner_tbl = Table([[banner_p]], colWidths=[col_w - 4])
            banner_tbl.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#2563EB")),
                        ("TOPPADDING", (0, 0), (-1, -1), 4),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                    ]
                )
            )
            story.append(banner_tbl)
            story.append(Spacer(1, 6))

        story.append(build_question_flowable(q, style_map, col_w))

    doc.build(story)


def main():
    register_turkish_fonts()
    base_dir = os.path.dirname(os.path.abspath(__file__))

    letters = ["A", "B", "C", "D", "E"]
    assert len(QUESTIONS_KASIM_1_7) == 60
    for i, q in enumerate(QUESTIONS_KASIM_1_7, 1):
        assert q["no"] == i
        assert len(q["options"]) == 5
        assert len({o[1] for o in q["options"]}) == 5, f"Duplicate options in Q{i}"
        assert q["answer"] in letters

    for day in range(1, 7):
        day_qs = [q for q in QUESTIONS_KASIM_1_7 if q["day"] == day]
        counts = {L: sum(1 for q in day_qs if q["answer"] == L) for L in letters}
        day_title, day_desc = TEST_INFO[day]
        q_start = day_qs[0]["no"]
        q_end = day_qs[-1]["no"]
        fname = f"EMIR_1-7_KASIM_TEST_{day}_(Sorular_{q_start}-{q_end}).pdf"
        fpath = os.path.join(base_dir, fname)
        create_pdf_for_questions(
            fpath,
            day_qs,
            subtitle_text=f"{day_title} | {day_desc} (10 Soru)",
        )
        print(f"Created Test {day} PDF: {fname} | Dist: {counts}")

    master_fname = "EMIR_1-7_KASIM_USLU_SAYILAR_ODEVLENDIRME.pdf"
    master_fpath = os.path.join(base_dir, master_fname)
    create_pdf_for_questions(
        master_fpath,
        QUESTIONS_KASIM_1_7,
        subtitle_text="6 Adet Çoktan Seçmeli Test (Günlük 10 Soru — Toplam 60 Soru) | Maarif Modeli Üslü İfadeler",
    )
    print(f"Created Master PDF: {master_fname}")

    import fitz
    doc = fitz.open(master_fpath)
    print(f"Master PDF total pages: {len(doc)}")
    for p in [0, 2, 4, len(doc) - 1]:
        doc[p].get_pixmap(dpi=130).save(f"extracted_pages_analysis/preview_kasim_p{p+1}.png")


if __name__ == "__main__":
    main()
