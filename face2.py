from tkinter import *
import os

import pyperclip
import create_data
import face_recognize
creds = 'tempfile.txt' # This just sets the variable creds to 'tempfile.temp'
 
def Signup(): # This is the signup definition, 
    global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them
    global nameE
    global roots
    #global nameE
    roots = Tk() # This creates the window, just a blank one.
    roots.title('Signup') # This renames the title of said window to 'signup'
    intruction = Label(roots, text='Please Enter new Credidentials\n') # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=0, sticky=E) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)
 
    nameL = Label(roots, text='New Username: ') # This just does the same as above, instead with the text new username.
    pwordL = Label(roots, text='New Password: ') # ^^
    nameL.grid(row=1, column=0, sticky=W) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    pwordL.grid(row=2, column=0, sticky=W) # ^^
 
    nameE = Entry(roots) # This now puts a text box waiting for input.
    pwordE = Entry(roots, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    nameE.grid(row=1, column=1) # You know what this does now :D
    pwordE.grid(row=2, column=1) # ^^
 
    signupButton = Button(roots, text='Signup', command=FSSignup) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop() # This just makes the window keep open, we will destroy it soon
       
def FSSignup():
    with open(creds, 'a') as f: # Creates a document using the variable we made at the top.
        f.write(nameE.get()) # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
        f.write('\n') # Splits the line so both variables are on different lines.
        f.write(pwordE.get()) # Same as nameE just with pword var
        f.write('\n') # Splits the line so both variables are on different lines.
        f.close() # Closes the file
        create_data.main(nameE.get())
    roots.after(20000, lambda: roots.destroy())
    roots.destroy() # This will destroy the signup window. :)
    Login() # This will move us onto the login definition :D
 
def Login():
    global nameEL
    global pwordEL # More globals :D
    global rootA
 
    rootA = Tk() # This now makes a new window.
    rootA.title('Login') # This makes the window title 'login'
 
    intruction = Label(rootA, text='Please Login\n') # More labels to tell us what they do
    intruction.grid(sticky=E) # Blahdy Blah
 
    nameL = Label(rootA, text='Username: ') # More labels
    pwordL = Label(rootA, text='Password: ') # ^
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=W)
    rootA.after(20000, lambda: rootA.destroy())
    rootA.mainloop()
 
def CheckLogin():
  with open(creds) as f:
    i=0
    j=1
    data = f.readlines()
    face_recognize.main()
    text="0"
    text= pyperclip.paste()
    try:
     for k in data:
        # This takes the entire document we put the info into and puts it into the data variable
        uname = data[i].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[j].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
        i=i+2
        j=j+2
        if nameEL.get() == uname and pwordEL.get() == pword and text == "1" :
            count=1
        else :
            count=0
    except IndexError as error:
        print("")
    if count==1:
            r = Tk() # Opens new window
            r.title(':D')
            r.geometry('150x50') # Makes the window a certain size
            rlbl = Label(r, text='\n[+] Logged In') # "logged in" label
            rlbl.pack() # Pack is like .grid(), just different
            r.after(2000, lambda: r.destroy())
            #r.destroy() 
    else:
            r = Tk()
            r.title('D:')
            r.geometry('150x50')
            rlbl = Label(r, text='\n[!] Invalid Login')
            rlbl.pack()
            #r.mainloop()
            r.after(2000, lambda: r.destroy()) # Destroy the widget after 30 secondstime.sleep(2)
            #r.destroy()  
         # Checks to see if you entered the correct data.
 
def mainpage():
    global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them
    global nameE
    global roots
 
    roots = Tk() # This creates the window, just a blank one.
    roots.title('MAINPAGE') # This renames the title of said window to 'signup'
    intruction = Label(roots, text='press the button\n') # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=0, sticky=E) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)
 
    MyButton1 = Button(roots, text="Signup", width=10, command=Signup)
    MyButton1.grid(row=1, column=1)
    MyButton2 = Button(roots, text="login", width=10, command=Login)
    MyButton2.grid(row=1, column=2)
    roots.destroy
    roots.mainloop() # This just makes the window keep open, we will destroy it soon
   
mainpage()