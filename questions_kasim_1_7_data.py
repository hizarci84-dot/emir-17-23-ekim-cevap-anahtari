# -*- coding: utf-8 -*-
"""
EMİR 1-7 KASIM TARİHLERİ ÜSLÜ SAYILAR ÖDEVLENDİRME
Maarif Modeli Video Ders Kitabı (Sayfa 7-23) Ayrıntılı Analiziyle Hazırlanmış
Daha Önce Kullanılmamış Yeni Tarzda 6 Adet Çoktan Seçmeli Test (6 Gün x 10 Soru = 60 Soru)
"""

TEST_INFO = {
    1: ("1. GÜN TESTİ (1 KASIM 2026)", "Test 1 (Sorular 1 – 10): Üslü İfadelerde Toplama-Çıkarma ve Ortak Parantez"),
    2: ("2. GÜN TESTİ (2 KASIM 2026)", "Test 2 (Sorular 11 – 20): Üslü İfadelerde Sıralama ve Eşitsizlikler"),
    3: ("3. GÜN TESTİ (3 KASIM 2026)", "Test 3 (Sorular 21 – 30): Bilimsel Gösterim ve Çok Büyük/Küçük Sayılar"),
    4: ("4. GÜN TESTİ (4 KASIM 2026)", "Test 4 (Sorular 31 – 40): Sayı Doğrusu, Modelleme ve Basamak Analizi"),
    5: ("5. GÜN TESTİ (5 KASIM 2026)", "Test 5 (Sorular 41 – 50): Üslü Denklemler ve Birbiri Türünden Yazma"),
    6: ("6. GÜN TESTİ (6-7 KASIM 2026)", "Test 6 (Sorular 51 – 60): Bağlam Temelli Üslü Sayılar Sentez Testi"),
}

QUESTIONS_KASIM_1_7 = [
    # =========================================================================
    # TEST 1 (1 KASIM 2026) — SORULAR 1 - 10 (Üslü Toplama-Çıkarma / Sayfa 14)
    # =========================================================================
    {
        "no": 1,
        "day": 1,
        "topic": "Üslü Sayılarda Toplama-Çıkarma (Örnek 46)",
        "text": (
            "7 · 2<sup>6</sup> + 5 · 4<sup>3</sup> - 4 · 8<sup>2</sup><br/>"
            "<b>işleminin sonucu aşağıdakilerden hangisidir?</b>"
        ),
        "options": [("A", "2<sup>7</sup>"), ("B", "2<sup>8</sup>"), ("C", "2<sup>9</sup>"), ("D", "2<sup>10</sup>"), ("E", "2<sup>11</sup>")],
        "answer": "C",
    },
    {
        "no": 2,
        "day": 1,
        "topic": "Ondalık Katsayılı Üslü Toplama (Örnek 46)",
        "text": (
            "(0,48 · 10<sup>-5</sup> + 0,32 · 10<sup>-5</sup> - 0,05 · 10<sup>-4</sup>) / (1,5 · 10<sup>-6</sup>)<br/>"
            "<b>işleminin sonucu kaçtır?</b>"
        ),
        "options": [("A", "1"), ("B", "2"), ("C", "3"), ("D", "4"), ("E", "5")],
        "answer": "B",
    },
    {
        "no": 3,
        "day": 1,
        "topic": "Rasyonel Üslü Sadeleştirme (Örnek 47)",
        "text": (
            "(5 · 3<sup>10</sup>) / (9<sup>6</sup> - 6 · 27<sup>3</sup>)<br/>"
            "<b>işleminin sonucu kaçtır?</b>"
        ),
        "options": [("A", "5/7"), ("B", "5/6"), ("C", "1"), ("D", "6/5"), ("E", "7/5")],
        "answer": "A",
    },
    {
        "no": 4,
        "day": 1,
        "topic": "Ortak Çarpan Parantezi (Örnek 47)",
        "text": (
            "(2<sup>13</sup> + 2<sup>12</sup> - 2<sup>10</sup>) / (2<sup>11</sup> - 2<sup>9</sup>)<br/>"
            "<b>işleminin sonucu kaçtır?</b>"
        ),
        "options": [("A", "11/3"), ("B", "14/3"), ("C", "16/3"), ("D", "22/3"), ("E", "8")],
        "answer": "D",
    },
    {
        "no": 5,
        "day": 1,
        "topic": "Çarpım ve Tekrarlı Toplam Eşitliği (Örnek 48)",
        "text": (
            "a bir gerçek sayı olmak üzere,<br/>"
            "5<sup>2</sup> · 5<sup>4</sup> · 5<sup>5</sup> = 25<sup>a</sup> + 25<sup>a</sup> + 25<sup>a</sup> + 25<sup>a</sup> + 25<sup>a</sup><br/>"
            "eşitliği sağlanmaktadır.<br/>"
            "<b>Buna göre a değeri kaçtır?</b>"
        ),
        "options": [("A", "3"), ("B", "4"), ("C", "5"), ("D", "6"), ("E", "7")],
        "answer": "C",
    },
    {
        "no": 6,
        "day": 1,
        "topic": "Tekrarlı Toplam ve Çarpım Oranı (Örnek 49)",
        "text": (
            "m bir gerçek sayı olmak üzere,<br/>"
            "A = 2<sup>m</sup> + 2<sup>m</sup> + ... + 2<sup>m</sup> (32 tane 2<sup>m</sup>'nin toplamı)<br/>"
            "B = 2<sup>m</sup> · 2<sup>m</sup> · ... · 2<sup>m</sup> (6 tane 2<sup>m</sup>'nin çarpımı)<br/>"
            "olarak veriliyor. <b>A / B = 1/32 olduğuna göre m kaçtır?</b>"
        ),
        "options": [("A", "2"), ("B", "3"), ("C", "4"), ("D", "5"), ("E", "6")],
        "answer": "A",
    },
    {
        "no": 7,
        "day": 1,
        "topic": "Üslü Toplama ve Kütle Problemi (Örnek 50)",
        "text": (
            "Bir ilaç fabrikasında üretilen özdeş kapsüllerin her birinin kütlesi 5<sup>-6</sup> gramdır. "
            "K kutusunda bu kapsüllerden 25<sup>3</sup> adet, L kutusunda ise 4 · 125<sup>2</sup> adet bulunmaktadır.<br/>"
            "<b>Buna göre K ve L kutularında bulunan kapsüllerin toplam kütlesi kaç gramdır?</b>"
        ),
        "options": [("A", "1"), ("B", "5"), ("C", "10"), ("D", "25"), ("E", "125")],
        "answer": "B",
    },
    {
        "no": 8,
        "day": 1,
        "topic": "Mikro-Kondansatör Kapasite Toplamı (Örnek 50)",
        "text": (
            "Bir elektronik devredeki her bir mikro-kondansatörün enerji kapasitesi 10<sup>-9</sup> joule'dür. "
            "Birinci devrede 4<sup>4</sup> adet, ikinci devrede 8<sup>3</sup> adet ve üçüncü devrede "
            "16<sup>2</sup> adet bu mikro-kondansatörlerden bulunmaktadır.<br/>"
            "<b>Buna göre üç devredeki mikro-kondansatörlerin toplam enerji kapasitesi kaç joule'dür?</b>"
        ),
        "options": [
            ("A", "1,28 · 10<sup>-7</sup>"),
            ("B", "2,56 · 10<sup>-7</sup>"),
            ("C", "5,12 · 10<sup>-7</sup>"),
            ("D", "6,4 · 10<sup>-7</sup>"),
            ("E", "1,024 · 10<sup>-6</sup>"),
        ],
        "answer": "E",
    },
    {
        "no": 9,
        "day": 1,
        "topic": "Birim Dönüşümlü Üslü Çıkarma (Örnek 51)",
        "table_data": [
            ["Birim", "Karşılığı"],
            ["1 palet", "9 koli"],
            ["1 koli", "27 kutu"],
        ],
        "text": (
            "Bir züccaciyede bardakların paketlenmesinde kullanılan palet, koli ve kutu birimleri "
            "arasındaki ilişki yukarıdaki tabloda verilmiştir.<br/>"
            "<b>Depodaki 3<sup>5</sup> palet bardağın 3<sup>8</sup> kutuluk kısmı satıldığına göre, "
            "geriye kaç koli bardak kalmıştır?</b>"
        ),
        "options": [
            ("A", "2 · 3<sup>5</sup>"),
            ("B", "4 · 3<sup>5</sup>"),
            ("C", "6 · 3<sup>5</sup>"),
            ("D", "8 · 3<sup>5</sup>"),
            ("E", "8 · 3<sup>6</sup>"),
        ],
        "answer": "D",
    },
    {
        "no": 10,
        "day": 1,
        "topic": "Veri Birimleri Dönüşümlü Çıkarma (Örnek 51)",
        "table_data": [
            ["Veri Birimi", "Alt Birim Karşılığı"],
            ["1 blok", "16 küme"],
            ["1 küme", "8 sektör"],
        ],
        "text": (
            "Bir veri merkezindeki depolama birimleri arasındaki ilişki yukarıdaki tabloda verilmiştir.<br/>"
            "<b>Toplam 2<sup>8</sup> blokluk depolama alanının 2<sup>13</sup> sektörlük kısmı dolu "
            "olduğuna göre, boş kalan kısım kaç kümedir?</b>"
        ),
        "options": [
            ("A", "2<sup>9</sup>"),
            ("B", "2<sup>10</sup>"),
            ("C", "3 · 2<sup>9</sup>"),
            ("D", "2<sup>11</sup>"),
            ("E", "3 · 2<sup>10</sup>"),
        ],
        "answer": "E",
    },

    # =========================================================================
    # TEST 2 (2 KASIM 2026) — SORULAR 11 - 20 (Üslü Sıralama / Sayfa 15)
    # =========================================================================
    {
        "no": 11,
        "day": 2,
        "topic": "Tabanları Eşitleyerek Sıralama (Örnek 52)",
        "text": (
            "• x = 27<sup>13</sup><br/>"
            "• y = 9<sup>19</sup><br/>"
            "• z = 81<sup>10</sup><br/>"
            "<b>olduğuna göre x, y ve z sayılarının küçükten büyüğe doğru sıralanışı aşağıdakilerden hangisidir?</b>"
        ),
        "options": [("A", "x < y < z"), ("B", "y < x < z"), ("C", "y < z < x"), ("D", "z < x < y"), ("E", "z < y < x")],
        "answer": "B",
    },
    {
        "no": 12,
        "day": 2,
        "topic": "Negatif Kuvvetlerde Sıralama (Örnek 52)",
        "text": (
            "• A = 8<sup>-12</sup><br/>"
            "• B = 4<sup>-17</sup><br/>"
            "• C = 16<sup>-8</sup><br/>"
            "<b>olduğuna göre A, B ve C sayılarının küçükten büyüğe doğru sıralanışı aşağıdakilerden hangisidir?</b>"
        ),
        "options": [("A", "A < B < C"), ("B", "A < C < B"), ("C", "B < A < C"), ("D", "C < B < A"), ("E", "C < A < B")],
        "answer": "A",
    },
    {
        "no": 13,
        "day": 2,
        "topic": "Üslü Sayı Aralık Tahmini (Örnek 53)",
        "text": (
            "a, b ve c birer gerçek sayı olmak üzere;<br/>"
            "• 2<sup>a</sup> = 90<br/>"
            "• 3<sup>b</sup> = 200<br/>"
            "• 5<sup>c</sup> = 600<br/>"
            "<b>olduğuna göre a, b ve c sayılarının küçükten büyüğe doğru sıralanışı hangisidir?</b>"
        ),
        "options": [("A", "a < b < c"), ("B", "b < c < a"), ("C", "c < b < a"), ("D", "c < a < b"), ("E", "b < a < c")],
        "answer": "C",
    },
    {
        "no": 14,
        "day": 2,
        "topic": "Üslü Sayı Aralık Tahmini (Örnek 53)",
        "text": (
            "x, y ve z birer gerçek sayı olmak üzere;<br/>"
            "• 3<sup>x</sup> = 50<br/>"
            "• 2<sup>y</sup> = 40<br/>"
            "• 5<sup>z</sup> = 100<br/>"
            "<b>olduğuna göre x, y ve z sayılarının küçükten büyüğe doğru sıralanışı hangisidir?</b>"
        ),
        "options": [("A", "x < y < z"), ("B", "x < z < y"), ("C", "y < x < z"), ("D", "z < x < y"), ("E", "z < y < x")],
        "answer": "D",
    },
    {
        "no": 15,
        "day": 2,
        "topic": "Üsleri Eşitleyerek Sıralama (Örnek 54)",
        "text": (
            "• K = 2<sup>105</sup><br/>"
            "• L = 3<sup>75</sup><br/>"
            "• M = 5<sup>45</sup><br/>"
            "<b>olduğuna göre K, L ve M sayılarının küçükten büyüğe doğru sıralanışı hangisidir?</b>"
        ),
        "options": [("A", "K < L < M"), ("B", "K < M < L"), ("C", "L < K < M"), ("D", "M < L < K"), ("E", "M < K < L")],
        "answer": "E",
    },
    {
        "no": 16,
        "day": 2,
        "topic": "Üsleri Eşitleyerek Sıralama (Örnek 54)",
        "text": (
            "• a = 6<sup>40</sup><br/>"
            "• b = 15<sup>30</sup><br/>"
            "• c = 32<sup>20</sup><br/>"
            "<b>olduğuna göre a, b ve c sayılarının küçükten büyüğe doğru sıralanışı hangisidir?</b>"
        ),
        "options": [("A", "c < a < b"), ("B", "a < c < b"), ("C", "b < a < c"), ("D", "c < b < a"), ("E", "a < b < c")],
        "answer": "A",
    },
    {
        "no": 17,
        "day": 2,
        "topic": "Basit Kesir Tabanlı Eşitsizlik (Örnek 55)",
        "text": (
            "x, y ve z birer pozitif tam sayı olmak üzere,<br/>"
            "(4/7)<sup>x</sup> &lt; (4/7)<sup>y</sup> &lt; (4/7)<sup>z</sup><br/>"
            "eşitsizliği veriliyor.<br/>"
            "<b>Buna göre x, y ve z değerlerinin küçükten büyüğe doğru sıralanışı hangisidir?</b>"
        ),
        "options": [("A", "x < y < z"), ("B", "x < z < y"), ("C", "y < x < z"), ("D", "z < y < x"), ("E", "z < x < y")],
        "answer": "D",
    },
    {
        "no": 18,
        "day": 2,
        "topic": "Rasyonel Tabanlı Üslü Eşitsizlik (Örnek 55)",
        "text": (
            "(3/4)<sup>2x - 5</sup> &gt; (16/9)<sup>-4</sup><br/>"
            "<b>eşitsizliğini sağlayan en büyük x tam sayısı kaçtır?</b>"
        ),
        "options": [("A", "4"), ("B", "5"), ("C", "6"), ("D", "7"), ("E", "8")],
        "answer": "C",
    },
    {
        "no": 19,
        "day": 2,
        "topic": "Ondalık Çarpanlı Negatif Üs Sıralaması (Örnek 56)",
        "text": (
            "• x = (0,6) · (5<sup>-2</sup>)<br/>"
            "• y = (0,6) · (2<sup>-2</sup>)<br/>"
            "• z = (0,6) · (3<sup>-2</sup>)<br/>"
            "<b>olduğuna göre x, y ve z değerlerinin küçükten büyüğe doğru sıralanışı hangisidir?</b>"
        ),
        "options": [("A", "y < z < x"), ("B", "x < z < y"), ("C", "x < y < z"), ("D", "z < x < y"), ("E", "y < x < z")],
        "answer": "B",
    },
    {
        "no": 20,
        "day": 2,
        "topic": "Rasyonel Kuvvetlerle Bağlam Sıralaması (Örnek 57)",
        "table_data": [
            ["Sunucu", "Veri Aktarım Verimlilik Oranı"],
            ["1. Sunucu", "(81/16)<sup>-3</sup>"],
            ["2. Sunucu", "(8/27)<sup>5</sup>"],
            ["3. Sunucu", "(4/9)<sup>7</sup>"],
        ],
        "text": (
            "Üç farklı bulut sunucusunun veri aktarım verimlilik oranları yukarıdaki tabloda verilmiştir.<br/>"
            "<b>Buna göre bu sunucuların verimlilik oranlarının küçükten büyüğe doğru sıralanışı hangisidir?</b>"
        ),
        "options": [
            ("A", "1. Sunucu < 2. Sunucu < 3. Sunucu"),
            ("B", "1. Sunucu < 3. Sunucu < 2. Sunucu"),
            ("C", "2. Sunucu < 1. Sunucu < 3. Sunucu"),
            ("D", "3. Sunucu < 2. Sunucu < 1. Sunucu"),
            ("E", "2. Sunucu < 3. Sunucu < 1. Sunucu"),
        ],
        "options_vertical": True,
        "answer": "E",
    },

    # =========================================================================
    # TEST 3 (3 KASIM 2026) — SORULAR 21 - 30 (Bilimsel Gösterim / Sayfa 16)
    # =========================================================================
    {
        "no": 21,
        "day": 3,
        "topic": "Bilimsel Gösterim Tanımı (Örnek 58-59)",
        "text": (
            "Bir uzay teleskobunun 1 yılda kaydettiği veri miktarı 0,00064 · 10<sup>13</sup> bayttır. "
            "Bu sayının bilimsel gösterimi a · 10<sup>n</sup> şeklindedir.<br/>"
            "<b>Buna göre a + n toplamı kaçtır?</b>"
        ),
        "options": [("A", "14,4"), ("B", "15,4"), ("C", "16,4"), ("D", "17,4"), ("E", "18,4")],
        "answer": "B",
    },
    {
        "no": 22,
        "day": 3,
        "topic": "Çok Küçük Sayılarda Birim Dönüşümü (Örnek 60)",
        "text": (
            "Bir virüsün çapı ortalama 0,00000012 metredir.<br/>"
            "• 1 metre = 1000 milimetre<br/>"
            "<b>Buna göre bu virüsün çapının milimetre cinsinden bilimsel gösterimi aşağıdakilerden hangisidir?</b>"
        ),
        "options": [
            ("A", "1,2 · 10<sup>-4</sup>"),
            ("B", "1,2 · 10<sup>-5</sup>"),
            ("C", "1,2 · 10<sup>-6</sup>"),
            ("D", "1,2 · 10<sup>-9</sup>"),
            ("E", "1,2 · 10<sup>-10</sup>"),
        ],
        "answer": "A",
    },
    {
        "no": 23,
        "day": 3,
        "topic": "Toplama İşleminin Bilimsel Gösterimi (Örnek 61)",
        "text": (
            "• x = 0,0036 · 10<sup>9</sup><br/>"
            "• y = 44 · 10<sup>4</sup><br/>"
            "<b>olduğuna göre x + y toplamının bilimsel gösterimi aşağıdakilerden hangisidir?</b>"
        ),
        "options": [
            ("A", "4,04 · 10<sup>5</sup>"),
            ("B", "4,04 · 10<sup>6</sup>"),
            ("C", "4,04 · 10<sup>7</sup>"),
            ("D", "8 · 10<sup>5</sup>"),
            ("E", "8 · 10<sup>6</sup>"),
        ],
        "answer": "B",
    },
    {
        "no": 24,
        "day": 3,
        "topic": "Çarpma İşleminin Bilimsel Gösterimi (Örnek 61)",
        "text": (
            "• A = 0,0008 · 10<sup>-3</sup><br/>"
            "• B = 2500 · 10<sup>8</sup><br/>"
            "<b>olduğuna göre A · B çarpımının bilimsel gösterimi aşağıdakilerden hangisidir?</b>"
        ),
        "options": [
            ("A", "2 · 10<sup>3</sup>"),
            ("B", "2 · 10<sup>4</sup>"),
            ("C", "2 · 10<sup>5</sup>"),
            ("D", "2 · 10<sup>6</sup>"),
            ("E", "2 · 10<sup>7</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 25,
        "day": 3,
        "topic": "Gezegenler Arası Süre ve Bilimsel Gösterim (Örnek 62)",
        "text": (
            "Dünya ile Mars arasındaki yörünge uzaklığının 2,25 · 10<sup>8</sup> km olduğu bir anda, "
            "saatteki ortalama hızı 7,5 · 10<sup>4</sup> km olan bir uzay sondası fırlatılıyor.<br/>"
            "<b>Buna göre sondanın bu mesafeyi alma süresinin dakika cinsinden bilimsel gösterimi nedir?</b>"
        ),
        "options": [
            ("A", "3 · 10<sup>3</sup>"),
            ("B", "1,8 · 10<sup>4</sup>"),
            ("C", "3 · 10<sup>4</sup>"),
            ("D", "1,8 · 10<sup>5</sup>"),
            ("E", "1,8 · 10<sup>6</sup>"),
        ],
        "answer": "D",
    },
    {
        "no": 26,
        "day": 3,
        "topic": "Hacim ve Damla Sayısı Bilimsel Gösterimi (Örnek 63)",
        "text": (
            "Bir su damlasının hacmi yaklaşık 0,00005 litredir. (1 metreküp = 1000 litre)<br/>"
            "<b>Buna göre 400 metreküp suyun yaklaşık kaç su damlasına karşılık geldiğinin "
            "bilimsel gösterimi aşağıdakilerden hangisidir?</b>"
        ),
        "options": [
            ("A", "8 · 10<sup>7</sup>"),
            ("B", "8 · 10<sup>8</sup>"),
            ("C", "8 · 10<sup>9</sup>"),
            ("D", "8 · 10<sup>10</sup>"),
            ("E", "8 · 10<sup>11</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 27,
        "day": 3,
        "topic": "Elektrik Tüketim Maliyeti Bilimsel Gösterimi (Örnek 64)",
        "text": (
            "Bir tekstil atölyesindeki lazer kesim makinesi çalışma süresi boyunca toplam "
            "4 · 10<sup>5</sup> metre kumaş kesmiştir. Makine her 500 metre kesimde ortalama "
            "0,25 kWh elektrik tüketmektedir. Elektriğin 1 Wh maliyeti 0,003 TL'dir. (1 kWh = 1000 Wh)<br/>"
            "<b>Buna göre bu süreçte ödenen toplam elektrik ücretinin TL cinsinden bilimsel gösterimi nedir?</b>"
        ),
        "options": [
            ("A", "6 · 10<sup>-2</sup>"),
            ("B", "6 · 10<sup>-1</sup>"),
            ("C", "6 · 10<sup>0</sup>"),
            ("D", "6 · 10<sup>1</sup>"),
            ("E", "6 · 10<sup>2</sup>"),
        ],
        "answer": "E",
    },
    {
        "no": 28,
        "day": 3,
        "topic": "Güneş Santrali Enerji Üretimi (Örnek 64)",
        "text": (
            "Bir güneş enerjisi santralinde 2,5 · 10<sup>4</sup> adet panel bulunmaktadır. Her bir panel "
            "günde ortalama 0,0032 MWh elektrik üretmektedir. (1 MWh = 10<sup>6</sup> Wh)<br/>"
            "<b>Buna göre bu santralin 30 günde ürettiği toplam elektrik enerjisinin Wh cinsinden "
            "bilimsel gösterimi aşağıdakilerden hangisidir?</b>"
        ),
        "options": [
            ("A", "2,4 · 10<sup>7</sup>"),
            ("B", "2,4 · 10<sup>8</sup>"),
            ("C", "8 · 10<sup>8</sup>"),
            ("D", "2,4 · 10<sup>9</sup>"),
            ("E", "2,4 · 10<sup>10</sup>"),
        ],
        "answer": "D",
    },
    {
        "no": 29,
        "day": 3,
        "topic": "Biyolojik Ölçek ve Bilimsel Gösterim (Örnek 63)",
        "text": (
            "Yetişkin bir insanın vücudunda ortalama 5 litre kan bulunmakta olup, 1 mm<sup>3</sup> kanda "
            "yaklaşık 4,8 · 10<sup>6</sup> adet alyuvar hücresi vardır. (1 litre = 10<sup>6</sup> mm<sup>3</sup>)<br/>"
            "<b>Buna göre yetişkin bir insanın vücudundaki toplam alyuvar hücresi sayısının "
            "bilimsel gösterimi aşağıdakilerden hangisidir?</b>"
        ),
        "options": [
            ("A", "2,4 · 10<sup>11</sup>"),
            ("B", "2,4 · 10<sup>12</sup>"),
            ("C", "4,8 · 10<sup>12</sup>"),
            ("D", "9,6 · 10<sup>12</sup>"),
            ("E", "2,4 · 10<sup>13</sup>"),
        ],
        "answer": "E",
    },
    {
        "no": 30,
        "day": 3,
        "topic": "Nano-Kaplama Kalınlığı (Örnek 60)",
        "text": (
            "Bir optik mercek üzerine her bir katmanı 0,0000025 cm kalınlığında olan koruyucu nano-film "
            "kaplanacaktır. Mercek üzerine üst üste 80 katman kaplandığında oluşan toplam kaplama "
            "kalınlığının <b>metre</b> cinsinden bilimsel gösterimi nedir? (1 m = 100 cm)"
        ),
        "options": [
            ("A", "2 · 10<sup>-6</sup>"),
            ("B", "2 · 10<sup>-5</sup>"),
            ("C", "2 · 10<sup>-4</sup>"),
            ("D", "2,5 · 10<sup>-6</sup>"),
            ("E", "2,5 · 10<sup>-5</sup>"),
        ],
        "answer": "A",
    },

    # =========================================================================
    # TEST 4 (4 KASIM 2026) — SORULAR 31 - 40 (Sayı Doğrusu, Modelleme ve Basamak)
    # =========================================================================
    {
        "no": 31,
        "day": 4,
        "topic": "Sayı Doğrusunda Üslü Uzaklık (Örnek 11)",
        "text": (
            "a bir tam sayı olmak üzere, sayı doğrusu üzerinde a<sup>1</sup> ve a<sup>0</sup> değerleri "
            "işaretlenmiştir. Sayı doğrusu üzerinde a<sup>1</sup> noktası a<sup>0</sup> noktasının "
            "7 birim solunda yer almaktadır.<br/>"
            "<b>Buna göre sayı doğrusunda a<sup>1</sup> noktası ile a<sup>2</sup> noktası arasındaki "
            "uzaklık kaç birimdir?</b>"
        ),
        "options": [("A", "30"), ("B", "35"), ("C", "36"), ("D", "42"), ("E", "49")],
        "answer": "D",
    },
    {
        "no": 32,
        "day": 4,
        "topic": "Sayı Doğrusunda Eş Bölmeler ve Negatif Üs (Örnek 24)",
        "text": (
            "x, y ve z birer tam sayı olmak üzere; sayı doğrusu üzerindeki 0 ile 1 arası 4 eş parçaya, "
            "-1 ile 0 arası ise 8 eş parçaya ayrılmıştır.<br/>"
            "• 0'ın sağındaki 1. bölme noktası 2<sup>x</sup>, 2. bölme noktası 2<sup>y</sup>,<br/>"
            "• 0'ın solundaki 1. bölme noktası (-2)<sup>z</sup><br/>"
            "olarak işaretlenmiştir. <b>Buna göre (x + z)<sup>y</sup> ifadesinin değeri kaçtır?</b>"
        ),
        "options": [("A", "-1/5"), ("B", "-1/3"), ("C", "1/5"), ("D", "1/25"), ("E", "-5")],
        "answer": "A",
    },
    {
        "no": 33,
        "day": 4,
        "topic": "İç İçe Geometrik Kutu Modellemesi (Örnek 12)",
        "text": (
            "a pozitif bir tam sayı olmak üzere, bir dikdörtgenin içine yazılan a sayısı her "
            "dikdörtgen katmanı için 5 · a şeklinde modelleniyor (Örneğin 1 dikdörtgen içinde a = 5a).<br/>"
            "<b>İç içe n tane dikdörtgenin en içine 125 sayısı yazıldığında elde edilen ifadenin "
            "eşiti 5<sup>14</sup> olduğuna göre n değeri kaçtır?</b>"
        ),
        "options": [("A", "9"), ("B", "10"), ("C", "11"), ("D", "12"), ("E", "13")],
        "answer": "C",
    },
    {
        "no": 34,
        "day": 4,
        "topic": "Sembol Fonksiyon Modellemesi (Örnek 23)",
        "text": (
            "a sıfırdan farklı bir gerçek sayı olmak üzere;<br/>"
            "• Üçgen içinde a: Δ(a) = -3<sup>a + 1</sup><br/>"
            "• Daire içinde a: ○(a) = (-2)<sup>a + 2</sup><br/>"
            "şeklinde modelleniyor.<br/>"
            "<b>Buna göre Δ(2) + ○(3) işleminin sonucu kaçtır?</b>"
        ),
        "options": [("A", "-59"), ("B", "-5", ), ("C", "5"), ("D", "59"), ("E", "61")],
        "answer": "A",
    },
    {
        "no": 35,
        "day": 4,
        "topic": "Üslü Eşitlikte Sembol Değerleri (Örnek 10)",
        "text": (
            "□ bir tam sayı ve Δ bir pozitif tam sayı olmak üzere,<br/>"
            "□<sup>Δ</sup> = 81<br/>"
            "eşitliği sağlanmaktadır.<br/>"
            "<b>Buna göre □ + Δ toplamının alabileceği en büyük değer ile en küçük değerin toplamı kaçtır?</b>"
        ),
        "options": [("A", "73"), ("B", "75"), ("C", "77"), ("D", "83"), ("E", "93")],
        "answer": "B",
    },
    {
        "no": 36,
        "day": 4,
        "topic": "Basamak Sayısı Bulma (Örnek 35)",
        "text": (
            "27 · 4<sup>7</sup> · 25<sup>6</sup><br/>"
            "<b>çarpımının sonucu kaç basamaklı bir doğal sayıdır?</b>"
        ),
        "options": [("A", "13"), ("B", "14"), ("C", "15"), ("D", "16"), ("E", "17")],
        "answer": "C",
    },
    {
        "no": 37,
        "day": 4,
        "topic": "Sondan Kaç Basamağı 9'dur (Örnek 35)",
        "text": (
            "16<sup>4</sup> · 125<sup>5</sup> - 1<br/>"
            "<b>işleminin sonucunda elde edilen doğal sayının sondan kaç basamağı 9'dur?</b>"
        ),
        "options": [("A", "12"), ("B", "13"), ("C", "14"), ("D", "15"), ("E", "16")],
        "answer": "D",
    },
    {
        "no": 38,
        "day": 4,
        "topic": "Bellek Aktarımı ve Boş Kalan Oran (Örnek 26)",
        "text": (
            "X markası 2<sup>8</sup> GB kapasiteli belleğin 8<sup>-1</sup>'i, Y markası 4<sup>3</sup> GB "
            "kapasiteli belleğin ise 2<sup>-1</sup>'i doludur.<br/>"
            "<b>Y marka bellekteki verilerin tamamı X marka belleğe aktarılırsa, X marka belleğin "
            "kaçta kaçı BOŞ kalır?</b>"
        ),
        "options": [("A", "1/8"), ("B", "1/4"), ("C", "1/2"), ("D", "5/8"), ("E", "3/4")],
        "answer": "E",
    },
    {
        "no": 39,
        "day": 4,
        "topic": "Hücre Bölünmesi Modellemesi (Örnek 44)",
        "text": (
            "Bir laboratuvarda başlangıçta 12 adet bulunan özel bir bakteri türü, her 20 dakikada "
            "bir bölünerek sayısını 3 katına çıkarmaktadır.<br/>"
            "<b>Buna göre 2 saatin sonunda ortamda toplam kaç adet bakteri bulunur?</b>"
        ),
        "options": [
            ("A", "4 · 3<sup>5</sup>"),
            ("B", "4 · 3<sup>6</sup>"),
            ("C", "3<sup>7</sup>"),
            ("D", "2 · 3<sup>7</sup>"),
            ("E", "4 · 3<sup>7</sup>"),
        ],
        "answer": "E",
    },
    {
        "no": 40,
        "day": 4,
        "topic": "Dikdörtgen ve Kare Alan-Çevre Geçişi (Örnek 45)",
        "text": (
            "Kenar uzunlukları 25<sup>x</sup> birim ve 9<sup>x + 1</sup> birim olan bir dikdörtgenin "
            "alanı 2025 birimkaredir.<br/>"
            "<b>Buna göre bir kenar uzunluğu 15<sup>x</sup> birim olan bir karenin çevresi kaç birimdir?</b>"
        ),
        "options": [("A", "45"), ("B", "60"), ("C", "75"), ("D", "90"), ("E", "120")],
        "answer": "B",
    },

    # =========================================================================
    # TEST 5 (5 KASIM 2026) — SORULAR 41 - 50 (Üslü Denklemler & Türünden Yazma)
    # =========================================================================
    {
        "no": 41,
        "day": 5,
        "topic": "İç İçe Negatif Kuvvet İşlemi (Örnek 18-22)",
        "text": (
            "((2<sup>-1</sup> + 1)<sup>-1</sup> - 3<sup>-1</sup>)<sup>-2</sup><br/>"
            "<b>ifadesinin eşiti kaçtır?</b>"
        ),
        "options": [("A", "9"), ("B", "3"), ("C", "1/3"), ("D", "1/9"), ("E", "-9")],
        "answer": "A",
    },
    {
        "no": 42,
        "day": 5,
        "topic": "Negatif Kuvvet Değer Hesabı (Örnek 19)",
        "text": (
            "a<sup>x</sup> = 2 ve b<sup>x</sup> = 6 olduğuna göre,<br/>"
            "a<sup>-2x</sup> · b<sup>x</sup> + b<sup>-x</sup><br/>"
            "<b>işleminin sonucu kaçtır?</b>"
        ),
        "options": [("A", "4/3"), ("B", "5/3"), ("C", "2"), ("D", "7/3"), ("E", "8/3")],
        "answer": "B",
    },
    {
        "no": 43,
        "day": 5,
        "topic": "Birbiri Türünden Eşiti (Örnek 20)",
        "text": (
            "2<sup>x</sup> - 3 = a olduğuna göre,<br/>"
            "2<sup>-x + 2</sup> + 1<br/>"
            "<b>ifadesinin a türünden eşiti aşağıdakilerden hangisidir?</b>"
        ),
        "options": [
            ("A", "(a + 4) / (a + 3)"),
            ("B", "(a + 5) / (a + 3)"),
            ("C", "(a + 7) / (a + 3)"),
            ("D", "(2a + 5) / (a + 3)"),
            ("E", "(a + 7) / (a - 3)"),
        ],
        "answer": "C",
    },
    {
        "no": 44,
        "day": 5,
        "topic": "Cebirsel Üslü İfade Sadeleştirme (Örnek 30)",
        "text": (
            "x ≠ 0 olmak üzere,<br/>"
            "((-3x<sup>3</sup>)<sup>2</sup> · (-x<sup>2</sup>)<sup>3</sup>) / (-x<sup>4</sup>)<sup>2</sup><br/>"
            "<b>ifadesinin en sade hâli aşağıdakilerden hangisidir?</b>"
        ),
        "options": [("A", "-9x<sup>4</sup>"), ("B", "-3x<sup>4</sup>"), ("C", "3x<sup>4</sup>"), ("D", "9x<sup>4</sup>"), ("E", "-9x<sup>6</sup>")],
        "answer": "A",
    },
    {
        "no": 45,
        "day": 5,
        "topic": "Üslü Denklem Çözümü (Örnek 37)",
        "text": (
            "15<sup>2x - 1</sup> / 3<sup>2x - 1</sup> = 125<sup>x - 2</sup><br/>"
            "<b>eşitliğini sağlayan x değeri kaçtır?</b>"
        ),
        "options": [("A", "3"), ("B", "4"), ("C", "5"), ("D", "6"), ("E", "7")],
        "answer": "C",
    },
    {
        "no": 46,
        "day": 5,
        "topic": "Üslü Denklemde Değer Bulma (Örnek 40)",
        "text": (
            "36<sup>x</sup> = 4<sup>x + 2</sup> olduğuna göre,<br/>"
            "<b>27<sup>x</sup> ifadesinin değeri kaçtır?</b>"
        ),
        "options": [("A", "16"), ("B", "27"), ("C", "32"), ("D", "64"), ("E", "81")],
        "answer": "D",
    },
    {
        "no": 47,
        "day": 5,
        "topic": "Zincirleme Üslü Eşitlikler (Örnek 41)",
        "text": (
            "a, b ve c gerçek sayılar olmak üzere;<br/>"
            "• 3<sup>a</sup> = 5<br/>"
            "• 5<sup>b</sup> = 8<br/>"
            "• 2<sup>c</sup> = 81<br/>"
            "<b>olduğuna göre a · b · c çarpımı kaçtır?</b>"
        ),
        "options": [("A", "6"), ("B", "8"), ("C", "9"), ("D", "12"), ("E", "16")],
        "answer": "D",
    },
    {
        "no": 48,
        "day": 5,
        "topic": "Asal Çarpanlarla Türünden Yazma (Örnek 42)",
        "text": (
            "2<sup>x</sup> = m ve 5<sup>x</sup> = n olduğuna göre,<br/>"
            "<b>200<sup>x</sup> ifadesinin m ve n türünden eşiti aşağıdakilerden hangisidir?</b>"
        ),
        "options": [("A", "m<sup>2</sup> · n<sup>2</sup>"), ("B", "m<sup>2</sup> · n<sup>3</sup>"), ("C", "m<sup>3</sup> · n"), ("D", "m<sup>4</sup> · n<sup>2</sup>"), ("E", "m<sup>3</sup> · n<sup>2</sup>")],
        "answer": "E",
    },
    {
        "no": 49,
        "day": 5,
        "topic": "Ondalık Tabanı Türünden Yazma (Örnek 42)",
        "text": (
            "3<sup>x</sup> = a ve 5<sup>x</sup> = b olduğuna göre,<br/>"
            "<b>(1,8)<sup>x</sup> ifadesinin a ve b türünden eşiti aşağıdakilerden hangisidir?</b>"
        ),
        "options": [("A", "a / b"), ("B", "a<sup>2</sup> / b"), ("C", "a / b<sup>2</sup>"), ("D", "a<sup>2</sup> · b"), ("E", "2a / b")],
        "answer": "B",
    },
    {
        "no": 50,
        "day": 5,
        "topic": "İki Bilinmeyenli Üslü Sistem (Örnek 43)",
        "text": (
            "x, m ve n pozitif gerçek sayılar olmak üzere;<br/>"
            "• x<sup>2m - n</sup> = 18<br/>"
            "• x<sup>2m + n</sup> = 72<br/>"
            "eşitlikleri sağlanmaktadır.<br/>"
            "<b>Buna göre x<sup>m</sup> + x<sup>n</sup> toplamı kaçtır?</b>"
        ),
        "options": [("A", "5"), ("B", "6"), ("C", "7"), ("D", "9"), ("E", "8")],
        "answer": "E",
    },

    # =========================================================================
    # TEST 6 (6-7 KASIM 2026) — SORULAR 51 - 60 (Bağlam Temelli Sentez Testi)
    # =========================================================================
    {
        "no": 51,
        "day": 6,
        "topic": "Bağlam Temelli Bölme ve Üs (Sentez)",
        "text": (
            "Uzunluğu 12<sup>4</sup> mm olan metal bir çubuk önce 4 eş parçaya, ardından elde edilen "
            "her bir parça tekrar 9 eş parçaya bölünüyor.<br/>"
            "<b>Son durumda elde edilen en küçük parçalardan birinin uzunluğu kaç milimetredir?</b>"
        ),
        "options": [("A", "24<sup>2</sup>"), ("B", "18<sup>2</sup>"), ("C", "16<sup>2</sup>"), ("D", "12<sup>3</sup>"), ("E", "36<sup>2</sup>")],
        "answer": "A",
    },
    {
        "no": 52,
        "day": 6,
        "topic": "Bulut Yedekleme Maliyeti (Sentez)",
        "text": (
            "Bir şirketin 32<sup>3</sup> GB büyüklüğündeki veri tabanı her gece sıkıştırılarak boyutu "
            "1/8'ine düşürülmekte ve bulut sunucusuna yedeklenmektedir. Bulut sunucusu her 1 GB veri "
            "için gecelik 2<sup>-5</sup> TL ücret almaktadır.<br/>"
            "<b>Buna göre 16 gecelik yedekleme için ödenecek toplam ücret kaç TL'dir?</b>"
        ),
        "options": [("A", "2<sup>9</sup>"), ("B", "2<sup>11</sup>"), ("C", "2<sup>12</sup>"), ("D", "2<sup>13</sup>"), ("E", "2<sup>14</sup>")],
        "answer": "B",
    },
    {
        "no": 53,
        "day": 6,
        "topic": "Karbon Ayak İzi ve Bilimsel Gösterim (Sentez)",
        "text": (
            "Bir sanayi tesisi yılda 3,6 · 10<sup>7</sup> kg karbon emisyonu üretmektedir. Yetişkin "
            "bir çam ağacı yılda ortalama 24 kg karbonu atmosferden temizlemektedir.<br/>"
            "<b>Tesisin 1 yıllık karbon emisyonunun %40'ını dengelemek için dikilmesi gereken çam "
            "ağacı sayısının bilimsel gösterimi nedir?</b>"
        ),
        "options": [
            ("A", "6 · 10<sup>4</sup>"),
            ("B", "1,5 · 10<sup>5</sup>"),
            ("C", "6 · 10<sup>5</sup>"),
            ("D", "1,5 · 10<sup>6</sup>"),
            ("E", "6 · 10<sup>6</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 54,
        "day": 6,
        "topic": "3B Yazıcı Filament Tüketimi (Sentez)",
        "text": (
            "Bir 3B yazıcı A model bir parçayı basarken 3 · 2<sup>6</sup> cm, B model bir parçayı "
            "basarken ise 5 · 2<sup>5</sup> cm filament kullanmaktadır.<br/>"
            "<b>Bu yazıcıda 8 adet A modeli ve 16 adet B modeli basıldığında toplam kaç santimetre "
            "filament kullanılır?</b>"
        ),
        "options": [("A", "2<sup>10</sup>"), ("B", "2<sup>11</sup>"), ("C", "3 · 2<sup>10</sup>"), ("D", "2<sup>12</sup>"), ("E", "2<sup>13</sup>")],
        "answer": "D",
    },
    {
        "no": 55,
        "day": 6,
        "topic": "Etken Madde Azalımı (Sentez)",
        "text": (
            "Bir hastaya verilen 810 mg'lık bir ilacın kandaki etken madde miktarı, geçen her 2 saatin "
            "sonunda bir önceki miktarın 2/3'üne düşmektedir.<br/>"
            "<b>Buna göre ilaç verildikten 8 saat sonra hastanın kanında kaç mg etken madde kalır?</b>"
        ),
        "options": [("A", "80"), ("B", "120"), ("C", "135"), ("D", "180"), ("E", "160")],
        "answer": "E",
    },
    {
        "no": 56,
        "day": 6,
        "topic": "Güneş Enerjili Sokak Lambası (Sentez)",
        "text": (
            "Güneş enerjili bir sokak lambası gündüz boyunca bataryasında 4<sup>5</sup> Wh enerji "
            "depolamaktadır. Gece olduğunda lamba ilk 4 saat boyunca saatte 2<sup>7</sup> Wh, sonraki "
            "6 saat boyunca ise tasarruf moduna geçerek saatte 2<sup>6</sup> Wh enerji harcamaktadır.<br/>"
            "<b>Sabaha karşı lamba kapandığında bataryasında kalan enerji kaç Wh'dir?</b>"
        ),
        "options": [("A", "2<sup>7</sup>"), ("B", "2<sup>8</sup>"), ("C", "3 · 2<sup>6</sup>"), ("D", "2<sup>9</sup>"), ("E", "3 · 2<sup>7</sup>")],
        "answer": "A",
    },
    {
        "no": 57,
        "day": 6,
        "topic": "Kargo Dronu Menzil Hesabı (Sentez)",
        "text": (
            "Bir kargo dronunun tam dolu batarya ile uçabildiği menzil, taşıdığı paketin kütlesi her "
            "2 katına çıktığında 3/4 katına düşmektedir. Dron 250 gram yük ile tam dolu bataryayla "
            "64 km uçabilmektedir.<br/>"
            "<b>Buna göre dron 2 kg (2000 gram) yük ile tam dolu bataryayla kaç km uçabilir?</b>"
        ),
        "options": [("A", "18"), ("B", "27"), ("C", "32"), ("D", "36"), ("E", "48")],
        "answer": "B",
    },
    {
        "no": 58,
        "day": 6,
        "topic": "Mikro-İşlemci Transistör Yoğunluğu (Sentez)",
        "text": (
            "Yeni nesil bir işlemcinin yüzey alanı 4 cm<sup>2</sup> olup, her 1 mm<sup>2</sup>'lik "
            "alanında 2,5 · 10<sup>7</sup> adet transistör bulunmaktadır. (1 cm<sup>2</sup> = 100 mm<sup>2</sup>)<br/>"
            "<b>Bu işlemcideki toplam transistör sayısının bilimsel gösterimi aşağıdakilerden hangisidir?</b>"
        ),
        "options": [
            ("A", "1 · 10<sup>8</sup>"),
            ("B", "1 · 10<sup>9</sup>"),
            ("C", "1 · 10<sup>10</sup>"),
            ("D", "2,5 · 10<sup>9</sup>"),
            ("E", "2,5 · 10<sup>10</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 59,
        "day": 6,
        "topic": "İnternet Paket Hızlarının Karşılaştırılması (Sentez)",
        "text": (
            "Emir'in incelediği üç farklı fiber internet paketinin veri indirme hızları:<br/>"
            "• A Paketi: 25<sup>6</sup> Kbps<br/>"
            "• B Paketi: 125<sup>4</sup> Kbps<br/>"
            "• C Paketi: 5<sup>11</sup> + 5 · 5<sup>11</sup> Kbps<br/>"
            "<b>Buna göre bu üç paketin indirme hızları arasındaki doğru sıralama hangisidir?</b>"
        ),
        "options": [("A", "A < B < C"), ("B", "B < A < C"), ("C", "C < A = B"), ("D", "A = B < C"), ("E", "A = B = C")],
        "answer": "D",
    },
    {
        "no": 60,
        "day": 6,
        "topic": "E-Kitap Okuyucu Bellek Hesabı (Sentez)",
        "text": (
            "Bir e-kitap okuyucuda her bir sayfası ortalama 2<sup>11</sup> bayt yer kaplayan 512 sayfalı "
            "e-kitaplardan 12 tanesi ile her bir sayfası 2<sup>12</sup> bayt yer kaplayan 256 sayfalı "
            "e-kitaplardan 20 tanesi kayıtlıdır. (1 MB = 2<sup>20</sup> bayt)<br/>"
            "<b>Bu e-kitapların tamamı bellekte toplam kaç MB yer kaplar?</b>"
        ),
        "options": [("A", "2<sup>3</sup>"), ("B", "2<sup>4</sup>"), ("C", "24"), ("D", "28"), ("E", "2<sup>5</sup>")],
        "answer": "E",
    },
]
