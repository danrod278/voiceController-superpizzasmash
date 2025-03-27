import http.client
import json



def enviarParaIA(content):
    # Criando a conexão HTTPS
    conn = http.client.HTTPSConnection("chatgpt-42.p.rapidapi.com")

    # Criando o payload corretamente como um dicionário e convertendo para JSON
    payload = json.dumps({
        "messages": [
            {"role": "user", "content": """{}
                                        f'quero que quando eu enviar a mensagem voce retorne apenas um json (ou uma lista em json) com instruções do que deve ser feito. Quando a mensagem conter um pedido de adicionar um produto ao carrinho, então retorne no json add:”Oque_foi_pedido”. quando pedir para retirar tal item do carrinho, então retorne remove:”Nome_produto” - lembre se que o usuário pode fazer mais de um pedido por vez.
                                        """.format(content)}
        ],
        "model": "gpt-4o-mini"
    })

    # Definindo os headers corretamente
    headers = {
        'x-rapidapi-key': "c497809e7fmsh2c41bd3a9d5afe2p142abdjsn932596df0d3c",  # Substitua por sua chave válida
        'x-rapidapi-host': "chatgpt-42.p.rapidapi.com",
        'Content-Type': "application/json"
    }

    # Enviando a requisição
    conn.request("POST", "/chat", body=payload, headers=headers)

    # Obtendo a resposta
    res = conn.getresponse()
    data = res.read()

    # Exibindo a resposta decodificada
    return json.loads(data.decode("utf-8"))

comando = "quero um suco de maracuja e uma coca dois litros. tira pizza de queijo da lista"
retornoIA = enviarParaIA(comando)

if "choices" in retornoIA:
    print(retornoIA["choices"][0]["message"]["content"])
