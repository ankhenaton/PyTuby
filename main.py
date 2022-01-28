import os
from pytube import YouTube
from time import sleep
from pytube import Search
from pytube import Playlist


os.system("cls")

def tekci():

    try:
        link = input("İndirmek İstediğiniz Videonun Linkini Giriniz :  ")
        yt = YouTube(link)

        print("Başlık             : ",yt.title)
        print("Görüntülenme Sayısı: ",yt.views)
        print("Video Uzunluğu     : ",yt.length)
        print("Değerlendirme      : ",yt.rating)

        ys = yt.streams.get_highest_resolution()

        print("İndiriliyor...")
        ys.download()
        print("İndirme Tamamlandı!!")
        sleep(3)
        menu()
    except:
        print("Bir Hata Oluştu. Lütfen Tekrar Deneyiniz .!")
        sleep(3)
        os.system('cls')
        tekci()


def listeci():
    listeAl=input("İndirmek İstediğiniz Youtube Playlistinin Linkini Giriniz   :")
    kelimeAra=listeAl.find('list')
    if kelimeAra > 0:
        p=Playlist(listeAl)
        videoSay=len(p.videos)
        indirilenSay=0
        print(videoSay," Adet Video İndirilecektir !")
        for video in p.videos:
            video.streams.get_highest_resolution().download()
            videoSay-=1
            indirilenSay+=1
            print("İndirilen Video Sayısı ",indirilenSay," Kalan Video Sayısı ",videoSay)
            if videoSay==0:
                print("İndirmeler Tamamlandı !")
                nedir=input("Anamenu için (1) , Yeni Tek Video İndirme Görevi İçin (2) , Yeni PlayList İndirme Görevi İçin (3) , Kelime İle Arama Yapmak İçin (4) , Çıkış İçin (5) :")
                if nedir=="1":
                    menu()
                elif nedir=="2":
                    tekci()
                elif nedir=="3":
                    listeci()
                elif nedir=="4":
                    arama()
                elif nedir=="5":
                    exit()
                else:
                    print("Geçerli Bir Tercih Girmediniz Anamenu'ye Yönlendiriliyorsunuz !")
                    os.system('cls')
                    menu()
            
        
    elif kelimeAra<0:
        print("Geçerli Bir Youtube Playlist Linki Değil")
        kelimeAra1=listeAl.find('youtube')
        if kelimeAra1>0:
            print("Bu Linkin Tek Bir Video'ya Ait Olduğunu Düşünüyorum, Deneyelim !")
            try:
                link = listeAl
                yt = YouTube(link)

                print("Başlık             : ",yt.title)
                print("Görüntülenme Sayısı: ",yt.views)
                print("Video Uzunluğu     : ",yt.length)
                print("Değerlendirme      : ",yt.rating)

                ys = yt.streams.get_highest_resolution()

                print("Evet Bir Video Linki , İndiriliyor...")
                ys.download()
                print("İndirme Tamamlandı!!")
                sleep(3)
                menu()
            except:
                print("Hiç Olmadı be , Lütfen Tekrar Deneyiniz .!")
                sleep(3)
                os.system('cls')
                menu()

def arama():
    aranan=input("Youtube Üzerinde Aramak İstediğini Kelimeleri Yazınız :")
    def arama1():
        if len(aranan)>0:
            s = Search(aranan)
            for result in s.results:
                print(str(result).strip("<pytube.__main__.YouTube object: ").strip(">"))
            tercih=input("Çıktılardan Video İndirmek İstiyor musunuz? (E/H)").lower()
            if tercih=="h":
                tercih1=input("Ana Menu İçin (1) , Arama İçin (2) , Çıkış İçin (3) :")
                if tercih1=="1":
                    menu()
                elif tercih=="2":
                    arama()
                elif tercih=="3":
                    print("Byeee !!")
                    sleep(3)
                else:
                    print("Lütfen Geçerli Bir Tercih Giriniz !")
                    arama1()
            elif tercih=="e":
                yturl='www.youtube.com/watch?v='
                videoID=input('Lütfen Arama Sonuçlarında Yer Alan VideoID Karakter Kümesini Yazınız \n "=" Sonrası :')
                try:
                    link = yturl+videoID
                    yt = YouTube(link)

                    print("Başlık             : ",yt.title)
                    print("Görüntülenme Sayısı: ",yt.views)
                    print("Video Uzunluğu     : ",yt.length)
                    print("Değerlendirme      : ",yt.rating)

                    ys = yt.streams.get_highest_resolution()

                    print("İndiriliyor...")
                    ys.download()
                    print("İndirme Tamamlandı!!")
                    tercih1=input("Ana Menu İçin (1) , Arama İçin (2) , Çıkış İçin (3) :")
                    if tercih1=="1":
                        menu()
                    elif tercih=="2":
                        arama()
                    elif tercih=="3":
                        print("Byeee !!")
                        sleep(3)
                    else:
                        print("Lütfen Geçerli Bir Tercih Giriniz !")
                        menu()
                except:
                    print("Bir Hata Oluştu. Lütfen Tekrar Deneyiniz .!")
        else:
            print("Lütfen Aranacak Bir Kelime Giriniz !")
            arama()
    arama1()

def menu():
    print("|> Tek Bir Video Linki İçin     (T)  <| ")
    print("|> PlayList  Linki  İçin        (P)  <| ")
    print("|> Kelime İle Arama Yapmak İçin (A)  <| ")
    print("|> Çıkış İçin                   (C)  <| ") 
    secenek=input("Tercihinizi Giriniz :").lower()

    if secenek=="t":
        tekci()
    elif secenek=="p":
        listeci()
    elif secenek=="a":
        arama()
    elif secenek=="ç" or secenek=="c":
        print("Çıkış Yapıldı.")
        sleep(2)
    else:
        print("Lütfen Geçerli Bir Tercih Yapınız !")
        os.system("cls")
        menu()
menu()