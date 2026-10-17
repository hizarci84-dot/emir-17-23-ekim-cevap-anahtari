# -*- coding: utf-8 -*-
"""
Maarif Modeli Video Ders Kitabı Sayfa 17-23 (Bağlam Temelli Sorular)
- İlk 29 Soru: Sayfa 17-23 arasındaki orijinal sorular (aslına sadık kalınarak 5 şıklı çoktan seçmeli).
- Sonraki 61 Soru (30-90): Bu 29 soruya benzer kurgulanmış 61 bağlam temelli soru.
Toplam: 90 Soru (6 Gün x 15 Soru/Gün).
"""

QUESTIONS_17_23 = [
    # =========================================================================
    # 1. GÜN (SORULAR 1 - 15) — ORİJİNAL SORULAR (SAYFA 17 - 20)
    # =========================================================================
    {
        "no": 1,
        "day": 1,
        "is_original": True,
        "page": 17,
        "image": "cropped_figs/fig_q01.png",
        "img_height": 95,
        "text": (
            "Kenar uzunluklarının oranı sabit kalacak şekilde tasarlanan dikdörtgen bir aynanın "
            "iki farklı modeli yukarıda verilmiştir.<br/>"
            "<b>Buna göre büyük modeldeki x uzunluğu kaç birimdir?</b>"
        ),
        "options": [
            ("A", "2<sup>12</sup>"),
            ("B", "2<sup>14</sup>"),
            ("C", "2<sup>16</sup>"),
            ("D", "3<sup>8</sup>"),
            ("E", "6<sup>8</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 2,
        "day": 1,
        "is_original": True,
        "page": 17,
        "image": "cropped_figs/fig_q02.png",
        "img_height": 90,
        "text": (
            "Yukarıda iki farklı özellikteki dizüstü bilgisayar görseli verilmiştir. "
            "Bilgisayarın bir işlemi yapma süresi çekirdek sayısı ile ters orantılıdır. "
            "Şekil 1'deki bilgisayar bir işlemi 8<sup>-2</sup> saniyede yapmaktadır.<br/>"
            "<b>Buna göre Şekil 2'deki bilgisayar aynı işlemi kaç saniyede yapar?</b>"
        ),
        "options": [
            ("A", "2<sup>-5</sup>"),
            ("B", "2<sup>-4</sup>"),
            ("C", "2<sup>-3</sup>"),
            ("D", "2<sup>-2</sup>"),
            ("E", "2<sup>-1</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 3,
        "day": 1,
        "is_original": True,
        "page": 17,
        "text": (
            "Zeynep'in elinde 10<sup>13</sup> adet 10 kuruşluk madeni para, Mehmet'in elinde ise "
            "10<sup>n</sup> adet 100 TL'lik banknot bulunmaktadır.<br/>"
            "<b>Zeynep ve Mehmet'in elindeki paralar TL türünden birbirine eşit olduğuna göre "
            "n değerini bulunuz.</b>"
        ),
        "options": [
            ("A", "8"),
            ("B", "9"),
            ("C", "10"),
            ("D", "11"),
            ("E", "12"),
        ],
        "answer": "C",
    },
    {
        "no": 4,
        "day": 1,
        "is_original": True,
        "page": 17,
        "text": (
            "18 ilçesi bulunan bir ilin her ilçesinde 24 mahalle, her mahallede ise 4 okul bulunmaktadır. "
            "Bu ildeki tüm okulların her birine eşit sayıda kitap dağıtılmıştır.<br/>"
            "<b>Dağıtılan toplam kitap sayısı 12<sup>5</sup> olduğuna göre bir okula dağıtılan kitap sayısı kaçtır?</b>"
        ),
        "options": [
            ("A", "72"),
            ("B", "96"),
            ("C", "108"),
            ("D", "120"),
            ("E", "144"),
        ],
        "answer": "E",
    },
    {
        "no": 5,
        "day": 1,
        "is_original": True,
        "page": 17,
        "image": "cropped_figs/fig_q05.png",
        "img_height": 100,
        "text": (
            "Yukarıdaki görselde Hakan'ın hesabında bulunan kripto paraların miktarları ve "
            "TL türünden değerleri gösterilmiştir.<br/>"
            "<b>Buna göre A coin'in TL türünden birim değerinin B coin'in TL türünden birim değerine oranı kaçtır?</b>"
        ),
        "options": [
            ("A", "750"),
            ("B", "1000"),
            ("C", "1200"),
            ("D", "1500"),
            ("E", "1800"),
        ],
        "answer": "D",
    },
    {
        "no": 6,
        "day": 1,
        "is_original": True,
        "page": 18,
        "text": (
            "A ortamında bulunan bakteriler her bir saatin sonunda 8 katına çıkarken B ortamında "
            "bulunan bakteriler her bir saatin sonunda 32 katına çıkmaktadır. Başlangıçta A ortamında "
            "64<sup>2</sup> tane bakteri bulunurken B ortamında 32<sup>4</sup> tane bakteri bulunmaktadır.<br/>"
            "<b>2 saatlik sürenin sonunda B ortamında bulunan bakteri sayısı ile t saatlik sürenin "
            "sonunda A ortamında bulunan bakteri sayısına eşittir. Buna göre t kaçtır?</b>"
        ),
        "options": [
            ("A", "4"),
            ("B", "5"),
            ("C", "6"),
            ("D", "7"),
            ("E", "8"),
        ],
        "answer": "C",
    },
    {
        "no": 7,
        "day": 1,
        "is_original": True,
        "page": 18,
        "text": (
            "2023 yılında YKS sınavına giren 3600000 öğrencilerin 13/25'i baraj altında kalmış, "
            "baraj altında kalmayan öğrencilerin 18/25'i istedikleri bölüme yerleşmiş, istedikleri "
            "bölüme yerleşen öğrencilerin 1/5'i 2028 yılında yerleştikleri bölümden mezun olmuştur.<br/>"
            "<b>Buna göre 2023 yılında sınava giren öğrencilerden kaç tanesi 2028 yılında mezun olmuştur?</b>"
        ),
        "options": [
            ("A", "2<sup>9</sup> · 3<sup>4</sup>"),
            ("B", "2<sup>10</sup> · 3<sup>4</sup>"),
            ("C", "2<sup>10</sup> · 3<sup>5</sup>"),
            ("D", "2<sup>11</sup> · 3<sup>5</sup>"),
            ("E", "2<sup>12</sup> · 3<sup>4</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 8,
        "day": 1,
        "is_original": True,
        "page": 18,
        "text": (
            "Dijital veri birimleri arasında 1 GB = 2<sup>30</sup> bayt ve 1 TB = 2<sup>40</sup> bayt "
            "ilişkisi bulunmaktadır.<br/>"
            "Murat, bilgisayarında bulunan 8<sup>5</sup> GB büyüklüğündeki verinin boyutunu bir program "
            "yardımıyla başlangıçtaki boyutunun %25'ine düşürüyor.<br/>"
            "<b>Murat, bu veriyi tamamı boş olan 16 TB'lık taşınabilir belleğe yüklediğinde "
            "taşınabilir belleğin kaçta kaçı dolu olur?</b>"
        ),
        "options": [
            ("A", "1/8"),
            ("B", "1/4"),
            ("C", "3/8"),
            ("D", "1/2"),
            ("E", "3/4"),
        ],
        "answer": "D",
    },
    {
        "no": 9,
        "day": 1,
        "is_original": True,
        "page": 18,
        "image": "cropped_figs/fig_q09.png",
        "img_height": 85,
        "text": (
            "Nuri bir bilim dergisinin yukarıdaki sayfasını okumaktadır.<br/>"
            "<b>Dergideki verilere göre Dünya'daki doğrudan içilebilir veya kullanılabilir yüzey suları "
            "kaç kilogramdır?</b>"
        ),
        "options": [
            ("A", "4 · 10<sup>15</sup>"),
            ("B", "4 · 10<sup>16</sup>"),
            ("C", "4 · 10<sup>17</sup>"),
            ("D", "1,6 · 10<sup>17</sup>"),
            ("E", "1,6 · 10<sup>18</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 10,
        "day": 1,
        "is_original": True,
        "page": 18,
        "text": (
            "Bir ekonomistin gelecek yıllardaki ekonomik durumlarla ilgili öngörüsü aşağıdaki gibidir:<br/>"
            "• Her üç yıllık sürenin sonunda kamu çalışanlarının maaşları 2 katına çıkacaktır.<br/>"
            "• Her dört yıllık sürenin sonunda altının gram fiyatı 16 katına çıkacaktır.<br/>"
            "<b>Kamuda çalışan bir kişi 2016 yılında bir aylık maaşıyla 2<sup>5</sup> gram altın alabildiğine "
            "göre 2028 yılında aynı kamu çalışanı kaç gram altın alabilir?</b>"
        ),
        "options": [
            ("A", "2<sup>-4</sup>"),
            ("B", "2<sup>-3</sup>"),
            ("C", "2<sup>-2</sup>"),
            ("D", "2<sup>-1</sup>"),
            ("E", "1"),
        ],
        "answer": "B",
    },
    {
        "no": 11,
        "day": 1,
        "is_original": True,
        "page": 19,
        "image": "cropped_figs/fig_q11.png",
        "img_height": 105,
        "text": (
            "Yukarıda desibel ile ses şiddeti arasındaki ilişkiyi gösteren bir görsel verilmiştir.<br/>"
            "<b>Buna göre 130 desibel sesin şiddeti 50 desibel sesin şiddetinin kaç katıdır?</b>"
        ),
        "options": [
            ("A", "10<sup>6</sup>"),
            ("B", "10<sup>7</sup>"),
            ("C", "10<sup>8</sup>"),
            ("D", "10<sup>9</sup>"),
            ("E", "10<sup>10</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 12,
        "day": 1,
        "is_original": True,
        "page": 19,
        "text": (
            "• Geleneksel sulama sisteminde her bir saatte toprağa 8<sup>3</sup> litre su verilmektedir.<br/>"
            "• Akıllı sulama sisteminde ise nem sensörleri sayesinde her bir saatte 4<sup>4</sup> litre su verilmektedir.<br/>"
            "<b>54 saatlik sürede geleneksel sistem yerine akıllı sistem ile yapılacak sulama "
            "24<sup>n</sup> litre su tasarrufu sağlayacaktır. Buna göre n kaçtır?</b>"
        ),
        "options": [
            ("A", "2"),
            ("B", "3"),
            ("C", "4"),
            ("D", "5"),
            ("E", "6"),
        ],
        "answer": "B",
    },
    {
        "no": 13,
        "day": 1,
        "is_original": True,
        "page": 19,
        "text": (
            "Bir mahallede bulunan hayırsever fırıncı ihtiyaç sahipleri için \"Askıda Ekmek\" kampanyası başlatmıştır:<br/>"
            "• Kampanyanın ilk ayında askıya bırakılan toplam ekmek sayısı 64<sup>2</sup>'dir.<br/>"
            "• Her ay içerisinde askıya bırakılan ekmek sayısı bir önceki ayda askıya bırakılan ekmek sayısının 1,25 katı olmaktadır.<br/>"
            "<b>Buna göre kampanyanın 4. ayında askıya bırakılan ekmek sayısı kaçtır?</b>"
        ),
        "options": [
            ("A", "4000"),
            ("B", "5000"),
            ("C", "6400"),
            ("D", "8000"),
            ("E", "10000"),
        ],
        "answer": "D",
    },
    {
        "no": 14,
        "day": 1,
        "is_original": True,
        "page": 20,
        "image": "cropped_figs/fig_q14.png",
        "img_height": 135,
        "text": (
            "Sevgi, televizyonda bulaşık makinesi reklamına denk gelmiştir. Sevgi, suyun 1 tonunun "
            "64 TL olduğu bir ilde bir ay içerisinde 25 defa bulaşıkları elde yıkamaktadır.<br/>"
            "<b>Sevgi bir ay içerisinde bulaşıkları elde yıkamak yerine bulaşık makinesinde yıkarsa "
            "kaç TL daha az su faturası öder?</b>"
        ),
        "options": [
            ("A", "120"),
            ("B", "140"),
            ("C", "160"),
            ("D", "180"),
            ("E", "200"),
        ],
        "answer": "C",
    },
    {
        "no": 15,
        "day": 1,
        "is_original": True,
        "page": 20,
        "text": (
            "8 kişinin bulunduğu bir aile WhatsApp grubunda paylaşılan medya dosyalarıyla ilgili "
            "aşağıdaki bilgiler bilinmektedir:<br/>"
            "• Gruptaki her kişi günde ortalama 8 MB dosya paylaşmaktadır.<br/>"
            "• Grupta bir gün içinde paylaşılan tüm dosyalar, gönderen kişi de dâhil olmak üzere "
            "her üyenin telefonuna otomatik olarak kaydedilmektedir.<br/>"
            "<b>32 gün boyunca bu gruptan gelen dosyalar nedeniyle telefonun depolama alanının "
            "dolduğunu gören Sevgi, bu dosyaların %12,5'ini silerse telefonunda kaç MB yer açılır?</b>"
        ),
        "options": [
            ("A", "2<sup>6</sup>"),
            ("B", "2<sup>7</sup>"),
            ("C", "2<sup>8</sup>"),
            ("D", "2<sup>9</sup>"),
            ("E", "2<sup>10</sup>"),
        ],
        "answer": "C",
    },

    # =========================================================================
    # 2. GÜN (SORULAR 16 - 30) — ORİJİNAL SORULAR (16-29) + BENZER SORU (30)
    # =========================================================================
    {
        "no": 16,
        "day": 2,
        "is_original": True,
        "page": 20,
        "image": "cropped_figs/fig_q16.png",
        "img_height": 95,
        "text": (
            "Ekran parlaklığı 5 farklı kademede ayarlanabilen bir cep telefonunun parlaklık "
            "kademesinin her bir kademe artılışında enerji tüketimi bir önceki seviyenin 3/2 katına "
            "çıkmaktadır. Bu cep telefonunun şarjı tamamen dolu ve ekran parlaklığı 1. kademedeyken "
            "şarjı 36 saatte tamamen bitmektedir.<br/>"
            "<b>Buna göre cep telefonunun şarjı tamamen doluyken ekran parlaklığı 5. kademeye "
            "alınırsa şarjı tamamen kaç saatte biter?</b>"
        ),
        "options": [
            ("A", "32/9"),
            ("B", "16/3"),
            ("C", "64/9"),
            ("D", "8"),
            ("E", "32/3"),
        ],
        "answer": "C",
    },
    {
        "no": 17,
        "day": 2,
        "is_original": True,
        "page": 21,
        "text": (
            "Bir büyükşehir belediyesi, toplu taşımada vatandaşları teşvik etmek amacıyla "
            "\"Akıllı Aktarma Sistemi\" uygulamaktadır. Bu sistemde;<br/>"
            "• İlk biniş ücreti sabit 3<sup>4</sup> TL'dir.<br/>"
            "• İlk binişten sonraki ilk 45 dakika içinde yapılan 1. aktarmada biniş ücreti "
            "ilk binişin 2/3'sine düşer.<br/>"
            "• 1. aktarmadan sonraki ilk 45 dakika içinde yapılan 2. aktarmada ise biniş ücreti, "
            "1. aktarma ücretinin 2/3'sine düşer.<br/>"
            "<b>Bir halk otobüsündeki 32 yolcudan 8 tanesi 1. aktarma tarifesini, geriye kalan "
            "yolcular ise 2. aktarma tarifesini kullandığına göre bu yolculardan toplam kaç TL "
            "biniş ücreti alınmıştır?</b>"
        ),
        "options": [
            ("A", "6<sup>3</sup>"),
            ("B", "2 · 6<sup>3</sup>"),
            ("C", "3 · 6<sup>3</sup>"),
            ("D", "6<sup>4</sup>"),
            ("E", "2 · 6<sup>4</sup>"),
        ],
        "answer": "D",
    },
    {
        "no": 18,
        "day": 2,
        "is_original": True,
        "page": 21,
        "image": "cropped_figs/fig_q18.png",
        "img_height": 115,
        "text": (
            "Nurcan telefonundaki yemek uygulaması üzerinden sipariş vermiştir. Yukarıda "
            "siparişin ekran görüntüsü verilmiştir.<br/>"
            "<b>Buna göre Nurcan bu siparişte kaç TL indirim uygulamıştır?</b>"
        ),
        "options": [
            ("A", "16"),
            ("B", "32"),
            ("C", "48"),
            ("D", "64"),
            ("E", "128"),
        ],
        "answer": "D",
    },
    {
        "no": 19,
        "day": 2,
        "is_original": True,
        "page": 21,
        "text": (
            "Bir inşaat firması kentsel dönüşüm projesi kapsamında bir sitenin binalarını yenileyecektir:<br/>"
            "• Sitenin toplam arsa alanı 3 · 15<sup>3</sup> m<sup>2</sup>'dir.<br/>"
            "• Site arsasının tümü daire sahiplerine eşit paylaştırılacaktır.<br/>"
            "• Sitede 9 blok ve her blokta 5 daire yer almaktadır.<br/>"
            "<b>Buna göre bu sitede bir tane dairesi bulunan bir kişinin arsa payı kaç m<sup>2</sup>'dir?</b>"
        ),
        "options": [
            ("A", "75"),
            ("B", "125"),
            ("C", "150"),
            ("D", "225"),
            ("E", "375"),
        ],
        "answer": "D",
    },
    {
        "no": 20,
        "day": 2,
        "is_original": True,
        "page": 22,
        "group_notice": "20, 21 ve 22. soruları aşağıdaki bilgilere göre birbirinden bağımsız olarak cevaplayınız.",
        "image": "cropped_figs/fig_q20.png",
        "img_height": 85,
        "text": (
            "Kazım Bey, sahip olduğu farklı tarım arazilerini sulamak için kullandığı fıskiye "
            "sistemlerinin bir saatte harcadığı su miktarlarını yukarıdaki tabloda kayıt altına almıştır.<br/>"
            "<b>Kazım Bey 4 saat zeytin bahçesini, 1 saat lavanta bahçesini ve 8 saat domates bahçesini "
            "sularsa toplam kaç ton su kullanır?</b>"
        ),
        "options": [
            ("A", "2<sup>10</sup>"),
            ("B", "2<sup>11</sup>"),
            ("C", "3 · 2<sup>10</sup>"),
            ("D", "2<sup>12</sup>"),
            ("E", "2<sup>13</sup>"),
        ],
        "answer": "D",
    },
    {
        "no": 21,
        "day": 2,
        "is_original": True,
        "page": 22,
        "text": (
            "<b>[20. sorudaki tabloya göre] Kazım Bey meyve fidanlığını haftada 4 gün her gün 8 saat, "
            "botanik bahçesini ise x gün ve günde 2 saat sularsa bir haftada 21 · 2<sup>7</sup> ton su "
            "harcamış oluyor. Buna göre x kaçtır?</b>"
        ),
        "options": [
            ("A", "3"),
            ("B", "4"),
            ("C", "5"),
            ("D", "6"),
            ("E", "7"),
        ],
        "answer": "C",
    },
    {
        "no": 22,
        "day": 2,
        "is_original": True,
        "page": 22,
        "options_vertical": True,
        "text": (
            "<b>[20. sorudaki tabloya göre] Kazım Bey'in yaptığı aşağıdaki planlamalardan hangisinde, "
            "iki bahçenin haftalık toplam su tüketimi birbirine eşit olur?</b>"
        ),
        "options": [
            ("A", "Zeytin bahçesini 2 saat, Lavanta bahçesini 1 saat sulamak"),
            ("B", "Meyve fidanlığını 4 saat, Domates bahçesini 2 saat sulamak"),
            ("C", "Domates bahçesini 4 saat, Lavanta bahçesini 1 saat sulamak"),
            ("D", "Botanik bahçesini 8 saat, Zeytin bahçesini 4 saat sulamak"),
            ("E", "Lavanta bahçesini 2 saat, Meyve fidanlığını 16 saat sulamak"),
        ],
        "answer": "C",
    },
    {
        "no": 23,
        "day": 2,
        "is_original": True,
        "page": 22,
        "group_notice": "23, 24 ve 25. soruları aşağıdaki bilgilere göre cevaplayınız.",
        "text": (
            "Bir insansız hava aracının (İHA) görüntüleme sistemi, her km<sup>2</sup> alandan aldığı "
            "veriyi 2<sup>6</sup> adet küçük görüntü hücresine (piksel) bölerek merkeze iletmektedir.<br/>"
            "<b>16<sup>2</sup> km<sup>2</sup>'lik bir alanı bu İHA kaç piksele bölerek merkeze gönderir?</b>"
        ),
        "options": [
            ("A", "2<sup>12</sup>"),
            ("B", "2<sup>13</sup>"),
            ("C", "2<sup>14</sup>"),
            ("D", "2<sup>15</sup>"),
            ("E", "2<sup>16</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 24,
        "day": 2,
        "is_original": True,
        "page": 22,
        "text": (
            "<b>[23. sorudaki bilgiye göre] Merkeze toplam 8<sup>12</sup> piksel gönderildiğinde "
            "İHA taraması gereken tüm bölgeyi taramış oluyor. Buna göre İHA'nın taraması gereken "
            "bölge kaç km<sup>2</sup>'dir?</b>"
        ),
        "options": [
            ("A", "2<sup>24</sup>"),
            ("B", "2<sup>28</sup>"),
            ("C", "2<sup>30</sup>"),
            ("D", "2<sup>32</sup>"),
            ("E", "2<sup>36</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 25,
        "day": 2,
        "is_original": True,
        "page": 22,
        "text": (
            "<b>[23 ve 24. sorudaki bilgilere göre] Bu İHA görüntü netliğini artırmak için "
            "birimkaredeki piksel sayısını 2<sup>4</sup> katına, taranması gereken bölgeyi "
            "8<sup>2</sup> katına çıkartırsa İHA'nın merkeze göndermesi gereken toplam piksel "
            "sayısı kaç olur?</b>"
        ),
        "options": [
            ("A", "2<sup>40</sup>"),
            ("B", "2<sup>42</sup>"),
            ("C", "2<sup>44</sup>"),
            ("D", "2<sup>46</sup>"),
            ("E", "2<sup>48</sup>"),
        ],
        "answer": "D",
    },
    {
        "no": 26,
        "day": 2,
        "is_original": True,
        "page": 23,
        "group_notice": "26 ve 27. soruları aşağıdaki bilgilere göre birbirinden bağımsız olarak cevaplayınız.",
        "image": "cropped_figs/fig_q26.png",
        "img_height": 75,
        "text": (
            "Bir belediyenin akıllı yağmur suyu toplama ve drenaj sistemi, yağışın şiddetine göre "
            "farklı kapasitelerde çalışmaktadır. Yukarıdaki tabloda yağış kategorilerine göre "
            "1 metrekareye düşen ortalama yağış miktarı ve bu suyu tahliye etmek için çalışan "
            "pompa sisteminin saatlik enerji tüketimi verilmiştir.<br/>"
            "<b>Belediyenin sorumluluk alanındaki 8<sup>4</sup> m<sup>2</sup>'lik bir bölgeye "
            "\"Yüksek Şiddet\" kategorisinde yağış düşmüştür. Bu bölgenin tamamına düşen toplam "
            "yağış miktarı kaç kg olur?</b>"
        ),
        "options": [
            ("A", "2<sup>15</sup>"),
            ("B", "2<sup>17</sup>"),
            ("C", "2<sup>18</sup>"),
            ("D", "2<sup>19</sup>"),
            ("E", "2<sup>21</sup>"),
        ],
        "answer": "D",
    },
    {
        "no": 27,
        "day": 2,
        "is_original": True,
        "page": 23,
        "text": (
            "<b>[26. sorudaki tabloya göre] Tablodaki verilere göre, metrekareye düşen yağış "
            "miktarı 2<sup>2</sup> katına çıktığında sistemin enerji tüketimi yüzde kaç artmaktadır?</b>"
        ),
        "options": [
            ("A", "100"),
            ("B", "200"),
            ("C", "300"),
            ("D", "400"),
            ("E", "500"),
        ],
        "answer": "C",
    },
    {
        "no": 28,
        "day": 2,
        "is_original": True,
        "page": 23,
        "group_notice": "28 ve 29. soruları aşağıdaki bilgilere göre birbirinden bağımsız olarak cevaplayınız.",
        "text": (
            "Modern bir ofis binasında enerji tasarrufu sağlamak amacıyla \"Akıllı Katmanlı Cam\" "
            "sistemi kullanılmaktadır. Bu sistem, dışarıdan gelen güneş ışığının şiddetini (lüks "
            "birimiyle) her bir katmandan geçerken belirli bir oranda azaltmaktadır.<br/>"
            "Dış ortamdaki ışık şiddeti 27<sup>3</sup> lüks olarak belirlenmiştir. Bu ışık, camın "
            "her bir katmanından geçerken şiddeti bir önceki katmana göre 3<sup>-1</sup> katına düşmektedir.<br/>"
            "<b>Işık 4 katmanlı bir cam sisteminden geçip binanın içine ulaştığında, iç ortamdaki "
            "ışık şiddeti kaç lüks olur?</b>"
        ),
        "options": [
            ("A", "3<sup>3</sup>"),
            ("B", "3<sup>4</sup>"),
            ("C", "3<sup>5</sup>"),
            ("D", "3<sup>6</sup>"),
            ("E", "3<sup>7</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 29,
        "day": 2,
        "is_original": True,
        "page": 23,
        "options_vertical": True,
        "text": (
            "Pencereye ulaşan mevcut ışık şiddeti 3<sup>5</sup> lüks değerindedir. Mert'in konforlu "
            "çalışabilmesi için ışık şiddetini 3<sup>3</sup> lüks değerine indirmesi gerekmektedir.<br/>"
            "Mert'in elinde iki farklı ek filtre seçeneği vardır:<br/>"
            "• <b>Nano-Filtre A:</b> Işık şiddetini doğrudan 9<sup>-1</sup> katına düşürür.<br/>"
            "• <b>Katmanlı-Filtre B:</b> Her bir katmanın ışık şiddetini 3<sup>-1</sup> katına "
            "düşüren 3 ardışık katmandan oluşur.<br/>"
            "<b>Mert, hedeflediği 3<sup>3</sup> lüks değerine ulaşmak için hangi filtreyi tercih etmelidir?</b>"
        ),
        "options": [
            ("A", "Nano-Filtre A tercih edilmelidir. Çünkü bu filtre ışığı tam olarak 3<sup>3</sup> lüks seviyesine indirir."),
            ("B", "Katmanlı-Filtre B tercih edilmelidir. Çünkü 3 katmanlı yapı daha güvenli bir süzme sağlar ve 3<sup>3</sup> değerini verir."),
            ("C", "Her iki filtre de aynı sonucu (3<sup>3</sup> lüks) vereceği için herhangi biri tercih edilebilir."),
            ("D", "Nano-Filtre A ışığı 3<sup>2</sup> lükse düşürdüğü için yetersiz kalır, bu yüzden B seçilmelidir."),
            ("E", "Her iki filtre de ışığı 3<sup>3</sup> lüksün altına düşürdüğü için hiçbiri uygun değildir."),
        ],
        "answer": "A",
    },
    {
        "no": 30,
        "day": 2,
        "is_original": False,
        "sim_to": 1,
        "text": (
            "Kenar uzunluklarının oranı sabit kalacak şekilde tasarlanan dikdörtgen bir tablonun "
            "iki farklı modeli üretilmiştir. Küçük modelin kısa kenarı 6<sup>4</sup> birim, uzun "
            "kenarı 15<sup>4</sup> birimdir. Büyük modelin kısa kenarı 10<sup>4</sup> birim ve "
            "uzun kenarı x birimdir.<br/>"
            "<b>Buna göre büyük modeldeki x uzunluğu kaç birimdir?</b>"
        ),
        "options": [
            ("A", "5<sup>6</sup>"),
            ("B", "5<sup>8</sup>"),
            ("C", "15<sup>4</sup>"),
            ("D", "20<sup>4</sup>"),
            ("E", "25<sup>3</sup>"),
        ],
        "answer": "B",
    },

    # =========================================================================
    # 3. GÜN (SORULAR 31 - 45) — BENZER SORULAR
    # =========================================================================
    {
        "no": 31,
        "day": 3,
        "is_original": False,
        "sim_to": 1,
        "text": (
            "Kenar uzunluklarının oranı sabit kalacak şekilde tasarlanan dikdörtgen bir güneş panelinin "
            "küçük modelinde kısa kenar 4<sup>5</sup> cm, uzun kenar 6<sup>5</sup> cm'dir. Aynı orana "
            "sahip büyük modelinde ise kısa kenar 6<sup>5</sup> cm ve uzun kenar x cm'dir.<br/>"
            "<b>Buna göre x değeri aşağıdakilerden hangisine eşittir?</b>"
        ),
        "options": [
            ("A", "3<sup>8</sup>"),
            ("B", "3<sup>9</sup>"),
            ("C", "3<sup>10</sup>"),
            ("D", "6<sup>6</sup>"),
            ("E", "12<sup>5</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 32,
        "day": 3,
        "is_original": False,
        "sim_to": 1,
        "text": (
            "Kenar uzunluklarının oranı sabit kalacak şekilde dokunan dikdörtgen bir halının "
            "büyük modelinde kısa kenar 15<sup>3</sup> cm, uzun kenar 25<sup>3</sup> cm'dir. "
            "Küçük modelinde ise kısa kenar 9<sup>3</sup> cm ve uzun kenar x cm'dir.<br/>"
            "<b>Buna göre küçük modelin uzun kenarı (x) kaç cm'dir?</b>"
        ),
        "options": [
            ("A", "12<sup>3</sup>"),
            ("B", "15<sup>3</sup>"),
            ("C", "18<sup>3</sup>"),
            ("D", "5<sup>6</sup>"),
            ("E", "3<sup>6</sup>"),
        ],
        "answer": "B",
    },
    {
        "no": 33,
        "day": 3,
        "is_original": False,
        "sim_to": 2,
        "text": (
            "İki farklı özellikteki iş istasyonu bilgisayardan 1. bilgisayarın işlemci çekirdek "
            "sayısı 32, 2. bilgisayarın işlemci çekirdek sayısı ise 4'tür. Bilgisayarın bir işlemi "
            "yapma süresi çekirdek sayısı ile ters orantılıdır. 1. bilgisayar bir işlemi 4<sup>-3</sup> "
            "saniyede yapmaktadır.<br/>"
            "<b>Buna göre 2. bilgisayar aynı işlemi kaç saniyede yapar?</b>"
        ),
        "options": [
            ("A", "2<sup>-4</sup>"),
            ("B", "2<sup>-3</sup>"),
            ("C", "2<sup>-2</sup>"),
            ("D", "2<sup>-1</sup>"),
            ("E", "2<sup>0</sup>"),
        ],
        "answer": "B",
    },
    {
        "no": 34,
        "day": 3,
        "is_original": False,
        "sim_to": 2,
        "text": (
            "Grafik tasarımda kullanılan iki bilgisayardan A bilgisayarının çekirdek sayısı 27, "
            "B bilgisayarının çekirdek sayısı 3'tür. Bir video işleme süresi bilgisayarın çekirdek "
            "sayısı ile ters orantılıdır. A bilgisayarı bir videoyu 9<sup>-2</sup> dakikada işlemektedir.<br/>"
            "<b>Buna göre B bilgisayarı aynı videoyu kaç dakikada işler?</b>"
        ),
        "options": [
            ("A", "3<sup>-4</sup>"),
            ("B", "3<sup>-3</sup>"),
            ("C", "3<sup>-2</sup>"),
            ("D", "3<sup>-1</sup>"),
            ("E", "3"),
        ],
        "answer": "C",
    },
    {
        "no": 35,
        "day": 3,
        "is_original": False,
        "sim_to": 3,
        "text": (
            "Elif'in kumbarasında 10<sup>11</sup> adet 25 kuruşluk madeni para, Burak'ın cüzdanında "
            "ise 5 · 10<sup>n</sup> adet 50 TL'lik banknot bulunmaktadır.<br/>"
            "<b>Elif ve Burak'ın paralarının TL türünden toplam değerleri birbirine eşit olduğuna "
            "göre n kaçtır?</b>"
        ),
        "options": [
            ("A", "7"),
            ("B", "8"),
            ("C", "9"),
            ("D", "10"),
            ("E", "11"),
        ],
        "answer": "B",
    },
    {
        "no": 36,
        "day": 3,
        "is_original": False,
        "sim_to": 3,
        "text": (
            "Kerem'in elinde 4 · 10<sup>14</sup> adet 5 kuruşluk madeni para, Aslı'nın elinde ise "
            "10<sup>n</sup> adet 200 TL'lik banknot bulunmaktadır.<br/>"
            "<b>Kerem ve Aslı'nın ellerindeki paraların TL türünden tutarları birbirine eşit "
            "olduğuna göre n kaçtır?</b>"
        ),
        "options": [
            ("A", "9"),
            ("B", "10"),
            ("C", "11"),
            ("D", "12"),
            ("E", "13"),
        ],
        "answer": "C",
    },
    {
        "no": 37,
        "day": 3,
        "is_original": False,
        "sim_to": 4,
        "text": (
            "9 ilçesi bulunan bir ilin her ilçesinde 16 mahalle, her mahallede ise 12 okul "
            "bulunmaktadır. Bu ildeki tüm okulların her birine eşit sayıda fidan dağıtılmıştır.<br/>"
            "<b>Dağıtılan toplam fidan sayısı 12<sup>5</sup> olduğuna göre bir okula dağıtılan "
            "fidan sayısı kaçtır?</b>"
        ),
        "options": [
            ("A", "72"),
            ("B", "108"),
            ("C", "144"),
            ("D", "196"),
            ("E", "288"),
        ],
        "answer": "C",
    },
    {
        "no": 38,
        "day": 3,
        "is_original": False,
        "sim_to": 4,
        "text": (
            "25 şubesi bulunan bir kargo şirketinin her şubesinde 15 araç, her araçta ise 9 koli "
            "bulunmaktadır. Tüm kolilerin her birine eşit sayıda paket yerleştirilmiştir.<br/>"
            "<b>Yerleştirilen toplam paket sayısı 15<sup>5</sup> olduğuna göre bir kolide kaç "
            "paket vardır?</b>"
        ),
        "options": [
            ("A", "75"),
            ("B", "125"),
            ("C", "150"),
            ("D", "225"),
            ("E", "375"),
        ],
        "answer": "D",
    },
    {
        "no": 39,
        "day": 3,
        "is_original": False,
        "sim_to": 5,
        "text": (
            "Kaan'ın yatırım hesabında bulunan iki farklı kripto paradan X coin'in miktarı "
            "0,25 birim ve toplam değeri 10<sup>4</sup> TL; Y coin'in miktarı ise 1,5 birim ve "
            "toplam değeri 30 TL'dir.<br/>"
            "<b>Buna göre X coin'in TL türünden birim değerinin Y coin'in TL türünden birim "
            "değerine oranı kaçtır?</b>"
        ),
        "options": [
            ("A", "1000"),
            ("B", "1500"),
            ("C", "2000"),
            ("D", "2500"),
            ("E", "4000"),
        ],
        "answer": "C",
    },
    {
        "no": 40,
        "day": 3,
        "is_original": False,
        "sim_to": 5,
        "text": (
            "Bir yatırımcının portföyünde bulunan A fonunun miktarı 0,04 pay ve toplam değeri "
            "10<sup>3</sup> TL; B fonunun miktarı ise 1,25 pay ve toplam değeri 25 TL'dir.<br/>"
            "<b>Buna göre A fonunun TL türünden birim pay değerinin, B fonunun TL türünden "
            "birim pay değerine oranı kaçtır?</b>"
        ),
        "options": [
            ("A", "625"),
            ("B", "1000"),
            ("C", "1250"),
            ("D", "1500"),
            ("E", "2500"),
        ],
        "answer": "C",
    },
    {
        "no": 41,
        "day": 3,
        "is_original": False,
        "sim_to": 6,
        "text": (
            "X ortamında bulunan bakteriler her bir saatin sonunda 4 katına çıkarken, Y ortamında "
            "bulunan bakteriler her bir saatin sonunda 16 katına çıkmaktadır. Başlangıçta X ortamında "
            "16<sup>3</sup> tane bakteri bulunurken Y ortamında 8<sup>4</sup> tane bakteri bulunmaktadır.<br/>"
            "<b>3 saatlik sürenin sonunda Y ortamında bulunan bakteri sayısı, t saatlik sürenin "
            "sonunda X ortamında bulunan bakteri sayısına eşit olduğuna göre t kaçtır?</b>"
        ),
        "options": [
            ("A", "4"),
            ("B", "5"),
            ("C", "6"),
            ("D", "7"),
            ("E", "8"),
        ],
        "answer": "C",
    },
    {
        "no": 42,
        "day": 3,
        "is_original": False,
        "sim_to": 6,
        "text": (
            "K kültüründeki bakteriler her bir saatin sonunda 9 katına çıkarken, L kültüründeki "
            "bakteriler her bir saatin sonunda 27 katına çıkmaktadır. Başlangıçta K kültüründe "
            "27<sup>2</sup> tane bakteri, L kültüründe ise 9<sup>4</sup> tane bakteri vardır.<br/>"
            "<b>2 saatlik sürenin sonunda L kültüründeki bakteri sayısı, t saatlik sürenin "
            "sonunda K kültüründeki bakteri sayısına eşit olduğuna göre t kaçtır?</b>"
        ),
        "options": [
            ("A", "3"),
            ("B", "4"),
            ("C", "5"),
            ("D", "6"),
            ("E", "7"),
        ],
        "answer": "B",
    },
    {
        "no": 43,
        "day": 3,
        "is_original": False,
        "sim_to": 7,
        "text": (
            "Bir sınava giren 2400000 öğrencinin 17/25'i birinci aşamada elenmiş, elenmeyen "
            "öğrencilerin 9/25'i mülakata çağrılmış ve mülakata çağrılan öğrencilerin 1/5'i "
            "başarılı olarak burs almaya hak kazanmıştır.<br/>"
            "<b>Buna göre bu sınavda burs almaya hak kazanan öğrenci sayısı kaçtır?</b>"
        ),
        "options": [
            ("A", "2<sup>10</sup> · 3<sup>3</sup>"),
            ("B", "2<sup>11</sup> · 3<sup>3</sup>"),
            ("C", "2<sup>11</sup> · 3<sup>4</sup>"),
            ("D", "2<sup>12</sup> · 3<sup>3</sup>"),
            ("E", "2<sup>10</sup> · 3<sup>4</sup>"),
        ],
        "answer": "B",
    },
    {
        "no": 44,
        "day": 3,
        "is_original": False,
        "sim_to": 7,
        "text": (
            "Bir yarışmaya başvuran 5400000 kişinin 9/25'i ilk turu geçememiş, ilk turu geçenlerin "
            "3/25'i finale kalmış ve finale kalanların 1/5'i ödül kazanmıştır.<br/>"
            "<b>Buna göre bu yarışmada ödül kazanan yarışmacı sayısı kaçtır?</b>"
        ),
        "options": [
            ("A", "2<sup>9</sup> · 3<sup>4</sup>"),
            ("B", "2<sup>10</sup> · 3<sup>3</sup>"),
            ("C", "2<sup>10</sup> · 3<sup>4</sup>"),
            ("D", "2<sup>11</sup> · 3<sup>4</sup>"),
            ("E", "2<sup>10</sup> · 3<sup>5</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 45,
        "day": 3,
        "is_original": False,
        "sim_to": 8,
        "text": (
            "Dijital veri birimleri arasında 1 GB = 2<sup>30</sup> bayt ve 1 TB = 2<sup>40</sup> bayt "
            "ilişkisi bulunmaktadır.<br/>"
            "Berk, bilgisayarında bulunan 4<sup>6</sup> GB büyüklüğündeki bir arşiv dosyasının "
            "boyutunu sıkıştırma programıyla başlangıçtaki boyutunun %12,5'ine düşürüyor.<br/>"
            "<b>Berk bu sıkıştırılmış dosyayı tamamı boş olan 4 TB'lık taşınabilir diske "
            "yüklediğinde diskin kaçta kaçı dolu olur?</b>"
        ),
        "options": [
            ("A", "1/16"),
            ("B", "1/8"),
            ("C", "1/4"),
            ("D", "1/2"),
            ("E", "3/4"),
        ],
        "answer": "B",
    },

    # =========================================================================
    # 4. GÜN (SORULAR 46 - 60) — BENZER SORULAR
    # =========================================================================
    {
        "no": 46,
        "day": 4,
        "is_original": False,
        "sim_to": 8,
        "text": (
            "Dijital veri birimleri arasında 1 MB = 2<sup>20</sup> bayt ve 1 GB = 2<sup>30</sup> bayt "
            "ilişkisi bulunmaktadır.<br/>"
            "Selin, kamerasıyla çektiği 16<sup>3</sup> MB büyüklüğündeki ham videonun boyutunu "
            "düzenleme programıyla başlangıçtaki boyutunun %50'sine düşürüyor.<br/>"
            "<b>Selin bu videoyu tamamı boş olan 8 GB'lık bir belleğe yüklediğinde belleğin "
            "kaçta kaçı dolu olur?</b>"
        ),
        "options": [
            ("A", "1/8"),
            ("B", "1/4"),
            ("C", "3/8"),
            ("D", "1/2"),
            ("E", "3/4"),
        ],
        "answer": "B",
    },
    {
        "no": 47,
        "day": 4,
        "is_original": False,
        "sim_to": 9,
        "text": (
            "Bir jeoloji dergisinde yer alan verilere göre:<br/>"
            "• Bir bölgedeki toplam buz kütlesi yaklaşık 2,5 · 10<sup>10</sup> megatondur. "
            "[1 megaton = 10<sup>6</sup> ton, 1 ton = 1000 kg]<br/>"
            "• Bu buz kütlesinin yalnızca %4'ü yüksek dağ buzullarında bulunmakta olup, bu dağ "
            "buzullarının da sadece %2'si her yıl eriyerek akarsulara karışmaktadır.<br/>"
            "<b>Buna göre her yıl eriyerek akarsulara karışan dağ buzulu kütlesi kaç kilogramdır?</b>"
        ),
        "options": [
            ("A", "2 · 10<sup>14</sup>"),
            ("B", "2 · 10<sup>15</sup>"),
            ("C", "2 · 10<sup>16</sup>"),
            ("D", "5 · 10<sup>15</sup>"),
            ("E", "5 · 10<sup>16</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 48,
        "day": 4,
        "is_original": False,
        "sim_to": 9,
        "text": (
            "Bir tarım raporunda yer alan verilere göre:<br/>"
            "• Bir ülkedeki yıllık toplam tarımsal üretim 3,2 · 10<sup>4</sup> megatondur. "
            "[1 megaton = 10<sup>6</sup> ton, 1 ton = 1000 kg]<br/>"
            "• Toplam üretimin yalnızca %5'i organik tarım ürünü olup, bu organik ürünlerin de "
            "sadece %25'i yurt dışına ihraç edilmektedir.<br/>"
            "<b>Buna göre yurt dışına ihraç edilen organik tarım ürünü miktarı kaç kilogramdır?</b>"
        ),
        "options": [
            ("A", "4 · 10<sup>10</sup>"),
            ("B", "4 · 10<sup>11</sup>"),
            ("C", "4 · 10<sup>12</sup>"),
            ("D", "8 · 10<sup>10</sup>"),
            ("E", "8 · 10<sup>11</sup>"),
        ],
        "answer": "B",
    },
    {
        "no": 49,
        "day": 4,
        "is_original": False,
        "sim_to": 10,
        "text": (
            "Bir ekonomistin gelecek yıllardaki ekonomik durumlarla ilgili öngörüsü aşağıdaki gibidir:<br/>"
            "• Her 2 yıllık sürenin sonunda çalışanların maaşları 2 katına çıkacaktır.<br/>"
            "• Her 3 yıllık sürenin sonunda altının gram fiyatı 8 katına çıkacaktır.<br/>"
            "<b>Bir çalışan 2020 yılında bir aylık maaşıyla 2<sup>8</sup> gram altın alabildiğine "
            "göre 2032 yılında aynı çalışan bir aylık maaşıyla kaç gram altın alabilir?</b>"
        ),
        "options": [
            ("A", "1"),
            ("B", "2"),
            ("C", "4"),
            ("D", "8"),
            ("E", "16"),
        ],
        "answer": "C",
    },
    {
        "no": 50,
        "day": 4,
        "is_original": False,
        "sim_to": 10,
        "text": (
            "Bir finans uzmanının tahminine göre:<br/>"
            "• Her 3 yıllık sürenin sonunda çalışanların maaşları 3 katına çıkacaktır.<br/>"
            "• Her 2 yıllık sürenin sonunda nadir bir metalin gram fiyatı 9 katına çıkacaktır.<br/>"
            "<b>2018 yılında bir aylık maaşıyla 3<sup>10</sup> gram bu metalden alabilen bir çalışan, "
            "2030 yılında bir aylık maaşıyla kaç gram alabilir?</b>"
        ),
        "options": [
            ("A", "3<sup>-2</sup>"),
            ("B", "3<sup>-1</sup>"),
            ("C", "1"),
            ("D", "3"),
            ("E", "9"),
        ],
        "answer": "E",
    },
    {
        "no": 51,
        "day": 4,
        "is_original": False,
        "sim_to": 11,
        "text": (
            "Ses düzeyi her 10 desibel (dB) arttığında ses şiddeti 10 katına çıkmaktadır.<br/>"
            "<b>Bir kütüphanedeki ses düzeyi 40 dB, bir konser alanındaki ses düzeyi ise 110 dB "
            "olarak ölçüldüğüne göre, konser alanındaki sesin şiddeti kütüphanedeki sesin "
            "şiddetinin kaç katıdır?</b>"
        ),
        "options": [
            ("A", "10<sup>5</sup>"),
            ("B", "10<sup>6</sup>"),
            ("C", "10<sup>7</sup>"),
            ("D", "10<sup>8</sup>"),
            ("E", "10<sup>9</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 52,
        "day": 4,
        "is_original": False,
        "sim_to": 11,
        "text": (
            "Ses düzeyi her 10 desibel (dB) arttığında ses şiddeti 10 katına çıkmaktadır.<br/>"
            "<b>Ses düzeyi 30 dB olan bir fısıltının 10<sup>6</sup> katı ses şiddetine sahip bir "
            "ortamın ses düzeyi kaç desibeldir?</b>"
        ),
        "options": [
            ("A", "70"),
            ("B", "80"),
            ("C", "90"),
            ("D", "100"),
            ("E", "110"),
        ],
        "answer": "C",
    },
    {
        "no": 53,
        "day": 4,
        "is_original": False,
        "sim_to": 12,
        "text": (
            "• Geleneksel soğutma sisteminde her bir saatte 8<sup>3</sup> litre su tüketilmektedir.<br/>"
            "• Akıllı sensörlü soğutma sisteminde ise her bir saatte 4<sup>4</sup> litre su tüketilmektedir.<br/>"
            "<b>81 saatlik sürede geleneksel sistem yerine akıllı sistemin kullanılması 12<sup>n</sup> "
            "litre su tasarrufu sağladığına göre n kaçtır?</b>"
        ),
        "options": [
            ("A", "2"),
            ("B", "3"),
            ("C", "4"),
            ("D", "5"),
            ("E", "6"),
        ],
        "answer": "C",
    },
    {
        "no": 54,
        "day": 4,
        "is_original": False,
        "sim_to": 12,
        "text": (
            "• Geleneksel ısıtma sisteminde bir sera her bir saatte 9<sup>3</sup> kWh enerji harcamaktadır.<br/>"
            "• Akıllı termostatlı ısıtma sisteminde ise her bir saatte 2 · 3<sup>5</sup> kWh enerji harcanmaktadır.<br/>"
            "<b>32 saatlik sürede geleneksel sistem yerine akıllı sistemin kullanılması 6<sup>n</sup> "
            "kWh enerji tasarrufu sağladığına göre n kaçtır?</b>"
        ),
        "options": [
            ("A", "3"),
            ("B", "4"),
            ("C", "5"),
            ("D", "6"),
            ("E", "7"),
        ],
        "answer": "C",
    },
    {
        "no": 55,
        "day": 4,
        "is_original": False,
        "sim_to": 13,
        "text": (
            "Bir belediyenin başlattığı \"Askıda Fidan\" kampanyasında:<br/>"
            "• Kampanyanın 1. ayında bağışlanan toplam fidan sayısı 16<sup>3</sup>'tür.<br/>"
            "• Her ay bağışlanan fidan sayısı bir önceki ayda bağışlanan fidan sayısının 1,25 katı olmaktadır.<br/>"
            "<b>Buna göre kampanyanın 5. ayında bağışlanan fidan sayısı kaçtır?</b>"
        ),
        "options": [
            ("A", "5000"),
            ("B", "6400"),
            ("C", "8000"),
            ("D", "10000"),
            ("E", "12500"),
        ],
        "answer": "D",
    },
    {
        "no": 56,
        "day": 4,
        "is_original": False,
        "sim_to": 13,
        "text": (
            "Bir okulun yürüttüğü geri dönüşüm projesinde:<br/>"
            "• Projenin 1. haftasında toplanan atık pil sayısı 81<sup>2</sup> adettir.<br/>"
            "• Her hafta toplanan pil sayısı bir önceki haftada toplanan pil sayısının 4/3 katı olmaktadır.<br/>"
            "<b>Buna göre projenin 4. haftasında toplanan atık pil sayısı kaçtır?</b>"
        ),
        "options": [
            ("A", "2<sup>5</sup> · 3<sup>5</sup>"),
            ("B", "2<sup>6</sup> · 3<sup>4</sup>"),
            ("C", "2<sup>6</sup> · 3<sup>5</sup>"),
            ("D", "2<sup>8</sup> · 3<sup>4</sup>"),
            ("E", "2<sup>6</sup> · 3<sup>6</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 57,
        "day": 4,
        "is_original": False,
        "sim_to": 14,
        "text": (
            "Geleneksel bahçe hortumuyla yapılan her sulamada ortalama 2<sup>6</sup> litre su "
            "harcanmaktadır. Akıllı damla sulama sistemi ise su tüketiminde %75 tasarruf sağlamaktadır. "
            "Ali Bey, suyun 1 tonunun (1000 litre) 125 TL olduğu bir ilde bir ay içerisinde "
            "bahçesini 50 defa sulamaktadır.<br/>"
            "<b>Ali Bey bir ay içerisinde bahçesini hortum yerine damla sulama sistemi ile sularsa "
            "kaç TL daha az su faturası öder?</b>"
        ),
        "options": [
            ("A", "200"),
            ("B", "240"),
            ("C", "250"),
            ("D", "300"),
            ("E", "360"),
        ],
        "answer": "D",
    },
    {
        "no": 58,
        "day": 4,
        "is_original": False,
        "sim_to": 14,
        "text": (
            "Eski tip bir çamaşır makinesi her yıkamada ortalama 5<sup>3</sup> litre su harcarken, "
            "yeni nesil akıllı çamaşır makinesi su tüketiminde %60 tasarruf sağlamaktadır. "
            "Zeynep Hanım, suyun 1 tonunun (1000 litre) 80 TL olduğu bir şehirde ayda 16 defa "
            "çamaşır yıkamaktadır.<br/>"
            "<b>Zeynep Hanım çamaşırları eski makine yerine yeni nesil akıllı makinede yıkarsa "
            "ayda kaç TL daha az su faturası öder?</b>"
        ),
        "options": [
            ("A", "64"),
            ("B", "80"),
            ("C", "96"),
            ("D", "112"),
            ("E", "128"),
        ],
        "answer": "C",
    },
    {
        "no": 59,
        "day": 4,
        "is_original": False,
        "sim_to": 15,
        "text": (
            "16 kişinin bulunduğu bir proje mesajlaşma grubunda paylaşılan belgelerle ilgili "
            "aşağıdaki bilgiler bilinmektedir:<br/>"
            "• Gruptaki her kişi günde ortalama 4 MB büyüklüğünde belge paylaşmaktadır.<br/>"
            "• Grupta bir gün içinde paylaşılan tüm belgeler, gönderen kişi de dâhil olmak üzere "
            "her üyenin tabletine otomatik olarak kaydedilmektedir.<br/>"
            "<b>64 gün boyunca bu gruptan gelen belgeler nedeniyle tabletinin hafızası dolan "
            "Mert, bu belgelerin %25'ini silerse tabletinde kaç MB yer açılır?</b>"
        ),
        "options": [
            ("A", "2<sup>8</sup>"),
            ("B", "2<sup>9</sup>"),
            ("C", "2<sup>10</sup>"),
            ("D", "2<sup>11</sup>"),
            ("E", "2<sup>12</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 60,
        "day": 4,
        "is_original": False,
        "sim_to": 15,
        "text": (
            "4 kişinin bulunduğu bir fotoğrafçılık grubunda:<br/>"
            "• Gruptaki her üye günde ortalama 16 MB fotoğraf paylaşmaktadır.<br/>"
            "• Paylaşılan tüm fotoğraflar gönderen kişi de dâhil olmak üzere her üyenin telefonuna "
            "otomatik olarak kaydedilmektedir.<br/>"
            "<b>16 gün boyunca bu gruptan gelen fotoğrafların %6,25'ini (1/16'sını) silen Ece'nin "
            "telefonunda kaç MB yer açılır?</b>"
        ),
        "options": [
            ("A", "2<sup>4</sup>"),
            ("B", "2<sup>5</sup>"),
            ("C", "2<sup>6</sup>"),
            ("D", "2<sup>7</sup>"),
            ("E", "2<sup>8</sup>"),
        ],
        "answer": "C",
    },

    # =========================================================================
    # 5. GÜN (SORULAR 61 - 75) — BENZER SORULAR
    # =========================================================================
    {
        "no": 61,
        "day": 5,
        "is_original": False,
        "sim_to": 16,
        "text": (
            "Ekran parlaklığı 4 farklı kademede ayarlanabilen bir tabletin parlaklık kademesinin "
            "her bir kademe artırılışında enerji tüketimi bir önceki seviyenin 4/3 katına çıkmaktadır. "
            "Bu tabletin şarjı tamamen dolu ve ekran parlaklığı 1. kademedeyken şarjı 32 saatte "
            "tamamen bitmektedir.<br/>"
            "<b>Buna göre tabletin şarjı tamamen doluyken ekran parlaklığı 4. kademeye alınırsa "
            "şarjı tamamen kaç saatte biter?</b>"
        ),
        "options": [
            ("A", "27/4"),
            ("B", "9"),
            ("C", "27/2"),
            ("D", "18"),
            ("E", "24"),
        ],
        "answer": "C",
    },
    {
        "no": 62,
        "day": 5,
        "is_original": False,
        "sim_to": 16,
        "text": (
            "Emir'in kullandığı kablosuz süpürgenin emiş gücü 5 farklı kademede ayarlanabilmekte "
            "olup her bir kademe artışında batarya tüketim hızı bir önceki kademenin 3/2 katına "
            "çıkmaktadır. Tam dolu batarya ile 1. kademede 81 dakika kesintisiz çalışan bu süpürge,<br/>"
            "<b>tam dolu batarya ile 5. kademede kaç dakika kesintisiz çalışır?</b>"
        ),
        "options": [
            ("A", "8"),
            ("B", "12"),
            ("C", "16"),
            ("D", "24"),
            ("E", "32"),
        ],
        "answer": "C",
    },
    {
        "no": 63,
        "day": 5,
        "is_original": False,
        "sim_to": 17,
        "text": (
            "Bir şehirdeki metro \"Akıllı Aktarma Sistemi\"nde:<br/>"
            "• İlk biniş ücreti sabit 5<sup>3</sup> TL'dir.<br/>"
            "• 1. aktarmada biniş ücreti ilk binişin 2/5'sine düşer.<br/>"
            "• 2. aktarmada ise biniş ücreti, 1. aktarma ücretinin 2/5'sine düşer.<br/>"
            "<b>Bir metro vagonundaki 29 yolcudan 14 tanesi 1. aktarma tarifesini, geriye kalan "
            "15 yolcu ise 2. aktarma tarifesini kullandığına göre bu yolculardan toplam kaç TL "
            "biniş ücreti alınmıştır?</b>"
        ),
        "options": [
            ("A", "5<sup>4</sup>"),
            ("B", "800"),
            ("C", "10<sup>3</sup>"),
            ("D", "1250"),
            ("E", "2 · 10<sup>3</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 64,
        "day": 5,
        "is_original": False,
        "sim_to": 17,
        "text": (
            "Bir deniz otobüsü hattında uygulanan aktarma sisteminde:<br/>"
            "• İlk biniş ücreti sabit 2<sup>6</sup> TL'dir.<br/>"
            "• 1. aktarmada biniş ücreti ilk binişin 3/4'üne düşer.<br/>"
            "• 2. aktarmada ise biniş ücreti, 1. aktarma ücretinin 3/4'üne düşer.<br/>"
            "<b>Deniz otobüsündeki 8 yolcudan 3 tanesi 1. aktarma tarifesini, geriye kalan 5 yolcu "
            "ise 2. aktarma tarifesini kullandığına göre toplam kaç TL biniş ücreti alınmıştır?</b>"
        ),
        "options": [
            ("A", "12<sup>2</sup>"),
            ("B", "15<sup>2</sup>"),
            ("C", "18<sup>2</sup>"),
            ("D", "20<sup>2</sup>"),
            ("E", "24<sup>2</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 65,
        "day": 5,
        "is_original": False,
        "sim_to": 18,
        "text": (
            "Bir online alışveriş uygulamasında sepet tutarı 64 · 3<sup>7</sup> TL olarak "
            "hesaplanmıştır. Uygulamada kullanılan \"Süper Fırsat Kuponu\" ile toplam tutarın "
            "1/12<sup>3</sup>'ü kadar anında indirim uygulanmıştır.<br/>"
            "<b>Buna göre bu siparişte kaç TL indirim uygulanmıştır?</b>"
        ),
        "options": [
            ("A", "27"),
            ("B", "54"),
            ("C", "81"),
            ("D", "108"),
            ("E", "243"),
        ],
        "answer": "C",
    },
    {
        "no": 66,
        "day": 5,
        "is_original": False,
        "sim_to": 18,
        "text": (
            "Bir teknoloji mağazasının mobil uygulamasında 125 · 2<sup>10</sup> TL tutarındaki "
            "bir siparişe, toplam tutarın 1/10<sup>3</sup>'ü kadar anında kupon indirimi "
            "uygulanmıştır.<br/>"
            "<b>Buna göre uygulanan indirim tutarı kaç TL'dir?</b>"
        ),
        "options": [
            ("A", "32"),
            ("B", "64"),
            ("C", "128"),
            ("D", "256"),
            ("E", "512"),
        ],
        "answer": "C",
    },
    {
        "no": 67,
        "day": 5,
        "is_original": False,
        "sim_to": 20,
        "group_notice": "67, 68 ve 69. soruları aşağıdaki bilgilere göre birbirinden bağımsız olarak cevaplayınız.",
        "table_data": [
            ["Sera Türü", "Bir Saatteki Su Tüketimi (ton/saat)"],
            ["Çilek serası", "3<sup>5</sup>"],
            ["Orkide serası", "27<sup>2</sup>"],
            ["Biber serası", "9<sup>2</sup>"],
            ["Fide serası", "3<sup>4</sup>"],
            ["Kaktüs serası", "3<sup>3</sup>"],
        ],
        "text": (
            "Salih Bey, sahip olduğu farklı seraları sulamak için kullandığı sistemlerin bir "
            "saatte harcadığı su miktarlarını yukarıdaki tabloda kayıt altına almıştır.<br/>"
            "<b>Salih Bey 3 saat çilek serasını, 1 saat orkide serasını ve 9 saat biber serasını "
            "sularsa toplam kaç ton su kullanır?</b>"
        ),
        "options": [
            ("A", "3<sup>6</sup>"),
            ("B", "2 · 3<sup>6</sup>"),
            ("C", "3<sup>7</sup>"),
            ("D", "3<sup>8</sup>"),
            ("E", "3<sup>9</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 68,
        "day": 5,
        "is_original": False,
        "sim_to": 21,
        "text": (
            "<b>[67. sorudaki tabloya göre] Salih Bey fide serasını haftada 3 gün ve her gün 6 saat, "
            "kaktüs serasını ise haftada x gün ve günde 9 saat sularsa bir haftada toplam "
            "11 · 3<sup>5</sup> ton su harcamış oluyor. Buna göre x kaçtır?</b>"
        ),
        "options": [
            ("A", "3"),
            ("B", "4"),
            ("C", "5"),
            ("D", "6"),
            ("E", "7"),
        ],
        "answer": "C",
    },
    {
        "no": 69,
        "day": 5,
        "is_original": False,
        "sim_to": 22,
        "options_vertical": True,
        "text": (
            "<b>[67. sorudaki tabloya göre] Salih Bey'in yaptığı aşağıdaki planlamalardan hangisinde, "
            "iki seranın toplam su tüketimi birbirine eşit olur?</b>"
        ),
        "options": [
            ("A", "Çilek serasını 2 saat, Orkide serasını 1 saat sulamak"),
            ("B", "Fide serasını 3 saat, Orkide serasını 1 saat sulamak"),
            ("C", "Biber serasını 9 saat, Orkide serasını 1 saat sulamak"),
            ("D", "Kaktüs serasını 3 saat, Çilek serasını 1 saat sulamak"),
            ("E", "Orkide serasını 3 saat, Biber serasını 9 saat sulamak"),
        ],
        "answer": "C",
    },
    {
        "no": 70,
        "day": 5,
        "is_original": False,
        "sim_to": 20,
        "group_notice": "70, 71 ve 72. soruları aşağıdaki bilgilere göre birbirinden bağımsız olarak cevaplayınız.",
        "table_data": [
            ["Makine Türü", "Bir Saatteki Enerji Tüketimi (kWh/saat)"],
            ["Kesim makinesi", "2<sup>9</sup>"],
            ["Pres makinesi", "16<sup>3</sup>"],
            ["Montaj makinesi", "8<sup>3</sup>"],
            ["Paketleme makinesi", "4<sup>4</sup>"],
            ["Etiketleme makinesi", "2<sup>7</sup>"],
        ],
        "text": (
            "Bir fabrikadaki 5 farklı makinenin bir saatte tükettiği elektrik enerjisi miktarları "
            "yukarıdaki tabloda verilmiştir.<br/>"
            "<b>Fabrikada kesim makinesi 4 saat, pres makinesi 1 saat ve montaj makinesi 4 saat "
            "çalıştırılırsa toplam kaç kWh elektrik enerjisi tüketilir?</b>"
        ),
        "options": [
            ("A", "2<sup>11</sup>"),
            ("B", "2<sup>12</sup>"),
            ("C", "3 · 2<sup>11</sup>"),
            ("D", "2<sup>13</sup>"),
            ("E", "2<sup>14</sup>"),
        ],
        "answer": "D",
    },
    {
        "no": 71,
        "day": 5,
        "is_original": False,
        "sim_to": 21,
        "text": (
            "<b>[70. sorudaki tabloya göre] Fabrikada paketleme makinesi haftada 5 gün ve günde "
            "4 saat, etiketleme makinesi ise haftada x gün ve günde 8 saat çalıştırıldığında "
            "bir haftada toplam 11 · 2<sup>10</sup> kWh enerji tüketilmektedir. Buna göre x kaçtır?</b>"
        ),
        "options": [
            ("A", "3"),
            ("B", "4"),
            ("C", "5"),
            ("D", "6"),
            ("E", "7"),
        ],
        "answer": "D",
    },
    {
        "no": 72,
        "day": 5,
        "is_original": False,
        "sim_to": 22,
        "options_vertical": True,
        "text": (
            "<b>[70. sorudaki tabloya göre] Fabrika yönetiminin yaptığı aşağıdaki çalışma "
            "planlamalarından hangisinde, iki makinenin toplam enerji tüketimi birbirine eşit olur?</b>"
        ),
        "options": [
            ("A", "Kesim makinesini 4 saat, Pres makinesini 1 saat çalıştırmak"),
            ("B", "Etiketleme makinesini 4 saat, Montaj makinesini 2 saat çalıştırmak"),
            ("C", "Pres makinesini 1 saat, Paketleme makinesini 16 saat çalıştırmak"),
            ("D", "Paketleme makinesini 4 saat, Pres makinesini 1 saat çalıştırmak"),
            ("E", "Montaj makinesini 2 saat, Etiketleme makinesini 4 saat çalıştırmak"),
        ],
        "answer": "C",
    },
    {
        "no": 73,
        "day": 5,
        "is_original": False,
        "sim_to": 23,
        "group_notice": "73, 74 ve 75. soruları aşağıdaki bilgilere göre cevaplayınız.",
        "text": (
            "Bir gözlem uydusunun kamera sistemi, yeryüzündeki her km<sup>2</sup> alandan aldığı "
            "görüntüyü 2<sup>8</sup> adet küçük görüntü hücresine (piksel) bölerek yer istasyonuna "
            "iletmektedir.<br/>"
            "<b>32<sup>2</sup> km<sup>2</sup>'lik bir alanı bu uydu kaç piksele bölerek yer "
            "istasyonuna gönderir?</b>"
        ),
        "options": [
            ("A", "2<sup>14</sup>"),
            ("B", "2<sup>16</sup>"),
            ("C", "2<sup>18</sup>"),
            ("D", "2<sup>20</sup>"),
            ("E", "2<sup>22</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 74,
        "day": 5,
        "is_original": False,
        "sim_to": 24,
        "text": (
            "<b>[73. sorudaki bilgiye göre] Yer istasyonuna toplam 16<sup>10</sup> piksel "
            "gönderildiğinde uydu taraması gereken tüm bölgeyi taramış oluyor. Buna göre uydunun "
            "taraması gereken bölge kaç km<sup>2</sup>'dir?</b>"
        ),
        "options": [
            ("A", "2<sup>28</sup>"),
            ("B", "2<sup>30</sup>"),
            ("C", "2<sup>32</sup>"),
            ("D", "2<sup>34</sup>"),
            ("E", "2<sup>36</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 75,
        "day": 5,
        "is_original": False,
        "sim_to": 25,
        "text": (
            "<b>[73 ve 74. sorudaki bilgilere göre] Bu uydu görüntü netliğini artırmak için "
            "birimkaredeki piksel sayısını 2<sup>5</sup> katına, taranması gereken bölgeyi ise "
            "4<sup>3</sup> katına çıkartırsa yer istasyonuna göndermesi gereken toplam piksel "
            "sayısı kaç olur?</b>"
        ),
        "options": [
            ("A", "2<sup>47</sup>"),
            ("B", "2<sup>49</sup>"),
            ("C", "2<sup>51</sup>"),
            ("D", "2<sup>53</sup>"),
            ("E", "2<sup>55</sup>"),
        ],
        "answer": "C",
    },

    # =========================================================================
    # 6. GÜN (SORULAR 76 - 90) — BENZER SORULAR
    # =========================================================================
    {
        "no": 76,
        "day": 6,
        "is_original": False,
        "sim_to": 23,
        "group_notice": "76, 77 ve 78. soruları aşağıdaki bilgilere göre cevaplayınız.",
        "text": (
            "Bir haritalama dronunun lazer tarama sistemi, her km<sup>2</sup> alandan aldığı veriyi "
            "3<sup>4</sup> adet veri noktasına bölerek ana bilgisayara aktarmaktadır.<br/>"
            "<b>9<sup>3</sup> km<sup>2</sup>'lik bir ormanlık alanı bu dron kaç veri noktasına "
            "bölerek ana bilgisayara aktarır?</b>"
        ),
        "options": [
            ("A", "3<sup>8</sup>"),
            ("B", "3<sup>9</sup>"),
            ("C", "3<sup>10</sup>"),
            ("D", "3<sup>11</sup>"),
            ("E", "3<sup>12</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 77,
        "day": 6,
        "is_original": False,
        "sim_to": 24,
        "text": (
            "<b>[76. sorudaki bilgiye göre] Ana bilgisayara toplam 27<sup>8</sup> veri noktası "
            "aktarıldığında dron taraması gereken tüm bölgeyi tamamlamış oluyor. Buna göre dronun "
            "taraması gereken bölge kaç km<sup>2</sup>'dir?</b>"
        ),
        "options": [
            ("A", "3<sup>16</sup>"),
            ("B", "3<sup>18</sup>"),
            ("C", "3<sup>20</sup>"),
            ("D", "3<sup>22</sup>"),
            ("E", "3<sup>24</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 78,
        "day": 6,
        "is_original": False,
        "sim_to": 25,
        "text": (
            "<b>[76 ve 77. sorudaki bilgilere göre] Bu dron tarama hassasiyetini artırmak için "
            "birimkaredeki veri noktası sayısını 3<sup>3</sup> katına, taranması gereken bölgeyi "
            "ise 9<sup>2</sup> katına çıkartırsa ana bilgisayara aktarması gereken toplam veri "
            "noktası sayısı kaç olur?</b>"
        ),
        "options": [
            ("A", "3<sup>29</sup>"),
            ("B", "3<sup>30</sup>"),
            ("C", "3<sup>31</sup>"),
            ("D", "3<sup>32</sup>"),
            ("E", "3<sup>33</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 79,
        "day": 6,
        "is_original": False,
        "sim_to": 26,
        "group_notice": "79 ve 80. soruları aşağıdaki bilgilere göre birbirinden bağımsız olarak cevaplayınız.",
        "table_data": [
            ["Yağış Kategorisi", "1 m²'ye Düşen Yağış (kg)", "Sistemin Enerji Tüketimi (Watt)"],
            ["Düşük Şiddet", "3<sup>2</sup>", "3<sup>4</sup>"],
            ["Orta Şiddet", "3<sup>4</sup>", "3<sup>6</sup>"],
            ["Yüksek Şiddet", "3<sup>6</sup>", "3<sup>8</sup>"],
        ],
        "text": (
            "Bir sanayi sitesinin yağmur suyu tahliye sistemi, yağış şiddetine göre farklı "
            "kapasitelerde çalışmaktadır. Yukarıdaki tabloda yağış kategorilerine göre 1 m<sup>2</sup>'ye "
            "düşen yağış miktarı ve pompa sisteminin saatlik enerji tüketimi verilmiştir.<br/>"
            "<b>Sanayi sitesinin 27<sup>3</sup> m<sup>2</sup>'lik alanına \"Orta Şiddet\" "
            "kategorisinde yağış düştüğüne göre, bu alanın tamamına düşen toplam yağış miktarı "
            "kaç kg olur?</b>"
        ),
        "options": [
            ("A", "3<sup>11</sup>"),
            ("B", "3<sup>12</sup>"),
            ("C", "3<sup>13</sup>"),
            ("D", "3<sup>14</sup>"),
            ("E", "3<sup>15</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 80,
        "day": 6,
        "is_original": False,
        "sim_to": 27,
        "text": (
            "<b>[79. sorudaki tabloya göre] Tablodaki verilere göre, metrekareye düşen yağış "
            "miktarı 3<sup>2</sup> katına çıktığında sistemin enerji tüketimi yüzde kaç artmaktadır?</b>"
        ),
        "options": [
            ("A", "300"),
            ("B", "600"),
            ("C", "800"),
            ("D", "900"),
            ("E", "1000"),
        ],
        "answer": "C",
    },
    {
        "no": 81,
        "day": 6,
        "is_original": False,
        "sim_to": 26,
        "group_notice": "81 ve 82. soruları aşağıdaki bilgilere göre birbirinden bağımsız olarak cevaplayınız.",
        "table_data": [
            ["Güneşlenme Kategorisi", "1 m² Panelin Ürettiği Enerji (Wh)", "Soğutma Tüketimi (Watt)"],
            ["Düşük", "2<sup>4</sup>", "2<sup>2</sup>"],
            ["Orta", "2<sup>5</sup>", "2<sup>3</sup>"],
            ["Yüksek", "2<sup>6</sup>", "2<sup>4</sup>"],
        ],
        "text": (
            "Bir güneş enerjisi santralinde güneşlenme kategorisine göre 1 m<sup>2</sup> panelin "
            "saatlik enerji üretimi ve panel soğutma sisteminin enerji tüketimi yukarıdaki tabloda "
            "verilmiştir.<br/>"
            "<b>Santraldeki 16<sup>3</sup> m<sup>2</sup>'lik panel alanında \"Yüksek\" kategoride "
            "güneşlenme olduğunda 1 saatte üretilen toplam enerji kaç Wh olur?</b>"
        ),
        "options": [
            ("A", "2<sup>16</sup>"),
            ("B", "2<sup>17</sup>"),
            ("C", "2<sup>18</sup>"),
            ("D", "2<sup>19</sup>"),
            ("E", "2<sup>20</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 82,
        "day": 6,
        "is_original": False,
        "sim_to": 27,
        "text": (
            "<b>[81. sorudaki tabloya göre] Tablodaki verilere göre, 1 m<sup>2</sup> panelin "
            "ürettiği enerji 2 katına çıktığında soğutma sisteminin enerji tüketimi yüzde kaç "
            "artmaktadır?</b>"
        ),
        "options": [
            ("A", "50"),
            ("B", "100"),
            ("C", "150"),
            ("D", "200"),
            ("E", "300"),
        ],
        "answer": "B",
    },
    {
        "no": 83,
        "day": 6,
        "is_original": False,
        "sim_to": 28,
        "group_notice": "83 ve 84. soruları aşağıdaki bilgilere göre birbirinden bağımsız olarak cevaplayınız.",
        "text": (
            "Bir ses kayıt stüdyosunda dış ortam gürültüsünü engellemek için \"Akustik Katmanlı "
            "Panel\" sistemi kullanılmaktadır. Dış ortamdaki ses enerjisi düzeyi 16<sup>3</sup> "
            "birim olarak ölçülmüştür. Ses dalgası panelin her bir katmanından geçerken enerjisi "
            "bir önceki katmana göre 2<sup>-2</sup> katına düşmektedir.<br/>"
            "<b>Ses dalgası 3 katmanlı bir akustik panel sisteminden geçip stüdyo içine ulaştığında, "
            "iç ortamdaki ses enerjisi kaç birim olur?</b>"
        ),
        "options": [
            ("A", "2<sup>4</sup>"),
            ("B", "2<sup>5</sup>"),
            ("C", "2<sup>6</sup>"),
            ("D", "2<sup>7</sup>"),
            ("E", "2<sup>8</sup>"),
        ],
        "answer": "C",
    },
    {
        "no": 84,
        "day": 6,
        "is_original": False,
        "sim_to": 29,
        "options_vertical": True,
        "text": (
            "Stüdyo duvarına ulaşan mevcut ses enerjisi 2<sup>7</sup> birimdir. Kayıt kalitesi için "
            "bu enerjinin tam olarak 2<sup>4</sup> birim değerine indirilmesi gerekmektedir.<br/>"
            "Ses mühendisinin elinde iki farklı ek yalıtım süngeri seçeneği vardır:<br/>"
            "• <b>Akustik Sünger A:</b> Ses enerjisini doğrudan 4<sup>-1</sup> katına düşürür.<br/>"
            "• <b>Katmanlı Sünger B:</b> Her bir katmanı ses enerjisini 2<sup>-1</sup> katına "
            "düşüren 3 ardışık katmandan oluşur.<br/>"
            "<b>Mühendis, hedeflediği 2<sup>4</sup> birim değerine ulaşmak için hangi süngeri tercih etmelidir?</b>"
        ),
        "options": [
            ("A", "Akustik Sünger A tercih edilmelidir. Çünkü enerjisi tam olarak 2<sup>4</sup> birime indirir."),
            ("B", "Katmanlı Sünger B tercih edilmelidir. Çünkü 3 katman toplamda enerjiyi 2<sup>-3</sup> katına düşürerek 2<sup>4</sup> değerini verir."),
            ("C", "Her iki sünger de aynı sonucu (2<sup>4</sup> birim) vereceği için herhangi biri tercih edilebilir."),
            ("D", "Katmanlı Sünger B enerjiyi 2<sup>3</sup> birime düşürdüğü için A seçilmelidir."),
            ("E", "Her iki sünger de enerjiyi 2<sup>4</sup> birimin üstünde bıraktığı için hiçbiri uygun değildir."),
        ],
        "answer": "B",
    },
    {
        "no": 85,
        "day": 6,
        "is_original": False,
        "sim_to": 28,
        "group_notice": "85 ve 86. soruları aşağıdaki bilgilere göre birbirinden bağımsız olarak cevaplayınız.",
        "text": (
            "Bir laboratuvarda kullanılan \"Koruyucu Kurşun Cam\" sistemi, dışarıdan gelen "
            "ışınım şiddetini her bir katmandan geçerken belirli bir oranda azaltmaktadır.<br/>"
            "Kaynaktaki ışınım şiddeti 25<sup>4</sup> birim olarak belirlenmiştir. Bu ışınım, camın "
            "her bir katmanından geçerken şiddeti bir önceki katmana göre 5<sup>-1</sup> katına düşmektedir.<br/>"
            "<b>Işınım 5 katmanlı bir cam sisteminden geçip gözlem odasına ulaştığında, iç ortamdaki "
            "ışınım şiddeti kaç birim olur?</b>"
        ),
        "options": [
            ("A", "5<sup>2</sup>"),
            ("B", "5<sup>3</sup>"),
            ("C", "5<sup>4</sup>"),
            ("D", "5<sup>5</sup>"),
            ("E", "5<sup>6</sup>"),
        ],
        "answer": "B",
    },
    {
        "no": 86,
        "day": 6,
        "is_original": False,
        "sim_to": 29,
        "options_vertical": True,
        "text": (
            "Gözlem penceresine ulaşan mevcut ışınım şiddeti 5<sup>6</sup> birimdir. Güvenli "
            "çalışma için ışınım şiddetinin tam olarak 5<sup>4</sup> birim değerine indirilmesi "
            "gerekmektedir. Laboratuvar uzmanının elinde iki farklı filtre seçeneği vardır:<br/>"
            "• <b>Nano-Kalkan A:</b> Işınım şiddetini doğrudan 25<sup>-1</sup> katına düşürür.<br/>"
            "• <b>Çoklu-Kalkan B:</b> Her bir katmanı ışınım şiddetini 5<sup>-1</sup> katına "
            "düşüren 2 ardışık katmandan oluşur.<br/>"
            "<b>Uzman, hedeflediği 5<sup>4</sup> birim değerine ulaşmak için hangi kalkanı tercih etmelidir?</b>"
        ),
        "options": [
            ("A", "Yalnızca Nano-Kalkan A tercih edilmelidir, çünkü Çoklu-Kalkan B 5<sup>3</sup> değerini verir."),
            ("B", "Yalnızca Çoklu-Kalkan B tercih edilmelidir, çünkü Nano-Kalkan A 5<sup>2</sup> değerini verir."),
            ("C", "Her iki kalkan da ışınımı 5<sup>-2</sup> katına düşürerek tam olarak 5<sup>4</sup> birime indirdiği için herhangi biri tercih edilebilir."),
            ("D", "Nano-Kalkan A ışınımı 5<sup>5</sup> birime düşürdüğü için yetersiz kalır."),
            ("E", "Her iki kalkan da hedef değer olan 5<sup>4</sup> birime ulaşamaz."),
        ],
        "answer": "C",
    },
    {
        "no": 87,
        "day": 6,
        "is_original": False,
        "sim_to": 19,
        "text": (
            "Bir kentsel dönüşüm projesinde toplam arsa alanı 4 · 12<sup>3</sup> m<sup>2</sup> "
            "olan bir sitede 8 blok ve her blokta 6 daire bulunmaktadır. Site arsasının tamamı "
            "tüm daire sahiplerine eşit olarak paylaştırılacaktır.<br/>"
            "<b>Buna göre bu sitede 1 dairesi bulunan bir kişinin arsa payı kaç m<sup>2</sup>'dir?</b>"
        ),
        "options": [
            ("A", "96"),
            ("B", "108"),
            ("C", "120"),
            ("D", "144"),
            ("E", "192"),
        ],
        "answer": "D",
    },
    {
        "no": 88,
        "day": 6,
        "is_original": False,
        "sim_to": 19,
        "text": (
            "Toplam arsa alanı 5 · 20<sup>3</sup> m<sup>2</sup> olan bir konut projesinde 25 blok "
            "ve her blokta 4 daire yer almaktadır. Arsanın tamamı dairelere eşit olarak "
            "bölüştürülecektir.<br/>"
            "<b>Buna göre 1 daireye düşen arsa payı kaç m<sup>2</sup>'dir?</b>"
        ),
        "options": [
            ("A", "100"),
            ("B", "200"),
            ("C", "250"),
            ("D", "400"),
            ("E", "800"),
        ],
        "answer": "D",
    },
    {
        "no": 89,
        "day": 6,
        "is_original": False,
        "sim_to": 6,
        "text": (
            "M ortamındaki algler her saatin sonunda 8 katına çıkarken, N ortamındaki algler her "
            "saatin sonunda 16 katına çıkmaktadır. Başlangıçta M ortamında 32<sup>3</sup> adet alg, "
            "N ortamında ise 64<sup>3</sup> adet alg bulunmaktadır.<br/>"
            "<b>3 saatin sonunda N ortamında bulunan alg sayısı, t saatin sonunda M ortamında "
            "bulunan alg sayısına eşit olduğuna göre t kaçtır?</b>"
        ),
        "options": [
            ("A", "4"),
            ("B", "5"),
            ("C", "6"),
            ("D", "7"),
            ("E", "8"),
        ],
        "answer": "B",
    },
    {
        "no": 90,
        "day": 6,
        "is_original": False,
        "sim_to": 12,
        "text": (
            "• Eski nesil bir fırın her bir saatte 27<sup>2</sup> Wh elektrik enerjisi tüketmektedir.<br/>"
            "• A++ enerji sınıfı yeni nesil fırın ise her bir saatte 2 · 3<sup>5</sup> Wh elektrik "
            "enerjisi tüketmektedir.<br/>"
            "<b>125 saatlik kullanımda eski fırın yerine yeni fırının tercih edilmesi toplam "
            "15<sup>n</sup> Wh enerji tasarrufu sağladığına göre n kaçtır?</b>"
        ),
        "options": [
            ("A", "3"),
            ("B", "4"),
            ("C", "5"),
            ("D", "6"),
            ("E", "7"),
        ],
        "answer": "C",
    },
]
