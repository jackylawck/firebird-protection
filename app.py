import streamlit as st
from story_data import STORY_1_SCENES

# 頁面配置
st.set_page_config(
    page_title="火鷹俠故事館 | Firebird Protection",
    page_icon="🦸‍♂️",
    layout="centered"
)

# 🎨 兒童雙語與漫畫風 CSS
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
    .story-sfx { font-size: 1.2rem !important; color: #FF9800 !important; font-weight: 900; margin-bottom: 10px; }
    .story-text-tc { font-size: 1.3rem !important; line-height: 1.6; font-weight: bold; color: #000000 !important; }
    .story-text-en { font-size: 1.1rem !important; line-height: 1.5; font-weight: 600; color: #424242 !important; margin-top: 8px; }

    /* 按鈕置中與最大寬度限制 */
    div.stButton { display: flex; justify-content: center; }
    div.stButton > button {
        background-color: #FFEB3B !important; color: #000000 !important;
        font-size: 1.2rem !important; font-weight: 900 !important;
        border: 4px solid #000000 !important; border-radius: 16px !important;
        padding: 10px 20px !important; box-shadow: 4px 4px 0px #000000 !important;
        width: 100% !important; max-width: 500px !important;
        margin-bottom: 10px !important;
    }
    div.stButton > button:hover { background-color: #FFD600 !important; }
    </style>
""", unsafe_allow_html=True)

# ----------------- 標題與簡介 -----------------
st.markdown('<p class="kids-title">🦸‍♂️ 火鷹俠全人教育故事館 🚀</p>', unsafe_allow_html=True)
st.markdown('<p class="en-title">Firebird Protection: Interactive Storybook</p>', unsafe_allow_html=True)
st.caption("Son & Dad Exclusive | 純本地流暢模式 | 雙語互動繪本")
st.markdown("---")

# 初始化故事狀態
if "current_scene" not in st.session_state:
    st.session_state.current_scene = "1_START"

scene_key = st.session_state.current_scene

# 如果找不到對應章節，重置回起點
if scene_key not in STORY_1_SCENES:
    st.session_state.current_scene = "1_START"
    scene_key = "1_START"

scene = STORY_1_SCENES[scene_key]

# ----------------- 顯示當前頁面內容 -----------------
st.markdown(f'''
    <div class="story-card">
        <div class="story-title">📖 {scene.get("title_tc", "")} ({scene.get("title_en", "")})</div>
        <div class="story-sfx">{scene.get("sfx", "")}</div>
        <div class="story-text-tc">{scene.get("story_tc", "")}</div>
        <div class="story-text-en">{scene.get("story_en", "")}</div>
    </div>
''', unsafe_allow_html=True)

# 顯示插圖（如果有的話）
if "images" in scene and scene["images"]:
    cols = st.columns(len(scene["images"]))
    for idx, img_url in enumerate(scene["images"]):
        with cols[idx]:
            st.image(img_url, use_column_width=True)

st.markdown("---")
st.markdown("### 🎯 小隊長，下一步你要點做？ (What will you do next?)")

# ----------------- 顯示選項按鈕 -----------------
choices = scene.get("choices", {})

if choices:
    for opt_key, opt_text in choices.items():
        # 按鈕點擊後切換章節
        if st.button(f"👉 選項 {opt_key}: {opt_text}"):
            # 故事節點推算邏輯 (例如 1_START 選擇 A -> 變成 2_A)
            next_scene_id = f"{int(scene_key.split('_')[0]) + 1}_{opt_key}"
            
            # 檢查是否存在下一個章節
            if next_scene_id in STORY_1_SCENES:
                st.session_state.current_scene = next_scene_id
            else:
                # 若沒有下個節點，嘗試尋找 END 或返回起點
                st.session_state.current_scene = "1_START"
            st.rerun()
else:
    st.success("🎉 恭喜你完成咗呢個冒險章節！ (Chapter Completed!)")
    if st.button("🔄 重新開始故事 (Restart Story)"):
        st.session_state.current_scene = "1_START"
        st.rerun()

# 側邊欄重置
st.sidebar.markdown("## ⚙️ 故事控制")
if st.sidebar.button("🔄 返回故事第一頁"):
    st.session_state.current_scene = "1_START"
    st.rerun()
