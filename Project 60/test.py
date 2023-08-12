from flask import Flask, render_template, send_file
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def download_file():
    # Retrieve the file data from the database
    file_data = b"Shivam is Boss"  # Replace this with your logic to retrieve the file data

    # Create an in-memory file-like object
    file_stream = BytesIO(file_data)

    # Render the template with the download button and file content
    return render_template('download.html', file_data=file_stream.getvalue())

@app.route('/download-file/download')
def download():
    # Retrieve the file data from the database
    file_data = "Shivam Is boss"  # Replace this with your logic to retrieve the file data

    # Create an in-memory file-like object
    file_stream = BytesIO(file_data)

    # Return the file as a response for download
    return send_file(file_stream, attachment_filename='myfile.txt', as_attachment=True, download_name="myfile.txt")

if __name__ == '__main__':
    app.run(debug=True)
