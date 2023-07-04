from flask import Flask
from flask import request

app = Flask(__name__)

books = [
    {
        "link":"https://www.gramedia.com/products/generator-termoelektrik-sebagai-sumber-energi-alternatif",
        "title":"Generator Termoelektrik Sebagai Sumber Energi Alternatif",
        "publish_Date":"13 Jun 2023",
        "info":{"pages":74},
        "description":"Krisis energi berasal dari minyak bumi yang tidak dapat diperbarui maka perlu mencari inovasi baru sebagai sumber energi alternatif."
    },
    {
        "link":"https://www.gramedia.com/products/panduan-resmi-bidik-cpns-2023",
        "title":"Panduan Resmi Bidik CPNS 2023",
        "publish_Date":"18 Jan 2023",
        "info":{"pages":496},
        "description":"Integritas Diri, Semangat Berprestasi, Orientasi pada Pelayanan, Kemampuan Beradaptasi, Pengendalian Diri, Kerja Tuntas dan Mandiri, Kemampuan Belajar Berkelanjutan, Teamwork dan Kerjasama, kepemimpinan, Skala Prioritas, Teknik Problem Solving, DII."
    },
    {
        "link":"https://www.gramedia.com/products/super-modul-psikotes-verbal-non-verbal",
        "title":"Super Modul Psikotes Verbal & Non-Verbal",
        "publish_Date":"19 Jun 2023",
        "info":{"pages":498},
        "description":"Super Modul Psikotes terbit sebagai solusi tepat bagi Anda yang ingin sukses dalam menghadapi berbagai jenis psikotes. "
    },
    {
        "link":"https://www.gramedia.com/products/panduan-resmi-tes-seleksi-masuk-tni-polri-20232024",
        "title":"Panduan Resmi Tes Seleksi Masuk TNI-POLRI 2023/2024",
        "publish_Date":"21 Mei 2023",
        "info":{"pages":529},
        "description":"Kepolisian Negara Republik Indonesia (POLRI) adalah Kepolisian nasional di Indonesia, yang bertanggung jawab langsung di bawah Presiden. "
    },
    {
        "link":"https://www.gramedia.com/products/grandmaster-top-skor-tpa-bappenas-dan-pascasarjana",
        "title":"Grand Master TOP Skor TPA BAPPENAS Dan Pascasarjana",
        "publish_Date":"25 Mei 2023",
        "info":{"pages":288},
        "description":"Tes Potensi Akademik (TPA) merupakan salah satu tes yang digunakan untuk mengukur kualitas Sumber Daya Manusia (SDM)."
    },
]

allBooks =[
    
    {
        "link":"https://www.gramedia.com/products/pedoman-resmi-seleksi-tes-cpns-cat-20232024",
        "title":"Pedoman Resmi Seleksi Tes Cpns Cat 2023/2024",
        "publish_Date":"10 Apr 2023",
        "info":{"pages":494},
        "description":"SELEKSI KOMPETENSI DASAR (SKD)"
    },
    {
        "link":"https://www.gramedia.com/products/panduan-resmi-cpns-pppk-20232024",
        "title":"Panduan Resmi Cpns & Pppk 2023/2024",
        "publish_Date":"10 Apr 2023",
        "info":{"pages":491},
        "description":"Berdasarkan Undang-Undang No. 5 Tahun 2014, Aparatur Sipil Negara (ASN) adalah profesi bagi pegawai negeri sipil dan pegawai pemerintah dengan perjanjian kerja yang bekerja pada instansi pemerintah."
    },
    {
        "link":"https://www.gramedia.com/products/diktat-pasti-tes-seleksi-asn-cpns-20232024",
        "title":"Diktat Pasti Tes Seleksi ASN CPNS 2023/2024",
        "publish_Date":"8 Apr 2023",
        "info":{"pages":424},
        "description":"Buku berjudul “Diktat Pasti Tes Seleksi ASN CPNS 2023-2024 berisi berbagai materi, informasi, latihan soal, kunci jawaban dan pembahasan mengenai persiapan menghadapi tes ASN CPNS."
    },
    {
        "link":"https://www.gramedia.com/products/update-bank-soal-full-pembahasan-psikotes-tpatbs-1",
        "title":"Update Bank Soal Full Pembahasan Psikotes",
        "publish_Date":"7 Apr 2023",
        "info":{"pages":385},
        "description":"Buku ini merupakan solusi cerdas bagi Anda yang ingin menguasai semua jenis psikotes."
    },
    {
        "link":"https://www.gramedia.com/products/skd-kedinasan-super-drilling-bank-soal-akurat-1",
        "title":"Super Drilling Bank Soal Akurat",
        "publish_Date":"29 Mar 2023",
        "info":{"pages":402},
        "description":"Sekolah kedinasan menjadi pilihan lulusan SMA karena dinilai lebih menjanjikan masa depan mereka dari pada harus menempuh pendidikan di sekolah-sekolah umum."
    },
]

allPages =[
    [
        {
            "link":"https://www.gramedia.com/products/supertrik-lolos-rekrutmen-50-bumn-terbaik",
            "title":"Supertrik Lolos Rekrutmen 50++ BUMN Terbaik",
            "publish_Date":"28 Mar 2023",
            "info":{"page":272},
            "description":"Pegawai BUMN merupakan salah satu profesi yang menjadi daya tarik tersendiri di kalangan masyarakat Indonesia."
        },
        {
            "link":"https://www.gramedia.com/products/panduan-lolos-tes-calon-asn",
            "title":"Panduan Lolos Tes Calon ASN",
            "publish_Date":"28 Mar 2023",
            "info":{"page":176},
            "description":"Bahwa dalam rangka usaha mencapai tujuan nasional yaitu mewujudkan masyarakat adil dan makmur."
        },
    ],
    [
        {
            "link":"https://www.gramedia.com/products/99-lolos-tes-masuk-kerja",
            "title":"Lolos Tes Masuk Kerja",
            "publish_Date":"17 Mar 2023",
            "info":{"page":416},
            "description":"Mencari pekerjaan adalah suatu hal yang gampang-gampang susah. Ada pencari kerja yang hanya mengirimkan satu surat lamaran, kemudian dipanggil untuk wawancara dan langsung diterima bekerja."
        },
        {
            "link":"https://www.gramedia.com/products/all-in-one-diktat-tni-polri",
            "title":"All In One Diktat Tni Polri",
            "publish_Date":"14 Mar 2023",
            "info":{"page":428},
            "description":"Namun, sesuai dengan Ketetapan MPR nomor VI/MPR/2000 maka TNI dan POLRI kembali dipisah."
        },
        {
            "link":"https://www.gramedia.com/products/99-lolos-tes-masuk-tni-polri-20232024",
            "title":"Lolos Tes Masuk TNI POLRI ",
            "publish_Date":"12 Mar 2023",
            "info":{"page":584},
            "description":"Dalam rangka memenuhi kebutuhan organisasi melalui penambahan kekuatan personel."
        },
    ]
    
]

pages = [
    {
        "link":"https://www.gramedia.com/products/princeton-review-act-prep-2023",
        "title":"Princeton Review ACT Prep, 2023",
        "publish_Date":"7 Mar 2023",
        "info":{"page":880},
        "description":"The Princeton Review Gets Results.Get all the prep you need to ace the ACT."
    },
    {
        "link":"https://www.gramedia.com/products/paket-paten-lolos-tes-cpns-cat-20232024",
        "title":"Paket Paten Lolos Tes Cpns Cat 2023/2024",
        "publish_Date":"3 Mar 2023",
        "info":{"page":226},
        "description":"Seputar tes CPNS, kisi-kisi terkini, dan alur seleksinya."
    },
    {
        "link":"https://www.gramedia.com/products/somasi-cpns-sscn-dikdin",
        "title":"Somasi Cpns Sscn Dikdin",
        "publish_Date":"28 Feb 2023",
        "info":{"page":384},
        "description":"Tidak ada pekerjaan paling enak selain menjadi PNS. Semua pasti setuju itu."
    },
    {
        "link":"https://www.gramedia.com/products/penyelenggaraan-pemeliharaan-rutin-jalan-provinsi-berbasis-partisipasi",
        "title":"Penyelenggaraan Pemeliharaan Rutin Jalan Provinsi Berbasis Partisipasi",
        "publish_Date":"21 Feb 2023",
        "info":{"page":256},
        "description":"Penyelenggaraan pemeliharaan jalan provinsi di Indonesia memerlukan strategi dan sistem manajemen khusus terkait dengan kondisi geologi dan lingkungan alam di wilayah terkait."
    },
    {
        "link":"https://www.gramedia.com/products/sukses-menghadapi-rekrutmen-tni",
        "title":"Sukses Menghadapi Rekrutmen TNI",
        "publish_Date":"20 Feb 2023",
        "info":{"page":402},
        "description":"Dalam rangka memenuhi kebutuhan organisasi melalui penambahan kekuatan personel, TNI perlu menyelenggarakan penerimaan terpadu di setiap tahun anggaran."
    }
]


@app.route("/")
def index():
    return books

@app.route("/allBooks/<int:allBook_id>")
def book(allBook_id):
    return allBooks[allBook_id]

@app.route("/allPages")
def paginitation():
    page = request.args.get("page", type= int)
    if page < 1:
        return allPages[page -1]
    
@app.route("/pages", methods =["GET"])
def get_pages():
    full_Pages = []
    for page in pages:
        if page ["info"]["page"] >= 700:
            full_Pages.append(page)
    return full_Pages