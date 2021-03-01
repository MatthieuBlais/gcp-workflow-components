### GCS WRITE JSON

Upload a JSON document to GCS

#### Deploy

```
gcloud workflows deploy workflow-component-gcs-write-json \
--source=workflow.yaml \ 
[--location=MY_LOCATION]
[--service-account=MY_SERVICE_ACCOUNT@MY_PROJECT.IAM.GSERVICEACCOUNT.COM]
```

#### Parameters

- bucket: Bucket name where the JSON file will be stored
- key: Path of the JSON file in the bucket
- object: JSON object and content of the new file

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
          object:
            hello: world
      result: file_content
```


#### Output

```
{
    "bucket": "xxx-xxx-deployments",
    "name": "testfolder/",
    "size": "0"
    ...
}
```

