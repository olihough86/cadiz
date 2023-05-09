import os
import openai
from pathlib import Path
openai.api_key = os.getenv("OPENAI_API_KEY")

bootstap_file = open("Bootstap_Prompt.txt", "r")
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
loadloop = True
while loadloop == True:
    #print(response.choices[0].message.content)
    messages.append(response.choices[0].message)
    #attempt to parse the response
    print("attempting to parse the response")
    #print("The response contains " + str(len(response.choices[0].message.content.splitlines())) + " lines")
    # split the response into in a list os strings, the command shold be at index 0
    lstres = response.choices[0].message.content.split()
    if lstres[0] == "LOADFILE":
        print("LOADFILE command detected")
        print("The file path is " + lstres[1])
        print("attempting to open the file")
        file = Path( ".", lstres[1])
        filecontents = file.read_text()
        #print("Human: " + filecontents)
        messages.append({"role": "user", "content": filecontents})
        response = get_response(messages)
    else:
        print("LOADFILE command not detected, loading complete or not needed")
        #print(response.choices[0].message.content)
        # attempt to parse the response
        print("attempting to parse the response")
        #print("The response contains " + str(len(response.choices[0].message.content.splitlines())) + " lines")
        print(response.choices[0].message.content)
        loadloop = False