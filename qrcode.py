import qrcode

# Text or URL for QR
data = "https://chat.openai.com"

# Create QR
qr = qrcode.make(data)

# Save QR as image
qr.save("my_qr.png")
#pip install qrcode[pil]when run the code 1st install this 

print("✅ QR Code generated and saved as 'my_qr.png'")
