def classi(velocidade, permitida, multa):
    if multa == "S":
        if velocidade <= permitida:
            return "Nenhuma infração"
        elif velocidade >= (permitida + (permitida*0.20)):
            return penalidades()
        elif (permitida + (permitida*0.20)) > velocidade <= (permitida + (permitida*0.50)):
            return penalidades()
        else:
            return penalidades()
   
    elif multa =="N":
        if velocidade <= permitida:
            return "Nenhuma infração"
        elif velocidade >= (permitida + (permitida*0.20)):
            return "Infração leve - multa de R$ 130,16 e nenhum ponto na CNH."
        elif (permitida + (permitida*0.20)) > velocidade <= (permitida + (permitida*0.50)):
            return "Infração grave - multa de R$ 195,23 e adição de 5 pontos na CNH."
        else:
            return "Infração gravíssima - Multa de R$ 880,41, 7 pontos na CNH e suspensão da carteira."
    else:
        return "Algo deu errado"

def penalidades(dobrar):

def pagamentos():


if __name__ == '__main__':
    ## placa = input("Qual a placa do veículo: ")[:8]
    ##  nome = input("Qual o seu nome: ")
    ##  velocidade = int(input("Velocidade registrada por km/h: ")[:3])
    ##  permitida = int(input("Velocidade máxima permitida por km/h: ")[:3])
    ##  multa = input("Motorista já foi multado(Sim/Não): ")[:1].upper()
    ##  pagar = input("Deseja pagar a multa agora(Sim/Não): ")[:1].upper()

    ## print(f"Placa do veículo: {placa}")
    ## print(f"Nome do Motorista: {nome}")
    ##  print(f"Nome do Motorista: {velocidade} km/h")
    ##  print(f"Velocidade máxima permitida: {permitida} km/h")
    classi()
    pagamentos()

### integrantes: Guilherme Leite, Arthur Mestnik


