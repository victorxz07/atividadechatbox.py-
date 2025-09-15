import streamlit as st

st.set_page_config(page_title="Atendimento Jurídico Online", page_icon="⚖️")
st.title("Atendimento Jurídico Online")
 
faq = {
    "Quais são as áreas de atuação?": "Nosso escritório é especializado em Direito de Família (divórcios, pensão alimentícia), Direito Trabalhista (direitos do empregado, rescisão de contrato) e Direito Civil (contratos, indenizações).",
    "Como posso agendar uma consulta?": "Você pode agendar uma consulta pelo WhatsApp, telefone ou preenchendo o formulário em nosso site. Um de nossos assistentes entrará em contato para confirmar.",
    "Quais documentos devo levar para a consulta?": "Isso depende do seu caso. Para uma consulta inicial, é sempre bom ter em mãos documentos de identificação e qualquer documento relacionado ao problema, como contratos, e-mails ou notificações.",
    "Quanto custa uma consulta?": "A primeira consulta para avaliação do caso pode ter um custo simbólico ou ser gratuita, dependendo da política do escritório. Os honorários completos são definidos após a análise do seu problema.",
    "Qual o endereço do escritório?": "Estamos localizados na Avenida Liberdade, nº 789, sala 101. Atendemos com agendamento prévio.",
    "Falar com um advogado": "Você pode falar diretamente com um de nossos advogados pelo WhatsApp clicando no botão abaixo.",
}



if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

pergunta = st.chat_input("Digite sua pergunta ou escolha uma das sugestões abaixo:")

col1, col2 = st.columns(2)
with col1:
    for key in list(faq.keys())[:3]:
        if st.button(key):
            pergunta = key
with col2:
    for key in list(faq.keys())[3:]:
        if st.button(key):
            pergunta = key


if pergunta:

    resposta = faq.get(pergunta, "Desculpe, não tenho uma resposta para isso no momento. Por favor, tente reformular sua pergunta ou use os botões.")

    st.session_state.messages.append({"role": "user", "content": pergunta})
    st.session_state.messages.append({"role": "assistant", "content": resposta})

    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):
        st.markdown(resposta)

    if pergunta == "Falar com um advogado":
        whatsapp_url = "https://wa.me/559912345678" 
        st.markdown(f"**[Clique aqui para falar no WhatsApp]({whatsapp_url})**")