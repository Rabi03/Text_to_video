from fastapi import FastAPI, HTTPException, Request, Depends, File
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from functions.video_main_function import video_main
from transformers import CLIPProcessor, CLIPModel,CLIPTokenizerFast
import torch
from PIL import Image
import glob
import numpy as np
import json,os
import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.llms import GooseAI,HuggingFaceHub
from langchain import PromptTemplate, LLMChain

selected_key = json.load(open('apikeys.json', 'r'))['api_keys'][0]
os.environ["GOOSEAI_API_KEY"] = selected_key

embeddings = HuggingFaceEmbeddings()
# initialize pinecone
pinecone.init(
    api_key="19070c59-c72b-4823-979a-981b0807db95",  # fbaa593a-f83a-42d5-b2ed-d33e86abca6d
    environment="us-west1-gcp-free"  #  us-west4-gcp-free
)

index_name = "450"
index=Pinecone.from_existing_index(index_name=index_name,embedding=embeddings)

llm = GooseAI()
from langchain.chains.question_answering import load_qa_chain
chain = load_qa_chain(llm, chain_type="stuff")


imageFiles = json.load(open('F:/450 project/Project/backend/imageName.json'))
location='F:/450 project/Project/backend/'
app = FastAPI()
security = HTTPBasic()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_id = "openai/clip-vit-base-patch32"

tokenizer = CLIPTokenizerFast.from_pretrained(model_id)
processor = CLIPProcessor.from_pretrained(model_id)
imageModel = CLIPModel.from_pretrained(model_id)

# move model to device if possible
device = 'cuda' if torch.cuda.is_available() else 'cpu'

imageModel.to('cpu')

images = []
for f in imageFiles:
    images.append(Image.open(location+f))

img_arr=np.load("images_index_1.2.npy")

@app.post("/videoCreate")
async def create_insights(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    
    data = await request.json()
    message = data['message']
    characterName = data['characterName']

    path = video_main(message,characterName,imageModel,tokenizer,images,img_arr,chain,index)
    return FileResponse(path, media_type="video/mp4")
