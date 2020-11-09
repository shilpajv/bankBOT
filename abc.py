texts = [
"Hi what are you doing, I want loan from bank worh 100k.",
"Hi mujhe loan chayihe please arrange kar sakhe ho kya?",
"హాయ్ నాకు loan కావాలి arrange చేయగలవా?",
"hi मुझे loan चाहिए प्लीज अर्रंगे कर दोना",
"ही मुझे लोन चाहिए प्लीज अर्रंगे कर दोना",
"ही मुझे लोन chahiye please kar dona bhai",
"నాకు రుణం మాత్రమే కావాలి దయచేసి చేయండి",
"personal loan ka process kaha se pata chalega",
"joint home loan apply hota maloom nai",
"y my card  is not activated",
"upi pin set karne mein diikkat aa rahi hai",
"hello sir kya aap meri madad karenge",
]
from modules_helping import *
for i in texts :
    print(i)
    print(lang_detect(i))
    print("-------")