def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    result = []
    for name, info in users.items():
        if info.get("active") == True:
            result.append(name)
    return result


users = {
    "Ali": {"email": "ali@mail.com", "active": True},
    "Vali": {"email": "vali@mail.com", "active": False},
    "Sami": {"email": "sami@mail.com", "active": False}
}
print(get_active_users(users))