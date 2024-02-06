from functions.create_search_query_function import create_search_query
from functions.get_image_function import get_image


def create_audio_image(topic_name,script, character_name, timestamp,imageModel,tokenizer,images,img_arr):

    list = script.split(".")
    search_dict = {}
    print(list)
    for i in list:
        if len(i)>0:
            
            search_query =f'{topic_name}-{i}'.lstrip().rstrip()
            if search_query in search_dict:
                search_dict[search_query] += 1
            else:
                search_dict[search_query] = 1

    count = 0
    img_added=[]
    for key, value in search_dict.items():
        get_image(key, value, timestamp, count,imageModel,tokenizer,images,img_arr,character_name,img_added)
        count = count + value
