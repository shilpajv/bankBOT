

#ashus3868 gthub


## Run this command in terminal  before executing this program
## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also run this in seperate terminal
## rasa run actions

import requests


bot_message = ""
message = ""



while message != "Bye" :

    try:
        message=input('enter text\n')
        r = requests.post('http://localhost:5005/webhooks/rest/webhook',json={"message": message})

        print("You said : {}".format(message))
        print("Bot says, ", end=' ')
        for i in r.json():
            bot_message = i['text']
            print(f"{bot_message}")
    except:
        pass

    





