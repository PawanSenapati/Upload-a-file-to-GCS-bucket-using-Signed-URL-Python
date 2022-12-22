import datetime
from flask import Flask, request, render_template, url_for, redirect
from google.oauth2 import service_account
import os
import requests
from google.cloud import storage
from werkzeug.utils import secure_filename

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/path/to/key.json'

EXPIRATION = datetime.timedelta(hours=60)
FILE_TYPE = 'application/pdf'
BUCKET = 'BUCKET_NAME'

def upload_via_signed(bucket_name, blob_name, filename, expiration, file_type):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(blob_name)

    signed_url = blob.generate_signed_url(version="v4", method='PUT', expiration=expiration, content_type=file_type)
    print(signed_url)
    """
    print(
        "curl -X PUT -H 'Content-Type: application/octet-stream' "
        "--upload-file my-file '{}'".format(signed_url)
    )
    """
    requests.put(signed_url, open(filename.filename, 'rb'), headers={'Content-Type': file_type})

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        
        diag = request.files['file']
        filename_1 = secure_filename(diag.filename)
        diag.save(filename_1)
        print(diag)

        upload_via_signed(BUCKET, 'diag', diag, EXPIRATION, FILE_TYPE)
        os.remove(filename_1)

        return "done"
    
if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="0.0.0.0", port=8080, debug=True)
