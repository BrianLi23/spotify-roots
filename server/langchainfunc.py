# Import necessary libraries
import os
from dotenv import load_dotenv
import songsearcher

from langchain.llms.huggingface_hub import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv(".env")

# Initialize your SongSearcher with a specific song
searcher = songsearcher.SongSearcher("Love Scenario", "track")

# Assuming your SongSearcher class has methods to retrieve song and album names
song_name = searcher.result["tracks"]["items"][0]["name"]
album_name = searcher.result["tracks"]["items"][0]["album"]["name"]

# Create a prompt template
template = """

Question: {query}

Context: You are a sophisticated song recommendation engine tasked with suggesting songs to a user based on their preferences. You have access to a vast library of songs and albums, and you can provide detailed explanations for your recommendations.

Answer:
"""
prompt = PromptTemplate(input_variables=['query'], template=template)

# Load a model
llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={
    'temperature': 0.9, 'max_length': 128
})

# Create and run a chain with your modified prompt
chain = LLMChain(prompt=prompt, llm=llm)

# Your query is now more focused on recommendations based on song and album
query = "What is a song I would enjoy if I like the song Love Scenario by iKON? Provide me an explanation of why I would like it"
out = chain.run({
    'query': query,
})
print(out)
