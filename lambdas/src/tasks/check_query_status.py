import boto3

from decorators import with_logger

client = boto3.client("athena")


@with_logger
def handler(event, context):
    execution_details = client.get_query_execution(
        QueryExecutionId=event
    )["QueryExecution"]

    return {
        "State": execution_details["Status"]["State"],
        "Reason": execution_details["Status"].get("StateChangeReason", "n/a")
    }