import http.client
import json



def enviarParaIA(content):
    # Criando a conexão HTTPS
    conn = http.client.HTTPSConnection("chatgpt-42.p.rapidapi.com")

    # Criando o payload corretamente como um dicionário e convertendo para JSON
    payload = json.dumps({
        "messages": [
            {"role": "user", "content": """{}
                                        
Utilize a seguinte estrutura para o JSON (não utilize chaves em nenhum momento):
(retorne tudo em json)
"add": []
"remove": []
"action": []
invalid: []

Regras de Interpretação:

Adicionar um Produto ao Pedido

Se o usuário fizer mais de um pedido com a mesma ação então adicione todas juntas
exemplo: "Ouvir preço de produto":["Combo Mario & Luigi"]

Se o usuário mencionar que quer um produto específico, adicione-o na lista add.

Exemplo:

Entrada: "Quero um suco de maracujá"

Saída: add: ["suco de maracujá"]

Remover um Produto do Pedido

Se o usuário mencionar que quer remover um produto, adicione-o na lista remove.

Exemplo:

Entrada: "Tira a pizza de queijo da lista"

Saída: remove: ["pizza de queijo"]

Definir Forma de Consumo
a. Levar para viagem

Se o usuário indicar que quer levar o pedido para viagem, adicione "Levar para viagem" na lista action.

Exemplo:

Entrada: "Quero levar para viagem"

Saída: action: ["Levar para viagem"]
b. Comer no local

Se o usuário indicar que quer consumir no local, adicione "Comer aqui" na lista action.

Exemplo:

Entrada: "Vou comer aqui"

Saída: action: ["Comer aqui"]

Exibir Itens do Cardápio

 Se o usuário pedir para ver combos, adicione "Ver combos" na lista action.

 Se o usuário pedir para ver bebidas, adicione "Ver bebidas" na lista action.

 Se o usuário pedir para ver sobremesas, adicione "Ver sobremesas" na lista action.

Se o usuário pedir para ver pizzas, adicione "Ver pizzas" na lista action.

Exemplo:

Entrada: "Quais são as pizzas?"

Saída: action: ["Ver pizzas"]

Consultar Preços
a. Ouvir preço de um produto

Se o usuário pedir para ouvir o preço de um produto, adicione "Ouvir preço de produto":["nome_produto"] na lista action.
b. Ver preço de um produto

Se o usuário pedir para ver o preço de um produto, adicione "Ver preço" na lista action.
c. Ouvir preço

Se o usuário pedir para ouvir o preço (de um produto já mencionado anteriormente), adicione "Ouvir preço" na lista action.

Exemplo:

Entrada: "Me fala o preço da pizza de calabresa"

Saída: action: ["Ouvir preço de produto":["nome_produto"]]

Gerenciar Pedidos

Ver pedidos: Se o usuário pedir para ver os pedidos, adicione "Ver pedidos" na lista action.

Ouvir pedidos: Se o usuário pedir para ouvir os pedidos, adicione "Ouvir pedidos" na lista action.

Remover pedido inteiro: Se o usuário quiser cancelar o pedido, adicione "Remover pedido" na lista action.

Exemplo:

Entrada: "Cancela meu pedido"

Saída: action: ["Cancelar"]

Finalizar Pedido

Pagar: Se o usuário quiser pagar, adicione "Pagar" na lista action.

Exemplo:

Entrada: "Quero pagar agora"

Saída: action: ["Pagar"]

Chamar Atendimento Humano

Chamar atendente humano: Se o usuário quiser falar com alguém, adicione "Chamar atendente humano" na lista action.

Exemplo:

Entrada: "Preciso falar com alguém"

Saída: action: ["Chamar atendente humano"]

Comando Não Claro

Se o usuário não especificar claramente um produto ou ação, adicione uma mensagem amigável na lista invalid explicando o problema.

Exemplo:

Entrada: "Quero remover um item."

Saída: invalid: ["Qual item você quer remover?"]
Entrada: "Quero uma coca de 2L" (não temos coca de 2l)
saida: invalid:["Não temos esse produto"]

Cardápio Disponível:

Pizzas:

Hyrule Supreme

Super Star 4 Queijos

Fire Flower Calabresa

PokéPizza (Frango com Catupiry)

Fatality BBQ (Costela ao Barbecue)

Acompanhamentos:

Red Shell Fries

Rupee Nuggets

Yoshi Rings

Bebidas:

Mana Potion (Refrigerante lata)

Health Potion (Suco natural 500ml)

Elixir Supreme (Milkshake 500ml)

Sobremesas:

Choco-Kart

Donut do Kirby

Ice Beam Sundae

Combos:

Combo Mario & Luigi

Combo Sonic Dash

Combo Mestre Pokémon

Combo Final Boss

Combo Zelda & Link

Observação: Se o produto solicitado não constar no cardápio, retorne uma mensagem de erro utilizando a estrutura, por exemplo:
invalid: ["Produto não encontrado no cardápio"]


                                        """.format(content)}
        ],
        "model": "gpt-4o-mini"
    })



    # Definindo os headers corretamente
    headers = {
    'x-rapidapi-key': "c497809e7fmsh2c41bd3a9d5afe2p142abdjsn932596df0d3c",
    'x-rapidapi-host': "chatgpt-42.p.rapidapi.com",
    'Content-Type': "application/json"
    }

    conn.request("POST", "/gpt4o", payload, headers)

    # Obtendo a resposta
    res = conn.getresponse()
    data = res.read()

    # Exibindo a resposta decodificada
    return json.loads(data.decode("utf-8"))

comando = "quero um suco de maracuja e uma coca dois litros, quanto custa ?. tira pizza de queijo da lista. qual era o preço do suco mesmo? pode repetir o que eu pedi? quanto custa a coca? quanto custa o combo sonic dash?"
retornoIA = enviarParaIA(comando)

if "choices" in retornoIA:
    print(retornoIA)
