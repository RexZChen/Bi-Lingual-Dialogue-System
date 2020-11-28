"""
authors: Zirong Chen; Haotian Xue
Main Session for Dialogue

23/11/2020
"""
from utils import GoogleTranslator, typeIn, Discriminator, initializeRes
import DialogueManagement
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--num_of_turns", default=10, type=int)
parser.add_argument("--reward_factor", default=20, type=int)

arg = parser.parse_args()

initializeRes('TempRes/')

lastIntent = 'bread'
warning = False

for i in range(arg.num_of_turns):
    utterance = typeIn()
    ## NLU ##
    discriminator = Discriminator()
    discriminator.load(utterance=utterance, languages="zh_en")
    NLU_detection = discriminator.tell()
    print("Current language:", NLU_detection)
    if discriminator.tell() == 'en':  # when no translation is needed, which should be "en" in this case.
        NLU_translation = utterance
    else:  # when translation from zh to en is needed.
        NLU_translation = GoogleTranslator(utterance=utterance, src='zh', dest='en').getTranslation().lower()
        # print(NLU_translation)

    ## DM ##
    DM = DialogueManagement.DialogueManager()
    DM.load(NLU_translation)
    _, _, warning = DM.tell()
    if warning:
        print("This system currently can not understand your input, and your input and help is now learnt")
        print("This conversation will be terminated. Please restart this system...")
        break

    action, lastIntent = DM.getAction(lastIntent=lastIntent)  # default english

    ## NLG ##
    NLG_translation = GoogleTranslator(utterance=action, src='en', dest=NLU_detection).getTranslation()
    print(NLG_translation)
    if lastIntent == 'conclusion':
        conclusion = DM.getConclusion()
        NLG_translation = GoogleTranslator(utterance=conclusion, src='en', dest=NLU_detection).getTranslation()
        print(NLG_translation)
        break
