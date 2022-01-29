"""A Python Flask App for DanaXA Test By Shahab Rahnama"""

import argparse
import os
from flask import Flask
from flask_cors import CORS
from routes import request_api


APP = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
 
APP.secret_key = "secret key"
APP.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
APP.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
 
 
APP.register_blueprint(request_api.get_blueprint())
 
if __name__ == '__main__':
    
    PARSER = argparse.ArgumentParser(description="Python Flask Danaxa Test By Shahab Rahnama")

    PARSER.add_argument('--debug', 
                        action='store_true',
                        help="Use flask debug/dev mode with file change reloading")
    ARGS = PARSER.parse_args()

    PORT = int(os.environ.get('PORT', 5000))

    if ARGS.debug:
        print("Running in debug mode")
        CORS = CORS(APP)
        APP.run(host='0.0.0.0', port=PORT, debug=True)
    else:
        APP.run(host='0.0.0.0', port=PORT, debug=False)