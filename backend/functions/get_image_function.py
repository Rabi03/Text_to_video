import numpy as np
from numpy.linalg import norm
import easyocr
from functions.create_speech_function import create_speech
from functions.create_text_image import text_to_image
reader = easyocr.Reader(['en'])

def my_progressbar(url, progress):
    print(url + " " + progress + "%")


def get_image(query, value, timestamp, count,imageModel,tokenizer,images,img_arr,character_name,img_added):
    character_dict = {'Benjamin': "en-GB-RyanNeural",
                      'Sophia': 'en-IE-EmilyNeural'}
    inputs = tokenizer(query, return_tensors="pt",max_length=77,truncation=True,padding=True)
    text_emb = imageModel.get_text_features(
    **inputs
    )
    img_arr = img_arr / np.linalg.norm(img_arr, axis=0)

    text_emb = text_emb.cpu().detach().numpy()
    scores = np.dot(text_emb, img_arr.T)
    cos_sim = np.dot(text_emb, img_arr.T) / (norm(text_emb, axis=1) * norm(img_arr, axis=1))
    top_k = 1
    # get the top k indices for most similar vecs
    idx = np.argsort(-cos_sim[0])[:top_k]
    if len(query)>0 and round(scores[0][idx[0]],2)<2.00:
        text_to_image(query,f'{timestamp}/images',f'{count}.jpg')
        create_speech(query, f'{timestamp}/audio/{count}.wav',
                            character_dict[character_name])
    elif len(query)>0 and idx[0] not in img_added:
        print(f"{idx[0]}: {scores[0][idx[0]]}")
        img_added.append(idx[0])
        texts=reader.readtext(images[idx[0]], detail=0)
        if len(texts)>0:
            textforVoice=" ".join(texts)
        else:textforVoice=query
        create_speech(textforVoice, f'{timestamp}/audio/{count}.wav',
                            character_dict[character_name])
        images[idx[0]].save(f'{timestamp}/images/{count}.jpg')
