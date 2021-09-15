import os
import requests

os.environ['HTTPS_PROXY'] = 'http://USuvzyoEH3SMKo9waZZSMDeM:fb0f4b9c-7013-4ed6-a2ee-a59b753f2001@tntag4ploit.SANDBOX.verygoodproxy.com:8080'
response = requests.post('https://echo.apps.verygood.systems/post',
                         json={'card_number': 'ALIAS'},
                         verify='app/templates/cert.pem')
print(str(response.text))