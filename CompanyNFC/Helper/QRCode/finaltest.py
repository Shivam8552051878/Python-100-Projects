import qrcode
from flask import Flask, render_template
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def generate_qr_code_with_logo():
    data = "Hello, World!"  # The data you want to encode into the QR code
    logo_path = "img.png"  # Path to the logo image

    # Create an instance of the QRCode class
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Add the data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create the QR code image
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Open the logo image
    logo_image = Image.open(logo_path)

    # Calculate the size of the QR code image and the logo image
    qr_size = qr_image.size
    logo_size = (qr_size[0] // 4, qr_size[1] // 4)

    # Resize the logo image to fit within the QR code
    logo_image = logo_image.resize(logo_size)

    # Calculate the position to place the logo in the center of the QR code
    logo_position = ((qr_size[0] - logo_size[0]) // 2, (qr_size[1] - logo_size[1]) // 2)

    # Create a new image with RGBA format for the QR code with logo
    qr_with_logo = Image.new("RGBA", qr_size)

    # Paste the QR code onto the new image
    qr_with_logo.paste(qr_image, (0, 0))

    # Create a mask from the logo image's alpha channel
    logo_mask = logo_image.convert("RGBA").split()[3]

    # Paste the logo image onto the QR code image at the calculated position
    qr_with_logo.paste(logo_image, logo_position, mask=logo_mask)

    # Create an in-memory byte stream
    qr_stream = BytesIO()
    qr_with_logo.save(qr_stream, format='PNG')
    qr_stream.seek(0)

    # Convert the byte stream to Base64 encoding
    qr_base64 = base64.b64encode(qr_stream.getvalue()).decode('utf-8')
    # print(type(qr_base64))
    # print(qr_base64)
    return render_template('index.html', qr_image=qr_base64)


if __name__ == '__main__':
    app.run()
