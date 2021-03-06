"""
authors: Zirong Chen; Haotian Xue
Main Session for Dialogue

23/11/2020
"""
from utils import GoogleTranslator, typeIn, Discriminator, initializeRes, bcolors, welcome, BingTranslator
import DialogueManagement
import argparse
from Evaluator import Evaluator

parser = argparse.ArgumentParser()

parser.add_argument("--num_of_turns", default=10, type=int)
parser.add_argument("--task_reward", default=20, type=int)
parser.add_argument("--turn_penalty", default=-1, type=int)
parser.add_argument("--score_factor", default=2, type=int)
parser.add_argument("--translator", default='bing', type=str)

arg = parser.parse_args()

initializeRes('TempRes/')

lastIntent = 'bread'
warning_time = 0
end_of_turns = 0

welcome()

# if arg.translator == 'bing' or 'Bing':
#     Translator = BingTranslator
# if arg.translator == 'google' or 'Google':
#     Translator = GoogleTranslator

for i in range(arg.num_of_turns):
    end_of_turns = i
    utterance = typeIn()
    ## NLU ##
    discriminator = Discriminator()
    discriminator.load(utterance=utterance, languages="zh_en")
    NLU_detection = discriminator.tell()
    print(f"{bcolors.OKGREEN}Current language detected:{bcolors.ENDC} ", NLU_detection)

    if discriminator.tell() == 'en':  # when no translation is needed, which should be "en" in this case.
        NLU_translation = utterance
    else:  # when translation from zh to en is needed.
        NLU_translation = BingTranslator(utterance=utterance, src='zh', dest='en').getTranslation().lower()
        # print(NLU_translation)

    ## DM ##
    DM = DialogueManagement.DialogueManager()
    DM.load(NLU_translation)

    action, lastIntent = DM.getAction(lastIntent=lastIntent)  # default english
    if DM.warning:
        warning_time += 1

    ## NLG ##
    NLG_translation = BingTranslator(utterance=action, src='en', dest=NLU_detection).getTranslation()
    print(NLG_translation)
    if lastIntent == 'conclusion':
        conclusion = DM.getConclusion()
        NLG_translation = BingTranslator(utterance=conclusion, src='en', dest=NLU_detection).getTranslation()
        print(NLG_translation)
        break

    if end_of_turns + 2 * warning_time > arg.num_of_turns:
        print(f"{bcolors.WARNING}Turns were used up in this task! {bcolors.ENDC}")
        break

print("--------------- Evaluation Begins ---------------")
num_of_turns = (end_of_turns + 1) + (2 * warning_time)
# num_of_turns, task_reward, turn_penalty
Evaluator = Evaluator(num_of_turns=num_of_turns, task_reward=arg.task_reward, turn_penalty=arg.turn_penalty, score_factor=arg.score_factor)
print(f"{bcolors.OKGREEN}Here is the score of this system in your task: {bcolors.ENDC}", str(Evaluator.getScores()))
