### first run to get all the data. Next updates should be incremental
import requests

url="https://services.nvd.nist.gov/rest/json/cves/2.0"
resp = requests.get(url)

if(resp.status_code==200):
    data=resp.json()
    print("results per page = {0}".format(data["resultsPerPage"]))
    print("total results = {0}".format(data["totalResults"]))
    print("timestamp = {0}".format(data["timestamp"]))
    print("version = {0}".format(data["version"]))
    print("format = {0}".format(data["format"]))
    print("start index = {0}".format(data["startIndex"]))

else:
    print(resp.status_code)