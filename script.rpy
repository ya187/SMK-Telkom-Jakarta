# Script untuk kelangsungan game visual novel SMK Telkom Jakarta

# Default settings
define config.default_text_cps = 7  # Kecepatan teks ketikan (30 karakter per detik)
# define config.start_label = "start"

#Transform
transform bigger:
    zoom 1.5

transform smaller:
    zoom 0.5

# Resource
# Backgrounds
image gerbang = "images/background/bg gerbang.jpeg"
image gor = "images/background/bg gor.jpeg"
image kantin = "images/background/bg kantin.jpeg"
image kelas = "images/background/bg kelas.jpeg"
image koridor = "images/background/bg koridor.jpeg"
image lab = "images/background/bg lab.jpeg"
image lantai2 = "images/background/bg lantaisatu.jpeg"
image lantai1 = "images/background/bg lantaidua.jpeg"
image lantai3 = "images/background/bg lantaitiga.jpeg"
image lobi = "images/background/bg lobi.jpeg"
image masjid = "images/background/bg masjid.jpeg"
image petamoja = "images/background/bg petamoja.jpeg"

#Sprites Char

#Kak Zahra (K_Z)
image k_z happy = "images/characters/K_Z/k_z happy.png"
image k_z idle = "images/characters/K_Z/k_z idle.png"
image k_z point = "images/characters/K_Z/k_z point.png"
image k_z sad = "images/characters/K_Z/k_z sad.png"
image k_z talk = "images/characters/K_Z/k_z talking.png"
image k_z smile = "images/characters/K_Z/k_z smiling.png"
image k_z original = "images/characters/K_Z/k_z original.png"

#Kak Alya (K_A)
image k_a idle = "images/characters/K_A/k_a idle.png"
image k_a mad = "images/characters/K_A/k_a mad.png"
image k_a point = "images/characters/K_A/k_a point_serious.png"
image k_a talking = "images/characters/K_A/k_a talking.png"



# Tokoh dalam game
# Main Character
define aku = Character("Aku")
# Kakak-kakak Senior
define k_z = Character("Kak Zahra")
define k_a = Character("Kak Alya")
define k_d = Character("Kak Dika")

# Scene
scene bg titiktemu at Transform(xalign=0.5, yalign=0.5, zoom=2.0)
scene bg bus at Transform(xalign=0.5, yalign=0.5, zoom=2.0)
 
# Alur Game dimulai disini.
label start:
    # show bg titiktemu
    # show aku di tengah
    scene black

    "Aku berdiri sedikit terpisah dari teman-teman sekelasku yang berkumpul di halaman SMP."
    "Mataku memandang jauh, sementara tanganku tanpa sadar memilin ujung seragam yang sedikit kusut."
    "Hari ini kami ada visitasi ke SMK Telkom Jakarta."

    "Sebentar lagi bus akan datang."
    "Aku harus membawa buku catatan sesuai arahan wali kelas."
    "Memangnya kita disuruh menulis esai tentang kunjungan membosankan ini?"

    "Tak akan ada yang tahu di balik topeng angkuhku, aku terluka sangat dalam."
    "Ketika aku masih SD, ayahku, seorang programmer, menceraikan ibuku."
    "Sejak saat itu, hidupku berubah."

    "Kami pindah ke rumah yang lebih kecil, dan ibuku harus bekerja ekstra keras."
    "Waktu SD dulu, aku pernah menjadi bahan ejekan karena kami menjadi miskin sejak saat itu."

    # ganti scene ke bus
    # show aku gabut di tengah 

    "Di bus, aku memilih duduk sendirian."
    "Aku memakai handphone dan menatap keluar jendela."

    "Dalam hati, sebenarnya ada ketertarikan tentang SMK yang akan kami kunjungi."
    "Terutama jurusan Rekayasa Perangkat Lunak, bidang yang dulu digeluti ayahku."
    "Tapi lebih mudah bagiku untuk berpura-pura tidak peduli."


label pengenalan_pagi:
    scene gerbang with fade :
        bigger
    # ganti scene ke smk telkom
    # tampilkan senior

    "Setibanya di SMK Telkom Jakarta, kami disambut oleh beberapa siswa SMK."
    "Mereka mengenakan seragam rapi dengan almamater merah marun."

    # tampilkan kaka dika
    show k_d #with smile

    k_d "Selamat datang adik-adik!"

    "Wow, semangat banget ya, menyedihkan."
    "Gumamku pelan, tapi mataku diam-diam mengamati dengan seksama."

    show k_d #with normal

    k_d "Rombongannya dibagi menjadi beberapa kelompok kecil ya.."
    k_d "Nah, kamu mau mengenal jurusan apa dulu nih?"

    k_d "Teknik Transmisi, Teknik Jaringan Akses, Teknik Komputer Jaringan, "
    k_d "atau Rekayasa Perangkat Lunak?"

    "Tiba-tiba jantungku seperti berhenti ketika mendengar jurusan terakhir itu."
    "Aku masih trauma."
    "Aku tidak suka jurusan itu!"

menu:
    "Teknik Transmisi":
        jump teknik_transmisi
    "Teknik Jaringan Akses":
        jump jaringan_akses
    "Teknik Komputer Jaringan":
        jump komputer_jaringan

label teknik_transmisi:
    scene bg_gerbang with fade

    k_d "Oke!" 
    "Ucap Dika lagi."
    k_d "Berarti sama Kak Dika ya. Perkenalkan, nama saya Dika Saputra."
    k_d "Kakak dari jurusan Teknik Transmisi."
    k_d "Kalian nggak usah canggung sama kakak ya, adik-adik."
    k_d "Kita cuman beda setahun doang kok! Hehe.."

    k_d "Teknik Transmisi ya? Bagus juga pilihanmu," 
    "Ucap Dika sambil memimpin kelompok kami."
    k_d "Ini jurusan yang banyak prakteknya lho."

    "Aku hanya mengangguk singkat, berusaha menampilkan wajah tidak peduli."
    "Meski diam-diam penasaran."
    "Lebih baik begini—jaga jarak, jangan terlalu antusias."
    "Pengalaman mengajariku bahwa ketertarikan yang ditunjukkan bisa menjadi kelemahan yang dimanfaatkan."

    scene bg lab_telecom with fade

    k_d "Di sini kita belajar tentang sistem telekomunikasi, mulai dari transmisi satelit, gelombang radio, hingga fiber optik."
    "Kak Dika menjelaskan sambil menunjukkan laboratorium dengan berbagai peralatan canggih."

    "Beberapa teman sekelasku terlihat terkagum-kagum, bertanya ini-itu dengan semangat."
    "Aku tetap menjaga jarak di belakang kelompok, mengamati semuanya dalam diam."
    "Sebuah perangkat di sudut ruangan menarik perhatianku—beberapa kabel fiber optik yang tersambung ke sebuah panel."

    aku "Itu apa?"
    "Tanyaku tanpa sadar, lalu segera menyesali keputusanku."
    "Seharusnya aku tetap diam saja."

    k_d "Nah, itu sistem transmisi fiber optik kita. Keren kan?"
    k_d "Kamu tertarik sama teknologi komunikasi?"

    aku "Biasa aja," 
    "Jawabku singkat, kembali ke sikap acuhku."
    aku "Cuma penasaran."

    scene bg multimedia_room with fade

    "Setelah mengunjungi beberapa laboratorium, kami dibawa ke ruang multimedia."
    "Di sana ada beberapa komputer dengan program-program yang tidak asing bagiku."
    "Tanpa kusadari, mataku terpaku pada salah satu layar yang menampilkan baris-baris kode."

    "Ini ruang praktikum bersama dengan anak-anak RPL."
    "Jelas Kak Dika."
    "Kadang kita juga butuh skill coding dasar."

    "Mendengar kata 'RPL' membuat perutku seperti diaduk."
    "Bayangan ayah yang duduk di depan laptop, mengabaikan kehadiranku saat aku masih kecil, muncul tiba-tiba."

    "Aku ke toilet dulu."
    "Ucapku tiba-tiba, perlu keluar dari ruangan itu."

    scene bg hallway with fade

    "Kembali dari toilet, aku terdiam sejenak."
    "Jemariku bergerak gelisah, seolah sudah rindu menyentuh keyboard."
    "Sudah lama aku tidak mencoba coding lagi sejak..."

    scene bg lab_coding with fade

    "Di lab pemrograman, beberapa komputer sudah dinyalakan dengan program sederhana yang siap digunakan."
    "Nah, ini simulasi pemrograman dasar."
    "Kalian bisa mencoba membuat aplikasi kalkulator sederhana."

    "Ada yang mau mencoba duluan?"

    "Beberapa saat kemudian, teman-temanku mulai mencoba dengan canggung."
    "Sebagian besar kebingungan dengan konsep dasar pemrograman."
    "Tanpa sadar, aku mendecih pelan melihat kesalahan-kesalahan sederhana yang mereka lakukan."

    "Kenapa?"
    "Tanya Kak Dika yang menyadari reaksiku."

    "Bukan apa-apa."
    "Bantahku cepat."

    "Kalau kamu bisa, kenapa nggak bantu mereka?"
    "Tantang Lina."

    "Siapa bilang aku bisa?"
    "Tanyaku tajam."

    "Gerak-gerikmu."
    "Jawabnya santai."
    "Kamu paham coding kan?"
    "Terlihat dari caramu memperhatikan layar mereka."
    "Kamu bahkan menggumamkan koreksi tadi."

    "Aku tidak menyadari bahwa aku melakukan itu."
    "Sejenak, aku merasa terpojok."

    "Kenapa sih kakak peduli?"
    "Tanyaku dingin."

    "Cuma penasaran aja, kenapa kamu pura-pura nggak bisa padahal bisa."

    "Kata-katanya menusuk tepat sasaran. Aku terdiam, memikirkan jawaban yang tepat."

    "Oke, saya mau coba."
    "Tiba-tiba aku berkata, mengangkat tangan dan maju ke depan."

    scene bg lab_coding_focus with fade

    "Entah apa yang merasukiku."
    "Mungkin ego, mungkin juga rasa kesal karena Kak Dika membaca karakterku dengan tepat."
    "Aku duduk di depan komputer dan mulai mengetik dengan cepat."
    "Jari-jariku bergerak dengan familier di atas keyboard, seolah bertemu kembali dengan teman lama."

    "Dalam waktu singkat, aku tidak hanya membuat kalkulator sederhana, tapi juga menambahkan beberapa fitur seperti penghitung akar kuadrat dan logaritma."

    "Lab mendadak sunyi."
    "Aku tersadar dan segera berhenti mengetik."
    "Semua mata tertuju padaku dengan tatapan kagum."

    "Wah, kamu jago banget!"
    "Seru Kak Dika."
    "Kamu belajar coding di mana?"

    "Internet."
    "Jawabku singkat, berusaha mengusir kenangan itu."

    "Kamu cocok banget masuk jurusan RPL lho."
    "Kata Kak Dika antusias."
    "Dengan dasar seperti ini, kamu bisa—"

    "Aku nggak tertarik dengan RPL."
    "Potongku tajam, bangkit dari kursi."
    "Permisi."

    "Aku berjalan cepat keluar dari lab, mengabaikan panggilan Kak Dika di belakangku."
    "Koridor sekolah terasa panjang dan menyesakkan. Aku butuh udara segar."

    scene bg school_yard with fade

    "Di halaman belakang sekolah, aku duduk sendirian di bawah pohon rindang."
    "Angin sepoi-sepoi menyapu wajahku, tapi tidak cukup untuk mendinginkan gejolak di dadaku."

    "Boleh duduk di sini?"
    "Suara familiar Kak Dika terdengar."

    "Tanpa menunggu jawabanku, dia sudah duduk di sampingku."

    jump end

label jaringan_akses:
    scene bg school_gate with fade

    k_d "Oke!"
    "Ucap Kak Dika sambil tersenyum."
    k_d "Kalau begitu, kamu bisa ikut kelompok Kak Alya. Dia ketua dari jurusan Teknik Jaringan Akses."
    
    scene bg lab_telecom with fade

    "Di jurusan Teknik Jaringan Akses, kita fokus pada infrastruktur telekomunikasi yang langsung berhubungan dengan pengguna."
    "Kak Alya berbicara dengan lantang dan tegas."
    "Tidak seperti jurusan lain, kita punya target yang TERUKUR dan JELAS! Waktu kita terbatas, jadi dengarkan baik-baik!"
    
    "Beberapa teman sekelompokku saling berpandangan, tidak menyangka akan mendapat pemandu yang begitu... intens."
    "Tiba-tiba, Kak Alya menunjuk ke arahku."
    
    "Kamu! Ya, kamu yang baru gabung. Kenapa terlambat? Kita sudah mulai lima menit yang lalu!"
    "Saya baru pindah kelompok, Kak, jawabku datar, berusaha tetap tenang."
    
    "Lain kali, kalau mau pindah, bilang dari awal! Waktu kita berharga! tegurnya tanpa basa-basi. Oke, semuanya ikut saya!"
    
    scene bg lab_fiber_optic with fade
    
    "Ini laboratorium kabel optik kita, jelasnya sambil menunjuk beberapa perangkat. Di sini kita belajar bagaimana mentransmisikan data melalui jaringan fiber optik yang menghubungkan rumah-rumah pelanggan!"
    
    "Aku memperhatikan dengan acuh tak acuh, meski sebenarnya cukup tertarik."
    "Ada sesuatu tentang cara kerja perangkat keras yang menarik bagiku—jauh berbeda dari dunia pemrograman yang abstrak."
    
    "Kamu, Kak Alya kembali menunjukku. Coba jelaskan apa yang kamu tahu tentang fiber optik."
    "Umm, itu kabel yang mentransmisikan data melalui cahaya? jawabku ragu."
    
    "BENAR! serunya. Dan kenapa kita menggunakan fiber optik daripada kabel tembaga? Ada yang tahu?"
    
    "Karena kecepatannya jauh lebih tinggi? jawabku pelan."
    "Tepat! Kabel fiber optik bisa mentransmisikan data hingga 100 Gbps! Itu seratus kali lipat dari kabel tembaga biasa!"
    
    "Oh."
    "Oh? Hanya itu responsmu? tantangnya. Kamu tidak terlihat tertarik. Apa ini bukan jurusan yang kamu minati?"
    
    "Saya cuma belum paham sepenuhnya, Kak, jawabku, sedikit defensif."
    
    "Bagus. Keraguan adalah awal dari pengetahuan, ucapnya. Mari kita lihat peralatan fusion splicer untuk menyambung kabel fiber optik."
    
    scene bg lab_fusion_splicer with fade
    
    "Ini adalah alat untuk menyambung kabel fiber optik yang putus. Prosesnya sangat presisi dan membutuhkan ketelitian tinggi, jelasnya. Siapa yang mau mencoba?"
    
    "Tanpa kusadari, tanganku terangkat."
    "Saya, Kak."
    
    "Bagus! Akhirnya ada yang berinisiatif! Kemari!"
    
    "Aku melangkah maju, mencoba mengingat apa yang pernah kubaca tentang kabel optik di internet."
    "Kak Alya memberikan instruksi dengan tegas tapi jelas, menunjukkan cara memasang kabel pada penjepit dengan hati-hati."
    
    "Pegang steady... fokus... tekanannya harus pas... BAGUS! serunya. Kamu punya bakat untuk pekerjaan presisi!"
    
    "Pujian itu terasa menyenangkan. Berbeda dengan coding yang selalu mengingatkanku pada ayah, ini adalah sesuatu yang baru—sesuatu yang murni milikku."
    
    scene bg lab_measurement with fade
    
    "Oke, selanjutnya kita akan ke lab pengukuran, Kak Alya melanjutkan. Di sana kalian akan melihat bagaimana kita menganalisis kualitas sinyal pada jaringan akses!"
    
    "Psst, bisik seorang teman di sampingku. Kak Alya serem ya?"
    
    "Aku mengangkat bahu. Menurutku sih biasa aja. Dia cuma... passionate."
    
    "Di lab pengukuran, Kak Alya menunjukkan berbagai alat canggih yang digunakan untuk menganalisis kualitas sinyal."
    "Ini namanya OTDR—Optical Time Domain Reflectometer, jelasnya. Alat ini bisa mendeteksi di mana letak putusnya kabel fiber optik bahkan dalam jarak puluhan kilometer!"
    
    "Aku tidak bisa menyembunyikan ketertarikanku. Teknologi ini benar-benar keren."
    
    "Bagaimana cara kerjanya, Kak? tanyaku tanpa sadar."
    
    "Mata Kak Alya bersinar. OTDR memancarkan pulsa cahaya ke dalam fiber optik, lalu menganalisis seberapa banyak cahaya yang dipantulkan kembali. Jika ada kerusakan, akan terlihat sebagai spike pada grafik!"
    
    "Beberapa menit kemudian, aku sudah terlibat diskusi teknis dengan Kak Alya. Aku lupa sejenak tentang sikapku yang biasanya acuh tak acuh."
    
    "Kamu punya potensi di bidang ini, kata Kak Alya tiba-tiba. Tidak banyak siswa SMP yang bisa memahami konsep-konsep teknis secepat kamu."
    
    "Aku terdiam, tidak tahu harus merespon bagaimana."
    
    "Kenapa kamu tertarik dengan Teknik Jaringan Akses? Biasanya anak-anak lebih tertarik dengan jurusan seperti RPL."
    
    "Mendengar kata 'RPL', wajahku langsung berubah. Kak Alya menyadarinya."
    
    "Ah, ada masalah dengan RPL?"
    "Tidak, jawabku singkat. Saya cuma lebih tertarik dengan hardware daripada software."
    
    "Baiklah, katanya akhirnya. Tapi ingat, di dunia teknologi, pilihan terbaik adalah memahami keduanya—hardware dan software. Jangan pernah membatasi dirimu hanya karena... apapun alasanmu."
    
    "Kata-katanya menusuk tepat sasaran. Aku tertegun."
    
    scene bg school_hall with fade
    
    "Saat kembali ke kelompok utama, aku memikirkan kata-kata Kak Alya. Mungkinkah dia benar?"
    "Apakah aku membatasi diriku sendiri hanya karena trauma masa lalu?"
    
    "Tapi sebelum aku sempat memikirkannya lebih jauh, pengumuman berkumpul untuk sesi terakhir sudah terdengar. Saatnya kembali ke aula utama."
    
    "Setidaknya sekarang aku punya sesuatu yang baru untuk kupikirkan—sesuatu yang tidak terkait dengan bayang-bayang masa lalu."

    jump end

label komputer_jaringan:
    scene bg school_gate with fade

    k_d "Oke!"  
    "Ucap Kak Dika sambil tersenyum."
    k_d "Kalau begitu, kamu bisa ikut kelompok Kak Zahra. Dia ketua dari jurusan Teknik Komputer dan Jaringan."

    scene bg lab_network with fade

    show k_z talk with fade :
        smaller
        xalign 0.5
    k_z "Di jurusan TKJ, kita belajar segala hal tentang jaringan komputer dan teknologi informasi."  
    "Kak Zahra berbicara dengan ceria, matanya berbinar penuh semangat."  
    k_z"Di sini kita belajar tentang setting router, troubleshooting jaringan, hingga keamanan siber!"

    show k_z idle :
        smaller
        xalign 0.5
    "Beberapa teman sekelompokku terlihat antusias, tapi aku masih ragu."  
    "Aku memang tertarik dengan teknologi, tapi ada sesuatu dalam diriku yang membuatku menahan diri."

    "Kak Zahra tiba-tiba menunjukku."  
    show k_z point :
        smaller
        xalign 0.5
    "Kamu kelihatan penasaran! Mau coba setting router?"

    "Eh... nggak perlu, Kak, jawabku cepat, berusaha tetap tenang."

    show k_z talking :
        smaller
        xalign 0.5
    "Yakin? Aku perhatiin dari tadi kamu kayak udah ngerti dasar-dasarnya. Pasti pernah coba sendiri, kan?"

    show k_z idle :
        smaller
        xalign 0.5
    "Aku terkejut dia bisa membaca sikapku. Dengan ragu, aku akhirnya menerima router yang disodorkannya."

    "Aku mulai menyambungkan kabel dengan hati-hati, mengikuti instruksi Kak Zahra. Begitu halaman konfigurasi router muncul, tanganku bergerak otomatis."
    
    show k_z happy :
        smaller
        xalign 0.5
    k_z "Wah, kamu tahu default username dan passwordnya!"
    
    show k_z point :
        smaller
        xalign 0.5
    k_z "Beneran cuma 'baca-baca sedikit' nih?"

    "Aku mengangkat bahu, mencoba tampak acuh tak acuh meski diam-diam merasa senang dengan pengakuannya."

    show k_z smiling :
        smaller
        xalign 0.5
    aku "Ini konfigurasi dasar untuk setting WiFi"

    show k_z idle :
        smaller
        xalign 0.5

    aku "Kalau mau lebih aman, enkripsinya pakai WPA2-PSK."

    show k_z happy :
        smaller
        xalign 0.5

    k_z "Ya ampun! Kamu udah kayak pro! Kenapa nggak bilang dari tadi?"
    
    show k_z idle :
        smaller
        xalign 0.5

    aku "Aku... dulunya suka teknologi"

    show k_z talk :
        smaller
        xalign 0.5

    k_z "Terus kenapa sekarang nggak suka lagi?"
    
    show k_z idle :
        smaller
        xalign 0.5

    aku "Karena teknologi mengingatkanku pada seseorang yang sudah pergi."

    show k_z sad:
        smaller
        xalign 0.5

    "Kak Zahra terdiam sejenak"

    k_z "Aku ngerti. Tapi teknologi itu cuma alat."

    show k_z smile:
        smaller
        xalign 0.5

    k_z "Yang menentukan bagaimana kita menggunakannya adalah kita sendiri."

    "Aku terdiam, mencerna kata-katanya."

    show k_z point:
        smaller
        xalign 0.5

    k_z "Hey, tahu nggak? Kita juga belajar Ethical Hacking! Seru banget!"

    "katanya berusaha mengubah suasana."

    show k_z idle:
        smaller
        xalign 0.5

    aku "Ethical hacking?"

    show k_z smiling:
        smaller
        xalign 0.5

    k_z "Iya! Kita belajar cara melindungi sistem dari serangan. Jadi, kalau kamu gabung TKJ"
    
    show k_z original with fade:
        smaller
        xalign 0.5

    k_z "kita bisa jadi superhero digital!"

    show k_z happy with fade:
        smaller
        xalign 0.5

    "Aku tak bisa menahan senyum tipis. Mungkin... ini bisa jadi awal yang baru bagiku."

    jump end

label end:
    "terima kasih"
