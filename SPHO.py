import streamlit as st

# Configurações iniciais do app
st.title("SPHO_2025_1")
st.write("Simulador de Previsão de Honorários Odontológicos")
st.write("Gestão e Planejamento em Odontologia - FOUSP.")
st.write("Michel-Crosato E, Azevedo CL, Biazevic MGH, Martini Filho IE.")
st.write("Material didático para ser utilizado em disciplinas de graduação em odontologia.")
st.write("Preencha os campos abaixo para calcular os honorários previstos de um estabelecimento odontológico:")
st.write("manual e aplicativo disponível em: https://www.gtivsd.com/ferramentas")

# Configurações adicionais na barra lateral
st.sidebar.header("Configurações adicionais")
imposto_custom = st.sidebar.slider("Imposto (%)", min_value=0, max_value=30, value=10) / 100
lucro_custom = st.sidebar.slider("Lucro (%)", min_value=0, max_value=50, value=15) / 100

# Entradas de dados
pro_labore_inicial = st.number_input("Pró-labore inicial (R$)", value=0.0, step=100.0)
custo_fixo = st.number_input("Custo fixo (R$)", value=0.0, step=100.0)
horas_semanais = st.number_input("Horas trabalhadas por semana", value=0, step=1)
tempo_servico_horas = st.number_input("Tempo para executar o serviço (em horas)", value=0.0, step=0.1)
custo_variado = st.number_input("Custo variado (R$)", value=0.0, step=1.0)

# Botão para cálculo
if st.button("Calcular"):
    # Cálculos
    if horas_semanais > 0:  # Evitar divisão por zero
        pro_labore_adequado = pro_labore_inicial * 1.11  # Exemplo de ajuste automático de pró-labore
        horas_mensais = horas_semanais * 4
        horas_mensais_corrigidas = horas_mensais * 0.85  # Correção de 15%
        hora_clinica = (pro_labore_adequado + custo_fixo) / horas_mensais_corrigidas
        preco = (hora_clinica * tempo_servico_horas) + custo_variado
        imposto = preco * imposto_custom
        lucro = preco * lucro_custom
        preco_final = preco + imposto + lucro
        # Exibição dos resultados
        st.subheader("Resultados")
        st.write(f"Horas mensais corrigidas: {horas_mensais_corrigidas:.2f} horas")
        st.write(f"Custo por hora clínica: R$ {hora_clinica:.2f}")
        st.write(f"Preço: R$ {preco:.2f}")
        st.write(f"Imposto estimado ({imposto_custom * 100:.0f}%): R$ {imposto:.2f}")
        st.write(f"Lucro estimado ({lucro_custom * 100:.0f}%): R$ {lucro:.2f}")
        st.write(f"Preço final: R$ {preco_final:.2f}")
    else:
        st.error("Por favor, insira um valor maior que zero para as horas trabalhadas por semana.")
        