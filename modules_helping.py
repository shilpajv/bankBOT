import fasttext
import pandas as pd
import re
import math

num_dict={'k':1000,'K':1000,'l':100000,'L':100000,'m':1000000,'M':1000000,'b':1000000000,'B':1000000000,'t':1000000000000,'T':1000000000000}

standard = {'aap':'aap','bal':'balance','min':'minimum','asap':'as soon as possible','sa':'saving account','mab':"minimum average balance",\
          'amb':'minimum average balance','amt':'amount','m1':'money','vth draw':'withdraw','fr':'for','dba':'dbs','xtra':'extra',\
            'txns':'transaction','hallo':'hello','muje':'I','gv':'give','mane':'I','ac':'account','acount':'account','devit':'debit',\
            'avi':'now','kyu':'why','kb':'when','mene':'i','benefissor':'benificiary','benefissear':'benificiary','bnk':'bank',\
'tranjection':'transaction','sevng':'saving','seving':"saving",'aacound':'account','हज़ार':"thousand" ,"सौ":"Hundred" ,'pasa':"paise",\
            'तरीका':"process", "लाख":"lakh" ,'dont': "do not" ,"knw" : "know","acc":"account","pls":"please"}

def stand(msg):
    try:
        word_list=msg.split()
        m=msg
        for word in word_list:
            if word.lower() in standard.keys():
                m=msg.replace(word,standard[word.lower()])
        return m
    except:
        return msg
    
def text2int (textnum, numwords={}):
    try:
        if not numwords:
            units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
            ]

            tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

            scales = ["hundred", "thousand", "million", "billion", "trillion"]

            numwords["and"] = (1, 0)
            for idx, word in enumerate(units):  numwords[word] = (1, idx)
            for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
            for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

        ordinal_words = {'first':1, 'second':2, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}
        ordinal_endings = [('ieth', 'y'), ('th', '')]

        textnum = textnum.replace('-', ' ')

        current = result = 0
        curstring = ""
        onnumber = False
        for word in textnum.split():
            if word in ordinal_words:
                scale, increment = (1, ordinal_words[word])
                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
                onnumber = True
            else:
                for ending, replacement in ordinal_endings:
                    if word.endswith(ending):
                        word = "%s%s" % (word[:-len(ending)], replacement)

                if word not in numwords:
                    if onnumber:
                        curstring += repr(result + current) + " "
                    curstring += word + " "
                    result = current = 0
                    onnumber = False
                else:
                    scale, increment = numwords[word]

                    current = current * scale + increment
                    if scale > 100:
                        result += current
                        current = 0
                    onnumber = True

        if onnumber:
            curstring += repr(result + current)

        return curstring
    
    except:
        return textnum
    
def num2numeric(text):
    try:
        step1=[]
        for i in text.split():
            if ((type(i[-1]) is str) and (len(i)>=1) and (i[:-1].replace('.','').replace(',','').isdigit()) and (i[-1].isdigit()==False)):
                if(i[-1] in num_dict.keys()):
                    mul=float(i[:-1])
                    res=mul*num_dict[i[-1]]
                    step1.append(round(res))
                else:
                    step1.append(i)
            else:
                step1.append(i)
        step1=[str(i) for i in step1]
        step1_str=' '.join(step1)
        step2_str=text2int(step1_str)
        return step2_str
    except:
        return text

def lang_detect(text):
    try:
        lang_dict={'english':'en','hindi':'hi'}
        model_general = fasttext.load_model('lid.176.ftz')
        multi_lang_general=model_general.predict(text, k=1)  # top 1 matching languages
        languages_general=[i.split('__label__')[1] for i in multi_lang_general[0]]
        confidence_general=list(multi_lang_general[1])
        lang_confidence_general=list(zip(languages_general,confidence_general))
        
        if(lang_confidence_general[0][0] == 'en'):
            model_hinglish = fasttext.load_model('model1.bin')
            multi_lang_hinglish=model_hinglish.predict(text, k=1) # top 1 matching languages
            languages_hinglish=[i.split('__label__')[1] for i in multi_lang_hinglish[0]]
#             languages_hinglish=[lang_dict[i] for i in languages_hinglish]
            confidence_hinglish=list(multi_lang_hinglish[1])
            lang_confidence_hinglish=list(zip(languages_hinglish,confidence_hinglish))
#             print(lang_confidence_hinglish)
            return lang_confidence_hinglish[0][0]
        
        else:
#             print(lang_confidence_general)
            return lang_confidence_general[0][0]
    except:
        return 'en'
        
    
        
        
        
   
    
