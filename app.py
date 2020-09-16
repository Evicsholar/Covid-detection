from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'Uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template("index.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/inputform", methods=["GET", "POST"])
def input_symptoms():
    if request.method == 'POST':
        travel = str(request.form['travel'])
        tiredcough = str(request.form['commonsym'])
        breath = str(request.form['majorsym'])
        exposure = str(request.form['exposure'])
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
        if 0 == 0:
            result = 'here, '+travel, tiredcough, breath, exposure+" you go"
            return render_template('index.html', results=result)
    return None

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER





if __name__ == '__main__':
    app.run(debug=True)
