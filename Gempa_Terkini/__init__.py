import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal: 27 Jun 2025
    Waktu: 11:53:53 WIB
    Lokasi: Berada di darat 3 km Barat Daya Kolaka Timur
    Magnitudo: 3,6
    Kedalaman: 5 Km
    Koordinat: 4,12 LS - 121,88 BT
    :return:
    """

    content = requests.get('https://www.bmkg.go.id/')
    print(content.status_code)

    soup = BeautifulSoup(content.text, 'html.parser')
    result = soup.find('p', {'class':'mt-2 text-sm leading-[22px] font-medium text-gray-primary'})
    Waktu = result.text.split(', ')[1]
    Tanggal = result.text.split(', ')[0]

    Lokasi = soup.find('p', {'class':'mt-4 text-xl lg:text-2xl font-bold text-black-primary'})
    Lokasi = Lokasi.text

    result = soup.find('div', {'class': 'mt-5 flex flex-wrap lg:flex-nowrap gap-3'})
    result = result.findChildren('div')
    i= 0
    Magnitudo = None
    Kedalaman = None
    Koordinat = None
    LS = None
    BT = None


    for res in result:

        if i == 1:
            Magnitudo = res.text
        elif i == 3:
            Kedalaman = res.text
        elif i == 5:
            Koordinat = res.text

        i = i + 1




    hasil = dict()
    hasil['Tanggal'] = Tanggal  # '27 Jun 2025'
    hasil['Waktu'] = Waktu #'11:53:53 WIB'
    hasil['Lokasi'] = Lokasi #'Berada di darat 3 km Barat Daya Kolaka Timur'
    hasil['Magnitudo'] = Magnitudo  #'3.6'
    hasil['Kedalaman'] = Kedalaman #'5 Km'
    hasil['Koordinat'] = Koordinat #{'LS': 4.12, 'BT': 121.88}

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir dari BMKG')
    print(f"Tanggal {result['Tanggal']}")
    print(f"Waktu {result['Waktu']}")
    print(f"Lokasi {result['Lokasi']}")
    print(f"Magnitudo {result['Magnitudo']}")
    print(f"Kedalaman {result['Kedalaman']}")
    print(f"Koordinat: {result['Koordinat']}")


if __name__ == '__main__':
    print('Aplikasi Utama')
