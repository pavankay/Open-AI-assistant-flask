# Open-AI-assistant-flask
Framework for a Openai assistant api server to a html webpage

## About
In this repositary I use flask for this example however you can be switch it or take it out for your needs. 
I use the beta Assistant api with threads, messages, and runs. 

The thread object holds multiple message object so when you call the assistant it can look at the thread for contex. The thread object has a id atrobute of you to add messsages later.

The message object holds text so you can add it to the thread, you use the threads id to find which thread to add it to.

The run object is used for the exuction of a thread which means to make the assistant to look at the thread and see the last messsage to give a response. For the run object you need the id of the assistint, and the id of the thread.





## Prerequisites

Before you get started, ensure you have the following prerequisites:
- MAKE SURE you have [Python](https://www.python.org/downloads/release/python-3120/) **3.12** installed and on PATH
- Get an ApI key from [OpenAi Api keys](https://platform.openai.com/api-keys) and paste it into the .env file
- Install the the nessecary requirements in python:
   ```bash
        pip3 install openai, load_dotenv, flask==2.2.5

## Getting started

- Clone this respostiry
- Make sure you have everything in the prerequisites
- Go to your directory in your terminal and run:
   ```bash
       python3 app.py
- Make sure the links in the html and python is correct for your directory

#### Short notes
- Change the use of your assistant for your needs at the top of the python file
- Depending on your subscription for your Openai acount use diffrent models so you wont get errors. You can switch the line to be:
 ```bash
     model="gpt-3.5-turbo",
 ```
 or other models depending on your needs for your project
- For each call you need pay check this [pricing](https://openai.com/pricing#language-models) for details

  
