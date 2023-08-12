import pywhatkit as kit

data = [{
    "name": "Shivam",
    "phone": "+918552051878",
}, {
    "name": "Amol",
    "phone": "+919158336173",
},
    {
        "name": "Nikesh",
        "phone": "+919819389701",
    }
]
# Define the components of your custom message
title = "Important Update:"
title_color = "red"
image_url = "Images/invitation.jpeg"
thank_you_msg = "Thank you for your attention!"
emoji = "🙌"

# Combine the components into a formatted message

counter = 44
for send_msg in data:
    formatted_msg = f"{title} to {send_msg['name']}\n\n{image_url}\n\n{thank_you_msg} {emoji}"

    # Sending the formatted message using pywhatkit
    kit.sendwhats_image("+918552051878", image_url, "Hello")
