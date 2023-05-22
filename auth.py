
from boxsdk import OAuth2, Client

auth = OAuth2(
    client_id='all141k6ieixjsv11a0z79nams8edaj2',
    client_secret='9mtjMleAyz490H5Q5zobaB0GvrceGeSG'
)
auth_url, csrf_token = auth.get_authorization_url('https://your.domain.com/path')

#AKsXB9bc4P6Ppu5LKJJVsGFwTXPROFGT
print(auth.authenticate('QzyJdgouOPh7raUxsTMENqQiA2qizxvy'))
client = Client(auth)
print(client)
print(auth)