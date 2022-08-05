def mood_enhancer():
    mood = ''
    while (mood.lower() != 'happy') and (mood.lower() != 'sad') and (mood.lower() != 'excited') and (mood.lower() != 'worried'):
        
        mood = input('\nEnter your current mood : ')
        
        if mood.lower() == 'happy':
            print('\nTry spreading your happiness around you with your vibrant smile.')
            
        elif mood.lower() == 'sad':
            print("\nHere are some of our suggestions to uplift your mood :\n\tListening songs can help you get in better mood. ♫\n\tWrite in a journal your feeling.  \n\tWatch comic sketches.  \n\tTalk to your loved ones.")
            
        elif mood.lower() == 'excited':
            print("\nHope your day goes the way you claimed.")
            
        elif mood.lower() == 'worried':
            print("\nTry doing these :\n   Practice deep breathing.\n   Discuss your problem with someone whom you trust.\n   Be patient.\n")
            import time
            breathing_exercise = ['Take a deep breath.....', 'Inhale', 'Exhale', 'Inhale', 'Exhale']
            for i in breathing_exercise:
                print('  ',i)
                time.sleep(2)
        else:
            print('Enter "Happy" or "Sad" or "Excited" or "Worried"')
