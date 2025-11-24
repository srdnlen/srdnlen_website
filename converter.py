import json

"""
{
  "name": "Nuno Coração",
  "image": "img/nuno_avatar.jpg",
  "bio": "Theme Creator",
  "social": [
    { "linkedin": "https://linkedin.com/in/nunocoracao" },
    { "twitter": "https://twitter.com/nunocoracao" },
    { "instagram": "https://instagram.com/nunocoracao" },
    { "medium": "https://medium.com/@nunocoracao" },
    { "github": "https://github.com/nunocoracao" },
    { "goodreads": "http://goodreads.com/nunocoracao" },
    { "keybase": "https://keybase.io/nunocoracao" },
    { "reddit": "https://reddit.com/user/nunoheart" }
  ]
}
"""

with open("./data/members.json", "r") as f:
    data = json.load(f)
    for category, members in data.items():
        for member in members:
            if member["nick"]:
                data_new = {
                    "name": member["name"] + " @" + member["nick"],
                    "image": f"/img/members/{member['avatar']}",
                    "bio": member["position"],
                    "tags": [category.lower()] if category.lower() != "foren/misc" else ["forensics", "misc"],
                    "social": [
                        {"linkedin": member["link"]}
                    ]
                }
            else:
                data_new = {
                    "name": member["name"],
                    "image": f"/img/members/{member['avatar']}",
                    "bio": member["position"],
                    "social": [
                        {"linkedin": member["link"]}
                    ]
                }

            with open("./data/authors/" + member["nick"].lower() + ".json", "w") as f2:
                json.dump(data_new, f2, indent=1)
