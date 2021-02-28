### CloudBuild Job

Trigger a CloudBuild job and wait for its completion.


#### Deploy

`
gcloud workflows deploy my-test-workflow \
--source=workflow.yaml \ 
[--location=MY_LOCATION]
[--service-account=MY_SERVICE_ACCOUNT@MY_PROJECT.IAM.GSERVICEACCOUNT.COM]
`

#### Parameters

- project_id: Name of your GCP project. You can use the built-in [environment variable](https://cloud.google.com/workflows/docs/reference/environment-variables) GOOGLE_CLOUD_WORKFLOW_ID
- build: Standard CloudBuild [build configuration](https://cloud.google.com/build/docs/build-config).


#### Example

```
steps:
  - trigger_cloudbuild:
      call: experimental.executions.run
      args:
        workflow_id: my-test-workflow
        argument:
            project_id: ${sys.get_env("GOOGLE_CLOUD_WORKFLOW_ID")}
            build:
              steps:
                - name: 'gcr.io/cloud-builders/gcloud'
                  entrypoint: 'sh'
                  args:
                    - '-c'
                    - |
                        echo "hello"
      result: submit_build
```

#### Output

```
{
  "create_time": "2021-02-27T16:00:34.292057589Z",
  "finish_time": "2021-02-27T16:00:46.893086Z",
  "id": "6430d5cd-xxxx-xxxx-xxxx-70bdd9b16f03",
  "log_url": "https://console.cloud.google.com/cloud-build/builds/6430d5cd-xxxx-xxxx-xxxx-70bdd9b16f03?project=xxxxxxxxxxxx",
  "logs_bucket": "gs://xxxxxxxxxxxx.cloudbuild-logs.googleusercontent.com",
  "name": "projects/xxxxxxxxxxxx/locations/global/builds/6430d5cd-xxxx-xxxx-xxxx-70bdd9b16f03",
  "project_id": "xxxx",
  "status": "SUCCESS"
}
```

