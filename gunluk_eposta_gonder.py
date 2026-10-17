# -*- coding: utf-8 -*-
"""
EMİR 17-23 EKİM 2026 GÜNLÜK CEVAP ANAHTARI E-POSTA GÖNDERİM BOTU (GITHUB ACTIONS BULUT)
Alıcılar:
  - emiiruysal@gmail.com
  - gonuluysal532@gmail.com
  - uysalhseyin@gmail.com
  - hizarci84@gmail.com
Saat: Her gün 18:00 (Türkiye Saati / UTC+3)
"""

import os
import sys
import json
import smtplib
from datetime import datetime, timezone, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sys.stdout.reconfigure(encoding="utf-8")

import balance_and_verify_17_23 as b

RECIPIENTS = [
    "emiiruysal@gmail.com",
    "gonuluysal532@gmail.com",
    "uysalhseyin@gmail.com",
    "hizarci84@gmail.com",
]

# Türkiye saati (UTC+3) tarih -> Gün eşleşmesi
DAY_DATES = {
    "2026-10-17": (1, "17 Ekim 2026 Cumartesi"),
    "2026-10-18": (2, "18 Ekim 2026 Pazar"),
    "2026-10-19": (3, "19 Ekim 2026 Pazartesi"),
    "2026-10-20": (4, "20 Ekim 2026 Salı"),
    "2026-10-21": (5, "21 Ekim 2026 Çarşamba"),
    "2026-10-22": (6, "22 Ekim 2026 Perşembe"),
    "2026-10-23": (6, "23 Ekim 2026 Cuma"),
}

DAY_TITLES = {
    1: "1. GÜN (17 Ekim 2026) — Sorular 1 - 15 (Sayfa 17-20 Orijinal Sorular)",
    2: "2. GÜN (18 Ekim 2026) — Sorular 16 - 30 (Sayfa 20-23 Orijinal + Benzer Sorular)",
    3: "3. GÜN (19 Ekim 2026) — Sorular 31 - 45 (Pekiştirme / Benzer Sorular)",
    4: "4. GÜN (20 Ekim 2026) — Sorular 46 - 60 (Pekiştirme / Benzer Sorular)",
    5: "5. GÜN (21 Ekim 2026) — Sorular 61 - 75 (Pekiştirme / Benzer Sorular)",
    6: "6. GÜN (22-23 Ekim 2026) — Sorular 76 - 90 (Pekiştirme / Benzer Sorular)",
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
HISTORY_FILE = os.path.join(DATA_DIR, "sent_history.json")


def get_turkey_now() -> datetime:
    tz_tr = timezone(timedelta(hours=3))
    return datetime.now(tz_tr)


def load_history() -> dict:
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_history(date_key: str, day_no: int):
    os.makedirs(DATA_DIR, exist_ok=True)
    hist = load_history()
    hist[date_key] = {
        "day": day_no,
        "sent_at_trt": get_turkey_now().strftime("%Y-%m-%d %H:%M:%S"),
        "recipients": RECIPIENTS,
    }
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(hist, f, ensure_ascii=False, indent=2)


def build_html_for_day(day_no: int) -> tuple[str, str]:
    day_qs = [q for q in b.QUESTIONS_17_23 if q["day"] == day_no]
    q_start = day_qs[0]["no"]
    q_end = day_qs[-1]["no"]
    day_subtitle = DAY_TITLES.get(day_no, f"{day_no}. GÜN (Sorular {q_start}-{q_end})")

    subject = f"📘 [EMİR - {day_no}. GÜN CEVAP ANAHTARI] 17-23 Ekim 2026 (Sorular {q_start}-{q_end})"

    letters = ["A", "B", "C", "D", "E"]

    # Hızlı cevap matrisi (5 sütun x 3 satır = 15 soru)
    matrix_rows = ""
    for r in range(0, len(day_qs), 5):
        chunk = day_qs[r : r + 5]
        tds = ""
        for q in chunk:
            tds += (
                f"<td style='padding:10px 6px;border:1px solid #BFDBFE;background:#EFF6FF;"
                f"text-align:center;border-radius:6px;'>"
                f"<div style='font-size:11px;color:#475569;font-weight:bold;'>{q['no']}. Soru</div>"
                f"<div style='font-size:17px;color:#1E3A8A;font-weight:800;margin-top:2px;'>{q['answer']}</div>"
                f"</td>"
            )
        matrix_rows += f"<tr>{tds}</tr>"

    # Detaylı tablo satırları
    rows_html = ""
    for idx, q in enumerate(day_qs):
        ans_letter = q["answer"]
        ans_val = q["options"][letters.index(ans_letter)][1]
        q_type = f"Sayfa {q['page']} Orijinal Soru" if q.get("is_original") else f"{q.get('sim_to')}. Soruya Benzer"
        bg = "#F8FAFC" if idx % 2 == 0 else "#FFFFFF"
        rows_html += (
            f"<tr style='background:{bg};'>"
            f"<td style='padding:9px 12px;border:1px solid #CBD5E1;text-align:center;font-weight:bold;color:#0F172A;'>{q['no']}</td>"
            f"<td style='padding:9px 12px;border:1px solid #CBD5E1;text-align:center;font-weight:bold;color:#1D4ED8;font-size:15px;'>{ans_letter}</td>"
            f"<td style='padding:9px 12px;border:1px solid #CBD5E1;text-align:left;color:#0F172A;font-weight:600;'>{ans_val}</td>"
            f"<td style='padding:9px 12px;border:1px solid #CBD5E1;text-align:left;color:#64748B;font-size:12px;'>{q_type}</td>"
            f"</tr>"
        )

    now_str = get_turkey_now().strftime("%d.%m.%Y %H:%M")

    html = f"""<!DOCTYPE html>
<html lang="tr">
<head><meta charset="UTF-8"></head>
<body style="margin:0;padding:16px;background-color:#F1F5F9;font-family:Calibri,Arial,sans-serif;">
  <div style="max-width:640px;margin:0 auto;background:#FFFFFF;border:1px solid #CBD5E1;border-radius:12px;overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.06);">
    <div style="background:linear-gradient(135deg,#1E3A8A,#1D4ED8);color:#FFFFFF;padding:22px 24px;text-align:center;">
      <div style="font-size:11px;letter-spacing:1px;text-transform:uppercase;color:#BFDBFE;font-weight:bold;margin-bottom:6px;">
        MÜFİT HOCA ONLINE DERS &amp; ÖDEV TAKİP SİSTEMİ
      </div>
      <h2 style="margin:0;font-size:19px;font-weight:800;">
        EMİR 17-23 EKİM 2026 TARİHLERİ ARASI ÇÖZÜLECEK SORULAR
      </h2>
      <p style="margin:8px 0 0 0;color:#DBEAFE;font-size:14px;font-weight:600;">
        {day_subtitle}
      </p>
    </div>

    <div style="padding:22px 24px;">
      <div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:8px;padding:12px 16px;margin-bottom:18px;">
        <div style="font-size:13px;font-weight:bold;color:#166534;">
          ✅ GÜNLÜK SAAT 18:00 CEVAP ANAHTARI KONTROLÜ ({now_str})
        </div>
        <div style="font-size:12.5px;color:#15803D;margin-top:4px;line-height:1.45;">
          Emir'in bugünkü 15 soruluk üslü ifadeler ödevinin cevap anahtarı aşağıdadır. Yanlış veya boş bırakılan soruları test üzerinde işaretleyiniz; dersimizde birlikte çözeceğiz.
        </div>
      </div>

      <div style="font-size:13px;font-weight:800;color:#1E3A8A;margin-bottom:8px;border-left:4px solid #2563EB;padding-left:8px;">
        HIZLI CEVAP ANAHTARI TABLOSU (SORULAR {q_start} – {q_end})
      </div>
      <table style="width:100%;border-collapse:separate;border-spacing:6px;margin-bottom:20px;">
        {matrix_rows}
      </table>

      <div style="font-size:13px;font-weight:800;color:#1E3A8A;margin-bottom:8px;border-left:4px solid #0284C7;padding-left:8px;">
        DETAYLI CEVAP DEĞERLERİ VE SORU KAYNAĞI
      </div>
      <table style="width:100%;border-collapse:collapse;font-size:13.5px;">
        <thead>
          <tr style="background:#1E3A8A;color:#FFFFFF;">
            <th style="padding:9px;border:1px solid #CBD5E1;width:14%;">Soru</th>
            <th style="padding:9px;border:1px solid #CBD5E1;width:16%;">Doğru Şık</th>
            <th style="padding:9px;border:1px solid #CBD5E1;width:40%;text-align:left;">Doğru Cevap Değeri</th>
            <th style="padding:9px;border:1px solid #CBD5E1;width:30%;text-align:left;">Kaynak / Kalıp</th>
          </tr>
        </thead>
        <tbody>
          {rows_html}
        </tbody>
      </table>
    </div>

    <div style="background:#F8FAFC;border-top:1px solid #E2E8F0;padding:14px 24px;text-align:center;font-size:11.5px;color:#64748B;">
      Bu e-posta GitHub Bulut Otomasyonu üzerinden her gün saat 18:00'de otomatik olarak<br/>
      <b>{', '.join(RECIPIENTS)}</b> adreslerine gönderilmektedir.
    </div>
  </div>
</body>
</html>"""
    return subject, html


def send_day_email(day_no: int) -> bool:
    sender_email = os.environ.get("GMAIL_USER", "hizarci84@gmail.com").strip() or "hizarci84@gmail.com"
    app_password = os.environ.get("GMAIL_APP_PASSWORD", "").replace(" ", "").strip()

    subject, html_body = build_html_for_day(day_no)

    if not app_password:
        print(f"[HATA] GMAIL_APP_PASSWORD ortam değişkeni tanımlı değil!")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"Müfit Hoca (Matematik Ödev Takip) <{sender_email}>"
    msg["To"] = ", ".join(RECIPIENTS)
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    import time
    for attempt in range(1, 4):
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30) as server:
                server.login(sender_email, app_password)
                server.sendmail(sender_email, RECIPIENTS, msg.as_string())
            print(f"[BAŞARILI] {day_no}. Gün cevap anahtarı {', '.join(RECIPIENTS)} adreslerine gönderildi (Deneme {attempt}).")
            return True
        except Exception as exc:
            print(f"[UYARI] SMTP gönderim denemesi {attempt}/3 başarısız: {exc}")
            if attempt < 3:
                time.sleep(10)
    return False


def main():
    import time
    now_tr = get_turkey_now()
    today_str = now_tr.strftime("%Y-%m-%d")
    print(f"[*] Türkiye Saati: {now_tr.strftime('%Y-%m-%d %H:%M:%S')}")

    input_day = os.environ.get("INPUT_DAY", "").strip()
    force_send = os.environ.get("FORCE_SEND", "false").strip().lower() == "true"
    event_name = os.environ.get("GITHUB_EVENT_NAME", "").strip()

    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        input_day = sys.argv[1]

    # Eğer otomatik zamanlayıcı (schedule) ile tetiklendiyse saat 18:00 kontrolü yap
    if event_name == "schedule" and not force_send and not input_day:
        if now_tr.hour < 17 or (now_tr.hour == 17 and now_tr.minute < 45):
            print(f"[BİLGİ] Henüz saat 18:00 olmadı ({now_tr.strftime('%H:%M')}). Gönderim saati 18:00'dir.")
            return
        elif now_tr.hour == 17 and now_tr.minute >= 45:
            wait_sec = (59 - now_tr.minute) * 60 + (60 - now_tr.second)
            print(f"[*] Saat 18:00'e {wait_sec} saniye var; tam 18:00:00'de göndermek için bekleniyor...")
            time.sleep(wait_sec)
            now_tr = get_turkey_now()
            today_str = now_tr.strftime("%Y-%m-%d")

    if input_day and input_day.isdigit():
        day_no = int(input_day)
        date_key = f"manual_day_{day_no}_{today_str}"
    else:
        if today_str not in DAY_DATES:
            print(f"[BİLGİ] Bugünün tarihi ({today_str}) 17-23 Ekim 2026 ödev takvimi dışında. Gönderim yapılmadı.")
            return
        day_no, label = DAY_DATES[today_str]
        date_key = f"day_{day_no}_{today_str}"
        print(f"[*] Bugünün ödev günü: {day_no}. Gün ({label})")

    history = load_history()
    if date_key in history and not force_send:
        print(f"[BİLGİ] {date_key} için cevap anahtarı zaten gönderilmiş ({history[date_key]['sent_at_trt']}). Tekrar gönderilmedi.")
        return

    ok = send_day_email(day_no)
    if ok:
        save_history(date_key, day_no)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
