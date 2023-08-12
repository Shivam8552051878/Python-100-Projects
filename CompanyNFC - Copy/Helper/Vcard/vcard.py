class VCardFormate():
    def __init__(self):
        self.start_line = "BEGIN:VCARD\nVERSION:3.0"
        self.end_line = "END:VCARD"

        """
        FN (Formatted Name)
        N (Name)
        ORG (Organization)
        TITLE (Title/Position)
        EMAIL (Email Address)
        TEL (Phone Number)
        ADR (Address)
        URL (Website)
        PHOTO (Photo)
        """
        self.property_order = ["FN", "N", "ORG", "TITLE", "PHOTO", "EMAIL", "TEL", "URL", "ADR", "BDAY", "ANNIVERSARY",
                               "NOTE", "X-SOCIALPROFILE"]


    def name(self, name):
        return f"N:{name}"

    def formated_name(self, first_name, last_name):
        return f"FN:{last_name} {first_name}"

    def organization(self, organization):
        return f"ORG:{organization}"

    def title(self, title):
        return f"TITLE:{title}"

    def photo(self, imge_type, encoded_image):
        """
        here encoded_image using base64
        example:
              with open("path/to/your/image.jpg", "rb") as image_file:
              encoded_string = base64.b64encode(image_file.read())
              Decode:
              image_vcard_string = base64.b64decode(base64_string)

        :param imge_type:
        :param encoded_image:
        :return:
        """
        return f"PHOTO;TYPE={imge_type};ENCODING=BASE64:{encoded_image}"

    def phone(self, phone, type="work", phone_num_type="voice"):
        return f"TEL;TYPE={type},{phone_num_type}:{phone}"

    def email(self, email_id, type="work"):
        return f"EMAIL;TYPE={type}:{email_id}"

    def website(self, website_url, type="work"):
        return f"URL;TYPE={type}:{website_url}"

    def address(self, address_main, type):
        """
        # ADR;TYPE=work:;;123 Main St;City;State;ZIP;Country

        :param address_main:
        :param type:
        :return:
        """
        return f"# ADR;TYPE=work:;;{address_main}"

    def social_profile(self, url, type="whatsapp"):
        """X-SOCIALPROFILE;TYPE=linkedin:http://www.linkedin.com/in/johndoe
X-SOCIALPROFILE;TYPE=twitter:http://www.twitter.com/johndoe
X-SOCIALPROFILE;TYPE=facebook:http://www.facebook.com/johndoe
X-SOCIALPROFILE;TYPE=whatsapp:1234567890

  :param url=exception for whatsup type number needed

"""
        return f"X-SOCIALPROFILE;TYPE={type}:{url}"

    def notes(self, note):
        """
        NOTE:Additional notes or comments
        :param note:
        :return:
        """
        return f"NOTE:{note}"

    def birthday(self, bd_date):
        """
        bd_date formate example:
            BDAY:1990-01-01
        :param bd_date:
        :return:
        """
        return f"BDAY:{bd_date}"

    def anniversary(self, anniversary_date):
        """
        ANNIVERSARY example date formate:
            2010-05-10
        :param anniversary_date:
        :return:
        """
        return f"ANNIVERSARY:{anniversary_date}"

    def format_vcard(self, *args):
        # Split the VCard vcard_string into lines
        vcard_vcard_string = ""

        for arg in args:
            vcard_vcard_string += "\n" + arg

        lines = vcard_vcard_string.strip().split('\n')
        properties = {}
        formated_list = []

        for line in lines:
            if line != "":
                # print(line)
                # print(line.split(':'))
                key = line.split(':')[0]
                value = line.split(':')[1]
                if value.startswith("http") or value.startswith("https"):
                    value = line.split(':')[1] + ":" + line.split(':')[2]
                properties[key] = value

        # for key in properties:
        #     print(key.split(";")[0])

        for prop_name in self.property_order:
            for key in properties:
                if prop_name == key.split(";")[0]:
                    formated_list.append(f"{key}:{properties[key]}")
        # print(formated_list)
        str_formate = "\n".join(formated_list)
        vcard_string = self.start_line + "\n"
        vcard_string += str_formate
        vcard_string += "\n" + self.end_line
        return vcard_string


first = """
BEGIN:VCARD
VERSION:3.0
N:Smith;John;;Mr.;
FN:John Smith
ORG:ABC Corporation

URL;TYPE=HOME:https://www.personalwebsite.com

PHOTO;VALUE=URL;TYPE=JPEG:https://www.example.com/john_smith.jpg
BDAY:1980-01-01
X-ANNIVERSARY:2005-05-10
END:VCARD



In this updated example, the following fields have been added:
PHOTO (PHOTO): Specifies a photo or image associated with the contact. In this case, it's a URL pointing to John Smith's photo.
BDAY: Specifies John Smith's birth date (1980-01-01).
X-ANNIVERSARY: An extension field used to indicate John Smith's anniversary date (2005-05-10).
NOTE: Additional notes or comments about John Smith.Again, please note that this example uses vCard version 3.0, and different versions may have slightly different syntax or support additional fields.
"""
second = "NOTE:This is a note about John Smith."
thireds = """
TITLE:Marketing Manager



TEL;TYPE=WORK,VOICE:123-456-7890


TEL;TYPE=HOME,VOICE:987-654-3210
ADR;TYPE=WORK,PREF:;;123 Main Street;Anytown;CA;12345;USA
ADR;TYPE=HOME:;;456 Elm Avenue;Sometown;NY;54321;USA





EMAIL;TYPE=WORK:john.smith@abccorp.com
EMAIL;TYPE=HOME:johnsmith@gmail.com
URL;TYPE=WORK:https://www.abccorp.com
"""
# print(vcard.format_vcard(thireds, first, second))
