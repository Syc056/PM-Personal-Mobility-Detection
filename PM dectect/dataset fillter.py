import json

with open('sample.json', 'r') as f:
content = json.load(f)

api_list = [ x for x in content['apistats']['2512'].keys()]

print(api_list)

출처: https://hashcode.tistory.com/entry/json-파일에서-특정-데이터를-추출하기 [hashcode]