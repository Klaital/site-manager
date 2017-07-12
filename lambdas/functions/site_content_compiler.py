import json
import boto3
from models.site import Site

class SiteContentCompiler:
    @staticmethod
    def compileSiteJson(sites):
        if len(sites) == 0:
            return None

        s3_bucket = 'vita-static-content-dev'
        s3_key = 'sites.json'
        s3 = boto3.resource('s3')
        
        json_str = ",".join([site.to_json() for site in sites])
        json_str = "[" + json_str + "]"
        response = s3.Bucket(s3_bucket).put_object(Key=s3_key, Body=json_str)
        response.Acl().put(ACL='public-read')
        print("Upload complete. Response: " + response.key)
        return True

def lambda_handler(event, context):
    print("Recompiling All Sites static JSON")

    print("Uploading to S3")
    SiteContentCompiler.compileSiteJson(Site.all())
    
