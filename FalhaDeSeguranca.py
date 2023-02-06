# OBI2021 - Nível 3 - Nível Sênior
#
# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f3/falha/
#
# Solução e código escrito por Henrique Lima

from itertools import permutations   

# KMP Algoritmo usado e disponível em https://gist.github.com/m00nlight/daa6786cc503fde12a77
# 
# KMP - Knuth Morris Pratt é um algoritmo clássico para matching de strings

class KMP:
    def partial(self, pattern):
        
        ret = [0]
        
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
        
    def search(self, T, P):
     
        partial, ret, j = self.partial(P), [], 0
        
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = partial[j - 1]
            
        return ret


if __name__ == "__main__":

    # Declaração de variáveis
    numUser = 0
    answer = 0

    # Leitura do arquivo .txt
    print("Digite o nome to arquivo test de entrada: ")
    filename = input()
    file = open("./"+filename, "r")

    # Popular as variáveis com as respectivas linhas
    numUser = int(file.readline())
    passwords = [None for i in range(numUser)]
    for i in range(numUser):
        passwords[i] = file.readline().strip()

    # Invocar biblioteca de permutações
    perm = permutations(passwords, 2)
    
    # Invocar função Knuth Morris Pratt (String Matching)
    kmp = KMP()
    for i in list(perm): 
        if(len(kmp.search(list(i).pop(0), list(i).pop(1))) >= 1):
            answer += 1

    # Mostrar resultado final
    print("\nResposta: " + str(answer))
