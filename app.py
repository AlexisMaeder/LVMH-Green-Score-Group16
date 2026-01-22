import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import datetime 

st.set_page_config(page_title="LVMH Green AI", page_icon="🌿", layout="wide")

st.markdown("""
    <style>. 
    .stApp { background-color: #0E1117; }
    h1, h2, h3, h4, h5, h6, p, li, .stMarkdown { color: #FAFAFA !important; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    h1 { font-weight: 300; letter-spacing: 2px; text-transform: uppercase; }
    
    /* Metrics Cards */
    div[data-testid="metric-container"] {
        background-color: #262730; border: 1px solid #41444C; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    div[data-testid="metric-container"] label { color: #B0B0B0 !important; }
    div[data-testid="metric-container"] div[data-testid="stMetricValue"] { color: #FFFFFF !important; }
    
    /* Sidebar & Inputs */
    section[data-testid="stSidebar"] { background-color: #161920; }
    .stTextInput, .stNumberInput, .stSelectbox, .stSlider { color: white; }
    
    /* CLEAN INTERFACE */
    [data-testid="stHeaderActionElements"] { display: none !important; }
    [data-testid="stElementToolbar"] { display: none !important; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.title("LVMH • AI GREEN SCORE")
st.markdown("<p style='text-align: center; color: #B0B0B0; margin-bottom: 40px;'>GO / NO-GO Decision Support Tool for AI Projects</p>", unsafe_allow_html=True)

st.sidebar.header("🎛️ Project Settings")
st.sidebar.markdown("---")

project_name = st.sidebar.text_input("Project Name", "Veolia Secure GPT Assistant")
model_type = st.sidebar.selectbox("Model Type", ["GPT-Standard (Inference)", "Fine-Tuned Model", "Training from Scratch"])

st.sidebar.subheader("1. Text Usage")
num_users = st.sidebar.slider("👤 Number of Users", 10, 5000, 500)
requests_per_day = st.sidebar.slider("💬 Requests / day / user", 1, 50, 10)
avg_tokens = st.sidebar.number_input("📝 Avg. Tokens / request", value=500, step=100)

st.sidebar.subheader("2. Multimodal Usage (High Impact)")
use_media = st.sidebar.checkbox("📸 Include Image & Video Gen?", value=False)
img_per_day = 0
vid_sec_per_day = 0
if use_media:
    st.sidebar.warning("⚠️ High Energy Impact Detected")
    img_per_day = st.sidebar.number_input("Images / day / user", 0, 50, 2)
    vid_sec_per_day = st.sidebar.number_input("Video seconds / day / user", 0, 60, 5)

st.sidebar.markdown("---")
project_duration = st.sidebar.slider("📅 Project Duration (months)", 1, 36, 12)

st.sidebar.subheader("3. Infrastructure")
region = st.sidebar.selectbox("🌍 Server Location", ["France (Low Carbon)", "USA (Mixed Mix)", "Global (Average)"])
carbon_factor = 1.0
if region == "France (Low Carbon)":
    carbon_factor = 0.1
elif region == "USA (Mixed Mix)":
    carbon_factor = 1.5

st.sidebar.markdown("---")
with st.sidebar.expander("ℹ️ Methodology & Scales"):
    st.markdown("""
    **Formula:**
    Total = Training + Inference (Text + Media)
    
    **Score Thresholds (Annual CO2):**
    - 🟢 **A (GO):** < 1 ton
    - 🟢 **B (GO):** < 10 tons
    - 🟠 **C (WARN):** < 50 tons
    - 🔴 **D (NO-GO):** < 100 tons
    - 🔴 **E (NO-GO):** > 100 tons
    """)

CO2_PER_TOKEN = 0.0031
WATER_PER_TOKEN = 0.12
CO2_PER_IMAGE = 4.0 
CO2_PER_VIDEO_SEC = 15.0
WATER_PER_MEDIA_UNIT = 5.0

total_days = 30 * project_duration
total_tokens = num_users * requests_per_day * total_days * avg_tokens
total_images = num_users * img_per_day * total_days
total_video_sec = num_users * vid_sec_per_day * total_days

text_co2 = (total_tokens * CO2_PER_TOKEN) / 1000
media_co2 = ((total_images * CO2_PER_IMAGE) + (total_video_sec * CO2_PER_VIDEO_SEC)) / 1000
text_water = (total_tokens * WATER_PER_TOKEN) / 1000
media_water = ((total_images + total_video_sec) * WATER_PER_MEDIA_UNIT) / 1000

training_co2 = 19200000 if model_type == "Training from Scratch" else (5000 if model_type == "Fine-Tuned Model" else 0)

total_co2 = (text_co2 + media_co2) * carbon_factor + training_co2
total_water = text_water + media_water
km_voiture = total_co2 / 0.12

if total_co2 < 1000:
    score, color, msg = "A", "#2E7D32", "GO • SUSTAINABLE PROJECT"     
elif total_co2 < 10000:
    score, color, msg = "B", "#66BB6A", "GO • MANAGED IMPACT"          
elif total_co2 < 50000:
    score, color, msg = "C", "#FFA726", "WARNING • OPTIMIZATION NEEDED" 
elif total_co2 < 100000:
    score, color, msg = "D", "#EF5350", "NO-GO • HIGH RISK"            
else:
    score, color, msg = "E", "#C62828", "NO-GO • CRITICAL"             

col1, col2, col3 = st.columns(3)
col1.metric("☁️ Carbon Footprint", f"{total_co2:,.0f} kg", "Total Project")
col2.metric("💧 Water Consumption", f"{total_water:,.0f} L", "Cooling")
col3.metric("🚗 Car Equivalent", f"{km_voiture:,.0f} km", "Thermal Engine")

st.markdown("---")

col_left, col_right = st.columns([1.5, 2.5])

with col_left:
    st.subheader("Decision & Score")
    st.markdown(f"""
        <div style="
            background-color: #262730; 
            border: 1px solid #444;
            border-left: 10px solid {color}; 
            border-radius: 10px; 
            padding: 30px; 
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
            text-align: center;">
            <h1 style="color: {color} !important; font-size: 80px; margin: 0; padding: 0;">{score}</h1>
            <h3 style="margin: 10px 0 0 0; color: #FFFFFF !important; text-transform: uppercase;">{msg}</h3>
            <p style="color: #B0B0B0 !important; margin-top: 10px; font-size: 14px;">Based on selected energy mix</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("###") 
    report_text = f"""
    LVMH AI GREEN SCORE - CERTIFICATE
    --------------------------------------------------
    Project Name: {project_name}
    Date: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}
    --------------------------------------------------
    
    DECISION: {msg} (Score {score})
    
    KEY METRICS:
    - Total Carbon Footprint: {total_co2:,.0f} kg CO2eq
    - Water Consumption: {total_water:,.0f} L
    - Car Equivalent: {km_voiture:,.0f} km
    
    CONFIGURATION:
    - Users: {num_users}
    - Location: {region}
    - Multimodal: {"Yes" if use_media else "No"}
    
    --------------------------------------------------
    Generated by LVMH Green AI Tool
    """
    st.download_button(
        label="📥 Download Official Certificate",
        data=report_text,
        file_name=f"LVMH_GreenScore_{project_name.replace(' ', '_')}.txt",
        mime="text/plain"
    )

with col_right:
    st.subheader("Impact Breakdown")
    data_dict = {
        "Source": ["Text (LLM)", "Training (Model)", "Multimodal (Img/Vid)"],
        "Impact (kg CO2)": [text_co2 * carbon_factor, training_co2, media_co2 * carbon_factor]
    }
    df_chart = pd.DataFrame(data_dict)
    
    base = alt.Chart(df_chart).encode(
        x=alt.X('Impact (kg CO2)', title='CO2 Footprint (kg)'),
        y=alt.Y('Source', sort='-x', title=None)
    )
    
    bars = base.mark_bar(color=color).encode(
        tooltip=['Source', 'Impact (kg CO2)']
    )
    
    final_chart = (bars).configure_axis(
        labelColor='white', titleColor='white', gridColor='#444444'
    ).configure_view(strokeWidth=0).properties(height=320)
    
    st.altair_chart(final_chart, use_container_width=True)
    
    if use_media:
        st.caption("⚠️ Note: Multimodal usage (Image/Video) drastically increases footprint.")

st.markdown("<br><br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555; font-size: 12px;'>Alberthon 2025 • Prototype developed for LVMH</p>", unsafe_allow_html=True)