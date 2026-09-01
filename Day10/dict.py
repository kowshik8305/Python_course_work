data["name"]
'jagadeesh'
data["batch"]
64
64 in data
False
data.get("age","key is not present")
'key is not present'
data.get("course","key is not present")
'PFS'
data["batch"]=789
data
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS'}
data["skills"]=["Python","sql","flask"]
data
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask']}
data.pop[age]
data["age"]=23
     
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'age': 21}
data.update({"phone":7893952075,"email":"jagadeesh.vinnakota@gmail.com","surname":"vinnakota"})
     
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'age': 21, 'phone': 7893952075, 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
data.pop("age")
     
21
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'phone': 7893952075, 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
data.pop("phone")
     
7893952075
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
data.popitem("surname")
     
del data['name']
     
data
     
{'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
data.popitem()
     
('surname', 'vinnakota')
data
     
{'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'email': 'jagadeesh.vinnakota@gmail.com'}
data.popitem()
     
('email', 'jagadeesh.vinnakota@gmail.com')
data.popitem()

('skills', ['Python', 'sql', 'flask'])
data
     
{'batch': 789, 'course': 'PFS'}
data.popitem()

('course', 'PFS')
data
     
{'batch': 789}
data.popitem()

('batch', 789)
data
     
{}
data.clear()
     
data
     
{}
data
     
{}
data={'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'age': 21, 'phone': 7893952075, 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
     
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'age': 21, 'phone': 7893952075, 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
data.keys()
     
dict_keys(['name', 'batch', 'course', 'skills', 'age', 'phone', 'email', 'surname'])
data.values()
     
dict_values(['jagadeesh', 789, 'PFS', ['Python', 'sql', 'flask'], 21, 7893952075, 'jagadeesh.vinnakota@gmail.com', 'vinnakota'])
data,items()
     
data.items()
     
dict_items([('name', 'jagadeesh'), ('batch', 789), ('course', 'PFS'), ('skills', ['Python', 'sql', 'flask']), ('age', 21), ('phone', 7893952075), ('email', 'jagadeesh.vinnakota@gmail.com'), ('surname', 'vinnakota')])
sorted.data()
sorted(data)
     
['age', 'batch', 'course', 'email', 'name', 'phone', 'skills', 'surname']
sorted(data,reverse=True)
     
['surname', 'skills', 'phone', 'name', 'email', 'course', 'batch', 'age']
max(data)
     
'surname'
min(data)
     
'age'
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'age': 21, 'phone': 7893952075, 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
dat["age"]
     
data["age"]
     
21
data.get("age")
     
21
data.setdefault("age",0)
     
21
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'age': 21, 'phone': 7893952075, 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
data.setdefault("name",'')
     
'jagadeesh'
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'age': 21, 'phone': 7893952075, 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
len(data)
     
8
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'age': 21, 'phone': 7893952075, 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
d
...      
{'a': 0, 'b': 0}
