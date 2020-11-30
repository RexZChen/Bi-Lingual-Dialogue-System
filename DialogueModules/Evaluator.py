"""
authors: Zirong Chen, Haotian Xue
Evaluator for Dialogue System

11/27/2020
"""
from utils import bcolors, Sigmoid


class Evaluator(object):
    def __init__(self, num_of_turns, task_reward, turn_penalty, score_factor):
        self.num_of_turns = num_of_turns
        self.task_completion = False
        self.task_reward = task_reward
        self.turn_penalty = turn_penalty
        self.user_experience = None
        self.user_name = "anonymous"
        self.score_factor = Sigmoid(score_factor)

    def getScores(self):
        self.user_name = input(f"{bcolors.OKCYAN}What is your preferred name? {bcolors.ENDC}")
        self.user_experience = int(input(f"{bcolors.OKCYAN}What is your rate for using this system (0-10)? {bcolors.ENDC}"))
        # if self.user_experience > 10 or self.user_experience < 0:
        #     raise ValueError("Invalid input, please choose a correct one")
        if self.user_experience > 10 or self.user_experience < 0:
            print("Invalid input, please choose a correct one between 0-10")
            self.user_experience = int(
                input(f"{bcolors.OKCYAN}What is your rate for using this system (0-10)? {bcolors.ENDC}"))
        self.task_completion = True if input(
            f"{bcolors.OKCYAN}Did this system help you solve your problem? Y for yes, N for no {bcolors.ENDC}") == "Y" else False

        turn_score = self.turn_penalty * self.num_of_turns
        task_score = self.task_reward if self.task_completion else -self.task_reward
        user_score = self.user_experience
        total_score = user_score * self.score_factor + (turn_score + task_score) * (1 - self.score_factor)

        fname = "UserScores/{}.txt".format(self.user_name)
        with open(fname, 'a+', encoding='utf-8') as f:
            f.write(str(total_score) + ", ")

        return total_score
