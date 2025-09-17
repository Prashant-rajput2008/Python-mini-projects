import qrcode

data = "https://youtu.be/uX5twbuJVKI?list=RDuX5twbuJVKI"

qr = qrcode.QRCode(
    version=1,           
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,        
    border=4,           
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("qrcode.png")

print("QR code generated and saved as qrcode.png!")
