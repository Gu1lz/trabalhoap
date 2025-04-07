### integrantes: Guilherme Leite, Arthur Mestnik

def classi(velocidade, permitida, multa): ## 4 e 2 e 3
    if multa == "S":
        if velocidade <= permitida:
            return "Nenhuma infração"
        elif velocidade >= (permitida + (permitida*0.20)): 
            print("Infração leve - Multa de  R$ 130,16  e nenhum ponto na CNH")
            return 
        elif (permitida + (permitida*0.20)) > velocidade <= (permitida + (permitida*0.50)): ### 2 Infração grave
            print("Infração grave - Multa de  R$ 195,23 e 5 pontos na CNH")
            valor = dobrar(2)
            return valor
        else: ### 3 Infração gravíssima
            print("Infração gravíssima - Multa de R$ 880,41, 7 pontos na CNH e suspensão da carteira.")
            valor = dobrar(3)
            print("Atenção: CNH suspensa! Compareça ao Detran.")
            print("Atenção: Você precisa fazer um curso de reciclagem no Detran.")
            return valor

    elif multa == "N":
        if velocidade <= permitida:
            return "Nenhuma infração"
        elif velocidade >= (permitida + (permitida*0.20)): 
            print("Infração leve - Multa de  R$ 130,16  e nenhum ponto na CNH")
            return 130.16
        elif (permitida + (permitida*0.20)) > velocidade <= (permitida + (permitida*0.50)): 
            print("Infração grave - Multa de  R$ 195,23 e 5 pontos na CNH")
            return 195.23
        else: 
            print("Infração gravíssima - Multa de R$ 880,41, 7 pontos na CNH e suspensão da carteira.")
            print("Atenção: CNH suspensa! Compareça ao Detran.")
            print("Atenção: Você precisa fazer um curso de reciclagem no Detran.")
            return 880.41
    else:
        return "Algo deu errado"
    
def dobrar(tipo):            ## 4 e 5
    print("Atenção: Multa DOBRADA por reincidência!")
    if tipo == 2:
        return 195.23 * 2
    elif tipo == 3: 
        return 880.41 * 2
    else:
        return

def pagamentos(valorf, agora): ## 6
    if agora == "S":
        valorf = valorf - (valorf * 0.20)
        print(f"Pagamento realizado! Você recebeu um desconto de 20%. Valor final: {valorf}")
    else:
        print(f"Pagamento realizado! Você recebeu um desconto de 20%. Valor final: {valorf}")

if __name__ == '__main__':
    placa = input("Qual a placa do veículo: ")[:8]
    nome = input("Qual o seu nome: ")
    velocidade = int(input("Velocidade registrada por km/h: ")[:3])
    permitida = int(input("Velocidade máxima permitida por km/h: ")[:3])
    multa = input("Motorista já foi multado(Sim/Não): ")[:1].upper()
    pagar = input("Deseja pagar a multa agora(Sim/Não): ")[:1].upper()

    print(f"Placa do veículo: {placa}")
    print(f"Nome do Motorista: {nome}")
    print(f"Nome do Motorista: {velocidade} km/h")
    print(f"Velocidade máxima permitida: {permitida} km/h")
    valor = classi(velocidade, permitida, multa)
    pagamentos(valor, pagar)
