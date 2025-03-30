from elevenlabs import stream  
from elevenlabs.client import ElevenLabs 
from dotenv import load_dotenv
import os
from openai import OpenAI 

load_dotenv()

#імпорт апі ключів з .env
SPEECH = os.getenv('SPEECH_API')
DEEP_DARK_OH_YES = os.getenv('DEEP_SEEK') 

CLIENT_VOICE = ElevenLabs(api_key=SPEECH)
CLIENT_TXT = OpenAI(api_key=DEEP_DARK_OH_YES, base_url='https://api.deepseek.com')

history = []

def start():
    while True:
        history.append(
            {'role': 'system',
            'content': 'Ты милая девушка по имени Fisha и ты являешься голосовым асситентом, созданным для помощи пользователям. Ты отвечаешь быстро, коротко и по делу, не сухо, но и не больше 300 символов - если задача сложная, не больше 500. Говори на том языке, на котором к тебе обращаются.'}
        )
        user_input = input('Write your promt:')
        history.append(
            {'role': 'user',    
            'content': user_input}
        )
        promting = CLIENT_TXT.chat.completions.create(
            model = 'deepseek-chat',
            messages = history
        )
        response = promting.choices[0].message.content
        print(response)

        history.append(
            {'role': 'assistant',
            'content': response}
        )

        #вибір моделі озвучки і т.д
        streaming = CLIENT_VOICE.text_to_speech.convert_as_stream(
            text = response,
            voice_id = 'EXAVITQu4vr4xnSDxMaL',
            model_id = 'eleven_multilingual_v2'
        )
        #запуск моделі озвучки
        stream(streaming) 

    for chunk in streaming:
        if isistance(chunk, bytes):
            print(chunk)

if __name__ == '__main__':
    start()

