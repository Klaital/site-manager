# Operations Requirements / Cloudformation

The CF template needs to create the following:

1. VPC 'vita-app-<env>'
2. 2 Subnets, Public and Private
3. DynamoDB table 'vita-app-sites-<env>'
4. DynamoDB table 'vita-app-users-<env>'
5. DynamoDB table 'vita-app-sessions-<env>'

6. API Gateway pointing to the lambdas
7. Lambdas for the required APIs

8. S3 Bucket for static content
9. S3 Static content 
  - Images
  - Web page HTML (for login/logout/etc)
  - CSS for the static pages
