import json
import random
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain


def create_search_query(text):
    # Randomly select an API key
    selected_key = json.load(open('apikeys.json', 'r'))['api_keys'][1]
    repo_id = "google/flan-t5-xxl"
    # Initialise model
    llm = HuggingFaceHub( huggingfacehub_api_token=selected_key,
        repo_id=repo_id, model_kwargs={"temperature": 1.2, "max_length": 1700})

    # create the template string
    template = """Instructions:\nCreate a search query for the text to get relevant images.\n\nText: Quantum computing is a multidisciplinary field comprising aspects of computer science, physics, and mathematics that utilizes quantum mechanics to solve complex problems faster than on classical computers.\nSearch Query: Quantum Computing\n\nText: {text}\nSearch Query:"""

    # create prompt
    prompt = PromptTemplate(template=template, input_variables=["text"])

    # Create and run the llm chain
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    response = llm_chain.run(text=text).replace('\n', "")

    return response
