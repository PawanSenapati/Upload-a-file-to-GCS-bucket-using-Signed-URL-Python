# Upload-a-file-to-GCS-bucket-using-Signed-URL-Python
Learn how to upload a file to Google Cloud Storage Bucket using Signed URL (Python).

```
1. Navigate to GCP Cloud Shell.
2. Clone this repository to your GCP console using (gcloud source repos clone [REPO_NAME] --project=[PROJECT_NAME])
3. Ensure that you have a GCS bucket in your GCP project.
4. Create a Service Account and a private key for the service account.
    https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating
5. Download the JSON file (say key.json) of the private key. Upload the key.json file to GCP console.
6. Replace the bucket name and the credential (i.e. path to key.json) in main.py.
7. Run command: python main.py
```
