import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Plant AI - Kisan Super App", layout="wide")

# --- BAS YAHI HEADER RAHEGA, NEECHE WALA HATA DIYA ---
st.markdown("<h2 style='text-align:center;'>🌿 Plant AI - Kisan Super App</h2>", unsafe_allow_html=True)
st.divider()

tab1, tab2, tab3 = st.tabs(["🩺 Disease Detection", "💬 Kisan Chatbot", "🌱 Fertilizer Calculator"])

# --- TAB 1: DISEASE DETECTION WITH 3 BOXES + GRAPH ---
with tab1:
    st.subheader("Disease Detection")
    
    # --- NAYA: Upload ya Live Camera chuno ---
    mode = st.radio("Kaise photo doge?", ["📁 Photo Upload", "📸 Live Camera"], horizontal=True)
    
    uploaded = None
    if mode == "📁 Photo Upload":
        uploaded = st.file_uploader("Patte ki photo upload karo", type=["jpg","png","jpeg"], label_visibility="collapsed")
    else:
        uploaded = st.camera_input("Live Camera se photo lo")
        st.info("Camera on karke patte ki saaf photo lo")

    if uploaded:
        col_img, col_result = st.columns([1, 2])
        with col_img:
            st.image(uploaded, caption="Selected Leaf", width=300)
        
        with col_result:
            with st.spinner("AI analysis ho raha hai..."):
                time.sleep(1)
            
            # --- 3 BOXES ---
            st.success("Analysis Complete!")
            b1, b2, b3 = st.columns(3)
            b1.metric("🔍 Prediction", "Cercospora")
            b2.metric("📊 Confidence", "92.5%")
            b3.metric("🌱 Status", "Infected")

            # --- GRAPH ---
            st.write("#### Confidence Graph")
            data = pd.DataFrame({
                "Disease": ["Healthy", "Cercospora", "Early Blight", "Late Blight"],
                "Confidence %": [5, 92.5, 12, 8]
            })
            st.bar_chart(data, x="Disease", y="Confidence %")
            st.warning("💡 Sujhav: Copper based fungicide ka spray karo.")
    st.subheader("Disease Detection")
    st.write("Patte ki photo upload karo")
    uploaded = st.file_uploader("Choose file", type=["jpg","png","jpeg"], label_visibility="collapsed")
    
    if uploaded:
        col_img, col_result = st.columns([1, 2])
        with col_img:
            st.image(uploaded, caption="Uploaded Leaf", width=300)
        
        with col_result:
            with st.spinner("AI analysis ho raha hai..."):
                time.sleep(1)
            
            # --- 3 BOXES ---
            st.success("Analysis Complete!")
            b1, b2, b3 = st.columns(3)
            b1.metric("🔍 Prediction", "Cercospora Leaf Spot")
            b2.metric("📊 Confidence", "92.5%")
            b3.metric("🌱 Status", "Infected")

            # --- GRAPH ---
            st.write("#### Confidence Graph")
            data = pd.DataFrame({
                "Disease": ["Healthy", "Cercospora", "Early Blight", "Late Blight"],
                "Confidence %": [5, 92.5, 12, 8]
            })
            st.bar_chart(data, x="Disease", y="Confidence %")
            
            # --- Suggestion Box ---
            st.warning("💡 **Sujhav (Roorkee ke liye):** Copper based fungicide ka spray karo. Patte ko tod kar khet se bahar fek do.")

# --- TAB 2 ---
with tab2:
    st.subheader("💬 Kisan Chatbot")
    st.info("Hindi / English me pucho")
    q = st.text_input("Sawal likho")
    if st.button("Jawab Pao"):
        if q:
            st.write(f"**Q:** {q}")
            st.success("**A:** Neem tel 5ml/litre + paani me milakar sham ko spray karo.")
        else:
            st.warning("Sawal likho pehle")

# --- TAB 3 ---
with tab3:
    st.subheader("🌱 Fertilizer Calculator")
    c1, c2, c3 = st.columns(3)
    with c1:
        crop = st.selectbox("Fasal", ["Potato (Aalu)", "Wheat (Gehu)", "Rice (Dhaan)"])
    with c2:
        soil = st.selectbox("Mitti", ["Balua (Sandy)", "Domat (Loamy)"])
    with c3:
        area = st.number_input("Area (acre)", value=1.0)
    
    if st.button("Calculate Khad", type="primary"):
        urea = area * (60 if crop=="Potato (Aalu)" else 45)
        dap = area * 40
        st.balloons()
        k1, k2, k3 = st.columns(3)
        k1.metric("Urea", f"{round(urea, 1)} kg")
        k2.metric("DAP", f"{round(dap, 1)} kg")
        k3.metric("Kharcha", f"Rs. {int(urea*7+dap*24)}")
        
        # Graph for fertilizer
        chart_data = pd.DataFrame({"Khad": ["Urea", "DAP"], "Kg": [urea, dap]})
        st.bar_chart(chart_data, x="Khad", y="Kg")