# Calculadora de consumo de energia

print("= Calculadora de Consumo Elétrico Inteligente =")

# Entrada de dados
nome_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input(f"Digite a potência da(o) {nome_aparelho} em watts (W): "))
horas_dia = float(input(f"Digite o tempo médio de uso diário em horas: "))

# Cálculo do consumo mensal em Kwh
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo do custo estimado
valor_kwh = 0.75
custo_estimado = consumo_mensal * valor_kwh

# Saída
print("\n=== Resultado ===")
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}")