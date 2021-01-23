import yaml
from copy import deepcopy

def automate_qa(text, qa_pairs, yml_files, filename):
	
	filename = filename.split(".")[0]

	# Relevante Dateien einlesen
	with open(yml_files["nlu_yml"], "r") as file:
		data_nlu = yaml.load(file, Loader=yaml.FullLoader)

	with open(yml_files["domain_yml"], "r") as file:
		data_domain = yaml.load(file, Loader=yaml.FullLoader)	

	with open(yml_files["stories_yml"], "r") as file:
		data_stories = yaml.load(file, Loader=yaml.FullLoader)
	
	# Kopien erstellen mit deepcopy
	out_data_nlu = deepcopy(data_nlu)
	out_data_domain = deepcopy(data_domain)
	out_data_stories = deepcopy(data_stories)


	for i, elem in enumerate(qa_pairs):

		q = elem["question"]
		a = elem["answer"]
		intent = f"qa_{filename}_{i}"
		utter = f"utter_{intent}"
		story = f"{intent} path"
		
		# Neuen intent erstellen
		for i in data_nlu["nlu"]:
			if i["intent"] == intent:
				break
		else:
			out_data_nlu["nlu"].append({"intent": intent, "examples": "- " + q})

		# In domain.yml neuen intent & repsonse einfügen:
		for i in data_domain["intents"]:

			if intent in i:
				break
		else:
			out_data_domain["intents"].append({intent: {"use_entities": True}})
			out_data_domain["responses"].update({utter: [{"text": a}]})

		# neue story einfügen
		for i in data_stories["stories"]:
			
			if i["story"] == story:
				break
		else:
			out_data_stories["stories"].append({"story": story, "steps": [{"intent": intent}, {"action": utter}]})


	# die veränderten datensätze in die zugehörigen yml files schreiben	
	with open(yml_files["nlu_yml"], "w") as file:
		yaml.dump(out_data_nlu, file)

	with open(yml_files["domain_yml"], "w") as file:
		yaml.dump(out_data_domain, file)

	with open(yml_files["stories_yml"], "w") as file:
		yaml.dump(out_data_stories, file)