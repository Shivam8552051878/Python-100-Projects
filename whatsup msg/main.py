import pywhatkit
from bs4 import BeautifulSoup
# pywhatkit.start_server()
html_content = "<h1>Hello, this is an HTML message!</h1><p>This is a <strong>bold</strong> and <em>italic</em> message.</p>"

# Convert HTML to plain text
soup = BeautifulSoup(html_content, 'html.parser')
plain_text_content = soup.get_text()
pywhatkit.sendwhatmsg("+918552051878", plain_text_content, 11, 50, True, 8)

# # Same as above but Closes the Tab in 2 Seconds after Sending the Message
# pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)
#
# # Send an Image to a Group with the Caption as Hello
# pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")
#
# # Send an Image to a Contact with the no Caption
# pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")
#
# # Send a WhatsApp Message to a Group at 12:00 AM
# pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)
#
# # Send a WhatsApp Message to a Group instantly
# pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")
#
# # Play a Video on YouTube
# pywhatkit.playonyt("PyWhatKit")