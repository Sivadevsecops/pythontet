import json

def lambda_handler(event, context):
    # TODO implement
    print("Executing Lambda Test Function")
    print ("testing change deployment")
    print("step 3")
    print("New Code Deployment done")
    print("Dummy"
    print("step 4")
    print("Demo for Siva")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
