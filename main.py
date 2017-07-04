from spy_details import spy, Spy, ChatMessage, friends#imports these things from spy_details rather than creating them again
from steganography.steganography import Steganography
import string
from termcolor import *
import colorama

STATUS_MESSAGES = ["The name's Bond, James Bond!", "Shaken, not stirred.", "I don't stop when i'm tired, i stop when i'm done!"]
colorama.init()

print "Hey spy! Let\'s get started"

question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "  #confirmation of the authenticity of the user
existing = raw_input(question)  #raw_input takes the input as a string
#password = raw_input("So, Mr. Bond please enter your password to confirm your authentication : ")



def add_status():  #function used to add and update statuses

    updated_status_message = None

    if spy.current_status_message != None:

        print "Your current status message is %s \n"% (spy.current_status_message)  #prints the current status
    else:
        print "You don't have any status message currently \n"

    default = raw_input("So, Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":  #.upper() function automatically converts the input into upper case,  N is for adding new status
        new_status_message = raw_input("What's on your mind right now ? ")


        if len(new_status_message) > 0:  #length of the status message should be greater than zero
            STATUS_MESSAGES.append(new_status_message)   #new status message is added in the list of status messages
            updated_status_message = new_status_message

    elif default.upper() == "Y":   #it is for using one of the the previously added messages

        item_position = 1

        for message in STATUS_MESSAGES:
            print "%d. %s" % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages:  "))


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print "Oops! Incorrect option pal! Press either y or n."  #if the option chosen is not mentoned in the list,this message is displayed

    if updated_status_message:
        print "Your updated status message is : %s" % (updated_status_message)
    else:
        print "Uh-Oh! You currently don't have a status update"

    return updated_status_message  #status is updated




def add_friend():#function for adding friends
    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("So, Who is your friend ? : ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.? : ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age? ")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating? ")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print "Hurrah! Your Friend is Added!"
    else:
        print "Oops Sorry! Invalid entry. You must try again later."

    return len(friends)


def select_a_friend():  #function for selecting a friend among the listed friends
    item_number = 0

    for friend in friends:
        print "%d. %s %s of age %d with rating %.2f is online" % (item_number +1, friend.salutation, friend.name, friend.age, friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose one of your friends : ")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position  #returns the index of the friend chosen


def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image ? ")
    output_path = "output.jpg"  #image path
    text = raw_input("What secret message would you want to hide behind this image or if u want to choose among 1.SOS 2.SAVE ME 3.NEED ASSISTENCE? ")

    invalidchar = set(string.punctuation.replace("_", " "))  #this checks that the secret contains space or underscore or nothing
    if any(char in invalidchar for char in text):
        print "Invalid, The secret message should not contain spaces !"
        text = raw_input("Enter a valid secret message or if u want to choose among 1.SOS 2.SAVE ME 3.NEED ASSISTENCE ? ")

    else:
        print "Hurrah! Your secret message is good to go, wait a few seconds untill your message is encoded in the image !"

    Steganography.encode(original_image, output_path, text)  #this encodes the secret message in the image

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)  #the chat is added to the previous chat

    print "Awesome! Your secret message-image is finally ready!"


def read_message():  #ths function reads the messages sent by spy

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file ?")

    secret_text = Steganography.decode(output_path)
    if len(secret_text) == 0:
        print "Oh Crap! There is no secret message in it."
    elif secret_text.upper() == "SOS" or secret_text.upper() == "Save me" or secret_text.upper()== "Need assistance ":
        print "the secret message is : " + secret_text
        print "Wait ! I'll be right there rightaway !"

    else:
        print "Voila! here it is :D"
        print "Your secret message i.e '" +secret_text + "' has been saved !"
    new_chat = ChatMessage(secret_text, False)
    friends[sender].chats.append(new_chat)
    words= secret_text.split(" ")
    #average = sum(len(j) for j in words) / len(words)
    print len(words)





def read_chat_history():

    read_for = select_a_friend()

    print "\n6"
#time blue spy name red chat black
    for chat in friends[read_for].chats:

        if chat.sent_by_me:
            #cprint'[%s] %s: %s' % (chat.time.strftime("%d %B %Y"),  'You said:', chat.message)
             cprint (chat.time.strftime("%d %B %Y"), 'blue')
             cprint ('You said :', 'red')
             print chat.message
        else:
             cprint(chat.time.strftime("%d %B %Y"), 'blue')
             cprint(friends[read_for].name, 'red')
             print chat.message
          #print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


def start_chat(spy):  #this starts the chat by spy

    spy.name = spy.salutation + " " + spy.name


    if spy.age>12 and spy.age<50:  #age constraint is checked


        print "Authentication complete. Welcome " + spy.name + " , of age: "+ str(spy.age) + " and rating : " + str(spy.rating) + ". Overwhelmed to have you onboard !"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do ? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print "You have %d friends! You must always enter a valid friend name with rating greater than or equal to yours! Can't really afford you to have bad compaby you see!" % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    print "See you next time pal!"
                    show_menu = False

    else:
        print 'Oops Sorry! you are Too young pal! Better luck next time!'


if existing == "Y" or existing == "y":
    start_chat(spy)
else:

    spy = Spy('','',0,0.0)  #is the existing spy is not Mr.Bond then new entry of spy is made under constraints


    spy.name = raw_input("Hey pal ! Welcome to spy chat, may i know your spy name first: ")

    if len(spy.name) > 0:

         if set('[~!@#$%^&*()_+{}":;\']+$ " "').intersection(spy.name):
             print "Invalid name."
         else:
             print "Valid name!"
             spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")
             spy.age = int(raw_input("What is your age ?"))
             spy.rating = float(raw_input("What is your spy rating?"))
             if spy.rating > 4.5:
                 print 'Great ace!'
             elif spy.rating > 3.5 and spy.rating <= 4.5:
                 print 'You are one of the good ones.'
             elif spy.rating >= 2.5 and spy.rating <= 3.5:
                 print 'You can always do better'
             else:
                 print 'We can always use somebody to help in the office.'
             start_chat(spy)
    else:
        print 'Please add a valid spy name !'



