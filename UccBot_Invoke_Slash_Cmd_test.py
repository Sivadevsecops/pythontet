import json
import boto3

depclient = boto3.client('codedeploy')

def lambda_handler(event, context):
    #Read the DeploymentId & LifecycleEventHookExecutionId from the event payload
    print("Printing DeploymentID and lifecycleEventHookExecutionIds")
    deploymentIds = event['DeploymentId']
    lifecycleEventHookExecutionIds = event['LifecycleEventHookExecutionId']
    
    print(deploymentIds)
    print(lifecycleEventHookExecutionIds)
    
    ## Validation to be done
    print("Validation to be done")
    
    ## Returning Data to code deploy
    print("Returning Response to Code Deploy")
    response = depclient.put_lifecycle_event_hook_execution_status(
    deploymentId=deploymentIds,
    lifecycleEventHookExecutionId=lifecycleEventHookExecutionIds,
    status='Succeeded'
    )
    
    print("Printing Response")
    print(response)
    
    return 'completed execution'
