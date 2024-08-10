# Build a simple LLM application

# importing necessary modules
import os
import groq

from load_dotenv import load_dotenv
load_dotenv()


GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# instantiating a groq class - working with groq

# creating a client
groq_client = groq.Groq(api_key = GROQ_API_KEY)

sys_prompt = "You are a helpful virtual assistant, \
    your goal is to provide useful and relevant responses to my queries"

modes = [
    "llama-3.1-405b-reasoning", 
    "llama-3.1-70b-versatile", 
    "llama-3.1-8b-instant", 
    "mixtral-8x7b-32768"
]

# defining a function that takes a model as an argument
def generate(model, query):

    response = groq_client.chat.completion.create(
        model=model,
        messages=[
            {"role": "system", "content":sys_prompt},
            {"role": "user", "content": query}
        ],
        response_format = "text",
        temperature = 0.1
    )

