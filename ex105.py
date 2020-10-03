def notas( * num, sit=False):
    maior = max(num)
    total = len(num)
    menor = min(num)
    media = sum(num) / len(num)
    dicionario = {"total": total, "Maior": maior, "Menor": menor, "Média": media}
    if sit == True:
        if media >= 7:
            dicionario[situação]
    return dicionario





resp = notas(8, 10, sit=True)
print(resp)