def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal (IMC)."""
    try:
        imc = peso / (altura ** 2)
        return round(imc, 2)
    except ZeroDivisionError:
        return "Erro: Altura não pode ser zero."
    except TypeError:
        return "Erro: Peso e altura devem ser números."

def classificar_imc(imc):
    """Classifica o IMC em categorias."""
    if not isinstance(imc, (int, float)):
        return "IMC inválido."
    elif imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    print("Calculadora de IMC")
    print("-----------------")
    
    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))
        
        imc = calcular_imc(peso, altura)
        if isinstance(imc, str):  # Verifica se houve erro
            print(imc)
        else:
            classificacao = classificar_imc(imc)
            print(f"Seu IMC é: {imc}")
            print(f"Classificação: {classificacao}")
    except ValueError:
        print("Erro: Digite apenas números válidos.")

if __name__ == "__main__":
    main()