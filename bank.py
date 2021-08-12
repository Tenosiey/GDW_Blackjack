import json

def register(discord_uid, username, user_id):
    data = {}
    data["user"] = []
    data["user"].append({
        "discord_uid": str(discord_uid),
        "username": username,
        "user_id": user_id,
        "money": 0,
        "games_played": 0,
        "games_won": 0
    })

    with open("bank.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    register()