TAXA_CAMBIO = 5.65
with open("Projeto_2_Conversao_Monetaria/vendas_dolar.txt", "r") as arquivo:
    linhas = arquivo.readlines()
  
valores = []
for I in linhas:

    try:

        valor_dolar = float(I.strip())

        valor_real = valor_dolar * TAXA_CAMBIO

        valores.append(f"{valor_real:.2f}\n")

    except ValueError:
        
        continue

with open("vendas_real.txt", "w") as vendas_real:

    vendas_real.writelines(valores)


print("✅ Conversão concluída com sucesso! Arquivo 'vendas_real.txt' criado.")
