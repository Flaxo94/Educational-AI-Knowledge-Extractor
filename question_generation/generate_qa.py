import yaml

def automate_qa(text, qa_pairs, yml_files):
        # nlp = pipeline("question-generation")
        
        #print(nlp(text))

        for i, elem in enumerate(qa_pairs):

                q = elem["question"]
                a = elem["answer"]
                intent = "qa_" + str(i)
                utter = "utter_" + intent
                story = intent + " path"

                # Neuen intent erstellen
                
                with open(yml_files["nlu_yml"], "r") as file:

                        data = yaml.load(file, Loader=yaml.FullLoader)
                        for i in data["nlu"]:
                                if i["intent"] == intent:
                                        break
                        else:
                                data["nlu"].append({"intent": intent, "examples": "- " + q})
                        

                with open(yml_files["nlu_yml"], "w") as file:
                        yaml.dump(data, file)

                # In domain.yml neuen intent & repsonse einfügen:
                with open(yml_files["domain_yml"], "r") as file:

                        data = yaml.load(file, Loader=yaml.FullLoader)
                        for i in data["intents"]:
                                print(i)
                                if i == intent:
                                        break
                        else:
                                data["intents"].update({intent: {"use_entities": True}})
                                data["responses"].update({utter: [{"text": a}]})			

                with open(yml_files["domain_yml"], "w") as file:
                        yaml.dump(data, file)

                # neue story einfügen

                with open(yml_files["stories_yml"], "r") as file:

                        data = yaml.load(file, Loader=yaml.FullLoader)
                        
                        for i in data["stories"]:
                                if i["story"] == story:
                                        break
                        else:
                                data["stories"].append({"story": story, "steps": [{"intent": intent}, {"action": utter}]})

                with open(yml_files["stories_yml"], "w") as file:
                        yaml.dump(data, file)


