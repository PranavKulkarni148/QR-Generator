from turtle import color
import qrcode
from tkinter import*
import cv2
from tkinter import messagebox
root = Tk()
root.title("QR Code Generator")
root.geometry("700x700")
root.config(bg="Black")

def read():
    img = cv2.imread("yt.png")
    detector = cv2.QRCodeDetector()
    data, vertices, binary = detector.detectAndDecode(img)
    print(data)
def code():
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text.get())
    qr.make(fit=True)
    img = qr.make_image()
    img.save(f'.png')
    messagebox.showinfo("QR Code Generator", "QR Code is successfully saved")


frame1 = Frame(root, bg='green', bd=8)
frame1.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)
label1 = Label(frame1, text="QR Code Generator", bg='green', font="Times 20 bold")
label1.place(relx=0, rely=0, relwidth=1, relheight=1)

#To take Input text
frame2 = Frame(root, bg="Black")
frame2.place(relx=0.1, rely=0.15, relwidth=0.7, relheight=0.3)
label2 = Label(frame2, text="Enter the text/URL: ", bg="Black", fg='green', font="Courier 13 bold")
label2.place(relx=0.05, rely=0.2, relheight=0.08)
text = Entry(frame2, font='Century 12')
text.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

#To take input image name
frame3 = Frame(root, bg="Black")
frame3.place(relx=0.1, rely=0.35, relwidth=0.7, relheight=0.3)
label3 = Label(frame3, text="Enter the name of the QR Code", bg="Black", fg='green', font="Courier 13 bold")
label3.place(relx=0.05, rely=0.2, relheight=0.2)
name = Entry(frame3, font="Century 12")
name.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

#To take input of the sie of QR code
frame4 = Frame(root, bg="Black")
frame4.place(relx=0.1, rely=0.55, relwidth=0.7, relheight=0.3)
label4 = Label(frame4, text="Enter the size from 1 to 40:", bg="black", fg='green', font='Courier 13 bold')
label4.place(relx=0.05, rely=0.2, relheight=0.08)
size = Entry(frame4, font='Century 12')
size.place(relx=0.05, rely=0.4, relwidth=0.5, relheight=0.2)
button = Button(root, text="Generate Code", font='Courier 15 normal',fg='black', command=code)
button.place(relx=0.15, rely=0.9, relwidth=0.25, relheight=0.05)
root.mainloop()