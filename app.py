import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def tempo_resposta(x):
    return 1000 / (50 - x)

st.title("Simulador de Saturação de API")
st.write("Este app mostra como o tempo de resposta de uma API cresce conforme a carga se aproxima da capacidade máxima de 50 requisições por segundo.")

carga = st.slider("Carga (requisições por segundo)", 0, 49, 25)

tempo = tempo_resposta(carga)
st.write(f"**Tempo de resposta estimado:** {tempo:.1f} ms")

if tempo > 200:
    st.error("Tempo de resposta muito alto! O sistema está perto da saturação.")
elif carga >= 40:
    st.warning("Atenção: a carga está na região crítica (acima de 40 req/s).")
else:
    st.success("Sistema operando normalmente.")

x_valores = np.linspace(0, 49.9, 200)
y_valores = tempo_resposta(x_valores)

fig, ax = plt.subplots()
ax.plot(x_valores, y_valores, label="Modelo T(x)")
ax.axvline(x=50, color="red", linestyle="--", label="Capacidade máxima (50 req/s)")
ax.scatter([carga], [tempo], color="orange", s=100, zorder=5, label="Carga escolhida")
ax.set_xlabel("Carga (req/s)")
ax.set_ylabel("Tempo de resposta (ms)")
ax.set_ylim(0, 1100)
ax.legend()

st.pyplot(fig)
