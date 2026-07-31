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
    
    /* 普通故事卡片 */
    .story-card {
        background: #FFFFFF;
        border: 4px solid #000000;
        border-radius: 20px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 6px 6px 0px #000000;
    }
    
    /* 💥 壞結局卡片 */
    .bad-card {
        background: #FFEBEE;
        border: 4px solid #D32F2F;
        border-radius: 20px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 6px 6px 0px #D32F2F;
    }

    /* 🏆 勝利結局卡片 */
    .achievement-card {
        background: #FFF9C4;
        border: 4px solid #FBC02D;
        border-radius: 20px;
        padding: 20px;
        margin: 15px 0;
        text-align: center;
        box-shadow: 6px 6px 0px #000000;
    }

    .story-title { font-size: 1.5rem !important; color: #D81B60 !important; font-weight: 900; margin-bottom: 5px; }
    .story-progress { font-size: 0.9rem !important; color: #00838F !important; font-weight: bold; background: #E0F7FA; padding: 4px 12px; border-radius: 10px; display: inline-block; margin-bottom: 10px; }
    .story-sfx { font-size: 1.2rem !important; color: #FF9800 !important; font-weight: 900; margin-bottom: 10px; }
    .story-text-tc { font-size: 1.3rem !important; line-height: 1.6; font-weight: bold; color: #000000 !important; }
    .story-text-en { font-size: 1.1rem !important; line-height: 1.5; font-weight: 600; color: #424242 !important; margin-top: 8px; }

    /* 按鈕置中與樣式 */
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
    
    [data-testid="stSidebar"] { background-color: #1E293B !important; }
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span { color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# ----------------- 標題與簡介 -----------------
st.markdown('<p class="kids-title">🦸‍♂️ 火鷹俠全人教育故事館 🚀</p>', unsafe_allow_html=True)
st.markdown('<p class="en-title">Firebird Protection: Whole-Person Interactive Hub</p>', unsafe_allow_html=True)
st.caption("Son & Dad Exclusive | 條件分支 × 挫折學習 × 多重結局")
st.markdown("---")

# ----------------- ⚙️ 初始化狀態機 (State Machine) -----------------
def reset_game():
    st.session_state.current_scene = "1_START"
    st.session_state.stats = {"bravery": 0, "creativity": 0, "empathy": 0}
    st.session_state.history = []  # 歷史記錄，用於時空回溯 (Undo)

if "stats" not in st.session_state:
    st.session_state.stats = {"bravery": 0, "creativity": 0, "empathy": 0}

if "history" not in st.session_state:
    st.session_state.history = []

# ----------------- ⚙️ 側邊欄：故事選擇與面板 -----------------
st.sidebar.markdown("## 📚 選擇冒險故事")
story_choice = st.sidebar.radio(
    "小隊長，你想玩邊個故事？", 
    ["Story1", "Story2", "Story3"],
    format_func=lambda x: STORIES[x]["name_tc"]
)

if "current_story" not in st.session_state or st.session_state.current_story != story_choice:
    st.session_state.current_story = story_choice
    reset_game()

if "current_scene" not in st.session_state:
    reset_game()

current_story_nodes = STORIES[st.session_state.current_story]["nodes"]
scene_key = st.session_state.current_scene

if scene_key not in current_story_nodes:
    reset_game()
    scene_key = "1_START"

scene = current_story_nodes[scene_key]

# 顯示小隊長屬性面板
st.sidebar.markdown("---")
st.sidebar.markdown("### ⭐ 小隊長能力徽章")
st.sidebar.markdown(f"🦁 **勇氣堅毅 (Bravery)**: {'⭐' * st.session_state.stats['bravery']}")
st.sidebar.markdown(f"💡 **STEAM 創意 (Creativity)**: {'⭐' * st.session_state.stats['creativity']}")
st.sidebar.markdown(f"❤️ **同理愛心 (Empathy)**: {'⭐' * st.session_state.stats['empathy']}")

# ----------------- 📖 判斷場景類型 (壞結局 / 勝利結局 / 普通場景) -----------------
is_bad_ending = scene.get("is_bad_ending", False)
is_victory_ending = scene_key.startswith("6_") or scene.get("is_victory", False)

# 卡片渲染
card_class = "bad-card" if is_bad_ending else "story-card"
st.markdown(f'''
    <div class="{card_class}">
        <span class="story-progress">📌 冒險進度：{scene.get("progress_tag", "進行中")}</span>
        <div class="story-title">📖 {scene.get("title_tc", "")} ({scene.get("title_en", "")})</div>
        <div class="story-sfx">{scene.get("sfx", "")}</div>
        <div class="story-text-tc">{scene.get("story_tc", "")}</div>
        <div class="story-text-en">{scene.get("story_en", "")}</div>
    </div>
''', unsafe_allow_html=True)

# 顯示插圖
if "images" in scene and scene["images"]:
    cols = st.columns(len(scene["images"]))
    for idx, img_url in enumerate(scene["images"]):
        with cols[idx]:
            try:
                st.image(img_url, use_container_width=True)
            except Exception:
                st.image("https://via.placeholder.com/800x500?text=🎨+火鷹俠+想像力+繪本", use_container_width=True)

st.markdown("---")

# ----------------- 🔀 邏輯 A：壞結局 (Bad Ending) 處理 -----------------
if is_bad_ending:
    st.error("💡【火鷹俠的成長型思維課】：失敗不可怕！重點係我哋從中學到咩，然後再試一次！")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("↩️ 穿越時空！返回上一頁重新選擇！"):
            if st.session_state.history:
                st.session_state.current_scene = st.session_state.history.pop()
            else:
                st.session_state.current_scene = "1_START"
            st.rerun()
    with col2:
        if st.button("🔄 重新開始成個故事"):
            reset_game()
            st.rerun()

# ----------------- 🏆 邏輯 B：勝利結局 (Victory Ending) 處理 -----------------
elif is_victory_ending:
    st.balloons()
    
    b_pts = st.session_state.stats["bravery"]
    c_pts = st.session_state.stats["creativity"]
    e_pts = st.session_state.stats["empathy"]

    if b_pts >= c_pts and b_pts >= e_pts:
        title_tc = "🦁 勇敢堅毅的冒險領袖 (Courageous Leader)"
        desc_tc = "你在冒險中展現了無畏的勇氣與 Perseverance（堅毅）！面對任何困難都一往無前！"
    elif c_pts >= b_pts and c_pts >= e_pts:
        title_tc = "💡 創意無限的 STEAM 小發明家 (STEAM Inventor)"
        desc_tc = "你非常擅長靈活運用科學、邏輯與創造力去解開謎題！是真正的智慧擔當！"
    else:
        title_tc = "❤️ 充滿同理心的愛心守護者 (Caring Guardian)"
        desc_tc = "你總是能體貼別人的感受（Empathy），用包容與尊重（Respect）化解危機！"

    st.markdown(f'''
        <div class="achievement-card">
            <h2>🏆 榮譽認證：小隊長全人成就頒發 🏆</h2>
            <h3>{title_tc}</h3>
            <p style="font-size: 1.2rem; font-weight: bold;">{desc_tc}</p>
            <p>累積徽章：🦁 勇氣 x{b_pts} | 💡 創意 x{c_pts} | ❤️ 同理心 x{e_pts}</p>
        </div>
    ''', unsafe_allow_html=True)

    if st.button("🔄 挑戰其他路線與故事 (Play Again)"):
        reset_game()
        st.rerun()

# ----------------- 🎯 邏輯 C：普通故事選擇 -----------------
else:
    st.markdown("### 🎯 小隊長，下一步你要點做？ (What will you do next?)")
    choices = scene.get("choices", {})

    for opt_key, opt_data in choices.items():
        # 條件判斷 (Condition Check)
        is_locked = False
        req_stat = opt_data.get("requires", None)
        if req_stat:
            stat_name, req_val = req_stat
            if st.session_state.stats.get(stat_name, 0) < req_val:
                is_locked = True

        btn_label = f"👉 選項 {opt_key}: {opt_data['text']}"
        if is_locked:
            btn_label = f"🔒 [條件不足] 選項 {opt_key}: {opt_data['text']} (需 {stat_name} ≥ {req_val})"

        if st.button(btn_label, disabled=is_locked, key=f"btn_{scene_key}_{opt_key}"):
            # 1. 記錄歷史，供回溯 (Undo)
            st.session_state.history.append(scene_key)

            # 2. 增加屬性點數 (Effect)
            effects = opt_data.get("effect", {})
            for k, v in effects.items():
                st.session_state.stats[k] = st.session_state.stats.get(k, 0) + v

            # 3. 切換至下個場景
            st.session_state.current_scene = opt_data["next"]
            st.rerun()

# 側邊欄重置按鈕
st.sidebar.markdown("---")
if st.sidebar.button("🔄 返回故事第一頁"):
    reset_game()
    st.rerun()
