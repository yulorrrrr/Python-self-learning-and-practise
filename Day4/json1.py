
#translate python to json
import json
data = [{"name" : "Christine", "age": 11}]
json_str = json.dumps(data, ensure_ascii= False)
print(json_str)

#translate json to python: json.loads 

