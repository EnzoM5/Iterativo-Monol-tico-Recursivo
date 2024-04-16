#include <stdio.h>

int main() {
    int num, i = 2;
    
    printf("Digite um número inteiro positivo: ");
    scanf("%d", &num);
    
    if (num <= 1) {
        printf("%d não é um número primo.\n", num);
        goto end;
    }
    
    while (i <= num/2) {
        if (num % i == 0) {
            printf("%d não é um número primo.\n", num);
            goto end;
        }
        i++;
    }
    
    printf("%d é um número primo.\n", num);
    
    end:
        return 0;
}