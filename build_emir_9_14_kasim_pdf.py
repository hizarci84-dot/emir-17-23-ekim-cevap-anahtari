# -*- coding: utf-8 -*-
"""
9-14 KASIM ARASI MÜFİT HOCANIN KÖKLÜ İFADELER ÖDEVİ
- Maarif_Video_Ders_Kitabi Köklü İfadeler Bölümü (Sayfa 22-27 | Örnek 1 - Örnek 31)
- Günlük 10 soru olacak şekilde toplam 6 adet çoktan seçmeli test (60 soru).
- Gerçek köklü ifade mathtext dizgisi + bağlamlı sorular için vektör çizimler.
- Her soru altında Emir'in rahatça işlem yapabilmesi için geniş çözüm alanı bırakılmıştır.
- Cevap anahtarı PDF sonunda yer almaz (günlük saat 18:00'de e-posta olarak gönderilir).
"""

import hashlib
import math
import os
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.mathtext import MathTextParser, math_to_image
from PIL import Image as PILImage

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import (
    Drawing,
    Rect,
    Line,
    Circle,
    Polygon,
    String,
    Group,
    Wedge,
)
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
    Image,
)

from questions_kasim_9_14_data import QUESTIONS_KASIM_9_14, TEST_INFO


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MATH_CACHE_DIR = os.path.join(BASE_DIR, "extracted_pages_analysis", "math_cache_kasim9_14")
os.makedirs(MATH_CACHE_DIR, exist_ok=True)

plt.rcParams["mathtext.fontset"] = "dejavusans"
_MATH_PARSER = MathTextParser("agg")


def register_turkish_fonts():
    font_dir = "C:/Windows/Fonts"
    candidates = [
        ("Calibri", "calibri.ttf", "calibrib.ttf", "calibrii.ttf"),
        ("Arial", "arial.ttf", "arialbd.ttf", "ariali.ttf"),
        ("SegoeUI", "segoeui.ttf", "segoeuib.ttf", "segoeuii.ttf"),
    ]
    chosen = None
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
            chosen = family
            break
    if not chosen:
        raise RuntimeError("Türkçe destekli TrueType font bulunamadı!")

    sym_p = os.path.join(font_dir, "seguisym.ttf")
    if os.path.exists(sym_p):
        pdfmetrics.registerFont(TTFont("SymFont", sym_p))
    else:
        pdfmetrics.registerFont(TTFont("SymFont", os.path.join(font_dir, "calibri.ttf")))
    return chosen


def _compile_math_image(latex_inner: str, font_size: float) -> tuple[str, float, float, float]:
    """Render $latex_inner$ at 300 DPI and return (png_path, w_pt, h_pt, valign_pt)."""
    dpi = 300
    full = f"${latex_inner}$"
    key = hashlib.md5(f"{latex_inner}|{font_size}".encode("utf-8")).hexdigest()
    path = os.path.join(MATH_CACHE_DIR, f"{key}.png")
    prop = matplotlib.font_manager.FontProperties(size=font_size)
    _, _, _, _, depth, _ = _MATH_PARSER.parse(full, dpi=dpi, prop=prop)
    if not os.path.exists(path):
        math_to_image(full, path, prop=prop, dpi=dpi, format="png")
    with PILImage.open(path) as im:
        w_px, h_px = im.size
    scale = 72.0 / dpi
    w_pt = w_px * scale
    h_pt = h_px * scale
    valign = -depth * scale
    return path, w_pt, h_pt, valign


def _wrap_symbols(text_chunk: str) -> str:
    """Wrap special geometric/math Unicode symbols cleanly with SymFont."""
    return re.sub(
        r"([□△★✓✗∈∉≤≥≠])",
        r'<font name="SymFont">\1</font>',
        text_chunk,
    )


def render_inline_math(text: str, font_size: float = 9.0) -> str:
    """Replace inline $...$ spans with baseline-aligned <img> tags and wrap Unicode symbols."""
    parts = []
    pos = 0
    for m in re.finditer(r"\$(.+?)\$", text):
        before = text[pos : m.start()]
        if before:
            parts.append(_wrap_symbols(before))
        expr = m.group(1)
        path, w_pt, h_pt, valign = _compile_math_image(expr, font_size)
        parts.append(
            f'<img src="{path}" width="{w_pt:.2f}" height="{h_pt:.2f}" valign="{valign:.2f}"/>'
        )
        pos = m.end()
    tail = text[pos:]
    if tail:
        parts.append(_wrap_symbols(tail))
    return "".join(parts)


def split_question_segments(raw_text: str, font_size: float = 9.0) -> list[tuple[str, str]]:
    """
    Split raw question text into ('para', html) and ('display_math', expr) blocks
    so $$...$$ stacked fractions get their own centered line without colliding vertically.
    """
    segments = []
    pos = 0
    for m in re.finditer(r"\$\$(.+?)\$\$", raw_text, flags=re.DOTALL):
        before = raw_text[pos : m.start()].strip()
        if before:
            before = re.sub(r"^(<br/>)+|(<br/>)+$", "", before).strip()
            if before:
                segments.append(("para", render_inline_math(before, font_size)))
        segments.append(("display_math", m.group(1).strip()))
        pos = m.end()
    after = raw_text[pos:].strip()
    if after:
        after = re.sub(r"^(<br/>)+|(<br/>)+$", "", after).strip()
        if after:
            segments.append(("para", render_inline_math(after, font_size)))
    return segments


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


def _draw_radical(d: Drawing, x: float, y: float, idx_sym: str, inside: str, sym_color=colors.white):
    """Draw a crisp vector nth-root sign + vinculum bar on a Drawing."""
    # Symbol index top-left
    d.add(String(x, y + 8, idx_sym, fontName="SymFont", fontSize=7.2, fillColor=sym_color))
    # Radical check mark + bar
    rx = x + 6
    d.add(Line(rx, y + 3, rx + 2.5, y - 1, strokeColor=sym_color, strokeWidth=1.0))
    d.add(Line(rx + 2.5, y - 1, rx + 5.5, y + 11, strokeColor=sym_color, strokeWidth=1.0))
    bar_w = max(22, len(inside) * 4.9 + 4)
    d.add(Line(rx + 5.5, y + 11, rx + 5.5 + bar_w, y + 11, strokeColor=sym_color, strokeWidth=1.0))
    d.add(String(rx + 7.5, y + 1.5, inside, fontName="TRFont-Bold", fontSize=8.5, fillColor=sym_color))


def build_diagram_flowable(diagram_name: str, col_w: float) -> Drawing:
    w = min(col_w - 8, 232)

    if diagram_name == "board_symbols":
        h = 54
        d = Drawing(w, h)
        # Wooden frame & dark green chalkboard
        d.add(Rect(6, 2, w - 12, h - 4, fillColor=colors.HexColor("#78350F"), strokeColor=colors.HexColor("#451A03"), strokeWidth=1.2, rx=4, ry=4))
        d.add(Rect(10, 6, w - 20, h - 12, fillColor=colors.HexColor("#14532D"), strokeColor=colors.HexColor("#166534"), strokeWidth=0.8, rx=2, ry=2))
        _draw_radical(d, 22, 26, "□", "-27", colors.white)
        _draw_radical(d, 90, 26, "△", "(-3)²", colors.HexColor("#FEF08A"))
        _draw_radical(d, 160, 26, "★", "(-2⁴)", colors.HexColor("#BAE6FD"))
        d.add(String(w / 2.0, 9, "Matematik Tahtası", fontName="TRFont-Italic", fontSize=6.8, fillColor=colors.HexColor("#BBF7D0"), textAnchor="middle"))
        return d

    if diagram_name == "number_line_klm":
        h = 40
        d = Drawing(w, h)
        y_line = 17
        x0, x1 = 14, w - 14
        d.add(Line(x0, y_line, x1, y_line, strokeColor=colors.HexColor("#1E293B"), strokeWidth=1.2))
        # Arrowheads
        d.add(Polygon([x0 - 4, y_line, x0 + 2, y_line + 2.5, x0 + 2, y_line - 2.5], fillColor=colors.HexColor("#1E293B"), strokeWidth=0))
        d.add(Polygon([x1 + 4, y_line, x1 - 2, y_line + 2.5, x1 - 2, y_line - 2.5], fillColor=colors.HexColor("#1E293B"), strokeWidth=0))
        # Integers 0 to 8
        step = (x1 - x0 - 16) / 8.0
        start_x = x0 + 8
        for n in range(9):
            tx = start_x + n * step
            d.add(Line(tx, y_line - 3, tx, y_line + 3, strokeColor=colors.HexColor("#334155"), strokeWidth=0.9))
            d.add(String(tx, y_line - 12, str(n), fontName="TRFont-Bold", fontSize=7.5, fillColor=colors.HexColor("#0F172A"), textAnchor="middle"))
        # Points K (2.67), L (4.85), M (6.7)
        for lbl, val, clr in [("K", 2.67, "#DC2626"), ("L", 4.88, "#2563EB"), ("M", 6.72, "#059669")]:
            px = start_x + val * step
            d.add(Circle(px, y_line, 2.7, fillColor=colors.HexColor(clr), strokeColor=colors.white, strokeWidth=0.6))
            d.add(String(px, y_line + 6.5, lbl, fontName="TRFont-Bold", fontSize=8.5, fillColor=colors.HexColor(clr), textAnchor="middle"))
        return d

    if diagram_name == "corner_cafe_kutuphane":
        h = 74
        d = Drawing(w, h)
        # Background plaza
        px, py, pw, ph = 34, 4, w - 42, h - 22
        d.add(Rect(px, py, pw, ph, fillColor=colors.HexColor("#F1F5F9"), strokeColor=colors.HexColor("#64748B"), strokeWidth=1.0))
        # KÜTÜPHANE along top
        d.add(Rect(px, py + ph, pw, 14, fillColor=colors.HexColor("#FBCFE8"), strokeColor=colors.HexColor("#9D174D"), strokeWidth=0.9))
        d.add(String(px + pw / 2.0, py + ph + 4, "K Ü T Ü P H A N E", fontName="TRFont-Bold", fontSize=7.8, fillColor=colors.HexColor("#831843"), textAnchor="middle"))
        # KAFE along left
        d.add(Rect(10, py, 24, ph, fillColor=colors.HexColor("#BBF7D0"), strokeColor=colors.HexColor("#166534"), strokeWidth=0.9))
        for idx, ch in enumerate(["K", "A", "F", "E"]):
            d.add(String(22, py + ph - 11 - idx * 11, ch, fontName="TRFont-Bold", fontSize=7.4, fillColor=colors.HexColor("#14532D"), textAnchor="middle"))
        # Dashed yellow curb along top & left of plaza
        d.add(Line(px + 2, py + ph - 2, px + pw - 2, py + ph - 2, strokeColor=colors.HexColor("#D97706"), strokeWidth=1.3, strokeDashArray=[4, 3]))
        d.add(Line(px + 2, py + 2, px + 2, py + ph - 2, strokeColor=colors.HexColor("#D97706"), strokeWidth=1.3, strokeDashArray=[4, 3]))
        # Three people:
        # Left girl/boy (Efe): middle distance from TOP, closest to LEFT (x=px+22, y=py+25 -> 25 from bottom, 27 from top)
        # Bottom-center (Mert): farthest from TOP, middle from LEFT (x=px+pw*0.48, y=py+9 -> bottom! 43 from top)
        # Top-right (Kaan): closest to TOP, farthest from LEFT (x=px+pw*0.80, y=py+ph-12 -> 12 from top!)
        def draw_person(cx, cy, clr):
            d.add(Circle(cx, cy + 7.5, 3.0, fillColor=colors.HexColor(clr), strokeWidth=0))
            d.add(Rect(cx - 2.6, cy - 1, 5.2, 6.2, fillColor=colors.HexColor(clr), strokeWidth=0, rx=1.5, ry=1.5))

        draw_person(px + 24, py + ph - 26, "#2563EB")       # Efe (leftmost, mid height)
        draw_person(px + pw * 0.48, py + 9, "#0F172A")      # Mert (center x, lowest/farthest top)
        draw_person(px + pw * 0.80, py + ph - 13, "#DC2626") # Kaan (rightmost, highest/closest top)
        return d

    if diagram_name == "gauge_bar":
        h = 62
        d = Drawing(w, h)
        cx, cy = w / 2.0, 12
        r_out = 33
        # Semicircle dial
        d.add(Wedge(cx, cy, r_out, 0, 180, fillColor=colors.HexColor("#EFF6FF"), strokeColor=colors.HexColor("#1E3A8A"), strokeWidth=1.4))
        d.add(Wedge(cx, cy, r_out - 7, 0, 180, fillColor=colors.white, strokeColor=colors.HexColor("#93C5FD"), strokeWidth=0.8))
        # Ticks inside outer ring, numbers clearly outside the arc so needle never overlaps digits
        for v in [0, 2, 4, 6, 8, 10, 12]:
            ang = math.radians(180 - v * 15)
            x_in = cx + (r_out - 7) * math.cos(ang)
            y_in = cy + (r_out - 7) * math.sin(ang)
            x_out = cx + r_out * math.cos(ang)
            y_out = cy + r_out * math.sin(ang)
            d.add(Line(x_in, y_in, x_out, y_out, strokeColor=colors.HexColor("#1E3A8A"), strokeWidth=1.0))
            tx = cx + (r_out + 7.5) * math.cos(ang)
            ty = cy + (r_out + 7.5) * math.sin(ang) - 2.2
            d.add(String(tx, ty, str(v), fontName="TRFont-Bold", fontSize=7.0, fillColor=colors.HexColor("#0F172A"), textAnchor="middle"))
        # Needle pointing sharply to 8 (stops inside the white ring)
        n_ang = math.radians(60)
        d.add(Line(cx, cy, cx + (r_out - 4) * math.cos(n_ang), cy + (r_out - 4) * math.sin(n_ang), strokeColor=colors.HexColor("#DC2626"), strokeWidth=1.8))
        d.add(Circle(cx, cy, 3.0, fillColor=colors.HexColor("#1E293B"), strokeWidth=0))
        d.add(String(cx, 1.5, "Örnek Gösterge (Gerçek basınç = 32 bar)", fontName="TRFont-Italic", fontSize=6.8, fillColor=colors.HexColor("#475569"), textAnchor="middle"))
        return d

    if diagram_name == "lined_notebook":
        h = 74
        d = Drawing(w, h)
        box_w = (w - 18) / 2.0
        for b_idx, bx in enumerate([4, 4 + box_w + 10]):
            d.add(Rect(bx, 9, box_w, h - 13, fillColor=colors.white, strokeColor=colors.HexColor("#475569"), strokeWidth=0.9))
            # 7 horizontal parallel blue lines with ample margin above & below border
            dy = 7.2
            base_y = 14.5
            for k in range(7):
                ly = base_y + k * dy
                d.add(Line(bx + 1, ly, bx + box_w - 1, ly, strokeColor=colors.HexColor("#93C5FD"), strokeWidth=0.75))
            if b_idx == 0:
                rx = bx + box_w * 0.36
                rw = box_w * 0.28
                ry = base_y + 1 * dy
                rh = 4.55 * dy  # strictly > 4 intervals and < 5 intervals
                d.add(Rect(rx, ry, rw, rh, fillColor=colors.HexColor("#0284C7"), strokeColor=colors.HexColor("#0F172A"), strokeWidth=0.8))
                d.add(String(bx + box_w / 2.0, 1.5, "1. Görünüm (Dikey)", fontName="TRFont-Italic", fontSize=6.5, fillColor=colors.HexColor("#475569"), textAnchor="middle"))
            else:
                rx = bx + box_w * 0.14
                rw = box_w * 0.72
                ry = base_y + 2 * dy
                rh = 1.42 * dy  # strictly > 1 interval and < 2 intervals
                d.add(Rect(rx, ry, rw, rh, fillColor=colors.HexColor("#0284C7"), strokeColor=colors.HexColor("#0F172A"), strokeWidth=0.8))
                d.add(String(bx + box_w / 2.0, 1.5, "2. Görünüm (Yatay)", fontName="TRFont-Italic", fontSize=6.5, fillColor=colors.HexColor("#475569"), textAnchor="middle"))
        return d

    if diagram_name == "road_lanes":
        h = 48
        d = Drawing(w, h)
        x0, x1 = 10, w - 10
        span = x1 - x0
        def kx(km):
            return x0 + (km / 28.0) * span
        # Road segments along y=22
        ry = 18
        rh = 12
        segs = [
            (0, 6, "#DCFCE7", "#166534", "Çift"),
            (6, 11, "#FEE2E2", "#991B1B", "Tek Şerit"),
            (11, 18, "#DCFCE7", "#166534", "Çift Şerit"),
            (18, 23, "#FEE2E2", "#991B1B", "Tek Şerit"),
            (23, 28, "#DCFCE7", "#166534", "Çift"),
        ]
        for a, b, bg, fg, lbl in segs:
            sx = kx(a)
            sw = kx(b) - sx
            d.add(Rect(sx, ry, sw, rh, fillColor=colors.HexColor(bg), strokeColor=colors.HexColor(fg), strokeWidth=0.8))
            d.add(String(sx + sw / 2.0, ry + 3.5, lbl, fontName="TRFont-Bold", fontSize=6.2, fillColor=colors.HexColor(fg), textAnchor="middle"))
        for km in [0, 6, 11, 18, 23]:
            px = kx(km)
            d.add(Line(px, ry - 3, px, ry, strokeColor=colors.HexColor("#0F172A"), strokeWidth=0.8))
            d.add(String(px, ry - 11, f"{km}", fontName="TRFont-Bold", fontSize=7.0, fillColor=colors.HexColor("#0F172A"), textAnchor="middle"))
        d.add(String(kx(0) + 12, ry + rh + 5, "İzmir →", fontName="TRFont-Bold", fontSize=6.8, fillColor=colors.HexColor("#1E3A8A")))
        d.add(String(kx(28) - 4, ry + rh + 5, "Manisa →", fontName="TRFont-Bold", fontSize=6.8, fillColor=colors.HexColor("#1E3A8A"), textAnchor="end"))
        return d

    if diagram_name == "shelf_boxes":
        h = 64
        d = Drawing(w, h)
        # Shelving unit on left
        sx, sw = 18, w * 0.56
        dy = 8.5
        base_y = 8.0
        d.add(Rect(sx, base_y, sw, 5.5 * dy, fillColor=colors.HexColor("#F8FAFC"), strokeColor=colors.HexColor("#475569"), strokeWidth=1.0))
        for k in range(1, 6):
            ly = base_y + k * dy
            d.add(Line(sx, ly, sx + sw, ly, strokeColor=colors.HexColor("#64748B"), strokeWidth=1.0, strokeDashArray=[3, 2]))
        # Stacked boxes rising past 4 intervals, below 5th interval (4.55 * dy)
        box_h = 4.55 * dy / 3.0
        for b in range(3):
            by = base_y + b * box_h
            d.add(Rect(sx + 18, by, 42, box_h, fillColor=colors.HexColor("#FDBA74"), strokeColor=colors.HexColor("#9A3412"), strokeWidth=0.8))
        # Height bracket + digital readout panel on right
        px = sx + sw + 10
        pw = w - px - 10
        d.add(Rect(px, 16, pw, 30, fillColor=colors.HexColor("#1E293B"), strokeColor=colors.HexColor("#38BDF8"), strokeWidth=1.0, rx=3, ry=3))
        _draw_radical(d, px + 7, 25, "", "245", colors.HexColor("#38BDF8"))
        d.add(String(px + 37, 26.5, "cm", fontName="TRFont-Bold", fontSize=8.2, fillColor=colors.HexColor("#38BDF8")))
        d.add(String(px + pw / 2.0, 8, "Koli Yüksekliği", fontName="TRFont-Italic", fontSize=6.4, fillColor=colors.HexColor("#475569"), textAnchor="middle"))
        return d

    return Drawing(w, 10)


def build_question_flowable(q, styles, col_w):
    q_no = q["no"]
    raw_text = q["text"]
    opts = q["options"]

    elements = []

    if q.get("diagram"):
        diag = build_diagram_flowable(q["diagram"], col_w)
        elements.append(diag)
        elements.append(Spacer(1, 4))

    if q.get("table_data"):
        tdata = q["table_data"]
        n_cols = len(tdata[0])
        cw = (col_w - 10) / n_cols
        formatted_rows = []
        for r_idx, row in enumerate(tdata):
            frow = []
            for cell in row:
                st = styles["TableCellHeader"] if r_idx == 0 else styles["TableCell"]
                frow.append(Paragraph(render_inline_math(cell, 7.8), st))
            formatted_rows.append(frow)
        data_tbl = Table(formatted_rows, colWidths=[cw] * n_cols)
        data_tbl.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E0E7FF")),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F8FAFC")),
                    ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#94A3B8")),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 3),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                    ("TOPPADDING", (0, 0), (-1, -1), 2.5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
                ]
            )
        )
        elements.append(data_tbl)
        elements.append(Spacer(1, 4))

    segments = split_question_segments(raw_text, font_size=9.1)
    first_para = True
    for seg_type, seg_val in segments:
        if seg_type == "para":
            prefix = f"<font color='#1E3A8A'><b>{q_no}.</b></font> " if first_para else ""
            first_para = False
            elements.append(Paragraph(prefix + seg_val, styles["Question"]))
        else:
            if first_para:
                elements.append(Paragraph(f"<font color='#1E3A8A'><b>{q_no}.</b></font>", styles["Question"]))
                first_para = False
            path, w_pt, h_pt, _ = _compile_math_image(seg_val, font_size=9.5)
            elements.append(Spacer(1, 3))
            img = Image(path, width=w_pt, height=h_pt)
            img.hAlign = "CENTER"
            elements.append(img)
            elements.append(Spacer(1, 4))

    elements.append(Spacer(1, 4))

    # Render options with crisp mathtext tags
    rendered_opts = [(o[0], render_inline_math(o[1], 8.6)) for o in opts]
    plain_lens = [len(re.sub(r"\$|\\sqrt|\\frac|\\left|\\right|\{|\}|\\", "", o[1])) for o in opts]
    max_opt_len = max(plain_lens)

    if q.get("options_vertical") or max_opt_len > 22:
        opt_rows = [
            [Paragraph(f"<b>{o[0]})</b> {o[1]}", styles["OptionLong"])]
            for o in rendered_opts
        ]
        opt_table = Table(opt_rows, colWidths=[col_w - 6])
    else:
        row1 = [
            Paragraph(f"<b>{rendered_opts[0][0]})</b> {rendered_opts[0][1]}", styles["Option"]),
            Paragraph(f"<b>{rendered_opts[1][0]})</b> {rendered_opts[1][1]}", styles["Option"]),
            Paragraph(f"<b>{rendered_opts[2][0]})</b> {rendered_opts[2][1]}", styles["Option"]),
        ]
        row2 = [
            Paragraph(f"<b>{rendered_opts[3][0]})</b> {rendered_opts[3][1]}", styles["Option"]),
            Paragraph(f"<b>{rendered_opts[4][0]})</b> {rendered_opts[4][1]}", styles["Option"]),
            Paragraph("", styles["Option"]),
        ]
        c_w = (col_w - 6) / 3.0
        opt_table = Table([row1, row2], colWidths=[c_w, c_w, c_w])

    opt_table.setStyle(
        TableStyle(
            [
                ("LEFTPADDING", (0, 0), (-1, -1), 1),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                ("TOPPADDING", (0, 0), (-1, -1), 1.8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.8),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    elements.append(opt_table)
    elements.append(Spacer(1, 5))
    elements.append(WorkspaceLabel(col_w - 4))
    # Keep generous workspace while accounting cleanly for taller diagram/table questions
    ws_height = 64 if (q.get("diagram") or q.get("table_data")) else 76
    elements.append(Spacer(1, ws_height))
    elements.append(DividerLine(col_w - 4))
    elements.append(Spacer(1, 7))

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

    MAIN_TITLE = "9-14 KASIM ARASI MÜFİT HOCANIN KÖKLÜ İFADELER ÖDEVİ"

    def draw_first_page(canvas, doc):
        canvas.saveState()
        banner_h = 18 * mm
        banner_y = page_h - 25 * mm
        canvas.setFillColor(colors.HexColor("#1E3A8A"))
        canvas.roundRect(left_m, banner_y, usable_w, banner_h, 5, fill=1, stroke=0)

        canvas.setFillColor(colors.white)
        canvas.setFont("TRFont-Bold", 11.4)
        canvas.drawCentredString(
            page_w / 2.0,
            banner_y + 10.5 * mm,
            MAIN_TITLE,
        )
        canvas.setFont("TRFont", 8.8)
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
        canvas.setFont("TRFont-Bold", 8.0)
        canvas.drawString(left_m + 3 * mm, header_y + 2.2 * mm, MAIN_TITLE)
        canvas.setFont("TRFont", 7.6)
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
        author="Müfit Hoca",
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
        fontSize=9.1,
        leading=15.4,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=2,
    )
    opt_style = ParagraphStyle(
        "Option",
        parent=styles["Normal"],
        fontName="TRFont",
        fontSize=8.6,
        leading=12.2,
        textColor=colors.HexColor("#1E293B"),
    )
    opt_long_style = ParagraphStyle(
        "OptionLong",
        parent=styles["Normal"],
        fontName="TRFont",
        fontSize=8.3,
        leading=11.8,
        textColor=colors.HexColor("#1E293B"),
    )
    tbl_hdr_style = ParagraphStyle(
        "TableCellHeader",
        parent=styles["Normal"],
        fontName="TRFont-Bold",
        fontSize=7.8,
        leading=10.5,
        alignment=1,
        textColor=colors.HexColor("#1E3A8A"),
    )
    tbl_cell_style = ParagraphStyle(
        "TableCell",
        parent=styles["Normal"],
        fontName="TRFont",
        fontSize=7.8,
        leading=10.5,
        alignment=1,
        textColor=colors.HexColor("#0F172A"),
    )
    day_banner_style = ParagraphStyle(
        "DayBanner",
        parent=styles["Normal"],
        fontName="TRFont-Bold",
        fontSize=8.6,
        leading=11.4,
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
    letters = ["A", "B", "C", "D", "E"]
    assert len(QUESTIONS_KASIM_9_14) == 60
    for i, q in enumerate(QUESTIONS_KASIM_9_14, 1):
        assert q["no"] == i
        assert len(q["options"]) == 5
        assert len({o[1] for o in q["options"]}) == 5, f"Duplicate options in Q{i}"
        assert q["answer"] in letters

    for day in range(1, 7):
        day_qs = [q for q in QUESTIONS_KASIM_9_14 if q["day"] == day]
        counts = {L: sum(1 for q in day_qs if q["answer"] == L) for L in letters}
        day_title, day_desc = TEST_INFO[day]
        q_start = day_qs[0]["no"]
        q_end = day_qs[-1]["no"]
        fname = f"EMIR_9-14_KASIM_TEST_{day}_(Sorular_{q_start}-{q_end}).pdf"
        fpath = os.path.join(BASE_DIR, fname)
        create_pdf_for_questions(
            fpath,
            day_qs,
            subtitle_text=f"{day_title} | {day_desc}",
        )
        print(f"Created Test {day} PDF: {fname} | Dist: {counts}")

    master_fname = "EMIR_9-14_KASIM_KOKLU_IFADELER_ODEVI.pdf"
    master_fpath = os.path.join(BASE_DIR, master_fname)
    create_pdf_for_questions(
        master_fpath,
        QUESTIONS_KASIM_9_14,
        subtitle_text="6 Adet Çoktan Seçmeli Test (Günlük 10 Soru — Toplam 60 Soru) | Köklü İfadeler (Örnek 1–31)",
    )
    print(f"Created Master PDF: {master_fname}")

    import fitz
    doc = fitz.open(master_fpath)
    print(f"Master PDF total pages: {len(doc)}")
    for p in range(len(doc)):
        doc[p].get_pixmap(dpi=130).save(
            os.path.join(BASE_DIR, f"extracted_pages_analysis/preview_kasim9_14_p{p+1}.png")
        )


if __name__ == "__main__":
    main()
