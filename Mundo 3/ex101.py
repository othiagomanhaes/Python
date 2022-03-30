from datetime import date
def voto(ano):
    idade = date.today().year - ano
    if 65 > idade >= 18:
        return 'Voto Obrigatório!'
    elif idade < 18:
        return 'Não tem idade para voto!'
    elif idade >= 65:
        return 'Voto Opcional!'


print(voto(int(input('Digite o ano de nascimento: '))))

