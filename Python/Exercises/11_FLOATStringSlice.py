string = "X-DSPAM-Confidence: 0.8475 "
zero = string.find("0")  # Vai encontrar a posição 0
end_sp = string.find(" ", zero)  # Divide a partir do 0 para a frente
flt_extract = float(string[zero: end_sp])  # Converte o número string em float começando no 0 até ao fim
print(flt_extract)

print('---')
string = "X-DSPAM-Confidence: 0.8475 "
div = string.split()
print(div)
num = float(div[1])
print(num)
print(type(num))