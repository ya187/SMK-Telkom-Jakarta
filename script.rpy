# Script untuk kelangsungan game visual novel SMK Telkom Jakarta

# Default settings
define config.default_text_cps = 7  # Kecepatan teks ketikan (30 karakter per detik)
# define config.start_label = "start"

# Resource
# Gambar Template
image bg blck = "images/blck.png"

# Tokoh dalam game
# Main Character
define aku = Character("[inputname]")
# Side Character
define kak_zahra = Character("Kak Zahra")
define kak_alya = Character("Kak Alya")
define kak_dika = Character("Kak Dika")
define tp = Character("Seorang Teman")

# Scene
scene bg titiktemu at Transform(xalign=0.5, yalign=0.5, zoom=2.0)
scene bg bus at Transform(xalign=0.5, yalign=0.5, zoom=2.0)
 
# Alur Game dimulai disini.
label start:
    # show bg titiktemu
    # show aku di tengah
    scene bg blck

    $ inputname = renpy.input("Namaku adalah?")
    

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

    "{color=#666666}Setibanya di SMK Telkom Jakarta, kami disambut oleh beberapa siswa SMK.{/color}"
    "{color=#666666}Mereka mengenakan seragam rapi dengan almamater merah marun.{/color}"

    # tampilkan kaka dika
    show kak_dika #with smile

    kak_dika "Selamat datang adik-adik!"

    show aku #with think

    "{color=#666666}Wow, semangat banget ya, menyedihkan.{/color}"
    "{color=#666666}Gumamku pelan, tapi mataku diam-diam mengamati dengan seksama.{/color}"

    show kak_dika #with normal

    kak_dika "Rombongannya dibagi menjadi beberapa kelompok kecil ya.."
    kak_dika "Nah, kamu mau mengenal jurusan apa dulu nih?"

    kak_dika "Teknik Transmisi, Teknik Jaringan Akses, Teknik Komputer Jaringan, "
    kak_dika "atau Rekayasa Perangkat Lunak?"

    show aku #with shock

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
    "Ucap Dika lagi."
    "Berarti sama Kak Dika ya. Perkenalkan, nama saya Dika Saputra."
    "Kakak dari jurusan Teknik Transmisi."
    "Kalian nggak usah canggung sama kakak ya, adik-adik."
    "Kita cuman beda setahun doang kok! Hehe.."

    "Teknik Transmisi ya? Bagus juga pilihanmu," 
    "Ucap Dika sambil memimpin kelompok kami."
    "Ini jurusan yang banyak prakteknya lho."

    "Aku hanya mengangguk singkat, berusaha menampilkan wajah tidak peduli."
    "Meski diam-diam penasaran."
    "Lebih baik begini—jaga jarak, jangan terlalu antusias."
    "Pengalaman mengajariku bahwa ketertarikan yang ditunjukkan bisa menjadi kelemahan yang dimanfaatkan."

    scene bg lab_telecom with fade

    "Di sini kita belajar tentang sistem telekomunikasi, mulai dari transmisi satelit, gelombang radio, hingga fiber optik."
    "Kak Dika menjelaskan sambil menunjukkan laboratorium dengan berbagai peralatan canggih."

    "Beberapa teman sekelasku terlihat terkagum-kagum, bertanya ini-itu dengan semangat."
    "Aku tetap menjaga jarak di belakang kelompok, mengamati semuanya dalam diam."
    "Sebuah perangkat di sudut ruangan menarik perhatianku—beberapa kabel fiber optik yang tersambung ke sebuah panel."

    "Itu apa?"
    "Tanyaku tanpa sadar, lalu segera menyesali keputusanku."
    "Seharusnya aku tetap diam saja."

    "Nah, itu sistem transmisi fiber optik kita. Keren kan?"
    "Kamu tertarik sama teknologi komunikasi?"

    "Biasa aja," 
    "Jawabku singkat, kembali ke sikap acuhku."
    "Cuma penasaran."

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

    "Oke!"
    "Ucap Kak Dika sambil tersenyum."
    "Kalau begitu, kamu bisa ikut kelompok Kak Alya. Dia ketua dari jurusan Teknik Jaringan Akses."
    
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

    "Oke!"  
    "Ucap Kak Dika sambil tersenyum."
    "Kalau begitu, kamu bisa ikut kelompok Kak Zahra. Dia ketua dari jurusan Teknik Komputer dan Jaringan."

    scene bg lab_network with fade

    "Di jurusan TKJ, kita belajar segala hal tentang jaringan komputer dan teknologi informasi."  
    "Kak Zahra berbicara dengan ceria, matanya berbinar penuh semangat."  
    "Di sini kita belajar tentang setting router, troubleshooting jaringan, hingga keamanan siber!"

    "Beberapa teman sekelompokku terlihat antusias, tapi aku masih ragu."  
    "Aku memang tertarik dengan teknologi, tapi ada sesuatu dalam diriku yang membuatku menahan diri."

    "Kak Zahra tiba-tiba menunjukku."  
    "Kamu kelihatan penasaran! Mau coba setting router?"

    "Eh... nggak perlu, Kak, jawabku cepat, berusaha tetap tenang."

    "Yakin? Aku perhatiin dari tadi kamu kayak udah ngerti dasar-dasarnya. Pasti pernah coba sendiri, kan?"

    "Aku terkejut dia bisa membaca sikapku. Dengan ragu, aku akhirnya menerima router yang disodorkannya."

    "Aku mulai menyambungkan kabel dengan hati-hati, mengikuti instruksi Kak Zahra. Begitu halaman konfigurasi router muncul, tanganku bergerak otomatis."

    "Wah, kamu tahu default username dan passwordnya! seru Kak Zahra kagum. Beneran cuma 'baca-baca sedikit' nih?"

    "Aku mengangkat bahu, mencoba tampak acuh tak acuh meski diam-diam merasa senang dengan pengakuannya."

    "Ini konfigurasi dasar untuk setting WiFi, lanjutku, jari-jariku mengubah beberapa parameter. Kalau mau lebih aman, enkripsinya pakai WPA2-PSK."

    "Ya ampun! Kamu udah kayak pro! Kenapa nggak bilang dari tadi? kata Kak Zahra sambil tertawa."

    "Aku... dulunya suka teknologi, kataku akhirnya."

    "Terus kenapa sekarang nggak suka lagi?"

    "Karena teknologi mengingatkanku pada seseorang yang sudah pergi."

    "Kak Zahra terdiam sejenak, lalu tersenyum hangat. Aku ngerti. Tapi teknologi itu cuma alat. Yang menentukan bagaimana kita menggunakannya adalah kita sendiri."

    "Aku terdiam, mencerna kata-katanya."

    "Hey, tahu nggak? Kita juga belajar ethical hacking! Seru banget! katanya berusaha mengubah suasana."

    "Ethical hacking?"

    "Iya! Kita belajar cara melindungi sistem dari serangan. Jadi, kalau kamu gabung TKJ, kita bisa jadi superhero digital! katanya sambil mengacungkan tinjunya ke udara."

    "Aku tak bisa menahan senyum tipis. Mungkin... ini bisa jadi awal yang baru bagiku."

    jump end

label end:
    "terima kasih"
