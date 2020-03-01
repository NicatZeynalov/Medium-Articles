import pyttsx3
import speech_recognition
import webbrowser
import requests
from bs4 import BeautifulSoup
import re
import httplib2
b="Alisa: "
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def main1():
    print(b,'Hello! My name is Alisa! How can I help you?')
    speak('Hello! My name is Alisa! How can I help you?')
def takeCommand():
    while True:
        query=input("Nijat: ")
        query=query.replace(' ','+')
        page2=requests.get("https://answers.search.yahoo.com/search;_ylt=AwrC1Ch4XUVeKGwAkzhPmolQ;_ylc=X1MDMTM1MTE5NTIxNQRfcgMyBGZyAwRncHJpZAMxMmF3YVpRQlRWU1ZnM2NXNE5QRVhBBG5fcnNsdAMwBG5fc3VnZwM0BG9yaWdpbgNhbnN3ZXJzLnNlYXJjaC55YWhvby5jb20EcG9zAzIEcHFzdHIDaG93JTIwY2FuJTIweW91JTIwcHJvdGVjdARwcXN0cmwDMTkEcXN0cmwDMzMEcXVlcnkDaG93JTIwY2FuJTIweW91JTIwcHJvdGVjdCUyMHdhdGVyBHRfc3RtcAMxNTgxNjA0MjQ5?p="+query+"&fr2=sa-gp-answers.search&guce_referrer=aHR0cHM6Ly9hbnN3ZXJzLnNlYXJjaC55YWhvby5jb20v&guce_referrer_sig=AQAAACHN4HuxaFHfJJH6Sl36bkFJRRn_BEdTtmdtgRqgZq5L36SsFqMIoPtOFssoaRlg1b_a3JZdK4X1UrcbTau9cYHNOH7O7m9dtqZnZfd6fe8PpjsuUZ6kuL5fIx8FaE4tpOKWEjAojxs_-bl6aA8v3oy2FNXJnxwbBTOaiRe3RteE&_guc_consent_skip=1581604327")            
        soup=BeautifulSoup(page2.content, "html.parser")           
        name = soup.find("div",{"class":"dd algo fst AnswrsV2"})
        try:
            for link in name.findAll('a', attrs={'href': re.compile("^https://answers.yahoo.com/question")}):
                a= (link.get('href'))                  
            page1=requests.get(a)              
            soup=BeautifulSoup(page1.content, "html.parser")               
            name = soup.find("div",{"class":"AnswersList__container___3vQdv"}).text.replace("\n","").strip()
            temp=name.rsplit("Favorite Answer",1)
            temp=temp[1].split('.')
            for i in temp[:2]:
                    print(b, i)
                    speak(i)            
        except Exception as e:
            print('I am sorry, I havent found anything related to your query')
main1()
takeCommand()