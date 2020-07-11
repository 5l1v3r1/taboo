class Player:
    username = "fatopato"
    point = 0

    def __init__(self, user_name):
        self.username = user_name
        print("Player oluşturuldu:", self.username)

    def point_up(self, addded_point):
        self.point += addded_point
        print("Puan artırıldı. Yeni puanınız:", self.point)

    def point_down(self, decreased_point):
        self.point -= decreased_point
        print("Puan kaybettiniz! Yeni puanınız:", self.point)

    def __str__(self):
        return self.username + "-" + str(self.point)
