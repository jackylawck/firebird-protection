import streamlit as st
import requests

# 頁面配置
st.set_page_config(
    page_title="火鷹俠故事館 | Firebird Protection",
    page_icon="🦸‍♂️",
    layout="centered"
)

# 🎨 兒童雙語與響應式 CSS 升級
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
    .story-text { font-size: clamp(1.2rem, 4vw, 1.6rem) !important; line-height: 1.6; font-weight: bold; }
    
    /* 側邊欄 */
    [data-testid="stSidebar"] { background-color: #1E293B !important; }
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label { color: #FFFFFF !important; }

    div.stButton { display: flex; justify-content: center; }
    div.stButton > button {
        background-color: #FFEB3B !important; color: #000000 !important;
        font-size: 1.3rem !important; font-weight: 900 !important;
        border: 4px solid #000000 !important; border-radius: 16px !important;
        padding: 10px 20px !important; box-shadow: 4px 4px 0px #000000 !important;
        width: 100% !important; max-width: 400px !important;
    }
    div.stButton > button:hover { background-color: #FFD600 !important; }
    </style>
""", unsafe_allow_html=True)

# ----------------- GitHub 免費 API 呼叫函式 (多通道自動兼容) -----------------
def call_github_ai(token, messages, max_tokens=800):
    clean_token = token.strip() if token else ""
    
    # 備選 GitHub API Endpoints
    endpoints = [
        "https://models.inference.ai.azure.com/chat/completions",
        "https://api.githubcopilot.com/chat/completions"
    ]
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {clean_token}",
        "User-Agent": "GitHub-Free-Client/1.0"
    }
    payload = {
        "messages": messages,
        "model": "gpt-4o-mini",
        "temperature": 0.8,
        "max_tokens": max_tokens
    }
    
    for url in endpoints:
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=20)
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
        except:
            continue
            
    return "ERROR_401"

# ----------------- 標題與簡介 -----------------
st.markdown('<p class="kids-title">🦸‍♂️ 火鷹俠全人教育故事館 🚀</p>', unsafe_allow_html=True)
st.markdown('<p class="en-title">Firebird Protection: Whole-Person Education Hub</p>', unsafe_allow_html=True)
st.caption("Son & Dad Exclusive | 傳承全人精神 | 雙語繪本 × 成長對講機")
st.markdown("---")

# ================= 自動讀取 Secrets 或 側邊欄設定 =================
github_token = ""

if "GITHUB_TOKEN" in st.secrets:
    github_token = st.secrets["GITHUB_TOKEN"]
elif "AI_TOKEN" in st.secrets:
    github_token = st.secrets["AI_TOKEN"]
else:
    with st.sidebar.expander("👨‍💼 家長設定區 (Parent Zone)", expanded=True):
        st.markdown("請在此輸入 API 憑證：")
        github_token = st.text_input("通訊密碼 (GitHub Token):", type="password")

if not github_token:
    st.warning("👈 請爸爸先在 Streamlit Secrets 或左邊「家長設定區」設定通訊密碼，幫火鷹俠對講機充電喔！")
else:
    tab1, tab2 = st.tabs(["📖 互動故事冒險", "📻 火鷹俠全能學習對講機"])

    # 🛡️ 核心教育精神 System Prompt (融入 A-School 全人教育理念)
    base_education_rules = """你扮演超級英雄「火鷹俠 (Firebird)」，專門陪一位 6 歲、聰明且充滿好奇心的小隊長互動。
    
【核心教育藍圖：全人為本，學子為先】：
1. 正向教育與成長型思維 (Growth Mindset)：以愛與關懷為基石，當小隊長面對挑戰時，教導他永不放棄。
2. 啟迪多元潛能：培養他明辨是非、包容多元價值、團隊合作與公民責任感。
3. 精通三語技能 (3-Literacy)：對話需自然融合廣東話/繁體中文、地道英文，並巧妙加入科學與生活常識。

【互動與引導規範】：
1. 蘇格拉底式啟發：永遠不直接給出標準答案，而是用幽默例子引導他主動探索。
2. 倫理與安全護欄：嚴格禁止色情、暴力、危險行為，價值觀必須健康正向。
3. 語言與視覺：親切生動的廣東話為主，附帶英文對照，語氣天馬行空幽默，帶有大量生動 Emoji (如 🚨🦖🍕🔥🦆)！"""

    # ================= TAB 1：互動故事 =================
    with tab1:
        if "ai_history" not in st.session_state:
            st.session_state.ai_history = []

        story_system_prompt = base_education_rules + """\n【任務】：寫互動故事繪本。將科學、數學或常識小謎題無縫融入情節中！
每一頁必須包含：
- 中文故事情節 (帶大量 Emoji)
- English translation
- 三個超有創意、結合解難能力的搞笑選項：A、B、C
- 注意：如果小隊長輸入了自訂行動，請將其視為「D 選項」，並順著他的天馬行空想法編寫下一頁，最後依然給出新的 A/B/C 選項供選擇。"""

        if len(st.session_state.ai_history) == 0:
            if st.button("🚀 點擊開始全新的火鷹俠冒險！"):
                messages = [
                    {"role": "system", "content": story_system_prompt},
                    {"role": "user", "content": "請為《火鷹俠》創作第 1 頁的全新爆笑開頭！設定一個涉及宇宙、科學或數學謎題的搞笑危機！"}
                ]
                with st.spinner("🚀 火鷹俠正在登場中..."):
                    reply = call_github_ai(github_token, messages, max_tokens=800)
                    if reply == "ERROR_401":
                        st.error("❌ 驗證失敗！請點擊左側「🔄 重新開始故事與對話」清除快取重試。")
                    else:
                        st.session_state.ai_history.append({"role": "assistant", "content": reply})
                        st.rerun()

        for msg in st.session_state.ai_history:
            if msg["role"] == "assistant":
                st.markdown(f'<div class="story-card"><p class="story-text">{msg["content"]}</p></div>', unsafe_allow_html=True)
            elif msg["role"] == "user":
                with st.chat_message("user", avatar="🦸‍♂️"):
                    st.write(f"**我們的決定：** {msg['content']}")

        if len(st.session_state.ai_history) > 0:
            st.markdown("---")
            user_choice = st.text_input("👉 選擇 A/B/C，或發揮想像力自己寫行動：", key="story_input")
            
            if st.button("🔥 確定！翻去下一頁！ (Next Page!)"):
                if user_choice:
                    api_messages = [{"role": "system", "content": story_system_prompt}]
                    for m in st.session_state.ai_history:
                        api_messages.append(m)
                    
                    api_messages.append({"role": "user", "content": f"我選擇了：{user_choice}。請繼續寫下一頁故事！帶大量 Emoji 與選項 A, B, C！"})
                    st.session_state.ai_history.append({"role": "user", "content": user_choice})
                    
                    with st.spinner("🚀 火鷹俠正在飛往下一個場景..."):
                        reply = call_github_ai(github_token, api_messages, max_tokens=800)
                        if reply == "ERROR_401":
                            st.error("❌ 通訊失敗，請重新嘗試。")
                            st.session_state.ai_history.pop()
                        else:
                            st.session_state.ai_history.append({"role": "assistant", "content": reply})
                            st.rerun()

    # ================= TAB 2：全能學習對講機 =================
    with tab2:
        st.markdown("### 📻 火鷹俠全能學習對講機 (Talk & Learn)")
        st.caption("小隊長可以隨時喺度同火鷹俠聊天、問功課，或者討論宇宙知識喔！")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        chat_system_prompt = base_education_rules + """\n【任務】：對講機全能學習導師。
- 緊記「成長型思維」，遇到困難鼓勵他。
- 回答中西文化、中英數常識問題，善用生活化例子。
- **重要限制：回覆請保持簡短精練，每段不超過 5 句話，確保 6 歲兒童有耐心閱讀。**
- 保持廣東話 + 雙語對話 + 大量 Emoji！"""

        for message in st.session_state.chat_history:
            with st.chat_message(message["role"], avatar="🦸‍♂️" if message["role"] == "user" else "📻"):
                st.markdown(message["content"])

        if prompt := st.chat_input("📻 對火鷹俠說話... (例如：恐龍點解會絕種？)"):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user", avatar="🦸‍♂️"):
                st.markdown(prompt)

            api_chat_messages = [{"role": "system", "content": chat_system_prompt}]
            for m in st.session_state.chat_history:
                api_chat_messages.append(m)

            with st.chat_message("assistant", avatar="📻"):
                with st.spinner("📻 火鷹俠正在思考並按對講機回覆你..."):
                    chat_reply = call_github_ai(github_token, api_chat_messages, max_tokens=500)
                    if chat_reply == "ERROR_401":
                        st.error("❌ 通訊失敗，請重試。")
                        st.session_state.chat_history.pop()
                    else:
                        st.markdown(chat_reply)
                        st.session_state.chat_history.append({"role": "assistant", "content": chat_reply})

# 側邊欄重置
st.sidebar.markdown("---")
if st.sidebar.button("🔄 重新開始故事與對話"):
    st.session_state.ai_history = []
    st.session_state.chat_history = []
    st.rerun()
