import os
from extract_file_content import read_files, read_pdf
from generate_qa import automate_qa
from pipelines import pipeline
from pprint import pprint

user = "Esad" # mach daraus "Felix" dann müsste es bei dir gehen

if user == "Esad":
	# Esad path
	nlu_yml = "../chatbot/data/nlu.yml"
	domain_yml = "../chatbot/domain.yml"
	stories_yml = "../chatbot/data/stories.yml"
	chatbot_dir = "../chatbot"
	rasa_cmd = "rasa train"
else:
	# Felix path
	nlu_yml = "C:/Users/norha/Documents/Rasa/data/nlu.yml"
	domain_yml = "C:/Users/norha/Documents/Rasa/domain.yml"
	stories_yml = "C:/Users/norha/Documents/Rasa/data/stories.yml"
	chatbot_dir = "C:/Users/norha/Documents/Rasa"
	rasa_cmd = "start cmd /K rasa train"

yml_files = {
		"nlu_yml": nlu_yml,
		"domain_yml": domain_yml,
		"stories_yml": stories_yml
	}

# debug = True zeigt mehr infos an
debug = True 
print()
print("Please wait while the QA pairs are being created..")

# 1. nlp Modul laden
nlp = pipeline("question-generation")
print()

# 2. aus file den inhalt holen und als string speichern
filename = "guitar.pdf"
text = read_pdf(filename)
print("guitar.pdf gelesen:\n")
print(text, "\n") if debug else None

# 3. qa pairs generieren
qa_pairs = nlp(text)
print(qa_pairs, "\n") if debug else None

# 4. yml dateien füllen
automate_qa(text, qa_pairs, yml_files, filename)
print("yml files gefüllt.\n") if debug else None

# 5. Modell trainieren

print("Great success! Now the new model will be trained...\n")
os.chdir(chatbot_dir)
os.system(rasa_cmd)
print("Training new model...Please wait until CMD process\
is finished. Your new model will be in /models/")

"""
file = read_files()
print(file)
# aktuell muss man genau eine datei auswählen wegen performance
text = file["guitar.pdf"]
print(text)
"""
