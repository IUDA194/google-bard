# Слюбовью проебал 3 часа и написал костыль iuda194
import requests
import config
import translators as ts
import googletrans
import time
from googletrans import Translator
import os
from colorama import init, Fore

# Кароче блять, я заебался искать переводчик больших текстов, так что встречайте вашу любимую рубрику "Костыль"

os.system("cls||clear")
BARD_TOKEN = input("Enter your BARD TOKEN without space: ") # Прошу апи токен этого додика
os.system("cls||clear")

# Функция переводчика основанная на бесплатной библиотеке
def translate(text, lang):
    result = ts.translate_text(text, translator="bing" ,to_language=lang) # Параметр translator для указание какое апи юзаем подробнее чиать док тварь
    #print(result)
    return result

# Костыль 1
def splice_text(text) -> list:
    result = []
    sentence = ""
    last_char_number = 0
    for char_n in range(len(text)):
        if text[char_n] == "." or text[char_n] == "!" or text[char_n] == "?":
            result.append(sentence + text[char_n])
            sentence = ""
        else:
            sentence += text[char_n]
    return result

# Костыль 2
def translate_big_text(text, lang):
    result = ""
    text_sentense = splice_text(text)
    for sentence in text_sentense:
        result += translate(sentence, lang)
    return {"input" : text, "output" : result, "lang" : lang}
    
# В принципе весь функционал
def main():
    prompt = input(Fore.LIGHTBLUE_EX + "User:") # Просим промпт
    if prompt != "q": # На случай если захочешь сьебатся
        try:
            ts_prompt = translate(prompt, 'en')
            headers = { 'Authorization': f'Bearer {BARD_TOKEN}', 'Content-Type': 'text/plain' }
            data = { "input": f"{ts_prompt}" }
            req = requests.post('https://api.bardapi.dev/chat', headers=headers, json=data)
            result = req.json() # Получаю ответ от апи
            print(Fore.LIGHTBLACK_EX + 'Ai:\n', translate_big_text(result['output'], "ru")['output'])
            main() # Рекурсия наше всё
        except:
            os.system("cls||clear")
            print("Проверьте токен барда")
            BARD_TOKEN = input("Enter your BARD TOKEN without space: ") # Прошу апи токен этого додика
            os.system("cls||clear")
    else: # Если тут что-то не понятно убейся от стену
        os.system("cls||clear") 
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("|||Спасибо за то что использовали консольную версию google bard от iuda194|||")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        time.sleep(1.5)
        os.system("cls||clear")

main() # Вызов функции

# Elena shilo sosi hui