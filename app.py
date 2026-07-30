import streamlit as st
from story_data import STORIES

# 頁面配置
st.set_page_config(
    page_title="火鷹俠故事庫 | Firebird Protection",
    page_icon="🦸‍♂️",
    layout="centered"
)

# 🎨 雙語超大字體 CSS
st.markdown("""
    <style>
    .stApp { background-color: #E0F7FA; color: #000000 !important; }
    p, span, label, div, h1, h2, h3, h4 { color: #000000 !important; font-family: 'Comic Sans MS', sans-serif; }
    .kids-title { font-size: 2.6rem !important; color: #00838F !important; font-weight: 900; text-align: center; margin-bottom: 5px; text-shadow: 2px 2px 0px #B2EBF2; }
    .en-title { font-size: 1.8rem !important; color: #006064 !important; font-weight: 900; text-align: center; margin-bottom: 15px; }
    .kids-sfx { font-size: 2rem !important; color: #E65100 !important; font-weight: 900; text-align: center; margin: 10px 0; }
    .kids-speech-bubble { background: #FFFFFF; border: 5px solid #000000; border-radius: 25px; padding: 25px; margin: 15px 0; box-shadow: 8px 8px 0px #000000; }
    .tc-story { font-size: 1.6rem !important; line-height: 1.6; font-weight: bold; margin-bottom: 15px; }
    .en-story { font-size: 1.3rem !important; line-height: 1.5; color: #37474F !important; font-style: italic; }
    
    [data-testid="stSidebar"] { background-color: #1E293B !important; }
    [data-testid="stSidebar"] h2 { color: #FFEB3B !important; font-size: 1.5rem !important; }
    [data-testid="stSidebar"] label p { color: #000000 !important; font-size: 1.05rem !important; font-weight: 900 !important; }

    .stRadio label { font-size: 1.3rem !important; font-weight: bold !important; color: #000000 !important; padding: 8px 0; }
    .stRadio { background-color: #FFFFFF; padding: 15px; border: 4px solid #000000; border-radius: 20px; box-shadow: 6px 6px 0px #000000; margin-bottom: 20px; }
    .stRadio p { color: #000000 !important; }

    div.stButton > button {
        background-color: #FFEB3B !important; color: #000000 !important;
        font-size: 1.4rem !important; font-weight: 900 !important;
        border: 4px solid #000000 !important; border-radius: 18px !important;
        padding: 12px 20px !important; box-shadow: 5px 5px 0px #000000 !important;
        width: 100% !important;
    }
    div.stButton > button:hover { background-color: #FFD600 !important; color: #000000 !important; }

    .comic-panel { background-color: #FFFFFF; border: 5px solid #000000; padding: 20px; margin-bottom: 20px; border-radius: 15px; box-shadow: 6px 6px 0px #FF9800; }
    img { border-radius: 15px; border: 3px solid #000000; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# ================= 封裝故事引擎 =================
class StoryEngine:
    def __init__(self, story_key):
        self.story_key = story_key
        self.story_data = STORIES[story_key]
        self.reset()

    def reset(self):
        self.current_node = "1_START"
        self.history = []

    def get_current_step(self):
        try:
            return int(self.current_node.split("_")[0])
        except:
            return 1

    def get_current_node_data(self):
        return self.story_data["nodes"].get(self.current_node)

    def is_ending(self):
        return self.current_node == "END"

    def choose(self, title, choice_letter, choice_text):
        self.history.append((title, choice_text))
        next_step = self.get_current_step() + 1
        
        if next_step <= 6:
            next_node = f"{next_step}_{choice_letter}"
            if next_node not in self.story_data["nodes"]:
                next_node = f"{next_step}_A"
            self.current_node = next_node
            
    def finish_story(self, title):
        self.history.append((title, "故事圓滿結束！ The End!"))
        self.current_node = "END"

    def jump_to_page(self, page_num):
        self.history = []
        if page_num == 1:
            self.current_node = "1_START"
        else:
            self.current_node = f"{page_num}_A"

# ================= 初始化系統狀態 =================
if "engine" not in st.session_state:
    st.session_state.engine = StoryEngine("Story1")

engine = st.session_state.engine

# ================= 側邊欄 UI =================
st.sidebar.markdown("## 📚 選擇故事 (Select Story)")
story_options = {k: v["name_tc"] for k, v in STORIES.items()}
selected_story_title = st.sidebar.radio(
    "今日想聽邊個故事？", 
    list(story_options.values()), 
    index=list(story_options.keys()).index(engine.story_key)
)

selected_key = [k for k, v in story_options.items() if v == selected_story_title][0]
if selected_key != engine.story_key:
    st.session_state.engine = StoryEngine(selected_key)
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("## 📖 快速跳頁 (Jump to Page)")
page_options = ["第 1 頁", "第 2 頁", "第 3 頁", "第 4 頁", "第 5 頁", "第 6 頁"]
current_step = engine.get_current_step() if not engine.is_ending() else 6

selected_page_str = st.sidebar.radio("選擇頁數：", page_options, index=current_step - 1)
jump_page_num = page_options.index(selected_page_str) + 1

if st.sidebar.button("🚀 跳轉到此頁 (Jump Now)"):
    engine.jump_to_page(jump_page_num)
    st.rerun()

st.sidebar.markdown("---")
if st.sidebar.button("🔄 重頭開始 (Start Over)"):
    engine.reset()
    st.rerun()

# ================= 主介面渲染 =================
story_title_tc = engine.story_data["name_tc"]
story_title_en = engine.story_data["name_en"]

st.markdown(f'<p class="kids-title">🦸‍♂️ {story_title_tc} 🦸‍♂️</p>', unsafe_allow_html=True)
st.markdown(f'<p class="en-title">{story_title_en}</p>', unsafe_allow_html=True)
st.caption("Son & Dad Exclusive | 雙語爆笑繪本 App")
st.markdown("---")

if not engine.is_ending():
    stage = engine.get_current_node_data()
    step = engine.get_current_step()
    
    st.progress(step / 6, text=f"📖 故事進度 Story Progress：{step} / 6")
    
    st.markdown(f'<p class="kids-sfx">{stage["title_tc"]}<br><span style="font-size:1.1rem;">{stage["title_en"]}</span></p>', unsafe_allow_html=True)
    if "sfx" in stage:
        st.markdown(f'<p class="kids-sfx" style="color:#D32F2F !important;">{stage["sfx"]}</p>', unsafe_allow_html=True)

    # 💥 徹底修復：穩定的單圖與多圖渲染邏輯
    if "images" in stage and isinstance(stage["images"], list):
        cols = st.columns(len(stage["images"]))
        for idx, img_url in enumerate(stage["images"]):
            with cols[idx]:
                st.image(img_url, use_column_width=True)
    elif "image" in stage and stage["image"]:
        st.image(stage["image"], use_column_width=True)

    st.markdown(f"""
    <div class="kids-speech-bubble">
    <p class="tc-story">💬 {stage["story_tc"]}</p>
    <p class="en-story">{stage["story_en"]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if step < 6:
        option_keys = list(stage["choices"].keys())
        option_texts = [f"{k}. {stage['choices'][k]}" for k in option_keys]
        
        selected_text = st.radio("👉 請做出超搞笑抉擇 (Choose your action):", option_texts)
        selected_letter = selected_text[0] 
        
        if st.button("🔥 確定！翻去下一頁！ (Next Page!)"):
            engine.choose(stage["title_tc"], selected_letter, selected_text)
            st.rerun()
    else:
        if st.button("🎉 看完了！印出專屬雙語故事書！ (Print Storybook!)"):
            engine.finish_story(stage["title_tc"])
            st.rerun()

else:
    st.balloons()
    st.success("🎉 恭喜！成功解鎖了爆笑雙語結局！ Congratulations!")
    
    st.header("🖼️ 專屬雙語故事繪本 (Our Bilingual Storybook)")
    for i, (title, choice) in enumerate(engine.history, 1):
        st.markdown(f"""
        <div class="comic-panel">
        <h2 style="font-size: 1.6rem; color: #00838F;">📖 {title}</h2>
        <p style="font-size: 1.3rem; color: #000000; font-weight: bold;"><b>💥 我們的行動 (Action)：</b><br>{choice}</p>
        </div>
        """, unsafe_allow_html=True)
        
    if st.button("🔄 再玩一次！探索其他結局！ (Play Again!)"):
        engine.reset()
        st.rerun()

st.markdown("---")
st.caption("🔥 Firebird Protection App | Son & Dad Exclusive")
