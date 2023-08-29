from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    image_list = [
        "/static/dummy_images/sunset_serenade_beachside_captures.jpg",
        "/static/dummy_images/vibrant_abstract_watercolor_flow.jpg",
        "/static/dummy_images/vibrant_glow_technology_connection_joyful_smile.jpg"
    ]
    return render_template('home.html', image_list=image_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)