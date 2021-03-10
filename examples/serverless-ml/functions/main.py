import base64
from google.cloud.workflows.executions_v1beta.services.executions import ExecutionsClient
from google.cloud.workflows.executions import Execution, CreateExecutionRequest
import json
import uuid

client = ExecutionsClient()

def trigger(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    message = json.loads(base64.b64decode(event['data']).decode('utf-8'))
    args = message.get("arguments", {})
    args["execution_id"] = uuid.uuid1().hex
    execution = Execution(
        argument=json.dumps(args)
    )
    parent = message["workflow"]
    response = client.create_execution(parent=parent, execution=execution)
    return args