from flask import Flask, jsonify, request,send_file, render_template
from boxsdk.object.events import UserEventsStreamType
import pandas as pd
from connection import connection
app = Flask(__name__)


@app.route('/reports')
def reports():
    source = request.args.get('source')
    id = request.args.get('id')
    result = Events(source,id)
    #return dict(result)
    #return result.to_html(header="true", table_id="table")
    path = "userreport.csv"
    #download_file()
    return send_file(path, as_attachment=True)
    #return render_template('download.html')

def Events(source,id):
    events = client.events().get_events(limit=200,stream_position=0,stream_type = UserEventsStreamType.ALL)
    stream_position = events['next_stream_position']
    print("stream position is",stream_position)
    lst_dict = []
    for event in events['entries']:
        if((source=="File" or source=="Folder") and id != 'null'):
            if str(event.source).__contains__(id):
                lst_dict.append({"Action":event.event_type,"Created_at":event.created_at,"Created_by":event.created_by,"Source":event.source})
        else:
            lst_dict.append({"Action": event.event_type, "Created_at": event.created_at, "Created_by": event.created_by,
                             "Source": event.source})
    df = pd.DataFrame(lst_dict)
    '''if source == "File":
        print(df['Source'])
        if (df['Source'].str.contains("File")):
            print("df is",df)
    elif source == "Folder":
        if (df['Source'].str.contains("Folder")):
            print("df is", df)'''

    filecreate(df)
    return df

def filecreate(data):
    f = data.to_csv("userreport.csv")
#realtime events
'''events = client.events().generate_events_with_long_polling()
for event in events:
    print(f'rGot {event.event_type} event that occurred at {event.created_at}')'''

if __name__ == '__main__':
    client = connection()
    app.run()