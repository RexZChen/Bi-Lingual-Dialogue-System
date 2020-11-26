"""
authors: Zirong Chen; Haotian Xue
Utils for Dialogue

23/11/2020
"""
import translators as ts
import random
import os


def typeIn():
    return input("enter your sentence here: ")


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


class BertTranslator(object):
    pass


class GoogleTranslator(object):
    def __init__(self, utterance, src, dest):
        self.src = src
        self.dest = dest
        self.utterance = utterance

    def getTranslation(self):
        return ts.google(self.utterance, from_language=self.src, to_language=self.dest)


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