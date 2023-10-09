import const
import random
import time
import discord
import re


class Quiz():
    def __init__(self, content, client, quizLen=1):
        print(f'Making Quiz.')
        self.author = content.author
        self.client = client
        self.content = content
        self.number = quizLen
        self.answers = []
        self.correct = ""
        self.correctIndex = -1
        self.choices = self.get_question()
    
    async def start_quiz(self):
        print("Begin Quiz")
        await self.content.channel.send(f'Quiz Time!')
        random.shuffle(self.choices)
        index = self.choices.index(self.correct)
        self.correctIndex = index
        print(self.choices)
        print(f'{self.correctIndex}')
        await self.content.channel.send(f'Question 1: What term does this definiton describe: {const.DICT.get(self.correct)}\n 1.) {self.choices[0]}\n 2.) {self.choices[1]}\n 3.) {self.choices[2]}\n 4.) {self.choices[3]}\n')
        print("Closing start quiz")
        return

    def get_author(self):
        return self.author
                 
    def get_question(self) -> list:
        print("Getting Questions")
        choice = [0 for i in range(4)]
        randomNum1 = random.randint(0, const.DICT.__len__() - 1)
        randomNum2 = random.randint(0, const.DICT.__len__() - 1)
        randomNum3 = random.randint(0, const.DICT.__len__() - 1)
        randomNum4 = random.randint(0, const.DICT.__len__() - 1)
        while randomNum1 in self.answers:
            randomNum1 = random.randint(0, const.DICT.__len__() - 1)
        while randomNum2 == randomNum1:
            randomNum2 = random.randint(0, const.DICT.__len__() - 1)
        while randomNum3 == randomNum1 or randomNum3 == randomNum2:
            randomNum3 = random.randint(0, const.DICT.__len__() - 1)
        while randomNum4 == randomNum1 or randomNum4 == randomNum2 or randomNum4 == randomNum3:
            randomNum4 = random.randint(0, const.DICT.__len__() - 1)
        count = 0
        for key in const.DICT.keys():
            if count == randomNum1:
                choice[0] = key
            elif count == randomNum2:
                choice[1] = key
            elif count == randomNum3:
                choice[2] = key
            elif count == randomNum4:
                choice[3] = key
            count += 1
        self.answers += [randomNum1]
        self.correct = choice[0]
        return choice
