def notas(*num, sit=False):
    """
    Essa função cria um dicionário sobre a quantidade de notas, a maior nota, a menor nota e a média
    de um aluno. A situação boa(>=7), razoável(>=6) e ruim(<6) varia de acordo com a média do aluno.

    :param num: quantidade de notas do aluno.
    :param sit: é opcional, serve para mostrar a situação do aluno.
    :return: não tem retorno.
    """
    aluno = {}
    aluno['total'] = len(num)
    aluno['maior'] = max(num)
    aluno['menor'] = min(num)
    aluno['media'] = sum(num) / len(num)
    if sit:
        if aluno['media'] >= 7:
            aluno['situação'] = 'BOA!'
        elif 7 > aluno['media'] >= 6:
            aluno['situação'] = 'RAZOÁVEL!'
        else:
            aluno['situação'] = 'RUIM!'
    return aluno


resp = notas(6, 8.6, 10, sit=True)
print(resp)
