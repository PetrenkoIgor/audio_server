import glob
import os

from flask import Flask, render_template, request, redirect, url_for

from audio import *

app = Flask(__name__)
app.config['FILE_UPLOADS'] = "static/file"
mp3_str = Mp3_streamer()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin_audio_controller', methods=['POST', 'GET'])
def admin_audio_controller():
    if request.method == "POST":
        if request.form.get("start"):
            mp3_str.run()
        elif request.form.get("stop"):
            mp3_str.stop()
        elif request.form.get("change"):
            redirect(url_for('admin_set_audio'))
    return render_template("admin_audio_controller.html")


@app.route('/admin_set_audio', methods=['POST', 'GET'])
def admin_set_audio():

    if request.method == 'POST':
        files = request.files.getlist("file")
        for file in files:
            if request.files["file"]:
                file_path = os.path.join(app.config["FILE_UPLOADS"], file.filename).replace("\\", "/")
                file.save(file_path)
                mp3_str.change_music(file_path)
                print(file_path)
                return redirect(url_for('admin_audio_controller'))
    return render_template("admin_set_audio.html")


if __name__ == '__main__':
    app.secret_key = "^A%!kklKH^JJ123"
    app.run(host='0.0.0.0', port=5001, debug=True)
