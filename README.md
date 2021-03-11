# gcp-workflow-components

Ready-to-use components for GCP Workflow.

GCP Workflow has been GA since January 2021. Currently, we have to write our own subworkflows to integrate with other GCP services. This increases the complexity of the workflow definitions and force to copy/paste integrations across workflows. 

The goal of these components is to have common integration for calling other GCP services that can be re-used across workflows. This is a pattern similar to AWS Step Function and we can foresee GCP will come-up with their own components in the future.

**Note:** Calling a workflow from another workflow is still an [experimental feature](https://cloud.google.com/workflows/docs/reference/stdlib/experimental.executions/run) at the moment.

 
### Integrations

In the components folder, you can find custom integrations for:

**AI Platform**: 
- Trigger Training job
- Get status of a training job
**BigQuery**:
- Trigger a job
- Trigger a query
**CloudBuild**:
- Trigger a build
**Firestore**:
- Delete a document
- Read a document
- Write a document
**CloudFunction**:
- GET invocation
- POST invocation
**GCS**:
- Read a JSON object
- List objects
- Write JSON object
**GKE**:
- Trigger batch Job



### Examples

**Serverless ML Pipeline**: Extract datasets from BigQuery and trigger a ML training job.
**Serverless Batch Job**: Execute a Batch job using GKE Autopilot.