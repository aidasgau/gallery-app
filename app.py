from flask import Flask, render_template
from datetime import datetime 
import os

app = Flask(__name__)

current_year = datetime.now().year
full_name = 'Aidas Gaučas'

@app.route('/')
def index():
    return render_template('home.html', current_year=current_year, full_name=full_name)

@app.route('/gallery')
def gallery():
    image_thumbnail_directory = os.path.join(app.static_folder, 'dummy_images', 'thumbnails')

    image_files = [f for f in os.listdir(image_thumbnail_directory) if f.endswith('.png')]

    image_list = [os.path.join('/static/dummy_images/thumbnails', image) for image in image_files]

    return render_template('gallery.html', image_list=image_list, current_year=current_year, full_name=full_name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)