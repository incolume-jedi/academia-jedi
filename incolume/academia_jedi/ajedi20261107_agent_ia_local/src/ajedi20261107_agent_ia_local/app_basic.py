"""
Assistente RAG de Políticas Internas (RH)
- Streamlit (interface)
- LangChain com LCEL (orquestração)
- FAISS (banco vetorial)
- OpenAI (embeddings + LLM)
"""

import streamlit as st


# ============================================================
# INTERFACE
# ============================================================

st.title("Assistente RAG — Políticas Internas")

# carregar chain e vector store

# inicia a lista de mensagens
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# exibe as mensagens na tela
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Pergunte sobre as políticas da empresa...")
if prompt :
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Buscando..."):
            answer = f"Resposta da IA para a pergunta: {prompt}"
            st.write(answer)

    st.session_state["messages"].append({"role": "assistant", "content": answer})