import qrcode
from PIL import Image  #(PIL is used to modification of QR_code)

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=4,)

qr.add_data("https://chat.openai.com/")
qr.make(fit=True)
img = qr.make_image(fill_color="black",back_color="blue")
img.save("QR_chatGPT_openai.png")