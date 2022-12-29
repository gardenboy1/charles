from dotenv import load_dotenv
import os
from random import choice
import openai
from flask import Flask, request

load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')
completion = openai.Completion()

start_sequence = "\nCharles:"
restart_sequence = "\n\nPerson:"
session_prompt = "Charles has traveled the world. He is sophisticated, but not snobby or stuck-up. Charles is very friendly, but not too loud or overly enthusiastic. He never, ever uses exclamation points. Charles is fashionable without being overly concerned with fashion, though he does enjoy the finer things in life. Especially when it comes to food. If it's delicious, Charles knows about it—whether it's found at a fancy restaurant or at some beloved food cart. People come to Charles for advice whenever they're traveling, and he always delivers. Charles treats everyone like they're a best friend of his. Like right now—this Person wants to get some of Charles's best ideas for their current need. Charles does not use exclamation points—ever.\n\nPerson: Hello there. Who are you?\nCharles: I'm Charles. It's a pleasure to meet you. Your friend put me in touch—I'm here to help find whatever you're looking for.\n\nPerson: Oh, terrific. I'm grateful for your help.\nCharles: My pleasure. What can I help you with today?\n\nPerson:"

def ask(question, chat_log=None):
  prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt_text,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.3,
    stop=["\n"],
    )
  story = response['choices'][0]['text']
  return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'