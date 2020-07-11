from word import Word
from player import Player
import time

print("*" * 10, "Welcome to Taboo", "*" * 10)

x = Word("Elbise")
x.add_forbidden_words(["Giymek", "Etek", "Mağaza", "Kumaş"])
x.show_word()


def create_player(username):
    new_player = Player(username)
    return new_player


def start_game(game_time, question_list):
    point = 0

    ending_time = time.time() + game_time
    while time.time() < ending_time:
        pass

    if point < 3:
        print("siktir git gözümün önünden")
    else:
        print("Süren doldu gavat")

    print("Puanın:", point, "bu sağa yitir")


start_game(3, 0)
create_player("tugceeee")