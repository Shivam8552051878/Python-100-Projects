from os import name

import vobject


# def Vcard():
#     """
#     BEGIN:VCARD
# VERSION:3.0
# N:Doe;John;;;
# FN:John Doe
# ORG:OpenAI;AI Research Lab
# TITLE:Research Scientist
# PHOTO;VALUE=URL;TYPE=JPEG:http://example.com/photo.jpg
# TEL;TYPE=work,voice:0987654321
# TEL;TYPE=home,voice:5555555555
# TEL;TYPE=cell,voice:1234567890
# TEL;TYPE=work,fax:9876543210
# EMAIL;TYPE=work:john.doe@example.com
# EMAIL;TYPE=home:john.doe@gmail.com
# URL;TYPE=work:http://www.example.com
# ADR;TYPE=work:;;123 Main St;City;State;ZIP;Country
# ADR;TYPE=home:;;456 Elm St;City;State;ZIP;Country
# BDAY:1990-01-01
# ANNIVERSARY:2010-05-10
# NOTE:Additional notes or comments
# X-SOCIALPROFILE;TYPE=linkedin:http://www.linkedin.com/in/johndoe
# X-SOCIALPROFILE;TYPE=twitter:http://www.twitter.com/johndoe
# X-SOCIALPROFILE;TYPE=facebook:http://www.facebook.com/johndoe
# X-SOCIALPROFILE;TYPE=whatsapp:1234567890
# END:VCARD
#     :return:
#     """
#
#
# import base64
#
#
# def encode_image_to_base64(image_path):
#     with open(image_path, "rb") as image_file:
#         encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
#     return encoded_image
#
# def add_address_to_vcard(vcard, address):
#     vcard += f"ADR;TYPE=HOME:;;{address['street']};{address['city']};{address['state']};{address['postal_code']};{address['country']}\n"
#     return vcard
#
# def generate_vcard_with_photo(name, organization, title, image_path, imge_type, home_phone, work_phone, cell_phone, work_phone_fax,
#                               work_email, home_email, home_add, work_add, note, linkidin_profile, twitter_profile,
#                               face_book_profile, whatsup_number):
#     encoded_image = encode_image_to_base64(image_path)
#
#     vcard = f"""
#     BEGIN:VCARD
# VERSION:3.0
# N:{name}
# FN:{name}
# ORG:{organization}
# TITLE:{title}
# PHOTO;TYPE={imge_type};ENCODING=b:{encoded_image}
# TEL;TYPE=work,voice:{work_phone}
# TEL;TYPE=home,voice:{home_phone}
# TEL;TYPE=cell,voice:{cell_phone}
# TEL;TYPE=work,fax:{work_phone_fax}
# EMAIL;TYPE=work:{work_email}
# EMAIL;TYPE=home:{home_email}
# URL;TYPE=work:http://www.example.com
# ADR;TYPE=work:;;123 Main St;City;State;ZIP;Country
# ADR;TYPE=home:;;456 Elm St;City;State;ZIP;Country
# BDAY:1990-01-01
# ANNIVERSARY:2010-05-10
# NOTE:Additional notes or comments
# X-SOCIALPROFILE;TYPE=linkedin:http://www.linkedin.com/in/johndoe
# X-SOCIALPROFILE;TYPE=twitter:http://www.twitter.com/johndoe
# X-SOCIALPROFILE;TYPE=facebook:http://www.facebook.com/johndoe
# X-SOCIALPROFILE;TYPE=whatsapp:1234567890
# END:VCARD
#     """
#     return vcard
#
#
# # vcard = generate_vcard_with_photo("shivam", "sg9967780426@gmail.com", 8552051878, "../static/img/contact-bg.jpg")
# # print(vcard)
# #
# # with open("file.vcf", "w") as file:
# #     file.write(vcard)

vcard = vobject.vCard()
vcard.add('fn').value = "shivam"
# vcard.add('n').value = "Gupta"
vcard.add('tel').value = "8552051878"
vcard.add('email').value = "sg9967780426@gmail.com"
print(type(vcard.serialize()))
print(vcard.serialize())