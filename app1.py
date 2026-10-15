# Primeiro exercicio
import streamlit as st

# Configuração da página para um visual mais limpo e elegante
st.set_page_config(
    page_title="Calculadora Simples",
    page_icon="🧮",
    layout="centered"
)

def main():
    # 1. Título principal com ícone amigável
    st.title("🧮 Calculadora Interativa Vibe Coding")
    st.write("Bem-vindo! Use os campos abaixo para realizar operações matemáticas de forma rápida e elegante.")

    # Criando colunas para organizar melhor a interface
    col1, col2 = st.columns(2)

    # 2. Dois campos de entrada numérica (st.number_input) com valores padrão 0.0
    with col1:
        num1 = st.number_input("Digite o primeiro número:", value=0.0, format="%.2f")
    
    with col2:
        num2 = st.number_input("Digite o segundo número:", value=0.0, format="%.2f")

    # 3. Componente de seleção para escolher a operação
    operacao = st.selectbox(
        "Escolha a operação desejada:",
        ("Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)")
    )

    st.markdown("---")

    # 4. Botão de ação com o texto "Calcular"
    if st.button("Calcular", use_container_width=True):
        resultado = None
        erro = False

        # Lógica das operações
        if operacao == "Soma (+)":
            resultado = num1 + num2
        elif operacao == "Subtração (-)":
            resultado = num1 - num2
        elif operacao == "Multiplicação (*)":
            resultado = num1 * num2
        elif operacao == "Divisão (/)":
            # 5. Tratamento de divisão por zero
            if num2 == 0.0:
                erro = True
            else:
                resultado = num1 / num2

        # 5. Exibição dos resultados ou mensagens de erro
        if erro:
            st.error("🚨 Opa! Não é possível realizar uma divisão por zero. Tente outro valor para o segundo número.")
        else:
            st.success("Cálculo realizado com sucesso!")
            st.metric(label="Resultado da Operação", value=f"{resultado:.2f}")

if __name__ == "__main__":
    main()
