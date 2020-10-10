a = 0;
t = 0;
g = 0;
ci = 0;
cont =0;
acu = '';
acumA = "";
acumT = "";
acumG = "";
acumCI = "";
compA = "";
compT = "";
compG = "";
compCI = "";
charAnt = "";
contMaxA = 1;
contMaxT = 1;
contMaxG = 1;
contMaxCI = 1;
archivo = open ('ttn.fasta', 'r');
for linea in archivo.readlines():
    linea1 = linea.rstrip('\n');
    acu += linea1;
archivo.close();

for char in acu:
    cont += 1;
    if char == 'A':
        a+=1;
        if charAnt == 'A':
            if acumA == "":
                acumA = acumA + char + char;
            else:
                acumA += char
        else:
            acumA = "";
        if acumA > compA:
            compA = acumA;
        if acumA == compA:
            contMaxA += 1;
        else:
            contMaxA = 1;
    if char == 'T':
        t +=1;
        if charAnt == 'T':
            if acumT == "":
                acumT = acumT + char + char;
            else:
                acumT += char
        else:
            acumT = "";
        if acumT > compT:
            compT = acumT;
        if acumT == compT:
            contMaxT += 1;
        else:
            contMaxT = 1;
    if char == 'G':
        g +=1;
        if charAnt == 'G':
            if acumG == "":
                acumG = acumG + char + char;
            else:
                acumG += char
        else:
            acumG = "";
        if acumG > compG:
            compG = acumG;
        if acumG == compG:
            contMaxG += 1;
        else:
            contMaxG = 1;
    if char == 'C':
        ci +=1;
        if charAnt == 'C':
            if acumCI == "":
                acumCI = acumCI + char + char;
            else:
                acumCI += char
        else:
            acumCI = "";
        if acumCI > compCI:
            compCI = acumCI;
        if acumCI == compCI:
            contMaxCI += 1;
        else:
            contMaxCI = 1;
    charAnt = char;

print('El porcentaje de Adenina dentro del nucleótido es ' + str(round((a/cont)*100,2)) + "%");
print('Su cadena mas larga tiene ' + str(len(compA)) + ' adeninas consecutivas y se repite ' + str(contMaxA)+ ' veces');
print('\n');
print('El porcentaje de Timina dentro del nucleótido es ' + str(round((t/cont)*100,2)) + "%");
print('Su cadena mas larga tiene ' + str(len(compT)) + ' timinas consecutivas y se repite ' + str(contMaxT)+ ' veces');
print('\n');
print('El porcentaje de Guanina dentro del nucleótido es ' + str(round((g/cont)*100,2)) + "%");
print('Su cadena mas larga tiene ' + str(len(compG)) + ' adeninas consecutivas y se repite ' + str(contMaxG)+ ' veces');
print('\n');
print('El porcentaje de Citocina dentro del nucleótido es ' + str(round((ci/cont)*100,2)) + "%");
print('Su cadena mas larga tiene ' + str(len(compCI)) + ' adeninas consecutivas y se repite ' + str(contMaxCI)+ ' veces');