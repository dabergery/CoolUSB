import os
import sys
import winreg as reg
import customtkinter
from pygame import mixer
a = 1
b = 1
c = 1
d = 1
figlet = """
   _____            _  _    _  _____ ____  
  / ____|          | || |  | |/ ____|  _ \ 
 | |     ___   ___ | || |  | | (___ | |_) |
 | |    / _ \ / _ \| || |  | |\___ \|  _ < 
 | |___| (_) | (_) | || |__| |____) | |_) |
  \_____\___/ \___/|_| \____/|_____/|____/   Tool coded by dabergery.
        
Bienvenue dans l'application CoolUSB.
vous pouvez personaliser votre environnement de travail en cliquant sur les boutons bleu la !"""
print(figlet)
def main():
    global a
    global b
    global c
    global d
    if getattr(sys, 'frozen', False):
        a = os.path.dirname(sys.executable)
        print("Executable")
    elif __file__:
        a = os.path.dirname(__file__)
    print("File")
    c = a + '\\wav\\game1.wav'
    d = a + '\\wav\\game2.wav'
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    app = customtkinter.CTk()
    app.geometry("500x500")
    app.title("CoolUSB - A Tool to custom your fucking Windows")
    mixer.init()
    def noel1():
        global a
        global c
        global b
        global d
        c = a + '\\wav\\noel1.wav'
        d = a + '\\wav\\noel2.wav'
        mixer.music.load(c)
        mixer.music.play()
    def noel2():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\noel3.wav'
        d = a + '\\wav\\noel4.wav'
        mixer.music.load(c)
        mixer.music.play()
    def noel3():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\noel5.wav'
        d = a + '\\wav\\noel6.wav'
        mixer.music.load(c)
        mixer.music.play()
    def game1():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\game1.wav'
        d = a + '\\wav\\game2.wav'
        mixer.music.load(c)
        mixer.music.play()
    def game2():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\game3.wav'
        d = a + '\\wav\\game4.wav'
        mixer.music.load(c)
        mixer.music.play()
    def game3():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\game5.wav'
        d = a + '\\wav\\game6.wav'
        mixer.music.load(c)
        mixer.music.play()
    def film1():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\film1.wav'
        d = a + '\\wav\\film2.wav'
        mixer.music.load(c)
        mixer.music.play()
    def film2():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\film3.wav'
        d = a + '\\wav\\film4.wav'
        mixer.music.load(c)
        mixer.music.play()
    def film3():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\film5.wav'
        d = a + '\\wav\\film6.wav'
        mixer.music.load(c)
        mixer.music.play()
    def anime1():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\anime1.wav'
        d = a + '\\wav\\anime2.wav'
        mixer.music.load(c)
        mixer.music.play()
    def anime2():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\anime3.wav'
        d = a + '\\wav\\anime4.wav'
        mixer.music.load(c)
        mixer.music.play()
    def anime3():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\anime5.wav'
        d = a + '\\wav\\anime6.wav'
        mixer.music.load(c)
        mixer.music.play()
    def animal1():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\animal1.wav'
        d = a + '\\wav\\animal2.wav'
        b = 'animal1'
        mixer.music.load(c)
        mixer.music.play()
        print(b)
    def animal2():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\animal3.wav'
        d = a + '\\wav\\animal4.wav'
        mixer.music.load(c)
        mixer.music.play()
    def animal3():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\animal5.wav'
        d = a + '\\wav\\animal6.wav'
        mixer.music.load(c)
        mixer.music.play()
    def pop1():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\pop1.wav'
        d = a + '\\wav\\pop2.wav'
        mixer.music.load(c)
        mixer.music.play()
    def pop2():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\pop3.wav'
        d = a + '\\wav\\pop4.wav'
        mixer.music.load(c)
        mixer.music.play()
    def pop3():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\pop5.wav'
        d = a + '\\wav\\pop6.wav'
        mixer.music.load(c)
        mixer.music.play()
    def default():
        global a
        global d
        global b
        global c
        c = a + '\\wav\\win1.wav'
        d = a + '\\wav\\win2.wav'
        mixer.music.load(c)
        mixer.music.play()
    def size01():
        app.geometry("300x200")
    def size02():
        app.geometry("400x600")
    def size03():
        app.geometry("700x300")

    buttonsize01 = customtkinter.CTkButton(master=app, text="Gemetrie 1", command=size01)
    buttonsize02 = customtkinter.CTkButton(master=app, text="Gemetrie 2", command=size02)
    buttonsize03 = customtkinter.CTkButton(master=app, text="Gemetrie 3", command=size03)
    button01 = customtkinter.CTkButton(master=app, text="Noel1", command=noel1)
    button02 = customtkinter.CTkButton(master=app, text="Noel2", command=noel2)
    button03 = customtkinter.CTkButton(master=app, text="Noel3", command=noel3)
    button04 = customtkinter.CTkButton(master=app, text="game1", command=game1)
    button05 = customtkinter.CTkButton(master=app, text="game2", command=game2)
    button06 = customtkinter.CTkButton(master=app, text="game3", command=game3)
    button07 = customtkinter.CTkButton(master=app, text="anime1", command=anime1)
    button08 = customtkinter.CTkButton(master=app, text="anime2", command=anime2)
    button09 = customtkinter.CTkButton(master=app, text="anime3", command=anime3)
    button10 = customtkinter.CTkButton(master=app, text="animal1", command=animal1)
    button11 = customtkinter.CTkButton(master=app, text="animal2", command=animal2)
    button12 = customtkinter.CTkButton(master=app, text="animal3", command=animal3)
    button13 = customtkinter.CTkButton(master=app, text="film1", command=film1)
    button14 = customtkinter.CTkButton(master=app, text="film2", command=film2)
    button15 = customtkinter.CTkButton(master=app, text="film3", command=film3)
    button16 = customtkinter.CTkButton(master=app, text="pop1", command=pop1)
    button17 = customtkinter.CTkButton(master=app, text="pop2", command=pop2)
    button18 = customtkinter.CTkButton(master=app, text="pop3", command=pop3)
    buttondefault = customtkinter.CTkButton(master=app, text="Return default Windows Sound", command=default)
    buttondefault.place(relx=.5, rely=.75, anchor=customtkinter.CENTER)

    checkbox01 = customtkinter.CTkCheckBox(app, text="est tu débile ?")
    checkbox01.grid(row=0, column=0, padx=250, pady=600, sticky="w")
    checkbox02 = customtkinter.CTkCheckBox(app, text="Espèce de grosse merde.")
    checkbox02.grid(row=0, column=0, padx=450, pady=700, sticky="w")
    buttonsize01.place(relx=.2, rely=.9, anchor=customtkinter.CENTER)
    buttonsize02.place(relx=.5, rely=.9, anchor=customtkinter.CENTER)
    buttonsize03.place(relx=.8, rely=.9, anchor=customtkinter.CENTER)
    button01.place(relx=.2, rely=.1, anchor=customtkinter.CENTER)
    button02.place(relx=.5, rely=.1, anchor=customtkinter.CENTER)
    button03.place(relx=.8, rely=.1, anchor=customtkinter.CENTER)
    button04.place(relx=.2, rely=.2, anchor=customtkinter.CENTER)
    button05.place(relx=.5, rely=.2, anchor=customtkinter.CENTER)
    button06.place(relx=.8, rely=.2, anchor=customtkinter.CENTER)
    button07.place(relx=.2, rely=.3, anchor=customtkinter.CENTER)
    button08.place(relx=.5, rely=.3, anchor=customtkinter.CENTER)
    button09.place(relx=.8, rely=.3, anchor=customtkinter.CENTER)
    button10.place(relx=.2, rely=.4, anchor=customtkinter.CENTER)
    button11.place(relx=.5, rely=.4, anchor=customtkinter.CENTER)
    button12.place(relx=.8, rely=.4, anchor=customtkinter.CENTER)
    button13.place(relx=.2, rely=.5, anchor=customtkinter.CENTER)
    button14.place(relx=.5, rely=.5, anchor=customtkinter.CENTER)
    button15.place(relx=.8, rely=.5, anchor=customtkinter.CENTER)
    button16.place(relx=.2, rely=.6, anchor=customtkinter.CENTER)
    button17.place(relx=.5, rely=.6, anchor=customtkinter.CENTER)
    button18.place(relx=.8, rely=.6, anchor=customtkinter.CENTER)
    app.mainloop()

def update_registry(reg_path, sound_file):
    try:
        with reg.OpenKey(reg.HKEY_CURRENT_USER, reg_path, 0, reg.KEY_SET_VALUE) as registry_key:
            reg.SetValueEx(registry_key, None, 0, reg.REG_SZ, sound_file)
    except Exception as e:
        print(f"Erreur :{e}")

if __name__ == '__main__':
    main()

if os.path.exists(c) and os.path.exists(d):
    regpath_in = r"AppEvents\Schemes\Apps\.Default\DeviceConnect\.Current"
    regpath_out = r"AppEvents\Schemes\Apps\.Default\DeviceDisconnect\.Current"
    update_registry(regpath_in, c)
    update_registry(regpath_out, d)