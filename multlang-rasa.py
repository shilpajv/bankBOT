

#ashus3868 gthub


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
        
        #string standardization
        message1=stand(message)
        user_values['normalized_message']=message1
        
        #num to numeric
        message2=num2numeric(message1)
        user_values['numbers_in_message']=message2
        
        r = requests.post('http://localhost:5005/webhooks/rest/webhook',json={"message": message2})

        print("You said : {}".format(message2))
        print("Bot says, ", end=' ')
        for i in r.json():
            bot_message = i['text']
            print(f"{bot_message}")
        
    except:
        print("didn't get you can you please try again?")

    finally:
        print(user_values)





