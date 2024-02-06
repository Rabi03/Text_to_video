import requests
import json

searchTerm = 'machine learning'
startIndex = '1'
key = 'AIzaSyCDswolGOTGj_B4hGI0k1GuprSmK5EJ95A'
cx = '47c60e0f85ff14ba9'
searchUrl = "https://www.googleapis.com/customsearch/v1?q=" + \
    searchTerm + "&start=" + startIndex + "&key=" + key + "&cx=" + cx + \
    "&searchType=image"
r = requests.get(searchUrl)
response = r.content.decode('utf-8')
result = json.loads(response)

print(result)