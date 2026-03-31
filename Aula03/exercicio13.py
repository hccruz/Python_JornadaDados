### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é 
# processada em loop até que não haja mais páginas.
import time

pagina_atual = 1
paginas_totais = 5

while pagina_atual <= paginas_totais:
    print(f'Processando página {pagina_atual} de {paginas_totais}')
    time.sleep(5)
    pagina_atual += 1

print('Todas as páginas forma processadas')