
from modules_helping import *
#ashus3868 gthub
import warnings
warnings.simplefilter("ignore")

## Run this command in terminal  before executing this program
## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also run this in seperate terminal
## rasa run actions

import requests


bot_message = ""
message = ""



while message.lower() != "bye" :

    try:
        user_values=dict()
        
        #input from user
        message=input('enter text\n')
        
        #language detection
        lang=lang_detect(message)
        
        user_values['language']=lang
        lang = 'en' if lang not in ['hi','en','te'] else lang
        #NER
            #NUmber
        user_values['account_number'] = re.findall(r'[0-9]{11,16}',message)
        #print(user_values['account_number'][1])
        #print('-----------')
        #for i,phonenumber in enumerate(user_values['account_number'][1]): 
         #   if len(phonenumber) > 10 & len(phonenumber) <= 16:
          #      print('456')
           #     pass
            #else :
             #   print('123')
              #  del user_values['account_number'][1][i]
               # del user_values['account_number'][0][i]
        #if 10 < len(user_values['account_number'][1][0]) <= 16:
        #    pass
        #else:
        #bye
        #     user_values['account_number'] = None
            #Currency
        user_values['currency'] = get_currency(message,lang)
            #Phone
        user_values['phone_number'] = get_phone(message,lang)
        for i,phonenumber in enumerate(user_values['phone_number'][1]): 
            if len(phonenumber) ==10:
                pass
            else :
                del user_values['phone_number'][1][i]
                del user_values['phone_number'][0][i]

            #Range
        user_values['currency_range'] = get_num_range(message,lang)
            #Date
        user_values['date'] = get_date(message,lang)
            #Time
        user_values['time'] = get_time(message,lang)

        #string standardization
        message1=stand(message)
        user_values['normalized_message']=message1
        
        #num to numeric
        message2=num2numeric(message1)
        user_values['numbers_in_message']=message2
        
        r = requests.post('http://localhost:5005/webhooks/rest/webhook',json={"message": message2})
        print('----------------------------------')
        print("You said : {}".format(message2))
        print('\n')
        print("Bot says, ", end=' ')
        for i in r.json():
            bot_message = i['text']
            print(f"{bot_message}")
        
    except Exception as e:
        print("didn't get you can you please try again?")
        print(e)

    finally:
        for sub in user_values: 
            print(sub , ':' , user_values[sub])
            
            
        





