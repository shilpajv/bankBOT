
from langdetect import detect

standard = {'aap':'aap','bal':'balance','min':'minimum','asap':'as soon as possible','sa':'saving account','mab':"minimum average balance",\
          'amb':'minimum average balance','amt':'amount','m1':'money','vth draw':'withdraw','fr':'for','dba':'dbs','xtra':'extra',\
            'txns':'transaction','hallo':'hello','muje':'I','gv':'give','mane':'I','ac':'account','acount':'account','devit':'debit',\
            'avi':'now','kyu':'why','kb':'when','mene':'i','benefissor':'benificiary','benefissear':'benificiary','bnk':'bank',\
'tranjection':'transaction','sevng':'saving','seving':"saving",'aacound':'account','हज़ार':"thousand" ,"सौ":"Hundred" ,'pasa':"paise",\
            'तरीका':"process", "लाख":"lakh" ,'dont': "do not" ,"knw" : "know"}

def stand(msg):
    word_list=msg.split()
    m=msg
    for word in word_list:
        if word in standard.keys():

            m=msg.replace(word,standard[word])
    return m

t=input('enter message')
res = stand(t)
print(res)
x = detect(res)
print('Language detected : ',x)
