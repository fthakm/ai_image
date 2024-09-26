from flask import Flask, render_template, request, redirect, url_for
import os
import model  # Mengimpor model Anda

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'male' not in request.files or 'female' not in request.files:
        return redirect(url_for('home'))

    male_file = request.files['male']
    female_file = request.files['female']

    if male_file.filename == '' or female_file.filename == '':
        return redirect(url_for('home'))

    male_path = os.path.join(app.config['UPLOAD_FOLDER'], male_file.filename)
    female_path = os.path.join(app.config['UPLOAD_FOLDER'], female_file.filename)

    male_file.save(male_path)
    female_file.save(female_path)

    # Menggunakan model AI untuk menghasilkan gambar
    generated_image_path = model.generate_image(male_path, female_path)

    return render_template('result.html', generated_image=generated_image_path)

if __name__ == '__main__':
    app.run(debug=True)
