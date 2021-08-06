from flask import Flask, jsonify, os
from programy.clients.embed.datafile import EmbeddedDataFileBot
import random

file = {
  'aiml': ['./storage/categories'],
  'denormals': './storage/lookups/denormal.txt',
  'normals': './storage/lookups/normal.txt',
  'genders': './storage/lookups/gender.txt',
  'persons': './storage/lookups/person.txt',
  'person2s': './storage/lookups/person2.txt',
  'regexes': './storage/regex/regex-templates.txt',
  'dynamics': ['./storage/dynamics'],
  'conversations': ['./storage/conversations'],
  'properties': './config/properties.txt',
}
logging = './config/logging.yaml'
error_message = [
  'I have no idea what that means.',
  'What does that mean?',
  'Is that even English?',
  'Idk what that means, leave me alone.',
  'Speak clearly',
  'Idk what to tell you chief.',
  'I hate you sometimes.',
  'Why are you like this?',
  'Uhhh try again please.',
  'What do you mean?',
  ''
]

aiml = EmbeddedDataFileBot(file, defaults=True, logging_filename=logging)
app = Flask(__name__)

@app.route('/', methods=['GET'])	
def home():
  return  "I'm alive"

def ask_question_(self, context, question):
  client_context = self.create_client_context(context)
  ques = self.process_question(client_context, question)
  resp = self.renderer.render(client_context, ques)
  return resp

@app.route('/context/<string:context>/question/<string:question>', methods=['GET'])
def add(context, question):
  print(context)
  print(question)
  try:
    aiml.ask_question = ask_question_.__get__(aiml, EmbeddedDataFileBot)
    response = aiml.ask_question(str(context), question[1:][:-1])
  except:
    response = aiml.ask_question(str(context), question[1:][:-1])
  if response == None:
    response = random.choice(error_message) + ' <:borryWeird:732920361179414578>'
  print(response)
  return jsonify({"success":  response})

def run():
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
  run()