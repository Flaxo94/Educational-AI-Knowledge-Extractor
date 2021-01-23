import yaml


def automate_qa(text, nlp):
        # nlp = pipeline("question-generation")
        qa_pairs = nlp(text)
        #print(nlp(text))

        for i, elem in enumerate(qa_pairs):

                q = elem["question"]
                a = elem["answer"]
                intent = "qa_" + str(i)
                utter = "utter_" + intent
                story = intent + " path"

                # Neuen intent erstellen

                with open("C:/Users/norha/Documents/Rasa/data/nlu.yml", "r") as file:

                        data = yaml.load(file, Loader=yaml.FullLoader)
                        for i in data["nlu"]:
                                if i["intent"] == intent:
                                        break
                        else:
                                data["nlu"].append({"intent": intent, "examples": "- " + q})
                        

                with open("C:/Users/norha/Documents/Rasa/data/nlu.yml", "w") as file:
                        yaml.dump(data, file)

                # In domain.yml neuen intent & repsonse einfügen:
                with open("C:/Users/norha/Documents/Rasa/domain.yml", "r") as file:

                        data = yaml.load(file, Loader=yaml.FullLoader)
                        for i in data["intents"]:
                                if i == intent:
                                        break
                        else:
                                data["intents"].append(intent)
                                data["responses"].update({utter: [{"text": a}]})			

                with open("C:/Users/norha/Documents/Rasa/domain.yml", "w") as file:
                        yaml.dump(data, file)

                # neue story einfügen

                with open("C:/Users/norha/Documents/Rasa/data/stories.yml", "r") as file:

                        data = yaml.load(file, Loader=yaml.FullLoader)
                        
                        for i in data["stories"]:
                                if i["story"] == story:
                                        break
                        else:
                                data["stories"].append({"story": story, "steps": [{"intent": intent}, {"action": utter}]})

                with open("C:/Users/norha/Documents/Rasa/data/stories.yml", "w") as file:
                        yaml.dump(data, file)

