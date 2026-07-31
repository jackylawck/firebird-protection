import streamlit as st
from story_data import STORIES, get_ending_key

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
    .story-sfx { font-size: 1.2rem !important; color: #FF9800 !important; font-weight: 900; margin-bottom: 10px; }
    .story-text-tc { font-size: 1.3rem !important; line-height: 1.6; font-weight: bold; color: #000000 !important; }
    .story-text-en { font-size: 1.1rem !important; line-height: 1.5; font-weight: 600; color: #424242 !important; margin-top: 8px; }

    /* 按鈕樣式 */
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
st.markdown('<p class="en-title">Firebird Protection: Interactive Branching Stories</p>', unsafe_allow_html=True)
st.caption("Son & Dad Exclusive | 狀態機敘事 × 挫折學習 × 多重結局")
st.markdown("---")

# ----------------- ⚙️ 初始化遊戲引擎 -----------------
def reset_game():
    st.session_state.current_scene = "1_START"
    st.session_state.stats = {"bravery": 0, "creativity": 0, "empathy": 0}
    st.session_state.history = []
    st.session_state.history_stats = []

if "stats" not in st.session_state:
    st.session_state.stats = {"bravery": 0, "creativity": 0, "empathy": 0}
if "history" not in st.session_state:
    st.session_state.history = []
if "history_stats" not in st.session_state:
    st.session_state.history_stats = []

# ----------------- 📚 側邊欄：故事選擇與能力面板 -----------------
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

st.sidebar.markdown("---")
st.sidebar.markdown("### ⭐ 小隊長能力徽章")
st.sidebar.markdown(f"🦁 **勇氣堅毅**: {'⭐' * st.session_state.stats['bravery']}")
st.sidebar.markdown(f"💡 **STEAM 創意**: {'⭐' * st.session_state.stats['creativity']}")
st.sidebar.markdown(f"❤️ **同理愛心**: {'⭐' * st.session_state.stats['empathy']}")

# ----------------- 📖 渲染場景 -----------------
is_bad_ending = scene.get("is_bad_ending", False)

if is_bad_ending:
    # 💥 壞結局渲染
    st.error("💡【火鷹俠的成長型思維課】：失敗不可怕！重點係我哋從中學到咩，然後再試一次！")
    st.markdown(f'''
        <div class="bad-card">
            <div class="story-title">📖 {scene.get("title_tc", "")} ({scene.get("title_en", "")})</div>
            <div class="story-sfx">{scene.get("sfx", "")}</div>
            <div class="story-text-tc">{scene.get("story_tc", "")}</div>
            <div class="story-text-en">{scene.get("story_en", "")}</div>
        </div>
    ''', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("↩️ 穿越時空！返回上一頁重新選擇！"):
            if st.session_state.history:
                st.session_state.current_scene = st.session_state.history.pop()
                st.session_state.stats = st.session_state.history_stats.pop()
            else:
                reset_game()
            st.rerun()
    with col2:
        if st.button("🔄 重新開始成個故事"):
            reset_game()
            st.rerun()

elif scene_key.startswith("6_"):
    # 🏆 勝利結局渲染
    st.balloons()
    ending_data = {
        "6_LEADER": ("🏆 結局：全人小領袖", "兼具勇氣與關懷，你是天生的全人小領袖！"),
        "6_HERO": ("⚔️ 結局：勇氣英雄", "你用無懼的勇氣擊敗了強敵，成為全城小朋友的英雄！"),
        "6_INVENTOR": ("🎨 結局：創意發明家", "你用科技與創意解決問題，是聰明的 STEAM 發明家！"),
        "6_CARER": ("❤️ 結局：關懷天使", "你用溫柔與關懷融化了對手，守護了和平！"),
        "6_BRAVE": ("💪 結局：純粹勇者", "你證明了堅持到底的力量，勇氣可嘉！"),
        "6_CREATIVE": ("🎯 結局：創意大師", "你用無限創意改變了遊戲規則，聰明絕頂！"),
        "6_EMPATHY": ("🫂 結局：同理心大師", "你用同理心理解了對手，化敵為友！"),
        "6_DEFAULT": ("😐 結局：平凡的冒險", "你成功完成了任務，下次試試其他選擇，或許會有驚喜！")
    }
    
    title_tc, desc_tc = ending_data.get(scene_key, ending_data["6_DEFAULT"])
    
    st.markdown(f'''
        <div class="achievement-card">
            <h2>🏆 榮譽認證：小隊長成就頒發 🏆</h2>
            <h3>{title_tc}</h3>
            <p style="font-size: 1.2rem; font-weight: bold;">{desc_tc}</p>
            <p>累積徽章：🦁 勇氣 x{st.session_state.stats['bravery']} | 💡 創意 x{st.session_state.stats['creativity']} | ❤️ 同理心 x{st.session_state.stats['empathy']}</p>
        </div>
    ''', unsafe_allow_html=True)
    
    if st.button("🔄 挑戰其他路線與故事 (Play Again)"):
        reset_game()
        st.rerun()

else:
    # 🎯 普通場景渲染
    st.markdown(f'''
        <div class="story-card">
            <div class="story-title">📖 {scene.get("title_tc", "")} ({scene.get("title_en", "")})</div>
            <div class="story-sfx">{scene.get("sfx", "")}</div>
            <div class="story-text-tc">{scene.get("story_tc", "")}</div>
            <div class="story-text-en">{scene.get("story_en", "")}</div>
        </div>
    ''', unsafe_allow_html=True)
    
    if "images" in scene and scene["images"]:
        cols = st.columns(len(scene["images"]))
        for idx, img_url in enumerate(scene["images"]):
            with cols[idx]:
                try:
                    st.image(img_url, use_container_width=True)
                except Exception:
                    st.image("https://via.placeholder.com/800x500?text=🎨+火鷹俠+繪本", use_container_width=True)

    st.markdown("---")
    st.markdown("### 🎯 小隊長，下一步你要點做？ (What will you do next?)")
    
    choices = scene.get("choices", {})
    if choices:
        for opt_key, opt_data in choices.items():
            if st.button(f"👉 選項 {opt_key}: {opt_data['text']}"):
                
                # 記錄回溯數據 (Undo data)
                st.session_state.history.append(scene_key)
                st.session_state.history_stats.append(st.session_state.stats.copy())
                
                # 屬性增減
                if "effect" in opt_data:
                    for k, v in opt_data["effect"].items():
                        st.session_state.stats[k] = max(0, st.session_state.stats[k] + v)
                
                # 決定下一頁 (若進入第五頁決戰，則自動推算最終結局)
                if opt_data["next"].startswith("6_"):
                    st.session_state.current_scene = get_ending_key(st.session_state.stats)
                else:
                    st.session_state.current_scene = opt_data["next"]
                
                # 若選項帶有壞結局屬性，直接覆蓋原因並跳轉
                if opt_data.get("is_bad", False):
                    st.session_state.current_scene = opt_data["next"]
                    if st.session_state.current_scene in current_story_nodes:
                        current_story_nodes[st.session_state.current_scene]["story_tc"] = opt_data.get("bad_reason", "發生了意外！")

                st.rerun()

st.sidebar.markdown("---")
if st.sidebar.button("🔄 返回故事第一頁"):
    reset_game()
    st.rerun()
