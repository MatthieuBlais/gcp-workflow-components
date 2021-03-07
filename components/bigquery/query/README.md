### BigQuery Synchronous Query

Execute a query in BigQuery and waits for its output.

#### Deploy

```
gcloud workflows deploy workflow-component-bigquery-query \
--source=workflow.yaml \ 
[--location=MY_LOCATION]
[--service-account=MY_SERVICE_ACCOUNT@MY_PROJECT.IAM.GSERVICEACCOUNT.COM]
```

#### Parameters

- projectId: BQ project ID. If same as Workflow, you can use ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
- query: [Query object](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query)

##### Query example

{
    "projectId":"xxxx-306xxx",
    "query":{
        "location":"US",
        "query":"SELECT * FROM mytable",
        "useLegacySql":false
    }
}

#### Example

```
steps:
- prepare_training_dataset:
    call: experimental.executions.run
    args: 
        workflow_id: "workflow-component-bigquery-query"
        argument:
            projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
            query:
                location: ${bq_location}
                useLegacySql: false
                query: |
                    CREATE OR REPLACE TABLE serverlessml.feateng_training_data AS
                    SELECT
                    (tolls_amount + fare_amount) AS fare_amount,
                    pickup_datetime,
                    pickup_longitude AS pickuplon,
                    pickup_latitude AS pickuplat,
                    dropoff_longitude AS dropofflon,
                    dropoff_latitude AS dropofflat,
                    passenger_count*1.0 AS passengers,
                    'unused' AS key
                    FROM `nyc-tlc.yellow.trips`
                    WHERE ABS(MOD(FARM_FINGERPRINT(CAST(pickup_datetime AS STRING)), 1000)) = 1
                    AND
                    trip_distance > 0
                    AND fare_amount >= 2.5
                    AND pickup_longitude > -78
                    AND pickup_longitude < -70
                    AND dropoff_longitude > -78
                    AND dropoff_longitude < -70
                    AND pickup_latitude > 37
                    AND pickup_latitude < 45
                    AND dropoff_latitude > 37
                    AND dropoff_latitude < 45
                    AND passenger_count > 0
    result: training_dataset
```


#### Output

Output is the [Query object](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query)

```
{
  "cacheHit": false,
  "jobComplete": true,
  "jobReference": {
    "jobId": "job_xxxxxxx_b2sSwftlyvr6wPzn",
    "location": "US",
    "projectId": "xxxxx-306xxx"
  },
  "kind": "bigquery#queryResponse",
  "schema": {
    "fields": [
      {
        "name": "fare_amount",
        "type": "FLOAT"
      },
      {
        "name": "pickup_datetime",
        "type": "TIMESTAMP"
      },
      {
        "name": "pickuplon",
        "type": "FLOAT"
      },
      {
        "name": "pickuplat",
        "type": "FLOAT"
      },
      {
        "name": "dropofflon",
        "type": "FLOAT"
      },
      {
        "name": "dropofflat",
        "type": "FLOAT"
      },
      {
        "name": "passengers",
        "type": "FLOAT"
      },
      {
        "name": "key",
        "type": "STRING"
      }
    ]
  },
  "totalBytesProcessed": "79831998488"
}
```