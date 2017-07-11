import boto3
import json

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
