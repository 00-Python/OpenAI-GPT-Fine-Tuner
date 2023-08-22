import requests
import openai
import os
import tiktoken

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Define your data
data = """
Your data here...
"""

# Initialize the OpenAI API client
openai.api_key = OPENAI_API_KEY

# Initialize the Tiktoken encoder for the corresponding model
encoder = tiktoken.encoding_for_model("gpt-3.5-turbo-0613")

# Encode the text and get the token count from the encoding
def count_tokens(text):
    encoding = encoder.encode(text)
    return len(encoding)

# Estimate cost based on token count
def estimate_cost(tokens):
    training_cost_per_1k_tokens = 0.008
    cost = (tokens / 1000) * training_cost_per_1k_tokens
    return cost

# Count tokens in the data
data_tokens = count_tokens(data)
print("Total tokens in data:", data_tokens)

# Estimate cost
data_cost = estimate_cost(data_tokens)
print("Estimated cost:", data_cost)
