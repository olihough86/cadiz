import os
import openai

# getthe API key and organization ID from the environment variables
openai.organization = os.getenv("OPENAI_ORG_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")

bootstap_file = open("Bootstap_Prompt.txt.md", "r")
bootstrap_prompt = bootstap_file.read()
bootstap_file.close() 

messages = [{"role": "system", "content": bootstrap_prompt}]

def get_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
)
    return response

# this is a test chat
print("Starting chat...")
print("sending a test message")
userMessage = "what is your name?"
messages.append({"role": "user", "content": userMessage})
print("Human: " + userMessage)
response = get_response(messages)
print(response.choices[0].message.content)
messages.append(response.choices[0].message)
userMessage = "check our financials"
messages.append({"role": "user", "content": userMessage})
print("Human: " + userMessage)
response = get_response(messages)
print(response.choices[0].message.content)
messages.append(response.choices[0].message)

# attempt to parse the response
print("attempting to parse the response")
print("The response conintains " + str(len(response.choices[0].message.content.splitlines())) + " lines")