import requests


def get_intelligence(hero_name):
    token = "2619421814940190"

    request_one = f"https://www.superheroapi.com/api.php/{token}/search/{hero_name}"
    resp = requests.get(request_one)
    if resp.status_code != 200 or resp.headers['content-type'] != "application/json":
        return None

    d = resp.json()
    id = d['results'][0]['id']

    request_two = f"https://www.superheroapi.com/api.php/{token}/{id}/powerstats"
    resp = requests.get(request_two)
    if resp.status_code != 200 or resp.headers['content-type'] != "application/json":
        return None

    d = resp.json()
    intel = d['intelligence']
    return int(intel)


names = ["Hulk", "Captain america", "Thanos"]
hero_intels = []
for hero_name in names:
    hero_intel = get_intelligence(hero_name)

    d = {"name": hero_name, "intelligence": hero_intel}
    hero_intels.append(d)
hero_intels.sort(key=lambda x: x['intelligence'])
print('the most intelligent superhero:')
print(hero_intels[-1])
