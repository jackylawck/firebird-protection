import streamlit as st
from story_data import STORIES

# ----------------- 頁面基礎配置 -----------------
st.set_page_config(
    page_title="火鷹俠故事館 | Firebird Protection",
    page_icon="🦸‍♂️",
    layout="centered"
)

# ----------------- 🎨 兒童雙語與漫畫風格 CSS -----------------
st.markdown("""
    <style>
    .stApp { background-color: #E0F7FA; color: #000000 !important; }
    p, span, label, div, h1, h2, h3, h4 { color: #000000 !important; font-family: 'Comic Sans MS', sans-serif; }
    .kids-title { font-size: clamp(1.8rem, 5vw, 2.5rem) !important; color: #00838F !important; font-weight: 900; text-align: center; margin-bottom: 5px; }
    .en-title { font-size: clamp(1rem, 3vw, 1.4rem) !important; color: #006064 !important; font-weight: 900; text-align: center; margin-bottom: 15px; }
    
    /* 故事卡片 */
    .story-card {
        background: #FFFFFF;
        border: 4px solid #000000;
        border-radius: 20px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 6px 6px 0px #000000;
    }
    .story-title { font-size: 1.5rem !important; color: #D81B60 !important; font-weight: 900; margin-bottom: 5px; }
    .story-progress { font-size: 0.9rem !important; color: #00838F !important; font-weight: bold; background: #E0F7FA; padding: 4px 12px; border-radius: 10px; display: inline-block; margin-bottom: 10px; }
    .story-sfx { font-size: 1.2rem !important; color: #FF9800 !important; font-weight: 900; margin-bottom: 10px; }
    .story-text-tc { font-size: 1.3rem !important; line-height: 1.6; font-weight: bold; color: #000000 !important; }
    .story-text-en { font-size: 1.1rem !important; line-height: 1.5; font-weight: 600; color: #424242 !important; margin-top: 8px; }

    /* 按鈕樣式與置中 */
    div.stButton { display: flex; justify-content: center; }
    div.stButton > button {
        background-color: #FFEB3B !important; color: #000000 !important;
        font-size: 1.2rem !important; font-weight: 900 !important;
        border: 4px solid #000000 !important; border-radius: 16px !important;
        padding: 12px 20px !important; box-shadow: 4px 4px 0px #000000 !important;
        width: 100% !important; max-width: 550px !important;
        margin-bottom: 12px !important;
    }
    div.stButton > button:hover { background-color: #FFD600 !important; }
    
    /* 側邊欄專用樣式 */
    [data-testid="stSidebar"] { background-color: #1E293B !important; }
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span { color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# ----------------- 標題與簡介 -----------------
st.markdown('<p class="kids-title">🦸‍♂️ 火鷹俠全人教育故事館 🚀</p>', unsafe_allow_html=True)
st.markdown('<p class="en-title">Firebird Protection: Whole-Person Interactive Hub</p>', unsafe_allow_html=True)
st.caption("Son & Dad Exclusive | PERCCI 品格培育 × STEAM 雙語繪本")
st.markdown("---")

# ----------------- ⚙️ 側邊欄：故事選擇與控制 -----------------
st.sidebar.markdown("## 📚 選擇冒險故事")
story_choice = st.sidebar.radio(
    "小隊長，你想玩邊個故事？", 
    ["Story1", "Story2", "Story3"],
    format_func=lambda x: STORIES[x]["name_tc"]
)

# 當切換不同故事時，自動重置進度回第一頁
if "current_story" not in st.session_state or st.session_state.current_story != story_choice:
    st.session_state.current_story = story_choice
    st.session_state.current_scene = "1_START"

if "current_scene" not in st.session_state:
    st.session_state.current_scene = "1_START"

current_story_nodes = STORIES[st.session_state.current_story]["nodes"]
scene_key = st.session_state.current_scene

if scene_key not in current_story_nodes:
    st.session_state.current_scene = "1_START"
    scene_key = "1_START"

scene = current_story_nodes[scene_key]

# 計算當前頁數進度 (根據節點名稱如 1_START, 2_A 推算)
try:
    current_page = scene_key.split('_')[0]
except:
    current_page = "1"

# ----------------- 📖 主畫面：顯示故事卡片 -----------------
st.markdown(f'''
    <div class="story-card">
        <span class="story-progress">📌 進度 (Progress): 第 {current_page} 頁 / 共 6 頁</span>
        <div class="story-title">📖 {scene.get("title_tc", "")} ({scene.get("title_en", "")})</div>
        <div class="story-sfx">{scene.get("sfx", "")}</div>
        <div class="story-text-tc">{scene.get("story_tc", "")}</div>
        <div class="story-text-en">{scene.get("story_en", "")}</div>
    </div>
''', unsafe_allow_html=True)

# ----------------- 🖼️ 顯示插圖（加入圖片容錯處理） -----------------
if "images" in scene and scene["images"]:
    cols = st.columns(len(scene["images"]))
    for idx, img_url in enumerate(scene["images"]):
        with cols[idx]:
            try:
                st.image(img_url, use_container_width=True)
            except Exception:
                # 圖片失效時顯示備用想像力插圖，防止介面破裂
                st.image("https://via.placeholder.com/800x500?text=🎨+火鷹俠+想像力+繪本", use_container_width=True)

st.markdown("---")
st.markdown("### 🎯 小隊長，下一步你要點做？ (What will you do next?)")

# ----------------- 🎯 顯示互動選項按鈕 -----------------
choices = scene.get("choices", {})

if choices:
    for opt_key, opt_text in choices.items():
        if st.button(f"👉 選項 {opt_key}: {opt_text}"):
            next_scene_id = f"{int(scene_key.split('_')[0]) + 1}_{opt_key}"
            
            if next_scene_id in current_story_nodes:
                st.session_state.current_scene = next_scene_id
            else:
                st.session_state.current_scene = "1_START"
            st.rerun()
else:
    st.success("🎉 恭喜你完成咗呢個冒險章節！ (Chapter Completed!)")
    if st.button("🔄 重新開始故事 (Restart Story)"):
        st.session_state.current_scene = "1_START"
        st.rerun()

# 側邊欄返回第一頁按鈕
st.sidebar.markdown("---")
st.sidebar.markdown(f"**目前位置：** 第 {current_page} 頁")
if st.sidebar.button("🔄 返回故事第一頁"):
    st.session_state.current_scene = "1_START"
    st.rerun()
