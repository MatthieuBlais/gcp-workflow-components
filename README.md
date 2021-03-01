# gcp-workflow-components

Ready-to-use components for GCP Workflow.

#### Problem definition

GCP Workflow has been GA for 2 months at the time of writing these components. Currently, we have to write our own subworkflows to integrate with other GCP services. This increases the complexity of the workflow definitions and force to copy/paste integrations across workflows. 

The goal of these components is to have common integration for calling other GCP services that can be re-used across workflows. This is a pattern similar to AWS Step Function and we could bet GCP will come-up with their own components in the future.

**Note:** Calling a workflow from another workflow is still an [experimental feature](https://cloud.google.com/workflows/docs/reference/stdlib/experimental.executions/run) at the moment.

 
### Integrations

- Cloudbuild job: Trigger a CloudBuild job and wait for it to complete.
- GCS JSON Read: Read a JSON object from Google Storage.
- GCS List Objects: List objects from a GCS bucket.
- GKE Batch Job: Execute a Kubernetes batch job on GKE.
