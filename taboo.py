from word import Word
from player import Player
import time
import random

print("*" * 10, "Welcome to Taboo", "*" * 10)

# x = Word("Elbise")
# x.add_forbidden_words(["Giymek", "Etek", "Mağaza", "Kumaş"])
# x.show_word()
#
# y = Word("Orman")
# y.add_forbidden_words(["Piknik", "Odun", "Ağaç", "Koru"])
# y.show_word()
#
# z = Word("Telaffuz")
# z.add_forbidden_words(["Diksiyon", "Kelime", "Söylemek", "Konuşmak"])
# z.show_word()
#
# t = Word("Panjur")
# t.add_forbidden_words(["Pembe", "Film", "Ev", "Pencere"])
# t.show_word()

all_words = []

with open("words", "r") as file:
    full_list = file.readlines()
    for full_words in full_list:
        real_word = full_words.split(":")[0]
        helper_words = full_words.split(":")[1].strip()
        result = {"real_word":real_word,"helper_words":helper_words}
        all_words.append(result)


def ask_question():
    random_word = random.choice(all_words)
    print(random_word.get("real_word"))
    print(random_word.get("helper_words"))
ask_question()



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

