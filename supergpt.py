import http.client
import json
from random import choice


def request(content):
    conn = http.client.HTTPSConnection("cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com")

    payload = json.dumps({
        "messages": [{"role": "user", "content": """ {}
        Utilize a seguinte estrutura para o JSON (não utilize chaves em nenhum momento):
    (retorne tudo em json)
    "add": []
    "remove": []
    "action": []
    "obs": []
    "invalid": []
    
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
    Se o usuário pedir para saber o preço de um produto, adicione "Ouvir preço de produto":["nome_produto"] na lista action. se o produto não estiver listado no cardápio, não execute o comando.
    
    
    Gerenciar Pedidos
    
    Ver pedidos: Se o usuário pedir para ver os pedidos, adicione "Ver pedidos" na lista action.
    
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
    
    Entrada: "Quero uma coca de 2L" 
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
    invalid: ["Produto nome_produto não encontrado no cardápio"]
    
    
        
        """.format(content)}],
        "model": "gpt-4o",
        "max_tokens": 100,
        "temperature": 0.9
    })
    headers = {
        'x-rapidapi-key': "c497809e7fmsh2c41bd3a9d5afe2p142abdjsn932596df0d3c",
        'x-rapidapi-host': "cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com",
        'Content-Type': "application/json"
    }

    conn.request("POST", "/v1/chat/completions", payload, headers)

    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

comando = input(str("Converse com o atendente: "))
retornoIA = request(comando)

if("choices" in retornoIA):
    print(retornoIA)
    print(retornoIA["choices"][0]["message"]["content"])
