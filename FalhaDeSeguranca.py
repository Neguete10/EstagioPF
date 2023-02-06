# OBI2021 - Nivel 3 - Nível Sênior
#
# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f3/falha/
#
# Solucao e codigo escrito por Henrique Lima

from itertools import permutations   

# KMP Algoritmo usado e disponivel em https://gist.github.com/m00nlight/daa6786cc503fde12a77
# 
# KMP - Knuth Morris Pratt e um algoritmo classico para matching de strings

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

    # Declaracao de variaveis
    numUser = 0
    answer = 0

    # Leitura do arquivo .txt
    print("Digite o nome to arquivo test de entrada: ")
    filename = input()
    file = open("./"+filename, "r")

    # Popular as variaveis com as respectivas linhas
    numUser = int(file.readline())
    passwords = [None for i in range(numUser)]
    for i in range(numUser):
        passwords[i] = file.readline().strip()

    # Invocar biblioteca de permutacoes
    perm = permutations(passwords, 2)
    
    # Invocar funcao Knuth Morris Pratt (String Matching)
    kmp = KMP()
    for i in list(perm): 
        if(len(kmp.search(list(i).pop(0), list(i).pop(1))) >= 1):
            answer += 1

    # Mostrar resultado final
    print("\nResposta: " + str(answer))
