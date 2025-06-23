import sys
import requests
import boto3
import json
from datetime import datetime

# -------- CONFIG -------
URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
S3_BUCKET = "mp-pbi-play-ground"
S3_KEY_PREFIX = "NVD_RAW"
FETCH_ALL = True


all_data = []
param = "?startIndex={0}"



resp = requests.get(URL)
if(resp.status_code==200):
    data=resp.json()
    resultsPerPage = data["resultsPerPage"]
    totalResults = data["totalResults"]
    timestamp = datetime.strptime(data["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
    filename = "nvd_{0}".format(datetime.strftime(timestamp,"%Y%m%d"))
    s3_key=f"{S3_KEY_PREFIX}/{filename}"

    print("results per page = {0}".format(data["resultsPerPage"]))
    print("total results = {0}".format(data["totalResults"]))
    print("timestamp = {0}".format(data["timestamp"]))
    print("version = {0}".format(data["version"]))
    print("format = {0}".format(data["format"]))
    
else:
    print(resp.status_code)


