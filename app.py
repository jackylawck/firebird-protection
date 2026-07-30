import streamlit as st

# 頁面配置
st.set_page_config(
    page_title="火鷹俠 Firebird Protection 2 | 恐龍島大冒險",
    page_icon="🦕",
    layout="centered"
)

# 🎨 專為 6 歲設計的大字體與高對比 CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #E8F5E9;
        color: #000000 !important;
    }
    p, span, label, div, h1, h2, h3, h4 {
        color: #000000 !important;
        font-family: 'Comic Sans MS', 'Microsoft JhengHei', sans-serif;
    }
    .kids-title { 
        font-size: 3rem !important; 
        color: #2E7D32 !important; 
        font-weight: 900; 
        text-align: center; 
        text-shadow: 3px 3px 0px #C8E6C9;
        margin-bottom: 10px;
    }
    .kids-sfx {
        font-size: 2.2rem !important;
        color: #FF5722 !important;
        font-weight: 900;
        text-align: center;
        margin: 15px 0;
    }
    .kids-speech-bubble {
        background: #FFFFFF;
        border: 5px solid #000000;
        border-radius: 25px;
        padding: 25px;
        margin: 20px 0;
        font-size: 1.6rem !important;
        line-height: 1.8;
        box-shadow: 8px 8px 0px #000000;
    }
    .stRadio label {
        font-size: 1.5rem !important;
        font-weight: bold !important;
        padding: 10px 0;
    }
    .stRadio {
        background-color: #FFFFFF;
        padding: 20px;
        border: 4px solid #000000;
        border-radius: 20px;
        box-shadow: 6px 6px 0px #000000;
        margin-bottom: 20px;
    }
    .comic-panel {
        background-color: #FFFFFF;
        border: 5px solid #000000;
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 15px;
        box-shadow: 6px 6px 0px #81C784;
    }
    </style>
""", unsafe_allow_html=True)

# 初始化遊戲狀態
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'story_history' not in st.session_state:
    st.session_state.story_history = []
if 'last_choice' not in st.session_state:
    st.session_state.last_choice = "START"

# 大標題
st.markdown('<p class="kids-title">🦕 火鷹俠：恐龍島大冒險 🦕</p>', unsafe_allow_html=True)
st.caption("第二集：專為 6 歲 Jarvis 設計的爆笑恐龍故事！")
st.markdown("---")

# ----------------- 全新恐龍島劇情 -----------------
def get_dino_stage(step, last_choice):
    if step == 1:
        return {
            "title": "第 1 頁：恐龍島的求救信！",
            "sfx": "🚨 嗶嗶！有恐龍求救！",
            "image": "https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9?w=800&auto=format&fit=crop",
            "story": "火鷹俠正在總部吃早餐，突然收到一封來自「恐龍玩具島」的求救信！原來有外星人搗蛋，把恐龍們都變成了滑嘟嘟的果凍！火鷹俠決定出發：",
            "choices": {
                "A": "🚀 展開 Firebird 光影翅膀，用超音速飛過去！",
                "B": "🚪 畫一道神奇的「多啦A夢式」隨意門，直接行過去！",
                "C": " submarine 召喚火鷹潛水艇，潛入海底尋找恐龍島！"
            }
        }
    
    elif step == 2:
        return {
            "title": "第 2 頁：登陸果凍恐龍島！",
            "sfx": "🌟 噗通！滑嘟嘟！",
            "image": "https://images.unsplash.com/photo-1569588661601-523101eb66d5?w=800&auto=format&fit=crop",
            "story": "到了恐龍島，火鷹俠發現四周圍都是粉紅色的香甜泡泡糖！一隻小三角龍被泡泡糖黏住了腳，急得哭了出來。火鷹俠要點樣幫佢？",
            "choices": {
                "A": "💦 噴出「火鷹溫泉水」，把甜甜的泡泡糖融化！",
                "B": "🪶 用羽毛狂搔三角龍的腳底，讓他笑到把泡泡糖撐破！",
                "C": "🎶 唱一首超級好聽的安眠曲，讓泡泡糖睡著變軟！"
            }
        }

    elif step == 3:
        return {
            "title": "第 3 頁：遇見暴龍大王！",
            "sfx": "🦖 吼——！我肚子餓！",
            "image": "https://images.unsplash.com/photo-1596743344692-e4272186711c?w=800&auto=format&fit=crop",
            "story": "三角龍得救了！這時，一隻超巨大的暴龍跑了過來。大家以為牠要生氣，結果牠是在哭訴：「搗蛋外星人搶了我的超級大漢堡！」",
            "choices": {
                "A": "🍔 火鷹俠立刻用手環變出一個更大的「火鷹特製熱狗」請牠吃！",
                "B": "🧸 送給暴龍一隻可愛的火鷹俠毛公仔，哄牠開心！",
                "C": "🤝 拍拍暴龍的膝蓋說：「別哭！我們一起去把漢堡搶回來！」"
            }
        }

    elif step == 4:
        return {
            "title": "第 4 頁：搗蛋外星人出現！",
            "sfx": "👽 嘻嘻哈哈！嗶啵！",
            "image": "https://images.unsplash.com/photo-1614027164847-1b28cfe1df60?w=800&auto=format&fit=crop",
            "story": "暴龍決定加入火鷹俠小隊！他們在火山口找到了「泡泡糖外星人」，他正坐在一架飛碟上向下面扔果凍炸彈！",
            "choices": {
                "A": "🛡️ 舉起「火鷹巨型防護罩」，把果凍炸彈全部彈飛！",
                "B": "🏸 拿出超級大羽毛球拍，把果凍炸彈當羽毛球打回去！",
                "C": "💨 飛上天用嘴巴吹出超級大風，把炸彈吹回太空！"
            }
        }

    elif step == 5:
        return {
            "title": "第 5 頁：外星人的大軍！",
            "sfx": "🤖 咔嚓咔嚓！果凍機器人！",
            "image": "https://images.unsplash.com/photo-1589254065878-42c9da997008?w=800&auto=format&fit=crop",
            "story": "外星人生氣了，變出了 50 隻會跳舞的「果凍機器人」包圍過來！機器人一邊跳舞一邊噴出黏黏的汽水！",
            "choices": {
                "A": "🧊 吐出「草莓冰淇淋氣息」，把機器人全部凍成冰棒！",
                "B": "🦖 叫暴龍大王出來，一腳把機器人踩成扁扁的鬆餅！",
                "C": "💃 跟機器人比拼跳街舞，跳到機器人全部頭暈跌倒！"
            }
        }

    elif step == 6:
        return {
            "title": "第 6 頁：超級恐龍合體！",
            "sfx": "✨ 閃閃發光！超帥氣！",
            "image": "https://images.unsplash.com/photo-1519098901909-b1553a1190af?w=800&auto=format&fit=crop",
            "story": "機器人被打敗了！外星人想開著飛碟逃跑。火鷹俠決定跟暴龍大王發動史無前例的「超級合體」去追他！",
            "choices": {
                "A": "🦖 騎在暴龍背上，給暴龍裝上 Firebird 火焰翅膀一起飛！",
                "B": "🤝 火鷹俠與暴龍手牽手，發射出「友誼大光波」！",
                "C": "🎩 給暴龍戴上神奇放大帽，讓暴龍變得比火山還要高！"
            }
        }

    elif step == 7:
        return {
            "title": "第 7 頁：追上外星飛碟！",
            "sfx": "🚀 嗖——！哪裡跑！",
            "image": "https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?w=800&auto=format&fit=crop",
            "story": "合體後的【暴龍火鷹俠】速度超快，一下子就追上了外星人的飛碟！外星人嚇得按下了飛碟的「超級加速按鈕」！",
            "choices": {
                "A": "🕸️ 扔出一個超級巨大的棉花糖網，把飛碟網住！",
                "B": "🪶 用最快的速度飛到飛碟下面，給飛碟的引擎搔癢！",
                "C": "🛑 大喊一聲「紅燈停！」，用超能力讓飛碟急剎車！"
            }
        }

    elif step == 8:
        return {
            "title": "第 8 頁：發動終極絕招！",
            "sfx": "🌈 準備好啦！一、二、三！",
            "image": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop",
            "story": "飛碟停下來了！泡泡糖外星人舉手投降。火鷹俠決定用一招超級善良的絕招來淨化他！",
            "choices": {
                "A": "🌈「—— 彩虹泡泡衝擊波 ！！！」（把飛碟變成巨大的泡泡）",
                "B": "✨「—— 閃亮亮星星粉 ！！！」（讓外星人變成可愛的小精靈）",
                "C": "🍩「—— 超級甜甜圈抱抱 ！！！」（給外星人一個溫暖的擁抱）"
            }
        }

    elif step == 9:
        return {
            "title": "第 9 頁：外星人變乖了！",
            "sfx": "🎉 耶！交到新朋友！",
            "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop",
            "story": "絕招發射！外星人身上的搗蛋病毒全沒了，變成了一個友善的彩色小圓球！他把漢堡還給了暴龍，還保證以後只做好事！",
            "choices": {
                "A": "🎺 恐龍島舉辦了一場超級歡樂的「漢堡果凍派對」！",
                "B": "🛸 讓外星人開飛碟帶大家去太空看流星雨！",
                "C": "📸 暴龍、外星人和火鷹俠一起拍了一張搞笑大合照！"
            }
        }

    else:
        return {
            "title": "第 10 頁：恐龍島英雄！",
            "sfx": "🏆 暴龍大王說謝謝！",
            "image": "https://images.unsplash.com/photo-1563089145-599997674d42?w=800&auto=format&fit=crop",
            "story": "火鷹俠再次成功拯救了世界！恐龍們為 Jarvis 送上了一個「黃金恐龍蛋」獎盃！Jarvis 對著大家說：",
            "choices": {
                "A": "💬「只要有 Firebird Protection，恐龍和人類都是好朋友！」",
                "B": "💬「外星人不可怕，只要我們勇敢又善良！」",
                "C": "💬「今天的漢堡真好吃！下一集冒險再見囉！」"
            }
        }

# ----------------- 遊戲流程控制 -----------------
current_step = st.session_state.step

if current_step <= 10:
    stage = get_dino_stage(current_step, st.session_state.last_choice)
    
    st.progress(current_step / 10, text=f"📖 故事進度：第 {current_step} / 10 頁")
    
    st.markdown(f'<p class="kids-sfx">{stage["title"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="kids-sfx">{stage["sfx"]}</p>', unsafe_allow_html=True)
    
    # 顯示高畫質清晰圖片
    st.image(stage["image"], use_column_width=True)
    
    # 超大字對話框
    st.markdown(f"""
    <div class="kids-speech-bubble">
    💬 <b>【故事內容】：</b><br>{stage["story"]}
    </div>
    """, unsafe_allow_html=True)
    
    # 選項
    option_keys = list(stage["choices"].keys())
    option_texts = [f"{k}. {stage['choices'][k]}" for k in option_keys]
    
    selected_text = st.radio("👉 請 Jarvis 做出選擇：", option_texts, key=f"radio_dino_{current_step}")
    
    if st.button("🔥 確定！翻去下一頁故事！"):
        st.session_state.story_history.append((stage["title"], selected_text))
        st.session_state.last_choice = selected_text
        st.session_state.step += 1
        st.rerun()

else:
    # 繪本 Print 版
    st.balloons()
    st.success("🎉 恭喜！Jarvis 成功完成了《火鷹俠 2：恐龍島大冒險》！")
    
    st.header("🖼️ Jarvis 的專屬《火鷹俠》恐龍繪本")
    
    for i, (title, choice) in enumerate(st.session_state.story_history, 1):
        st.markdown(f"""
        <div class="comic-panel">
        <h2 style="font-size: 1.8rem; color: #2E7D32;">📖 第 {i} 頁：{title}</h2>
        <p style="font-size: 1.5rem; color: #000000; font-weight: bold;"><b>💥 Jarvis 的選擇：</b><br>{choice}</p>
        </div>
        """, unsafe_allow_html=True)
        
    if st.button("🔄 重新再玩一次恐龍島"):
        st.session_state.step = 1
        st.session_state.story_history = []
        st.session_state.last_choice = "START"
        st.rerun()

# 頁尾
st.markdown("---")
st.caption("🔥 Firebird Protection Kids App 2 | Jarvis & 爸爸 專屬創作")
