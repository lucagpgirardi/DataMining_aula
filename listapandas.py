#Luca Gabriel Pace Girardi - 202302937357

import pandas as panda

base_alunos = panda.read_excel("https://github.com/danieltb3006/DM_Ibmec/raw/main/base_alunos.xlsx")

print(base_alunos)

#Ex 1

conceito = base_alunos[["Conceito"]]

print(conceito)

#Ex2

nota_conceito = base_alunos[["Nota", "Conceito"]]

print(nota_conceito)

#Ex3

filtro_ap2 = base_alunos[(base_alunos["AP2"]>=6)]
print(filtro_ap2)

#Ex4

conceito_b = base_alunos[(base_alunos["Conceito"] == "B")]
print(conceito_b)

#Ex5
adm_8 = base_alunos[(base_alunos["Curso"] == "ADM") & (base_alunos["Nota"] >= 8.0) & (base_alunos["Conceito"] == "B") ]
print(adm_8)