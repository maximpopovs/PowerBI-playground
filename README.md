# PowerBI-playground
Small project to sharpen skills in PowerBI and Azure cloud services for ETL, with some Python coding.

## Public Data Sources in use:
- FBI Internet Crime Report (IC3). https://www.ic3.gov. Includes yearly summaries of internet crime reports: types of crime, losses, victim locations.
- NVD (National Vulnerability Database) - CVE Feeds. https://nvd.nist.gov/vuln/data-feeds. CVE vulnerabilities, including severity and descriptions.
- Cybersecurity Breaches Database. https://privacyrights.org/data-breaches. breach incidents with type, sector, organization, and impact
- CISA Known Exploited Vulnerabilities Catalog.  https://www.cisa.gov/known-exploited-vulnerabilities-catalog. vulnerabilities with active exploits.

## Logging and telemetry
- Application Insights for every part of solution to store telemetry and logs

## Security
- Secure raw files
- Secure Processed data
- Secure executables

## Data Engineering part of scope
- Ingestion
  - pull data from URLs using Azure Functions (Python) or Logic Apps
  - Azure Blob Storage to store raw data as JSON/CSV
- Storage
  - Use 
- Transformation
- Serving

## Data Visualization part of scope.
- Trend analysis
- geographic crime heatmaps
- loss estimates
- vulnerability trends
- critical CVEs over time
- patch prioritization
- Breach types
- industries affected
- vulnerability tracking and prioritization
- 
