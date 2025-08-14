# Hava Durumu Sorgulama Uygulaması

Bu proje, kullanıcıdan şehir ismini alarak o şehre ait güncel hava durumu bilgilerini OpenWeatherMap API üzerinden çeken ve ekranda gösteren Python tabanlı bir komut satırı uygulamasıdır.

---

## İçindekiler

- [Genel Bakış](#genel-bakış)  
- [Özellikler](#özellikler)  
- [Kurulum](#kurulum)  
- [Kullanım](#kullanım)  
- [Dosya Yapısı](#dosya-yapısı)

---

## Genel Bakış

Bu Python uygulaması, bir şehir ismi girildikten sonra o şehrin sıcaklık, hissedilen sıcaklık, nem, rüzgar hızı ve hava durumu açıklamasını kullanıcıya sunar. Veriler, [OpenWeatherMap](https://openweathermap.org/) API'sinden JSON formatında çekilir ve sade bir formatla terminal ekranında gösterilir.

---

## Özellikler

- Şehir ismi girişinde Türkçe karakter düzeltme desteği (örneğin "İstanbul" → "Istanbul").
- Hatalı şehir adı veya bağlantı sorunlarında kullanıcı dostu uyarı mesajları.
- OpenWeatherMap API ile gerçek zamanlı hava durumu verisi.
- Kullanıcıdan yeni şehir sorgusu yapması istenerek tekrar kullanılabilir yapı.
- Hatalara karşı kapsamlı exception yönetimi (404, bağlantı hatası, zaman aşımı vb.)

---

## Kurulum

1. Python 3 yüklü olduğundan emin olun.
2. Projeyi klonlayın veya zip olarak indirin.
3. Kütüphaneleri yüklemek için terminalde:

```bash
pip install python-dotenv requests
```

4. Proje dizininde `.env` adlı bir dosya oluşturun ve içine aşağıdaki satırı ekleyin:

```
API_KEY=senin_openweathermap_api_anahtarın
```

[API anahtarını buradan alabilirsin](https://home.openweathermap.org/api_keys)

---

## Kullanım

Terminal veya komut satırında projenin bulunduğu dizinde çalıştır:

```bash
python main.py
```

- Program şehir adını soracaktır.
- Hava durumu bilgisi ekrana yazdırılacaktır.
- Ardından başka bir şehir sorgulamak isteyip istemediğiniz sorulacaktır.

---

## Dosya Yapısı

```
.
├── .env             # API anahtarınızı içeren gizli dosya
├── .gitignore       # Versiyon kontrolünde izlenmemesi gereken dosyalar
├── main.py          # Ana uygulama dosyası
├── README.md        # Bu dosya
├── requirements.txt # Gerekli kütüphanelerin listesi
```

---
## Lisans

Bu proje [MIT Lisansı](LICENSE) kapsamında açık kaynak olarak sunulmuştur.  
Dilediğiniz gibi kullanabilir, değiştirebilir ve paylaşabilirsiniz — ancak orijinal geliştiriciyi belirtmeniz gerekir.

---

## Proje Sahibi

**Berk DÖNMEZ**

GitHub: [github.com/berkdnmz](https://github.com/berkdnmz)  
LinkedIn: [linkedin.com/in/berkdnmz](https://linkedin.com/in/berkdnmz)  

Sorularınız veya katkı talepleriniz için benimle iletişime geçebilirsiniz.  

---

**İyi kodlamalar ve bol güneşli günler!**
