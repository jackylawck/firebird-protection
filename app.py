import streamlit as st
import streamlit.components.v1 as components
from story_data import STORIES, get_ending_key

# ----------------- 1. 頁面基礎配置 -----------------
st.set_page_config(
    page_title="火鷹俠全人教育故事館",
    page_icon="🦸‍♂️",
    layout="centered"
)

# ----------------- 2. 🎨 WhatsApp 網址分享預覽卡片 (Open Graph) 與 UI CSS -----------------
st.markdown("""
    <!-- WhatsApp / Social Media Share Meta Tags -->
    <head>
        <meta property="og:title" content="🦸‍♂️ 火鷹俠全人教育故事館" />
        <meta property="og:description" content="Son & Dad Exclusive | 雙語繪本 × 成長型思維 × STEAM 互動冒險" />
        <meta property="og:type" content="website" />
    </head>

    <style>
    .stApp { background-color: #E0F7FA; color: #000000 !important; }
    p, span, label, div, h1, h2, h3, h4 { color: #000000 !important; font-family: 'Comic Sans MS', sans-serif; }
    
    .kids-title { font-size: clamp(1.5rem, 4vw, 2rem) !important; color: #00838F !important; font-weight: 900; text-align: center; margin-bottom: 2px; }
    .en-title { font-size: clamp(0.9rem, 2.5vw, 1.1rem) !important; color: #006064 !important; font-weight: 900; text-align: center; margin-bottom: 8px; }
    
    /* 上格：故事獨立滾動區域 */
    .story-scroll-box {
        max-height: 48vh;
        overflow-y: auto;
        background: #FFFFFF;
        border: 4px solid #000000;
        border-radius: 20px;
        padding: 16px;
        margin-bottom: 10px;
        box-shadow: 6px 6px 0px #000000;
        -webkit-overflow-scrolling: touch;
    }
    
    .bad-scroll-box {
        max-height: 48vh;
        overflow-y: auto;
        background: #FFEBEE;
        border: 4px solid #D32F2F;
        border-radius: 20px;
        padding: 16px;
        margin-bottom: 10px;
        box-shadow: 6px 6px 0px #D32F2F;
        -webkit-overflow-scrolling: touch;
    }

    .story-title { font-size: 1.3rem !important; color: #D81B60 !important; font-weight: 900; margin-bottom: 5px; }
    .story-progress { font-size: 0.8rem !important; color: #00838F !important; font-weight: bold; background: #E0F7FA; padding: 2px 8px; border-radius: 8px; display: inline-block; margin-bottom: 6px; }
    .story-sfx { font-size: 1rem !important; color: #FF9800 !important; font-weight: 900; margin-bottom: 6px; }
    .story-text-tc { font-size: 1.25rem !important; line-height: 1.5; font-weight: bold; color: #000000 !important; }
    .story-text-en { font-size: 1rem !important; line-height: 1.4; font-weight: 600; color: #424242 !important; margin-top: 6px; }
    .bad-reason-text { font-size: 1.05rem !important; font-weight: bold; color: #D32F2F !important; margin-top: 10px; padding: 8px; border-left: 4px solid #D32F2F; background: #FFCDD2; line-height: 1.4;}

    /* 下格：選擇按鈕區域 */
    div.stButton { display: flex; justify-content: center; }
    div.stButton > button { 
        background-color: #FFEB3B !important; 
        color: #000000 !important; 
        font-size: 1.1rem !important; 
        font-weight: 900 !important; 
        border: 3.5px solid #000000 !important; 
        border-radius: 14px !important; 
        padding: 8px 14px !important; 
        box-shadow: 3px 3px 0px #000000 !important; 
        width: 100% !important; 
        max-width: 650px !important; 
        margin-bottom: 8px !important; 
        white-space: pre-wrap; 
    }
    div.stButton > button:hover { background-color: #FFD600 !important; }
    
    [data-testid="stSidebar"] { background-color: #1E293B !important; }
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span { color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# ----------------- 3. ⚙️ 初始化遊戲引擎 -----------------
def reset_game():
    st.session_state.current_scene = "1_START"
    st.session_state.stats = {"bravery": 0, "creativity": 0, "empathy": 0}
    st.session_state.history = []
    st.session_state.history_stats = []
    st.session_state.bad_reason = ""

if "stats" not in st.session_state:
    st.session_state.stats = {"bravery": 0, "creativity": 0, "empathy": 0}
if "history" not in st.session_state:
    st.session_state.history = []
if "history_stats" not in st.session_state:
    st.session_state.history_stats = []
if "bad_reason" not in st.session_state:
    st.session_state.bad_reason = ""
if "unlocked_endings" not in st.session_state:
    st.session_state.unlocked_endings = set()

# ----------------- 4. 📚 側邊欄：故事選擇與能力面板 -----------------
st.sidebar.markdown("## 📚 選擇冒險故事\n*(Choose a Story)*")
story_choice = st.sidebar.radio(
    "小隊長，你想玩哪個故事？ (Captain, which story do you want to play?)", 
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
st.sidebar.markdown("### ⭐ 小隊長能力徽章\n*(Captain's Badges)*")
st.sidebar.markdown(f"🦁 **勇氣堅毅**: {'⭐' * st.session_state.stats['bravery']}")
st.sidebar.markdown(f"💡 **STEAM 創意**: {'⭐' * st.session_state.stats['creativity']}")
st.sidebar.markdown(f"❤️ **同理愛心**: {'⭐' * st.session_state.stats['empathy']}")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏆 成就圖鑑\n*(Unlocked Endings)*")
if len(st.session_state.unlocked_endings) == 0:
    st.sidebar.caption("尚未解鎖任何結局！\n(No endings unlocked yet!)")
else:
    for ending in st.session_state.unlocked_endings:
        st.sidebar.markdown(f"✅ {ending}")

# 計算頁數進度
try:
    current_page = int(scene_key.split('_')[0])
    progress_text = f"第 {current_page} 頁 (Page {current_page})"
except:
    progress_text = "特殊進度"

# ----------------- 5. 🔝 標題 -----------------
st.markdown('<p class="kids-title">🦸‍♂️ 火鷹俠故事館 🚀</p>', unsafe_allow_html=True)
st.markdown('<p class="en-title">Firebird Protection: Interactive Hub</p>', unsafe_allow_html=True)

# ----------------- 6. 📦 上格：獨立滾動劇情容器 -----------------
is_bad_ending = scene.get("is_bad_ending", False)

if is_bad_ending:
    st.error("💡【成長型思維】：失敗不可怕，讓我們再試一次！\n*(Failure is just a chance to learn!)*")
    st.markdown(f'''
        <div class="bad-scroll-box" id="story-box">
            <span class="story-progress">📌 冒險進度：💥 遇到挫折 (Setback)</span>
            <div class="story-title">📖 {scene.get("title_tc", "")} ({scene.get("title_en", "")})</div>
            <div class="story-sfx">{scene.get("sfx", "")}</div>
            <div class="story-text-tc">{scene.get("story_tc", "")}</div>
            <div class="story-text-en">{scene.get("story_en", "")}</div>
            <div class="bad-reason-text">💥 發生了什麼事：<br>{st.session_state.bad_reason}</div>
        </div>
    ''', unsafe_allow_html=True)
elif scene_key.startswith("6_"):
    st.balloons()
    ending_data = {
        "6_LEADER": ("🏆 結局：全人小領袖", "兼具勇氣與關懷，你是天生的全人小領袖！"),
        "6_HERO": ("⚔️ 結局：勇氣英雄", "你用無懼的勇氣擊敗了強敵，成為英雄！"),
        "6_INVENTOR": ("🎨 結局：創意發明家", "你運用科技與創意解決問題，是聰明的發明家！"),
        "6_CARER": ("❤️ 結局：關懷天使", "你用溫柔與關懷融化了對手，守護了和平！"),
        "6_BRAVE": ("💪 結局：純粹勇者", "你證明了堅持到底的力量，勇氣可嘉！"),
        "6_CREATIVE": ("🎯 結局：創意大師", "你運用無限創意改變了規則，聰明絕頂！"),
        "6_EMPATHY": ("🫂 結局：同理心大師", "你用同理心理解了對手，化敵為友！"),
        "6_DEFAULT": ("😐 結局：平凡的冒險", "你成功完成了任務，下次試試其他選擇！")
    }
    title_tc, desc_tc = ending_data.get(scene_key, ending_data["6_DEFAULT"])
    st.session_state.unlocked_endings.add(title_tc.split("：")[1])
    
    st.markdown(f'''
        <div class="story-scroll-box" id="story-box">
            <h2>🏆 榮譽認證：成就頒發 🏆</h2>
            <h3>{title_tc}</h3>
            <p style="font-size: 1.1rem; font-weight: bold;">{desc_tc}</p>
        </div>
    ''', unsafe_allow_html=True)
else:
    # 標準劇情盒子
    st.markdown(f'''
        <div class="story-scroll-box" id="story-box">
            <span class="story-progress">📌 {progress_text}</span>
            <div class="story-title">📖 {scene.get("title_tc", "")} ({scene.get("title_en", "")})</div>
            <div class="story-sfx">{scene.get("sfx", "")}</div>
            <div class="story-text-tc">{scene.get("story_tc", "")}</div>
            <div class="story-text-en">{scene.get("story_en", "")}</div>
        </div>
    ''', unsafe_allow_html=True)

# 🎯 強制歸頂 JavaScript：每次切換頁面時，將「故事盒子」與「整個手機頁面」同時捲動回最頂部
components.html("""
    <script>
        const storyBox = window.parent.document.getElementById('story-box');
        if (storyBox) {
            storyBox.scrollTop = 0;
        }
        window.parent.scrollTo(0, 0);
    </script>
""", height=0)

# ----------------- 7. 📦 下格：選擇按鈕區域 -----------------
if is_bad_ending:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("↩️ 返回上一頁重新選擇\n(Go back and choose again)"):
            if st.session_state.history:
                st.session_state.current_scene = st.session_state.history.pop()
                st.session_state.stats = st.session_state.history_stats.pop() 
            else:
                reset_game()
            st.rerun()
    with col2:
        if st.button("🔄 重新開始故事\n(Restart Story)"):
            reset_game()
            st.rerun()

elif scene_key.startswith("6_"):
    if st.button("🔄 挑戰其他路線與故事 (Play Again)"):
        reset_game()
        st.rerun()

else:
    choices = scene.get("choices", {})
    if choices:
        choices_items = list(choices.items())
        for idx, (opt_key, opt_data) in enumerate(choices_items):
            letter = chr(ord('A') + idx)
            
            if st.button(f"👉 選項 {letter}: \n{opt_data['text']}", key=f"btn_{scene_key}_{idx}"):
                st.session_state.history.append(scene_key)
                st.session_state.history_stats.append(st.session_state.stats.copy())
                
                if "effect" in opt_data:
                    for k, v in opt_data["effect"].items():
                        st.session_state.stats[k] = max(0, st.session_state.stats[k] + v)
                
                if opt_data.get("is_bad", False):
                    st.session_state.bad_reason = opt_data.get("bad_reason", "你的選擇帶來了意外後果！")
                    st.session_state.current_scene = opt_data["next"]
                else:
                    if opt_data["next"].startswith("6_"):
                        st.session_state.current_scene = get_ending_key(st.session_state.stats)
                    else:
                        st.session_state.current_scene = opt_data["next"]
                
                st.rerun()

st.sidebar.markdown("---")
if st.sidebar.button("🔄 返回故事第一頁 (Back to Page 1)"):
    reset_game()
    st.rerun()
