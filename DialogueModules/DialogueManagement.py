import os
import random
from utils import randomizeAction, initializeRes


class DialogueManager(object):
    def __init__(self):
        self.utterance = None
        self.namespace = [file[:-4] for file in os.listdir('IntentDetails/')]

    def load(self, utterance):
        self.utterance = utterance

    def getNamespace(self):
        return self.namespace

    def tell(self):
        flag = "UKN"
        keyword = None
        initial_utterance = self.utterance.lower()
        utterance = initial_utterance.split(" ")

        reference = {}
        for name in self.namespace:
            fname = 'IntentDetails/{}.txt'.format(name)
            with open(fname, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    reference[name] = line.split(", ")

        for intent in reference.keys():
            for option in reference[intent]:
                if option in utterance:
                    keyword = option
                    flag = intent

        # Human-in-loop error handling
        # TODO: new intentions need to be fixed
        if flag == 'UKN':
            namestring = ""
            for name in self.namespace:
                namestring = namestring + name + ", "

            intent = input("Fail to map this sentence: \" {} \" to existing intents: {} what is your idea on this? \n ".format(initial_utterance, namestring))
            fname = 'IntentDetails/{}.txt'.format(intent)

            with open(fname, 'a+', encoding='utf-8') as f:
                f.write(initial_utterance + ", ")
                flag = intent

            if intent not in self.namespace:
                self.namespace.append(intent)

        return flag, keyword

    def getAction(self):
        """
        Default Dialogue path: Greet+Bread -> Cheese -> Vegetable -> Sauce -> Extra -> Farewell
        :return:
        """
        flag, keyword = self.tell()
        if flag == 'greet':
            return randomizeAction('DialogueTemplates/greet.txt')

        if flag == 'bread':
            fname = 'TempRes/{}.txt'.format(flag)
            with open(fname, 'a+', encoding='utf-8') as f:
                f.write(keyword)

            return randomizeAction('DialogueTemplates/additionCheese_Bread.txt').format(keyword, flag)

        if flag == 'cheese':
            fname = 'TempRes/{}.txt'.format(flag)
            with open(fname, 'a+', encoding='utf-8') as f:
                f.write(keyword)

            return randomizeAction('DialogueTemplates/additionVegetable_Cheese.txt').format(keyword, flag)

        if flag == 'vegetable':
            fname = 'TempRes/{}.txt'.format(flag)
            with open(fname, 'a+', encoding='utf-8') as f:
                f.write(keyword)

            return randomizeAction('DialogueTemplates/additionSauce_Vegetable.txt').format(keyword, flag)

        if flag == 'sauce':
            fname = 'TempRes/{}.txt'.format(flag)
            with open(fname, 'a+', encoding='utf-8') as f:
                f.write(keyword)

            return randomizeAction('DialogueTemplates/additionExtra_Sauce.txt').format(keyword, flag)

        if flag == 'extra':
            fname = 'TempRes/{}.txt'.format(flag)
            with open(fname, 'a+', encoding='utf-8') as f:
                f.write(keyword)

            return randomizeAction('DialogueTemplates/Conclusion_Extra.txt').format(keyword, flag)