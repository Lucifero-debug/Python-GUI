import qrcode

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Thickness of the border
)

# Add data to the QR code
upi_id=input("Enter Upi Id:\n")
url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image
# img.save('test.png')
img.show()
