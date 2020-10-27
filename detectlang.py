

#ashus3868 gthub


## Run this command in terminal  before executing this program
## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also run this in seperate terminal
## rasa run actions

import requests
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

bot_message = ""
message = ""



while message != "Bye" :

    try:
        message=input('enter text\n')
        from langdetect import detect
        x =detect("mujhe loan चाहिए")
       # if x=='hi'
        r = requests.post('http://localhost:5002/webhooks/rest/webhook',
                         json={"message": transliterate(message, sanscript.DEVANAGARI, sanscript.ITRANS)})

        print("You said : {}".format(transliterate(message, sanscript.DEVANAGARI, sanscript.ITRANS)))
        print("Bot says, ", end=' ')
        for i in r.json():
            bot_message = i['text']
            print(f"{bot_message}")


    except:

        print("Sorry could not decpher")





