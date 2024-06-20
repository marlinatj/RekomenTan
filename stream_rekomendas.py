from joblib import load
import streamlit as st

tanaman_model = load('rekomendasi_tanaman_model.joblib')
st.title ('Program Rekomendasi Tanaman')
col1, col2 = st.columns(2)
with col1:
    nitrogen = st.text_input ('Input Nilai Nitrogen Dalam Tanah')
with col2:
    fosfor = st.text_input ('Input Nilai Fosfor Dalam Tanah')
with col1:
    potash = st.text_input ('Input Nilai Potasium Dalam Tanah')
with col2:
    temp = st.text_input ('Input Nilai Temperatur')
with col1:
    humid = st.text_input ('Input Nilai Kelembaban')
with col2:
    ph = st.text_input ('Input Nilai Ph Tanah')
with col1:
    rain = st.text_input ('Input Curah Hujan')

rekomd = ''

if st.button('Tentukan Tanaman yang Cocok'):
    rekom = tanaman_model.predict([[nitrogen, fosfor, potash, temp, humid, ph, rain]])
    if (rekom == 'Blackgram'):
        rekom = 'Blackgram. Rekomendasi tanaman lain: Maize, Pigeon, Mungbean, Chickpea'
    elif (rekom == 'ChickPea'):
        rekom = 'Chickpea. Rekomendasi tanaman lain: Lentil, MungBean, Maize, PigeonPeas'
    elif (rekom == 'Jute'):
        rekom = 'Jute. Rekomendasi tanaman lain: Rekomendasi Pertama: Maize, Rice, PigeonPeas'
    elif (rekom == 'KidneyBeans'):
        rekom = 'Kidneybeans. Rekomendasi tanaman lain: MungBean, Maize'
    elif (rekom == 'Lentil'):
        rekom = 'Lentil. Rekomendasi tanaman lain: ChickPea, Mungbean'
    elif (rekom == 'Maize'):
        rekom = 'Maize. Rekomendasi tanaman lain: Blackgram, Jute, PigeonPeas'
    elif (rekom == 'MothBeans'):
        rekom = 'MothBeans. Rekomendasi tanaman lain: MungBean, Maize'
    elif (rekom == 'MungBean'):
        rekom = 'MungBean. Rekomendasi tanaman lain: Maize, KidneyBean, MothBeans'
    elif (rekom == 'PigeonPeas'):
        rekom = 'PigeonPeas. Rekomendasi tanaman lain: Blackgram, PigeonPeas, Maize, Jute'
    elif (rekom == 'Rice'):
        rekom = 'Rice. Rekomendasi tanaman lain: Maize, Jute'
    else:
        ('We also recommend planting carbohydrate source plants such as Rice or Maize to support food security activities :)')

    st.success(rekom)
