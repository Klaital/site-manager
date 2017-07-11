class User:
    """ A class representing a user interacting with the VITA web services, either via webpage or app """

    # These properties describe the user, and are stored in DynamoDB
    email = 'user@example.org'
    password = 'hashed password here'
    roles = [ 'New User' ] # Valid Values are 'New User', 'Site Coordinator', 'Admin', 'Site Coordinator, Inactive'
