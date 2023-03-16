import random
import os

words = [
    'banana', 'flor', 'pedra', 'lata',
    'furo', 'tesoura', 'carro', 'moto', 'porta',
    'carreta', 'brita', 'combo', 'pano', 'prego',
    'cano', 'corno', 'cortar', 'quebrar', 'pegar',
    'amassar', 'falar', 'andar', 'cair', 'queda',
    'partida', 'inicio', 'fim', 'final', 'total',
    'pequeno', 'grande', 'bobo', 'forte', 'fraco'
]

secret_word = words[random.randint(1, len(words)-1)]

mask = []

attempts = []
limit = 5
errors = 0

def jogo(keys, mask, limit, errors):
    for key in keys:
        mask.append('_')
