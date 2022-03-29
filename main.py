import random

words = ["code", "bit", "list", "soul", "next"]
codes = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

answers = []


def morse_encode(sentence):
    encoded = ""
    for i in sentence:
        encoded += codes[i] + " "
    return encoded


def get_word():
    return random.choice(words)


def print_statistics(answers):
    total = len(answers)
    correct = sum(answers)
    incorrect = len(answers) - sum(answers)
    print(f"Всего задачек: {total}")
    print(f"Отвечено верно: {correct}")
    print(f"Отвечено неверно: {incorrect}")


def main():
    print("Сегодня мы потренируемся расшифровывать азбуку Морзе")
    print("Нажмите Enter и начнем")
    input()

    for i in range(len(words)):
        word = get_word()
        current_encoded = morse_encode(word)
        print(f"Слово {i + 1} {current_encoded}")
        user_input = input()
        if user_input.lower() == word:
            print(f"Верно, {word}!")
            answers.append(True)
        else:
            print(f"Неверно, {word}!")
            answers.append(False)
    print_statistics(answers)


main()
