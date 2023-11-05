from sentence_transformers import SentenceTransformer
import pinecone
import openai
import streamlit as st

# Set up your OpenAI API key (replace this with a more secure method)
openai.api_key = "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"

# Initialize Pinecone and Sentence Transformer
model = SentenceTransformer('all-MiniLM-L6-v2')
pinecone.init(api_key='de3defb8-3e52-4ccf-82b1-9d785b981ec5', environment='gcp-starter')
index = pinecone.Index('langchain-chatbot')

def find_match(input):
    try:
        input_em = model.encode(input).tolist()
        result = index.query(input_em, top_k=2, includeMetadata=True)
        return result['matches'][0]['metadata']['text']+"\n"+result['matches'][1]['metadata']['text']
    except Exception as e:
        st.error("An error occurred during the match finding process: " + str(e))
        return ""

def query_refiner(conversation, query):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Given the following user query and conversation log, formulate a question that would be the most relevant to provide the user with an answer from a knowledge base.\n\nCONVERSATION LOG: \n{conversation}\n\nQuery: {query}\n\nRefined Query:",
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response['choices'][0]['text']
    except Exception as e:
        st.error("An error occurred during query refinement: " + str(e))
        return ""

def get_conversation_string():
    try:
        conversation_string = ""
        for i in range(len(st.session_state['responses'])-1):
            conversation_string += "Human: "+st.session_state['requests'][i] + "\n"
            conversation_string += "Bot: "+ st.session_state['responses'][i+1] + "\n"
        return conversation_string
    except Exception as e:
        st.error("An error occurred while generating conversation string: " + str(e))
        return ""
