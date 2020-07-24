import json 
with open('test.json','r') as file:
    data =json.load(file)
print (data)
print (data['user'].keys())

if 'saint' not in data['user'].values():
    print ('saint not present')

user = data['user']
for role in user['roles']:
        print (role)
print (user['location'])

#Ensure the dictionary is accessiable before modifccation by printing 
user['location']['city']='bangalore'
with open('test_edited.json','w') as file:
    json.dump(data,file ,indent=4)
