import yaml
from boxsdk import Client, OAuth2
def connection():
    with open('config.yaml','r') as f:
        try:
            conn = yaml.safe_load(f)
            #print(data)
        except yaml.YAMLError as exc:
            print(exc)
    auth = OAuth2(
        client_id=conn['clientid'],
        client_secret=conn['clientsecret'],
        access_token=conn['accesstoken']
    )
    client = Client(auth)
    return client