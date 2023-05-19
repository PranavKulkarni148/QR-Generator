import qrcode

# Get inputs from the user
data1 = input("Enter argument 1: ")
data2 = input("Enter argument 2: ")
data3 = input("Enter argument 3: ")

if data3 == "":
    data3="-"
else:
    data3 = " " + data3

# Concatenate the inputs
data = f"{data1}\n{data2}\n{data3}"

# Generate the QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
image = qr.make_image(fill_color="black", back_color="white")

# Save the image
image.save("qr_code.png")