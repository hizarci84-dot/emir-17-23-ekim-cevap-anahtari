# -*- coding: utf-8 -*-
r"""
9-14 KASIM ARASI MÜFİT HOCANIN KÖKLÜ İFADELER ÖDEVİ
Maarif_Video_Ders_Kitabi Köklü İfadeler Bölümü (Sayfa 22-27 | Örnek 1 - Örnek 31)
Günlük 10 soru olacak şekilde 6 adet çoktan seçmeli test (Toplam 60 özgün soru).
"""

TEST_INFO = {
    1: ("1. GÜN TESTİ (9 KASIM 2026 PAZARTESİ)", "Test 1 (Sorular 1 – 10): Köklü İfade Tanımı ve Gerçek Sayı Tanım Aralığı"),
    2: ("2. GÜN TESTİ (10 KASIM 2026 SALI)", "Test 2 (Sorular 11 – 20): Kök Dışına Çıkma, Mutlak Değer ve İşaret İncelemesi"),
    3: ("3. GÜN TESTİ (11 KASIM 2026 ÇARŞAMBA)", "Test 3 (Sorular 21 – 30): Üslü-Köklü İlişki ve Katsayıyı Kök Dışına/İçine Alma"),
    4: ("4. GÜN TESTİ (12 KASIM 2026 PERŞEMBE)", "Test 4 (Sorular 31 – 40): Ardışık Tam Sayı Aralığı ve Yaklaşık Değer"),
    5: ("5. GÜN TESTİ (13 KASIM 2026 CUMA)", "Test 5 (Sorular 41 – 50): Kök Derecesi Genişletme/Sadeleştirme ve Sıralama"),
    6: ("6. GÜN TESTİ (14 KASIM 2026 CUMARTESİ)", "Test 6 (Sorular 51 – 60): Bağlam Temelli ve Yeni Nesil Sentez Soruları"),
}

QUESTIONS_KASIM_9_14 = [
    # =========================================================================
    # TEST 1 (9 KASIM 2026 PAZARTESİ) — SORULAR 1 - 10 (Örnek 1-4, 6-8, 11)
    # =========================================================================
    {
        "no": 1,
        "day": 1,
        "topic": r"Köklü İfade Tanımı ve $x^n = a$ Denklemleri (Örnek 1-2)",
        "text": (
            r"Gerçek sayılar kümesinde verilen aşağıdaki ifadelerden hangisi <b>kesinlikle doğrudur</b>?"
        ),
        "options": [
            ("A", r"$x^2 = 21$ ise $x = \sqrt{21}$ dir."),
            ("B", r"$x^3 = -11$ ise $x = \pm\sqrt[3]{11}$ dir."),
            ("C", r"$x \cdot x \cdot x \cdot x = 15$ ve $x < 0$ ise $x = -\sqrt[4]{15}$ tir."),
            ("D", r"$x^5 = 18$ ise $x = \pm\sqrt[5]{18}$ dir."),
            ("E", r"Her $x$ gerçek sayısı için $\sqrt{x^2} = x$ tir."),
        ],
        "options_vertical": True,
        "answer": "C",
    },
    {
        "no": 2,
        "day": 1,
        "topic": r"Tek ve Çift Dereceli Köklerin Çözüm Sayısı (Örnek 2)",
        "text": (
            r"$x$ ve $y$ birer gerçek sayı olmak üzere,<br/>"
            r"$x^3 = 19$<br/>"
            r"$y \cdot y = 23$<br/>"
            r"eşitlikleri veriliyor. Buna göre $x$ ve $y$ ile ilgili aşağıdakilerden hangisi doğrudur?"
        ),
        "options": [
            ("A", r"$x$ yerine $2$ farklı değer, $y$ yerine $1$ farklı değer yazılabilir."),
            ("B", r"$x = \sqrt[3]{19}$ olup $y$'nin alabileceği değerlerin toplamı $0$'dır."),
            ("C", r"$x \cdot y$ çarpımı her zaman pozitif bir gerçek sayıdır."),
            ("D", r"$x = 19^3$ ve $y = \pm 23$ olarak bulunur."),
            ("E", r"$y$ değerlerinden biri $-\sqrt{23}$, diğeri $23$'tür."),
        ],
        "options_vertical": True,
        "answer": "B",
    },
    {
        "no": 3,
        "day": 1,
        "topic": r"Kare Kenarı, Küp Ayrıtı ve Sıralama (Örnek 3)",
        "text": (
            r"Alanı $49$ cm² olan karenin bir kenar uzunluğu $a$ cm, "
            r"alanı $15$ cm² olan karenin bir kenar uzunluğu $b$ cm ve "
            r"hacmi $27$ cm³ olan küpün bir ayrıt uzunluğu $c$ cm'dir.<br/>"
            r"<b>Buna göre $a$, $b$ ve $c$ arasındaki doğru sıralama aşağıdakilerden hangisidir?</b>"
        ),
        "options": [
            ("A", r"$a < b < c$"),
            ("B", r"$b < c < a$"),
            ("C", r"$c < a < b$"),
            ("D", r"$c < b < a$"),
            ("E", r"$b < a < c$"),
        ],
        "answer": "D",
    },
    {
        "no": 4,
        "day": 1,
        "topic": r"Gerçek Sayı Olma Koşulu ve Parantez İnceliği (Örnek 4)",
        "text": (
            r"Aşağıda verilen köklü ifadelerden kaç tanesi bir <b>gerçek sayı değildir</b>?<br/>"
            r"I. $\sqrt[4]{(-2)^4}$ &nbsp;&nbsp; II. $\sqrt{(-3^2)}$ &nbsp;&nbsp; III. $\sqrt[5]{-32}$<br/>"
            r"IV. $\sqrt[6]{(-1)^5}$ &nbsp;&nbsp; V. $\sqrt[8]{0}$ &nbsp;&nbsp; VI. $\sqrt[3]{(-4^2)}$ &nbsp;&nbsp; VII. $\sqrt[4]{-16}$"
        ),
        "options": [
            ("A", r"$1$"),
            ("B", r"$2$"),
            ("C", r"$3$"),
            ("D", r"$4$"),
            ("E", r"$5$"),
        ],
        "answer": "C",
    },
    {
        "no": 5,
        "day": 1,
        "topic": r"Çift ve Tek Kök Bir Arada Tanım Aralığı (Örnek 6)",
        "text": (
            r"$\sqrt{7 - x} + \sqrt[5]{x - 3}$<br/>"
            r"ifadesi bir gerçek sayı olduğuna göre, $x$ yerine yazılabilecek <b>kaç farklı doğal sayı</b> değeri vardır?"
        ),
        "options": [
            ("A", r"$4$"),
            ("B", r"$5$"),
            ("C", r"$6$"),
            ("D", r"$7$"),
            ("E", r"$8$"),
        ],
        "answer": "E",
    },
    {
        "no": 6,
        "day": 1,
        "topic": r"İki Çift Kök + Paydalı Tanım Aralığı (Örnek 7)",
        "text": (
            r"$$\frac{\sqrt{10 - x} + \sqrt[4]{2x - 6}}{\sqrt[3]{x - 4}}$$"
            r"ifadesi bir gerçek sayı olduğuna göre, $x$ yerine yazılabilecek <b>tam sayı değerlerinin toplamı</b> kaçtır?"
        ),
        "options": [
            ("A", r"$48$"),
            ("B", r"$49$"),
            ("C", r"$50$"),
            ("D", r"$52$"),
            ("E", r"$55$"),
        ],
        "answer": "A",
    },
    {
        "no": 7,
        "day": 1,
        "topic": r"Zıt İşaretli Kök İçi Denklem Değeri (Örnek 8)",
        "text": (
            r"$K$ ve $x$ birer gerçek sayı olmak üzere,<br/>"
            r"$K = \sqrt[4]{3x - 18} + \sqrt{6 - x} + \sqrt[3]{x + 2} + 4x$<br/>"
            r"eşitliği veriliyor. <b>Buna göre $K$ değeri kaçtır?</b>"
        ),
        "options": [
            ("A", r"$22$"),
            ("B", r"$24$"),
            ("C", r"$25$"),
            ("D", r"$26$"),
            ("E", r"$28$"),
        ],
        "answer": "D",
    },
    {
        "no": 8,
        "day": 1,
        "topic": r"Sembollü Kök Dereceleri Tablosu (Örnek 11)",
        "diagram": "board_symbols",
        "table_data": [
            ["Öncül", "□", "△", "★"],
            ["I", "3", "4", "5"],
            ["II", "5", "2", "4"],
            ["III", "7", "6", "3"],
        ],
        "text": (
            r"Yukarıdaki tahtaya yazılan üç köklü ifadenin de birer <b>gerçek sayı</b> olması için "
            r"□, △ ve ★ sembolleri yerine tablodaki satırlardan hangileri yazılabilir?"
        ),
        "options": [
            ("A", "Yalnız I"),
            ("B", "Yalnız II"),
            ("C", "Yalnız III"),
            ("D", "I ve II"),
            ("E", "I ve III"),
        ],
        "answer": "E",
    },
    {
        "no": 9,
        "day": 1,
        "topic": r"Kök Derecesi Koşulu ($n \geq 2$) ve Tek/Çift Analiz (Tanım + Örnek 4)",
        "text": (
            r"$n$ bir doğal sayı olmak üzere, $\sqrt[n+1]{x - 5}$ köklü ifadesi "
            r"<b>her $x$ gerçek sayısı için</b> bir gerçek sayı belirtmektedir.<br/>"
            r"<b>Buna göre $n$'nin alabileceği en küçük değer kaçtır?</b>"
        ),
        "options": [
            ("A", r"$1$"),
            ("B", r"$2$"),
            ("C", r"$3$"),
            ("D", r"$4$"),
            ("E", r"$5$"),
        ],
        "answer": "B",
    },
    {
        "no": 10,
        "day": 1,
        "topic": r"Köklü Kenarlı Kare Alanı ve Küp Hacmi (Örnek 2-3)",
        "text": (
            r"Bir kenar uzunluğu $\sqrt{18}$ cm olan karenin alanı $A$ cm², "
            r"bir ayrıt uzunluğu $\sqrt[3]{7}$ cm olan küpün hacmi $V$ cm³'tür.<br/>"
            r"<b>Buna göre $A - V$ farkı kaçtır?</b>"
        ),
        "options": [
            ("A", r"$11$"),
            ("B", r"$13$"),
            ("C", r"$15$"),
            ("D", r"$25$"),
            ("E", r"$29$"),
        ],
        "answer": "A",
    },

    # =========================================================================
    # TEST 2 (10 KASIM 2026 SALI) — SORULAR 11 - 20 (Örnek 5, 9, 10, 12, 13)
    # =========================================================================
    {
        "no": 11,
        "day": 2,
        "topic": r"Tek ve Çift Derecede Kök Dışına Çıkarma (Örnek 5 & 9)",
        "text": (
            r"$\sqrt[3]{(-5)^3} + \sqrt[4]{(-2)^4} - \sqrt[6]{(-1)^6} + \sqrt[5]{(-3)^5}$<br/>"
            r"<b>işleminin sonucu kaçtır?</b>"
        ),
        "options": [
            ("A", r"$-7$"),
            ("B", r"$-5$"),
            ("C", r"$-1$"),
            ("D", r"$3$"),
            ("E", r"$5$"),
        ],
        "answer": "A",
    },
    {
        "no": 12,
        "day": 2,
        "topic": r"Kesirli Mutlak Değer ve Kök Çıkarma (Örnek 9)",
        "text": (
            r"$$\frac{\sqrt{(-9)^2} - \sqrt[3]{(-4)^3} + \sqrt[8]{(-2)^8}}{\sqrt[5]{(-1)^5} + \sqrt[4]{(-4)^4}}$$"
            r"<b>işleminin sonucu kaçtır?</b>"
        ),
        "options": [
            ("A", r"$-5$"),
            ("B", r"$3$"),
            ("C", r"$5$"),
            ("D", r"$7$"),
            ("E", r"$9$"),
        ],
        "answer": "C",
    },
    {
        "no": 13,
        "day": 2,
        "topic": r"Kök Dışına Çıkarma Kuralları (Örnek 5)",
        "text": (
            r"Aşağıdaki eşitliklerden hangisi <b>yanlıştır</b>?"
        ),
        "options": [
            ("A", r"$\sqrt[3]{(-6)^3} = -6$"),
            ("B", r"$-\sqrt{(-7)^2} = -7$"),
            ("C", r"$\sqrt[4]{(-3)^4} = 3$"),
            ("D", r"$\sqrt[6]{(-2)^6} = -2$"),
            ("E", r"$-\sqrt[5]{-32} = 2$"),
        ],
        "answer": "D",
    },
    {
        "no": 14,
        "day": 2,
        "topic": r"Tek / Çift Derece Parite Çıkarımı (Örnek 10)",
        "text": (
            r"$m$ ve $n$, $1$'den büyük birer tam sayı olmak üzere,<br/>"
            r"$\sqrt[m]{(-6)^m} + \sqrt[n]{(-3)^n} = -3$<br/>"
            r"eşitliği verilmiştir. Buna göre,<br/>"
            r"$\sqrt[m+n]{(-2)^{m+n}} + \sqrt[m \cdot n]{(-4)^{m \cdot n}} - \sqrt[n+1]{(-5)^{n+1}}$<br/>"
            r"<b>işleminin sonucu kaçtır?</b>"
        ),
        "options": [
            ("A", r"$-7$"),
            ("B", r"$-3$"),
            ("C", r"$3$"),
            ("D", r"$5$"),
            ("E", r"$7$"),
        ],
        "answer": "E",
    },
    {
        "no": 15,
        "day": 2,
        "topic": r"Çıkarma İle Parite Belirleme (Örnek 10)",
        "text": (
            r"$k$ ve $t$, $1$'den büyük birer tam sayı olmak üzere,<br/>"
            r"$\sqrt[k]{(-7)^k} - \sqrt[t]{(-3)^t} = 10$<br/>"
            r"eşitliği sağlanmaktadır. Buna göre,<br/>"
            r"$\sqrt[k+t]{(-8)^{k+t}} + \sqrt[k \cdot t]{(-1)^{k \cdot t}}$<br/>"
            r"<b>işleminin sonucu kaçtır?</b>"
        ),
        "options": [
            ("A", r"$-9$"),
            ("B", r"$-7$"),
            ("C", r"$7$"),
            ("D", r"$9$"),
            ("E", r"$11$"),
        ],
        "answer": "B",
    },
    {
        "no": 16,
        "day": 2,
        "topic": r"Harfli Mutlak Değer Kök Çıkarma (Örnek 12)",
        "text": (
            r"$a < 0 < b$ olmak üzere,<br/>"
            r"$\sqrt{a^2} + \sqrt[3]{(b - a)^3} - \sqrt[4]{(a - b)^4} + \sqrt[5]{b^5}$<br/>"
            r"<b>ifadesinin eşiti aşağıdakilerden hangisidir?</b>"
        ),
        "options": [
            ("A", r"$a - b$"),
            ("B", r"$a + b$"),
            ("C", r"$b - a$"),
            ("D", r"$2b - a$"),
            ("E", r"$2a - b$"),
        ],
        "answer": "C",
    },
    {
        "no": 17,
        "day": 2,
        "topic": r"Negatif Harflerde Kök Çıkarma (Örnek 12)",
        "text": (
            r"$x < y < 0$ olmak üzere,<br/>"
            r"$\sqrt[4]{x^4} - \sqrt{(x - y)^2} + \sqrt[3]{y^3}$<br/>"
            r"<b>ifadesinin eşiti aşağıdakilerden hangisidir?</b>"
        ),
        "options": [
            ("A", r"$0$"),
            ("B", r"$2x$"),
            ("C", r"$2y$"),
            ("D", r"$2y - 2x$"),
            ("E", r"$-2x$"),
        ],
        "answer": "A",
    },
    {
        "no": 18,
        "day": 2,
        "topic": r"Verilen Aralıkta Harfli Kök Sadeleştirme (Örnek 12)",
        "text": (
            r"$2 < x < 5$ olmak üzere,<br/>"
            r"$\sqrt{(x - 2)^2} + \sqrt[4]{(x - 5)^4} + \sqrt[3]{(1 - x)^3}$<br/>"
            r"<b>ifadesinin eşiti aşağıdakilerden hangisidir?</b>"
        ),
        "options": [
            ("A", r"$x - 4$"),
            ("B", r"$4 - x$"),
            ("C", r"$x + 2$"),
            ("D", r"$2 - x$"),
            ("E", r"$8 - x$"),
        ],
        "answer": "B",
    },
    {
        "no": 19,
        "day": 2,
        "topic": r"Doğru / Yanlış ile Dört Haneli Şifre Oluşturma (Örnek 13)",
        "text": (
            r"Okul dolabının $1$ ve $0$ rakamlarından oluşan dört haneli şifresini "
            r'unutan Emir, abisinin bıraktığı şu notu okumuştur: <i>"Her hane için yazdığım eşitlik doğru ise o haneye $1$, yanlış ise $0$ yaz."</i><br/>'
            r"• 1. hane için: $\sqrt[4]{(-5)^4} = 5$<br/>"
            r"• 2. hane için: $\sqrt{(-4^2)} = 4$<br/>"
            r"• 3. hane için: $\sqrt[3]{(-7)^3} = -7$<br/>"
            r"• 4. hane için: $-\sqrt[6]{(-2)^6} = 2$<br/>"
            r"<b>Buna göre Emir dolabını açmak için hangi şifreyi tuşlamalıdır?</b>"
        ),
        "options": [
            ("A", r"$1110$"),
            ("B", r"$1011$"),
            ("C", r"$1001$"),
            ("D", r"$1010$"),
            ("E", r"$1100$"),
        ],
        "answer": "D",
    },
    {
        "no": 20,
        "day": 2,
        "topic": r"İrrasyonel Sayılı Mutlak Değer Çıkarma (Örnek 9 & 12)",
        "text": (
            r"$\sqrt{(\sqrt{7} - 3)^2} - \sqrt[3]{(2 - \sqrt{7})^3} + \sqrt[4]{(-4)^4}$<br/>"
            r"<b>işleminin sonucu kaçtır?</b>"
        ),
        "options": [
            ("A", r"$1$"),
            ("B", r"$2$"),
            ("C", r"$3$"),
            ("D", r"$4$"),
            ("E", r"$5$"),
        ],
        "answer": "E",
    },

    # =========================================================================
    # TEST 3 (11 KASIM 2026 ÇARŞAMBA) — SORULAR 21 - 30 (Örnek 14-19)
    # =========================================================================
    {
        "no": 21,
        "day": 3,
        "topic": r"Köklü İfadeyi Üslü İfade Biçiminde Yazma (Örnek 14)",
        "text": (
            r"Aşağıdaki eşitliklerden kaç tanesi <b>doğrudur</b>?<br/>"
            r"I. $\sqrt[3]{7^2} = 7^{\frac{2}{3}}$ &nbsp;&nbsp;&nbsp; II. $\sqrt[5]{8} = 2^{\frac{3}{5}}$<br/>"
            r"III. $\sqrt{3^5} = 3^{\frac{5}{2}}$ &nbsp;&nbsp;&nbsp; IV. $\sqrt[4]{2^{x+3}} = 2^{4x+12}$<br/>"
            r"V. $\sqrt[5]{9^2} = 3^{\frac{4}{5}}$"
        ),
        "options": [
            ("A", r"$1$"),
            ("B", r"$2$"),
            ("C", r"$3$"),
            ("D", r"$4$"),
            ("E", r"$5$"),
        ],
        "answer": "D",
    },
    {
        "no": 22,
        "day": 3,
        "topic": r"Üslü İfadeyi Köklü İfade Biçiminde Yazma (Örnek 15)",
        "text": (
            r"Rasyonel kuvvet olarak verilen aşağıdaki eşitliklerden hangisi <b>yanlıştır</b>?"
        ),
        "options": [
            ("A", r"$11^{\frac{2}{3}} = \sqrt[3]{11^2}$"),
            ("B", r"$(-3)^{\frac{1}{5}} = \sqrt[5]{-3}$"),
            ("C", r"$4^{\frac{3}{2}} = \sqrt[3]{4^2}$"),
            ("D", r"$(-x)^{\frac{4}{7}} = \sqrt[7]{(-x)^4}$"),
            ("E", r"$2^{\frac{5}{6}} = \sqrt[6]{32}$"),
        ],
        "answer": "C",
    },
    {
        "no": 23,
        "day": 3,
        "topic": r"Üslü - Köklü Denklem Çözümü (Örnek 16)",
        "text": (
            r"$x$ ve $y$ birer gerçek sayı olmak üzere,<br/>"
            r"$\sqrt[4]{25^{x - 1}} = 5^2$<br/>"
            r"$\sqrt[3]{8^{y + 1}} = 2^5$<br/>"
            r"eşitlikleri verilmiştir. <b>Buna göre $x + y$ kaçtır?</b>"
        ),
        "options": [
            ("A", r"$7$"),
            ("B", r"$8$"),
            ("C", r"$9$"),
            ("D", r"$10$"),
            ("E", r"$11$"),
        ],
        "answer": "C",
    },
    {
        "no": 24,
        "day": 3,
        "topic": r"Negatif Tabanlı Üslü - Köklü Eşitlikler (Örnek 16)",
        "text": (
            r"$\sqrt[5]{(-8)^7} = (-2)^a$ ve $\sqrt[5]{(-4)^2} = 2^b$<br/>"
            r"eşitliklerini sağlayan $a$ ve $b$ gerçek sayıları için <b>$a + b$ toplamı kaçtır?</b>"
        ),
        "options": [
            ("A", r"$3$"),
            ("B", r"$\frac{17}{5}$"),
            ("C", r"$4$"),
            ("D", r"$5$"),
            ("E", r"$\frac{29}{5}$"),
        ],
        "answer": "D",
    },
    {
        "no": 25,
        "day": 3,
        "topic": r"Kök Dışına $a\sqrt[n]{b}$ Biçiminde Çıkarma (Örnek 17)",
        "text": (
            r"$a$, $b$ ve $c$ birer pozitif tam sayı olmak üzere,<br/>"
            r"$\sqrt{162} = a\sqrt{2}$<br/>"
            r"$\sqrt[3]{135} = b\sqrt[3]{5}$<br/>"
            r"$\sqrt[4]{162} = c\sqrt[4]{2}$<br/>"
            r"eşitlikleri veriliyor. <b>Buna göre $a + b + c$ toplamı kaçtır?</b>"
        ),
        "options": [
            ("A", r"$12$"),
            ("B", r"$15$"),
            ("C", r"$17$"),
            ("D", r"$18$"),
            ("E", r"$21$"),
        ],
        "answer": "B",
    },
    {
        "no": 26,
        "day": 3,
        "topic": r"Katsayıyı Kök İçine Alma (Örnek 18)",
        "text": (
            r"$a\sqrt[n]{b}$ biçiminde verilen sayıların kök içine alınmış hallerinden hangisi <b>yanlıştır</b>?"
        ),
        "options": [
            ("A", r"$4\sqrt{7} = \sqrt{112}$"),
            ("B", r"$3\sqrt[3]{5} = \sqrt[3]{135}$"),
            ("C", r"$2\sqrt[5]{3} = \sqrt[5]{96}$"),
            ("D", r"$5\sqrt[3]{2} = \sqrt[3]{250}$"),
            ("E", r"$3\sqrt[4]{2} = \sqrt[4]{54}$"),
        ],
        "answer": "E",
    },
    {
        "no": 27,
        "day": 3,
        "topic": r"$\sqrt{N} = a\sqrt{b}$ İkilileri (Örnek 19)",
        "text": (
            r"$a$ ve $b$ birer pozitif tam sayı olmak üzere,<br/>"
            r"$\sqrt{180} = a\sqrt{b}$<br/>"
            r"eşitliğini sağlayan tüm $(a, b)$ ikilileri inceleniyor.<br/>"
            r"<b>Buna göre $a + b$ toplamının alabileceği en büyük değer ile en küçük değerin toplamı kaçtır?</b>"
        ),
        "options": [
            ("A", r"$192$"),
            ("B", r"$196$"),
            ("C", r"$204$"),
            ("D", r"$228$"),
            ("E", r"$262$"),
        ],
        "answer": "A",
    },
    {
        "no": 28,
        "day": 3,
        "topic": r"Küpkökte $\sqrt[3]{N} = a\sqrt[3]{b}$ İkilileri (Örnek 19)",
        "text": (
            r"$a$ ve $b$ birer pozitif tam sayı olmak üzere,<br/>"
            r"$\sqrt[3]{432} = a\sqrt[3]{b}$<br/>"
            r"eşitliğinde <b>$a$'nın alabileceği farklı değerlerin toplamı kaçtır?</b>"
        ),
        "options": [
            ("A", r"$6$"),
            ("B", r"$9$"),
            ("C", r"$10$"),
            ("D", r"$11$"),
            ("E", r"$12$"),
        ],
        "answer": "E",
    },
    {
        "no": 29,
        "day": 3,
        "topic": r"Üslü - Köklü Denklem Çözümü (Örnek 14 & 16)",
        "text": (
            r"$\sqrt[6]{x^4} = 9$<br/>"
            r"eşitliğini sağlayan <b>pozitif $x$ gerçek sayısı kaçtır?</b>"
        ),
        "options": [
            ("A", r"$9$"),
            ("B", r"$27$"),
            ("C", r"$81$"),
            ("D", r"$243$"),
            ("E", r"$729$"),
        ],
        "answer": "B",
    },
    {
        "no": 30,
        "day": 3,
        "topic": r"Kare Alanı ve En Sade $a\sqrt{b}$ Formu (Örnek 3 & 17 & 19)",
        "text": (
            r"Alanı $300$ cm² olan kare şeklindeki bir fayansın bir kenar uzunluğu "
            r"$a\sqrt{b}$ cm biçiminde yazılıyor ($a$ ve $b$ pozitif tam sayılardır).<br/>"
            r"<b>Buna göre $a + b$ toplamının alabileceği en küçük değer kaçtır?</b>"
        ),
        "options": [
            ("A", r"$13$"),
            ("B", r"$17$"),
            ("C", r"$25$"),
            ("D", r"$30$"),
            ("E", r"$77$"),
        ],
        "answer": "A",
    },

    # =========================================================================
    # TEST 4 (12 KASIM 2026 PERŞEMBE) — SORULAR 31 - 40 (Örnek 20-24)
    # =========================================================================
    {
        "no": 31,
        "day": 4,
        "topic": r"Farklı Dereceli Köklerde Tam Sayı Aralığı (Örnek 20 & 22)",
        "text": (
            r"Aşağıdaki köklü ifadelerden hangisi sayı doğrusunda <b>$4$ ile $5$</b> ardışık doğal sayıları arasında yer <b>almaz</b>?"
        ),
        "options": [
            ("A", r"$\sqrt{19}$"),
            ("B", r"$\sqrt[3]{70}$"),
            ("C", r"$2\sqrt{6}$"),
            ("D", r"$\sqrt[4]{250}$"),
            ("E", r"$\sqrt[3]{120}$"),
        ],
        "answer": "D",
    },
    {
        "no": 32,
        "day": 4,
        "topic": r"Katsayılı Köklü Sayının Tam Sayı Aralığı (Örnek 21)",
        "text": (
            r"$7\sqrt{5}$ sayısı aşağıdaki ardışık doğal sayı çiftlerinden hangisinin arasındadır?"
        ),
        "options": [
            ("A", r"$13$ ile $14$"),
            ("B", r"$14$ ile $15$"),
            ("C", r"$15$ ile $16$"),
            ("D", r"$16$ ile $17$"),
            ("E", r"$17$ ile $18$"),
        ],
        "answer": "C",
    },
    {
        "no": 33,
        "day": 4,
        "topic": r"Negatif Köklü İfadenin Tam Sayı Aralığı (Örnek 21)",
        "text": (
            r"$-4\sqrt{7}$ sayısı sayı doğrusunda hangi iki ardışık tam sayı arasındadır?"
        ),
        "options": [
            ("A", r"$-12$ ile $-11$"),
            ("B", r"$-11$ ile $-10$"),
            ("C", r"$-10$ ile $-9$"),
            ("D", r"$-9$ ile $-8$"),
            ("E", r"$-8$ ile $-7$"),
        ],
        "answer": "B",
    },
    {
        "no": 34,
        "day": 4,
        "topic": r"İki Karekök Arasındaki Tam Sayılar (Örnek 23)",
        "text": (
            r"$\sqrt{19} < \sqrt{2x - 1} < \sqrt{41}$<br/>"
            r"olduğuna göre, $x$ yerine yazılabilecek <b>kaç farklı tam sayı</b> değeri vardır?"
        ),
        "options": [
            ("A", r"$10$"),
            ("B", r"$11$"),
            ("C", r"$12$"),
            ("D", r"$13$"),
            ("E", r"$21$"),
        ],
        "answer": "A",
    },
    {
        "no": 35,
        "day": 4,
        "topic": r"İki Tam Sayı Arasındaki Kareköklü Sayı (Örnek 24)",
        "text": (
            r"$5 < \sqrt{x} < 7$<br/>"
            r"eşitsizliğini sağlayan $x$'in alabileceği <b>kaç farklı doğal sayı</b> değeri vardır?"
        ),
        "options": [
            ("A", r"$22$"),
            ("B", r"$23$"),
            ("C", r"$24$"),
            ("D", r"$25$"),
            ("E", r"$26$"),
        ],
        "answer": "B",
    },
    {
        "no": 36,
        "day": 4,
        "topic": r"İki Tam Sayı Arasındaki Küpköklü Sayı (Örnek 22 & 24)",
        "text": (
            r"$2 \leq \sqrt[3]{2x} \leq 4$<br/>"
            r"eşitsizliğini sağlayan $x$'in alabileceği <b>kaç farklı tam sayı</b> değeri vardır?"
        ),
        "options": [
            ("A", r"$25$"),
            ("B", r"$26$"),
            ("C", r"$27$"),
            ("D", r"$28$"),
            ("E", r"$29$"),
        ],
        "answer": "E",
    },
    {
        "no": 37,
        "day": 4,
        "topic": r"Köklü Sayıya En Yakın Tam Sayı (Örnek 20-21)",
        "text": (
            r"Sayı doğrusunda $4\sqrt{5}$ sayısına en yakın tam sayı $A$, $-\sqrt{51}$ sayısına en yakın tam sayı $B$'dir.<br/>"
            r"<b>Buna göre $A + B$ toplamı kaçtır?</b>"
        ),
        "options": [
            ("A", r"$-2$"),
            ("B", r"$-1$"),
            ("C", r"$0$"),
            ("D", r"$1$"),
            ("E", r"$2$"),
        ],
        "answer": "E",
    },
    {
        "no": 38,
        "day": 4,
        "topic": r"İki Köklü İfade Arasındaki Tam Sayı Adedi (Örnek 20-21)",
        "text": (
            r"Sayı doğrusunda $-\sqrt{11}$ ile $3\sqrt{5}$ sayıları arasında yer alan <b>kaç tane tam sayı</b> vardır?"
        ),
        "options": [
            ("A", r"$8$"),
            ("B", r"$9$"),
            ("C", r"$10$"),
            ("D", r"$11$"),
            ("E", r"$12$"),
        ],
        "answer": "C",
    },
    {
        "no": 39,
        "day": 4,
        "topic": r"Ardışık Sınırlar ve Uç Değerlerin Toplamı (Örnek 21-22)",
        "text": (
            r"$a, b, c, d$ birer tam sayı olmak üzere,<br/>"
            r"$a < 5\sqrt{3} < b$ eşitsizliğini sağlayan en büyük $a$ tam sayısı ile,<br/>"
            r"$c < \sqrt[3]{200} < d$ eşitsizliğini sağlayan en küçük $d$ tam sayısının <b>toplamı kaçtır?</b>"
        ),
        "options": [
            ("A", r"$11$"),
            ("B", r"$12$"),
            ("C", r"$13$"),
            ("D", r"$14$"),
            ("E", r"$15$"),
        ],
        "answer": "D",
    },
    {
        "no": 40,
        "day": 4,
        "topic": r"Sayı Doğrusu Üzerinde Aralık Eşleştirme (Örnek 20-22)",
        "diagram": "number_line_klm",
        "text": (
            r"Yukarıdaki eşit bölmelendirilmiş sayı doğrusunda gösterilen $K$, $L$ ve $M$ noktalarına "
            r"karşılık gelen köklü sayılar sırasıyla $(K, L, M)$ aşağıdakilerden hangisi olabilir?"
        ),
        "options": [
            ("A", r"$(\sqrt[3]{19},\; 2\sqrt{6},\; 3\sqrt{5})$"),
            ("B", r"$(\sqrt{10},\; 2\sqrt{5},\; 4\sqrt{3})$"),
            ("C", r"$(\sqrt[3]{28},\; \sqrt{21},\; \sqrt[3]{210})$"),
            ("D", r"$(\sqrt{7},\; 3\sqrt{3},\; 2\sqrt{10})$"),
            ("E", r"$(\sqrt[4]{15},\; 2\sqrt{6},\; 5\sqrt{2})$"),
        ],
        "options_vertical": True,
        "answer": "A",
    },

    # =========================================================================
    # TEST 5 (13 KASIM 2026 CUMA) — SORULAR 41 - 50 (Örnek 25-27)
    # =========================================================================
    {
        "no": 41,
        "day": 5,
        "topic": r"Kök Derecesinin Genişletilmesi (Örnek 25)",
        "text": (
            r"$\sqrt[3]{5} = \sqrt[9]{a}$ ve $\sqrt[4]{3} = \sqrt[12]{b}$<br/>"
            r"eşitliklerini sağlayan $a$ ve $b$ sayıları için <b>$a - b$ farkı kaçtır?</b>"
        ),
        "options": [
            ("A", r"$84$"),
            ("B", r"$92$"),
            ("C", r"$98$"),
            ("D", r"$104$"),
            ("E", r"$152$"),
        ],
        "answer": "C",
    },
    {
        "no": 42,
        "day": 5,
        "topic": r"Kök Derecesi Sadeleştirme ve Zincir Eşitlik (Örnek 25)",
        "text": (
            r"$a, b, c$ pozitif tam sayılar olmak üzere,<br/>"
            r"$\sqrt[10]{32} = \sqrt{a}$ ve $\sqrt[6]{16} = \sqrt[3]{b} = \sqrt[9]{c}$<br/>"
            r"eşitlikleri veriliyor. <b>Buna göre $a + b + c$ toplamı kaçtır?</b>"
        ),
        "options": [
            ("A", r"$68$"),
            ("B", r"$70$"),
            ("C", r"$72$"),
            ("D", r"$74$"),
            ("E", r"$82$"),
        ],
        "answer": "B",
    },
    {
        "no": 43,
        "day": 5,
        "topic": r"Üs Bilinmeyenli Derece Denkleştirme (Örnek 25)",
        "text": (
            r"$x$ ve $y$ birer tam sayı olmak üzere,<br/>"
            r"$\sqrt[4]{3^3} = \sqrt[12]{3^x}$ ve $\sqrt[8]{2^6} = \sqrt[4]{2^y}$<br/>"
            r"eşitlikleri sağlanmaktadır. <b>Buna göre $x \cdot y$ çarpımı kaçtır?</b>"
        ),
        "options": [
            ("A", r"$12$"),
            ("B", r"$18$"),
            ("C", r"$21$"),
            ("D", r"$27$"),
            ("E", r"$36$"),
        ],
        "answer": "D",
    },
    {
        "no": 44,
        "day": 5,
        "topic": r"Aynı Dereceli Kökleri Katsayıyı İçeri Alarak Sıralama (Örnek 26)",
        "text": (
            r"$a = 3\sqrt{6}$, &nbsp; $b = 4\sqrt{3}$ ve $c = 2\sqrt{13}$<br/>"
            r"sayılarının <b>küçükten büyüğe</b> doğru sıralanışı aşağıdakilerden hangisidir?"
        ),
        "options": [
            ("A", r"$b < c < a$"),
            ("B", r"$b < a < c$"),
            ("C", r"$c < b < a$"),
            ("D", r"$c < a < b$"),
            ("E", r"$a < c < b$"),
        ],
        "answer": "A",
    },
    {
        "no": 45,
        "day": 5,
        "topic": r"Negatif Katsayılı Köklü İfadeleri Sıralama (Örnek 26)",
        "text": (
            r"$x = -2\sqrt{11}$, &nbsp; $y = -3\sqrt{5}$ ve $z = -\sqrt{46}$<br/>"
            r"sayılarının <b>büyükten küçüğe</b> doğru sıralanışı aşağıdakilerden hangisidir?"
        ),
        "options": [
            ("A", r"$z > y > x$"),
            ("B", r"$y > x > z$"),
            ("C", r"$y > z > x$"),
            ("D", r"$x > z > y$"),
            ("E", r"$x > y > z$"),
        ],
        "answer": "E",
    },
    {
        "no": 46,
        "day": 5,
        "topic": r"Farklı Kök Derecelerinde Derece Eşitleyerek Sıralama (Örnek 27)",
        "text": (
            r"$a = \sqrt[3]{5}$, &nbsp; $b = \sqrt[4]{7}$ ve $c = \sqrt[6]{20}$<br/>"
            r"sayılarının <b>küçükten büyüğe</b> doğru sıralanışı aşağıdakilerden hangisidir?"
        ),
        "options": [
            ("A", r"$a < b < c$"),
            ("B", r"$a < c < b$"),
            ("C", r"$b < a < c$"),
            ("D", r"$b < c < a$"),
            ("E", r"$c < b < a$"),
        ],
        "answer": "D",
    },
    {
        "no": 47,
        "day": 5,
        "topic": r"Tam Sayı ile Farklı Dereceli Kökleri Sıralama (Örnek 27)",
        "text": (
            r"$x = 2$, &nbsp; $y = \sqrt[3]{9}$ ve $z = \sqrt[6]{80}$<br/>"
            r"sayılarının <b>doğru sıralanışı</b> aşağıdakilerden hangisidir?"
        ),
        "options": [
            ("A", r"$x < y < z$"),
            ("B", r"$y < z < x$"),
            ("C", r"$x < z < y$"),
            ("D", r"$z < x < y$"),
            ("E", r"$z < y < x$"),
        ],
        "answer": "C",
    },
    {
        "no": 48,
        "day": 5,
        "topic": r"İkili Derece Eşitleme Stratejisi ile Sıralama (Örnek 25 & 27)",
        "text": (
            r"$k = \sqrt{6}$, &nbsp; $m = \sqrt[3]{15}$ ve $n = \sqrt[4]{35}$<br/>"
            r"sayılarının <b>küçükten büyüğe</b> doğru sıralanışı aşağıdakilerden hangisidir?"
        ),
        "options": [
            ("A", r"$m < k < n$"),
            ("B", r"$n < k < m$"),
            ("C", r"$n < m < k$"),
            ("D", r"$k < n < m$"),
            ("E", r"$k < m < n$"),
        ],
        "answer": "B",
    },
    {
        "no": 49,
        "day": 5,
        "topic": r"Basit Kesirli Farklı Dereceli Kök Sıralaması (Örnek 27)",
        "text": (
            r"$a = \sqrt[3]{\frac{1}{2}}$, &nbsp; $b = \sqrt[4]{\frac{1}{3}}$ ve $c = \sqrt[6]{\frac{1}{5}}$<br/>"
            r"sayılarının <b>küçükten büyüğe</b> doğru sıralanışı aşağıdakilerden hangisidir?"
        ),
        "options": [
            ("A", r"$b < c < a$"),
            ("B", r"$a < b < c$"),
            ("C", r"$c < b < a$"),
            ("D", r"$a < c < b$"),
            ("E", r"$b < a < c$"),
        ],
        "answer": "A",
    },
    {
        "no": 50,
        "day": 5,
        "topic": r"Farklı Dereceli Kökler Arasındaki Tam Sayılar (Örnek 25 & 26)",
        "text": (
            r"$2\sqrt{2} < \sqrt[4]{x} < 3$<br/>"
            r"eşitsizliğini sağlayan $x$'in alabileceği <b>kaç farklı tam sayı</b> değeri vardır?"
        ),
        "options": [
            ("A", r"$12$"),
            ("B", r"$13$"),
            ("C", r"$14$"),
            ("D", r"$15$"),
            ("E", r"$16$"),
        ],
        "answer": "E",
    },

    # =========================================================================
    # TEST 6 (14 KASIM 2026 CUMARTESİ) — SORULAR 51 - 60 (Örnek 28-31 & Sentez)
    # =========================================================================
    {
        "no": 51,
        "day": 6,
        "topic": r"Kroki / Konum Sıralama Problemi (Örnek 28)",
        "diagram": "corner_cafe_kutuphane",
        "table_data": [
            ["Durum", "Efe", "Mert", "Kaan"],
            ["I", r"$2\sqrt{5}$ m", r"$3\sqrt{3}$ m", r"$4\sqrt{2}$ m"],
            ["II", r"$3\sqrt{2}$ m", r"$2\sqrt{6}$ m", r"$5$ m"],
            ["III", r"$4$ m", r"$2\sqrt{5}$ m", r"$3\sqrt{2}$ m"],
        ],
        "text": (
            r"Yukarıdaki meydanda bulunan Efe, Mert ve Kaan'ın <b>Kütüphane</b>'ye olan uzaklıkları sırasıyla "
            r"$4\sqrt{3}$ m, $5\sqrt{2}$ m ve $3\sqrt{5}$ m'dir.<br/>"
            r"<b>Buna göre Efe, Mert ve Kaan'ın Kafe'ye olan uzaklıkları tablodakilerden hangileri olabilir?</b>"
        ),
        "options": [
            ("A", "Yalnız I"),
            ("B", "Yalnız II"),
            ("C", "Yalnız III"),
            ("D", "I ve II"),
            ("E", "I, II ve III"),
        ],
        "answer": "D",
    },
    {
        "no": 52,
        "day": 6,
        "topic": r"Ölçeklendirilmiş Gösterge Problemi (Örnek 29)",
        "diagram": "gauge_bar",
        "text": (
            r"Yukarıdaki sanayi makinesine ait basınç göstergesi, gerçek basıncın $\frac{1}{4}$'ünü gösterecek şekilde tasarlanmıştır "
            r"(örneğin gerçek basınç $32$ bar iken ibre $8$'i gösterir).<br/>"
            r"<b>Buna göre gerçek basınç $\sqrt{780}$ bar iken gösterge ibresi hangi iki tam sayı arasında ve hangisine daha yakın konumda durur?</b>"
        ),
        "options": [
            ("A", r"$5$ ile $6$ arasında, $6$'ya yakın"),
            ("B", r"$6$ ile $7$ arasında, $6$'ya yakın"),
            ("C", r"$6$ ile $7$ arasında, $7$'ye yakın"),
            ("D", r"$7$ ile $8$ arasında, $7$'ye yakın"),
            ("E", r"$7$ ile $8$ arasında, $8$'e yakın"),
        ],
        "options_vertical": True,
        "answer": "C",
    },
    {
        "no": 53,
        "day": 6,
        "topic": r"Paralel Çizgili Defter / Karton Uzunluğu (Örnek 30)",
        "diagram": "lined_notebook",
        "text": (
            r"Yukarıdaki birbirine paralel ve eşit mesafeli çizgilerden oluşan defterde, "
            r"uzun kenarı $\sqrt{288}$ birim olan mavi renkli dikdörtgen kartonun iki farklı görünümü verilmiştir.<br/>"
            r"<b>Buna göre bu dikdörtgenin kısa kenar uzunluğunun alabileceği kaç farklı tam sayı değeri vardır?</b>"
        ),
        "options": [
            ("A", r"$4$"),
            ("B", r"$5$"),
            ("C", r"$6$"),
            ("D", r"$7$"),
            ("E", r"$8$"),
        ],
        "answer": "B",
    },
    {
        "no": 54,
        "day": 6,
        "topic": r"Yol Çalışması / Şerit Analizi (Örnek 31)",
        "diagram": "road_lanes",
        "text": (
            r"İzmir–Manisa kara yolunda $6$. ile $11$. kilometreler arası ile $18$. ile $23$. kilometreler arası "
            r"yol çalışması nedeniyle <b>tek şeritli</b>, diğer kısımlar ise <b>çift şeritli</b> olarak kullanılmaktadır.<br/>"
            r"<b>Buna göre aşağıda İzmir'e uzaklıkları kilometre cinsinden verilen araçlardan hangisi çift şeritli yolda hareket etmektedir?</b>"
        ),
        "options": [
            ("A", r"$3\sqrt{7}$"),
            ("B", r"$4\sqrt{5}$"),
            ("C", r"$6\sqrt{3}$"),
            ("D", r"$5\sqrt{13}$"),
            ("E", r"$4\sqrt{17}$"),
        ],
        "answer": "E",
    },
    {
        "no": 55,
        "day": 6,
        "topic": r"Alt Geçit Yükseklik Limiti Problemi (Örnek 18, 22, 31)",
        "text": (
            r"Maksimum geçiş yüksekliği $4$ metre olan bir köprü altı geçidinden "
            r"yükseklikleri metre cinsinden aşağıda verilen tırlardan <b>kaç tanesi geçebilir</b>?<br/>"
            r"I. $2\sqrt[3]{7}$ &nbsp;&nbsp;&nbsp; II. $\sqrt[4]{240}$ &nbsp;&nbsp;&nbsp; III. $3\sqrt{2}$<br/>"
            r"IV. $2\sqrt{3}$ &nbsp;&nbsp;&nbsp; V. $\sqrt[3]{70}$"
        ),
        "options": [
            ("A", r"$1$"),
            ("B", r"$2$"),
            ("C", r"$3$"),
            ("D", r"$4$"),
            ("E", r"$5$"),
        ],
        "answer": "C",
    },
    {
        "no": 56,
        "day": 6,
        "topic": r"Kare Tablo Alanı, $a\sqrt{b}$ Formu ve Aralık Sentezi (Örnek 3, 17, 20)",
        "text": (
            r"Alanı $162$ cm² olan kare şeklindeki bir tablonun kenar uzunluğu $a\sqrt{2}$ cm, "
            r"alanı $180$ cm² olan başka bir kare tablonun kenar uzunluğu ise $k$ ve $k+1$ ardışık tam sayıları arasındadır.<br/>"
            r"<b>Buna göre $a + k$ toplamı kaçtır?</b>"
        ),
        "options": [
            ("A", r"$19$"),
            ("B", r"$20$"),
            ("C", r"$21$"),
            ("D", r"$22$"),
            ("E", r"$23$"),
        ],
        "answer": "D",
    },
    {
        "no": 57,
        "day": 6,
        "topic": r"Parite Çıkarımı ve Mutlak Değer Sentezi (Örnek 5, 9, 10)",
        "text": (
            r"$m$ ve $n$, $1$'den büyük birer tam sayı olmak üzere,<br/>"
            r"$\sqrt[m]{(-4)^m} - \sqrt[n]{(-5)^n} = -9$<br/>"
            r"eşitliği veriliyor. $A = \sqrt[m+1]{(-3)^{m+1}}$, $B = \sqrt[n+1]{(-7)^{n+1}}$ ve $C = \sqrt{(-1)^2}$ olduğuna göre, "
            r"<b>$A + B + C$ toplamı kaçtır?</b>"
        ),
        "options": [
            ("A", r"$-9$"),
            ("B", r"$-3$"),
            ("C", r"$3$"),
            ("D", r"$9$"),
            ("E", r"$11$"),
        ],
        "answer": "B",
    },
    {
        "no": 58,
        "day": 6,
        "topic": r"Eşit Raf Aralıklı Kule Yüksekliği (Örnek 30 varyasyonu)",
        "diagram": "shelf_boxes",
        "text": (
            r"Eşit aralıklı yatay raflara sahip bir dolabın yanındaki bilgi paneli, yerleştirilen kolilerin toplam yüksekliğini "
            r"$\sqrt{245}$ cm olarak göstermektedir. Koli yığını $4$ raf aralığından fazla, $5$ raf aralığından az yer kaplamaktadır.<br/>"
            r"<b>Buna göre bu dolaptaki $2$ raf aralığının toplam yüksekliğinin alabileceği tam sayı değeri kaç cm'dir?</b>"
        ),
        "options": [
            ("A", r"$3$"),
            ("B", r"$4$"),
            ("C", r"$5$"),
            ("D", r"$6$"),
            ("E", r"$7$"),
        ],
        "answer": "E",
    },
    {
        "no": 59,
        "day": 6,
        "topic": r"Kare Kenar Aralığından Tam Sayı Alan Sayma (Örnek 3 & 21 & 24)",
        "text": (
            r"$x$ bir tam sayı olmak üzere, alanı $x$ cm² olan bir karenin bir kenar uzunluğu "
            r"$4\sqrt{2}$ cm ile $2\sqrt{10}$ cm arasındadır.<br/>"
            r"<b>Buna göre bu karenin alanı $x$'in alabileceği kaç farklı tam sayı değeri vardır?</b>"
        ),
        "options": [
            ("A", r"$7$"),
            ("B", r"$8$"),
            ("C", r"$9$"),
            ("D", r"$10$"),
            ("E", r"$11$"),
        ],
        "answer": "A",
    },
    {
        "no": 60,
        "day": 6,
        "topic": r"Büyük Sentez: Tanım Aralığı, Sadeleştirme ve Derece Eşitleme (Örnek 8, 14, 25, 27)",
        "text": (
            r"$x$ bir gerçek sayı olmak üzere, $\sqrt{x - 3} + \sqrt[4]{3 - x}$ ifadesi bir gerçek sayıdır.<br/>"
            r"Buna göre,<br/>"
            r"$A = \sqrt[3]{x^2}$, &nbsp; $B = \sqrt[4]{(x + 1)^2}$, &nbsp; $C = \sqrt[6]{(x + 2)^3}$<br/>"
            r"<b>sayılarının küçükten büyüğe doğru sıralanışı aşağıdakilerden hangisidir?</b>"
        ),
        "options": [
            ("A", r"$B < A < C$"),
            ("B", r"$A < B < C$"),
            ("C", r"$B < C < A$"),
            ("D", r"$C < B < A$"),
            ("E", r"$A < C < B$"),
        ],
        "answer": "A",
    },
]
