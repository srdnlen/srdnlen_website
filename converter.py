import json
import os
from unidecode import unidecode

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

with open("./members.json", "r") as f:
    data = json.load(f)
    for category, members in data.items():
        for member in members:
            if member["nick"]:
                data_new = {
                    "name": member["name"] + " @" + member["nick"],
                    "image": f"/img/members/{member['avatar']}",
                    "bio": member["position"],
                    "categories": {
                        "main": category.lower()
                    } if category.lower() != "foren/misc" else {
                        "main": "forensics",
                        "secondary": ["misc"]
                    },
                    "social": [
                        {"linkedin": member["link"]}
                    ]
                }

                normalized_nick = unidecode(member["nick"]).lower()
                with open("./data/authors/" + normalized_nick + ".json", "w") as f2:
                    json.dump(data_new, f2, indent=1)
                os.mkdir(f"./content/authors/{normalized_nick}")
                with open(f"./content/authors/{normalized_nick}/_index.md", "w") as f2:
                    f2.write(f"""---
title: {member["name"]}
layout: profile
---""")
            else:
                data_new = {
                    "name": member["name"],
                    "image": f"/img/members/{member['avatar']}",
                    "bio": member["position"],
                    "categories": {
                        "main": "professor"
                    },
                    "social": [
                        {"linkedin": member["link"]}
                    ]
                }

                normalized_name = unidecode(member["name"]).lower().replace(" ", "-")
                with open("./data/authors/" + normalized_name + ".json", "w") as f2:
                    json.dump(data_new, f2, indent=1)
                os.mkdir(f"./content/authors/{normalized_name}")
                with open(f"./content/authors/{normalized_name}/_index.md", "w") as f2:
                    f2.write(f"""---
title: {member["name"]}
layout: profile
---""")
