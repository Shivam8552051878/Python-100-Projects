import qrcode
from PIL import Image, ImageDraw

data = "Hello, World!"  # The data you want to encode into the QR code

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

# Create an image from the QR code
qr_image = qr.make_image(fill_color="red", back_color="yellow")

# Convert the image to RGBA format
qr_image = qr_image.convert("RGBA")

# Get the size of the image
width, height = qr_image.size

# Create a new image with a transparent background
circle_image = Image.new("RGBA", (width, height), (255, 255, 255, 255))

# Create a draw object
draw = ImageDraw.Draw(circle_image)

# Calculate the radius of the circles
radius = qr.box_size // 2

# Iterate over each module (box) in the QR code image
for row in range(qr.modules_count):
    for col in range(qr.modules_count):
        # Check if the module should be filled
        if qr.modules[row][col]:
            # Calculate the position of the current module
            x = qr.border * qr.box_size + col * qr.box_size
            y = qr.border * qr.box_size + row * qr.box_size

            # Calculate the coordinates of the circle
            x1 = x + qr.box_size - radius
            y1 = y + qr.box_size - radius
            x2 = x + qr.box_size + radius
            y2 = y + qr.box_size + radius

            # Draw a circle at the current position
            draw.ellipse((x1, y1, x2, y2), fill=(255, 0, 0, 255))

# Combine the circle image with the QR code image
result_image = Image.alpha_composite(qr_image, circle_image)

# Save the final QR code image with circles
result_image.save("qr_code_with_circles.png")
result_image.show()
