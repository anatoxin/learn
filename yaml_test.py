import yaml
with open('test.yaml','r') as file:
    data =yaml.safe_load(file)
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
with open('test_edited.yaml','w') as file:
    yaml.dump(data,file ,default_flow_style = False)
