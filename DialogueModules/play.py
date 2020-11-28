from DialogueManagement import initializeRes
import DialogueManagement
#

# initializeRes("TempRes/")

DM = DialogueManagement.DialogueManager()
utterance = 'aa'
DM.load(utterance=utterance)
# print(DM.tell())
# print(DM.getAction(lastIntent=''))


# import os
# filePath = 'IntentDetails/'
# print(os.listdir(filePath))
# for file in os.listdir(filePath):
#     print(file[:-4])


