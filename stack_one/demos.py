#first make your class
class Skater:

    def __init__(self,skaters):
        self.skaters = lots_of_skaters

    def do_a_kickflip(self):
        print(f'{self.name} did a kickflip!')
        return self
 
#now lets make our dictionary

trick_list = ['tre','fakie flip', 'kickflip']

lots_of_skaters = [
    {"name" : 'mike mo capaldi', "age" : 37, "favorite_tricks" : trick_list, "skate_style" : 'street'},
    {"name" : 'chris chann', "age" : 22, "favorite_tricks" : trick_list, "skate_style" : 'street'},
    {"name" : 'chris joslyn', "age" : 25, "favorite_tricks" : trick_list, "skate_style" : 'street'}
    ]

#now we can take this whole list  and create an instance, when we do that now skater only takes one parameter

lots_of_skaters_instance = Skater(lots_of_skaters)

print(lots_of_skaters_instance.skaters[1]['name'])
#now this will output the second dictionaries name no mare need for attributes if its included :)