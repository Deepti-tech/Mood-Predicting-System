from os import system
name = input('Enter your name : ')
print('Welcome', name, ", to our mood predicting system.")
print("Here, our aim is to predict your mood and help you in tracking the same.\n")

from History import *
days = number_of_days()
print('Day :', days)
 
choice = 0
predicted = False
while choice != 5:
    print("\n{1} Check your mood\n{2} Enhance your mood\n{3} Check your mood for the past", days-1 ,  "day(s)\n{4} Help\n{5} Exit\n\n")
    choice = int(input('Enter your choice : '))
    if choice == 1:
        system('clear')
        if predicted: print('Mood already predicted for the day.\nMeet you tommorow.')
        else:
            predicted = True
            from Predictor import *
            mood_predictor()
            days = days + 1
    elif choice == 2:
        system('clear')
        from Enhancer import *
        mood_enhancer()
    elif choice == 3:
        system('clear')
        mood_history()
    elif choice == 4:
        system("clear")
        print("Hi,",name, "!!")
        from Help import *
        more_about_us()
    elif choice == 5:
        system('clear')
        print('\nThankyou!!!\nHave a great day ahead!!')
    else: print('Enter a number between 1 and 5')
        
        
        
        
