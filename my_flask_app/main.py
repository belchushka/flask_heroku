from os import walk
from flask import Flask, send_file, request
from kerykeion import KrInstance, MakeSvgInstance
from flask_cors import CORS
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/image', methods=['GET'])
def get_image():

    args = request.args

    name = args.get("name")
    year = args.get("year")
    month = args.get("month")
    day = args.get("day")
    hour = args.get("hour")
    minute = args.get("minute")
    city = args.get("city")

    kr_instance = KrInstance(name, int(year), int(month), int(day), int(hour), int(minute), city)

    svg_instance = MakeSvgInstance(kr_instance, chart_type="Natal")

    svg_instance.makeSVG()

    drawing = svg2rlg(svg_instance.chartname)

    dir = './natals/'+svg_instance.name+'.png'

    renderPM.drawToFile(drawing, dir, fmt='PNG')
    
    return send_file(dir, mimetype='image/png')

if __name__ == '__main__':
 app.run(debug=True,host='0.0.0.0', port=3000)
