import tkinter
from tkinter import * 
import datetime 
import webbrowser
import os
from chatterbot import ChatBot

Ira_bot = ChatBot("Ira", storage_adapter="chatterbot.storage.SQLStorageAdapter",logic_adapters=[
                "chatterbot.logic.BestMatch"
            ],
            database_uri="sqlite:///db.sqlite3")


chromedir= 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' #for windows

def chat_response(msg):
    feed = msg
    if 'Hey Ira' in feed:
        return str("Hey master,I'm Ira, how are you?")

    elif 'open youtube' in feed:
            webbrowser.get(chromedir).open("youtube.com") # for windows
            webbrowser.open("youtube.com") # for every os
            return str('Opening Youtube') 
    elif 'Ira, tell me something about SDG goal 9?' in feed:
            return str("Master, Sustainable Development Goal 9, is about “Industry, innovation, and Infrastructure”. What do you want me to tell you about this?")
    elif 'Umm, tell me when was it proposed?' in feed:
            return str("Master, SDG goal 9 was established in 2015 by the United Nations, where 9 targets were selected for this particular goal.")
    elif '9 targets? What are those Ira?' in feed:
                return str("Master, The goals will be shows below: Develop sustainable, resilient and inclusive infrastructure. Promote inclusive and sustainable industrialisation Increase access to financial services and markets Upgrade all industries and infrastructure for sustainability Enhance research and upgrade industrial technologies Facilitate sustainable infrastructure development for developing countries Support domestic technology development and industrial diversification Universal access to information and communications technology Custodian agencies ")
    
    elif 'Wow, thats a nice goal. Is it being implemented in Bharat?' in feed:
                return str("Yes master, GOI has been enabling smart cities with internet connectivity to help both the people and industries")
    elif 'Network? How is it related to this SDG?' in feed:
                return str("Master, It is estimated that just 53.4% of the world's population are currently internet users, this means large population doesnt have the access to the biggest network.")
    elif 'What is the solution to this Ira?' in feed:
                return str("Master, industrialies and government, come together in this goal, to aachieve a profitable nusiness that is also cheap for the masses, example. Jio by Reliance under Make in India gave Free 4g connectivity for 1 year.")
    elif 'Is this goal about economy in a way?' in feed:
                return str("Yes, the aim is to unleash dynamic and competitive economic forces that generate employment and income through resilience of engineering and construction.")
    elif 'Tell me about it’s first target.' in feed:
                return str("Sure master, this target includes regional and trans-border infrastructure like roadways, trains and airways.")
    elif 'ira, has this been implemented in india?' in feed:
                return str("Master, india has the biggest railway system, but the airway is still being expanded, so we are developing.")
    elif 'hmm, how do we know this goal has been completed?' in feed:
                return str("By seeing the Proportion of rural population that lives within 2km of an all season road, and by the volume of passengers in all modes of transport.")
    elif 'whats target 2?' in feed:
                return str("Master, it is to promote inclusive and sustainable industrialisation")
    elif 'how is this in any way helpful to common man?' in feed:
                return str("Master, common man is the biggest consumer of industrial products. If industries thrive to success, then consumer’s life is also enriched.")
    elif 'you are smart ira.' in feed:
                return str("Thank you master.")
    elif 'How does an industry help the common man.' in feed:
                return str("Master By creating employment. Manufacturing is a major source of employment. 14% of the world workers are employed in manufacturing sector. By providing Consumer Expected products Uplifting economy ")
    elif 'what is target 3?' in feed:
                return str("Master, it is to increase small scale industries to make value chains.")
    elif 'okay ira, what is the progress?' in feed:
                return str("Capacity investment in solar slipped 3per cent to $131.1 billion in 2019, while that in wind climbed 6per cent to $138.2 billion – the first time that wind has outweighed solar in terms of dollars committed since 2010. Developing countries continued to outpace developed economies in renewables investment. In 2019, they committed $152.2 billion, compared to $130 billion for developed countries. ")
    elif 'dont you think industrial revolution will hurt our climate?' in feed:
                return str("Master, overproduction of technology and making it obsolete will anyway hurt the climate")
    elif 'questions' in feed:
                return str("answres")

    elif 'time' in feed:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        return str(f"Sir, the time is {strTime}")

    elif 'who created' in feed:
        return str("I am created by Abhijeet and Utkarsh")
        
    else:
        return str("Sorry, master, I dont have a clue about it.")

def send():
    """
    This method is for to get from user and displays to chatbox with bot response 
    """
    message = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if message != '':
        ChatBox.config(state=NORMAL)
        ChatBox.insert(END, "YOU: " + message + '\n\n')
        ChatBox.config(foreground="#1a1a1a", font=("Helvetica", 12 ))
        res = chat_response(message)
        ChatBox.insert(END, "Ira: " + res + '\n\n')
        ChatBox.config(state=DISABLED)
        ChatBox.yview(END)
Ira = Tk()
Ira.title("Ira Chatbot")
Ira.geometry("400x440")
Ira.iconbitmap('logo.ico')
Ira.resizable(width=True, height=True)
ChatBox = Text(Ira, bg="#ded1dc", bd=2, height="100", width="180",
               font="Arial",cursor="arrow")
ChatBox.config(state=NORMAL)
scrollbar = Scrollbar(Ira, command=ChatBox.yview, cursor="heart")
ChatBox['yscrollcommand'] = scrollbar.set
SendButton = Button(Ira, font=("Verdana",8,'bold'), text="Send", width="9",
                    height="4", bd=3, bg="#1a1a1a",
                    activebackground="#534293",fg='#ffffff',
                    command= lambda:send())
EntryBox = Text(Ira, bd=2, bg="#B9B4B1",width="25", height="2", font=("Arial",15))
scrollbar.place(x=385,y=6, height=386, width=8)
ChatBox.place(x=6,y=6, height=386, width=375)
EntryBox.place(x=6, y=401, height=30, width=280)
SendButton.place(x=300, y=400, height=30)
Ira.mainloop()