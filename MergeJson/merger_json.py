import json
a_json = 'json-a.json'
b_json = 'json-b.json'

f = open(b_json,)
b_data = json.load(f)
b_deployment = [i['deploymentName'] for i in b_data]


f1 = open(a_json, )
a_data = json.load(f1)
a_deployment = [i['deploymentName'] for i in a_data]

for xx in b_data:
    if xx['deploymentName'] not in a_deployment:
        if not xx.get('env'):
            b_data.remove(xx)


final_result = []
for m in a_data:
    if m['deploymentName'] in b_deployment:
        for k in b_data:
            if m['deploymentName'] == k['deploymentName']:
                k['resources']['requests']['cpu'] = m['resources']['requests']['cpu']
                final_result.append(k)
    else:
        final_result.append(m)

json_object = json.dumps(final_result, indent = 4)

with open("result.json", "w") as outfile:
    outfile.write(json_object)

