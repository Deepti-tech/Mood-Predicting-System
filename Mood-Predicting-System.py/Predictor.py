def mood_predictor():
    Happy = Sad = Excited = Worried = 0
    ans = ans_2 = ans_3 = ans_4 = ans_5 = ''
    file = open('Mood.txt', 'a')
    
    print("\nTo know your mood please answer the following questions.")
    print("(The questions below should be answered in Yes/No format only.)")
    print("(In order to skip a question, enter 'Skip'.)\n\n")
    	
    while (ans.lower() != 'yes') and (ans.lower() != 'no') and (ans.lower() != 'skip'):
        ans = input('1. Are you feeling grateful today?\n\t-->')
        if ans.lower() == 'yes':     Happy = Happy + 1
        elif ans.lower() == 'no':    Sad = Sad + 1
        elif ans.lower() == 'skip':
            break
        else:
            print('[Enter "Yes" or "No" or "Skip"]\n')
            continue
            
    while (ans_2.lower() != 'yes') and (ans_2.lower() != 'no') and (ans_2.lower() != 'skip'):
        ans_2 = input('2. Do you feel motivated and satisfied?\n\t-->')
        if ans_2.lower() == 'yes':    Happy = Happy + 1
        elif ans_2.lower() == 'no':   Worried = Worried + 1
        elif ans_2.lower() == 'skip':
            break
        else:
            print('[Enter "Yes" or "No" or "Skip"]\n')
            continue
            
    while (ans_3.lower() != 'yes') and (ans_3.lower() != 'no') and (ans_3.lower() != 'skip'):
        ans_3 = input('3. Is your day going according to you?\n\t-->')
        if ans_3.lower() == 'yes':    Happy = Happy + 1
        elif ans_3.lower() == 'no':   Sad = Sad + 1
        elif ans_3.lower() == 'skip':
            break
        else:
            print('[Enter "Yes" or "No" or "Skip"]\n')
            continue
            
    while (ans_4.lower() != 'yes') and (ans_4.lower() != 'no') and (ans_4.lower() != 'skip'):
        ans_4 = input('4. Are you looking forward for your day?\n\t-->')
        if ans_4.lower() == 'yes':    Excited =Excited + 1
        elif ans_4.lower() == 'no':   Worried = Worried + 1
        elif ans_4.lower() == 'skip':
            break
        else:
            print('[Enter "Yes" or "No" or "Skip"]\n')
            continue
            
    while (ans_5.lower() != 'yes') and (ans_5.lower() != 'no') and (ans_5.lower() != 'skip'):
        ans_5 = input('5. Are your manifestations coming close?\n\t-->')
        if ans_5.lower() == 'yes':    Excited = Excited+ 1
        elif ans_5.lower() == 'no':   Sad = Sad + 1
        elif ans_5.lower() == 'skip':
            break
        else:
            print('[Enter "Yes" or "No" or "Skip"]\n')
            continue
            
    if((Happy>Sad) and (Happy>Excited) and (Happy>Worried)):         
        file.write("\nHappy")                            
        print("\nRESULT : \nGreat!!\nYour mood is happy!!\n\n")
    else:
        if ((Sad>Excited) and (Sad>Worried)):                  
            file.write("\nSad")                     
            print("\nRESULT : \nAlas!!\nYour mood is sad.\n\n")
        else:                
            if (Excited>Worried):                           
                file.write("\nExcited")              
                print("\nRESULT : \nWhoopee!!\nYou are excited!!\n\n")
            elif(Worried>Excited):
                file.write("\nWorried")                
                print("\nRESULT : \nSeems, you are worried.\nRemember, you cannot run away from problems but worrying is not the solution.")
            else:
                print("\nAs you have skip all the questions we cannot predict your mood.\nTry answering these questions.\n\n")
                mood_predictor_2()
                
    file.close()
    
def mood_predictor_2():
    Happy = Sad = Excited = Worried = 0
 
    ans = ans_2 = ans_3 = ans_4 = ans_5 = ''
    file = open('Mood.txt', 'a')
    	
    while (ans.lower() != 'yes') and (ans.lower() != 'skip'):
        ans = input('1. Are you craving for sweets and chocolates?\n\t-->')
        if ans.lower() == 'yes':   Sad = Sad + 1
        elif ans.lower() == 'skip' or (ans.lower() == 'no'):   break
        else:
            print('[Enter "Yes" or "No" or "Skip"]\n')
            continue
            
    while (ans_2.lower() != 'yes') and (ans_2.lower() != 'skip'):
        ans_2 = input('2. Are you satisfied with how your life now is?\n\t-->')
        if ans_2.lower() == 'yes':   Happy = Happy + 1
        elif ans_2.lower() == 'skip' or (ans_2.lower() == 'no'):  break
        else:
            print('[Enter "Yes" or "No" or "Skip"]\n')
            continue
            
    while (ans_3.lower() != 'yes') and (ans_3.lower() != 'skip'):
        ans_3 = input('3. Are you thinking about anything bad that might happen?\n\t-->')
        if ans_3.lower() == 'yes':   Worried = Worried + 1
        elif (ans_3.lower() == 'skip') or (ans_3.lower() == 'no'):   break
        else:
            print('[Enter "Yes" or "No" or "Skip"]\n')
            continue
            
    while (ans_4.lower() != 'yes') and (ans_4.lower() != 'skip'):
        ans_4 = input('4. Do feel like being over the moon?\n\t-->')
        if ans_4.lower() == 'yes':   Excited =Excited + 1
        elif ans_4.lower() == 'skip' or (ans_4.lower() == 'no'):  break
        else:
            print('[Enter "Yes" or "No" or "Skip"]\n')
            continue
            
    if((Happy>Sad) and (Happy>Excited) and (Happy>Worried)):         
        file.write("\nHappy")                            
        print("\nRESULT : \nGreat!!\nYour mood is happy!!\n\n")
    else:
        if ((Sad>Excited) and (Sad>Worried)):                  
            file.write("\nSad")                     
            print("\nRESULT : \nAlas!!\nYour mood is sad.\n\n")
        else:                
            if (Excited>Worried):                           
                file.write("\nExcited")              
                print("\nRESULT : \nWhoopee!!\nYou are excited!!\n\n")
            elif(Worried>Excited):
                file.write("\nWorried")                
                print("\nRESULT : \nSeems, you are worried.\nRemember, you cannot run away from problems but worrying is not the solution.")
                
                    
    file.close()
    
        
    





