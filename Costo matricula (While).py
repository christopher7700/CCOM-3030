# Costo Anual  = 2000.00 matricula
## Aumento anual de 3% por los proximos 5 anños
### calcula y despliega el amuento de matricula por los prx 5 anos.

Rate = 0.03
Costo_Anual = 2000.00
year = 0

while year <= 5:
    Costo_Anual *= (1.0 + Rate)
    print(year,'\t',format(Costo_Anual,'8,.2f'))
    year += 1

    
print('bota bumba')
