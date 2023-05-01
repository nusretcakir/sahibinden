import sqlite3
import requests
from bs4 import BeautifulSoup
import time
import telebot


url = "https://www.sahibinden.com/otomobil/benzin,benzin-lpg,dizel,hybrid/ikinci-el?pagingOffset=0&a5_max=2023&a116445=1263354&price_min=50000&a9620=143038&address_city=11&address_city=34&address_city=35&address_city=26&address_city=16&address_city=17&address_city=41&address_city=10&a4054=72907&pagingSize=50&a4_max=250000&sorting=yil-nu_desc&a5_min=1985&price_max=250000"


def create_db():

    # Veritabanına bağlan
    conn = sqlite3.connect('arac.db')
    c = conn.cursor()

    # Tabloyu oluştur
    c.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            marka TEXT,
            model TEXT,
            yil TEXT,
            km REAL,
            fiyat REAL,
            tarih TEXT
            konum TEXT,
            aciklama TEXT,
        );
    ''')
    conn.commit()
    conn.close()


def kontrol_ve_yaz(tarih, enlem, boylam, derinlik, buyukluk, yer):
    conn = sqlite3.connect('deprem.db')
    c = conn.cursor()
    
    # Veritabanında aynı tarih verisini kontrol etmek için sorgu yapılır
    c.execute("SELECT tarih FROM depremler WHERE tarih=?", (tarih,))
    result = c.fetchone()
    
    # Tarih verisi veritabanında yoksa, yeni bir satır eklenir
    if not result:
        c.execute("INSERT INTO depremler VALUES (?, ?, ?, ?, ?, ?)",
                  (tarih, enlem, boylam, derinlik, buyukluk, yer))
        conn.commit()
        print("Deprem verisi eklendi.",tarih,yer,buyukluk)

        if float(buyukluk)>=4.5: ################

            for i in range(2):

                #bana mesaj gönder
                send_message(f"""
                Yer: {yer}
                Büyüklük: {buyukluk}
                Derinlik: {derinlik}
                Tarih: {tarih}
                Enlem ve Boylam: {enlem} , {boylam}
                """)
                time.sleep(0.5)
    
    conn.close()