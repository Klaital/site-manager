
import json
import boto3

from models.site import Site

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''
    print("Received event: " + json.dumps(event, indent=2))

    sites = Site.all()
    print("Got %s sites from Dynamo" % len(sites))
    sites_json = []
    
    for site in sites:
        sites_json.append(site.to_json())

    j = ','.join(sites_json)
    j = "[ " + j + " ]"
    print ("Compiles Response: " + j)
    return {
        'statusCode': '200',
        'body': j,
        'headers': {
            'Content-Type': 'application/json',
        },
    }
    
