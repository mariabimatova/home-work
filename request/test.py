import requests

resp = requests.get("http://mariabimatova.github.io/sample.json")

print("Status code:")
print(resp.status_code)

print("Content type:")
print(resp.headers['content-type'])

if resp.status_code == 200:
    print("Text:")
    print(resp.text)

    print("Json:")
    d = resp.json()
    print(d)

    if "name" in d:
        print("Name")
        print(d["name"])
    else:
        print("No name")