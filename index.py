import os
from flask import Flask, render_template, request

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    # remove all the existing image from the folder before uploading new one
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        #os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # move the file to the folder preview folder 
        os.rename(os.path.join(app.config['UPLOAD_FOLDER'], filename), os.path.join(app.config['UPLOAD_FOLDER'], '../preview', filename))
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename) 
    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    file.save(f)
    # upload the file into google drive

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)
