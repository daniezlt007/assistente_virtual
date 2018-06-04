# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

convI = ['oi','olá','olá, bom dia', 'bom dia','bom dia, como vai?',
        'estou bem']

convF = ['que filmes que você gosta?', 'eu gosto de filmes de terror']

convS = ['O que você é?','Sou um robô','Quem é você?']


bot.set_trainer(ListTrainer)

bot.train(convI)
bot.train(convF)
bot.train(convS)

while True:
    quest = input('Você: ')
    response = bot.get_response(quest)
    print('Bot:' , response)

        
