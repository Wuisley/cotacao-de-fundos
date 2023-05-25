import pandas as pd

df = pd.read_csv('inf_diario_fi_202305.csv', sep = ';')

lista = pd.read_excel('CNPJ Fundos IPSEMC.xlsx')

df2 = []

for i in lista['CNPJ']:
    n = df[df['CNPJ_FUNDO'] == i]
    df2.append(n)

df_concat = pd.concat(df2)  

df_concat['VL_TOTAL'] = df_concat['VL_TOTAL'].astype(str).str.replace('.', ',')
df_concat['VL_QUOTA'] = df_concat['VL_QUOTA'].astype(str).str.replace('.', ',')
df_concat['VL_PATRIM_LIQ'] = df_concat['VL_PATRIM_LIQ'].astype(str).str.replace('.', ',')
df_concat['CAPTC_DIA'] = df_concat['CAPTC_DIA'].astype(str).str.replace('.', ',')
df_concat['RESG_DIA'] = df_concat['RESG_DIA'].astype(str).str.replace('.', ',')

df_concat.to_csv('arquivo.csv', sep = ';', index=False)