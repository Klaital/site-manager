
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

    response_body = ''
    response_code = '200'
    if event['queryStringParameters'] == None:
        print("Fetching all sites")
        sites = Site.all()
        sites_json = []
        for site in sites:
            sites_json.append(site.to_json())
        j = ','.join(sites_json)
        response_body = "[ " + j + " ]"
        response_code = '200'
        
    elif 'site-name' in event['queryStringParameters']:
        print("Querying a single site: " + event['queryStringParameters']['site-name'])
        site = Site.find(event['queryStringParameters']['site-name'])
        response_body = site.to_json()
        response_code = '200'
    else:
        response_body = '{"error":"bad request"}'
        response_code = '400'
    
    print ("Compiled Response: " + response_body)
    print ("Response Code: " + response_code)
    
    return {
        'statusCode': response_code,
        'body': response_body,
        'headers': {
            'Content-Type': 'application/json',
        },
    }
    
