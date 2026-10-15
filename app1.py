
import streamlit as st

# Configuração da página (deve ser o primeiro comando Streamlit)
st.set_page_config(
    page_title="Calculadora Interativa",
    page_icon="🧮",
    layout="centered",
)

# Título principal com ícone amigável
st.title("🧮 Calculadora Interativa")
st.write(
    "Bem-vindo(a)! Use a barra lateral para escolher a operação e insira os números abaixo."
)

# 1. Menu lateral para escolher a operação matemática
st.sidebar.header("Configurações")
st.sidebar.write("Escolha a operação desejada:")

operacao = st.sidebar.radio(
    "Operação", ["Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)"]
)

st.sidebar.markdown("---")
st.sidebar.info("Dica: No modo de divisão, evite dividir por zero!")

# 2. Campos de entrada numérica na tela principal
st.subheader("Entrada de Dados")
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Digite o primeiro número", value=0.0, format="%.2f")

with col2:
    num2 = st.number_input("Digite o segundo número", value=0.0, format="%.2f")

st.markdown("---")

# 4. Botão de ação "Calcular"
if st.button("Calcular", type="primary", use_container_width=True):
    # Lógica de cálculo baseada na seleção do menu lateral
    resultado = None
    erro = None

    if operacao == "Soma (+)":
        resultado = num1 + num2
    elif operacao == "Subtração (-)":
        resultado = num1 - num2
    elif operacao == "Multiplicação (*)":
        resultado = num1 * num2
    elif operacao == "Divisão (/)":
        # 5. Tratamento para divisão por zero
        if num2 == 0.0:
            erro = (
                "⚠️ Erro matemático: Não é possível realizar divisão por zero!"
            )
        else:
            resultado = num1 / num2

    # Exibição dos resultados ou erros
    if erro:
        st.error(erro)
    else:
        st.success("Cálculo realizado com sucesso!")
        st.metric(label="Resultado da Operação", value=f"{resultado:.2f}")
