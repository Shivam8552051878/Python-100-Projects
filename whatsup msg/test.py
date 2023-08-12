import pyautogui
import time
import pywhatkit as kit

# Open WhatsApp Web in a browser and navigate to the chat you want to send the image to

# Delay to ensure the browser is fully loaded
time.sleep(5)

# Perform actions to attach and send an image
pyautogui.click(x=500, y=500)  # Click the attachment button (replace with actual coordinates)
time.sleep(1)
pyautogui.click(x=600, y=600)  # Click the "Gallery" option (replace with actual coordinates)
time.sleep(1)

# Select the image (replace with actual coordinates)
pyautogui.click(x=700, y=700)

# Add more actions if needed, such as confirming the image selection and sending

# Wait for some time to allow the message to be sent
time.sleep(5)

# Sending a follow-up message (replace with your actual message)
kit.sendwhatmsg("+918552051878", "Check out this image!", 12, 54)
