""" class User:
    pass

user_1=User()
user_1.id=10092
user_1.username="Abhishek"

print(user_1.username)

user_2=User()
user_2.id=5100
user_2.username="Rishav"

print(user_2.username)"""

#construtor
class User:
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.followers=0
        self.following=0

    def follow(self,user):
        user.followers +=1
        self.following +=1

user_1=User(10092,"Abhishek")
user_2=User(5100,"Rishav")

# print(user_1.username)
# print(user_2.id)

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)