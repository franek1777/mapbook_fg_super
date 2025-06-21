
def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów.')

def add_user(users_data: list) -> None:
    new_name = input('Podaj imię nowego użytkownika: ')
    new_location = input('Podaj lokalizację nowego użytkownika: ')
    new_posts = int(input('Podaj liczbę postów nowego użytkownika: '))
    users_data.append({"name": new_name, "location": new_location, "posts": new_posts})

def remove_user(users_data: list) -> None:
    uzytkownik_do_usuniecia = input('Podaj użytkownika do usunięcia: ')

    for user in users_data:
        if user['name'] == uzytkownik_do_usuniecia:
            users_data.remove(user)

def update_user(users_data: list) -> None:
    uzytkownik_do_edycji = input('Podaj użytkownika do edycji: ')

    for user in users_data:
        if user['name'] == uzytkownik_do_edycji:
            user['name'] = input('Podaj nowe imię użytkownika: ')
            user['location'] = input('Podaj nową lokalizację użytkownika: ')
            user['posts'] = int(input('Podaj nową liczbę postów: '))
