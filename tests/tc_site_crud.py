import unittest
import sys
sys.path.insert(0, ".")
from models.site import Site

class TCSiteCrud(unittest.TestCase):
    def test_get_one(self):
        site = Site.find('test_site_1')
        self.assertEqual("123 Fake Street", site.address)
        self.assertEqual('test_site_1', site.name)
        self.assertEqual('Yellow', site.availability_status)
        self.assertEqual(False, site.is_open)
        self.assertEqual('8-4', site.hours)

    def test_get_all(self):
        sites = Site.all()
        self.assertEqual(1, len(sites), 'Incorrect number of sites fetched during scan')
        self.assertEqual("123 Fake Street", sites[0].address)

    def test_create_new(self):
        site = Site()
        site.name = 'test_site_2'
        site.address = '234 Fake Street'
        site.availability_status = 'Green'
        site.hours = '1-2'
        site.is_open = True

        result = site.save()
        self.assertTrue(result, 'Failed to save the new site')
        # Validate that the record was indeed written out to the DB
        self.assertEqual(2, len(Site.all()))

        # Now fetch the site data back out
        site2 = Site.find('test_site_2')
        self.assertEqual("234 Fake Street", site.address)
        self.assertEqual('test_site_2', site.name)
        self.assertEqual('Green', site.availability_status)
        self.assertEqual(True, site.is_open)
        self.assertEqual('1-2', site.hours)
        
        # Delete the newly created site
        site2.delete()
        self.assertEqual(1, len(Site.all()))
    

if __name__ == '__main__':
    unittest.main()
