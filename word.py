class Word:
    main_word = "kelime"
    forbidden_word = ["ağaç", "saklama kabı", "regl"]

    def __init__(self, word, other_words=[]):
        self.main_word = word
        self.forbidden_word = other_words
        print ("Kelime oluşturuldu:", word)

    def __str__(self):
        return self.main_word

    def add_forbidden_word(self, word):
        self.forbidden_word.append(word)
        print (word, "eklendi.")


    def add_forbidden_words(self,words):
        for i in words:
            self.forbidden_word.append(i)

    def show_word(self):
        print ("-"*7, self.main_word, "-"*7)
        for i in self.forbidden_word:
            print(i)