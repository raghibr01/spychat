


'''spy = {
    'name': 'bond',
    'salutation': 'Mr.',
    'age': 24,
    'rating': 4.7,
    'is_online': True

} instead of using dictionaries we use classes as follows '''


from datetime import datetime#datetime class imported from datetime file

class Spy:#Class Spy created for the spy details

    def __init__(self, name, salutation, age, rating):#constructor created to build the objects of the class
        self.name = name#self is the keyword to initialise, access and store values in the constructor
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:  #class chatmessage created and used for storing, appending and printing the chats

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()#it is used to access the current system datetime
        self.sent_by_me = sent_by_me

spy = Spy('Bond', 'Mr.', 24, 4.0)

friend_one = Spy('Bill Tanner', 'Mr.', 30, 4.0)
friend_two = Spy('M', 'Ms.', 23,  4.39)
friend_three = Spy('Mary goodnight', 'Ms.', 27 , 4.19)


friends = [friend_one, friend_two, friend_three]  #friends of the spy Bond initially stored in
