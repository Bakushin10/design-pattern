roledict = {}
admin = "admin"

# it is long and takes 4 lines
if 'owner' in roledict:
    owner = roledict['owner']
else:
    owner = admin

# instead, use python dictionary get method
owner = roledict.get('owner', admin)

