### List GCS objects

List all objects in a GCS Bucket

#### Deploy

```
gcloud workflows deploy workflow-component-gcs-list-objects \
--source=workflow.yaml \ 
[--location=MY_LOCATION]
[--service-account=MY_SERVICE_ACCOUNT@MY_PROJECT.IAM.GSERVICEACCOUNT.COM]
```

#### Parameters

- bucket: Bucket name
- query: API parameters as defined in [API Ref](https://cloud.google.com/storage/docs/json_api/v1/objects/list)

#### Example


```
steps:
  - download:
      call: experimental.executions.run
      args:
        workflow_id: "workflow-component-gcs-readjson"
        argument:
          bucket: "xxx-xxx-deployments"
          query: 
            prefix: ""
            maxResults: 1
      result: objects_list
```



#### Output

```
{
  "items": [
    {
      "bucket": "xxx-xxx-deployments",
      "name": "testfolder/",
      "size": "0"
      ...
    }
  ],
  "nextPageToken": "Cgt0ZXN0Zm9sZGVyLw=="
}
```

