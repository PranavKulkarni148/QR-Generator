import qrcode
from PIL import Image

data=input("enter data here: ")

qrcolor=input(str("Enter QR Color: "))
bgcolor=input(str("Enter Background Color: "))

qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=8,border=3,)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color=qrcolor,back_color=bgcolor)
img.save("Pranav.png")