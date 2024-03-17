import subprocess
from tkinter import *
import os
from datetime import datetime

now = datetime.now()

currentTime = now.strftime("%H:%M:%S")


acc = str(input("Account to warn about: "))

print("[" + currentTime + "] Accounts scanning started for account " + acc +"...\nThe window will apear as soon as the account will be detected! (ctrl + C to stop)")


def poweroff():
    #return os.system("shutdown -h now")
    return os.system("systemctl poweroff")

def reboot():
    #return os.system("shutdown -r now")
    return os.system("systemctl reboot")

def suspend():
    return os.system("systemctl suspend")

#def logout():
#    return os.system("shutdown -l")




def warnWindow(): 
    master = Tk()
    master.configure(background="grey")
    master.title("Account Tracker")
    master.geometry("300x270")


    logged = Canvas(master, width=250, height=45, background="grey", highlightbackground="grey")

    logged.create_text(126, 25, text=acc + " LOGGED IN", fill="black", font=("Helvetica 15 bold"))
    logged.pack()

    actions = Canvas(master, width=250, height=20, background="grey", highlightbackground="grey")

    actions.create_text(126, 8, text="Actions:", fill="black", font=("Helvetica 10 "))
    actions.pack()

    Button(master, text="Suspend", command=suspend, width=10, background="grey", highlightbackground="black", font=("Helvetica 15")).pack()
    
    Button(master, text="Power Off", command=poweroff, width=10, background="grey", highlightbackground="black", font=("Helvetica 15")).pack()

    Button(master, text="Reboot", command=reboot, width=10, background="grey", highlightbackground="black", font=("Helvetica 15")).pack()

    Button(master, text="Ignore", command=master.destroy, width=10, background="grey", highlightbackground="black", font=("Helvetica 15")).pack()

    close = Canvas(master, width=250, height=50, background="grey", highlightbackground="grey")

    close.create_text(126, 32, text="You can close this\nwindow after performing\nan action", fill="black", font=("Helvetica 10 "))
    close.pack()

    #Button(master, text="Log out", command=logout).grid(row=3)

    
    mainloop()


def rootWindow(): 
    master = Tk()
    master.configure(background="grey")
    master.title("Account Tracker")
    master.geometry("300x270")


    logged = Canvas(master, width=250, height=45, background="grey", highlightbackground="grey")

    logged.create_text(126, 25, text="root LOGGED IN", fill="black", font=("Helvetica 15 bold"))
    logged.pack()

    actions = Canvas(master, width=250, height=20, background="grey", highlightbackground="grey")

    actions.create_text(126, 8, text="Actions:", fill="black", font=("Helvetica 10 "))
    actions.pack()

    Button(master, text="Suspend", command=suspend, width=10, background="grey", highlightbackground="black", font=("Helvetica 15")).pack()
    
    Button(master, text="Power Off", command=poweroff, width=10, background="grey", highlightbackground="black", font=("Helvetica 15")).pack()

    Button(master, text="Reboot", command=reboot, width=10, background="grey", highlightbackground="black", font=("Helvetica 15")).pack()

    Button(master, text="Ignore", command=master.destroy, width=10, background="grey", highlightbackground="black", font=("Helvetica 15")).pack()

    close = Canvas(master, width=250, height=50, background="grey", highlightbackground="grey")

    close.create_text(126, 32, text="You can close this\nwindow after performing\nan action", fill="black", font=("Helvetica 10 "))
    close.pack()

    #Button(master, text="Log out", command=logout).grid(row=3)

    
    mainloop()


while True:
    whoCheck = str(subprocess.check_output("who"))


    if acc in whoCheck:
        
        now = datetime.now()

        currentTime = now.strftime("%H:%M:%S")
        
        print("[" + currentTime + "] Account " + acc + " has beed detected!")
        warnWindow()
        break

    if "root" in whoCheck:
        
        now = datetime.now()

        currentTime = now.strftime("%H:%M:%S")
        
        print("[" + currentTime + "] Account root has beed detected!")
        rootWindow()
        break

#    stop = input()

#    if stop == "exit":
#        now = datetime.now()
#
#        currentTime = now.strftime("%H:%M:%S")
#        
#        print("[" + currentTime + "] Stopping...")
#        break

    

#Author: OlekAS13, 17.03.2024, 14:07
