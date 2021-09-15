import requests

response = requests.post("https://tntag4ploit.SANDBOX.verygoodproxy.com/post",
                          json={'card_number': 'tok_sandbox_8dSRC6Ta73ECQvUsekxkqS'}
                         )
print(str(response.text))
