from boxsdk import OAuth2, Client

auth = OAuth2(
    client_id='all141k6ieixjsv11a0z79nams8edaj2',
    client_secret='9mtjMleAyz490H5Q5zobaB0GvrceGeSG',
    access_token='pRPcLTyGjnkgZ1qaSTkORtsSaicp7ICg'
)
client = Client(auth)

user = client.user().get()
print(f'The current user ID is {user.id}')

#https://api.box.com/2.0/folders
#https://ciscoadmin.app.box.com/
'''subfolder = client.folder('199823001707').create_subfolder('My Workflow')
print(f'Created subfolder with ID {subfolder.id}')'''
folder = client.folder(folder_id='199823001707').get()
print(f'Folder "{folder.name}" has {folder.item_collection["total_count"]} items in it')

#list all metadata

file_metadata = client.file(file_id='1183050413409').get_all_metadata()
for instance in file_metadata:
    print(instance)

#get particular metadata

metadata = client.file(file_id='1183050413409').metadata(scope='enterprise', template='doccentralcore').get()
print(metadata["$id"],metadata["$template"])

#create task

tasks = client.file(file_id='1183050413409').get_tasks()
for task in tasks:
    print(f'Task ID is {task.id} and the type is {task.type}')