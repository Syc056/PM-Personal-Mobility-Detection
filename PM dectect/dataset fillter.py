import json

with open('sample.json', 'r') as f:
content = json.load(f)

api_list = [ x for x in content['person']['??'].keys()]

print(api_list)

