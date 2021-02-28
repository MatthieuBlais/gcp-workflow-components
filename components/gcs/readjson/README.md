### GCS JSON API

Download and Parse a JSON file from GS

#### Deploy

`
gcloud workflows deploy workflow-component-gcs-readjson \
--source=workflow.yaml \ 
[--location=MY_LOCATION]
[--service-account=MY_SERVICE_ACCOUNT@MY_PROJECT.IAM.GSERVICEACCOUNT.COM]
`

#### Parameters

- bucket: Bucket name where the JSON file is stored
- key: Path of the JSON file in the bucket

#### Example


```
steps:
  - download:
      call: experimental.executions.run
      args:
        workflow_id: "workflow-component-gcs-readjson"
        argument:
          bucket: "mybucket"
          key: "path/key.json"
      result: file_content
```


#### Output

```
{
  "key1": "value1",
  "key2": "value2"
}
```

