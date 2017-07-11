
import json
import boto3

class Site:
    """ A class representing a VITA tax prep location. It is managed by a Site Coordinator. """

    # These properties describe the user, and are stored in DynamoDB
    name = 'VITA tax prep site'
    address = '123 Fake Street, San Antonio, TX'
    hours = '9-5'
    is_open = False
    availability_status = 'green'

    @staticmethod
    def find(name):
        """ Look up the Site in the database """
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('vita-sites')
        response = table.get_item(
            Key = {
                'site-name': name
            }
        )
        item = response['Item']
        site = Site()
        site.name = item['site-name']
        site.address = item['address']
        site.hours = item['hours']
        site.is_open = item['is_open']
        site.availability_status = item['availability_status']
        return site
    
    @staticmethod
    def all():
        """ Look up all Sites in the database """
        sites = []
        dynamodb = boto3.resource('dynamodb')
        response = dynamodb.Table('vita-sites').scan()
        for item in response['Items']:
            site = Site()
            site.name = item['site-name']
            site.address = item['address']
            site.hours = item['hours']
            site.is_open = item['is_open']
            site.availability_status = item['availability_status']
            sites.append(site)
        
        return sites

    def save(self):
        """ Save all fields to the database """
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('vita-sites')
        table.put_item(
            Item = {
                'site-name': self.name,
                'address': self.address,
                'hours': self.hours,
                'is_open': self.is_open,
                'availability_status': self.availability_status,
            }
        )

        return True

    def delete(self):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('vita-sites')
        table.delete_item(
            Key = {
                'site-name': self.name
            }
        )
        return True
    
    def to_json(self):
        return json.dumps(self.__dict__)

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
    
