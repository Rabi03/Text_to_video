

def get_similiar_docs(query,index,k=4,score=False):
  if score:
    similar_docs = index.similarity_search_with_score(query,k=k)
  else:
    similar_docs = index.similarity_search(query,k=k)
  return similar_docs

def get_answer(query,chain,index):
  similar_docs = get_similiar_docs(query,index)
  # print(similar_docs)
  answer =  chain.run(input_documents=similar_docs, question=query)
  return  answer

def create_script(topic_name,chain,index):
    
    response=get_answer(topic_name,chain,index)

    return response
