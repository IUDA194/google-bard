import requests
import config
import translators as ts
import googletrans
from googletrans import Translator

def trans():
    translator = Translator()
    result = translator.translate('Привет', dest="en")
    print(result.text)


def translate(text, lang):
    result = ts.translate_text(text, translator="bing" ,to_language=lang)
    #print(result)
    return result


def main():
    prompt = input(":")
    if prompt != "q":
        ts_prompt = translate(prompt, 'en')
        headers = { 'Authorization': f'Bearer {config.BARD_TOKEN}', 'Content-Type': 'text/plain' }
        data = { "input": f"{ts_prompt}" }
        req = requests.post('https://api.bardapi.dev/chat', headers=headers, json=data)
        result = req.json() # ['Output: \n']
        print("|", result, "|")
        #ts_result = translate(text = result['output'], lang= "uk")
        print('Output: \n', result['output'])


trans()