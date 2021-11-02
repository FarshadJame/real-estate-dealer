from random import choice

from user import User

FIRST_NAME = ['Arash', 'Farshad', 'Hossein']
LAST_NAME = ['Hosseini', 'Ahmadi', 'Emani']
MOBILE = ['09129989897', '09129989796', '09129985455', '09129987879', '09129984549']

if __name__ == '__main__':

    for mobile in MOBILE:
        User(first_name=choice(FIRST_NAME), last_name=choice(LAST_NAME), phone_number=mobile)

    for user in User.objects_list:
        print(f"{user.id}\t{user.fullname()}\t{user.phone_number}")
