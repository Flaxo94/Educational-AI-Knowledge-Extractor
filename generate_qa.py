from question_generation.pipelines import pipeline
import yaml


nlp = pipeline("question-generation")

text = "42 is the answer to life, the universe and everything."
text = "A chatbot is a software application used to conduct an on-line chat conversation via text or text-to-speech, in lieu of providing direct contact with a live human agent. Designed to convincingly simulate the way a human would behave as a conversational partner, chatbot systems typically require continuous tuning and testing, and many in production remain unable to adequately converse or pass the industry standard Turing test. The term ChatterBot was originally coined by Michael Mauldin (creator of the first Verbot) in 1994 to describe these conversational programs."

qa_pairs = nlp(text)
#print(nlp(text))


for i, elem in enumerate(qa_pairs):

	q = elem["question"]
	a = elem["answer"]
	intent = "qa_" + str(i)
	utter = "utter_" + intent
	story = intent + " path"

	# Neuen intent erstellen

	with open("chatbot/data/nlu.yml", "r") as file:

		data = yaml.load(file, Loader=yaml.FullLoader)
		for i in data["nlu"]:
			if i["intent"] == intent:
				break
		else:
			data["nlu"].append({"intent": intent, "examples": "- " + q})
		

	with open("chatbot/data/nlu.yml", "w") as file:
		yaml.dump(data, file)

	# In domain.yml neuen intent & repsonse einfügen:
	with open("chatbot/domain.yml", "r") as file:

		data = yaml.load(file, Loader=yaml.FullLoader)
		for i in data["intents"]:
			if i == intent:
				break
		else:
			data["intents"].append(intent)
			data["responses"].update({utter: [{"text": a}]})			

	with open("chatbot/domain.yml", "w") as file:
		yaml.dump(data, file)

	# neue story einfügen

	with open("chatbot/data/stories.yml", "r") as file:

		data = yaml.load(file, Loader=yaml.FullLoader)
		
		for i in data["stories"]:
			if i["story"] == story:
				break
		else:
			data["stories"].append({"story": story, "steps": [{"intent": intent}, {"action": utter}]})

	with open("chatbot/data/stories.yml", "w") as file:
		yaml.dump(data, file)

