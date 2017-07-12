import unittest
import sys
import json

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
            'body': None,
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
            'body': None,
        }
        response = LambdaApiHandler.site_apis(event)
        self.assertEqual('200', response['statusCode'])

    def test_create_site(self):
        event = {
            'httpMethod': 'PUT',
            'path': '/site',
            'resource': '/site',
            'pathParameters': None,
            'body': json.dumps({
                "Site": {
                    "name": "tc_lambda_sites_test_create_site",
                    "address": "1234 Fake Street",
                    "hours": "8-3",
                    "is_open": False,
                    "availability_status":"Red"
                }
            }),
        }
        # Make note of the starting site count
        starting_sites = Site.all()
        
        response = LambdaApiHandler.site_apis(event)
        self.assertEqual('200', response['statusCode'])
        self.assertEqual(len(starting_sites) + 1, len(Site.all()))

        # Fetch the site separately and validate the content
        site = Site.find('tc_lambda_sites_test_create_site')
        self.assertIsNotNone(site)
        self.assertEqual('tc_lambda_sites_test_create_site', site.name)
        self.assertEqual("1234 Fake Street", site.address)
        self.assertEqual('Red', site.availability_status)
        self.assertEqual(False, site.is_open)
        self.assertEqual('8-3', site.hours)

        # Cleanup.
        if site != None:
            site.delete()
        # Cleanup validation
        self.assertEqual(len(starting_sites), len(Site.all()), "Failed to clean up the site we created!")

    def test_create_site_nodata(self):
        # Make note of the starting site count
        starting_sites = Site.all()
        
        event = {
            'httpMethod': 'PUT',
            'path': '/site',
            'resource': '/site',
            'pathParameters': None,
            'body': None,
        }
        
        response = LambdaApiHandler.site_apis(event)
        self.assertEqual('400', response['statusCode'])
        # Cleanup validation
        self.assertEqual(len(starting_sites), len(Site.all()), "Failed to clean up the site we created!")

    def test_update_site(self):
        # Make note of the starting site count
        starting_sites = Site.all()
        
        # Create a Site manually first so that we isolate this test to only the Update API
        raw_site = Site()
        raw_site.name = 'tc_lambda_sites_test_update_site'
        raw_site.address = '123 tc_lambda_sites_test_update_site street'
        raw_site.availability_status = 'Green'
        raw_site.hours = '12-12'
        raw_site.is_open = True

        raw_site.save()
        self.assertEqual("123 tc_lambda_sites_test_update_site street", raw_site.address)
        self.assertEqual('tc_lambda_sites_test_update_site', raw_site.name)
        self.assertEqual('Green', raw_site.availability_status)
        self.assertEqual(True, raw_site.is_open)
        self.assertEqual('12-12', raw_site.hours)

        event = {
            'httpMethod': 'POST',
            'path': '/site/tc_lambda_sites_test_update_site',
            'resource': '/site/{sitename}',
            'pathParameters': {
                'sitename': 'tc_lambda_sites_test_update_site'
            },
            'body': json.dumps({
                "Site": {
                    "name": raw_site.name,
                    "address": "123 tc_lambda_sites_test_update_site parkway",
                    "hours": raw_site.hours,
                    "is_open": raw_site.is_open,
                    "availability_status": raw_site.availability_status
                }
            }),
        }
        
        response = LambdaApiHandler.site_apis(event)
        self.assertEqual('', response['body'])
        self.assertEqual('200', response['statusCode'])
        self.assertEqual(len(starting_sites) + 1, len(Site.all()), 'Somehow the Update Site API created a new entry')

        # Fetch the site separately and validate the content
        site = Site.find('tc_lambda_sites_test_update_site')
        self.assertIsNotNone(site)
        self.assertEqual('tc_lambda_sites_test_update_site', site.name)
        self.assertEqual("123 tc_lambda_sites_test_update_site parkway", site.address)
        self.assertEqual('Green', site.availability_status)
        self.assertEqual(True, site.is_open)
        self.assertEqual('12-12', site.hours)

        # Cleanup.
        if raw_site != None:
            raw_site.delete()
        # Cleanup validation
        self.assertEqual(len(starting_sites), len(Site.all()), "Failed to clean up the site we created!")

    def test_delete_site(self):
        # Make note of the starting site count
        starting_sites = Site.all()
        
        # Create a Site manually first so that we isolate this test to only the Update API
        raw_site = Site()
        raw_site.name = 'tc_lambda_sites_test_delete_site'
        raw_site.address = '123 tc_lambda_sites_test_delete_site street'
        raw_site.availability_status = 'Green'
        raw_site.hours = '12-12'
        raw_site.is_open = True
        raw_site.save()
        self.assertEqual("123 tc_lambda_sites_test_delete_site street", raw_site.address)
        self.assertEqual('tc_lambda_sites_test_delete_site', raw_site.name)
        self.assertEqual('Green', raw_site.availability_status)
        self.assertEqual(True, raw_site.is_open)
        self.assertEqual('12-12', raw_site.hours)

        event = {
            'httpMethod': 'DELETE',
            'path': '/site/tc_lambda_sites_test_delete_site',
            'resource': '/site/{sitename}',
            'pathParameters': {
                'sitename': 'tc_lambda_sites_test_delete_site'
            },
            'body': None,
        }
        
        response = LambdaApiHandler.site_apis(event)
        self.assertEqual('', response['body'])
        self.assertEqual('200', response['statusCode'])
        self.assertEqual(len(starting_sites), len(Site.all()), 'The Delete Site API failed to destroy the record it created.')

        # Fetch the site separately and validate the content
        site = Site.find('tc_lambda_sites_test_delete_site')
        self.assertIsNone(site)
        
        # Cleanup.
        if raw_site != None:
            raw_site.delete()
        # Cleanup validation
        self.assertEqual(len(starting_sites), len(Site.all()), "Failed to clean up the site we created!")

if __name__ == '__main__':
    unittest.main()
