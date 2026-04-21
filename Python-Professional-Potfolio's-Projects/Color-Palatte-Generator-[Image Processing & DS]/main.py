from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % tuple(rgb)


def get_colors(image_path, num_colors=10):
    img = Image.open(image_path)
    img = img.convert('RGB')
    img = img.resize((150, 150))
    img_array = np.array(img)
    pixels = img_array.reshape(-1, 3)

    kmeans = KMeans(n_clusters=num_colors, random_state=42, n_init=10)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_.astype(int)
    hex_colors = [rgb_to_hex(color) for color in colors]
    return hex_colors


@app.route('/', methods=['GET', 'POST'])
def index():
    colors = None
    image_url = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            colors = get_colors(filepath)
            image_url = url_for('static', filename=f'uploads/{filename}')
    return render_template('index.html', colors=colors, image_url=image_url)


if __name__ == '__main__':
    app.run(debug=True)