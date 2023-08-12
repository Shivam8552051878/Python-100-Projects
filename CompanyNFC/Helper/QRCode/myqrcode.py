import qrcode
from qrcode import QRCode
from PIL import Image
from io import BytesIO
import base64


class MyQRCode(QRCode):
    def __init__(self, data, box_size=10, border=4, fill_color="black", back_color="white", logo_image=None):
        super().__init__(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=box_size,
            border=border,
        )
        # Add the data to the QR code
        self.add_data(data)
        self.make(fit=True)

        # Create the QR code image
        qr_image = self.make_image(fill_color="black", back_color="white")
        # Create an in-memory byte stream
        qr_stream = BytesIO()
        qr_image.save(qr_stream, format='PNG')
        qr_stream.seek(0)
        self.qr_base64 = base64.b64encode(qr_stream.getvalue()).decode('utf-8')

    # def __init__(self, data, logo_path,box_size=10, border=4, fill_color="black", back_color="white", logo_image=None):
    #     super().__init__(
    #         version=1,
    #         error_correction=qrcode.constants.ERROR_CORRECT_H,
    #         box_size=box_size,
    #         border=border,
    #     )
    #
    #     # Add the data to the QR code
    #     self.add_data(data)
    #     self.make(fit=True)
    #
    #     # Create the QR code image
    #     qr_image = self.make_image(fill_color="black", back_color="white")
    #
    #     # Open the logo image
    #     logo_image = Image.open(logo_path)
    #
    #     # Calculate the size of the QR code image and the logo image
    #     qr_size = qr_image.size
    #     logo_size = (qr_size[0] // 4, qr_size[1] // 4)
    #
    #     # Resize the logo image to fit within the QR code
    #     logo_image = logo_image.resize(logo_size)
    #
    #     # Calculate the position to place the logo in the center of the QR code
    #     logo_position = ((qr_size[0] - logo_size[0]) // 2, (qr_size[1] - logo_size[1]) // 2)
    #
    #     # Create a new image with RGBA format for the QR code with logo
    #     qr_with_logo = Image.new("RGBA", qr_size)
    #
    #     # Paste the QR code onto the new image
    #     qr_with_logo.paste(qr_image, (0, 0))
    #
    #     # Create a mask from the logo image's alpha channel
    #     logo_mask = logo_image.convert("RGBA").split()[3]
    #
    #     # Paste the logo image onto the QR code image at the calculated position
    #     qr_with_logo.paste(logo_image, logo_position, mask=logo_mask)
    #
    #     # Create an in-memory byte stream
    #     qr_stream = BytesIO()
    #     qr_with_logo.save(qr_stream, format='PNG')
    #     qr_stream.seek(0)
    #
    #     # Convert the byte stream to Base64 encoding
    #     self.qr_base64 = base64.b64encode(qr_stream.getvalue()).decode('utf-8')
    #
