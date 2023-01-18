import json
import time
import telepot
from botocore.vendored import requests

TELE_TOKEN='REDACTED-o'
URL = "https://api.telegram.org/bot{}/".format(TELE_TOKEN)

menubuttons = [
    ['btn1' , 'btn2' ,'btn3'],
    ['btn4' , 'btn5' ,'btn6']
]

AUX='0'

def send_message(text, chat_id, first_name):
    final_text = text
    #AUX=int(AUX)
    if final_text=='/start':
        final_text='¡Bienvenido a la instancia BETA de UABlunt!\nPor el momento, puedes enviarnos tus sugerencias y comentarios de forma anónima a través del propio bot y los leeremos encantados. Muchas gracias por ayudarnos a mejorar UABlunt.\nhttps://i.gyazo.com/995517c8391cd9e851ab0f14831dc560.png'
        url = URL + "sendMessage?text={}&chat_id={}".format(final_text, chat_id)
        requests.get(url)
    else:
        if len(final_text) > 500:
            final_text='[ERROR] ¡El mensaje supera los 500 caracteres! Por favor, acorta el mensaje. \n\nLongitud: '+str(len(text))+'\n\nTraceback: '+text
        else: 
           if len(final_text) < 15:
               final_text='[ADVERTENCIA] ¡El mensaje es muy corto! Por favor, no envíes mensajes sin contenido, tus comentarios nos ayudan a mejorar. 💚\n\nTu mensaje se ha enviado satisfactoriamente a los desarrolladores.\n\nTraceback: '+text
        
           else:    
               final_text='Tu mensaje se ha enviado satisfactoriamente a los desarrolladores.\n\nTraceback: '+text
           if chat_id!=156316529:
              send_admin(text, chat_id)
        url = URL + "sendMessage?text={}&chat_id={}".format(final_text, chat_id)
        requests.get(url)
    
    
def send_admin(text, chat_id):
    final_text = "[ADMIN] El usuario con chat_id "+str(chat_id) + " ha enviado un comentario diciendo:\n" + text
    url = URL + "sendMessage?text={}&chat_id={}".format(final_text,156316529)
    requests.get(url)

def lambda_handler(event, context):
    message = json.loads(event['body'])
    chat_id = message['message']['chat']['id']
    reply = message['message']['text']
    first_name = message['message']['chat']['first_name'] #He descubierto que sí tengo acceso al nombre de usuario xdd (21/06)
    
    send_message(reply, chat_id, first_name)

    return{
        'statusCode': 200
    }

#ID CHAT ADMINISTRADOR: 156316529