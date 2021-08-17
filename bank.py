import json

def register(discord_uid, username, user_id):
    with open("bank.json") as jsonFile:
        dict_bank = json.load(jsonFile)
        jsonFile.close()

    if str(discord_uid) in dict_bank:
        print("User \"" + str(discord_uid) + "\" is already registered")
    else:
        dict_bank[str(discord_uid)] = {
            "discord_uid": str(discord_uid),
            "username": username,
            "user_id": user_id,
            "rank": "player",
            "money": 1000,
            "games_played": 0,
            "games_won": 0
        }

        with open("bank.json", "w", encoding="utf-8") as f:
            json.dump(dict_bank, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    register()