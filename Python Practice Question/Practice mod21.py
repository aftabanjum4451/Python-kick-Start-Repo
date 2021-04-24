# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:20:47 2020

@author: aftab
"""


#Q1
import requests
#import requests_with_caching
def get_movies_from_tastedive(movieName):
    baseurl = "https://tastedive.com/api/similar"
    params_d = {}
    params_d['key']='385702-AftabAnj-E6294P5D'
    params_d["q"] = movieName
    params_d["type"] = "movies"
    params_d["limit"] = "5"
    resp = requests.get(baseurl, params=params_d)
    print(resp.url)
    respDic = resp.json()
    return respDic

get_movies_from_tastedive("Bridesmaids")
get_movies_from_tastedive("Black Panther")


# Q2
'''
Please copy the completed function from above into this active 
code window. Next, you will need to write a function that extracts 
just the list of movie titles from a dictionary returned by 
get_movies_from_tastedive. Call it extract_movie_titles.
'''

import requests
#import requests_with_caching
def get_movies_from_tastedive(movieName):
    baseurl = "https://tastedive.com/api/similar"
    params_d = {}
    params_d['key']='385702-AftabAnj-E6294P5D'
    params_d["q"] = movieName
    params_d["type"] = "movies"
    params_d["limit"] = "5"
    resp = requests.get(baseurl, params=params_d)
    print(resp.url)
    respDic = resp.json()
    return respDic

get_movies_from_tastedive("Bridesmaids")
get_movies_from_tastedive("Black Panther")

''' to see in json form 
data=get_movies_from_tastedive("Black Panther")
print(json.dumps(data,indent=4) )

'''      
def extract_movie_titles(movieName):
    name=movieName
    movie_tilt=[]
    data=get_movies_from_tastedive(name)
    for item in data.keys() :
        for item2 in data[item].keys():
            for item3 in data[item][item2]:
                 #print(item3['Name'])
                 tem_name=item3['Name']
                 #print(tem_name)
                 movie_tilt.append(tem_name)
                 
           
    return movie_tilt

    
extract_movie_titles(["Black Panther", "Captain Marvel"])  

# Q3
'''
Please copy the completed functions from the two code windows 
above into this active code window. Next, you’ll write a function, 
called get_related_titles. It takes a list of movie titles as input.
 It gets five related movies for each from TasteDive, extracts the 
 titles for all of them, and combines them all into a single list.
 Don’t include the same movie twice.

'''   
def get_related_titles(listMovieName):
    if listMovieName != []:
        auxList = []
        relatedList = []
        for movieName in listMovieName:
            auxList = extract_movie_titles(get_movies_from_tastedive(movieName))
            for movieNameAux in auxList:
                if movieNameAux not in relatedList:
                    relatedList.append(movieNameAux)

        return relatedList
    return listMovieName
    
    
 
#Q4
'''
Your next task will be to fetch data from OMDB. The documentation 
for the API is at https://www.omdbapi.com/

Define a function called get_movie_data. It takes in one parameter 
which is a string that should represent the title of a movie you want
 to search. The function should return a dictionary with information 
 about that movie.

Again, use requests_with_caching.get(). For the queries on movies 
that are already in the cache, you won’t need an api key. You will
 need to provide the following keys: t and r. As with the TasteDive
 cache, be sure to only include those two parameters in order to 
 extract existing data from the cache.
'''

    
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
  

def get_movie_data(movieName, key="546c6742"):
    baseurl = "http://www.omdbapi.com/"
    params_d = {}
    params_d["t"] = movieName
    params_d["apikey"] = key
    params_d["r"] = "json"
    resp = requests.get(baseurl, params=params_d)
    print(resp.url)
    respDic = resp.json()
    return respDic 
temmp_data=get_movie_data("Venom")

#print(temmp_data['Ratings']['Source'])

temmp_data=get_movie_data("Venom")
#print(json.dumps(temmp_data,indent=3) )
#get_movie_data("Baby Mama") 

#Q5
'''
Please copy the completed function from above into this active 
code window. Now write a function called get_movie_rating. 
It takes an OMDB dictionary result for one movie and extracts
 the Rotten Tomatoes rating as an integer. For example, 
 if given the OMDB dictionary for “Black Panther”, 
 it would return 97. If there is no Rotten Tomatoes rating, return 0.
 '''
def get_movie_rating(movieNameJson):
    strRanting = ""
    for typeRantingList in movieNameJson["Ratings"]:
        if typeRantingList["Source"] == "Rotten Tomatoes":
            strRanting = typeRantingList["Value"]
    if strRanting != "":
        ranting = int(strRanting[:2])
        print('now the ranting',ranting)
    else:
        ranting = 0
    return ranting

get_movie_rating(get_movie_data("Deadpool 2"))
    
    

 #Q6
'''
Now, you’ll put it all together. Don’t forget to copy all of the 
functions that you have previously defined into this code window. 
Define a function get_sorted_recommendations. It takes a list of 
movie titles as an input. It returns a sorted list of related movie
 titles as output, up to five related movies for each input movie title. 
 The movies should be sorted in descending order by their Rotten Tomatoes
 rating, as returned by the get_movie_rating function. Break ties in 
 
 reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.
'''   

def get_sorted_recommendations(list):
    new_list = get_related_titles(list)
    new_dict = {}
    for i in new_list:
        rating = get_movie_rating(get_movie_data(i))
        new_dict[i] = rating
    print(new_dict)
    #print(sorted(new_dict, reverse=True))
    return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]


get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])


