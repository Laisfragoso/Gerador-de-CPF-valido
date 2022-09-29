from random import randint

nums = ''.join(list(map(lambda n: str(n), [randint(1,10) for x in range(9)])))
comp1 = [x for x in range(10,1,-1)]
comp2 = [x for x in range(11,1,-1)]

def calc(cpf):
    sum = 0

    try:
        for n in range(len(cpf)):
            if len(cpf) < 10:
                sum += int(cpf[n]) * comp1[n]
            else:
                sum += int(cpf[n]) * comp2[n]
    except:
        global nums
        nums = ''.join(list(map(lambda n: str(n), [randint(1,10) for x in range(9)])))
        calc(nums)

    sum = sum * 10 % 11

    return str(sum) if sum < 10 else '0'

final_digits = calc(nums)
final_digits += calc(nums+final_digits)
print(nums + final_digits)


"""from random import randint
digits = ''

for n in range(9):
    digits += str(randint(1,10))

n1 = [10,9,8,7,6,5,4,3,2]
n2 = [11,10,9,8,7,6,5,4,3,2]
soma = 0

for n in range(len(n1)):
    soma += n1[n] * int(digits[n])
soma *=10
resto = soma %11

if resto < 2:
    resto = 0
    
digits += str(resto) 
soma = 0
for n in range(len(n2)):
    soma += n2[n] * int(digits[n])
soma *=10
resto = soma %11

if resto < 2:
    resto = 0
    
    
digits +=  str (resto) 
print (digits)  




#treinar converter os tipos 
#conversao de inteiro pra str = var str(var)"""
 
    
    
    
    
