### AI Platform Training Job

Trigger a training job on the AI Platform and can wait for its completion

#### Deploy

```
gcloud workflows deploy workflow-component-aiplatform-job \
--source=workflow.yaml \ 
[--location=MY_LOCATION]
[--service-account=MY_SERVICE_ACCOUNT@MY_PROJECT.IAM.GSERVICEACCOUNT.COM]
```

#### Parameters

- projectId: Training job Project ID. If same as Workflow, you can use ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
- job: [Job object](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.jobs#Job)
- wait: boolean. Wait for the job to complete or not. If you call this component as part of another workflow, note the current GCP hard limit is a timeout of 30min. If you training job is longer, you should set wait to false and build the waiting logic as part of your main workflow.


##### Job example

{
    "jobId": "serverlesstesting",
    "trainingInput": {
        "scaleTier": "CUSTOM",
        "masterType": "n1-standard-4",
        "region": "asia-southeast1",
        "jobDir": "gs://xxxx-306xxx-ml",
        "masterConfig": {
            "imageUri": "gcr.io/xxxx-306xxx/serverlessml_training_container"
        }
    }
}


#### Example

```
steps:
- train_model:
    call: experimental.executions.run
    args: 
        workflow_id: "workflow-component-aiplatform-job"
        argument:
            projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
            job:
                jobId: serverlesstesting
                trainingInput:
                    jobDir: gs://xxxx-306xxx-ml
                    masterConfig:
                        imageUri: gcr.io/xxxx-306xxx/serverlessml_training_container
                    masterType: n1-standard-4
                    region: asia-southeast1
                    scaleTier: CUSTOM
    result: job
```

#### Output

Output is the [Job object](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.jobs#Job)

```
{
    "createTime":"2021-03-04T16:02:51Z",
    "endTime":"2021-03-04T16:04:48Z",
    "errorMessage":"Job is cancelled by the user.",
    "etag":"AghtSvPU7IA=",
    "jobId":"serverlesstesting",
    "startTime":"2021-03-04T16:03:47Z",
    "state":"CANCELLED",
    "trainingInput":{
        "jobDir":"gs://freel-306204-ml",
        "masterConfig":{
            "imageUri":"gcr.io/freel-306204/serverlessml_training_container"
        },
        "masterType":"n1-standard-4",
        "region":"asia-southeast1",
        "scaleTier":"CUSTOM"
    },
    "trainingOutput":{
        "consumedMLUnits":0.07
    }
}
```


