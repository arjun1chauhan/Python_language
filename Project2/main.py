#creating a Rule Based Chatbot

import datetime
import time

name=input("Enter your Name: ")
presentHour=datetime.datetime.now().hour

if 5<= presentHour <=11:
    print("Good Morning,",name)
elif 11<= presentHour <=17:
    print("Good AfterNoon,",name)
elif 17<= presentHour <=20:
    print("Good Evening,",name)
else:
    print("Good Night,",name)




print("Namaste! Welcome to your Chatbot")
print("You can ask me basic Questions , type 'bye' to Exit")

#chatbot memory creation {dictionary of responses}

responses={
    "hello":"Hi!,Welcome, How can I Help You?",
    "how are you":"I am Fine,Thankyou",
    "who are you":"I am Smart AI Chatbot ",
    "motivate me":"keep going. Every bug of your project makes you a better developer",
    "happy":"Great to hear that"

}

def getResponseOfBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]

    return "i am unable to response , Still training"

#Take User input 
while True:
    userInput=input("please ask Your question: ")
    reply=getResponseOfBot(userInput)
    print("Bot Response: ",reply)
    if "bye" in userInput.lower():
        break