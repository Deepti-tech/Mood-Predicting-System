import os

def number_of_days():
    days = 0
    
    if os.path.isfile("Mood.txt"):
        file = open("Mood.txt", "r")
        for line in open("Mood.txt").readlines(  ): days = days + 1
        file.close()
    else:
        days = 1
    return days

def mood_history():
    days = number_of_days()
    
    day = 1
    try:
        file = open("Mood.txt", "r")
        print("\nYour mood for the past", days-1 ,"day(s) are as follows : ") 
        
        next(file)
        for line in file:
            print('Day',day,'=>',line)
            day = day + 1
        file.close()
    except FileNotFoundError: print('After you predict your mood, we will show you the history of your moods.')
        
    
        
    
