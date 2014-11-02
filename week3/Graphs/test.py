import requests


def get_following_for(name):
    following = requests.get("https://api.github.com/users/{}/following".format(name))
    return following


def following(name):
    following = get_following_for(name)
    following_names = []
    for i in range(len(following.json())):
        following_names.append(following.json()[i]["login"])
    return following_names

print(following("DiviqLud"))