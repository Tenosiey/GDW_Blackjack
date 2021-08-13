import json

def register(discord_uid, username, user_id):
    with open("bank.json") as jsonFile:
        a_dictionary = json.load(jsonFile)
        jsonFile.close()

    if str(discord_uid) in a_dictionary:
        print("User \"" + str(discord_uid) + "\" is already registered")
    else:
        data = {}
        data[str(discord_uid)] = []
        data[str(discord_uid)].append({
            "discord_uid": str(discord_uid),
            "username": username,
            "user_id": user_id,
            "money": 0,
            "games_played": 0,
            "games_won": 0
        })

        with open("bank.json", "a", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    register()