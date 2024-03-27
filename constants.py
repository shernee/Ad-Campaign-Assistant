import os

embedding_model = 'sentence-transformers/all-MiniLM-l6-v2'
llama_model = 'meta-llama/Llama-2-7b-chat-hf'
sd_model = '' # path to stable diffusion model

OPENAI_AUTH = os.environ['OPENAI_API_KEY']
PINECONE_AUTH = os.environ['PINECONE_API_KEY']
HF_AUTH = os.environ['HF_TOKEN']
REPLICATE_AUTH = os.environ['REPLICATE_API_TOKEN']
