class User:
    all_rewards_members = []

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        # print(*self, sep='\n')
        # attributes = dir(self)
        # print(attributes)
        print(self.first_name, self.last_name, self.email, self.age)
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print(f'{self} is already a member')
            return self
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(self.gold_card_points)
            self.all_rewards_members.append(self)

            return self

    def spend_points(self, points_spent):
        if points_spent > self.gold_card_points:
            print(f'{self} does not have enough points')
            return self
        else:
            self.gold_card_points = self.gold_card_points - points_spent
            print(self.gold_card_points)
            return self

user_1 = User('jack','piro','jackpiro1133@gmail.com',20)
user_2 = User('emily','Schultze','em@gmail',20)
user_3 = User('sam','prio','sam@gmail',16)

user_1.display_info().enroll().spend_points(50)
# user_1.enroll()
# user_1.spend_points(50)

user_2.enroll().spend_points(80)
# user_2.spend_points(80)

user_1.display_info()
user_2.display_info()
user_3.display_info().spend_points(30)

user_1.enroll()
# user_3.spend_points(30)

print(User.all_rewards_members)