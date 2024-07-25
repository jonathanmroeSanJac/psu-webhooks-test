import requests
import json

##params = {
##    "payload": {
##        "input": {
##            "text": "¿Qué servicios de salud mental están disponibles en PSU?"
##        },
##        "context": {
##            "skills": {
##                "main skill": {
##                    "user_defined": {}
##                }
##            }
##        }
##    }
##}

def main(params):
    print(json.dumps(params))
    if params['payload']['input']['text'] != '':
        url = 'https://api.neuralseek.com/v1/crn%3Av1%3Abluemix%3Apublic%3Aneuralseek%3Aus-south%3Aa%2F594368b649164c1eb07b9ac5f7f446df%3Afc9a1c18-2fe7-4bc1-946e-be225c49a5b9%3A%3A/translate'
        headers = {
            'accept': 'application/json',
            'apikey': '44f38f83-d934de69-f2376412-c645d90c',
            'Content-Type': 'application/json'
            }
        input_text = params['payload']['input']['text']
        data = {
        "text": input_text,
        "target": "en"
        }
        
        response = requests.post(url, headers=headers, json=data)
        response_json = response.json()

        # Set the language property of the incoming message to the language that was identified by Watson Language Translator.
        #params['payload']['context']['skills']['main skill']['user_defined']['language'] = response_json['translations']
        params['payload']['input']['text'] = response_json['translations']
        print('The response_json:')
        print(response_json)
        print('The params')
        print(json.dumps(params))
        return params
    else:
        params['payload']['context']['skills']['main skill']['user_defined']['language'] = 'none'
        return params

# Example usage


result = main(params)
print(json.dumps(result, indent=2))
