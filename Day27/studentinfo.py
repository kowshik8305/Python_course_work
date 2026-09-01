'''import json
with open('data.json','r') as file:
    data=json.load(file)
data['username']='kowshik'
data['skils'].append('jango')

with open('data.json','w') as file:
    data=json.dump(file)

json_data=json.dumps(student)

print(json_data)

student=json.loads(json_data)
print(student)
print(type(student))'''