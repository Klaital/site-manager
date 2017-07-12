import unittest
import sys
sys.path.insert(0, ".")
from models.site import Site
from functions.api_handler import LambdaApiHandler

class TCLambdaSites(unittest.TestCase):
    def test_list_sites(self):
        event = {
            'httpMethod': 'GET',
            'path': '/site',
            'resource': '/site',
            'pathParameters': None,
        }
        response = LambdaApiHandler.site_apis(event)
        self.assertEqual('200', response['statusCode'])
        
    def test_get_site_details(self):
        event = {
            'httpMethod': 'GET',
            'path': '/site/test_site_1',
            'resource': '/site/{sitename}',
            'pathParameters': {
                'sitename': 'test_site_1'
            },
        }
        response = LambdaApiHandler.site_apis(event)
        self.assertEqual('200', response['statusCode'])

if __name__ == '__main__':
    unittest.main()
