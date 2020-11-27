"""
authors: Zirong Chen; Haotian Xue
Main Session for Dialogue

23/11/2020
"""
from utils import GoogleTranslator, typeIn, Discriminator, initializeRes
import DialogueManagement
import argparse
from colorModule import bcolors
from Evaluator import Evaluator

parser = argparse.ArgumentParser()

parser.add_argument("--num_of_turns", default=10, type=int)
parser.add_argument("--task_reward", default=20, type=int)
parser.add_argument("--turn_penalty", default=-1, type=int)

arg = parser.parse_args()

initializeRes('TempRes/')

lastIntent = 'bread'
warning_time = 0
end_of_truns = 0

for i in range(arg.num_of_turns):
    end_of_truns = i
    utterance = typeIn()
    ## NLU ##
    discriminator = Discriminator()
    discriminator.load(utterance=utterance, languages="zh_en")
    NLU_detection = discriminator.tell()
    print(f"{bcolors.OKGREEN}Current language detected:{bcolors.ENDC} ", NLU_detection)

    if discriminator.tell() == 'en':  # when no translation is needed, which should be "en" in this case.
        NLU_translation = utterance
    else:  # when translation from zh to en is needed.
        NLU_translation = GoogleTranslator(utterance=utterance, src='zh', dest='en').getTranslation().lower()
        # print(NLU_translation)

    ## DM ##
    DM = DialogueManagement.DialogueManager()
    DM.load(NLU_translation)

    action, lastIntent = DM.getAction(lastIntent=lastIntent)  # default english
    if DM.warning:
        warning_time += 1

    ## NLG ##
    NLG_translation = GoogleTranslator(utterance=action, src='en', dest=NLU_detection).getTranslation()
    print(NLG_translation)
    if lastIntent == 'conclusion':
        conclusion = DM.getConclusion()
        NLG_translation = GoogleTranslator(utterance=conclusion, src='en', dest=NLU_detection).getTranslation()
        print(NLG_translation)
        break

print("--------------- Evaluation Begins ---------------")
num_of_turns = (end_of_truns + 1) + (2 * warning_time)
# num_of_turns, task_reward, turn_penalty
Evaluator = Evaluator(num_of_turns=num_of_turns, task_reward=arg.task_reward, turn_penalty=arg.turn_penalty)
print(f"{bcolors.OKGREEN}Here is the score of this system in your task: {bcolors.ENDC}", str(Evaluator.getScores()))
