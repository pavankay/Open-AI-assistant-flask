from openai import OpenAI
import time
import json
from flask import Flask, request, jsonify,  render_template
import os
from dotenv import load_dotenv

load_dotenv()  

app = Flask(__name__)
MATH_ASSISTANT_ID = None

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



def show_json(data):
    if hasattr(data, 'to_dict'):
        data_dict = data.to_dict()
    else:
        data_dict = data.__dict__
    print(json.dumps(data_dict, indent=4))

@app.before_first_request
def create_assistant():
    global MATH_ASSISTANT_ID
    assistant = client.beta.assistants.create(
        name="Math Tutor",
        instructions="You are a personal math tutor. Answer questions briefly, in a sentence or less.",
        model="gpt-4-1106-preview",
    )
    MATH_ASSISTANT_ID = assistant.id
    show_json(assistant)

def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

def submit_message(assistant_id, thread, user_message):
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=user_message
    )
    return client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )

def get_response(thread):
    return client.beta.threads.messages.list(thread_id=thread.id, order="asc")

def asstinat_response(thread):
    thread_messages=client.beta.threads.messages.list(thread_id=thread.id, order="desc")
    response = thread_messages.data[0].content[0].text.value

    return response
def create_thread_and_run(user_input):
    thread = client.beta.threads.create()
    run = submit_message(MATH_ASSISTANT_ID, thread, user_input)
    return thread, run

def pretty_print(messages):
    print("# Messages")
    for m in messages:
        print(f"{m.role}: {m.content[0].text.value}")
    print()

@app.route('/')
def index():
    return render_template('index.html')

thread_counter=0
run1=None
thread1=None
response=None

thread1 = client.beta.threads.create()


@app.route('/send_message', methods=['POST'])
def send_message():

    data = request.json
    user_message = data['message']
    global run1
    global thread1

    run1=submit_message(MATH_ASSISTANT_ID, thread1, user_message)

    run1 = wait_on_run(run1, thread1)
    response = asstinat_response(thread1)
    pretty_print(get_response(thread1))

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

