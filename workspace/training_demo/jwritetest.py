import json

data = {}
data['posts'] = []
data['comments'] = []
data['profile'] = []
data['posts'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['comments'].append({
    
})
data['profile'].append({
    
})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)