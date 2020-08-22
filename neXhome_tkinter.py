import tkinter
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import os


def resize1_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo

image = Image.open('paint2.png')
main_screen = Tk()
main_screen.title("Designed by Shubhi Manral")
main_screen.geometry('1000x500')
#defining func for background image
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = tkinter.Label(main_screen, image = photo)
label.bind('<Configure>', resize1_image)#calling func: resize_image
label.pack(fill=BOTH, expand = YES)

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w") # open file "w".
    file.write(username_info + "\n") # write username in file "w" and move cursor to next line "\n".
    file.write(password_info)        # write password in file "w".
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()

# on and off functions
def on1(event):
    Label(bed_room_screen, text="ON", font=("Helvetica", 10), bg="yellow").place(relx=0.53, rely=0.259,height=40, width=45)
def off1(event):
    Label(bed_room_screen, text="OFF", font=("Helvetica", 10), bg="white").place(relx=0.53, rely=0.259, height=40,width=45)
def on2(event):
    Label(bed_room_screen, text="ON", font=("Helvetica", 10), bg="yellow").place(relx=0.53, rely=0.409,height=40, width=45)
def off2(event):
    Label(bed_room_screen, text="OFF", font=("Helvetica", 10), bg="white").place(relx=0.53, rely=0.409, height=40,width=45)
def on3(event):
    Label(bed_room_screen, text="ON", font=("Helvetica", 10), bg="yellow").place(relx=0.53, rely=0.565,height=40, width=45)
def off3(event):
    Label(bed_room_screen, text="OFF", font=("Helvetica", 10), bg="white").place(relx=0.53, rely=0.565, height=40,width=45)
def on4(event):
    Label(bed_room_screen, text="ON", font=("Helvetica", 10), bg="yellow").place(relx=0.53, rely=0.715,height=40, width=45)
def off4(event):
    Label(bed_room_screen, text="OFF", font=("Helvetica", 10), bg="white").place(relx=0.53, rely=0.715, height=40,width=45)
def on5(event):
    Label(bed_room_screen, text="ON", font=("Helvetica", 10), bg="yellow").place(relx=0.53, rely=0.865,height=40, width=45)
def off5(event):
    Label(bed_room_screen, text="OFF", font=("Helvetica", 10), bg="white").place(relx=0.53, rely=0.865, height=40,width=45)
def on6(event):
    Label(living_room_screen, text="ON", font=("Helvetica", 10), bg="yellow").place(relx=0.385, rely=0.35,height=40, width=45) #on6
def off6(event):
    Label(living_room_screen, text="OFF", font=("Helvetica", 10), bg="white").place(relx=0.385, rely=0.35, height=40,width=45) #off6
def on7(event):
    Label(living_room_screen, text="ON", font=("Helvetica", 10), bg="yellow").place(relx=0.385, rely=0.47,height=40, width=45) #on7
def off7(event):
    Label(living_room_screen, text="OFF", font=("Helvetica", 10), bg="white").place(relx=0.385, rely=0.47, height=40,width=45) #off7
def on8(event):
    Label(living_room_screen, text="ON", font=("Helvetica", 10), bg="yellow").place(relx=0.385, rely=0.57,height=40, width=45) #on8
def off8(event):
    Label(living_room_screen, text="OFF", font=("Helvetica", 10), bg="white").place(relx=0.385, rely=0.57, height=40,width=45) #off8
def on9(event):
    Label(living_room_screen, text="ON", font=("Helvetica", 10), bg="yellow").place(relx=0.385, rely=0.68,height=40, width=45) #on9
def off9(event):
    Label(living_room_screen, text="OFF", font=("Helvetica", 10), bg="white").place(relx=0.385, rely=0.68, height=40,width=45) #off9
def on10(event):
    Label(living_room_screen, text="ON", font=("Helvetica", 10), bg="yellow").place(relx=0.385, rely=0.8,height=40, width=45) #on10
def off10(event):
    Label(living_room_screen, text="OFF", font=("Helvetica", 10), bg="white").place(relx=0.385, rely=0.8, height=40,width=45) #off10
def on11(event):
    Label(kitchen_room_screen, text="ON", font=("Helvetica", 10), bg="yellow").place(relx=0.31, rely=0.35,height=40, width=45) #on11
def off11(event):
    Label(kitchen_room_screen, text="OFF", font=("Helvetica", 10), bg="white").place(relx=0.31, rely=0.35, height=40,width=45) #off11
def on12(event):
    Label(kitchen_room_screen, text="ON", font=("Helvetica", 10), bg="yellow").place(relx=0.31, rely=0.5,height=40, width=45) #on12
def off12(event):
    Label(kitchen_room_screen, text="OFF", font=("Helvetica", 10), bg="white").place(relx=0.31, rely=0.5, height=40,width=45) #off12
def on13(event):
    Label(kitchen_room_screen, text="ON",font=("Helvetica", 10),bg="yellow").place(relx=0.31, rely=0.68,height=40, width=45) #on13
def off13(event):
    Label(kitchen_room_screen, text="OFF",font=("Helvetica", 10),bg="white").place(relx=0.31, rely=0.68, height=40,width=45) #off13
def on14(event):
    Label(kitchen_room_screen, text="ON",font=("Helvetica", 10),bg="yellow").place(relx=0.31, rely=0.83,height=40, width=45) #on14
def off14(event):
    Label(kitchen_room_screen, text="OFF",font=("Helvetica", 10),bg="white").place(relx=0.31, rely=0.83, height=40,width=45) #off14
def on15(event):
    Label(washroom_screen, text="ON", font=("Helvetica", 10), bg="yellow").place(relx=0.645, rely=0.4,height=40, width=45) #on15
def off15(event):
    Label(washroom_screen, text="OFF", font=("Helvetica", 10), bg="white").place(relx=0.645, rely=0.4, height=40,width=45) #off15
def on16(event):
    Label(washroom_screen, text="ON",font=("Helvetica", 10),bg="yellow").place(relx=0.645, rely=0.58,height=40, width=45) #on16
def off16(event):
    Label(washroom_screen, text="OFF",font=("Helvetica", 10),bg="white").place(relx=0.645, rely=0.58, height=40,width=45) #off16
def on17(event):
    Label(washroom_screen, text="ON",font=("Helvetica", 10),bg="yellow").place(relx=0.645, rely=0.78,height=40, width=45) #on17
def off17(event):
    Label(washroom_screen, text="OFF",font=("Helvetica", 10),bg="white").place(relx=0.645, rely=0.78, height=40,width=45) #off17
def on18(event):
    Label(terrace_screen, text="ON",font=("Helvetica", 10),bg="yellow").place(relx=0.485, rely=0.65,height=40, width=45) #on18
def off18(event):
    Label(terrace_screen, text="OFF",font=("Helvetica", 10),bg="white").place(relx=0.485, rely=0.65, height=40,width=45) #off18
def on19(event):
    Label(terrace_screen, text="ON",font=("Helvetica", 10),bg="yellow").place(relx=0.485, rely=0.82,height=40, width=45) #on19
def off19(event):
    Label(terrace_screen, text="OFF",font=("Helvetica", 10),bg="white").place(relx=0.485, rely=0.82, height=40,width=45) #off19
def on20(event):
    Label(garden_screen, text="ON",font=("Helvetica", 10),bg="yellow").place(relx=0.25, rely=0.47,height=40, width=45) #on20
def off20(event):
    Label(garden_screen, text="OFF",font=("Helvetica", 10),bg="white").place(relx=0.25, rely=0.47, height=40,width=45) #off20
def on21(event):
    Label(garden_screen, text="ON",font=("Helvetica", 10),bg="yellow").place(relx=0.25, rely=0.69,height=40, width=45) #on21
def off21(event):
    Label(garden_screen, text="OFF",font=("Helvetica", 10),bg="white").place(relx=0.25, rely=0.69, height=40,width=45) #off21
def on22(event):
    Label(garage_screen, text="ON",font=("Helvetica", 10),bg="yellow").place(relx=0.41, rely=0.58,height=40, width=45) #on22
def off22(event):
    Label(garage_screen, text="OFF",font=("Helvetica", 10),bg="white").place(relx=0.41, rely=0.58, height=40,width=45) #off22
def on23(event):
    Label(garage_screen, text="ON",font=("Helvetica", 10),bg="yellow").place(relx=0.41, rely=0.7,height=40, width=45) #on23
def off23(event):
    Label(garage_screen, text="OFF",font=("Helvetica", 10),bg="white").place(relx=0.41, rely=0.7, height=40,width=45) #off23
def on24(event):
    Label(garage_screen, text="ON",font=("Helvetica", 10),bg="yellow").place(relx=0.41, rely=0.82,height=40, width=45) #on24
def off24(event):
    Label(garage_screen, text="OFF",font=("Helvetica", 10),bg="white").place(relx=0.41, rely=0.82, height=40,width=45) #off24
def exit():
    abc_screen.destroy()

def bed_room():
    global bed_room_screen
    bed_room_screen = Toplevel(abc_screen)
    bed_room_screen.geometry('1000x550')
    bed_room_screen.resizable(0,0)
    def resize2_image(event): #resizing background image
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
    image = Image.open('bedroom_neXhome++.png')  #setting background image
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(bed_room_screen, image=photo)
    label.bind('<Configure>', resize2_image)  # calling func: resize_image
    label.pack(fill=BOTH, expand=YES)
    b1=Button(bed_room_screen, text="Lights", bg='steel blue', fg="white", font=(None, 12))
    b1.place(relx=0.44, rely=0.259, height=40, width=80)
    b1.bind('<Button-1>', on1)
    b1.bind('<Double-1>', off1)
    b2=Button(bed_room_screen, text="Fan", bg='steel blue', fg="white", font=(None, 12))
    b2.place(relx=0.44, rely=0.409,height=40, width=80)
    b2.bind('<Button-1>', on2)
    b2.bind('<Double-1>', off2)
    b3=Button(bed_room_screen, text="AC", bg='steel blue', fg="white", font=(None, 12))
    b3.place(relx=0.44, rely=0.565,height=40, width=80)
    b3.bind('<Button-1>', on3)
    b3.bind('<Double-1>', off3)
    b4=Button(bed_room_screen, text="Lamp", bg='steel blue', fg="white", font=(None, 12))
    b4.place(relx=0.44, rely=0.715,height=40, width=80)
    b4.bind('<Button-1>', on4)
    b4.bind('<Double-1>', off4)
    b5=Button(bed_room_screen, text="TV", bg='steel blue', fg="white", font=(None, 12))
    b5.place(relx=0.44, rely=0.865,height=40, width=80)
    b5.bind('<Button-1>', on5)
    b5.bind('<Double-1>', off5)

def living_room():
    global living_room_screen
    living_room_screen = Toplevel(abc_screen)
    living_room_screen.geometry('1000x550')
    living_room_screen.resizable(0,0)
    def resize2_image(event): #resizing background image
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
    image = Image.open('living_neXhome++.png')  #setting background image
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(living_room_screen, image=photo)
    label.bind('<Configure>', resize2_image)  # calling func: resize_image
    label.pack(fill=BOTH, expand=YES)
    b6=Button(living_room_screen, text="Lights", bg='steel blue', fg="white", font=(None, 12))
    b6.place(relx=0.3, rely=0.35, height=40, width=80)
    b6.bind('<Button-1>', on6)
    b6.bind('<Double-1>', off6)
    b7=Button(living_room_screen, text="Fan", bg='steel blue', fg="white", font=(None, 12))
    b7.place(relx=0.3, rely=0.47,height=40, width=80)
    b7.bind('<Button-1>', on7)
    b7.bind('<Double-1>', off7)
    b8=Button(living_room_screen, text="AC", bg='steel blue', fg="white", font=(None, 12))
    b8.place(relx=0.3, rely=0.57, height=40, width=80)
    b8.bind('<Button-1>', on8)
    b8.bind('<Double-1>', off8)
    b9=Button(living_room_screen, text="Lamp", bg='steel blue', fg="white", font=(None, 12))
    b9.place(relx=0.3, rely=0.68,height=40, width=80)
    b9.bind('<Button-1>', on9)
    b9.bind('<Double-1>', off9)
    b10=Button(living_room_screen, text="Speakers", bg='steel blue', fg="white", font=(None, 12))
    b10.place(relx=0.3, rely=0.8,height=40, width=80)
    b10.bind('<Button-1>', on10)
    b10.bind('<Double-1>', off10)

def kitchen_room():
    global kitchen_room_screen
    kitchen_room_screen = Toplevel(abc_screen)
    kitchen_room_screen.geometry('1000x550')
    kitchen_room_screen.resizable(0,0)
    def resize2_image(event): #resizing background image
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
    image = Image.open('kitchen_neXhome++.png')  #setting background image
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(kitchen_room_screen, image=photo)
    label.bind('<Configure>', resize2_image)  # calling func: resize_image
    label.pack(fill=BOTH, expand=YES)
    b11=Button(kitchen_room_screen, text="Lights", bg='steel blue', fg="white", font=(None, 12))
    b11.place(relx=0.2, rely=0.35, height=40, width=105)
    b11.bind('<Button-1>', on11)
    b11.bind('<Double-1>', off11)
    b12=Button(kitchen_room_screen, text="Chimney", bg='steel blue', fg="white", font=(None, 12))
    b12.place(relx=0.2, rely=0.5,height=40, width=105)
    b12.bind('<Button-1>', on12)
    b12.bind('<Double-1>', off12)
    b13=Button(kitchen_room_screen, text="Exhaust Fan", bg='steel blue', fg="white", font=(None, 12))
    b13.place(relx=0.2, rely=0.68,height=40, width=105)
    b13.bind('<Button-1>', on13)
    b13.bind('<Double-1>', off13)
    b14=Button(kitchen_room_screen, text="Refrigerator", bg='steel blue', fg="white", font=(None, 12))
    b14.place(relx=0.2, rely=0.83,height=40, width=105)
    b14.bind('<Button-1>', on14)
    b14.bind('<Double-1>', off14)

def washroom():
    global washroom_screen
    washroom_screen = Toplevel(abc_screen)
    washroom_screen.geometry('1000x550')
    washroom_screen.resizable(0,0)
    def resize2_image(event): #resizing background image
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
    image = Image.open('washroom_neXhome++.png')  #setting background image
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(washroom_screen, image=photo)
    label.bind('<Configure>', resize2_image)  # calling func: resize_image
    label.pack(fill=BOTH, expand=YES)
    b15=Button(washroom_screen, text="Lights", bg='steel blue', fg="white", font=(None, 12))
    b15.place(relx=0.53, rely=0.4, height=40, width=105)
    b15.bind('<Button-1>', on15)
    b15.bind('<Double-1>', off15)
    b16=Button(washroom_screen, text="Exhaust Fan", bg='steel blue', fg="white", font=(None, 12))
    b16.place(relx=0.53, rely=0.58,height=40, width=105)
    b16.bind('<Button-1>', on16)
    b16.bind('<Double-1>', off16)
    b17=Button(washroom_screen, text="Geyser", bg='steel blue', fg="white", font=(None, 12))
    b17.place(relx=0.53, rely=0.78,height=40,width=105)
    b17.bind('<Button-1>', on17)
    b17.bind('<Double-1>', off17)

def terrace():
    global terrace_screen
    terrace_screen = Toplevel(abc_screen)
    terrace_screen.geometry('1000x550')
    terrace_screen.resizable(0,0)
    def resize2_image(event): #resizing background image
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
    image = Image.open('terrace_neXhome++.png')  #setting background image
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(terrace_screen, image=photo)
    label.bind('<Configure>', resize2_image)  # calling func: resize_image
    label.pack(fill=BOTH, expand=YES)
    b18=Button(terrace_screen, text="Lights", bg='steel blue', fg="white", font=(None, 12))
    b18.place(relx=0.4, rely=0.65, height=40, width=80)
    b18.bind('<Button-1>', on18)
    b18.bind('<Double-1>', off18)
    b19=Button(terrace_screen, text="Fan", bg='steel blue', fg="white", font=(None, 12))
    b19.place(relx=0.4, rely=0.82,height=40, width=80)
    b19.bind('<Button-1>', on19)
    b19.bind('<Double-1>', off19)

def garden():
    global garden_screen
    garden_screen = Toplevel(abc_screen)
    garden_screen.geometry('1000x550')
    garden_screen.resizable(0,0)
    def resize2_image(event): #resizing background image
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
    image = Image.open('garden_neXhome++.png')  #setting background image
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(garden_screen, image=photo)
    label.bind('<Configure>', resize2_image)  # calling func: resize_image
    label.pack(fill=BOTH, expand=YES)
    b20=Button(garden_screen, text="Lights", bg='steel blue', fg="white", font=(None, 12))
    b20.place(relx=0.117, rely=0.47, height=40, width=130)
    b20.bind('<Button-1>', on20)
    b20.bind('<Double-1>', off20)
    b21=Button(garden_screen, text="Sprinkler System", bg='steel blue', fg="white", font=(None, 12))
    b21.place(relx=0.117, rely=0.69,height=40, width=130)
    b21.bind('<Button-1>', on21)
    b21.bind('<Double-1>', off21)

def garage():
    global garage_screen
    garage_screen = Toplevel(abc_screen)
    garage_screen.geometry('1000x550')
    garage_screen.resizable(0,0)
    def resize2_image(event): #resizing background image
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
    image = Image.open('garage_neXhome++.png')  #setting background image
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(garage_screen, image=photo)
    label.bind('<Configure>', resize2_image)  # calling func: resize_image
    label.pack(fill=BOTH, expand=YES)
    b22=Button(garage_screen, text="Lights", bg='steel blue', fg="white", font=(None, 12))
    b22.place(relx=0.32, rely=0.58, height=40, width=80)
    b22.bind('<Button-1>', on22)
    b22.bind('<Double-1>', off22)
    b23=Button(garage_screen, text="Fan", bg='steel blue', fg="white", font=(None, 12))
    b23.place(relx=0.32, rely=0.7,height=40, width=80)
    b23.bind('<Button-1>', on23)
    b23.bind('<Double-1>', off23)
    b24=Button(garage_screen, text="Door", bg='steel blue', fg="white", font=(None, 12))
    b24.place(relx=0.32, rely=0.82,height=40, width=80)
    b24.bind('<Button-1>', on24)
    b24.bind('<Double-1>', off24)

def abc():
    global abc_screen
    abc_screen = Toplevel(login_success_screen)
    abc_screen.geometry('1000x500')

    def resize2_image(event): #resizing background image - about_neX.png
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo

    image = Image.open('blurr2.png')  #setting background image as about_neX.png
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(abc_screen, image=photo)
    label.bind('<Configure>', resize2_image)  # calling func: resize_image
    label.pack(fill=BOTH, expand=YES)

    Button(abc_screen, text="Bed Room", bg='midnight blue', fg="white", font=(None, 12),command=bed_room).place(relx=0.05,rely=0.5,height=40,width=100)
    Button(abc_screen, text="Living Room", bg='midnight blue', fg="white", font=(None, 12),command=living_room).place(relx=0.05, rely=0.6,height=40, width=100)
    Button(abc_screen, text="Kitchen", bg='midnight blue', fg="white", font=(None, 12),command=kitchen_room).place(relx=0.05, rely=0.7,height=40, width=100)
    Button(abc_screen, text="Washroom", bg='midnight blue', fg="white", font=(None, 12),command=washroom).place(relx=0.05, rely=0.8,height=40, width=100)
    Button(abc_screen, text="Terrace", bg='midnight blue', fg="white", font=(None, 12),command=terrace).place(relx=0.87, rely=0.5,height=40, width=100)
    Button(abc_screen, text="Garden", bg='midnight blue', fg="white", font=(None, 12),command=garden).place(relx=0.87, rely=0.6,height=40, width=100)
    Button(abc_screen, text="Garage", bg='midnight blue', fg="white", font=(None, 12),command=garage).place(relx=0.87, rely=0.7,height=40, width=100)
    Button(abc_screen, text="Exit", bg='midnight blue', fg="white", font=(None, 12),command=exit).place(relx=0.87, rely=0.8,height=40, width=100)


def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=abc).pack()

# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def neX():
    global neX_screen
    neX_screen = Toplevel(main_screen)
    neX_screen.title("What is neXhome")
    neX_screen.geometry('1000x500')

    def resize2_image(event): #resizing background image - about_neX.png
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo

    image = Image.open('what_is_neXhome_2.png')  #setting background image as about_neX.png
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(neX_screen, image=photo)
    label.bind('<Configure>', resize2_image)  # calling func: resize_image
    label.pack(fill=BOTH, expand=YES)

def home_aut():
    global home_aut_screen
    home_aut_screen = Toplevel(main_screen)
    home_aut_screen.title("Home Automation")
    home_aut_screen.geometry('1000x500')

    def resize3_image(event): #resizing background image - about_neX.png
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo

    image = Image.open('All.png')  #setting background image as about_neX.png
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(home_aut_screen, image=photo)
    label.bind('<Configure>', resize3_image)  # calling func: resize_image
    label.pack(fill=BOTH, expand=YES)


b1= Button(main_screen, text="What is neXhome",font=(None,12),relief="flat",command=neX)
b1.place(relx=0.5, rely=0.03, height=30, width=135)
b2= Button(main_screen, text="Home Automation",font=(None,12),relief="flat",command=home_aut)
b2.place(relx=0.64, rely=0.03, height=30, width=135)
b3= Button(main_screen, text="Login",font=(None,12),relief="flat",command=login)
b3.place(relx=0.78, rely=0.03, height=30, width=80)
b4= Button(main_screen, text="Register",font=(None,12),relief="flat",command=register)
b4.place(relx=0.89, rely=0.03, height=30, width=80)


main_screen.mainloop()
