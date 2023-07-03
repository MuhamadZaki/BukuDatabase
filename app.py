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
        "link":"",
        "title":"",
        "publish_Date":"",
        "info":{"pages":""},
        "description":""
    },
    {
         "link":"",
        "title":"",
        "publish_Date":"",
        "info":{"pages":""},
        "description":""
    },
    {
         "link":"",
        "title":"",
        "publish_Date":"",
        "info":{"pages":""},
        "description":""
    },
    {
         "link":"",
        "title":"",
        "publish_Date":"",
        "info":{"pages":""},
        "description":""
    },
]


@app.route("/")
def index():
    return books