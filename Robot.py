





import time
import sys
import random




Hindi_Dictionary ={
"Fast":"teez",
"Anger":"Gussa"

}

G_Knowledge =[ " 1 The Great Wall of China is the longest wall in the world."]

Science = ["1 The Majority of Earth's Oxygen Is Produced by Oceans"," 2 The Human Stomach Can Dissolve Razor Blades"," 3 Bananas are Radioactive"," 3 Animals Use Earth's Magnetic Field to Know Their Location"," 5 Helium Works Against Gravity","6 Humans May Harbour Genes from Other Species",]

Spirituality =[" 1 Spiritual knowledge is concerned with understanding the deeper aspects of human experience and the nature of reality beyond what is immediately perceptible."
" 2 It can be gained through personal experiences, introspection, and the study of spiritual practices and traditions"
" 3 Spiritual knowledge is not limited to any particular religion or belief system but encompasses a wide range of philosophical and metaphysical perspectives."
" 4 It often involves developing a greater sense of self-awareness, purpose, and interconnectedness with the world around us."
" 5The ultimate goal of spiritual knowledge is to lead a more fulfilling, compassionate, and meaningful life."
]

def speak(message):
    print("ChatBot:"+ message)

speak("Hey I am a chat bot Whats your name?\n")
name =input("User:")

speak("Hey " + name  +" How's your day going")
response = input("User:")
if "good" in response:
    speak("Oh i'm happy to hear that")
else:
    speak("Oh im sorry to hear that ")


speak("Do you want to ask a Question?")
response = input("User:") 

if("yes" in response ):
    print("ChatBot:Please Proceed") 
else:
    sys.exit("ok") 
  
q1 = input("User:")
if("Tell me general knowledge facts " in q1 ):
    for items in G_Knowledge:
        print(items)
elif("Tell me facts about science" in q1):
    print(Science)
    for items in Science:
        print(items)

speak("Do you want to ask  more Questions?")
response = input("User:")

if ("yes"  in response):
    print("ChatBot: Please Proceed")
else:
    sys.exit("ok")

q2 =input("User:")
if("Give me 5 points about spirituality" in q2):
    for items in Spirituality:
        print(items)
elif("Give me 2 words of hindi with english translation"):
    for items in Hindi_Dictionary:
        print(items)

response = input("User:")
if("I want to play stone paper scissor "in response):

    speak("ChatBot: Okay Your wish is my command")
    pass

def play_game(user_move):
    moves =["rock","paper","scissor"]
    Bot_moves=random.choice(moves)
    if user_move==Bot_moves:
        return f"Bot choses{Bot_moves},Its a tie"
    elif user_move=="rock" and Bot_moves=="paper" or user_move =="scissor" and Bot_moves=="paper" or user_move=="rock" and Bot_moves=="scissor":
        return f"Bot choses{Bot_moves},You win"
    else:
        return f"Bot choses{Bot_moves},You lose"
user_move =input("Please enter your moves:(rock,paper,scissor)\n")
result = play_game(user_move)
print(result)

speak("Do you want me to do something else dor you?")
response = input("User:")

if "yes" in response:
    print("ChatBot:Please proceed")
else:
    sys.exit("okay")

q3= input("User:")
if "Write a small poem for me":
    f =open("poem",'w')
    f.write('hello')
    print('poem')
    f.close()

