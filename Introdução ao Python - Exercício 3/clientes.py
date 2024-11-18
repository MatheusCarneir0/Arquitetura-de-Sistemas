import json

from util import gerar_registro

def calcular_medias(clientes):
    total_idade = 0
    total_renda = 0
    for cliente in clientes:
        total_idade += cliente['idade']
        total_renda += cliente['salario']
    
    media_idade = total_idade / len(clientes)
    media_renda = total_renda / len(clientes)
    
    return media_idade, media_renda

def main():   # No meu caso tive que usar todo  
              # c:/Users/Matheus/Desktop/Exercício 2/AULA_2/Atividade/clientes.txt
    with open('c:/Users/Matheus/Desktop/Exercício 2/AULA_2/Atividade/clientes.txt', 'r') as file:
        clientes_data = json.load(file)
    
    media_idade, media_renda = calcular_medias(clientes_data)
    
    print(f'Média de Idade: {media_idade:.2f}')
    print(f'Média de Renda: {media_renda:.2f}')

if __name__ == '__main__':
    main()
