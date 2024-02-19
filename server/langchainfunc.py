# Import necessary libraries
import os
from dotenv import load_dotenv
import songsearcher
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

class LangChainFunc:
    def __init__(self, song_name:str="", album_name:str="", artist_name:str=""):
        
        # Load environment variables
        load_dotenv(".env")
        openapikey = os.getenv("OPENAI_API_KEY")

        self.chat = ChatOpenAI(temperature=0, openai_api_key=openapikey)

        # Assuming your SongSearcher class has methods to retrieve song and album names
        self.song_name = song_name
        self.album_name = album_name
        self.artist_name = artist_name

        self.template = "You are a information generator thaat gives background information, song meanings and additional facts about the song about {input_song} by {input_artist} from the album {input_album}"

        self.system_message_prompt = SystemMessagePromptTemplate.from_template(self.template)
        self.human_template = "{input_song} is a song by {input_artist} from the album {input_album}"
        self.human_message_prompt = HumanMessagePromptTemplate.from_template(self.human_template)
        self.chat_prompt = ChatPromptTemplate.from_messages([self.system_message_prompt, self.human_message_prompt])
        
    def text_output(self):
        self.ai_message = self.chat.predict_messages(self.chat_prompt.format_prompt(input_song=self.song_name, input_album=self.album_name, input_artist=self.artist_name).to_messages())
        return self.ai_message
    
if __name__ == "__main__":
    langchainfunc = LangChainFunc("Cheating on you", "Cheating on you", "Charlie Puth")
    print(str(langchainfunc.text_output()))