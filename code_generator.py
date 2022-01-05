from tkinter import *
import tkinter.messagebox as tmsg
import requests
import qrcode
from PIL import ImageTk, Image
import os

root = Tk()
root.minsize(600,400)
root.maxsize(600,400)
root.title("QR code generator")
root.configure(bg="green")
wb_url = StringVar()
wb_name = StringVar()

def save_img():
    name = wb_name.get()
    filename = name + ".jpg"
    os.popen(f'copy img.jpg {filename}')
    tmsg.showinfo("Complete","File Saved successfully")
    exit(0)



def show_img():
    global img2
    img_frame = Frame(root)
    img_frame.pack(side=TOP, pady=20)
    img = Image.open("img.jpg")
    img1 = img.resize((150,150), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img1)
    print(img1.size)
    img_label = Label(img_frame, image=img2)
    img_label.pack()
    Button(root, text="Save image", bg="blue", font=("tacoma", 10, "bold"), command=save_img).pack(side=TOP, anchor='center')

def generate():
    features = qrcode.QRCode(version=1, box_size=40, border=3)
    features.add_data(wb_url.get())
    features.make(fit=True)
    generate_image = features.make_image(fill_color="black", back_color="white")
    generate_image.save("img.jpg")
    show_img()
    
def create():
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    wb_name.set("            Enter website name")
    wb_url.set("                     Enter website url here")
    heading_frame = Frame(root, bg="aqua")
    heading_frame.pack(side=TOP, fill=BOTH)
    Label(heading_frame, text="QR Code Generator", bg="aqua", font=("tacoma", 20, "bold")).pack(anchor="w")
    data_frame = Frame(root,bg="green")
    data_frame.pack(fill=BOTH, side=TOP)
    web_name = Entry(data_frame, textvariable=wb_name, font=("tacoma", 15, "bold"))
    web_name.pack(side=TOP, anchor="nw", fill=BOTH, padx=100, pady=5)
    web_url = Entry(data_frame, textvariable=wb_url, font=("tacoma", 15, "bold"))
    web_url.pack(side=TOP, anchor="nw", fill=BOTH, padx=10, pady=5)
    Button(data_frame, text="Generate", bg="blue", font=("tacoma", 10, "bold"), command=generate).pack(side=TOP)

def start():
    starting_frame = Frame(root, bg="green")
    starting_frame.pack(padx=50, pady=50)
    Label(starting_frame, text="Hey, Now you can create\n QR code \n for your website", fg="purple", bg="green", font=("tacoma", 19, "bold")).pack(side=TOP)
    Button(starting_frame, text="Let's start", bg="blue", font=("tacoma", 15, "bold"), command=create).pack(side=TOP, pady=20)
    Label(starting_frame, text="Note: You should put a valid url", fg="aqua", bg="green", font=("tacoma", 10, "bold")).pack(side=TOP, pady=30)

start()

root.mainloop()