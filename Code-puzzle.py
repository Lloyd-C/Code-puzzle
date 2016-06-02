import datetime #Import the datetime so that the end time can be subtracted from the start time to get how long they have been

print('This is a puzzle where you must work out what ten words are by cracking the code. Each symbol used in the coded words represents a unique letter...')#Display instructions

################################################################################

#Open and display file with the encrypted words in it and display it
def Read_and_print_words(x):#Bring in 'x', the file name
    try:
        lines=open(x, 'r') #Open the file
        words=lines.read() #Make it an appropriate format
        lines.close() #Close the file
        words=words.rstrip() #Remove the empty line at the end
    except:#Make sure that there will not be a run time error if the file cannot be found
        print('\nThe file:', x, 'could not be found.')
        print('Please make sure that it is in the same folder as this program and that it is a .txt file')
        print('It should be named', x)
        print('Run the program again once you think the problem is fixed...')
        exit(input('Please press enter to end the program...')) #End the program
    return (words) #Return the file

################################################################################

#Let the user choose how many clues they want
def Replace_clues(ten_words):#Bring in the ten words so that the clues can be subsituted into them
    (clues)=Read_and_print_words('clues.txt') #Read in the clues file
    print('\nHere are the ten words...'), print(ten_words)
    clue_choice=input('\nDo you want 0, 1, 2 or all 3 clues? ') #Ask the user how many clues they want
    while(clue_choice!='0' and clue_choice!='1' and clue_choice!='2' and clue_choice!='3'):#Make sure their input is valid
        print('Please enter a valid number, from 0-3...') #Display error message
        clue_choice=input('\nDo you want 0, 1, 2 or all 3 clues? ') #Ask the user how many clues they want
    clue_choice=int(clue_choice)#Change their choice into an integer for later use in the Extra_clue function
    clues=list(clues) #Turn their clues into a list
    clues.remove('\n'), clues.remove('\n') #Remove the whitespaces
    symbol_attempts=[] #Create the empty array that will contain the symbols that have been entered
    letter_attempts=[] #Create the empty array that will contain the letters that have been entered
    for i in range(0,(clue_choice*2), 2):#For the chosen amount of clues that they want...
        letter=clues[i] #Get the letter of that clue from the clues array
        symbol=clues[i+1] #Get the symbol of that clue from the clues array
        print(letter, '=', symbol) #Show them the clues
        ten_words=ten_words.replace(symbol, letter) #Replace the letter with the symbol
        symbol_attempts.append(symbol) #Add the symbol to the array of entered symbols
        letter_attempts.append(letter) #Add the letter to the array of entered letters
    if clue_choice!=0:
        print('\nHere are the ten words with the clue(s) in it...'), print(ten_words)#Display the new ten words
    return (ten_words,symbol_attempts,letter_attempts,clue_choice,clues)#Return the words, arrays, clue choice and the clues

################################################################################

#Check if the user's chosen letter has already been entered
def Get_letter_choice(letter_attempts, ten_words, symbol_choice):
    letter_choice=input(str('Please enter the letter that you want to replace it with: '))#Get what letter they want to enter
    while(len(letter_choice)!=1 or letter_choice.isalpha()==False or letter_choice.title() in letter_attempts):#Make sure their input is valid
        print('Please enter a valid, single letter that hasn\'t been entered yet...') #Display error message
        letter_choice=input(str('Please enter the letter that you want to replace it with: '))#Get what letter they want to enter
    letter_attempts.append(letter_choice.upper())#Add their input onto the array of entered letters
    ten_words=ten_words.replace(symbol_choice,letter_choice.upper()) #Replace the user's chosen symbol with the chosen letter
    print('\nHere are the new ten words:'), print(ten_words) #Display the new words
    return(ten_words, letter_attempts)

################################################################################

#Check if the user's chosen symbol has already been entered
def Get_symbol_choice(symbol_attempts):
    symbol_choice=input(str('\nPlease enter the symbol that you want to replace: ')) #Allow the user to choose the symbol
    while(len(symbol_choice)!=1 or symbol_choice.isalpha()==True or symbol_choice in symbol_attempts or symbol_choice not in ten_words): #Make sure the user only enters one symbol
        print('\nPlease enter a valid symbol, that is one character and is in the words above...') #Display error message
        symbol_choice=input(str('\nPlease enter the symbol that you want to replace: '))#Allow the user to choose the symbol
    symbol_attempts.append(symbol_choice) #Add the symbol to the array of entered symbols
    return (symbol_choice, symbol_attempts)

################################################################################

#Allow the user to enter a letter and symbol pairing
def Replace_user_choice(ten_words, symbol_attempts, letter_attempts, clue_choice):
    menu_choice='1'#Make sure that the 'while' loop below is carried out
    while(menu_choice.title()=='1' or menu_choice.title()=='2' or menu_choice.title()=='3' or menu_choice.title()=='4'):
        (symbol_choice, symbol_attempts)=Get_symbol_choice(symbol_attempts)#Run the function to get the user's choice of symbol
        (ten_words, letter_attempts)=Get_letter_choice(letter_attempts, ten_words, symbol_choice)#Run the function to get the user's chioce of letter
        menu_choice=input(str('\n1. Would you like to enter another symbol\t2. Receive a clue\n3. Delete a letter and return it to normal\t4. Get some help\n5. Check answers or stop playing\n'))
        while(menu_choice.title()!='1' and menu_choice.title()!='2' and menu_choice.title()!='3' and menu_choice.title()!='4' and menu_choice.title()!='5'):#Make sure their input is valid
            print('\nPlease enter a valid answer. Enter 1, 2, 3, 4 or 5...\n') #Display error message
            menu_choice=input(str('1. Would you like to enter another symbol\t2. Receive a clue\n3. Delete a letter and return it to normal\t\t4. Get some help\n5. Stop playing\n'))
        if menu_choice=='2':#If the user wants to receive an extra clue run the below function
            (ten_words,symbol_attempts,letter_attempts)=Extra_clue(ten_words, clue_choice, symbol_attempts, letter_attempts, clues)
        elif menu_choice=='3':#If the user wants to delete a pair, run the below function
            (ten_words, letter_attempts, symbol_attempts)=Delete_pair(ten_words, letter_attempts, symbol_attempts)
        elif menu_choice=='4':#If the user wants to get help, run the below function
            (frequency)=Help(ten_words, symbol_attempts, letter_attempts, start_time)
    return (ten_words)

################################################################################

def Extra_clue(ten_words, clue_choice, symbol_attempts, letter_attempts, clues):
    if clue_choice==0 or clue_choice==1 or clue_choice==2:
        while clue_choice!=3 and clues[clue_choice*2] in letter_attempts:#Make sure that they haven't manually entered the clue already
            if clue_choice<3:
                clue_choice+=1
        if clue_choice!=3:
            ten_words=ten_words.replace(clues[clue_choice*2+1], clues[clue_choice*2]) #Substitute the clues in
            print(), print(clues[clue_choice*2], '=', clues[clue_choice*2+1], '\n'), print('Here are the new ten words:'), print(ten_words)#Give them the clue and display the new ten  words
            letter_attempts.append(clues[clue_choice*2])
            symbol_attempts.append(clues[clue_choice*2+1])
        else:
            print('All of the clues are already in the ten words...')
    elif clue_choice==3:#If they already have all three of the clues...
        print('Your already have all of the clues...') #Display error message
    return (ten_words,symbol_attempts,letter_attempts)

################################################################################

#Allow the user to delete a letter and symbol pairing
def Delete_pair(ten_words,letter_attempts,symbol_attempts):
    delete_letter=input('Which letter would you like to return to normal? ')
    while(delete_letter.isalpha()==False or len(delete_letter)!=1 or delete_letter.title() not in letter_attempts):
        print('Please enter a valid, single letter')
        delete_letter=input('Which letter would you like to return to normal? ')
    index_of_letter=letter_attempts.index(delete_letter.title())
    letter_being_removed=letter_attempts.pop(index_of_letter) #Remove the letter from the list of attempts
    symbol_being_replaced=symbol_attempts.pop(index_of_letter) #Remove the symbol from the list of attempts
    ten_words=ten_words.replace(letter_being_removed, symbol_being_replaced)
    print('Here are the new ten words:'), print(ten_words)
    return(ten_words, letter_attempts, symbol_attempts)

################################################################################

#Check if the user's answers are right
def Check_answers(ten_words, start_time):
    again='No'
    ten_words=ten_words.rstrip()
    (solved)=Read_and_print_words('solved.txt')
    if solved!=ten_words: #Check if the user's answers are the same as the correct answers
        again=input('Your answers are incorrect...\nWould you still like to quit the puzzle? ')
        while(again.title()!='Yes' and again.title()!='No'):
            print('Please enter a valid answer: Yes or No\n')
            again=input('Would you still like to quit the puzzle? ')
        if again.title()=='Yes':
            print('\nHere are the solutions'), print(solved)
            end_time=datetime.datetime.now()
            print('\nYou have been', (end_time.minute - start_time.minute) ,'minutes and', (end_time.second - start_time.second), 'seconds')
        elif again.title()=='No':
            print(ten_words)
    elif solved==ten_words:
        print('You are correct!') #Tell them if they are correct
        again='Yes'
        end_time=datetime.datetime.now()
        print('\nYou were', (end_time.minute - start_time.minute) ,'minutes and', (end_time.second - start_time.second), 'seconds')
    return again

################################################################################

#Calculate the frequency with which each and tell the user how long they have been
def Help(ten_words, symbol_attempts, letter_attempts, start_time):
    frequency={} #Create an empty dictionary
    for key in ten_words:#Scan through the characters in the ten words
        if key in frequency:#If that character is already in the dictionary...
            frequency[key]+=1 #Add 1 to it
        else:#If that chacter isn't in the dictionary...
            frequency[key]=1 #Create a key for that symbol in the dictionary
    del frequency['\n'] #Delete the empty one
    loopcounter=0
    for key in frequency:#For every key in the dictionary of symbols
        if frequency[key]==1 and key.isalpha()==False:#Tell the user how many times that symbol is in it
            print(key, 'is in the coded words', frequency[key], 'time')
        elif key.isalpha()==False:
            print(key, 'is in the coded words', frequency[key], 'times')
        loopcounter+=1
    if loopcounter==0:
        print('The frequency cannot be displayed, as all of the symbols have been entered...')
    end_time=datetime.datetime.now() #Create a variable that stores the current time
    minutes_taken=end_time.minute - start_time.minute
    seconds_taken=end_time.second - start_time.second
    if seconds_taken<0:
        seconds_taken=seconds_taken*(-1)
    print('\nYou have been', minutes_taken ,'minutes and', seconds_taken, 'seconds') #Tell the user how long they have been
    return frequency

################################################################################

#Run the functions
(ten_words)=Read_and_print_words('words.txt')
(ten_words, symbol_attempts, letter_attempts, clue_choice, clues)=Replace_clues(ten_words)
again='No'
start_time=datetime.datetime.now() #Record the start time
while(again.title()=='No'):#While they keep wanting to play
    (ten_words)=Replace_user_choice(ten_words, symbol_attempts, letter_attempts, clue_choice)
    again=Check_answers(ten_words, start_time)
exit(input('Please press enter to end the program...'))
