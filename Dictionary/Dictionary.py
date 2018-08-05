#Dictionary to defination a word


#import modules
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json"))

def main():
    #get the word from the user
    word =input("Enter Word: ")
    print("Searching.....")
    print()
    #print the defination of the word
    word_def=translate(word) # call translate

    #check the type of the word
    # if it's a list (delete the brackets from it )
    if type(word_def) == list:
        for item in word_def:
            print(item)
    #else if it't a string
    else:
        print(word_def)
    print()


#translate word (return the defination of the word)
def translate(word):
    #makr all the letter lowecase letter

    #if the word entered by the user exit , return it
    if word in data:
        print("your word Defination :- ",end='\n')
        return data[word]
    elif word.lower() in data:
        print("your word Defination :- ",end='\n')
        return data[word.lower()]

    #display a word to user that matches the word entered
    elif len(get_close_matches(word,data.keys()))>0:
        matcher=get_close_matches(word,data.keys())[0]
        print( "Did you main %s instead ? ( y , n )"% matcher )
        ch=input();
        while(True):
            if ch=='y' or ch == 'Y':
                print("your word Defination :- ",end="\n")
                return data[matcher]
                break
            elif ch=='n' or ch=='N':
                return "the word dosen't exit, please check it"
                break
            else:
                print( "please, enter your choice (y , n )")
                ch=input()


    #if it's a dosent exist give a hint
    else:
        return "the word dosen't exit, please check it"

#call the main
#print (get_close_matches("ali" , ["ahmed","Khaled","nour","yara","ali","mohamed","eman"]))
main()
