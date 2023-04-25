import requests
import json
import time
import os
from playsound import playsound

while True:
    #Hazır api kullanılarak veri çekildi.
    url = "https://api.orhanaydogdu.com.tr/deprem/kandilli/live"
    response = requests.get(url)
    answer = json.loads(response.text)
    #print(json)

    #Veri düzenlendi.
    sayac = 0
    ses_sayaci = 0
    print("{:<30} {:<40} {:<15} {:<15}".format('Tarih', 'Bölge', 'Büyüklük', 'Derinlik')) # {:<} sayesinde yazı pozisyonları değiştirildi. 

    for i in answer["result"]:
        if sayac > 10:
            break
        elif (i["mag"]>3):
            print("{:<30} {:<40} {:<15} {:<15}".format(i["date"], i["title"], i["mag"], i["depth"]))
            sayac += 1
        elif ('İSTANBUL' in i["title"]):
            if ses_sayaci == 1:
                continue
            playsound('https://cdn.glitch.global/7694129e-5292-4bc4-8425-b6bf7800765d/Ses.mp3')
            ses_sayaci += 1
    time.sleep(30)
    os.system('cls')
    sayac = 0



