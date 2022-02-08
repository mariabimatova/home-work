import requests
filename = 'data1.txt'

# в переменную токен надо записать код токен полученный через яндекс
token = ""

h = {'Authorization': f'OAuth {token}'}
address = "https://cloud-api.yandex.net/v1/disk/resources/upload"
p = {'path': filename, 'overwrite': True}
resp = requests.get(url=address, headers=h, params=p)
if resp.status_code == 200:
    d = resp.json()
    a = d['href']
    print(a)

    with open(filename) as f:
        lines = f.readlines()
    text = ''
    for i in lines:
        text = text + i
    answer = requests.put(url=a, data=text)
    if answer.status_code == 201:
        print('The file uploaded to Yandex')
    else:
        print(answer.status_code)
        print('Second request: The file not uploaded to Yandex')
else:
    print(resp.status_code)
    print(resp.text)
    print('The file not uploaded to Yandex')
