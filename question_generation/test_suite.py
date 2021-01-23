import yaml

nlu_yml = "../chatbot/data/nlu.yml"
domain_yml = "../chatbot/domain.yml"
stories_yml = "../chatbot/data/stories.yml"
chatbot_dir = "../chatbot"

yml_files = {
	"nlu_yml": nlu_yml,
	"domain_yml": domain_yml,
	"stories_yml": stories_yml
}

qa_pairs = [{'answer': 'six', 'question': 'How many strings does the guitar usually have?'}, {'answer': 'strumming or plucking the strings with either a guitar pick or the fingers/fingernails of one hand', 'question': 'How is the guitar played with both hands?'}, {'answer': 'hollow chamber', 'question': 'What is the sound of the vibrating strings projected by?'}, {'answer': 'wood', 'question': 'What type of wood is the guitar traditionally constructed from?'}, {'answer': 'the archtop guitar', 'question': 'What type of guitar is sometimes called a "jazz guitar"?'}, {'answer': "the strings' vibration", 'question': 'What is the tone of an acoustic guitar produced by?'}, {'answer': 'finger-picking', 'question': 'What technique is used to play a guitar as a solo instrument?'}, {'answer': 'folk, blues, bluegrass, and country guitar playing in the United States', 'question': 'What does the term "finger-picking" refer to?'}, {'answer': 'one octave below a regular guitar', 'question': 'How is the acoustic bass guitar pitched?'}, {'answer': 'Electric guitars', 'question': 'What type of guitars use an amplifier and a loudspeaker that makes the sound of the instrument loud enough for the performers and audience to hear'}]

from pprint import pprint




