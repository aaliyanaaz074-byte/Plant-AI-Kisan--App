import streamlit as st
from PIL import Image

st.set_page_config(page_title="Plant AI - Kisan Super App", layout="centered")

st.title("🌿 Plant AI - Kisan Super App")

tab1, tab2, tab3 = st.tabs(["🦠 Disease Detection", "💬 Kisan Chatbot", "🌱 Fertiliser Calculator"])

with tab1:
    st.subheader("Disease Detection")
    st.write("Patte ki photo upload karo aur bimari ka pata lagao")
    
    option = st.radio("Kaise photo doge?", ["📁 Photo Upload", "📷 Live Camera"], horizontal=True)
    
    image = None
    if option == "📁 Photo Upload":
        uploaded_file = st.file_uploader("Upload", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
        if uploaded_file:
            image = Image.open(uploaded_file)
    else:
        camera_file = st.camera_input("Live photo lo")
        if camera_file:
            image = Image.open(camera_file)

    if image:
        st.image(image, caption="Tumhari Photo", use_container_width=True)
        st.success("### Result: Healthy Leaf (98% Confidence)")
        st.info("**Suggestion:** Paudha swasth hai. Regular pani dete raho.")
        st.warning("**Note:** Ye demo result hai. Model ko train karne ke baad asli result ayega.")
    else:
        st.write("Kripya ek photo upload karein.")

with tab2:
    st.subheader("Kisan Chatbot")
    st.write("Kheti se juda koi bhi sawal pucho!")
    query = st.text_input("Apna sawal likho")
    if st.button("Pucho"):
        if query:
            st.write(f"**Tumhara sawal:** {query}")
            st.write("**Jawab:** Iske liye aap apni fasal ko sahi samay par pani de aur khaad ka upyog karein. (Yahan AI Chatbot jodega)")

with tab3:
    st.subheader("Fertiliser Calculator")
    crop = st.selectbox("Fasal chuno", ["Gehu", "Dhaan", "Makki", "Aloo"])
    area = st.number_input("Zameen kitni hai (acre me)", min_value=1.0)
    if st.button("Calculate Karo"):
        st.success(f"{area} acre {crop} ke liye lagbhag {area*25} kg Urea ki zarurat hai.")
