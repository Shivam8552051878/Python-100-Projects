import os
import tempfile
data = """BEGIN:VCARD
VERSION:3.0
N:Smith;John;;Mr.;
FN:John Smith
ORG:ABC Corporation
TITLE:Marketing Manager
TEL;TYPE=WORK,VOICE:123-456-7890
TEL;TYPE=HOME,VOICE:987-654-3210
ADR;TYPE=WORK,PREF:;;123 Main Street;Anytown;CA;12345;USA
ADR;TYPE=HOME:;;456 Elm Avenue;Sometown;NY;54321;USA
EMAIL;TYPE=WORK:john.smith@abccorp.com
EMAIL;TYPE=HOME:johnsmith@gmail.com
URL;TYPE=WORK:https://www.abccorp.com
URL;TYPE=HOME:https://www.personalwebsite.com
PHOTO;VALUE=URL;TYPE=JPEG:https://www.example.com/john_smith.jpg
BDAY:1980-01-01
X-ANNIVERSARY:2005-05-10
NOTE:This is a note about John Smith.
END:VCARD
    """

# Create a temporary file
temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.vcf', prefix="contact")

# Write the data to the temporary file
temp_file.write(data.encode('utf-8'))

# Close the file
temp_file.close()
print(temp_file.name)
os.remove(temp_file.name)