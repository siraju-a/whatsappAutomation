import time
import tkinter as tk
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def startautomating():
    victim=str(name.get())
    msg=str(message.get())
    num=msgCount.get()
    driver=webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
    driver.get("https://web.whatsapp.com/")

    time.sleep(timewhen.get())
    user=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    user.send_keys(victim)
    user.send_keys(Keys.ENTER)

    msg_box=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    for i in range(num):
        msg_box.send_keys(msg)
        msg_box.send_keys(Keys.ENTER)


#GUI
root=tk.Tk()
root.title("Automate Whatsapp")
root.geometry("500x500")
root.resizable(height=False,width=False)

headingLabel=Label(root,fg='cyan',bg='black',text="Wait for 15 - 30 sec to start..",font=('Helvetics',12,'bold'))
headingLabel.place(relx=.5,y=15,anchor='center')
root.configure(bg='black')
# victim name label
Label(root,bg='gold',text="Enter Name/Mobile Number").place(x=120,y=80)
name=StringVar()
nameBox=Entry(root,bg='white',textvariable=name).place(x=280,y=80)
#  Msg label
Label(root,bg='gold',text="Enter Message").place(x=120,y=150)
message=StringVar()
msgBox=Entry(root,bg='white',textvariable=message).place(x=280,y=150)

Label(root,bg='gold',text="No Of Message").place(x=120,y=220)
msgCount=IntVar()
countBox=Entry(root,bg='white',textvariable=msgCount).place(x=280,y=220)

Label(root,bg='gold',text="When to send").place(x=120,y=290)
timewhen=IntVar()
timer=Entry(root,bg='white',textvariable=timewhen).place(x=280,y=290)

tk.Button(root,bg='white',text="Automate",command=startautomating).place(relx=.5,y=400,anchor="center")
root.mainloop()