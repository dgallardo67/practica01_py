from xml.dom.minidom import Element


user = {
    "name": ["Jesus", "Caro"],
    "Edad": 29,
    "Profesion": "Ingeniero"
}

#print(user)

for key in user:
    print(f'element[{key}]: {user[key]}')