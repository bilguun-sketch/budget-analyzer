import pandas as pd
import streamlit as st
from io import BytesIO
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
st.set_page_config(page_title="Төсөв анализ", layout="wide", page_icon="📊")



st.markdown("""
<style>
/* Make expander content use more width */
.streamlit-expanderContent {
    padding: 1rem 2rem;
}

/* Optional: make full-width expander container */
.css-1v0mbdj .streamlit-expander {
    width: 100% !important;
}

/* Optional: control figure size inside expander */
div[data-testid="stVerticalBlock"] img {
    max-width: 100% !important;
    height: auto;
}
</style>
""", unsafe_allow_html=True)


st.title("_Хувьсах зардал тооцоолуур_")

data = []
data_tsalin = []

uploaded_file = st.file_uploader("Файл оруулах:", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    name = st.text_input("Файл нэрлэх:")

    for row in df.itertuples():
        # INPUTS
        baiguullaga = row.Байгууллага
    
        hew_shinj = row._3
            
        bairshil = row.Байршил
    
    
        tuwuus_als = row._8
            
        umch_helber = row._6
    
        surgalt_tulbur = row._9
    
        aimag = row.Аймаг
                
        if baiguullaga == "ЕБС":
            
            db_bairshil = bairshil
            
            turul_hut = row._7
            
            angi_1 = row._27
            angi_2 = row._28
            angi_3 = row._29
            angi_4 = row._30
            angi_5 = row._31
            angi_6 = row._32
            angi_7 = row._33
            angi_8 = row._34
            angi_9 = row._35
            angi_10 = row._36
            angi_11 = row._37
            angi_12 = row._38
            
            angi_1_buleg = row._15
            angi_2_buleg = row._16
            angi_3_buleg = row._17
            angi_4_buleg = row._18
            angi_5_buleg = row._19
            angi_6_buleg = row._20
            angi_7_buleg = row._21
            angi_8_buleg = row._22
            angi_9_buleg = row._23
            angi_10_buleg = row._24
            angi_11_buleg = row._25
            angi_12_buleg = row._26
        
            angi_1_db = row._53
            angi_2_db = row._54
            angi_3_db = row._55
            angi_4_db = row._56
            angi_5_db = row._57
            angi_6_db = row._58
            angi_7_db = row._59
            angi_8_db = row._60
            angi_9_db = row._61
            angi_10_db = row._62
            angi_11_db = row._63
            angi_12_db = row._64
    
            angi_1_hb = row._40
            angi_2_hb = row._41
            angi_3_hb = row._42
            angi_4_hb = row._43
            angi_5_hb = row._44
            angi_6_hb = row._45
            angi_7_hb = row._46
            angi_8_hb = row._47
            angi_9_hb = row._48
            angi_10_hb = row._49
            angi_11_hb = row._50
            angi_12_hb = row._51
    
            niit_angi_too = int(angi_1)+int(angi_2)+int(angi_3)+int(angi_4)+int(angi_5)+int(angi_6)+int(angi_7)+int(angi_8)+int(angi_9)+int(angi_10)+int(angi_11)+int(angi_12)
            niit_hb_too = int(angi_1_hb)+int(angi_2_hb)+int(angi_3_hb)+int(angi_4_hb)+int(angi_5_hb)+int(angi_6_hb)+int(angi_7_hb)+int(angi_8_hb)+int(angi_9_hb)+int(angi_10_hb)+int(angi_11_hb)+int(angi_12_hb)
            
            angi_1 = int(angi_1)
            angi_2 = int(angi_2)
            angi_3 = int(angi_3)
            angi_4 = int(angi_4)
            angi_5 = int(angi_5)
            angi_6 = int(angi_6)
            angi_7 = int(angi_7)
            angi_8 = int(angi_8)
            angi_9 = int(angi_9)
            angi_10 = int(angi_10)
            angi_11 = int(angi_11)
            angi_12 = int(angi_12)
    
            angi_1_hb = int(angi_1_hb)
            angi_2_hb = int(angi_2_hb)
            angi_3_hb = int(angi_3_hb)
            angi_4_hb = int(angi_4_hb)
            angi_5_hb = int(angi_5_hb)
            angi_6_hb = int(angi_6_hb)
            angi_7_hb = int(angi_7_hb)
            angi_8_hb = int(angi_8_hb)
            angi_9_hb = int(angi_9_hb)
            angi_10_hb = int(angi_10_hb)
            angi_11_hb = int(angi_11_hb)
            angi_12_hb = int(angi_12_hb)
    
            angi_1_db = int(angi_1_db)
            angi_2_db = int(angi_2_db)
            angi_3_db = int(angi_3_db)
            angi_4_db = int(angi_4_db)
            angi_5_db = int(angi_5_db)
            angi_6_db = int(angi_6_db)
            angi_7_db = int(angi_7_db)
            angi_8_db = int(angi_8_db)
            angi_9_db = int(angi_9_db)
            angi_10_db = int(angi_10_db)
            angi_11_db = int(angi_11_db)
            angi_12_db = int(angi_12_db)
    
            niit_db_too = angi_1_db+angi_2_db+angi_3_db+angi_4_db+angi_5_db+angi_6_db+angi_7_db+angi_8_db+angi_9_db+angi_10_db+angi_11_db+angi_12_db
    
            angi_1_buleg = int(angi_1_buleg)
            angi_2_buleg = int(angi_2_buleg)
            angi_3_buleg = int(angi_3_buleg)
            angi_4_buleg = int(angi_4_buleg)
            angi_5_buleg = int(angi_5_buleg)
            angi_6_buleg = int(angi_6_buleg)
            angi_7_buleg = int(angi_7_buleg)
            angi_8_buleg = int(angi_8_buleg)
            angi_9_buleg = int(angi_9_buleg)
            angi_10_buleg = int(angi_10_buleg)
            angi_11_buleg = int(angi_11_buleg)
            angi_12_buleg = int(angi_12_buleg)
    
            # ITGELTSUURUUD
            
            if bairshil == "Нийслэл":
                bairshil_itg = 1
                if 1 < niit_angi_too <= 50:
                    suragch_too_itg = 5
                elif 50 < niit_angi_too <= 100:
                    suragch_too_itg = 3.5
                elif 100 < niit_angi_too <= 160:
                    suragch_too_itg = 2.5
                elif 160 < niit_angi_too <= 200:
                    suragch_too_itg = 2.1
                elif 200 < niit_angi_too <= 350:
                    suragch_too_itg = 1.77
                elif 350 < niit_angi_too <= 550:
                    suragch_too_itg = 1.52
                elif 550 < niit_angi_too <= 900:
                    suragch_too_itg = 1.31
                elif 900 < niit_angi_too <= 1200:
                    suragch_too_itg = 1.15
                elif 1200 < niit_angi_too <= 1500:
                    suragch_too_itg = 1.1
                elif 1500 < niit_angi_too <= 1800:
                    suragch_too_itg = 1
                elif 1800 < niit_angi_too <= 2000:
                    suragch_too_itg = 0.91
                elif 2000 < niit_angi_too <= 2500:
                    suragch_too_itg = 0.87
                elif 2500 < niit_angi_too <= 3000:
                    suragch_too_itg = 0.84
                elif 3000 < niit_angi_too <= 3500:
                    suragch_too_itg = 0.82
                elif niit_angi_too > 3500:
                    suragch_too_itg = 0.72
        
                db_bairshil_itg = 1
    
            elif bairshil == "Аймгийн төвийн сум":
                bairshil_itg = 1.176
                if 1 < niit_angi_too <= 50:
                    suragch_too_itg = 5
                elif 50 < niit_angi_too <= 100:
                    suragch_too_itg = 3.5
                elif 100 < niit_angi_too <= 160:
                    suragch_too_itg = 2.5
                elif 160 < niit_angi_too <= 200:
                    suragch_too_itg = 2.1
                elif 200 < niit_angi_too <= 350:
                    suragch_too_itg = 1.77
                elif 350 < niit_angi_too <= 550:
                    suragch_too_itg = 1.52
                elif 550 < niit_angi_too <= 900:
                    suragch_too_itg = 1.31
                elif 900 < niit_angi_too <= 1200:
                    suragch_too_itg = 1.15
                elif 1200 < niit_angi_too <= 1500:
                    suragch_too_itg = 1.1
                elif 1500 < niit_angi_too <= 1800:
                    suragch_too_itg = 1
                elif 1800 < niit_angi_too <= 2000:
                    suragch_too_itg = 0.91
                elif 2000 < niit_angi_too <= 2500:
                    suragch_too_itg = 0.87
                elif 2500 < niit_angi_too <= 3000:
                    suragch_too_itg = 0.84
                elif 3000 < niit_angi_too <= 3500:
                    suragch_too_itg = 0.82
                elif niit_angi_too > 3500:
                    suragch_too_itg = 0.72
    
                db_bairshil_itg = 1.181
    
            elif bairshil == "Сум":
                if tuwuus_als <= 200:
                    bairshil_itg = 1.38
                elif tuwuus_als > 200:
                    bairshil_itg = 1.384
                if 1 < niit_angi_too <= 50:
                    suragch_too_itg = 5
                elif 50 < niit_angi_too <= 100:
                    suragch_too_itg = 3.5
                elif 100 < niit_angi_too <= 160:
                    suragch_too_itg = 2.5
                elif 160 < niit_angi_too <= 200:
                    suragch_too_itg = 2.1
                elif 200 < niit_angi_too <= 300:
                    suragch_too_itg = 1.77
                elif 300 < niit_angi_too <= 400:
                    suragch_too_itg = 1.59
                elif 400 < niit_angi_too <= 500:
                    suragch_too_itg = 1.55
                elif 500 < niit_angi_too <= 700:
                    suragch_too_itg = 1.31
                elif 700 < niit_angi_too <= 900:
                    suragch_too_itg = 1.27
                elif 900 < niit_angi_too <= 1200:
                    suragch_too_itg = 1.17
                elif niit_angi_too > 1200:
                    suragch_too_itg = 0.95
                db_bairshil_itg = 1.373
    
            if umch_helber == "Хувийн":
                if bairshil == "Нийслэл":
                    if 0 <= int(surgalt_tulbur) <= 1000000:
                        surgalt_tulbur_itg = 0.93
                    elif 1000000 < int(surgalt_tulbur) <= 5000000:
                        surgalt_tulbur_itg = 0.56
                    elif 5000000 < int(surgalt_tulbur) <= 10000000:
                        surgalt_tulbur_itg = 0.47
                    elif 10000000 < int(surgalt_tulbur):
                        surgalt_tulbur_itg = 0
                else:
                    if 0 <= int(surgalt_tulbur) <= 5000000:
                        surgalt_tulbur_itg = 0.93
                    elif 5000000 < int(surgalt_tulbur) <= 10000000:
                        surgalt_tulbur_itg = 0.56
                    elif 10000000 < int(surgalt_tulbur):
                        surgalt_tulbur_itg = 0
            else:
                surgalt_tulbur_itg = None
    
            if turul_hut == "Тийм":
                turul_hut_itg = 1.17
            else:
                turul_hut_itg = 1
            if angi_1_buleg != 0:
                buleg_1 = angi_1 / angi_1_buleg
                if 35 <= buleg_1 <= 44:
                    angi_1_buleg_itg = 0.0001
                    angi_1_excess = buleg_1 - 35
                elif buleg_1 > 44:
                    angi_1_buleg_itg = -0.3
                    angi_1_excess = buleg_1 - 44
                else:
                    angi_1_buleg_itg = 0
                    angi_1_excess = 0
            else:
                angi_1_buleg_itg = 0
                angi_1_excess = 0
            if angi_2_buleg != 0:
                buleg_2 = angi_2 / angi_2_buleg
                if 35 <= buleg_2 <= 44:
                    angi_2_buleg_itg = 0.0001
                    angi_2_excess = buleg_2 - 35
                elif buleg_2 > 44:
                    angi_2_buleg_itg = -0.3
                    angi_2_excess = buleg_2 - 44
                else:
                    angi_2_buleg_itg = 0
                    angi_2_excess = 0
            else:
                angi_2_buleg_itg = 0
                angi_2_excess = 0
            if angi_3_buleg != 0:
                buleg_3 = angi_3 / angi_3_buleg
                if 35 <= buleg_3 <= 44:
                    angi_3_buleg_itg = 0.0001
                    angi_3_excess = buleg_1 - 35
                elif buleg_3 > 44:
                    angi_3_buleg_itg = -0.3
                    angi_3_excess = buleg_3 - 44
                else:
                    angi_3_buleg_itg = 0
                    angi_3_excess = 0
            else:
                angi_3_buleg_itg = 0
                angi_3_excess = 0
            if angi_4_buleg != 0:
                buleg_4 = angi_4 / angi_4_buleg
                if 35 <= buleg_4 <= 44:
                    angi_4_buleg_itg = 0.0001
                    angi_4_excess = buleg_4 - 35
                elif buleg_4 > 44:
                    angi_4_buleg_itg = -0.3
                    angi_4_excess = buleg_4 - 44
                else:
                    angi_4_buleg_itg = 0
                    angi_4_excess = 0
            else:
                angi_4_buleg_itg = 0
                angi_4_excess = 0
            if angi_5_buleg != 0:
                buleg_5 = angi_5 / angi_5_buleg
                if 35 <= buleg_5 <= 44:
                    angi_5_buleg_itg = 0.0001
                    angi_5_excess = buleg_5 - 35
                elif buleg_5 > 44:
                    angi_5_buleg_itg = -0.3
                    angi_5_excess = buleg_5 - 44
                else:
                    angi_5_buleg_itg = 0
                    angi_5_excess = 0
            else:
                angi_5_buleg_itg = 0
                angi_5_excess = 0
            if angi_6_buleg != 0:
                buleg_6 = angi_6 / angi_6_buleg
                if 35 <= buleg_6 <= 44:
                    angi_6_buleg_itg = 0.0001
                    angi_6_excess = buleg_6 - 35
                elif buleg_6 > 44:
                    angi_6_buleg_itg = -0.3
                    angi_6_excess = buleg_6 - 44
                else:
                    angi_6_buleg_itg = 0
                    angi_6_excess = 0
            else:
                angi_6_buleg_itg = 0
                angi_6_excess = 0
            if angi_7_buleg != 0:
                buleg_7 = angi_7 / angi_7_buleg
                if 35 <= buleg_7 <= 44:
                    angi_7_buleg_itg = 0.0001
                    angi_7_excess = buleg_7 - 35
                elif buleg_7 > 44:
                    angi_7_buleg_itg = -0.3
                    angi_7_excess = buleg_7 - 44
                else:
                    angi_7_buleg_itg = 0
                    angi_7_excess = 0
            else:
                angi_7_buleg_itg = 0
                angi_7_excess = 0
            if angi_8_buleg != 0:
                buleg_8 = angi_8 / angi_8_buleg
                if 35 <= buleg_8 <= 44:
                    angi_8_buleg_itg = 0.0001
                    angi_8_excess = buleg_8 - 35
                elif buleg_8 > 44:
                    angi_8_buleg_itg = -0.3
                    angi_8_excess = buleg_8 - 44
                else:
                    angi_8_buleg_itg = 0
                    angi_8_excess = 0
            else:
                angi_8_buleg_itg = 0
                angi_8_excess = 0
            if angi_9_buleg != 0:
                buleg_9 = angi_9 / angi_9_buleg
                if 35 <= buleg_9 <= 44:
                    angi_9_buleg_itg = 0.0001
                    angi_9_excess = buleg_9 - 35
                elif buleg_9 > 44:
                    angi_9_buleg_itg = -0.3
                    angi_9_excess = buleg_9 - 44
                else:
                    angi_9_buleg_itg = 0
                    angi_9_excess = 0
            else:
                angi_9_buleg_itg = 0
                angi_9_excess = 0
            if angi_10_buleg != 0:
                buleg_10 = angi_10 / angi_10_buleg
                if 35 <= buleg_10 <= 44:
                    angi_10_buleg_itg = 0.0001
                    angi_10_excess = buleg_10 - 35
                elif buleg_10 > 44:
                    angi_10_buleg_itg = -0.3
                    angi_10_excess = buleg_10 - 44
                else:
                    angi_10_buleg_itg = 0
                    angi_10_excess = 0
            else:
                angi_10_buleg_itg = 0
                angi_10_excess = 0
            if angi_11_buleg != 0:
                buleg_11 = angi_11 / angi_11_buleg
                if 35 <= buleg_11 <= 44:
                    angi_11_buleg_itg = 0.0001
                    angi_11_excess = buleg_11 - 35
                elif buleg_11 > 44:
                    angi_11_buleg_itg = -0.3
                    angi_11_excess = buleg_1 - 44
                else:
                    angi_11_buleg_itg = 0
                    angi_11_excess = 0
            else:
                angi_11_buleg_itg = 0
                angi_11_excess = 0
            if angi_12_buleg != 0:
                buleg_12 = angi_12 / angi_12_buleg
                if 35 <= buleg_12 <= 44:
                    angi_12_buleg_itg = 0.0001
                    angi_12_excess = buleg_12 - 35
                elif buleg_12 > 44:
                    angi_12_buleg_itg = -0.3
                    angi_12_excess = buleg_12 - 44
                else:
                    angi_12_buleg_itg = 0
                    angi_12_excess = 0
            else:
                angi_12_buleg_itg = 0
                angi_12_excess = 0
    
            if hew_shinj == 'Энгийн':
                ybs_tusuw = ((1477.0 * (angi_1 - angi_1_hb)) + 1477.0 * angi_1_excess * angi_1_buleg_itg + 1486.0 * (angi_2 - angi_2_hb) + 1486.0 * angi_2_excess * angi_2_buleg_itg
                + (1491.0 * (angi_3 - angi_3_hb)) + 1491.0 * angi_3_excess * angi_3_buleg_itg + (1610.0 * (angi_4  - angi_4_hb)) + 1610.0 * angi_4_excess * angi_4_buleg_itg + (1656.0 * (angi_5 - angi_5_hb)) + 1656.0 * angi_5_excess * angi_5_buleg_itg 
                + (1989.0 * (angi_6 - angi_6_hb)) + 1989.0 * angi_6_excess * angi_6_buleg_itg + (2091.0 * (angi_7 - angi_7_hb)) + 2091.0 * angi_7_excess * angi_7_buleg_itg 
                + (2147.0 * (angi_8 - angi_8_hb)) + 2147.0 * angi_8_excess * angi_8_buleg_itg + (2187.0 * (angi_9 - angi_9_hb)) + 2187.0 * angi_9_excess * angi_9_buleg_itg 
                + (2116.0 * (angi_10 - angi_10_hb)) + 2116.0 * angi_10_excess * angi_10_buleg_itg + (2214.0 * (angi_11 - angi_11_hb)) + 2214.0 * angi_11_excess * angi_11_buleg_itg 
                + (2247.0 * (angi_12 - angi_12_hb)) + 2247.0 * angi_12_excess * angi_12_buleg_itg + (1477.0 * angi_1_hb * 3) + (1486.0 * angi_2_hb * 3) + (1491.0 * angi_3_hb * 3)
                + (1610.0 * angi_4_hb * 3) + (1656.0 * angi_5_hb * 3) + (1989.0 * angi_6_hb * 3)
                + (2091.0 * angi_7_hb * 3) + (2147.0 * angi_8_hb * 3) + (2187.0 * angi_9_hb * 3) + (2116.0 * angi_10_hb * 3)
                + (2214.0 * angi_11_hb * 3) + (2247.0 * angi_12_hb * 3))
                if umch_helber == "Хувийн":
                    ybs_tusuw = ybs_tusuw * surgalt_tulbur_itg * bairshil_itg * turul_hut_itg
                    if aimag == "Баян-Өлгий":
                        bayn_ulgii = 1.01
                        ybs_tusuw = ybs_tusuw * bayn_ulgii
                    else: 
                        bayn_ulgii = None
                else:
                    ybs_tusuw = ybs_tusuw * suragch_too_itg * bairshil_itg * turul_hut_itg
                    if aimag == "Баян-Өлгий":
                        bayn_ulgii = 1.01
                        ybs_tusuw = ybs_tusuw * bayn_ulgii
                    else: 
                        bayn_ulgii = None
                hew_shinj_itg = None
            else:
                ybs_tusuw = (1477.0 * angi_1 + 1477.0 * angi_1_excess * angi_1_buleg_itg + 1486.0 * angi_2 + 1486.0 * angi_2_excess * angi_2_buleg_itg
                + 1491.0 * angi_3 + 1491.0 * angi_2_excess * angi_3_buleg_itg + 1610.0 * angi_4 + 1610.0 * angi_4_excess * angi_4_buleg_itg + 1656.0 * angi_5 + 1656.0 * angi_5_excess * angi_5_buleg_itg 
                + 1989.0 * angi_6 + 1989.0 * angi_6_excess * angi_6_buleg_itg + 2091.0 * angi_7 + 2091.0 * angi_7_excess * angi_7_buleg_itg 
                + 2147.0 * angi_8 + 2147.0 * angi_8_excess * angi_8_buleg_itg + 2187.0 * angi_9 + 2187.0 * angi_9_excess * angi_9_buleg_itg 
                + 2116.0 * angi_10 + 2116.0 * angi_10_excess * angi_10_buleg_itg + 2223.0 * angi_11 + 2223.0 * angi_11_excess * angi_11_buleg_itg 
                + 2247.0 * angi_12 + 2247.0 * angi_12_excess * angi_12_buleg_itg)
                hew_shinj_itg = 1.3
                if umch_helber == "Хувийн":
                    ybs_tusuw = ybs_tusuw * 1.3 * surgalt_tulbur_itg * bairshil_itg * turul_hut_itg
                    if aimag == "Баян-Өлгий":
                        bayn_ulgii = 1.01
                        ybs_tusuw = ybs_tusuw * bayn_ulgii
                    else: 
                        bayn_ulgii = None
                else:
                    ybs_tusuw = ybs_tusuw * 1.3 * suragch_too_itg * bairshil_itg * turul_hut_itg
                    if aimag == "Баян-Өлгий":
                        bayn_ulgii = 1.01
                        ybs_tusuw = ybs_tusuw * bayn_ulgii
                    else:
                        bayn_ulgii = None
    
                # DOTUUR_BAIR_TUSUW

            if 1 <= niit_db_too <= 50:
                db_too_itg = 2.0
            elif 50 < niit_db_too <= 100:
                db_too_itg = 1.00
            elif 100 < niit_db_too <= 200:
                db_too_itg = 0.7
            elif niit_db_too > 200:
                db_too_itg = 0.5
            
            db_tusuw = niit_db_too * 2524.39 * db_bairshil_itg * db_too_itg
    
        # HUTULBUR_TUSUW
    
            math_hut = (angi_3 * 1491.0 + angi_4 * 1610.0) * 0.021
            angli_hut = (angi_5 * 1656.0 + angi_6 * 1989.0) * 0.020
            ybs_tusuw = ybs_tusuw + math_hut + angli_hut
    
        # EH UUSWER
            niit_tusuw = ybs_tusuw + db_tusuw 
    
            if umch_helber == 'Төрийн':
                uls_tusuw = niit_tusuw
                huwi_tusuw = None
            else:
                if bairshil == "Нийслэл":
                    uls_tusuw = ybs_tusuw * 0.7125
                    huwi_tusuw = ybs_tusuw * 0.2875 + db_tusuw
                elif bairshil == "Аймгийн төвийн сум":
                    uls_tusuw = ybs_tusuw * 0.7142
                    huwi_tusuw = ybs_tusuw * 0.2858 + db_tusuw
                else:
                    uls_tusuw = ybs_tusuw * 0.7153
                    huwi_tusuw = ybs_tusuw * 0.2847 + db_tusuw
                    
            if bairshil == "Нийслэл":
                bagsh_tsalin = ybs_tusuw * 0.513
                bagsh_nemegdel = ybs_tusuw * 0.1893
                hicheel_zardal = ybs_tusuw * 0.01022
                zahirgaa_aa_tsalin = ybs_tusuw * 0.1561
                zahirgaa_aa_nemegdel = ybs_tusuw * 0.0547
                zahirgaa_aa_uram = ybs_tusuw * 0.00255
                surguuli_ajillagaa = ybs_tusuw * 0.01187
                bagsh_hugjil = ybs_tusuw * 0.00759
                eruul_mend_uilchilgee = ybs_tusuw * 0.00256
                tsahim = ybs_tusuw * 0.0186
                ybs_ariutgal = ybs_tusuw * 0.00258
                tanhimaas_gaduur = ybs_tusuw * 0.00170
                huuhed_hamgaalal = ybs_tusuw * 0.00253
                tonog_tuh_nuhult = ybs_tusuw * 0.0267
            elif bairshil == "Аймгийн төвийн сум":
                bagsh_tsalin = ybs_tusuw * 0.4684
                bagsh_nemegdel = ybs_tusuw * 0.2365
                hicheel_zardal = ybs_tusuw * 0.00928
                zahirgaa_aa_tsalin = ybs_tusuw * 0.1422
                zahirgaa_aa_nemegdel = ybs_tusuw * 0.0729
                zahirgaa_aa_uram = ybs_tusuw * 0.00316
                surguuli_ajillagaa = ybs_tusuw * 0.01083
                bagsh_hugjil = ybs_tusuw * 0.00692
                eruul_mend_uilchilgee = ybs_tusuw * 0.00228
                tsahim = ybs_tusuw * 0.0169
                ybs_ariutgal = ybs_tusuw * 0.00248
                tanhimaas_gaduur = ybs_tusuw * 0.0015
                huuhed_hamgaalal = ybs_tusuw * 0.00235
                tonog_tuh_nuhult = ybs_tusuw * 0.0243
            else:
                bagsh_tsalin = ybs_tusuw * 0.4206
                bagsh_nemegdel = ybs_tusuw * 0.2865
                hicheel_zardal = ybs_tusuw * 0.00823
                zahirgaa_aa_tsalin = ybs_tusuw * 0.1281
                zahirgaa_aa_nemegdel = ybs_tusuw * 0.09167
                zahirgaa_aa_uram = ybs_tusuw * 0.00424
                surguuli_ajillagaa = ybs_tusuw * 0.00965
                bagsh_hugjil = ybs_tusuw * 0.00627
                eruul_mend_uilchilgee = ybs_tusuw * 0.0021
                tsahim = ybs_tusuw * 0.0153
                ybs_ariutgal = ybs_tusuw * 0.00207
                tanhimaas_gaduur = ybs_tusuw * 0.00141
                huuhed_hamgaalal = ybs_tusuw * 0.00206
                tonog_tuh_nuhult = ybs_tusuw * 0.0218

        
        # SUB_INFO_ITGELTSUUR
        
        if baiguullaga == "СӨБ":
            huuhed_sub = row._11
            huuhed_sub_hb = row._12
            buleg = row._10
            y_buleg = row._13
            n_buleg = row._14
            if 1 < huuhed_sub <= 25:
                sub_too_itg = 2.5
            elif 25 < huuhed_sub <= 50:
                sub_too_itg = 2.3
            elif 50 < huuhed_sub <= 100:
                sub_too_itg = 1.75
            elif 100 < huuhed_sub <= 125:
                sub_too_itg = 1.6
            elif 125 < huuhed_sub <= 150:
                sub_too_itg = 1.51
            elif 150 < huuhed_sub <= 175:
                sub_too_itg = 1.5
            elif 175 < huuhed_sub <= 200:
                sub_too_itg = 1.35
            elif 200 < huuhed_sub <= 225:
                sub_too_itg = 1.3
            elif 225 < huuhed_sub <= 250:
                sub_too_itg = 1.2
            elif 250 < huuhed_sub <= 275:
                sub_too_itg = 1.17
            elif 275 < huuhed_sub <= 300:
                sub_too_itg = 1.14
            elif 300 < huuhed_sub <= 325:
                sub_too_itg = 1.1
            elif 325 < huuhed_sub <= 350:
                sub_too_itg = 1.08
            elif 350 < huuhed_sub <= 375:
                sub_too_itg = 1.06
            elif 375 < huuhed_sub <= 400:
                sub_too_itg = 1.05
            elif huuhed_sub > 400:
                sub_too_itg = 1

            if 1 < buleg <= 2:
                sub_buleg_itg = 1.018
            elif buleg == 3:
                sub_buleg_itg = 1.025
            elif buleg == 4:
                sub_buleg_itg = 1.028
            elif buleg == 5:
                sub_buleg_itg = 1.034
            elif buleg >= 6:
                sub_buleg_itg = 1.048
            else:
                sub_buleg_itg = 1
    
            
    
            if bairshil == "Нийслэл":
                bairshil_itg = 1
            elif bairshil == "Аймгийн төвийн сум":
                bairshil_itg = 1.183
            elif bairshil == "Сум":
                if tuwuus_als <= 200:
                    bairshil_itg = 1.35
                elif tuwuus_als > 200:
                    bairshil_itg = 1.354
            if 1 <= y_buleg <= 20:
                y_buleg_itg = 1.8
            elif 20 < y_buleg <= 35:
                y_buleg_itg = 1.1
            elif y_buleg > 35:
                y_buleg_itg = 0.8
            else:
                y_buleg_itg = 0
    
            if 1 <= n_buleg <= 20:
                n_buleg_itg = 1.8
            elif 20 < n_buleg <=40:
                n_buleg_itg = 1.3
            elif 40 < n_buleg <= 60:
                n_buleg_itg = 1
            elif 60 < n_buleg <= 80:
                n_buleg_itg = 0.7
            elif 80 < n_buleg:
                n_buleg_itg = 0.5
            else:
                n_buleg_itg = 0
    
            # SUB_TUSUW
            
            if hew_shinj == "Тусгай":
                sub_tusuw = (bairshil_itg * sub_too_itg * sub_buleg_itg * huuhed_sub * 1.3 * 2967.08 + (y_buleg * y_buleg_itg * 0.2 * 2967.08) + (n_buleg * n_buleg_itg * 0.25 * 2967.08))
                hew_shinj_itg = 1.3
            else:
                sub_tusuw = (bairshil_itg * sub_too_itg * sub_buleg_itg * ((huuhed_sub - huuhed_sub_hb) * 2967.08 + huuhed_sub_hb * 2967.08 * 3) + (y_buleg * y_buleg_itg * 0.2 * 2967.08) + (n_buleg * n_buleg_itg * 0.25 * 2967.08))
                hew_shinj_itg = None
            if umch_helber == "Төрийн":
                uls_tusuw = sub_tusuw
            else:
                if bairshil == "Нийслэл":
                    huwi_tusuw = sub_tusuw * 0.59952
                    uls_tusuw = sub_tusuw * 0.40047
                elif bairshil == "Аймгийн төвийн сум":
                    huwi_tusuw = sub_tusuw * 0.59972
                    uls_tusuw = sub_tusuw * 0.400277
                elif bairshil == "Сум":
                    huwi_tusuw = sub_tusuw * 0.59947
                    uls_tusuw = sub_tusuw * 0.4005

            if bairshil == "Нийслэл":
                bagsh_tsalin = sub_tusuw * 0.4448
                bagsh_nemegdel = sub_tusuw * 0.1254
                hicheel_zardal = sub_tusuw * 0.01086
                zahirgaa_aa_tsalin = sub_tusuw * 0.2819
                zahirgaa_aa_nemegdel = sub_tusuw * 0.10187
                zahirgaa_aa_uram = sub_tusuw * 0.00379
                zahirgaa_aa_nuhuh = sub_tusuw * 0.0012
                sub_ursgal_ariutgal = sub_tusuw * 0.0126
                huuhed_hamgaalal = sub_tusuw * 0.0038
                bagsh_hugjil = sub_tusuw * 0.00249
                eruul_mend_uilchilgee = sub_tusuw * 0.00249
                tsahim = sub_tusuw * 0.0055
                huuhdiin_togloom = sub_tusuw * 0.0033
            elif bairshil == "Аймгийн төвийн сум":
                bagsh_tsalin = sub_tusuw * 0.4003
                bagsh_nemegdel = sub_tusuw * 0.1675
                hicheel_zardal = sub_tusuw * 0.00981
                zahirgaa_aa_tsalin = sub_tusuw * 0.2538
                zahirgaa_aa_nemegdel = sub_tusuw * 0.13409
                zahirgaa_aa_uram = sub_tusuw * 0.00525
                zahirgaa_aa_nuhuh = sub_tusuw * 0.00161
                sub_ursgal_ariutgal = sub_tusuw * 0.0113
                huuhed_hamgaalal = sub_tusuw * 0.0034
                bagsh_hugjil = sub_tusuw * 0.0023
                eruul_mend_uilchilgee = sub_tusuw * 0.0023
                tsahim = sub_tusuw * 0.0053
                huuhdiin_togloom = sub_tusuw * 0.00304
            else:
                bagsh_tsalin = sub_tusuw * 0.3578
                bagsh_nemegdel = sub_tusuw * 0.2075
                hicheel_zardal = sub_tusuw * 0.00876
                zahirgaa_aa_tsalin = sub_tusuw * 0.2269
                zahirgaa_aa_nemegdel = sub_tusuw * 0.16558
                zahirgaa_aa_uram = sub_tusuw * 0.00669
                zahirgaa_aa_nuhuh = sub_tusuw * 0.00198
                sub_ursgal_ariutgal = sub_tusuw * 0.01
                huuhed_hamgaalal = sub_tusuw * 0.003
                bagsh_hugjil = sub_tusuw * 0.00201
                eruul_mend_uilchilgee = sub_tusuw * 0.00201
                tsahim = sub_tusuw * 0.0051
                huuhdiin_togloom = sub_tusuw * 0.00267
        # if turul_hut_itg == 1:
        #     turul_hut_itg = None
        # if db_bairshil_itg == 1:
        #     db_bairshil_itg = None
    
        if baiguullaga == "ЕБС":
            data.append({"Аймаг":aimag, 'Байгууллага':baiguullaga ,"Хэв шинж": hew_shinj, "Байршил":bairshil , "Дотуур байр байршил": db_bairshil, "Өмчийн хэлбэр":umch_helber , "Төрөлжсөн хөтөлбөр": turul_hut,
                         "Төвөөс алслагдсан байдал /км/":tuwuus_als, "Сургалтын төлбөр": surgalt_tulbur, "Салбар бүлэг": None, "СӨБ хүүхэд тоо": None, "Х.Б хүүхдийн тоо": None, "Явуулын бүлгийн хүүхэд тоо": None, "Нүүдлийн бүлгийн хүүхэд тоо": None,
                         "1-р анги": angi_1, "2-р анги": angi_2, "3-р анги": angi_3, "4-р анги": angi_4, "5-р анги": angi_5, "6-р анги": angi_6, "7-р анги": angi_7, "8-р анги": angi_8, "9-р анги": angi_9, "10-р анги": angi_10, "11-р анги": angi_11, "12-р анги": angi_12,"Нийт сурагч": niit_angi_too, 
                         "Х.Б 1-р анги": angi_1_hb, "Х.Б 2-р анги": angi_2_hb, "Х.Б 3-р анги": angi_3_hb, "Х.Б 4-р анги": angi_4_hb, "Х.Б 5-р анги": angi_5_hb, "Х.Б 6-р анги": angi_6_hb, "Х.Б 7-р анги": angi_7_hb, "Х.Б 8-р анги": angi_8_hb, "Х.Б 9-р анги": angi_9_hb, "Х.Б 10-р анги": angi_10_hb, "Х.Б 11-р анги": angi_11_hb, "Х.Б 12-р анги": angi_12_hb, "Нийт Х.Б хүүхэд тоо": niit_hb_too,
                         "Д.Б 1-р анги": angi_1_db, "Д.Б 2-р анги": angi_2_db, "Д.Б 3-р анги": angi_3_db, "Д.Б 4-р анги": angi_4_db, "Д.Б 5-р анги": angi_5_db, "Д.Б 6-р анги": angi_6_db, "Д.Б 7-р анги": angi_7_db, "Д.Б 8-р анги": angi_8_db, "Д.Б 9-р анги": angi_9_db, "Д.Б 10-р анги": angi_10_db, "Д.Б 11-р анги": angi_11_db, "Д.Б 12-р анги": angi_12_db, "Нийт Д.Б хүүхэд тоо": niit_db_too, "1-р анги бүлэг": angi_1_buleg, "2-р анги бүлэг": angi_2_buleg, "3-р анги бүлэг": angi_3_buleg, "4-р анги бүлэг": angi_4_buleg, "5-р анги бүлэг": angi_5_buleg, "6-р анги бүлэг": angi_6_buleg, "7-р анги бүлэг": angi_7_buleg, "8-р анги бүлэг": angi_8_buleg, "9-р анги бүлэг": angi_9_buleg, "10-р анги бүлэг": angi_10_buleg, "11-р анги бүлэг": angi_11_buleg, "12-р анги бүлэг": angi_12_buleg,
                         "Байршил итгэлцүүр": bairshil_itg, "Хэв шинж итгэлцүүр": hew_shinj_itg, "Баян-Өлгий аймаг итгэлцүүр": bayn_ulgii, "ЕБС сурагч тоо итгэлцүүр": suragch_too_itg,"СӨБ сурагч тоо итгэлцүүр": None, "Явуулын бүлэг итгэлцүүр": None, "Нүүдлийн бүлэг итгэлцүүр": None, "Сургалтын төлбөр итгэлцүүр": surgalt_tulbur_itg, "Дотуур байр байршил итгэлцүүр": db_bairshil_itg, "Төрөлжсөн хөтөлбөр итгэлцүүр": turul_hut_itg, "Багшийн цалин": bagsh_tsalin, "Багшийн нэмэгдэл": bagsh_nemegdel, "Сургалтын үйл ажиллагаа зардал": hicheel_zardal, "Захиргаа, АА цалин": zahirgaa_aa_tsalin, "Захиргаа, АА нэмэгдэл": zahirgaa_aa_nemegdel, "Захиргаа, АА нөхөх төлбөр": None, "Захиргаа, АА урамшуулал": zahirgaa_aa_uram, "Сургуулийн үйл ажиллагааны урсгал зардал": surguuli_ajillagaa, "Багш хөгжил": bagsh_hugjil, "Эрүүл мэндийн үйлчилгээний зардал": eruul_mend_uilchilgee, "Цахим хэрэглээний зардал": tsahim, "Цэцэрлэг үйл ажиллагаа болон ариутгал зардал": None, "ЕБС Анги ариутгал цэвэрлэгээний зардал": ybs_ariutgal, "Хүүхдийн тоглоом/тоног төхөөрөмж нөхөн хангалт": None,"Танхимаас гадуурх үйл ажиллагаа зардал": tanhimaas_gaduur, "Хүүхэд хамгаалал": huuhed_hamgaalal, "ЕБС Тоног төхөөрөмж нөхөн хангалт": tonog_tuh_nuhult,
                         "Дотуур байр төсөв": db_tusuw, "Мать хөтөлбөр төсөв": math_hut,"Англи хэл хөтөлбөр төсөв": angli_hut, "Сургууль төсөв": ybs_tusuw, "ЕБС нийт төсөв": niit_tusuw, "СӨБ нийт төсөв": None,"Төрөөс хариуцах": uls_tusuw,"Үүсгэн байгуулагч хариуцах": huwi_tusuw, "Нэг хүүхдийн дундаж хувьсах зардал":niit_tusuw/niit_angi_too })
        else:
            data.append({"Аймаг":aimag,'Байгууллага':baiguullaga ,"Хэв шинж": hew_shinj, "Байршил":bairshil , "Дотуур байр байршил": None, "Өмчийн хэлбэр":umch_helber , "Төрөлжсөн хөтөлбөр": None,
                         "Төвөөс алслагдсан байдал /км/":tuwuus_als, "Сургалтын төлбөр": surgalt_tulbur, "Салбар бүлэг": buleg, "СӨБ хүүхэд тоо": huuhed_sub, "Х.Б хүүхдийн тоо": huuhed_sub_hb, "Явуулын бүлгийн хүүхэд тоо": y_buleg, "Нүүдлийн бүлгийн хүүхэд тоо": n_buleg,
                         "1-р анги": None, "2-р анги": None, "3-р анги": None, "4-р анги": None, "5-р анги": None, "6-р анги": None, "7-р анги": None, "8-р анги": None, "9-р анги": None, "10-р анги": None, "11-р анги": None, "12-р анги": None,"Нийт сурагч": None, 
                         "Х.Б 1-р анги": None, "Х.Б 2-р анги": None, "Х.Б 3-р анги": None, "Х.Б 4-р анги": None, "Х.Б 5-р анги": None, "Х.Б 6-р анги": None, "Х.Б 7-р анги": None, "Х.Б 8-р анги": None, "Х.Б 9-р анги": None, "Х.Б 10-р анги": None, "Х.Б 11-р анги": None, "Х.Б 12-р анги": None, "Нийт Х.Б хүүхэд тоо": None,
                         "Д.Б 1-р анги": None, "Д.Б 2-р анги": None, "Д.Б 3-р анги": None, "Д.Б 4-р анги": None, "Д.Б 5-р анги": None, "Д.Б 6-р анги": None, "Д.Б 7-р анги": None, "Д.Б 8-р анги": None, "Д.Б 9-р анги": None, "Д.Б 10-р анги": None, "Д.Б 11-р анги": None, "Д.Б 12-р анги": None,"Нийт Д.Б хүүхэд тоо": None, "1-р анги бүлэг": angi_1_buleg, "2-р анги бүлэг": angi_2_buleg, "3-р анги бүлэг": angi_3_buleg, "4-р анги бүлэг": angi_4_buleg, "5-р анги бүлэг": angi_5_buleg, "6-р анги бүлэг": angi_6_buleg, "7-р анги бүлэг": angi_7_buleg, "8-р анги бүлэг": angi_8_buleg, "9-р анги бүлэг": angi_9_buleg, "10-р анги бүлэг": angi_10_buleg, "11-р анги бүлэг": angi_11_buleg, "12-р анги бүлэг": angi_12_buleg,
                         "Байршил итгэлцүүр": bairshil_itg, "Хэв шинж итгэлцүүр": hew_shinj_itg, "Баян-Өлгий аймаг итгэлцүүр": bayn_ulgii, "ЕБС сурагч тоо итгэлцүүр": None,"СӨБ сурагч тоо итгэлцүүр": sub_too_itg, "Явуулын бүлэг итгэлцүүр": y_buleg_itg, "Нүүдлийн бүлэг итгэлцүүр": n_buleg_itg, "Сургалтын төлбөр итгэлцүүр": None, "Дотуур байр байршил итгэлцүүр": None, "Төрөлжсөн хөтөлбөр итгэлцүүр": None, "Багшийн цалин": bagsh_tsalin, "Багшийн нэмэгдэл": bagsh_nemegdel, "Сургалтын үйл ажиллагаа зардал": hicheel_zardal, "Захиргаа, АА цалин": zahirgaa_aa_tsalin, "Захиргаа, АА нэмэгдэл": zahirgaa_aa_nemegdel, "Захиргаа, АА нөхөх төлбөр": zahirgaa_aa_nuhuh, "Захиргаа, АА урамшуулал": zahirgaa_aa_uram, "Сургуулийн үйл ажиллагааны урсгал зардал": None, "Багш хөгжил": bagsh_hugjil, "Эрүүл мэндийн үйлчилгээний зардал": eruul_mend_uilchilgee, "Цахим хэрэглээний зардал": tsahim, "Цэцэрлэг үйл ажиллагаа болон ариутгал зардал": sub_ursgal_ariutgal, "ЕБС Анги ариутгал цэвэрлэгээний зардал": None, "Хүүхдийн тоглоом/тоног төхөөрөмж нөхөн хангалт": huuhdiin_togloom,"Танхимаас гадуурх үйл ажиллагаа зардал": None, "Хүүхэд хамгаалал": huuhed_hamgaalal, "ЕБС Тоног төхөөрөмж нөхөн хангалт": None,
                         "Дотуур байр төсөв": None, "Мать хөтөлбөр төсөв": None,"Англи хэл хөтөлбөр төсөв": None, "Сургууль төсөв": None, "ЕБС нийт төсөв": None, "СӨБ нийт төсөв": sub_tusuw,"Төрөөс хариуцах": uls_tusuw,"Үүсгэн байгуулагч хариуцах": huwi_tusuw, "Нэг хүүхдийн дундаж хувьсах зардал":sub_tusuw/huuhed_sub})
            
    df = pd.DataFrame(data)
    original_df = df.copy()
    buffer = BytesIO()
    original_df.to_excel(buffer, index=False)
    buffer.seek(0)
    st.download_button(
        label="Файл татах",
        data=buffer.getvalue(),
        file_name=f"{name}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    st.write(original_df)
    st.write(f":blue[ЕБС бүх төсөв: {round(original_df['ЕБС нийт төсөв'].sum(), 3)}]")
    st.write(f":blue[ЕБС дундаж хувьсах зардал: {round(original_df['ЕБС нийт төсөв'].sum()/original_df['Нийт сурагч'].sum(), 3)}]")
    st.write(f":blue[СӨБ бүх төсөв: {round(original_df['СӨБ нийт төсөв'].sum(), 3)}]")
    st.write(f":blue[СӨБ дундаж хувьсах зардал: {round(original_df['СӨБ нийт төсөв'].sum()/original_df['СӨБ хүүхэд тоо'].sum(), 3)}]")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        ybs_tsalin_usult = st.number_input("ЕБС Цалин өсөлт (%)", value=0.0)
    with col2:
        sub_tsalin_usult = st.number_input("СӨБ Цалин өсөлт (%):", value=0.0)
    with col3:
        ybs_busad_usult = st.number_input("ЕБС Бусад зардал өсөлт (%)", value=0.0)
    with col4:
        sub_busad_usult = st.number_input("СӨБ Бусад зардал өсөлт (%)", value=0.0)
        
    
    if ybs_tsalin_usult != 0 or sub_tsalin_usult != 0 or ybs_busad_usult != 0 or sub_busad_usult != 0:
        bairshils = ["Нийслэл", "Аймгийн төвийн сум", "Сум"]

        ybs_before = {
        b: group.iloc[0].copy()
        for b in bairshils
        if not (group := df[(df["Байгууллага"] == "ЕБС") & (df["Байршил"] == b)]).empty
        }
        sub_before = {
        b: group.iloc[0].copy()
        for b in bairshils
        if not (group := df[(df["Байгууллага"] == "СӨБ") & (df["Байршил"] == b)]).empty
        }

        if sub_tsalin_usult != 0 or sub_busad_usult != 0:
            df.loc[df["Байгууллага"] == "СӨБ", ["Багшийн цалин", "Багшийн нэмэгдэл", "Захиргаа, АА цалин", "Захиргаа, АА нэмэгдэл", "Захиргаа, АА нөхөх төлбөр","Захиргаа, АА урамшуулал"]] *= (sub_tsalin_usult/100 + 1)
            df.loc[df["Байгууллага"] == "СӨБ", ["Сургалтын үйл ажиллагаа зардал", "Багш хөгжил", "Эрүүл мэндийн үйлчилгээний зардал", "Цахим хэрэглээний зардал", "Цэцэрлэг үйл ажиллагаа болон ариутгал зардал", "Хүүхдийн тоглоом/тоног төхөөрөмж нөхөн хангалт","Танхимаас гадуурх үйл ажиллагаа зардал", "Хүүхэд хамгаалал"]] *= (sub_busad_usult/100 + 1)
            df.loc[df["Байгууллага"] == "СӨБ","СӨБ нийт төсөв"] = df[["Багшийн цалин", "Багшийн нэмэгдэл", "Сургалтын үйл ажиллагаа зардал", "Захиргаа, АА цалин", "Захиргаа, АА нэмэгдэл", "Захиргаа, АА нөхөх төлбөр", "Захиргаа, АА урамшуулал", "Багш хөгжил", "Эрүүл мэндийн үйлчилгээний зардал", "Цахим хэрэглээний зардал", "Цэцэрлэг үйл ажиллагаа болон ариутгал зардал", "Хүүхдийн тоглоом/тоног төхөөрөмж нөхөн хангалт","Танхимаас гадуурх үйл ажиллагаа зардал", "Хүүхэд хамгаалал"]].sum(axis=1)
            df.loc[(df["Байгууллага"] == "СӨБ") & (df["Өмчийн хэлбэр"] == "Төрийн"), "Төрөөс хариуцах"] = df.loc[(df["Байгууллага"] == "СӨБ") & (df["Өмчийн хэлбэр"] == "Төрийн"), "СӨБ нийт төсөв"]
            df.loc[(df["Байгууллага"] == "СӨБ") & (df["Өмчийн хэлбэр"] == "Хувийн") & (df["Байршил"] == "Нийслэл"), "Төрөөс хариуцах"] = df.loc[(df["Байгууллага"] == "СӨБ") & (df["Өмчийн хэлбэр"] == "Хувийн") & (df["Байршил"] == "Нийслэл"), "СӨБ нийт төсөв"] * 0.40047
            df.loc[(df["Байгууллага"] == "СӨБ") & (df["Өмчийн хэлбэр"] == "Хувийн") & (df["Байршил"] == "Аймгийн төвийн сум"), "Төрөөс хариуцах"] = df.loc[(df["Байгууллага"] == "СӨБ") & (df["Өмчийн хэлбэр"] == "Хувийн") & (df["Байршил"] == "Аймгийн төвийн сум"), "СӨБ нийт төсөв"] * 0.4004277
            df.loc[(df["Байгууллага"] == "СӨБ") & (df["Өмчийн хэлбэр"] == "Хувийн") & (df["Байршил"] == "Сум"), "Төрөөс хариуцах"] = df.loc[(df["Байгууллага"] == "СӨБ") & (df["Өмчийн хэлбэр"] == "Хувийн") & (df["Байршил"] == "Сум"), "СӨБ нийт төсөв"] * 0.400527
            df.loc[(df["Байгууллага"] == "СӨБ") & (df["Өмчийн хэлбэр"] == "Хувийн"), "Үүсгэн байгуулагч хариуцах"] = df.loc[(df["Байгууллага"] == "СӨБ") & (df["Өмчийн хэлбэр"] == "Хувийн"), "СӨБ нийт төсөв"] - df.loc[(df["Байгууллага"] == "СӨБ") & (df["Өмчийн хэлбэр"] == "Хувийн"), "Төрөөс хариуцах"]
            
        if ybs_tsalin_usult != 0 or ybs_busad_usult != 0:
            df.loc[df["Байгууллага"] == "ЕБС", ["Багшийн цалин", "Багшийн нэмэгдэл", "Захиргаа, АА цалин", "Захиргаа, АА нэмэгдэл","Захиргаа, АА урамшуулал"]] *= (ybs_tsalin_usult/100 + 1)
            df.loc[df["Байгууллага"] == "ЕБС", ["Сургалтын үйл ажиллагаа зардал", "Сургуулийн үйл ажиллагааны урсгал зардал", "Багш хөгжил", "Эрүүл мэндийн үйлчилгээний зардал", "Цахим хэрэглээний зардал", "ЕБС Анги ариутгал цэвэрлэгээний зардал", "Танхимаас гадуурх үйл ажиллагаа зардал", "Хүүхэд хамгаалал", "ЕБС Тоног төхөөрөмж нөхөн хангалт"]] *= (ybs_busad_usult/100 + 1)
            df.loc[df["Байгууллага"] == "ЕБС", "Сургууль төсөв"] = df[["Багшийн цалин", "Багшийн нэмэгдэл", "Сургалтын үйл ажиллагаа зардал", "Захиргаа, АА цалин", "Захиргаа, АА нэмэгдэл", "Захиргаа, АА урамшуулал", "Сургуулийн үйл ажиллагааны урсгал зардал", "Багш хөгжил", "Эрүүл мэндийн үйлчилгээний зардал", "Цахим хэрэглээний зардал", "ЕБС Анги ариутгал цэвэрлэгээний зардал", "Танхимаас гадуурх үйл ажиллагаа зардал", "Хүүхэд хамгаалал", "ЕБС Тоног төхөөрөмж нөхөн хангалт", "Мать хөтөлбөр төсөв", "Англи хэл хөтөлбөр төсөв"]].sum(axis=1)
            df.loc[df["Байгууллага"] == "ЕБС", "ЕБС нийт төсөв"] = df.loc[df["Байгууллага"] == "ЕБС", "Сургууль төсөв"] + df.loc[df["Байгууллага"] == "ЕБС", "Дотуур байр төсөв"]
            df.loc[(df["Байгууллага"] == "ЕБС") & (df["Өмчийн хэлбэр"] == "Төрийн"), "Төрөөс хариуцах"] = df.loc[(df["Байгууллага"] == "ЕБС") & (df["Өмчийн хэлбэр"] == "Төрийн"), "ЕБС нийт төсөв"]
            df.loc[(df["Байгууллага"] == "ЕБС") & (df["Өмчийн хэлбэр"] == "Хувийн") & (df["Байршил"] == "Нийслэл"), "Төрөөс хариуцах"] = df.loc[(df["Байгууллага"] == "ЕБС") & (df["Өмчийн хэлбэр"] == "Хувийн") & (df["Байршил"] == "Нийслэл"), "Сургууль төсөв"] * 0.7125
            df.loc[(df["Байгууллага"] == "ЕБС") & (df["Өмчийн хэлбэр"] == "Хувийн") & (df["Байршил"] == "Аймгийн төвийн сум"), "Төрөөс хариуцах"] = df.loc[(df["Байгууллага"] == "ЕБС") & (df["Өмчийн хэлбэр"] == "Хувийн") & (df["Байршил"] == "Аймгийн төвийн сум"), "Сургууль төсөв"] * 0.7142
            df.loc[(df["Байгууллага"] == "ЕБС") & (df["Өмчийн хэлбэр"] == "Хувийн") & (df["Байршил"] == "Сум"), "Төрөөс хариуцах"] = df.loc[(df["Байгууллага"] == "ЕБС") & (df["Өмчийн хэлбэр"] == "Хувийн") & (df["Байршил"] == "Сум"), "Сургууль төсөв"] * 0.7153
            df.loc[(df["Байгууллага"] == "ЕБС") & (df["Өмчийн хэлбэр"] == "Хувийн"), "Үүсгэн байгуулагч хариуцах"] = df.loc[(df["Байгууллага"] == "ЕБС") & (df["Өмчийн хэлбэр"] == "Хувийн"), "ЕБС нийт төсөв"] - df.loc[(df["Байгууллага"] == "ЕБС") & (df["Өмчийн хэлбэр"] == "Хувийн"), "Төрөөс хариуцах"]

            db_salary_ratios = {
            "Дотуур байр багш цалин": 0.132,
            "Дотуур байр багш нэмэгдэл": 0.0467,
            "Дотуур байр багш урамшуулал": 0.01,
            "Дотуур байр захиргаа, АА цалин": 0.5393,
            "Дотуур байр захиргаа, АА нэмэгдэл": 0.217,
            "Дотуур байр захиргаа, АА урамшуулал": 0.036
            }
            db_other_ratio = {
                "Дотуур байрны үйл ажиллагаа зардал": 0.019
            }
            
            db_all_ratios = {**db_salary_ratios, **db_other_ratio}

            db_salary_part = sum(db_salary_ratios.values())
            db_other_part = sum(db_other_ratio.values())
            
            dorm_multiplier = db_salary_part * (1 + ybs_tsalin_usult / 100) + db_other_part * (1 + ybs_busad_usult / 100)
            
            df.loc[df["Байгууллага"] == "ЕБС", "Дотуур байр төсөв"] *= dorm_multiplier

            df.loc[df["Байгууллага"] == "ЕБС", "ЕБС нийт төсөв"] = (
            df.loc[df["Байгууллага"] == "ЕБС", "Сургууль төсөв"] + 
            df.loc[df["Байгууллага"] == "ЕБС", "Дотуур байр төсөв"]
            )




        buffer = BytesIO()
        df.to_excel(buffer, index=False)
        buffer.seek(0)
        st.download_button(
            label="Шинэ файл татах",
            data=buffer.getvalue(),
            file_name=f"{name}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        st.write(df)


        def plot_composition_pie(before_dict, after_dict, title_prefix, pct_threshold=3):
            labels = list(before_dict.keys())
            before_vals = [before_dict[l] for l in labels]
            after_vals = [after_dict[l] for l in labels]
        
            def filter_labels(vals):
                return [f"{l}" if v >= pct_threshold else "" for l, v in zip(labels, vals)]
        
            fig = make_subplots(
                rows=1, cols=2,
                specs=[[{'type':'domain'}, {'type':'domain'}]],
                subplot_titles=[f"{title_prefix} — Өмнө", f"{title_prefix} — Дараа"]
            )
        
            fig.add_trace(go.Pie(
                labels=labels,
                values=before_vals,
                text=filter_labels(before_vals),
                hoverinfo='label+percent',
                textinfo='percent+text',
                hole=0.3
            ), row=1, col=1)
        
            fig.add_trace(go.Pie(
                labels=labels,
                values=after_vals,
                text=filter_labels(after_vals),
                hoverinfo='label+percent',
                textinfo='percent+text',
                hole=0.3
            ), row=1, col=2)
        
            fig.update_layout(
                title_text=f"{title_prefix} төсвийн бүтцийн харьцуулалт",
                height=500,
                showlegend=True,
                legend=dict(orientation="v", x=1.1, y=0.5),
                margin=dict(l=50, r=120, t=80, b=20)
            )
        
            st.plotly_chart(fig, use_container_width=True)

        ybs_after = {
        b: group.iloc[0].copy()
        for b in bairshils
        if not (group := df[(df["Байгууллага"] == "ЕБС") & (df["Байршил"] == b)]).empty}
        sub_after = {
        b: group.iloc[0].copy()
        for b in bairshils
        if not (group := df[(df["Байгууллага"] == "СӨБ") & (df["Байршил"] == b)]).empty}

        
        compare_cols_ybs = ["Багшийн цалин", "Багшийн нэмэгдэл", "Сургалтын үйл ажиллагаа зардал", "Захиргаа, АА цалин", "Захиргаа, АА нэмэгдэл", "Захиргаа, АА урамшуулал", "Сургуулийн үйл ажиллагааны урсгал зардал", "Багш хөгжил", "Эрүүл мэндийн үйлчилгээний зардал", "Цахим хэрэглээний зардал", "ЕБС Анги ариутгал цэвэрлэгээний зардал","Танхимаас гадуурх үйл ажиллагаа зардал", "Хүүхэд хамгаалал", "ЕБС Тоног төхөөрөмж нөхөн хангалт"]
        compare_cols_sub = ["Багшийн цалин", "Багшийн нэмэгдэл", "Сургалтын үйл ажиллагаа зардал", "Захиргаа, АА цалин", "Захиргаа, АА нэмэгдэл", "Захиргаа, АА нөхөх төлбөр", "Захиргаа, АА урамшуулал", "Багш хөгжил", "Эрүүл мэндийн үйлчилгээний зардал", "Цахим хэрэглээний зардал", "Цэцэрлэг үйл ажиллагаа болон ариутгал зардал", "Хүүхдийн тоглоом/тоног төхөөрөмж нөхөн хангалт", "Хүүхэд хамгаалал"]

        
        def get_composition(row, cols):
            total = row[cols].sum()
            return {col: (row[col] / total * 100 if total != 0 else 0) for col in cols}
            
        
        for b in bairshils:
            try:
                before_ybs = get_composition(ybs_before[b], compare_cols_ybs)
                after_ybs = get_composition(ybs_after[b], compare_cols_ybs)
            
                comp_df_ybs = pd.DataFrame({
                    "Төрөл": compare_cols_ybs,
                    "Өмнө (%)": [before_ybs[c] for c in compare_cols_ybs],
                    "Дараа (%)": [after_ybs[c] for c in compare_cols_ybs],
                    "Өөрчлөлт (%)": [after_ybs[c] - before_ybs[c] for c in compare_cols_ybs]
                })
    
                tab1, tab2 = st.tabs(["🧩 Хүснэгт", "📊 График"])
                with tab1:
                    st.subheader(f"ЕБС төсвийн бүтэц өөрчлөлт — {b}")
                    st.dataframe(comp_df_ybs.style.format({
                    "Өмнө (%)": "{:.2f}",
                    "Дараа (%)": "{:.2f}",
                    "Өөрчлөлт (%)": "{:.2f}"
                    }))
                with tab2:
                    plot_composition_pie(
                    before_dict=before_ybs,
                    after_dict=after_ybs,
                    title_prefix=f"ЕБС төсөв — {b}",
                    )
            except:
                pass
        for b in bairshils:
            try:
                before_sub = get_composition(sub_before[b], compare_cols_sub)
                after_sub = get_composition(sub_after[b], compare_cols_sub)
            
                comp_df_sub = pd.DataFrame({
                    "Төрөл": compare_cols_sub,
                    "Өмнө (%)": [before_sub[c] for c in compare_cols_sub],
                    "Дараа (%)": [after_sub[c] for c in compare_cols_sub],
                    "Өөрчлөлт (%)": [after_sub[c] - before_sub[c] for c in compare_cols_sub]
                })
                tab1, tab2 = st.tabs(["🧩 Хүснэгт", "📊 График"])
                with tab1:
                    st.subheader(f"СӨБ төсвийн бүтэц өөрчлөлт — {b}")
                    st.dataframe(comp_df_sub.style.format({
                    "Өмнө (%)": "{:.2f}",
                    "Дараа (%)": "{:.2f}",
                    "Өөрчлөлт (%)": "{:.2f}"
                    }))
                with tab2:
                    plot_composition_pie(
                    before_dict=before_sub,
                    after_dict=after_sub,
                    title_prefix=f"СӨБ төсөв — {b}",
                    )
            except:
                pass

        db_salary_ratios = {
            "Дотуур байр багш цалин": 0.132,
            "Дотуур байр багш нэмэгдэл": 0.0467,
            "Дотуур байр багш урамшуулал": 0.01,
            "Дотуур байр захиргаа, АА цалин": 0.5393,
            "Дотуур байр захиргаа, АА нэмэгдэл": 0.217,
            "Дотуур байр захиргаа, АА урамшуулал": 0.036
        }
        db_other_ratio = {
            "Дотуур байрны үйл ажиллагаа зардал": 0.019
        }
        
        db_all_ratios = {**db_salary_ratios, **db_other_ratio}
        
        dorm_row = df[(df["Байгууллага"] == "ЕБС") & (df["Дотуур байр төсөв"] > 0)].iloc[0]
        dorm_total_before = dorm_row["Дотуур байр төсөв"]
        
        def get_percent_composition(total, ratio_dict):
            return {k: v * 100 for k, v in ratio_dict.items()}
        
        def get_adjusted_percent_composition(base, tsalin_usult, busad_usult):
            adjusted = {}
            for k, v in base.items():
                if k == "Дотуур байрны үйл ажиллагаа зардал":
                    adjusted[k] = v * (1 + busad_usult / 100)
                else:
                    adjusted[k] = v * (1 + tsalin_usult / 100)
            total = sum(adjusted.values())
            return {k: (v / total * 100 if total != 0 else 0) for k, v in adjusted.items()}
        
        base_comp = get_percent_composition(dorm_total_before, db_all_ratios)
        after_comp = get_adjusted_percent_composition(base_comp, ybs_tsalin_usult, ybs_busad_usult)
        
        comp_df = pd.DataFrame({
            "Төрөл": list(base_comp.keys()),
            "Өмнө (%)": [base_comp[k] for k in base_comp],
            "Дараа (%)": [after_comp[k] for k in base_comp],
            "Өөрчлөлт (%)": [after_comp[k] - base_comp[k] for k in base_comp]})

        tab1, tab2 = st.tabs(["🧩 Хүснэгт", "📊 График"])
        with tab1:
            st.subheader("Дотуур байр төсвийн бүтэц")
            st.dataframe(comp_df.style.format({
                "Өмнө (%)": "{:.2f}",
                "Дараа (%)": "{:.2f}",
                "Өөрчлөлт (%)": "{:.2f}"
            }))
        with tab2:
                plot_composition_pie(
                before_dict=base_comp,
                after_dict=after_comp,
                title_prefix=f"Дотуур байр төсөв",
                )

else:
    st.warning("Файл оруулаагүй байна.")
