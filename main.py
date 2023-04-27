from flask import Flask, Response, send_file, request
from kerykeion import KrInstance, MakeSvgInstance


app = Flask(__name__)

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

    print(request.args)
    # Create KrInstance object
    kr_instance = KrInstance(name, int(year), int(month), int(day), int(hour), int(minute), city)

    # Create MakeSvgInstance object with KrInstance object and chart type
    svg_instance = MakeSvgInstance(kr_instance, chart_type="Natal")

    # Call makeSVG method to generate SVG image
    svg_instance.makeSVG()

    # Return the SVG image as a response
    return send_file(svg_instance.chartname, mimetype='image/svg+xml')
