import os
from extract_file_content import read_files
from generate_qa import automate_qa
from pipelines import pipeline
from pprint import pprint

print("Please wait while the QA pairs are being created..")
nlp = pipeline("question-generation")
file = read_files()
# aktuell muss man genau eine datei auswählen wegen performance
text = file["guitar.pdf"]
automate_qa(text, nlp)
print("Great success! Now the new model will be trained...")
# füg deinen pfad ein
os.chdir('C:\\Users\\norha\\Documents\\Rasa')
os.system('start cmd /K rasa train')
print("Training new model...Please wait until CMD process\
is finished. Your new model will be in /models/")
