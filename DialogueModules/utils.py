"""
authors: Zirong Chen; Haotian Xue
Utils for Dialogue, including Discriminator, Translator and User Interfaces

23/11/2020
"""
import translators as ts
import random
import os
import numpy as np


def typeIn():
    return input(f"{bcolors.OKBLUE}Enter your sentence here: {bcolors.ENDC}")


class Discriminator(object):
    def __init__(self):
        self.languages = "en_zh"
        self.utterance = None

    def getLanguage(self):
        return self.languages

    def getUtterance(self):
        return self.utterance

    def load(self, utterance, languages):
        self.utterance = utterance
        if languages == "zh_en" or "en_zh":
            self.languages = languages
        else:
            raise NotImplementedError

    def tell(self):
        for char in self.utterance:
            if '\u4e00' <= char <= '\u9fff':
                # detect zh
                return "zh"
            else:
                return "en"


class GoogleTranslator(object):
    def __init__(self, utterance, src, dest):
        self.src = src
        self.dest = dest
        self.utterance = utterance

    def getTranslation(self):
        return ts.google(self.utterance, from_language=self.src, to_language=self.dest)


class BingTranslator(object):
    def __init__(self, utterance, src, dest):
        self.src = src
        self.dest = dest
        self.utterance = utterance

    def getTranslation(self):
        return ts.bing(self.utterance, from_language=self.src, to_language=self.dest)


def randomizeAction(file):
    template = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            template.append(line)
    index = random.randint(0, len(template) - 1)
    return str(template[index])


def initializeRes(dir):
    for file in os.listdir(dir):
        fname = dir + file
        os.remove(fname)
    open(dir + 'bread.txt', 'w')
    open(dir + 'cheese.txt', 'w')
    open(dir + 'sauce.txt', 'w')
    open(dir + 'extra.txt', 'w')
    open(dir + 'vegetable.txt', 'w')


# Reference: https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def welcome():
    print(
        f"{bcolors.HEADER} ######################## Welcome to Bi-Lingual Ordering System! ########################{bcolors.ENDC} \n"
        f"{bcolors.HEADER} ########################### Authors: Zirong Chen, Haotian Xue ########################## {bcolors.ENDC} \n"
        f"{bcolors.OKGREEN} ------------------ ##### Check order details under DIR: TepRes/ ##### ------------------ {bcolors.ENDC} \n"
        f"{bcolors.OKGREEN} ------------------ ### Check score details under DIR: UserScores/ ### ------------------ {bcolors.ENDC} \n"
        f"{bcolors.OKBLUE} ### See the menu @ https://www.subway.com/en-US/MenuNutrition/Menu/BreadsAndToppings ###{bcolors.ENDC} \n"
        f"{bcolors.HEADER} ################################# NOW, TIME TO BEGIN! ################################## {bcolors.ENDC} \n"
    )


def Sigmoid(X):
    s = 1 / (1 + np.exp(-X))
    return s