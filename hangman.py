import random
from hangmanPics import HANGMAN_PICS
from palavras import words


def getRandomWord(wordList):
    # retorna uma sequência aleatória da lista palavras.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    # substitui os espaços em branco pelas letras acertadas
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    # mostra as letras da palavra secreta com espaço entre elas
    for letter in blanks:
        print(letter, end=' ')
    print()

# retorna a letra que o jogador colocou.
# a função checa se é uma letra e não outra coisa


def getGuess(alredyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Por favor coloque uma letra de cada vez')
        elif guess in alredyGuessed:
            print('Você já escolheu esta letra. Escolha outra letra')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Po favor escolha uma letra')
        else:
            return guess

# a função retorna como verdadeiro caso o jogador queira jogar mais um vez
# e falso caso queira parar de jogar


def playAgain():
    print('Gostaria de jogar navamnete? (sim ou nao)')
    return input().lower().startswith('s')


print('H A N G M A N')

missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    # deixe o jogador escolher uma letra
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # checa se o jogador ganhou
        foundAllLetter = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetter = False
                break
        if foundAllLetter:
            print('Eba! A palavra secreta é ' + secretWord + '!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # verifica se o jogador já adivinhou muitas vezes e perdeu
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Você ficou sem chances!\nDepois de ' +
                  str(len(missedLetters)) + ' chances perdidas' +
                  str(len(correctLetters)) + ' e tentativas corretas a palavra secreta é: ' + secretWord )
            gameIsDone = True

        # pergunta pro jogador se gostaria de jogar novamente.
        # somente se o jogo já terminou

        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = True
                secretWord = getRandomWord(words)
            else:
                break