def verificar_primo_recursivo(num, i=2):
    if num < 2:
        return 'Não é primo'
    if i < num:
        if num % i == 0:
            return 'Não é primo'
        return verificar_primo_recursivo(num, i + 1)
    return 'É primo'

num = int(input('Digite um valor: '))
print(verificar_primo_recursivo(num))