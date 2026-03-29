# **AULA 03: DEBUG, IF, FOR, While, Listas e Dicionários em Python**

Vamos explorar estruturas de controle de fluxo como if, for e while.

Usamos estrutura de Controle de Fluxo para tomar decisões!

## **Estruturas de Controle de Fluxo**

Exploraremos como utilizar `if` para tomar decisões baseadas em condições, `for` para iterar sobre sequências de dados e `while` para executar blocos de código enquanto uma condição for verdadeira.

### **IF**

O `if` é uma estrutura condicional fundamental em Python que avalia se uma condição é verdadeira (`True`) e, se for, executa um bloco de código. Se a condição inicial não for verdadeira, você pode usar `elif` (`else if`) para verificar condições adicionais, e `else` para executar um bloco de código quando nenhuma das condições anteriores for verdadeira.

Provavelmente o mais conhecido comando de controle de fluxo é o if. Por exemplo:

```
x = int(input("Por favor, entre com um número inteiro: "))

if x < 0:
    x = 0
    print('Negativo trocado para zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Único')
else:
    print('Mais')
```

#### **Exercício 1: Verificação de Qualidade de Dados**

Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para `quantidade` e `preço`. Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

#### **Exercício 2: Classificação de Dados de Sensor**

Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

Temperatura < 18°C é 'Baixa'
Temperatura >= 18°C e <= 26°C é 'Normal'
Temperatura > 26°C é 'Alta'

#### **Exercício 3: Filtragem de Logs por Severidade**

Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. Dado um registro de log em formato de dicionário como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

#### **Exercício 4: Validação de Dados de Entrada**

Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

#### **Exercício 5: Detecção de Anomalias em Dados de Transações**

Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

### **FOR**

O loop `for` é utilizado para iterar sobre os itens de qualquer sequência, como listas, strings, ou objetos de dicionário, e executar um bloco de código para cada item. É especialmente útil quando você precisa executar uma operação para cada elemento de uma coleção.

O comando for em Python é um pouco diferente do que costuma ser em C ou Pascal. Ao invés de sempre iterar sobre uma progressão aritmética de números (como no Pascal), ou permitir ao usuário definir o passo de iteração e a condição de parada (como C), o comando for do Python itera sobre os itens de qualquer sequência (seja uma lista ou uma string), na ordem que aparecem na sequência. Por exemplo:

```
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Measure some strings:
nome = ['Luciano']
for letra in nome:
    print(letra)
```
Se você precisa iterar sobre sequências numéricas, a função embutida range() é a resposta. Ela gera progressões aritméticas:
```
for i in range(5):
    print(i)
```
O ponto de parada fornecido nunca é incluído na lista; range(10) gera uma lista com 10 valores, exatamente os índices válidos para uma sequência de comprimento 10. É possível iniciar o intervalo com outro número, ou alterar a razão da progressão (inclusive com passo negativo):
```
list(range(5, 10))
[5, 6, 7, 8, 9]

list(range(0, 10, 3))
[0, 3, 6, 9]

list(range(-10, -100, -30))
[-10, -40, -70]
```
Para iterar sobre os índices de uma sequência, combine range() e len() da seguinte forma:
```
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
```

#### **Exercício 6: Contagem de Palavras em Textos**

**Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

#### **Exercício 7: Normalização de Dados**

**Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

#### **Exercício 8: Filtragem de Dados Faltantes**

**Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.

#### **Exercício 9: Extração de Subconjuntos de Dados**

**Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

#### **Exercício 10: Agregação de Dados por Categoria**

**Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

### **WHILE**

O loop `while` é uma estrutura de controle de fluxo fundamental em Python, permitindo executar um bloco de código repetidamente enquanto uma condição especificada é avaliada como verdadeira (True). Na engenharia de dados, o uso do `while` pode ser extremamente útil para diversas tarefas, como monitoramento contínuo de fontes de dados, execução de processos de ETL (Extract, Transform, Load) até que não haja mais dados para processar, ou mesmo para implementar tentativas de reconexão automáticas a serviços ou bancos de dados quando a primeira tentativa falha.

#### **Exemplo de Uso do `while` em Engenharia de Dados**

Um cenário comum em engenharia de dados é a necessidade de executar uma tarefa de maneira periódica, como verificar novos dados em um diretório, fazer polling de uma API para novas respostas ou monitorar mudanças em um banco de dados. Nestes casos, um loop `while` pode ser utilizado para manter o script rodando continuamente ou até que uma condição específica seja atingida (por exemplo, um sinal para desligar ou uma condição de erro).

#### **Exemplo Prático: `while` True com Pausa**

Um exemplo direto do uso de `while` True em Python é criar um loop infinito que executa uma ação a cada intervalo definido, como imprimir uma mensagem a cada 10 segundos. Isso pode ser útil para monitorar processos ou dados em tempo real com uma verificação periódica.
```
import time

while True:
    print("Verificando novos dados...")
    # Aqui você pode adicionar o código para verificar novos dados,
    # por exemplo, checar a existência de novos arquivos em um diretório,
    # fazer uma consulta a um banco de dados ou API, etc.
    
    time.sleep(10)  # Pausa o loop por 10 segundos
```
Neste exemplo, o `while` True cria um loop infinito, que é uma maneira poderosa de manter um script rodando continuamente. O print simula a ação de verificar novos dados, e o `time.sleep(10)` pausa a execução do loop por 10 segundos antes da próxima iteração. Essa abordagem é simples, mas eficaz para muitos cenários de monitoramento e polling em engenharia de dados, permitindo que o script execute uma verificação ou tarefa de maneira periódica.

Contudo, é importante usar loops infinitos com cautela para evitar criar condições em que o script possa consumir recursos desnecessários ou tornar-se difícil de encerrar de forma controlada. Em ambientes de produção, outras abordagens como agendamento de tarefas (por exemplo, usando cron jobs em sistemas Unix) ou o uso de sistemas de enfileiramento de mensagens e triggers de banco de dados podem ser mais adequados para algumas dessas tarefas.

#### **Exercícios 11: Leitura de Dados até Flag**

**Objetivo:** Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

#### **Exercícios 12: Validação de Entrada**

**Objetivo:** Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

#### **Exercícios 13: Consumo de API Simulado**

**Objetivo:** Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

#### **Exercícios 14: Tentativas de Conexão**

**Objetivo:** Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

#### **Exercícios 15: Processamento de Dados com Condição de Parada**

**Objetivo:** Processar itens de uma lista até encontrar um valor específico que indica a parada.

## **Desafio**

Integre na solução da aula anterior um fluxo de `While` que repita o fluxo até que o usuário insira as informações corretas.