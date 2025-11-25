import os
from unidecode import unidecode
import json

categories = ["web","pwn","rev","crypto","foren","misc"]
data = {}
category = 0
social = None
confirm = ""

data["name"] = input("Write the full name: ")
data["nick"] = input("Write the nickname (enter if none): ")
data["bio"] = input("Write a short biography (keep it under 100 chars): ")

data["categories"] = {"main": "", "secondary": []}
confirm = input("Is the user the team's captain? (y/N): ")
if confirm == "y":
    data["categories"]["main"] = "captain"
confirm = input("Is the user a trainer? (y/N): ")
if confirm == "y":
    data["categories"]["main"] = "trainer"

while category in range(0, len(categories)):
    print("Add a user's category. The first one will be the main one, if the user is not a captain/trainer/professor (empty if none): ")
    for i, cat in enumerate(categories):
        print(f"{i + 1}) {cat}")
    try:
        category = int(input("?> "))
        if data["categories"]["main"] == "":
            data["categories"]["main"] = categories[category - 1]
        else:
            data["categories"]["secondary"].append(categories[category - 1])
    except:
        category = None


data["social"] = []
print("Select the socials to link with the author.")
print("You can add a social by checking available icons at https://blowfish.page/samples/icons/.")
print("Enter an empty social to exit.")
while social != "":
    social = input("Enter the social name: ")
    if social != "":
        data["social"].append({social: input("Enter the social link: ")})

data["image"] = "/img/members/" + input("Add the image's name: ")

key = ""
if data["nick"] != "":
    key = unidecode(data["nick"]).lower()
else:
    key = unidecode(data["name"]).lower().replace(" ", "-")

with open("./data/authors/" + key + ".json", "w") as f2:
    json.dump(data, f2, indent=1)

os.mkdir(f"./content/authors/{key}")
with open(f"./content/authors/{key}/_index.md", "w") as f2:
    f2.write(f"""---
title: {data["name"]}
layout: profile
---""")

print("Author added.")
print(f"Add the author's avatar at assets/{data['image']}")
