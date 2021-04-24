import requests 
import json 

# import statements
import requests_with_caching
import json
# import webbrowser

# apply for a flickr authentication key at http://www.flickr.com/services/apps/create/apply/?
# paste the key (not the secret) as the value of the variable flickr_key
flickr_key = 'yourkeyhere'

def get_flickr_data(tags_string):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = flickr_key # from the above global variable
    params_diction["tags"] = tags_string # must be a comma separated string to work correctly
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"] = 5
    params_diction["media"] = "photos"
    params_diction["format"] = "json"
    params_diction["nojsoncallback"] = 1
    flickr_resp = requests_with_caching.get(baseurl, params = params_diction, permanent_cache_file="flickr_cache.txt")
    # Useful for debugging: print the url! Uncomment the below line to do so.
    print(flickr_resp.url) # Paste the result into the browser to check it out...
    return flickr_resp.json()

result_river_mts = get_flickr_data("river,mountains")

# Some code to open up a few photos that are tagged with the mountains and river tags...

photos = result_river_mts['photos']['photo']
for photo in photos:
    owner = photo['owner']
    photo_id = photo['id']
    url = 'https://www.flickr.com/photos/{}/{}'.format(owner, photo_id)
    print(url)
    # webbrowser.open(url)
    
    
import requests
import requests_cache

requests_cache.install_cache()    


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
                 print(item3['Name'])
                 tem_name=item3['Name']
                 print(tem_name)
                 movie_tilt.append(tem_name)
                 
           
    return movie_tilt

    
extract_movie_titles("Black Panther")        
    
    






    
    