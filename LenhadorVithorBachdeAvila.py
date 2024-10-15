
#Boas-vindas
print("Bem-vindos a madereira do lenhador Vithor Bach de Ávila!")

#Funcao para escolher o tipo de madeira
def escolha_tipo():
    while True:
        tipo = input("Escolha o tipo de madeira (PIN/PER/MOG/IPE/IMB): ").upper()
        if tipo == "PIN":
            return 150.40 #Valor da tora de Pinho
        elif tipo == "PER":
            return 170.20 #Valor da tora de Peroba
        elif tipo == "MOG":
            return 190.90 #Valor da tora de Mongo
        elif tipo == "IPE":
            return 210.10 #Valor da tora de Ipe
        elif tipo == "IMB":
            return 220.70 #Valor da tora de Imbuia
        else:
            print("Opção inválida, tente novamente.") #Exigencia

#Funcao da quantidade de toras e calculo de desconto
def qtd_toras():
    while True:
        try:
            qtd = int(input("Digite a quantidade de toras (máx 2000 unidades): "))
            if qtd < 100:
                return qtd, 0
            elif 100 <= qtd < 500:
                return qtd, 0.04 #Desconto de 4%
            elif 500 <= qtd < 1000:
                return qtd, 0.09 #Desconto de 9%
            elif 1000 <= qtd <= 2000:
                return qtd, 0.16 #Desconto de 16%
            else:
                print("Quantidade inválida, limite de 2000 toras.") #Limite de toras 2k
        except ValueError:
            print("Entrada inválida, por favor digite um número.")

#Funcao para escolher o transporte
def transporte():
    while True:
        try:
            opcao_transporte = int(input("Escolha o tipo de transporte (1-Rodoviário, 2- Ferroviário, 3- Hidroviário):"))
            if opcao_transporte == 1:
                return 1000 #Custo rodoviario
            elif opcao_transporte == 2:
                return 2000 #Custo ferroviario
            elif opcao_transporte == 3:
                return 2500 #Custo hidroviario
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida, por favor insira 1, 2 ou 3.")

#Codigo principal
#Calculo total e uso de try/except

try:
    valor_madeira = escolha_tipo() #pegando o valor da madeira escolhida
    quantidade, desconto = qtd_toras() #quantidade de toras e desconto aplicavel
    valor_transporte = transporte() #pega o valor do transporte

    #Calculo do total
    total = ((valor_madeira * quantidade) * (1 - desconto)) + valor_transporte

    #Exibindo o resultado final
    print (f"Tipo de madeira: {valor_madeira} por m³")
    print (f"Quantidade de toras: {quantidade}")
    print (f"Desconto aplicado: {desconto * 100}%")
    print (f"Valor do transporte: {valor_transporte}")
    print (f"Total a pagar: R$ {total:.2f}")

except Exception as e:
    print(f"Ocorreu um erro no sistema: {e}")
