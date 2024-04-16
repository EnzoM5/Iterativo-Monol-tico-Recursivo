def verificar_primo_iterativo(num):
    if num < 2:
        return 'Não é primo'
    for i in range(2, num):
        if num % i == 0:
            return 'Não é primo'
    return 'É primo'


num = int(input('Digite um valor: '))
print(verificar_primo_iterativo(num))