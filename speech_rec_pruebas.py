import requests
import base64

def recognizer(audio = None):
    #audio = open('./audio.wav', 'rb').read()
    #encodedStr = str(base64.b64encode(audio), "utf-8")
    encodedStr = str(base64.b64encode(audio.read()), "utf-8")
    data = { 'config': {
        'languageCode': 'es-MX',
        'audioChannelCount': 2
    }, 'audio':{
        'content': encodedStr
    }}
    r = requests.post(url='https://speech.googleapis.com/v1/speech:recognize?key=AIzaSyDmedgCSS299rtO9X9aYA9JkBLHhhc0gr4', json=data)
    json = r.json()
    resul = json['results'][0]['alternatives'][0]['transcript'] if json['results'][0]['alternatives'][0]['confidence'] > .70 else 'Not Confidence'
    return resul