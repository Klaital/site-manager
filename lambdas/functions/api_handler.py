
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

class LambdaApiHandler:
    @staticmethod
    def site_apis(event):
        response_body = ''
        response_code = '200'

        site_name = None if event['pathParameters'] == None else event['pathParameters']['sitename']
        
        if event['httpMethod'] == 'GET':
            if site_name == None:
                # Fetch all sites
                print("Fetching all sites")
                sites = Site.all()
                sites_json = []
                for site in sites:
                    sites_json.append(site.to_json())
                j = ','.join(sites_json)
                response_body = "[ " + j + " ]"
                response_code = '200'
            else:
                # Fetch single site
                print("Querying a single site: " + site_name)
                site = Site.find(site_name)
                response_body = site.to_json()
                response_code = '200'
        
        elif event['httpMethod'] == 'PUT':
            # Create a new site
            site = Site()
            # TODO: Set the site values based on the http body
            if site.save():
                response_body = '{"error":"PUT /sitenot implemented yet"}'
                response_code = '500'
            else:
                response_body = '{"error":"failed to create site"}'
                response_code = '400'
        
        elif event['httpMethod'] == 'POST':
            # Update an existing site status
            if site_name == None:
                response_body = '{"error":"bad request. Please specify the site-name path parameter"}'
                response_code = '400'
            else:
                site = Site.find(site_name)
                # TODO: Set the site values based on the http body
                if site.save():
                    response_body = '{"error":"POST /site/{sitename} not implemented yet"}'
                    response_code = '500'
                else:
                    response_body = '{"error":"failed to update site"}'
                    response_code = '400'
        
        elif event['httpMethod'] == 'DELETE':
            # Destroy an existing Site
            if site_name == None:
                response_body = '{"error":"bad request. Please specify the site-name path parameter"}'
                response_code = '400'
            else:
                site = Site.find(site_name)
                if site.delete():
                    response_body = '{"error":"DELETE /site/{sitename} not implemented yet"}'
                    response_code = '500'
                else:
                    response_body = '{"error":"failed to delete site"}'
                    response_code = '400'
        else:
            response_body = '{"error":"bad request"}'
            response_code = '400'
        

        return {
            'statusCode': response_code,
            'body': response_body,
            'header': {
                'Content-Type': 'application/json'
            },
        }

    @staticmethod
    def user_apis(event):
        response_body = '{"error":"/user APIs not implemented yet"}'
        response_code = '404'
        return {
            'body': response_body,
            'statusCode': response_code,
            'header': {
                'Content-Type': 'application/json'
            },
        }

    @staticmethod
    def session_apis(event):
        response_body = '{"error":"/session APIs not implemented yet"}'
        response_code = '404'
        return {
            'body': response_body,
            'statusCode': response_code,
            'header': {
                'Content-Type': 'application/json'
            },
        }


def lambda_handler(event, context):
    ''' Lambda Entrypoint '''
    print("Received event: " + json.dumps(event, indent=2))

    response_body = ''
    response_code = '200'
    
    if event['path'].startswith('/site'):
        """ Handle Site management APIs """
        return LambdaApiHandler.site_apis(event)
    elif event['path'].startswith('/user'):
        """ Handle User management APIs """
        return LambdaApiHandler.user_apis(event)
    elif event['path'].startswith('/session'):
        """ Handle Session management APIs (login/logout) """
        return LambdaApiHandler.session_apis(event)
    
