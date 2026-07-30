import streamlit as st
import random
import time

# 頁面配置
st.set_page_config(
    page_title="Firebird Protection | 火鷹俠故事總部",
    page_icon="🔥",
    layout="centered"
)

# CSS 樣式美化 (支援深色/淺色模式，高對比度文字)
st.markdown("""
    <style>
    .main-title { 
        font-size: 2.3rem; 
        color: #FF4B4B; 
        font-weight: bold; 
        text-align: center; 
        margin-bottom: 5px;
    }
    .story-card { 
        background-color: #F0F4F8; 
        color: #1A1A1A !important; 
        padding: 20px; 
        border-radius: 12px; 
        border-left: 6px solid #FF4B4B; 
        margin-bottom: 20px;
        font-size: 1.05rem;
        line-height: 1.6;
    }
    .story-card b, .story-card i {
        color: #000000 !important;
    }
    .highlight-box {
        background-color: #FFF3CD;
        color: #856404 !important;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #FFEBAA;
        font-weight: bold;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# 語言切換選單
lang = st.sidebar.radio("🌐 Language / 語言", ["繁體中文", "English"])

# 側邊欄：英雄檔案
if lang == "繁體中文":
    st.sidebar.header("🛡️ 火鷹俠 (Firebird) 檔案")
    st.sidebar.info("**主角：** Jarvis (火鷹俠)")
    st.sidebar.success("**系統：** Firebird Protection v2.0")
    st.sidebar.progress(100, text="能量值：100% 滿格")
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎒 裝備與合體技能")
    st.sidebar.write("• **光影翅膀 (Firebird Wings)**")
    st.sidebar.write("• **百獸召喚 (Animal Squad)**")
    st.sidebar.write("• **獅王合體 (Lion Fusion)**")
    st.sidebar.write("• **終極絕招：顏色沙漠土**")
else:
    st.sidebar.header("🛡️ Firebird Profile")
    st.sidebar.info("**Hero:** Jarvis (Firebird)")
    st.sidebar.success("**System:** Firebird Protection v2.0")
    st.sidebar.progress(100, text="Energy: 100% Full")
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎒 Gear & Fusion Skills")
    st.sidebar.write("• **Firebird Wings**")
    st.sidebar.write("• **Animal Squad Call**")
    st.sidebar.write("• **Lion Fusion Form**")
    st.sidebar.write("• **Finisher: Desert Sand of Color**")

# 主標題
if lang == "繁體中文":
    st.markdown('<p class="main-title">🔥🦅 火鷹俠：Firebird Protection 傳奇</p>', unsafe_allow_html=True)
    st.caption("Jarvis 與爸爸聯合創作 — 雙語互動式英雄故事 App")
else:
    st.markdown('<p class="main-title">🔥🦅 Firebird Protection Legends</p>', unsafe_allow_html=True)
    st.caption("Co-created by Jarvis & Dad — Interactive Story Generator")

st.markdown("---")

# 主選單分頁
tab1, tab2 = st.tabs(["📖 經典故事篇章 (Classic Story)", "🎲 100篇故事生成器 (100 Story Generator)"])

# ----------------- Tab 1: 經典故事 -----------------
with tab1:
    if lang == "繁體中文":
        st.header("📜 主線故事：森林百獸合體大作戰")
        
        with st.expander("📖 第一章：走得太遠的深山冒險", expanded=True):
            st.markdown("""
            <div class="story-card">
            火鷹俠邊打電話邊尋找隱蔽地方，一不留神就走得太遠，來到了一座神秘的深山森林。<br>
            為了不被壞人發現，他藏在樹林深處，啟動了 <b>Firebird Protection</b> 的正義力量！<br>
            森林裡的野生動物們感受到了英雄的光芒，紛紛聚集過來，自願成為火鷹俠的忠誠手下！
            </div>
            """, unsafe_allow_html=True)

        with st.expander("📖 第二章：搜捕與發現壞人", expanded=True):
            st.markdown("""
            <div class="story-card">
            「大家一齊搵壞人！」火鷹俠一聲令下，動物大軍動員起來：小鳥在空中觀察，獵豹在陸地追蹤。<br>
            大家齊心協力，終於在山谷深處的溶洞裡找到了藏在那裡的壞人！
            </div>
            """, unsafe_allow_html=True)

        with st.expander("📖 第三章：獅王合體！", expanded=True):
            st.markdown("""
            <div class="story-card">
            面對壞人掏出的黑科技武器，百獸之王獅子大吼一聲衝上前！<br>
            火鷹俠將光影翅膀與獅子的霸氣力量融合——<br>
            <b>「 Firebird Protection！獅王火鷹俠，合體！！」</b>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("⚡ 決戰時刻：發動終極絕招！")
        if st.button("🔥 喊出絕招：顏色沙漠土！！"):
            st.balloons()
            st.markdown("""
            <div class="story-card" style="border-left: 6px solid #28A745;">
            <b>【第四章：完美成功拯救世界！】</b><br><br>
            獅王火鷹俠全身閃耀著金紅色的光芒，大聲喊出絕招：<br>
            <h3 style="color: #FF4B4B; text-align: center;">「—— 顏色沙漠土 ！！！」</h3><br>
            一道耀眼的彩虹火焰閃過，壞人與他們的武器瞬間全被淨化，變成了五彩繽紛的<b>「顏色沙漠土」</b>飄散在空中！<br><br>
            <b>🎉 成功啦！火鷹俠與動物手下們打勝仗，成功拯救了世界！</b>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.header("📜 Main Story: Forest Beast Fusion Battle")
        
        with st.expander("📖 Chapter 1: Deep into the Forest", expanded=True):
            st.markdown("""
            <div class="story-card">
            While on a phone call, Firebird accidentally walked too far and reached a deep, mysterious forest.<br>
            To stay hidden, he activated his <b>Firebird Protection</b> power! <br>
            The wild forest animals felt his heroic light and willingly became his loyal sidekicks!
            </div>
            """, unsafe_allow_html=True)

        with st.expander("📖 Chapter 2: Searching for Villains", expanded=True):
            st.markdown("""
            <div class="story-card">
            "Let's find the villains!" Firebird commanded. Birds scanned from the sky while leopards tracked on the ground.<br>
            Together, the animal squad finally spotted the villains hiding deep inside a mountain cave!
            </div>
            """, unsafe_allow_html=True)

        with st.expander("📖 Chapter 3: Lion Fusion!", expanded=True):
            st.markdown("""
            <div class="story-card">
            Facing the villain's heavy machinery, the King of Beasts—the Lion—roared and stepped forward!<br>
            Firebird combined his flame wings with the Lion's strength:<br>
            <b>"Firebird Protection! Lion Firebird Fusion!!"</b>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("⚡ Final Battle: Launch Ultimate Move!")
        if st.button("🔥 Shouting Move: Desert Sand of Color!!"):
            st.balloons()
            st.markdown("""
            <div class="story-card" style="border-left: 6px solid #28A745;">
            <b>【Chapter 4: World Saved Successfully!】</b><br><br>
            Glowing with golden-red energy, Lion Firebird shouted at the top of his lungs:<br>
            <h3 style="color: #FF4B4B; text-align: center;">"—— DESERT SAND OF COLOR !!!"</h3><br>
            A massive blast of rainbow flame swept across! The villains and their cannons instantly turned into colorful <b>Desert Sand of Color</b>!<br><br>
            <b>🎉 VICTORY! Firebird and the animal squad successfully saved the world!</b>
            </div>
            """, unsafe_allow_html=True)

# ----------------- Tab 2: 100篇故事生成器 -----------------
with tab2:
    if lang == "繁體中文":
        st.header("🎲 火鷹俠 100 篇冒險故事庫")
        st.write("利用動態生成技術，為 Jarvis 產生 100 篇獨一無二的火鷹俠冒險故事！")
        
        num_stories = st.slider("選擇要展示的故事數量：", 1, 100, 5)
        
        if st.button("🚀 生成故事"):
            animals_list = ["森林百獸", "飛天巨鷹隊", "迅捷猛虎群", "鋼鐵大象隊", "深山靈猴群"]
            fusion_list = ["百獸之王獅子", "黃金飛龍", "冰霜雪豹", "雷霆巨熊", "機械火鳳凰"]
            villain_list = ["時光黑影", "泥漿怪客", "噪音博士", "影子大魔王", "鋼鐵怪獸"]
            sand_list = ["顏色沙漠土", "彩虹星辰土", "五彩水晶砂", "黃金耀眼土"]

            st.success(f"已成功為你生成 {num_stories} 篇火鷹俠故事！")
            
            for i in range(1, num_stories + 1):
                a = random.choice(animals_list)
                f = random.choice(fusion_list)
                v = random.choice(villain_list)
                s = random.choice(sand_list)
                
                st.markdown(f"""
                <div class="story-card">
                <b>🔥 第 {i} 篇：火鷹俠與{f}的{s}大作戰</b><br>
                • <b>起因：</b> 火鷹俠打電話匿埋走太遠來到深山，召喚了【{a}】成為手下。<br>
                • <b>搜捕：</b> 手下們齊心協力，終於在山谷裏找到了壞人【{v}】！<br>
                • <b>合體：</b> 火鷹俠與【{f}】發動強大合體！<br>
                • <b>決戰：</b> 喊出一聲絕招<b>「{s}！」</b>將壞人全部變成彩色的土，成功拯救世界！
                </div>
                """, unsafe_allow_html=True)
    else:
        st.header("🎲 Firebird 100 Adventures Generator")
        st.write("Generates 100 unique Firebird adventure stories for Jarvis!")
        
        num_stories = st.slider("Select number of stories to display:", 1, 100, 5)
        
        if st.button("🚀 Generate Stories"):
            animals_list = ["Forest Beasts", "Eagle Squad", "Tiger Unit", "Elephant Force", "Monkey Troop"]
            fusion_list = ["Mighty Lion", "Golden Dragon", "Frost Leopard", "Thunder Bear", "Mecha Phoenix"]
            villain_list = ["Clockwork Shadow", "Mud Villain", "Noise Master", "Shadow King", "Iron Beast"]
            sand_list = ["Desert Sand of Color", "Rainbow Star Dust", "Crystal Sand", "Golden Sparkle Dust"]

            st.success(f"Successfully generated {num_stories} Firebird stories!")
            
            for i in range(1, num_stories + 1):
                a = random.choice(animals_list)
                f = random.choice(fusion_list)
                v = random.choice(villain_list)
                s = random.choice(sand_list)
                
                st.markdown(f"""
                <div class="story-card">
                <b>🔥 Story #{i}: Firebird & {f}'s {s} Operation</b><br>
                • <b>Start:</b> Firebird walked too far into the forest during a phone call and summoned the 【{a}】 as sidekicks.<br>
                • <b>Search:</b> The sidekicks searched everywhere and spotted the villain 【{v}】!<br>
                • <b>Fusion:</b> Firebird fused with 【{f}】 for ultimate strength!<br>
                • <b>Finisher:</b> Shouted <b>"{s}!"</b> turning the villains into colorful dust. Mission Success!
                </div>
                """, unsafe_allow_html=True)

# 頁尾
st.markdown("---")
st.caption("🔥 Firebird Protection App v2.0 | Co-created by Jarvis & Dad")
