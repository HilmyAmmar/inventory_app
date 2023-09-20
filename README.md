<h1>PBP Assignment</h1>
<h2>inventory_app </h2>

<p>Nama       : Hilmy Ammar Darmawan</p>
<p>Kelas      : PBP E</p>
<p>NPM        : 2206081736</p>
<p>Kode Asdos : AAA</p>
<p>Website: https://hilmy-inventory-app.adaptable.app</p>

<h2>Assignment 1</h2>
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

<h2>Assignment 2</h2>
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
  <li>GET HTML (http://localhost:8000/)
    <img src ="C:\Collage\Computer Science\Academics\Semester 3\Pemrograman Berbasis Platform\Tugas\Tugas 3\SS Postman\HTML.png">
  </li>
  <li>GET JSON (http://localhost:8000/JSON)
    <img src ="C:\Collage\Computer Science\Academics\Semester 3\Pemrograman Berbasis Platform\Tugas\Tugas 3\SS Postman\JSON.png">
  </li>
</ol>
