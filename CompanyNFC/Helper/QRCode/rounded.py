# # # # from qrcode import QRCode
# # # #
# # # #
# # # # class MyQRCode(QRCode):
# # # #     pass
# # #
# # # import qrcode
# # # from PIL import Image
# # #
# # # data = "Hello, World!"  # The data you want to encode into the QR code
# # # logo_path = "img.png"  # Path to the logo image
# # #
# # # # Create an instance of the QRCode class
# # # qr = qrcode.QRCode(
# # #     version=1,
# # #     error_correction=qrcode.constants.ERROR_CORRECT_H,
# # #     box_size=10,
# # #     border=4,
# # # )
# # #
# # # # Add the data to the QR code
# # # qr.add_data(data)
# # # qr.make(fit=True)
# # #
# # # # Create an image from the QR code
# # # qr_image = qr.make_image(fill_color="black", back_color="white")
# # #
# # # # Open the logo image
# # # logo_image = Image.open(logo_path)
# # #
# # # # Resize the logo image to fit within the QR code
# # # logo_image = logo_image.resize((100, 100))
# # #
# # # # Calculate the position to place the logo in the center of the QR code
# # # position = ((qr_image.size[0] - logo_image.size[0]) // 2, (qr_image.size[1] - logo_image.size[1]) // 2)
# # #
# # # # Paste the logo image onto the QR code image
# # # qr_image.paste(logo_image, position)
# # #
# # # # Save the final QR code image with the logo
# # # qr_image.save("qr_code_with_logo.png")
# # # qr_image.show()
# # # import qrcode
# # # from PIL import Image, ImageDraw
# # #
# # # data = "Hello, World!"  # The data you want to encode into the QR code
# # #
# # # # Create an instance of the QRCode class
# # # qr = qrcode.QRCode(
# # #     version=1,
# # #     error_correction=qrcode.constants.ERROR_CORRECT_H,
# # #     box_size=10,
# # #     border=4,
# # # )
# # #
# # # # Add the data to the QR code
# # # qr.add_data(data)
# # # qr.make(fit=True)
# # #
# # # # Create an image from the QR code
# # # qr_image = qr.make_image(fill_color="black", back_color="white")
# # #
# # # # Convert the image to RGBA format
# # # qr_image = qr_image.convert("RGBA")
# # #
# # # # Get the size of the image
# # # width, height = qr_image.size
# # #
# # # # Create a new image with a transparent background
# # # circle_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
# # #
# # # # Create a draw object
# # # draw = ImageDraw.Draw(circle_image)
# # #
# # # # Calculate the radius of the circles
# # # radius = qr.box_size // 2
# # #
# # # # Iterate over each module (box) in the QR code image
# # # for row in range(qr.modules_count):
# # #     for col in range(qr.modules_count):
# # #         # Calculate the position of the current module
# # #         x = qr.border * qr.box_size + col * qr.box_size
# # #         y = qr.border * qr.box_size + row * qr.box_size
# # #
# # #         # Calculate the coordinates of the circle
# # #         x1 = x + qr.box_size - radius
# # #         y1 = y + qr.box_size - radius
# # #         x2 = x + qr.box_size + radius
# # #         y2 = y + qr.box_size + radius
# # #
# # #         # Draw a circle at the current position
# # #         draw.ellipse((x1, y1, x2, y2), fill=(0, 255, 0, 255))
# # #
# # # # Combine the circle image with the QR code image
# # # result_image = Image.alpha_composite(qr_image, circle_image)
# # #
# # # # Save the final QR code image with circles
# # # result_image.save("qr_code_with_circles.png")
# # # result_image.show()
# # # import qrcode
# # #
# # # data = "Hello, World!"  # The data you want to encode into the QR code
# # #
# # # # Create an instance of the QRCode class
# # # qr = qrcode.QRCode(
# # #     version=1,  # The version parameter controls the size of the QR code (1 to 40)
# # #     error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level
# # #     box_size=10,  # The number of pixels each "box" of the QR code takes up
# # #     border=4,  # The number of boxes around the QR code
# # # )
# # #
# # # # Add the data to the QR code
# # # qr.add_data(data)
# # # qr.make(fit=True)
# # #
# # # # Create an image from the QR code
# # # img = qr.make_image(fill_color="black", back_color="white")
# # #
# # # # Save the image or display it
# # # img.save("qr_code.png")
# # # img.show()
# # ### Select Image factory
# #
# # # SVG
# # from qrcode_styled.svg.image import SVGStylingImage
# # # Pillow
# # from qrcode_styled.pil.image import PilStyledImage
# #
# # ### Create QRCode factory
# #
# # import qrcode_styled
# #
# # qr = qrcode_styled.QRCodeStyled(
# #     # QRCode version. Default: auto
# #     version=None,
# #     # How much ECC. Default: M
# #     error_correction=qrcode_styled.ERROR_CORRECT_L,
# #     # Image border thickness in tiles. Default: 1
# #     border=1,
# #     # Size of each separate tile. Default: 32
# #     box_size=32,
# #     # Image processing library. Default: Pillow
# #     image_factory=SVGStylingImage,
# #     # QRCode mask pattern version: [0 to 7] included. Default: auto
# #     mask_pattern=None,
# # )
# #
# # ### Generate QRCode
# # img = qr.get_image(
# #     # Payload. Required
# #     data='https://cifrazia.com',
# #     # Image to put in the middle of QRCode. file handler.
# #     image=None,
# #     # Data encoding optimization level, not Image optimization.
# #     optimize=20,
# # )
# # # img.save("hello")
# # # ### Store it in file
# # with open('link.webp', 'wb') as _fh:
# #     img.save(_fh, 'WEBP')
# import qrcode
# from PIL import Image
#
# data = "Hello, World!"  # The data you want to encode into the QR code
# logo_path = "img.png"  # Path to the logo image
#
# # Create an instance of the QRCode class
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_H,
#     box_size=10,
#     border=4,
# )
#
# # Add the data to the QR code
# qr.add_data(data)
# qr.make(fit=True)
#
# # Create the QR code image
# qr_image = qr.make_image(fill_color="red", back_color="black")
#
# # Open the logo image
# logo_image = Image.open(logo_path)
#
# # Calculate the size of the QR code image and the logo image
# qr_size = qr_image.size
# logo_size = (qr_size[0] // 4, qr_size[1] // 4)
#
# # Resize the logo image to fit within the QR code
# logo_image = logo_image.resize(logo_size)
#
# # Calculate the position to place the logo in the center of the QR code
# logo_position = ((qr_size[0] - logo_size[0]) // 2, (qr_size[1] - logo_size[1]) // 2)
#
# # Paste the logo image onto the QR code image
# qr_image.paste(logo_image, logo_position)
#
# # Save the final QR code image with the logo
# qr_image.save("qr_code_with_logo.png")
# qr_image.show()



# import qrcode
# from PIL import Image
#
# data = "Hello, World!"  # The data you want to encode into the QR code
# logo_path = "img.png"  # Path to the logo image
#
# # Create an instance of the QRCode class
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_H,
#     box_size=10,
#     border=4,
# )
#
# # Add the data to the QR code
# qr.add_data(data)
# qr.make(fit=True)
#
# # Create the QR code image
# qr_image = qr.make_image(fill_color="black", back_color="white")
#
# # Open the logo image
# logo_image = Image.open(logo_path)
#
# # Calculate the size of the QR code image and the logo image
# qr_size = qr_image.size
# logo_size = (qr_size[0] // 4, qr_size[1] // 4)
#
# # Resize the logo image to fit within the QR code
# logo_image = logo_image.resize(logo_size, Image.ANTIALIAS)
#
# # Calculate the position to place the logo in the center of the QR code
# logo_position = ((qr_size[0] - logo_size[0]) // 2, (qr_size[1] - logo_size[1]) // 2)
#
# # Create a new image with RGBA format for the QR code with logo
# qr_with_logo = Image.new("RGBA", qr_size)
#
# # Paste the QR code onto the new image
# qr_with_logo.paste(qr_image, (0, 0))
#
# # Paste the logo image onto the QR code image at the calculated position
# qr_with_logo.paste(logo_image, logo_position, mask=logo_image)
#
# # Save the final QR code image with the logo
# qr_with_logo.save("qr_code_with_logo.png")
# qr_with_logo.show()


import qrcode
from PIL import Image

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

logo_position = ((qr_size[0] - logo_size[0]) // 2, (qr_size[1] - logo_size[1]) // 2)

# Create a new image with RGBA format for the QR code with logo
qr_with_logo = Image.new("RGBA", qr_size)

# Paste the QR code onto the new image
qr_with_logo.paste(qr_image, (0, 0))

# Create a mask from the logo image's alpha channel
logo_mask = logo_image.convert("RGBA").split()[3]

# Paste the logo image onto the QR code image at the calculated position
qr_with_logo.paste(logo_image, logo_position, mask=logo_mask)

# Save the final QR code image with the logo
qr_with_logo.save("qr_code_with_logo.png")
qr_with_logo.show()
