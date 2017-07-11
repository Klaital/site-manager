class Site:
    """ A class representing a VITA tax prep location. It is managed by a Site Coordinator. """

    # These properties describe the user, and are stored in DynamoDB
    name = 'VITA tax prep site'
    address = '123 Fake Street, San Antonio, TX'
    hours = '9-5'
    is_open = False
    availability_status = 'green'

    @staticmethod
    def find(name)
        """ Look up the Site in the database """
        # TODO: implement Site.find
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('vita-sites')
        response = table.get_item(
            Key = {
                'site-name': name
            }
        )
        item = response['Item']
        print item
    
    @staticmethod
    def all
        """ Look up all Sites in the database """
        # TODO: implement Site.all

    def save
        """ Save all fields to the database """
        # TODO: implement Site#save
    