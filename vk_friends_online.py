import vk
import getpass


APP_ID = 0


def get_user_login():
    return input("Login: ")


def get_user_password():
    return getpass.getpass(prompt="Password: ")


def get_api(login, password, api_version="5.80"):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends"
    )
    return vk.API(session, v=api_version)


def get_friends_online(api):
    friends_id_online = api.friends.getOnline()
    return api.users.get(user_ids=friends_id_online)


def print_online_friends(friends_online):
    if friends_online:
        print("=== {} friends online ===".format(len(friends_online)))
        for friend in friends_online:
            print("{} {}".format(friend["first_name"], friend["last_name"]))


def main():
    login = get_user_login()
    password = get_user_password()
    try:
        vk_api = get_api(login, password)
    except vk.exceptions.VkAuthError as err:
        exit(err)
    friends_online = get_friends_online(vk_api)
    print_online_friends(friends_online)


if __name__ == "__main__":
    main()
