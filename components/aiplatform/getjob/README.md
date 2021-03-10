### AI Platform Get Training Job

Fetch the latest details of a training job. Useful to check job status.

#### Deploy

```
gcloud workflows deploy workflow-component-aiplatform-getjob \
--source=workflow.yaml \ 
[--location=MY_LOCATION]
[--service-account=MY_SERVICE_ACCOUNT@MY_PROJECT.IAM.GSERVICEACCOUNT.COM]
```

#### Parameters

- projectId: Training job Project ID. If same as Workflow, you can use ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
- jobId: Id of the training job.

#### Example

```
steps:
- train_model:
    call: experimental.executions.run
    args: 
        workflow_id: "workflow-component-aiplatform-job"
        argument:
            projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
            wait: false
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
- get_status:
    call: experimental.executions.run
    args: 
        workflow_id: "workflow-component-aiplatform-jobstatus"
        argument:
            projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
            jobId: ${job.jobId}
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


