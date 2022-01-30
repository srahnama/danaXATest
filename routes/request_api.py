"""The Endpoints to manage the DanaXA test"""
import uuid
from flask import Blueprint, flash, request, redirect, url_for, render_template
import ast
import os
from werkzeug.utils import secure_filename
from engine.spline import spline
from model import model


REQUEST_API = Blueprint('request_api', __name__)


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'static/uploads/'

def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
@REQUEST_API.route('/')
def home():
    return render_template('index.html')
 
@REQUEST_API.route('/', methods=['POST'])
def upload_image():
    req = request.form.to_dict()
   
    # print(req['cparam'])
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        model.save_data({file.filename:[ast.literal_eval(req['tparam']),ast.literal_eval(req['cparam']), int(req['kparam'])]})
        spline(filename,ast.literal_eval(req['tparam']),ast.literal_eval(req['cparam']), int(req['kparam']))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('index.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
@REQUEST_API.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)
 

