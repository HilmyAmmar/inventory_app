<h1>PBP Assignment</h1>
<h2>inventory_app </h2>

<p>Nama       : Hilmy Ammar Darmawan</p>
<p>Kelas      : PBP E</p>
<p>NPM        : 2206081736</p>
<p>Kode Asdos : AAA</p>

<h2>Assignment 2</h2>
<ol>
  
  <li>Untuk mengimplementasikan checklist assignment dengan lebih mudah, saya memanfaatkan aplikasi Google keep dengan memanfaatkan fitur 'Tick Boxes' yang tersedia di handphone pribadi. Selain itu, tentu saja saya tetap melihat tutorial 0 dan 1 agar pemahaman saya terus meningkat dan membantu mengimplentasikan checklist assignment </li>
  
  <li>Bagan <i>request client</i> ke web aplikasi berbasis Django beserta responnya</li>
  <img src="https://res.cloudinary.com/practicaldev/image/fetch/s--wZV9_uu3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/d85c2zuye6xw3odavxt0.png" >
  <p>urls.py berfungsi sebagai pengaturan rute atau URL dalam aplikasi yang telah dibuat. views.py berisi definisi tampilan atau fungsi yang akan dijalankan ketika URL tertentu dimasukkan oleh user melalui website. models.py berisi definisi struktur database yang akan digunakan oleh aplikasi. Terakhir, main.html berfungsi sebagai tampilan yang akan dihasilkan oleh tampilan python</p>
  
  <li><i>Virtual environment</i> merupakan sebuah tool yang membantu untuk memisahkan dependensi yang diperlukan oleh beberapa project yang berbeda dengan membuat <i>virtual environment</i> untuk project tertentu yang terisolasi dengan project yang lain. Meskipun begitu, penggunaan <i>virtual environment</i> bukanlah syarat untuk membuat aplikasi web dengan django. <i>Virtual environment</i> sangat berguna dalam suatu kasus dimana terdapat 2 projek yang memiliki versi python yang berbeda. Penggunaan <i>virtual environment</i> akan membuat dua <i>environments</i> yang berbeda dan mengisolasi masing-masing projectnya.</li>
  
  <li>
    <ul>
      <li>MVC(Model, View, Controller) merupakan sebuah konsep arsitektur dalam mebuat suatu aplikasi dengan memisahkan kode menjadi tiga bagian yang memiliki fungsinya masing-masing. Model bertanggung jawab untuk mengelola, mengatur, dan memanipulasi data yang disimpan dalam database. View berperan dalam menampilkan data dalam bentuk <i>Graphical User Interface</i> (GUI). Controller berfungsi sebagai penghubung dan pengatur agar model dan view dapat saling terhubung</li>  
      <li>Hampir sama dengan MVC, MVT(Model, View, Template) merupakan sebuah konsep arsitektur dalam membuat suatu aplikasi yang terdiri dari tiga komponen utama. Model bertanggung jawab dalam membantu mengelola dan mengatur data aplikasi. View merupakan komponen yang menangani logika presentasi dalam konsep MVT. Template berfungsi untuk mengatur tampilan aplikasi tersebut</li>
      <li>MVVM merupakan konsep arsitektur pembuatan aplikasi berbasis GUI yang berfokus pada memisahan antara kode untuk logika bisnis dan tampilan aplikasi. MVVM juga terbagi menjadi tiga komponen, yaitu Model, View, dan ViewModel. Model bertanggung jawab untuk merepresentasikan data yang akan digunakan pada logika bisnis. View berisi UI dari aplikasi untuk mengatur bagaimana informasi akan ditampilkan. ViewModel bertugas untuk berinteraksi dengan model di mana data yang ada akan diteruskan ke layer view</li>
    </ul>
  </li>
  
</ol>

<h2>Assignment 3</h2>
<ol>
  <li>
    Form POST mengirimkan data ke server tanpa menampilkannya dalam URL sehingga akan lebih aman, cocok untuk data yang sensitif dan data besar. Sementara itu, Form GET mengirim data melalui URL sehingga kurang aman untuk data yang sensitif
  </li>
  <li>
    HTML digunakan untuk menampilkan informasi di browser, bukan untuk melakukan pengiriman/pertukaran data. XML (Extensible Markup Language) menyimpan elemen-elemennya dengan cara yang terstruktur dan mudah dibaca oleh manusia dan mesin, akan tetapi kurang efisien. XML bertujuan untuk melakukan pertukaran data antar berbagai sistem dan platform secara lebih ekstensibel. JSON menyimpan elemennya secara efisien tapi tidak rapi untuk dilihat. JSON umumnya digunakan untuk pertukaran data dalam format yang lebih sederhana dan seringkali digunakan dalam aplikasi web untuk mengirim data antara server dan browser.  
  </li>
  <li>
    JSON adalah format pertukaran data yang sangat ringan dan mudah dibaca serta ditulis oleh manusia. Hal ini membuatnya mudah diterjemahkan dan dibuat oleh komputer. Selain itu, JSON juga memliki format data yang mudah diuraikan sehingga tidak memerlukan kode tambahan untuk penguraian. Hal ini sangat membantu pertukaran data dan hasil layanan website secara lebih cepat
  </li>
  <li>
    Untuk mengimplementasikan checklist assignment dengan lebih mudah, saya memanfaatkan aplikasi Google keep dengan memanfaatkan fitur 'Tick Boxes' yang tersedia di handphone pribadi. Selain itu, tentu saja saya tetap melihat tutorial 2 agar pemahaman saya terus meningkat dan membantu mengimplentasikan checklist assignment
  </li>
</ol>
<h3>Hasil akses URL pada postman</h3>
<ol>
  <li>GET HTML (http://localhost:8000/)</li>
  <img src = "https://cdn.discordapp.com/attachments/1015998793830895716/1153894934668120195/HTML.png">
  <li>GET JSON (http://localhost:8000/JSON)</li>
  <img src = "https://cdn.discordapp.com/attachments/1015998793830895716/1153894935209189506/JSON.png">
  <li>GET JSON by ID (http://localhost:8000/JSON/1)</li>
  <img src = "https://cdn.discordapp.com/attachments/1015998793830895716/1153894934923980850/JSON_by_ID.png">
  <li>GET XML (http://localhost:8000/XML)</li>
  <img src = "https://cdn.discordapp.com/attachments/1015998793830895716/1153894934328385536/XML.png">
  <li>GET XML by ID (http://localhost:8000/XML/1)</li>
  <img src = "https://cdn.discordapp.com/attachments/1015998793830895716/1153894934001233930/XML_by_ID.png">
</ol>

<h2>Assignment 4</h2>
<ol>
  <li>UserCreationForm merupakan form yang disediakan oleh Django dalam menangani pembuatan user dalam aplikasi website. Kelebihan dari UserCreationForm antara lain mudah digunakan karena langsung disediakan oleh django serta sudah menyertakan validasi dalam penentuan username dan password. Sedangkan, kekurangan dari UserCreationForm adalah developer harus bekerja ekstra untuk menulis view agar data formulir bisa diproses sehingga akan memperlama durasi pengerjaan.
  </li>
  <li>Autentikasi akan memverifikasi identitas user dengan menentukan apakah pengguna tersebut adalah orang yang menklaimnya. Setelah dilakukannya autentikas user, otorisasi akan digunakan selanjutnya untuk menentukan apa yang boleh dilakukan oleh user tersebut. Seperti, informasi dan fitur apa saja yang dapat diakses oleh user tersebut
  </li>
  <li>Cookie merupakan sebuah file yang disimpan oleh browser dan dapat digunakan oleh server website untuk mengidentifikasi user atau menyimpan informasi tertentu. Dalam konteks aplikasi website django, website akan melakukan holding state dengan session ID yang disimpan sebagai cookie pada komputer klien. Session ID dapat dipetakan ke dalam suatu struktur data pada server untuk menyimpan berbagai macam informasi yang mungkin dibutuhkan nantinya. 
  </li>
  <li>Data pada cookie umumnya tidak berbahaya dan tidak dapat menginfeksi situs website dengan malware. Namun, jika data cookie jatuh ke tangan yang salah, penyerang dapat mengakses sesi penelusuran, mencuri informasi pribadi, dan menyalahgunakan data cookie user. Ada beberapa resiko yang patut diwaspadai dalam penggunaan cookie, yaitu cookie fraud, Cross-Site Scripting (XSS), Session Fixation, Cross-Site Request Forgery Attack (CSRF), and Cookie Tossing Attack. Pengguna perlu untuk selalu waspada akan resiko - resiko yang ada agar data cookie tidak disalahgunakan oleh orang yang tidak bertanggung jawab. Salah satu cara yang bisa digunakan adalah dengan menggunakan anti-virus atau software" lain yang dapat memberi tahu bahwa website tertentu belum tentu aman dan sebaiknya dihindari.
  </li>
  <li>
    Dalam mengimplementasikan checklist di atas, ada sejumlah tahapan yang harus saya jalani. Berikut adalah tahapan - tahapannya:
  <h3>Membuat fungsi register, login, dan logout</h3>
  <p>Ketiganya kurang lebih memiliki tahapan yang sama. Setelah mengimport sejumlah library bawaan django, saya membuat ketiga fungsi yang berkaitan dengan register, login, dan logout ke views.py. Selanjutkan, saya membuat tiga file html dan menyalin template yang sudah disediakan dan disalin ke file tersebut. Terakhir, saya menambahkan path url ke dalam urlpatterns di urls.py setelah mengimpor fungsi yang telah dibuat sebelumnya. Ini memastikan agar saya bisa mengakses halaman - halaman tertentu dengan tombol yang juga telah ditentukan. </p>
    <h3>Merestriksi Akses Halaman Main</h3>
    <p>Tahapan ini perlu dilakukan agar halaman main hanya dapat diakses oleh pengguna yang telah login. Pada views.py, saya mengimport "login_required" dan menambahkan kode "@login_required(login_url='/login')" di atas fungsi show_main yang akan merestriksi halaman main</p>
    <h3>Menggunakan Data dari Cookies</h3>
    <p>Pada tahapan ini, saya menggunakan cookies dalam menambahkan data last login dan menampilkannya ke halaman main. Pertama, saya akan mengimport beberapa library pada views.py serta memodifikasi fungsi "login_user" dengan menambahkan cookie bernama "last_login" untuk melihat kapan terakhir kali user melakukan login. Selanjutnya, saya menambahkan "'last_login': request.COOKIES['last_login']" ke dalam variable context. Selain itu, saya juga memodifikasi fungsi "logout_user" untuk menghapus cookie "last_login" disaat user melakukan logout. Tidak lupa, saya juga mengedit file main.html agar data last login dapat ditampilkan pada browser. Setelah selesai, saya membuat akun terlebih dahulu agar bisa melanjutkan tahapan.</p>
    <h3>Menghubungkan Model Product dengan User</h3>
    <p>Pada tahapan ini, saya menghubungkan setiap produk yang ditambahkan dengan pengguna yang menambahkannya. Hal ini membuat pengguna hanya bisa melihat produk - produk yang telah ditambahkan sendiri. Pada models.py, saya mengimpor "user" dan menambahkan kode "user = models.ForeignKey(User, on_delete=models.CASCADE)" yang bergunakan untuk menghubungkan satu user dengan produk yang telah ditambahkannya melalui sebuah relationship. Selanjutnya, saya memodifikasi fungsi "create_product" pada views.py untuk menandakan bahwa objek product dimiliki oleh user yang sedang login. Lalu, saya mengubahkan salah satu kode pada fungsi "show_main" menjadi "products = Product.objects.filter(user=request.user)" sehingga hanya menampilkan objek product yang terasosiasikan dengan pengguna yang sedang login serta menambahkan "request.user.username" agar username pengguna yang login ditampilkan. Setelah semuanya disimpan, saya melakukan migrasi model dengan "python manage.py makemigrations" melalui command line untuk meng-update models py dan mengaplikasikan migrasi tersebut dengan "python manage.py migrate" </p>
  </li>
</ol>

<h2>Assignment 5</h2>
<ol>
  <li>(1) Universal Selector berarti memilih semua elemen yang ada pada suatu halaman HTML.(2) Element type selector melakukan styling pada elemen tertentu saja. (3) ID selector menggunakan atribut id pada HTML untuk memilih elemen tertentu. (4) Class Selector digunakan untuk memilih elemen HTML dengan class atribut tertentu. (5) Grouping Selector memilih sejumlah elemen HTML untuk diberikan style yang dipisahkan dengan tanda koma
  </li>
  <li>(title) membuat judul dari sebuah halaman. (h1) to (h6) membuat heading. (p) membuat paragraf. (br) membuat break line. (b) membuat huruf bercetak tebal. (!--..--) membuat komentar. (!DOCTYPE) menentukan tipe dokumen. (sub) membuat teks subskrip seperti penulisan zat kimia. (sup) membuat teks superscripted seperti dalam penulisan akar kuadrat. (img) membuat gambar. (input) membuat sebuah kontrol input. (button) membuat sebuah tombol yang dapat di-klik. etc...
  </li>
  <li>
    Padding merupakan jarak antara konten elemen dengan bordernya. Sementara itu, margin merupakan jarak antara border elemen dengan elemen di sekitarnya. 
  </li>
  <li>
    Tailwind membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya. Sementara itu, bootstrap menggunakan gaya dan komponen yang telah didefinisikan, yang memiliki tampilan yang sudah jadi dan dapat digunakan secara langsung. Lalu, tailwind CSS memberikan fleksibilitas dan adaptabilitas tinggi terhadap proyek. Sementara itu, bootstrap sering kali menghasilkan tampilan yang lebih konsisten di seluruh proyek karena menggunakan kompomen yang telah didefinisikan. 
  </li>
</ol>
