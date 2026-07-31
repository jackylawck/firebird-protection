import streamlit as st
from story_data import STORIES, get_ending_key

# ----------------- 頁面基礎配置 -----------------
st.set_page_config(
    page_title="火鷹俠故事館 | Firebird Protection",
    page_icon="🦸‍♂️",
    layout="centered"
)

# ----------------- 🎨 兒童友善與漫畫風格 CSS -----------------
st.markdown("""
    <style>
    .stApp { background-color: #E0F7FA; color: #000000 !important; }
    p, span, label, div, h1, h2, h3, h4 { color: #000000 !important; font-family: 'Comic Sans MS', sans-serif; }
    .kids-title { font-size: clamp(1.8rem, 5vw, 2.5rem) !important; color: #00838F !important; font-weight: 900; text-align: center; margin-bottom: 5px; }
    .en-title { font-size: clamp(1rem, 3vw, 1.4rem) !important; color: #006064 !important; font-weight: 900; text-align: center; margin-bottom: 15px; }
    
    .story-card { background: #FFFFFF; border: 4px solid #000000; border-radius: 20px; padding: 20px; margin: 15px 0; box-shadow: 6px 6px 0px #000000; }
    .bad-card { background: #FFEBEE; border: 4px solid #D32F2F; border-radius: 20px; padding: 20px; margin: 15px 0; box-shadow: 6px 6px 0px #D32F2F; }
    .achievement-card { background: #FFF9C4; border: 4px solid #FBC02D; border-radius: 20px; padding: 20px; margin: 15px 0; text-align: center; box-shadow: 6px 6px 0px #000000; }

    .story-title { font-size: 1.5rem !important; color: #D81B60 !important; font-weight: 900; margin-bottom: 5px; }
    .story-progress { font-size: 0.9rem !important; color: #00838F !important; font-weight: bold; background: #E0F7FA; padding: 4px 12px; border-radius: 10px; display: inline-block; margin-bottom: 10px; }
    .story-sfx { font-size: 1.2rem !important; color: #FF9800 !important; font-weight: 900; margin-bottom: 10px; }
    .story-text-tc { font-size: 1.3rem !important; line-height: 1.6; font-weight: bold; color: #000000 !important; }
    .story-text-en { font-size: 1.1rem !important; line-height: 1.5; font-weight: 600; color: #424242 !important; margin-top: 8px; }
    .bad-reason-text { font-size: 1.2rem !important; font-weight: bold; color: #D32F2F !important; margin-top: 15px; padding: 10px; border-left: 5px solid #D32F2F; background: #FFCDD2; line-height: 1.5;}

    div.stButton { display: flex; justify-content: center; }
    div.stButton > button { background-color: #FFEB3B !important; color: #000000 !important; font-size: 1.2rem !important; font-weight: 900 !important; border: 4px solid #000000 !important; border-radius: 16px !important; padding: 12px 20px !important; box-shadow: 4px 4px 0px #000000 !important; width: 100% !important; max-width: 650px !important; margin-bottom: 12px !important; white-space: pre-wrap; }
    div.stButton > button:hover { background-color: #FFD600 !important; }
    
    [data-testid="stSidebar"] { background-color: #1E293B !important; }
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span { color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# ----------------- 標題 -----------------
st.markdown('<p class="kids-title">🦸‍♂️ 火鷹俠全人教育故事館 🚀</p>', unsafe_allow_html=True)
st.markdown('<p class="en-title">Firebird Protection: Interactive Branching Stories</p>', unsafe_allow_html=True)
st.caption("Son & Dad Exclusive | 雙語並行學習 × 狀態機敘事 × 挫折學習")
st.markdown("---")

# ----------------- ⚙️ 初始化遊戲引擎 -----------------
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

# ----------------- 📚 側邊欄：故事選擇與能力面板 -----------------
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
st.sidebar.markdown(f"🦁 **勇氣堅毅 (Bravery)**: {'⭐' * st.session_state.stats['bravery']}")
st.sidebar.markdown(f"💡 **STEAM 創意 (Creativity)**: {'⭐' * st.session_state.stats['creativity']}")
st.sidebar.markdown(f"❤️ **同理愛心 (Empathy)**: {'⭐' * st.session_state.stats['empathy']}")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏆 成就圖鑑\n*(Unlocked Endings)*")
if len(st.session_state.unlocked_endings) == 0:
    st.sidebar.caption("尚未解鎖任何結局，繼續努力！\n(No endings unlocked yet, keep going!)")
else:
    for ending in st.session_state.unlocked_endings:
        st.sidebar.markdown(f"✅ {ending}")

# 計算頁數與進度
total_nodes = len([k for k in current_story_nodes.keys() if not k.startswith("BAD_") and not k.startswith("6_")])
try:
    current_page = int(scene_key.split('_')[0])
    progress_text = f"第 {current_page} 頁 (Page {current_page})"
except:
    progress_text = "特殊進度 (Special Event)"

# ----------------- 📖 渲染場景 -----------------
is_bad_ending = scene.get("is_bad_ending", False)

if is_bad_ending:
    # 💥 壞結局渲染 (雙語提示)
    st.error("💡【火鷹俠的成長型思維課】：失敗不可怕！最重要是我們從中學到什麼，然後再試一次！\n*(Growth Mindset: Failure is just a chance to learn. Let's try again!)*")
    st.markdown(f'''
        <div class="bad-card">
            <span class="story-progress">📌 冒險進度：💥 遇到挫折 (Setback)</span>
            <div class="story-title">📖 {scene.get("title_tc", "")} ({scene.get("title_en", "")})</div>
            <div class="story-sfx">{scene.get("sfx", "")}</div>
            <div class="story-text-tc">{scene.get("story_tc", "")}</div>
            <div class="story-text-en">{scene.get("story_en", "")}</div>
            <div class="bad-reason-text">💥 發生了什麼事 (What Happened)：<br>{st.session_state.bad_reason}</div>
        </div>
    ''', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("↩️ 穿越時空！返回上一頁重新選擇！\n(Time Travel! Go back and choose again!)"):
            if st.session_state.history:
                st.session_state.current_scene = st.session_state.history.pop()
                st.session_state.stats = st.session_state.history_stats.pop() 
            else:
                reset_game()
            st.rerun()
    with col2:
        if st.button("🔄 重新開始整個故事\n(Restart Story)"):
            reset_game()
            st.rerun()

elif scene_key.startswith("6_"):
    # 🏆 勝利結局渲染 (雙語成就卡)
    st.balloons()
    ending_data = {
        "6_LEADER": ("🏆 結局：全人小領袖 (Whole-Person Leader)", "兼具勇氣與關懷，你是天生的全人小領袖！<br>(With courage and care, you are a born Whole-Person Leader!)"),
        "6_HERO": ("⚔️ 結局：勇氣英雄 (Courage Hero)", "你用無懼的勇氣擊敗了強敵，成為全城小朋友的英雄！<br>(You defeated the enemy with bravery, becoming a hero!)"),
        "6_INVENTOR": ("🎨 結局：創意發明家 (Creative Inventor)", "你運用科技與創意解決問題，是聰明的 STEAM 發明家！<br>(You used tech and creativity to solve problems like a STEAM inventor!)"),
        "6_CARER": ("❤️ 結局：關懷天使 (Caring Angel)", "你用溫柔與關懷融化了對手，守護了和平！<br>(You melted the opponent with warmth and care, guarding the peace!)"),
        "6_BRAVE": ("💪 結局：純粹勇者 (Pure Bravery)", "你證明了堅持到底的力量，勇氣可嘉！<br>(You proved the power of perseverance, excellent bravery!)"),
        "6_CREATIVE": ("🎯 結局：創意大師 (Master of Creativity)", "你運用無限創意改變了遊戲規則，聰明絕頂！<br>(You changed the rules with infinite creativity, brilliant!)"),
        "6_EMPATHY": ("🫂 結局：同理心大師 (Master of Empathy)", "你用同理心理解了對手，化敵為友！<br>(You understood the opponent with empathy, turning foes into friends!)"),
        "6_DEFAULT": ("😐 結局：平凡的冒險 (Ordinary Adventure)", "你成功完成了任務，下次試試其他選擇，或許會有驚喜！<br>(You completed the mission. Try different choices next time!)")
    }
    
    title_tc, desc_tc = ending_data.get(scene_key, ending_data["6_DEFAULT"])
    
    # 加入解鎖清單 (只取中文名稱作顯示)
    st.session_state.unlocked_endings.add(title_tc.split("：")[1].split(" (")[0])
    
    st.markdown(f'''
        <div class="achievement-card">
            <h2>🏆 榮譽認證：小隊長成就頒發 🏆</h2>
            <h3>{title_tc}</h3>
            <p style="font-size: 1.1rem; font-weight: bold;">{desc_tc}</p>
            <p style="color: #555;">累積徽章 (Badges Earned)：<br>🦁 勇氣 (Bravery) x{st.session_state.stats['bravery']} | 💡 創意 (Creativity) x{st.session_state.stats['creativity']} | ❤️ 同理心 (Empathy) x{st.session_state.stats['empathy']}</p>
        </div>
    ''', unsafe_allow_html=True)
    
    if st.button("🔄 挑戰其他路線與故事\n(Play Again)"):
        reset_game()
        st.rerun()

else:
    # 🎯 普通場景渲染
    st.markdown(f'''
        <div class="story-card">
            <span class="story-progress">📌 冒險進度 (Progress)：{progress_text}</span>
            <div class="story-title">📖 {scene.get("title_tc", "")} ({scene.get("title_en", "")})</div>
            <div class="story-sfx">{scene.get("sfx", "")}</div>
            <div class="story-text-tc">{scene.get("story_tc", "")}</div>
            <div class="story-text-en">{scene.get("story_en", "")}</div>
        </div>
    ''', unsafe_allow_html=True)
    
    # 圖片渲染與容錯機制
    if "images" in scene and scene["images"]:
        cols = st.columns(len(scene["images"]))
        for idx, img_url in enumerate(scene["images"]):
            with cols[idx]:
                try:
                    st.image(img_url, use_container_width=True)
                except Exception:
                    st.markdown("🖼️ *(火鷹俠正在想像這個精彩畫面... Firebird is imagining this scene...)*")

    st.markdown("---")
    st.markdown("### 🎯 小隊長，下一步你要怎麼做？\n*(What will you do next?)*")
    
    choices = scene.get("choices", {})
    if choices:
        choices_items = list(choices.items())
        for idx, (opt_key, opt_data) in enumerate(choices_items):
            letter = chr(ord('A') + idx) # A, B, C...
            
            # 按鈕文字支援多行 (中文 \n 英文)
            if st.button(f"👉 選項 {letter}: \n{opt_data['text']}"):
                
                # 保存記錄
                st.session_state.history.append(scene_key)
                st.session_state.history_stats.append(st.session_state.stats.copy())
                
                # 累加新效果
                if "effect" in opt_data:
                    for k, v in opt_data["effect"].items():
                        st.session_state.stats[k] = max(0, st.session_state.stats[k] + v)
                
                # 處理跳轉與壞結局原因
                if opt_data.get("is_bad", False):
                    st.session_state.bad_reason = opt_data.get("bad_reason", "你的選擇帶來了意外後果！(Unexpected consequences!)")
                    st.session_state.current_scene = opt_data["next"]
                else:
                    if opt_data["next"].startswith("6_"):
                        st.session_state.current_scene = get_ending_key(st.session_state.stats)
                    else:
                        st.session_state.current_scene = opt_data["next"]
                
                st.rerun()

st.sidebar.markdown("---")
if st.sidebar.button("🔄 返回故事第一頁\n(Back to Page 1)"):
    reset_game()
    st.rerun()
