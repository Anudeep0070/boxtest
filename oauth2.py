from boxsdk import Client, OAuth2
from boxsdk.object.events import UserEventsStreamType
import pandas as pd
from connection import connection

def Events():
    events = client.events().get_events(limit=200,stream_position=0,stream_type = UserEventsStreamType.ALL)
    stream_position = events['next_stream_position']
    print("stream position is",stream_position)
    lst_dict = []
    for event in events['entries']:
        #print(f'Got {event.event_type} event that occurred at {event.created_at} by {event.created_by} and source is {event.source}')
        headers = ["Action","Created_at","Created_by","Source"]
        lst_dict.append({"Action":event.event_type,"Created_at":event.created_at,"Created_by":event.created_by,"Source":event.source})

        df = pd.DataFrame(lst_dict)
    return df

def filecreate(data):
    f = data.to_csv("userreport.csv")
#realtime events
'''events = client.events().generate_events_with_long_polling()
for event in events:
    print(f'rGot {event.event_type} event that occurred at {event.created_at}')'''
if __name__ == "__main__":
    client = connection()
    event = Events()
    fp = filecreate(event)
    print(event)
