import json
import requests
from bs4 import BeautifulSoup
from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import SystemMessage, HumanMessage


def main():    
    AUTH_KEY = ""
    
    ARTICLE_URL = "https://cyberleninka.ru/article/n/ugolovnyy-kodeks-finlyandii-1889-g-kak-zakonodatelnyy-istochnik-evropeyskoy-integratsii/viewer"
    
    try:
    
        response = requests.get(ARTICLE_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = (soup.find('div', class_='article__body') or soup).get_text(' ', strip=True)
    
        # Рубрикация текста
        giga = GigaChat(credentials=AUTH_KEY, verify_ssl_certs=False)
    
        #prompt = 'Ответ нужен в JSON с ключами!!!' + open("sf.txt", 'r', encoding='utf-8').read()
        prompt =  open("sf.txt", 'r', encoding='utf-8').read()
    
        messages = [SystemMessage(content=prompt), HumanMessage(content=text)]
        result = giga.invoke(messages).content
    
        # Вывод результата
        #print(json.dumps(json.loads(result), ensure_ascii=False, indent=2))
        print(result)
    
    except Exception as e:
    
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    main()
