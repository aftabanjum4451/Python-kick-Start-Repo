# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 00:41:31 2020

@author: aftab
"""


'''
We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv 
which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.

Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, 
Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, 
and produce a graph of the Net Score vs Number of Retweets.

To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)
'''

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(str1):
    str1=str1.replace("'",'')
    str1=str1.replace('"','')
    str1=str1.replace(",",'')
    str1=str1.replace(".",'')
    str1=str1.replace("!",'')
    str1=str1.replace(":",'')
    str1=str1.replace(";",'')
    str1=str1.replace('#','')
    str1=str1.replace('@','')
    return str1

variable='ali:,lahore@,.kahan!, love pakistan and i enjoy the movie and its best move and good and entertain'

strip_punctuation(variable)



'''
Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter,
 a string which represents one or more sentences, and calculates 
 how many words in the string are considered positive words. 
 Use the list, positive_words to determine what words will count 
 as positive. The function should return a positive integer
 - how many occurrences there are of positive words in the text. 
 Note that all of the words in positive_words are lower cased, 
 so you’ll need to convert all the words in the input 
 string to lower case as well.

'''


def get_pos(str1):
    str1=str1.replace("'",'')
    str1=str1.replace('"','')
    str1=str1.replace(",",'')
    str1=str1.replace(".",'')
    str1=str1.replace("!",'')
    str1=str1.replace(":",'')
    str1=str1.replace(";",'')
    str1=str1.replace('#','')
    str1=str1.replace('@','')
    positive_words = []
    with open("positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())
    str1=str1.lower() 
    str1=str1.split(' ')
    postive_count=0
    for item in str1:
        if item in positive_words:
            postive_count=postive_count+1
    return postive_count

get_pos(variable)
            
'''
Next, copy in your strip_punctuation function and define a 
function called get_neg which takes one parameter, a string 
which represents one or more sentences, and calculates how many
 words in the string are considered negative words. Use the list, 
 negative_words to determine what words will count as negative. 
 The function should return a positive integer - how many occurrences 
 there are of negative words in the text. Note that all of the words 
 in negative_words are lower cased, so you’ll need to convert all the 
 words in the input string to lower case as well.

'''            
def get_neg(str1):
    str1=str1.replace("'",'')
    str1=str1.replace('"','')
    str1=str1.replace(",",'')
    str1=str1.replace(".",'')
    str1=str1.replace("!",'')
    str1=str1.replace(":",'')
    str1=str1.replace(";",'')
    str1=str1.replace('#','')
    str1=str1.replace('@','')
    negative_words = []
    with open("negative_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())
    str1=str1.lower() 
    str1=str1.split(' ')
    negative_count=0
    for item in str1:
        if item in negative_words:
           negative_count=negative_count+1
    return negative_count

variable='ali:,lahore@,.kahan!, notgood , suck, love pakistan and i enjoy the movie and its best move and good and entertain'

get_neg(variable)    
            
'''
Finally, copy in your previous functions and write code that opens the 
file project_twitter_data.csv which has the fake generated twitter 
data (the text of a tweet, the number of retweets of that tweet,
      and the number of replies to that tweet). Your task is to build
 a sentiment classifier, which will detect how positive or negative 
 each tweet is. Copy the code from the code windows above, and put 
 that in the top of this code window. Now, you will write code to 
 create a csv file called resulting_data.csv, which contains the Number
 of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), 
 Negative Score (which is how many angry words are in the tweet), 
 and the Net Score (how positive or negative the text is overall) 
 for each tweet. The file should have those headers in that order. 
 Remember that there is another component to this project.
 You will upload the csv file to Excel or Google Sheets and 
 produce a graph of the Net Score vs Number of Retweets. 
 Check Coursera for that portion of the assignment, 
 if you’re accessing this textbook from Coursera.

''' 

project_Twitter_Data_File=open('project_twitter_data.csv','r')
resultingDataFile = open("resulting_data.csv","w")

negative_words = []
with open("negative_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())
                
    
def get_neg(str1):
    str1=str1.replace("'",'')
    str1=str1.replace('"','')
    str1=str1.replace(",",'')
    str1=str1.replace(".",'')
    str1=str1.replace("!",'')
    str1=str1.replace(":",'')
    str1=str1.replace(";",'')
    str1=str1.replace('#','')
    str1=str1.replace('@','')
    str1=str1.lower() 
    str1=str1.split(' ')
    negative_count=0
    for item in str1:
        if item in negative_words:
           negative_count=negative_count+1
    return negative_count

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []

with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
    
            

def get_pos(str1):
    str1=str1.replace("'",'')
    str1=str1.replace('"','')
    str1=str1.replace(",",'')
    str1=str1.replace(".",'')
    str1=str1.replace("!",'')
    str1=str1.replace(":",'')
    str1=str1.replace(";",'')
    str1=str1.replace('#','')
    str1=str1.replace('@','')
    positive_words = []
    str1=str1.lower() 
    str1=str1.split(' ')
    postive_count=0
    for item in str1:
        if item in positive_words:
            postive_count=postive_count+1
    return postive_count

def sentimen_classifier(resultingDataFile):
    resultingDataFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")
    linesPTDF =  project_Twitter_Data_File.readlines()
    headerDontUsed= linesPTDF.pop(0)
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(',')
        resultingDataFile.write("{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]), (get_pos(listTD[0])-get_neg(listTD[0]))))    
        resultingDataFile.write("\n")


sentimen_classifier(resultingDataFile)
project_Twitter_Data_File.close()
resultingDataFile.close()






            




             
    
        
    

        
        
        
        
        
      
        
               

        




        
        

def sentiment_classifier():
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

            
            
            
            
            
            
            
            
            
            
            