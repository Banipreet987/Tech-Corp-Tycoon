import json
data = {
    "name":"killer",
    "age":23
}
with open("data10.json","w") as file : acc = json.dump(data,file,indent=4)
