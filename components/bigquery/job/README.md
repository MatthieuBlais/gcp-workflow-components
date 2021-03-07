### BigQuery Job

Execute a BigQuery job and waits for its completion.

#### Deploy

```
gcloud workflows deploy workflow-component-bigquery-job \
--source=workflow.yaml \ 
[--location=MY_LOCATION]
[--service-account=MY_SERVICE_ACCOUNT@MY_PROJECT.IAM.GSERVICEACCOUNT.COM]
```

#### Parameters

- projectId: BQ project ID. If same as Workflow, you can use ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
- job: [Job object](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job)

##### Job example

{
    "configuration": {
        "extract": {
            "destinationUris": [
                "gs://xxxxx-306xxx-ml/quests/serverlessml2/data/taxi-train-*.csv"
            ],
            "destinationFormat": "CSV",
            "fieldDelimiter": ",",
            "sourceTable": {
                "projectId": "xxxxx-306xxx",
                "datasetId": "serverlessml",
                "tableId": "feateng_training_data"
            }
        }
    }
}


#### Example

```
steps:
- extract_training_dataset:
    call: experimental.executions.run
    args: 
        workflow_id: "workflow-component-bigquery-job"
        argument:
            projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
            job:
                configuration:
                    extract:
                        destinationUris:
                        - ${"gs://"+ bq_bucket + "/quests/serverlessml2/data/" + training_data }
                        destinationFormat: "CSV"
                        fieldDelimiter: ","
                        sourceTable:
                            projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                            datasetId: ${dataset_id}
                            tableId: ${table_id}
    result: bqjob
```


#### Output

Output is the [Job object](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job)

```
{
  "configuration": {
    "extract": {
      "destinationFormat": "CSV",
      "destinationUri": "gs://xxxx-306xxx-ml/quests/serverlessml2/data/taxi-train-*.csv",
      "destinationUris": [
        "gs://xxxx-306xxx-ml/quests/serverlessml2/data/taxi-train-*.csv"
      ],
      "fieldDelimiter": ",",
      "sourceTable": {
        "datasetId": "serverlessml",
        "projectId": "xxxx-306xxx",
        "tableId": "feateng_training_data"
      }
    },
    "jobType": "EXTRACT"
  },
  "etag": "1IFwjeDspdQVt3nLELQrSw==",
  "id": "xxxx-306xxx:US.job_qKCIkD3_8aVVAQM4Ak4-xxxxMBiV",
  "jobReference": {
    "jobId": "job_qKCIkD3_8aVVAQM4Ak4-xxxxMBiV",
    "location": "US",
    "projectId": "xxxx-306xxx"
  },
  "kind": "bigquery#job",
  "selfLink": "https://bigquery.googleapis.com/bigquery/v2/projects/xxxx-306xxx/jobs/job_qKCIkD3_8aVVAQM4Ak4-xxxxMBiV?location=US",
  "statistics": {
    "creationTime": "1614870569039",
    "startTime": "1614870569334"
  },
  "status": {
    "state": "RUNNING"
  },
  "user_email": "xxxx-306xxx@appspot.gserviceaccount.com"
}
```