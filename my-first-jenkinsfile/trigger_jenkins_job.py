import requests
from requests.auth import HTTPBasicAuth

# Configuration
JENKINS_URL = 'http://ec2-13-232-85-119.ap-south-1.compute.amazonaws.com:8080/'  # Replace with your Jenkins URL
JOB_NAME = 'demo'                     # Replace with your job name
USER = 'admin'                         # Replace with your Jenkins username
API_TOKEN = '119a0d5634c3163bb947feafe77517bb8d'                   # Replace with your Jenkins API token

# Trigger the Jenkins job
def trigger_job():
    url = f"{JENKINS_URL}/job/{JOB_NAME}/build"
    try:
        response = requests.post(url, auth=HTTPBasicAuth(USER, API_TOKEN))

        if response.status_code == 201:
            print(f"Successfully triggered job '{JOB_NAME}'.")
        else:
            print(f"Failed to trigger job '{JOB_NAME}'. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    trigger_job()

