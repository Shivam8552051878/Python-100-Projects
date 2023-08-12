# # # Importing library
# # import os
# #
# # import qrcode
# #
# # # Data to encode
# # data = "GeeksforGeeks"
# #
# # # Creating an instance of QRCode class
# # qr = qrcode.QRCode(version=1,
# #                    box_size=3,
# #                    border=1)
# #
# # # Adding data to the instance 'qr'
# # qr.add_data(data)
# #
# # qr.make(fit=True)
# # img = qr.make_image(fill_color='black',
# #                     back_color='white')
# #
# # img.save('MyQRCode2.png')
# # # os.rmdir("C:\Users\kdlte\PycharmProjects\CompanyNFC\MyQRCode2.png")
# # data = {'BEGIN': 'VCARD', 'VERSION': '3.0', 'N': 'Lastname;Firstname;;;', 'ADR;TYPE=HOME': ';;123 Main Street;Anytown;NY;12345;USA', 'FN': 'Firstname Lastname', 'EMAIL;TYPE=INTERNET': 'email@example.com', 'END': 'VCARD'}
# #
# # for va in data:
# #     print(va.split(";")[0])
# # data = """
# # jnedjcdnw
# # dewniocdekm
# # eokdwmsx
# #
# #
# #
# #
# # wdjiiwk2omsqx
# #
# # lkswkoqmxlqw
# #
# # swq mkqxmwq
# # """
# # print(data.split("\n"))
#
# from flask import Flask, send_file
# import tempfile
# import os
#
# app = Flask(__name__)
#
# @app.route('/download')
# def download_data():
#     # Retrieve data from the database
#     data = """BEGIN:VCARD
# VERSION:3.0
# N:Smith;John;;Mr.;
# FN:John Smith
# ORG:ABC Corporation
# TITLE:Marketing Manager
# TEL;TYPE=WORK,VOICE:123-456-7890
# TEL;TYPE=HOME,VOICE:987-654-3210
# ADR;TYPE=WORK,PREF:;;123 Main Street;Anytown;CA;12345;USA
# ADR;TYPE=HOME:;;456 Elm Avenue;Sometown;NY;54321;USA
# EMAIL;TYPE=WORK:john.smith@abccorp.com
# EMAIL;TYPE=HOME:johnsmith@gmail.com
# URL;TYPE=WORK:https://www.abccorp.com
# URL;TYPE=HOME:https://www.personalwebsite.com
# PHOTO;VALUE=URL;TYPE=JPEG:https://www.example.com/john_smith.jpg
# BDAY:1980-01-01
# X-ANNIVERSARY:2005-05-10
# NOTE:This is a note about John Smith.
# END:VCARD
#     """
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".vcf", prefix="Shivam", dir="./static") as file:
#         file.write(b"bskxns")
#         file.close()
#         # os.remove(file.name)
#         send_file(file.name, as_attachment=True, download_name="sxjhxjsk")
#         os.remove(file.name)
#         return "Succes"
#
#     # # Create a temporary file
#     # temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.vcf', prefix="contact")
#     #
#     # # Write the data to the temporary file
#     # temp_file.write(data.encode('utf-8'))
#     #
#     # # Close the file
#     # temp_file.close()
#     #
#     #
#     # # Send the temporary file as a download to the user
#     # response = send_file(temp_file.name, as_attachment=True)
#     #
#     # # Delete the temporary file
#     # os.remove(temp_file.name)
#
#     # return response
#
# if __name__ == '__main__':
#     app.run(debug=True)
import uuid

alpha = True
a = uuid.UUID() if alpha else "nbjdjw"
print(a)