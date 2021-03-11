### Kubernetes Batch Job

Trigger a Kubernetes Job (kind: Job) and wait for its completion.


**Limitation:** Currently limited to 30min job due to Timeout of the experimental API.
**TODO**: Create a new component get-job (can get from the step wait_for_completion) to workaround this timeout issue.

#### Deploy

```
gcloud workflows deploy workflow-component-kubernetes-trigger-job \
--source=workflow.yaml \ 
[--location=MY_LOCATION]
[--service-account=MY_SERVICE_ACCOUNT@MY_PROJECT.IAM.GSERVICEACCOUNT.COM]
```

#### Parameters

- cloudbuild_component: Name of the Workflow used for cloudbuild jobs
- project_id: GCP Project
- workflow_id: Name of the workflow calling this component. You can use the built-in [environment variable](https://cloud.google.com/workflows/docs/reference/environment-variables) GOOGLE_CLOUD_WORKFLOW_ID
- workflow_exec: Unique execution ID. Currently not available as built-in environment variable.
- job_name: Name of your job. As in Kubernetes, all job names must be unique, the job_name is modified during runtime to concatenate workflow_id, workflow_exec and job_name.
- compute_zone: GKE cluster zone
- cluster_name: GKE cluster name
- job_definition_location: GCS location of the Job YAML file.
- gcs_log_bucket: Bucket used by the component workflow to share data/logs between each step.
- gcs_log_prefix: Prefix used by the component workflow to share data/logs between each step.
- wait: Asynchronous execution (false) or wait for the job to complete before exiting. Current timeout for parallel workflow execution is 30min. If you job is longer than 30min, you should use wait: false

#### Example

Upload the Pi job example from the official [Kubernetes documentation](https://kubernetes.io/docs/concepts/workloads/controllers/job/) to a GCS bucket.

```
steps:
  - containerdemo:
      call: experimental.executions.run
      args: 
        workflow_id: "workflow-component-kubernetes-job"
        argument:
          cloudbuild_component: "workflow-component-cloudbuild-job"
          cluster_name: "mycluster"
          compute_zone: "asia-southeast-1"
          gcs_log_bucket: "mybucket"
          gcs_log_prefix: "_logs/location/"
          job_definition_location: "gs://bucket/key.yaml"
          job_name: "mypi
          project_id: "gs://bucket/key.yaml"
          workflow_id: "myworkflow"
          workflow_exec: "uuid"
      result: result
```


#### Output

```
{
  "apiVersion": "batch/v1",
  "kind": "Job",
  "metadata": {
    "creationTimestamp": "2021-02-27T15:57:27Z",
    "name": "myworkflow-uuid-mypi",
    "namespace": "default",
    "resourceVersion": "786098",
    "selfLink": "/apis/batch/v1/namespaces/default/jobs/myworkflow-uuid-mypi",
    "uid": "647eeff6-xxxx-xxxx-xxxx-d450161ae392"
  },
  "spec": {
    "backoffLimit": 4,
    "completions": 1,
    "parallelism": 1,
    "selector": {
      "matchLabels": {
        "controller-uid": "647eeff6-xxxx-xxxx-xxxx-d450161ae392"
      }
    },
    "template": {
      "metadata": {
        "annotations": {
          "seccomp.security.alpha.kubernetes.io/pod": "runtime/default"
        },
        "creationTimestamp": null,
        "labels": {
          "controller-uid": "647eeff6-xxxx-xxxx-xxxx-d450161ae392",
          "job-name": "myworkflow-uuid-mypi"
        }
      },
      "spec": {
        "containers": [
          {
            "command": [
              "perl",
              "-Mbignum=bpi",
              "-wle",
              "print bpi(2000)"
            ],
            "image": "perl",
            "imagePullPolicy": "Always",
            "name": "pi",
            "resources": {
              "limits": {
                "cpu": "500m",
                "ephemeral-storage": "1Gi",
                "memory": "2Gi"
              },
              "requests": {
                "cpu": "500m",
                "ephemeral-storage": "1Gi",
                "memory": "2Gi"
              }
            },
            "securityContext": {
              "capabilities": {
                "drop": [
                  "NET_RAW"
                ]
              }
            },
            "terminationMessagePath": "/dev/termination-log",
            "terminationMessagePolicy": "File"
          }
        ],
        "dnsPolicy": "ClusterFirst",
        "restartPolicy": "Never",
        "schedulerName": "default-scheduler",
        "securityContext": {},
        "terminationGracePeriodSeconds": 30
      }
    }
  },
  "status": {
    "completionTime": "2021-02-27T15:59:48Z",
    "conditions": [
      {
        "lastProbeTime": "2021-02-27T15:59:48Z",
        "lastTransitionTime": "2021-02-27T15:59:48Z",
        "status": "True",
        "type": "Complete"
      }
    ],
    "startTime": "2021-02-27T15:57:27Z",
    "succeeded": 1
  }
}
```

