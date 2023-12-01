# Open-AI-assistant-flask
Framework for a Openai assistant api server to a html webpage

## About
In this repositary I use flask for this example however you can be switch it or take it out for your needs. 
I use the beta Assistant api with threads, messages, and runs. 




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
  - For each call you need pay check this [link](https://openai.com/pricing#language-models)for details

  
