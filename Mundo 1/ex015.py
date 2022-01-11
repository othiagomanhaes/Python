kmc = float(input('Quantos Km você percorreu com o carro? '))
dc = int(input('Quantos dias você ficou com o carro? '))
vkmc = kmc * 0.15
vdc = dc * 60
print('Você ficou {} dias com o carro e andou {}Km com ele.'.format(dc, kmc))
print('Sendo assim, você pagará R${} pelo aluguel do veículo.'.format(vdc + vkmc))
