import fasttext
import pandas as pd
import re

num_dict={'k':1000,'K':1000,'l':100000,'L':100000,'m':1000000,'M':1000000,'b':1000000000,'B':1000000000,'t':1000000000000,'T':1000000000000}

standard = {'aap':'aap','bal':'balance','min':'minimum','asap':'as soon as possible','sa':'saving account','mab':"minimum average balance",\
          'amb':'minimum average balance','amt':'amount','m1':'money','vth draw':'withdraw','fr':'for','dba':'dbs','xtra':'extra',\
            'txns':'transaction','hallo':'hello','muje':'I','gv':'give','mane':'I','ac':'account','acount':'account','devit':'debit',\
            'avi':'now','kyu':'why','kb':'when','mene':'i','benefissor':'benificiary','benefissear':'benificiary','bnk':'bank',\
'tranjection':'transaction','sevng':'saving','seving':"saving",'aacound':'account','हज़ार':"thousand" ,"सौ":"Hundred" ,'pasa':"paise",\
            'तरीका':"process", "लाख":"lakh" ,'dont': "do not" ,"knw" : "know","acc":"account"}

def stand(msg):
    word_list=msg.split()
    m=msg
    for word in word_list:
        if word in standard.keys():

            m=msg.replace(word,standard[word])
    return m

def text2int (textnum, numwords={}):
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

def num2numeric(text):
    step1=[]
    for i in text.split():
        if ((type(i[-1])==type('akhil')) and (len(i)>=1) and (i[:-1].replace('.','').replace(',','').isdigit()) and (i[-1].isdigit()==False)):
            if(i[-1] in num_dict.keys()):
                step1.append(int(float(i[:-1])*num_dict[i[-1]]))
            else:
                step1.append(i)
        else:
            step1.append(i)
    step1=[str(i) for i in step1]
    step1_str=' '.join(step1)
    step2_str=text2int(step1_str)
    return step2_str

def lang_detect(text):
    model = fasttext.load_model('lid.176.ftz')
    multi_lang=model.predict('छत्तीस ఐదు akhil is not working for chatbot', k=2)  # top 2 matching languages
    languages=[i.split('__label__')[1] for i in multi_lang[0]]
    confidence=list(multi_lang[1])
    lang_confidence=list(zip(languages,confidence))
    return lang_confidence


    