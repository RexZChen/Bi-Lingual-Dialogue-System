from utils import GoogleTranslator, BingTranslator
from DialogueManagement import DialogueManager

txt = 'hi'

DM = DialogueManager()
DM.load(utterance=txt)
print(DM.tell())



