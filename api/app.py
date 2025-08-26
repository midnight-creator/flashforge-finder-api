from protocol import get_info, get_head_position, get_head_position, get_temp, get_progress, get_status
from socket_handler import get_devices

from flask import Flask, jsonify

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

PORT = 8899  # default port


@app.route("/")
def index():
    return 'Finder API'

@app.route("/<string:ip_address>/info")
def info(ip_address):
    printer_info = get_info({'ip': ip_address, 'port': PORT})
    return jsonify(printer_info)


@app.route("/<string:ip_address>/head-location")
def head_location(ip_address):
    printer_info = get_head_position({'ip': ip_address, 'port': PORT})
    return jsonify(printer_info)


@app.route("/<string:ip_address>/temp")
def temp(ip_address):
    printer_info = get_temp({'ip': ip_address, 'port': PORT})
    return jsonify(printer_info)


@app.route("/<string:ip_address>/progress")
def progress(ip_address):
    printer_info = get_progress({'ip': ip_address, 'port': PORT})
    return jsonify(printer_info)


@app.route("/<string:ip_address>/status")
def status(ip_address):
    printer_info = get_status({'ip': ip_address, 'port': PORT})
    return jsonify(printer_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
