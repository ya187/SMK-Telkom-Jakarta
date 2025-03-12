# Script untuk kelangsungan game visual novel SMK Telkom Jakarta

# Default settings
define config.default_text_cps = 7  # Kecepatan teks ketikan (7 karakter per detik)

# Image
# image kak_dika normal = "kak_dika normal.png"
# image kak_alya normal = "kak_alya normal.png"
# image kak_alya marah = "kak_alya marah.png"
# image kak_zahra normal = "kak_zahra normal.png"
# image kak_zahra bahagia = "kak_zahra bahagia.png"
# image kak_zahra kagum = "kak_zahra kagum.png"


# transform auto_scale:
    # zoom 0.5  # Atur sesuai kebutuhan
# define config.start_label = "start"

# Resource
# Gambar Template
image bg blck = "images/blck.png"

# Tokoh dalam game
define aku = Character("[inputname]")
define kak_zahra = Character("Kak Zahra")
define kak_alya = Character("Kak Alya")
define kak_dika = Character("Kak Dika")
define st = Character("Seorang Teman")

# Scene
scene bg titiktemu at Transform(xalign=0.5, yalign=0.5, zoom=2.0)
scene bg bus at Transform(xalign=0.5, yalign=0.5, zoom=2.0)
 
# Alur Game dimulai disini.
label start:
    # show bg titiktemu
    # show aku di tengah
    scene bg blck

    $ inputname = renpy.input("Namaku adalah?")
    "Namaku adalah [inputname], ini adalah ceritaku..."

    "{color=#666666}Aku berdiri sedikit terpisah dari teman-teman sekelasku yang berkumpul di halaman SMP.{/color}"
    "{color=#666666}Mataku memandang jauh, sementara tanganku tanpa sadar memilin ujung seragam yang sedikit kusut.{/color}"
    "{color=#666666}Hari ini kami ada visitasi ke SMK Telkom Jakarta.{/color}"

    "{color=#666666}Sebentar lagi bus akan datang.{/color}"
    "{color=#666666}Aku harus membawa buku catatan sesuai arahan wali kelas.{/color}"
    "{color=#666666}Memangnya kita disuruh menulis esai tentang kunjungan membosankan ini?{/color}"

    "{color=#666666}Tak akan ada yang tahu di balik topeng angkuhku, aku terluka sangat dalam.{/color}"
    "{color=#666666}Ketika aku masih SD, ayahku, seorang programmer, menceraikan ibuku.{/color}"
    "{color=#666666}Sejak saat itu, hidupku berubah.{/color}"

    "{color=#666666}Kami pindah ke rumah yang lebih kecil, dan ibuku harus bekerja ekstra keras.{/color}"
    "{color=#666666}Waktu SD dulu, aku pernah menjadi bahan ejekan karena kami menjadi miskin sejak saat itu.{/color}"

    # ganti scene ke bus
    # show aku gabut di tengah 

    "{color=#666666}Di bus, aku memilih duduk sendirian.{/color}"
    "{color=#666666}Aku memakai handphone dan menatap keluar jendela.{/color}"

    "{color=#666666}Dalam hati, sebenarnya ada ketertarikan tentang SMK yang akan kami kunjungi.{/color}"
    "{color=#666666}Terutama jurusan Rekayasa Perangkat Lunak, bidang yang dulu digeluti ayahku.{/color}"
    "{color=#666666}Tapi lebih mudah bagiku untuk berpura-pura tidak peduli.{/color}"


label pengenalan_pagi:
    # ganti scene ke smk telkom
    # tampilkan senior
    show kak_alya normal at right
    show kak_zahra normal at left

    "{color=#666666}Setibanya di SMK Telkom Jakarta, kami disambut oleh beberapa siswa SMK.{/color}"
    "{color=#666666}Mereka mengenakan seragam rapi dengan almamater merah marun.{/color}"

    # tampilkan kaka dika
    show kak_dika normal

    kak_dika "Selamat datang adik-adik!"


    "{color=#666666}Wow, semangat banget ya, menyedihkan.{/color}"
    "{color=#666666}Gumamku pelan, tapi mataku diam-diam mengamati dengan seksama.{/color}"

    show kak_dika normal

    kak_dika "Rombongannya dibagi menjadi beberapa kelompok kecil ya.."
    kak_dika "Nah, kamu mau mengenal jurusan apa dulu nih?"

    kak_dika "Teknik Transmisi, Teknik Jaringan Akses, Teknik Komputer Jaringan, "
    kak_dika "atau Rekayasa Perangkat Lunak?"


    "{color=#666666}Tiba-tiba jantungku seperti berhenti ketika mendengar jurusan terakhir itu.{/color}"
    "{color=#666666}Aku masih trauma.{/color}"
    "{color=#666666}Aku tidak suka jurusan itu!{/color}"

menu:
    "Teknik Transmisi":
        jump teknik_transmisi
    "Teknik Jaringan Akses":
        jump jaringan_akses
    "Teknik Komputer Jaringan":
        jump komputer_jaringan

label teknik_transmisi:
    scene bg school_gate with fade

    "Oke!"
    "{color=#666666}Ucap Kak Dika sambil tersenyum.{/color}"
    show kak_dika normal
    kak_dika "Berarti sama Kak Dika ya. Perkenalkan, nama saya Dika Saputra."
    kak_dika "Kakak dari jurusan Teknik Transmisi."
    kak_dika "Kalian nggak usah canggung sama kakak ya, adik-adik."
    kak_dika "Kita cuman beda setahun doang kok! Hehe.."

    kak_dika "Teknik Transmisi ya? Bagus juga pilihanmu."
    "{color=#666666}Ucap Kak Dika sambil memimpin kelompok kami.{/color}"
    kak_dika "Ini jurusan yang banyak prakteknya lho."

    "{color=#666666}Aku hanya mengangguk singkat, berusaha menampilkan wajah tidak peduli.{/color}"
    "{color=#666666}Meski diam-diam penasaran.{/color}"
    "{color=#666666}Lebih baik begini—jaga jarak, jangan terlalu antusias.{/color}"
    "{color=#666666}Pengalaman mengajariku bahwa ketertarikan yang ditunjukkan bisa menjadi kelemahan yang dimanfaatkan.{/color}"

    scene bg lab_telecom with fade

    kak_dika "Di sini kita belajar tentang sistem telekomunikasi, mulai dari transmisi satelit, gelombang radio, hingga fiber optik."
    "{color=#666666}Kak Dika menjelaskan sambil menunjukkan laboratorium dengan berbagai peralatan canggih.{/color}"

    "{color=#666666}Beberapa teman sekelasku terlihat terkagum-kagum, bertanya ini-itu dengan semangat.{/color}"
    "{color=#666666}Aku tetap menjaga jarak di belakang kelompok, mengamati semuanya dalam diam.{/color}"
    "{color=#666666}Sebuah perangkat di sudut ruangan menarik perhatianku—beberapa kabel fiber optik yang tersambung ke sebuah panel.{/color}"

    aku "Itu apa?"
    "{color=#666666}Tanyaku tanpa sadar, lalu segera menyesali keputusanku.{/color}"
    "{color=#666666}Seharusnya aku tetap diam saja.{/color}"

    kak_dika "Nah, itu sistem transmisi fiber optik kita. Keren kan?"
    kak_dika "Kamu tertarik sama teknologi komunikasi?"

    aku "Biasa aja."
    "{color=#666666}Jawabku singkat, kembali ke sikap acuhku.{/color}"
    aku "Cuma penasaran."

    scene bg multimedia_room with fade

    "{color=#666666}Setelah mengunjungi beberapa laboratorium, kami dibawa ke ruang multimedia.{/color}"
    "{color=#666666}Di sana ada beberapa komputer dengan program-program yang tidak asing bagiku.{/color}"
    "{color=#666666}Tanpa kusadari, mataku terpaku pada salah satu layar yang menampilkan baris-baris kode.{/color}"

    kak_dika "Ini ruang praktikum bersama dengan anak-anak RPL."
    "{color=#666666}Jelas Kak Dika.{/color}"
    kak_dika "Kadang kita juga butuh skill coding dasar."

    "{color=#666666}Mendengar kata 'RPL' membuat perutku seperti diaduk.{/color}"
    "{color=#666666}Bayangan ayah yang duduk di depan laptop, mengabaikan kehadiranku saat aku masih kecil, muncul tiba-tiba.{/color}"

    aku "Aku ke toilet dulu."
    "{color=#666666}Ucapku tiba-tiba, perlu keluar dari ruangan itu.{/color}"

    scene bg hallway with fade

    "{color=#666666}Kembali dari toilet, aku terdiam sejenak.{/color}"
    "{color=#666666}Jemariku bergerak gelisah, seolah sudah rindu menyentuh keyboard.{/color}"
    "{color=#666666}Sudah lama aku tidak mencoba coding lagi sejak...{/color}"

    scene bg lab_coding with fade

    "{color=#666666}Di lab pemrograman, beberapa komputer sudah dinyalakan dengan program sederhana yang siap digunakan.{/color}"
    kak_dika "Nah, ini simulasi pemrograman dasar."
    kak_dika "Kalian bisa mencoba membuat aplikasi kalkulator sederhana."

    kak_dika "Ada yang mau mencoba duluan?"

    "{color=#666666}Beberapa saat kemudian, teman-temanku mulai mencoba dengan canggung.{/color}"
    "{color=#666666}Sebagian besar kebingungan dengan konsep dasar pemrograman.{/color}"
    "{color=#666666}Tanpa sadar, aku mendecih pelan melihat kesalahan-kesalahan sederhana yang mereka lakukan.{/color}"

    kak_dika "Kenapa?"
    "{color=#666666}Tanya Kak Dika yang menyadari reaksiku.{/color}"

    aku "Bukan apa-apa."
    "{color=#666666}Bantahku cepat.{/color}"

    kak_dika "Kalau kamu bisa, kenapa nggak bantu mereka?"

    aku "Siapa bilang aku bisa?"
    "{color=#666666}Tanyaku tajam.{/color}"

    kak_dika "Gerak-gerikmu. Kamu paham coding kan?"
    kak_dika "Terlihat dari caramu memperhatikan layar mereka."
    kak_dika "Kamu bahkan menggumamkan koreksi tadi."

    "{color=#666666}Aku tidak menyadari bahwa aku melakukan itu.{/color}"
    "{color=#666666}Sejenak, aku merasa terpojok.{/color}"

    aku "Kenapa sih kakak peduli?"
    "{color=#666666}Tanyaku dingin.{/color}"

    kak_dika "Cuma penasaran aja, kenapa kamu pura-pura nggak bisa padahal bisa."

    "{color=#666666}Kata-katanya menusuk tepat sasaran. Aku terdiam, memikirkan jawaban yang tepat.{/color}"

    aku "Oke, saya mau coba."
    "{color=#666666}Tiba-tiba aku berkata, mengangkat tangan dan maju ke depan.{/color}"

    scene bg lab_coding_focus with fade

    "{color=#666666}Entah apa yang merasukiku.{/color}"
    "{color=#666666}Mungkin ego, mungkin juga rasa kesal karena Kak Dika membaca karakterku dengan tepat.{/color}"
    "{color=#666666}Aku duduk di depan komputer dan mulai mengetik dengan cepat.{/color}"

    jump lanjut_transmisi

label jaringan_akses:
    scene bg school_gate with fade

    "Oke!"
    "{color=#666666}Ucap Kak Dika sambil tersenyum.{/color}"
    show kak_dika normal
    kak_dika "Kalau begitu, kamu bisa ikut kelompok Kak Alya. Dia ketua dari jurusan Teknik Jaringan Akses."
    hide kak_dika

    scene bg lab_telecom with fade

    show kak_alya normal
    kak_alya "Di jurusan Teknik Jaringan Akses, kita fokus pada infrastruktur telekomunikasi yang langsung berhubungan dengan pengguna."
    "{color=#666666}Kak Alya berbicara dengan lantang dan tegas.{/color}"
    show kak_alya marah
    kak_alya "Tidak seperti jurusan lain, kita punya target yang TERUKUR dan JELAS! Waktu kita terbatas, jadi dengarkan baik-baik!"

    "{color=#666666}Beberapa teman sekelompokku saling berpandangan, tidak menyangka akan mendapat pemandu yang begitu... intens.{/color}"
    "{color=#666666}Tiba-tiba, Kak Alya menunjuk ke arahku.{/color}"

    kak_alya "Kamu! Ya, kamu yang baru gabung. Kenapa terlambat? Kita sudah mulai lima menit yang lalu!"
    aku "Saya baru pindah kelompok, Kak."
    "{color=#666666}jawabku datar, berusaha tetap tenang.{/color}"

    show kak_alya normal
    kak_alya "Lain kali, kalau mau pindah, bilang dari awal! Waktu kita berharga!"
    kak_alya "Oke, semuanya ikut saya!"

    scene bg lab_fiber_optic with fade

    kak_alya "Ini laboratorium kabel optik kita."
    "{color=#666666}jelasnya sambil menunjuk beberapa perangkat.{/color}"
    kak_alya "Di sini kita belajar bagaimana mentransmisikan data melalui jaringan fiber optik yang menghubungkan rumah-rumah pelanggan!"

    "{color=#666666}Aku memperhatikan dengan acuh tak acuh, meski sebenarnya cukup tertarik.{/color}"
    "{color=#666666}Ada sesuatu tentang cara kerja perangkat keras yang menarik bagiku—jauh berbeda dari dunia pemrograman yang abstrak.{/color}"

    kak_alya "Kamu,"
    "{color=#666666}Kak Alya kembali menunjukku.{/color}"
    kak_alya "Coba jelaskan apa yang kamu tahu tentang fiber optik."
    aku "Umm, itu kabel yang mentransmisikan data melalui cahaya?"
    "{color=#666666}jawabku ragu.{/color}"

    kak_alya "BENAR!"
    "{color=#666666}serunya.{/color}"
    kak_alya "Dan kenapa kita menggunakan fiber optik daripada kabel tembaga? Ada yang tahu?"

    aku "Karena kecepatannya jauh lebih tinggi?"
    "{color=#666666}jawabku pelan.{/color}"
    kak_alya "Tepat! Kabel fiber optik bisa mentransmisikan data hingga 100 Gbps! Itu seratus kali lipat dari kabel tembaga biasa!"

    aku "Oh."
    kak_alya "Oh? Hanya itu responsmu?"
    "{color=#666666}tantangnya.{/color}"
    kak_alya "Kamu tidak terlihat tertarik. Apa ini bukan jurusan yang kamu minati?"

    aku "Saya cuma belum paham sepenuhnya, Kak."
    "{color=#666666}jawabku, sedikit defensif.{/color}"

    kak_alya "Bagus. Keraguan adalah awal dari pengetahuan."
    "{color=#666666}ucapnya.{/color}"
    kak_alya "Mari kita lihat peralatan fusion splicer untuk menyambung kabel fiber optik."

    scene bg lab_fusion_splicer with fade

    kak_alya "Ini adalah alat untuk menyambung kabel fiber optik yang putus. Prosesnya sangat presisi dan membutuhkan ketelitian tinggi."
    "{color=#666666}jelasnya.{/color}"
    kak_alya "Siapa yang mau mencoba?"

    "{color=#666666}Tanpa kusadari, tanganku terangkat.{/color}"
    aku "Saya, Kak."

    kak_alya "Bagus! Akhirnya ada yang berinisiatif! Kemari!"

    "{color=#666666}Aku melangkah maju, mencoba mengingat apa yang pernah kubaca tentang kabel optik di internet.{/color}"
    "{color=#666666}Kak Alya memberikan instruksi dengan tegas tapi jelas, menunjukkan cara memasang kabel pada penjepit dengan hati-hati.{/color}"

    kak_alya "Pegang steady... fokus... tekanannya harus pas... BAGUS!"
    "{color=#666666}serunya.{/color}"
    kak_alya "Kamu punya bakat untuk pekerjaan presisi!"

    "{color=#666666}Pujian itu terasa menyenangkan. Berbeda dengan coding yang selalu mengingatkanku pada ayah, ini adalah sesuatu yang baru—sesuatu yang murni milikku.{/color}"

    scene bg lab_measurement with fade

    kak_alya "Oke, selanjutnya kita akan ke lab pengukuran."
    "{color=#666666}Kak Alya melanjutkan.{/color}"
    kak_alya "Di sana kalian akan melihat bagaimana kita menganalisis kualitas sinyal pada jaringan akses!"

    st "Psst," 
    "{color=#666666}bisik seorang teman di sampingku.{/color}"
    st "Kak Alya serem ya?"

    aku "Menurutku sih biasa aja. Dia cuma... passionate."

    "{color=#666666}Di lab pengukuran, Kak Alya menunjukkan berbagai alat canggih yang digunakan untuk menganalisis kualitas sinyal.{/color}"
    kak_alya "Ini namanya OTDR—Optical Time Domain Reflectometer."
    "{color=#666666}jelasnya.{/color}"
    kak_alya "Alat ini bisa mendeteksi di mana letak putusnya kabel fiber optik bahkan dalam jarak puluhan kilometer!"

    "{color=#666666}Aku tidak bisa menyembunyikan ketertarikanku. Teknologi ini benar-benar keren.{/color}"

    aku "Bagaimana cara kerjanya, Kak?"
    "{color=#666666}tanyaku tanpa sadar.{/color}"

    "{color=#666666}Mata Kak Alya bersinar.{/color}"
    kak_alya "OTDR memancarkan pulsa cahaya ke dalam fiber optik, lalu menganalisis seberapa banyak cahaya yang dipantulkan kembali. Jika ada kerusakan, akan terlihat sebagai spike pada grafik!"

    jump lanjut_akses

label komputer_jaringan:
    scene bg school_gate with fade

    "Oke!"
    "{color=#666666}Ucap Kak Dika sambil tersenyum.{/color}"
    show kak_dika normal
    kak_dika "Kalau begitu, kamu bisa ikut kelompok Kak Zahra. Dia ketua dari jurusan Teknik Komputer dan Jaringan."

    scene bg lab_network with fade

    show kak_zahra bahagia
    kak_zahra "Di jurusan TKJ, kita belajar segala hal tentang jaringan komputer dan teknologi informasi."
    "{color=#666666}Kak Zahra berbicara dengan ceria, matanya berbinar penuh semangat.{/color}"
    kak_zahra "Di sini kita belajar tentang setting router, troubleshooting jaringan, hingga keamanan siber!"

    "{color=#666666}Beberapa teman sekelompokku terlihat antusias, tapi aku masih ragu.{/color}"
    "{color=#666666}Aku memang tertarik dengan teknologi, tapi ada sesuatu dalam diriku yang membuatku menahan diri.{/color}"

    "{color=#666666}Kak Zahra tiba-tiba menunjukku.{/color}"
    show kak_zahra normal
    kak_zahra "Kamu kelihatan penasaran! Mau coba setting router?"

    aku "Eh... nggak perlu, Kak."
    "{color=#666666}Jawabku cepat, berusaha tetap tenang.{/color}"

    kak_zahra "Yakin? Aku perhatiin dari tadi kamu kayak udah ngerti dasar-dasarnya. Pasti pernah coba sendiri, kan?"

    "{color=#666666}Aku terkejut dia bisa membaca sikapku. Dengan ragu, aku akhirnya menerima router yang disodorkannya.{/color}"

    "{color=#666666}Aku mulai menyambungkan kabel dengan hati-hati, mengikuti instruksi Kak Zahra. Begitu halaman konfigurasi router muncul, tanganku bergerak otomatis.{/color}"

    show kak_zahra kagum
    kak_zahra "Wah, kamu tahu default username dan passwordnya!"
    "{color=#666666}Seru Kak Zahra kagum.{/color}"
    kak_zahra "Beneran cuma 'baca-baca sedikit' nih?"

    "{color=#666666}Aku mengangkat bahu, mencoba tampak acuh tak acuh meski diam-diam merasa senang dengan pengakuannya.{/color}"

    kak_zahra "Ini konfigurasi dasar untuk setting WiFi."
    "{color=#666666}Lanjutku, jari-jariku mengubah beberapa parameter.{/color}"
    aku "Kalau mau lebih aman, enkripsinya pakai WPA2-PSK."

    show kak_zahra bahagia
    kak_zahra "Ya ampun! Kamu udah kayak pro! Kenapa nggak bilang dari tadi?"
    "{color=#666666}Kata Kak Zahra sambil tertawa.{/color}"

    aku "Aku... dulunya suka teknologi."
    "{color=#666666}Kataku akhirnya.{/color}"

    show kak_zahra normal
    kak_zahra "Terus kenapa sekarang nggak suka lagi?"

    aku "Karena teknologi mengingatkanku pada seseorang yang sudah pergi."

    "{color=#666666}Kak Zahra terdiam sejenak, lalu tersenyum hangat.{/color}"
    show kak_zahra bahagia
    kak_zahra "Aku ngerti. Tapi teknologi itu cuma alat. Yang menentukan bagaimana kita menggunakannya adalah kita sendiri."

    "{color=#666666}Aku terdiam, mencerna kata-katanya.{/color}"

    show kak_zahra normal
    kak_zahra "Hey, tahu nggak? Kita juga belajar ethical hacking! Seru banget!"
    "{color=#666666}Katanya berusaha mengubah suasana.{/color}"

    aku "Ethical hacking?"

    show kak_zahra bahagia
    kak_zahra "Iya! Kita belajar cara melindungi sistem dari serangan. Jadi, kalau kamu gabung TKJ, kita bisa jadi superhero digital!"
    "{color=#666666}Katanya sambil mengacungkan tinjunya ke udara.{/color}"

    "{color=#666666}Aku tak bisa menahan senyum tipis. Mungkin... ini bisa jadi awal yang baru bagiku.{/color}"

    jump lanjut_jaringan

label lanjut_transmisi:
    "{color=#666666}Bel berbunyi nyaring, menandakan waktu istirahat. Aku masih duduk di bawah pohon, memikirkan percakapanku dengan Kak Dika. Kata-katanya tentang tidak kehilangan dua hal sekaligus masih terngiang di telingaku.{/color}"
    
    "Waktunya kumpul!" 
    kak_alya "Istirahat selesai, kita akan mulai sesi kedua pengenalan jurusan!"
    
    "{color=#666666}Dengan langkah berat, aku kembali ke lobi. Semua siswa sudah berkumpul, menunggu instruksi selanjutnya.{/color}"
    
    kak_dika "Baiklah adik-adik, setelah sesi pertama tadi, sekarang kita akan melanjutkan dengan sesi kedua pengenalan jurusan."
    kak_dika "Kalian boleh memilih jurusan yang berbeda dari sesi pertama untuk mendapatkan pengalaman yang lebih beragam."
    
    "{color=#666666}Kak Dika menjelaskan bahwa di sesi kedua ini, ada tiga jurusan yang bisa dikunjungi: Teknik Jaringan Akses, Teknik Komputer Jaringan (TKJ), dan Rekayasa Perangkat Lunak (RPL).{/color}"
    
    "{color=#666666}Mendengar kata RPL, jantungku berdegup kencang. Bayangan tentang ayah kembali berkelebat di pikiranku. Tapi kali ini, ada sesuatu yang berbeda. Kata-kata Kak Dika membuka celah kecil dalam perisaiku.{/color}"
    
    st "Kemana kamu akan pergi?"
    aku "Entahlah, {color=#666666}jawabku pendek, masih berpikir.{/color}"
    
    "{color=#666666}Di depanku terbentang tiga pilihan. Teknik Jaringan Akses yang tampaknya berfokus pada infrastruktur telekomunikasi. TKJ yang mungkin lebih ke arah hardware dan networking. Dan... RPL, jurusan yang selama ini kuhindari.{/color}"
    
menu:
    "Ending 1 RPL":
        jump ending_rpl
    "Ending 2 TKJ":
        jump ending_tkj
    "Ending 3 TJA":
        jump ending_tja
    "Ending 4 TR":
            jump ending_tr

label lanjut_akses:
    "{color=#666666}Setidaknya sekarang aku punya sesuatu yang baru untuk dipikirkan—sesuatu yang tidak terkait dengan bayang-bayang masa lalu. Mungkin... mungkin ada jalan lain untukku selain menghindari apa yang kusukai.{/color}"
    
    "{color=#666666}Di lobi, Kak Dika memberikan arahan ke kami. Aku berdiri agak di belakang, setengah mendengarkan. Pikiranku masih dipenuhi percakapan dengan Kak Alya tadi.{/color}"
    
    kak_dika "Setelah sesi pertama tadi, sekarang kita akan melanjutkan dengan sesi kedua pengenalan jurusan."
    kak_dika "Kalian boleh memilih jurusan yang berbeda dari sesi pertama untuk mendapatkan pengalaman yang lebih beragam."
    kak_dika "Manfaatkan kesempatan ini untuk lebih mengenal SMK Telkom Jakarta."
    
    "{color=#666666}Kak Dika menjelaskan bahwa di sesi kedua ini, ada tiga jurusan yang bisa dikunjungi: Teknik Jaringan Akses, Teknik Komputer Jaringan (TKJ), dan Rekayasa Perangkat Lunak (RPL).{/color}"
    
    "{color=#666666}Mendengar kata RPL, jantungku berdegup kencang. Bayangan tentang ayah kembali berkelebat di pikiranku. Tapi kali ini, ada sesuatu yang berbeda. Kata-kata Kak Dika membuka celah kecil dalam perisaiku.{/color}"
    
    st "Kemana kamu akan pergi?"
    aku "Entahlah, {color=#666666}jawabku pendek, masih berpikir.{/color}"
    
    "{color=#666666}Di depanku terbentang tiga pilihan. Teknik Transmisi yang tampaknya berfokus pada cara data dikirim melalui media komunikasi. TKJ yang mungkin lebih ke arah hardware dan networking. Dan... RPL, jurusan yang selama ini kuhindari.{/color}"
    
menu:
    "Ending 5 RPL":
        jump ending_rpl
    "Ending 6 TKJ":
        jump ending_tkj
    "Ending 7 TJA":
        jump ending_tja
    "Ending 8 TR":
        jump ending_tr

label lanjut_jaringan:
    "terima kasih"
