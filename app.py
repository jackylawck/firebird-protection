import streamlit as st
import time

# 頁面配置
st.set_page_config(
    page_title="Firebird Protection | Dog Man 風格漫畫大冒險",
    page_icon="💥",
    layout="centered"
)

# 🎨 Dog Man 爆笑美式漫畫 CSS 樣式 (強制所有文字變深色高對比)
st.markdown("""
    <style>
    /* 全局漫畫背景 */
    .stApp {
        background-color: #FFFDE7;
        color: #000000 !important;
    }
    
    /* 強制所有文字、label、radio 選項變黑色 */
    p, span, label, div, h1, h2, h3, h4, .stRadio label {
        color: #000000 !important;
        font-weight: 600;
    }

    /* 漫畫標題風格 */
    .comic-title { 
        font-size: 2.8rem; 
        color: #FF1744 !important; 
        font-weight: 900; 
        text-align: center; 
        text-shadow: 2px 2px 0px #000000;
        letter-spacing: 2px;
    }
    
    /* Dog Man 對話框風格 */
    .speech-bubble {
        background: #FFFFFF;
        border: 4px solid #000000;
        border-radius: 20px;
        padding: 20px;
        margin: 15px 0;
        font-size: 1.2rem;
        box-shadow: 5px 5px 0px #000000;
    }
    
    /* 漫畫音效文字 (SFX) */
    .sfx-text {
        font-size: 2rem;
        color: #FF6D00 !important;
        font-weight: 900;
        text-align: center;
        text-shadow: 1px 1px 0px #000;
        transform: rotate(-3deg);
        margin: 10px 0;
    }

    /* Radio 選項包裝 */
    .stRadio {
        background-color: #FFFFFF;
        padding: 15px;
        border: 3px solid #000000;
        border-radius: 12px;
        box-shadow: 4px 4px 0px #000000;
        margin-bottom: 15px;
    }

    /* 漫畫格 */
    .comic-panel {
        background-color: #FFFFFF;
        border: 4px solid #000000;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 5px 5px 0px #FFD600;
    }
    </style>
""", unsafe_allow_html=True)

# 初始化遊戲狀態
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'story_history' not in st.session_state:
    st.session_state.story_history = []

# 標題與 Dog Man 搞笑開場
st.markdown('<p class="comic-title">💥 火鷹俠 FIREBIRD 💥</p>', unsafe_allow_html=True)
st.markdown('<div class="sfx-text">✨ Dog Man 爆笑漫畫大冒險！ ✨</div>', unsafe_allow_html=True)

st.markdown("---")

# 10 個關卡
stages = {
    1: {
        "title": "CHAPTER 1: 深山迷路與神秘電話！",
        "image": "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d?w=600&auto=format&fit=crop",
        "sfx": "📞 BEEP BEEP!! ZZZZZT!!",
        "story": "火鷹俠一邊打電話一邊「匿埋」，點知行行嚇行得太遠，去咗一座神秘黑森林！「嘰嘰咕咕……」森林裡傳出奇怪的聲音！",
        "choices": [
            "A. 🚀 啟動 Firebird 力量！發射火焰餅乾召喚森林動物做手下！",
            "B. 🛡️ 開啟「搞笑隱形術」，貼喺樹幹度假裝自己係一片樹葉！",
            "C. 📢 用智能手環播《Dog Man 主題曲》，跳舞嚇退敵人！"
        ]
    },
    2: {
        "title": "CHAPTER 2: 動物手下搞搞震大搜尋！",
        "image": "https://images.unsplash.com/photo-1534188753412-3e26d0d618d6?w=600&auto=format&fit=crop",
        "sfx": "🔍 WOOF WOOF! ROAR!",
        "story": "火鷹俠召喚咗動物大軍（飛鷹、搞笑狼群、爆笑松鼠）！壞人唔知藏喺邊，動物手下要分工去搵壞人！",
        "choices": [
            "A. 🦅 派飛鷹小隊戴上墨鏡，飛上高空做 360 度搞笑偵查！",
            "B. 🐺 讓狼群用鼻哥聞，一邊搵壞人一邊搵骨頭！",
            "C. 🐿️ 讓松鼠向樹下投擲松果，用「松果雨」逼壞人現身！"
        ]
    },
    3: {
        "title": "CHAPTER 3: 發現神秘山洞基地！",
        "image": "https://images.unsplash.com/photo-1509114397022-ed747cca3f65?w=600&auto=format&fit=crop",
        "sfx": "💥 BAM! CRASH!",
        "story": "松鼠果真喺山洞口發現咗壞人！山洞門口有紫色的激光防禦網，壞人喺裏面吃食熱狗！",
        "choices": [
            "A. 💥 用「火鷹超音速屁屁衝擊」直接撞飛防禦網！",
            "B. 鑽進小松鼠挖嘅搞笑地道，偷偷溜進去搶壞人嘅熱狗！",
            "C. 讓大象搬來超大巨石，像打保齡球咁砸爛防禦網！"
        ]
    },
    4: {
        "title": "CHAPTER 4: 壞人的黑科技大砲！",
        "image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=600&auto=format&fit=crop",
        "sfx": "⚡ ZAP! ZAP!",
        "story": "壞人首領「時光黑影」搬出一台超級大砲，準備發射「時間倒轉光束」，把整座城市變成嬰兒王國！",
        "choices": [
            "A. 🛡️ 展開「火鷹巨型搞笑防護罩」，把光束彈回壞人身上！",
            "B. ⚡ 飛過去用香蕉皮滑倒壞人，順便拔掉大砲電源！",
            "C. 讓獵豹手下咬走壞人嘅褲子，讓壞人分心！"
        ]
    },
    5: {
        "title": "CHAPTER 5: 萬獸之王獅子登場！",
        "image": "https://images.unsplash.com/photo-1614027164847-1b28cfe1df60?w=600&auto=format&fit=crop",
        "sfx": "🦁 ROAAAAAR!!!",
        "story": "壞人發狂啦！就在此時，森林深處傳來巨響——森林之王「金獅」穿著超人披風帥氣登場！",
        "choices": [
            "A. 🦁 與金獅進行 Dog Man 式合體，變成【獅王火鷹俠】！",
            "B. 🤝 給金獅戴上「火鷹搞笑頭盔」，雙人組隊打壞人！",
            "C. 讓金獅大吼一聲，把壞人嘅頭髮全部吹成爆米花髮型！"
        ]
    },
    6: {
        "title": "CHAPTER 6: 鋼鐵蜘蛛大軍襲來！",
        "image": "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?w=600&auto=format&fit=crop",
        "sfx": "🕷️ KACHACK! KACHACK!",
        "story": "合體成功！【獅王火鷹俠】全身發光！壞人放出了 100 隻鋼鐵蜘蛛手下圍攻過來！",
        "choices": [
            "A. 🐾 發動「獅王火焰肉墊拳」，把蜘蛛打成搞笑玩具！",
            "B. 🦁 喊出「超大聲獅吼功」，直接將蜘蛛震到上天！",
            "C. 🪶 揮動火焰翅膀吹出甜甜圈形狀嘅火圈，套住所有蜘蛛！"
        ]
    },
    7: {
        "title": "CHAPTER 7: 壞人按下了自爆按鈕！",
        "image": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop",
        "sfx": "🚨 BEEP! BEEP! DANGER!",
        "story": "壞人輸唔起，按下了「30秒搞笑自爆按鈕」，山洞開始搖晃，壞人自己都嚇到哭！",
        "choices": [
            "A. 🧊 吐出一口「冰淇淋冷凍氣息」，凍結自爆計時器！",
            "B. 💨 用超光速把自爆彈抓起來，扔去外太空炸泡泡！",
            "C. 🛡️ 用防護罩把壞人和炸彈一齊罩住，聽「噗」一聲悶響！"
        ]
    },
    8: {
        "title": "CHAPTER 8: 終極絕招大發射！",
        "image": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=600&auto=format&fit=crop",
        "sfx": "🌈 KABOOM!!!",
        "story": "危機解除！獅王火鷹俠準備給壞人最後一擊！他聚精會神，喊出了傳說中的絕招：",
        "choices": [
            "A. 🌈「—— 顏色沙漠土 ！！！」（把壞人全變成彩色沙土）",
            "B. ✨「—— 彩虹彩帶爆米花 ！！！」（把壞人全變成彩帶）",
            "C. 💎「—— 糖果彩色水晶 ！！！」（把壞人封印成巨型軟糖）"
        ]
    },
    9: {
        "title": "CHAPTER 9: 壞人變成了顏色沙漠土！",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600&auto=format&fit=crop",
        "sfx": "🎉 YAY! WE WON!",
        "story": "絕招命中！壞人和他們的武器瞬間變成咗五彩繽紛嘅「顏色沙漠土」！森林保住了，動物們開心到跳舞！",
        "choices": [
            "A. 🎺 舉辦「Dog Man 式搞笑狂歡派對」，大家一齊吃熱狗！",
            "B. 🚁 用直升機把彩色沙漠土運去沙灘，建一座彩虹城堡！",
            "C. 擺一個超帥氣嘅波士 Pose，拍下英雄漫畫封面照！"
        ]
    },
    10: {
        "title": "CHAPTER 10: 英雄歸來與漫畫大結局！",
        "image": "https://images.unsplash.com/photo-1563089145-599997674d42?w=600&auto=format&fit=crop",
        "sfx": "🏆 HERO OF THE YEAR!",
        "story": "火鷹俠回到市中心，全城市民同智囊隊長歡呼慶祝！Jarvis（火鷹俠）對著鏡頭講出了最霸氣嘅名言：",
        "choices": [
            "A. 💬「只要有 Firebird Protection，正義同搞笑永遠勝出！」",
            "B. 💬「多謝我嘅動物好朋友！今晚大家一齊吃大餐！」",
            "C. 💬「拯救世界成功！下一集 Dog Man 冒險再見！」"
        ]
    }
}

# 流程控制
current_step = st.session_state.step

if current_step <= 10:
    stage = stages[current_step]
    
    # 進度條
    st.progress(current_step / 10, text=f"📖 漫畫頁數：第 {current_step} / 10 頁")
    
    # 關卡標題與音效
    st.subheader(stage["title"])
    st.markdown(f'<div class="sfx-text">{stage["sfx"]}</div>', unsafe_allow_html=True)
    
    # 顯示插圖
    st.image(stage["image"], use_column_width=True)
    
    # 對話框
    st.markdown(f"""
    <div class="speech-bubble">
    💬 <b>【劇情】：</b><br>{stage["story"]}
    </div>
    """, unsafe_allow_html=True)
    
    # 選項（強制黑字白底框）
    selected_option = st.radio("👉 請仔仔選擇 Dog Man 式搞笑走向：", stage["choices"], key=f"c_{current_step}")
    
    if st.button("💥 確定！翻去下一頁漫畫！"):
        st.session_state.story_history.append((stage["title"], selected_option))
        st.session_state.step += 1
        st.rerun()

else:
    # 通關頁面
    st.balloons()
    st.success("🎉 恭喜！你哋完成了 Dog Man 風格《火鷹俠》漫畫大冒險！")
    
    st.header("🖼️ 你的專屬 Dog Man 漫畫繪本 (Print 版)")
    
    for i, (title, choice) in enumerate(st.session_state.story_history, 1):
        st.markdown(f"""
        <div class="comic-panel">
        <h3>📖 第 {i} 格漫畫：{title}</h3>
        <p style="font-size: 1.1rem; color: #000000;"><b>💥 火鷹俠嘅抉擇：</b> {choice}</p>
        </div>
        """, unsafe_allow_html=True)
        
    if st.button("🔄 再畫一次新漫畫（重新玩）"):
        st.session_state.step = 1
        st.session_state.story_history = []
        st.rerun()

# 頁尾
st.markdown("---")
st.caption("💥 Firebird Protection x Dog Man Comic App | Jarvis & 爸爸 聯合出品")
