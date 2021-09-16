import json
import pandas as pd


def report(file1,file2):
    with open(file1) as f:
        dats = json.load(f)
    dfvalues=pd.DataFrame(dats['values'])

    with open(file2) as f:
        data = json.load(f)

    for i in data['tests']:
        i['value']=dfvalues.value[dfvalues['id'] == i['id']].item()
        if 'values' in i and type(i['values']) is list:
            for n in range(len(i['values'])):
                i['values'][n]['value']=dfvalues.value[dfvalues['id'] == i['values'][n]['id']].item()
                if 'values' in i['values'][n]:
                    for u in range(len(i['values'][n]['values'])):
                        if 'values' in i['values'][n]['values'][u] :
                            for r in range(len(i['values'][n]['values'][u]['values'])):
                                i['values'][n]['values'][u]['values'][r]['value']=dfvalues.value[dfvalues['id'] == i['values'][n]['values'][u]['values'][r]['id']].item()
    print(data)
    
    data_json = json.dumps(data)

    with open("report.json", "w") as my_file:
        my_file.write(data_json)
report('values.json','tests.json')