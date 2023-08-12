# import uuid
#
# unique_id = str(uuid.uuid4())
# print(unique_id)
from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://your_username:your_password@localhost/your_database'  # Replace with your database connection details
# db = SQLAlchemy(app)
#
# class File(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     file_data = db.Column(db.LargeBinary)
#     file_name = db.Column(db.String(256))

@app.route('/download-file')
def download_file():
    # file_record = File.query.filter_by(id=1).first()  # Replace 'id=1' with your desired file identifier

    response = make_response("shivam this side")
    response.headers['Content-Disposition'] = 'attachment; filename=' + "file_record.txt"

    return response

if __name__ == '__main__':
    app.run()
