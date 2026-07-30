import streamlit as st
import time

# 頁面配置
st.set_page_config(
    page_title="Firebird Protection | 10關互動故事大冒險",
    page_icon="🔥",
    layout="centered"
)

# CSS 樣式美化 (高對比度文字)
st.markdown("""
    <style>
    .main-title { 
        font-size: 2.2rem; 
        color: #FF4B4B; 
        font-weight: bold; 
        text-align: center; 
    }
    .story-card { 
        background-color: #F0F4F8; 
        color: #1A1A1A !important; 
        padding: 20px; 
        border-radius: 12px; 
        border-left: 6px solid #FF4B4B; 
        margin-bottom: 20px;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    .story-card b, .story-card i {
        color: #000000 !important;
    }
    .print-box {
        background-color: #FFFFFF;
        color: #000000 !important;
        padding: 25px;
        border: 2px dashed #FF4B4B;
        border-radius: 10px;
        font-family: 'Courier New', Courier, monospace;
        line-height: 1.8;
    }
    </style>
""", unsafe_allow_html=True)

# 初始化遊戲狀態 Session State
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'story_history' not in st.session_state:
    st.session_state.story_history = []

# 主標題
st.markdown('<p class="main-title">🔥🦅 火鷹俠：10關大冒險</p>', unsafe_allow_html=True)
st.caption("Jarvis & 爸爸 專屬創作 | Firebird Protection 互動故事")

st.markdown("---")

# 10 個關卡的劇情與 3 個選項設定
stages = {
    1: {
        "title": "第 1 關：深山迷路與神秘電話",
        "story": "火鷹俠一邊打電話一邊尋找隱蔽地方，一不留神走得太遠，來到了一座神秘的深山森林。四周靜悄悄的，突然樹林裡傳來異響！火鷹俠該怎麼辦？",
        "choices": [
            "A. 🚀 啟動 Firebird Protection 力量，召喚森林野生動物做手下！",
            "B. 🛡️ 開啟「火鷹隱形防護罩」，先躲在樹上觀察形勢！",
            "C. 🔊 用智能手環大聲播放「火鷹戰歌」，嚇退潛伏的敵人！"
        ]
    },
    2: {
        "title": "第 2 關：動物手下的搜尋任務",
        "story": "火鷹俠集結了動物小隊（飛鷹、狼群、松鼠）！現在需要展開搜尋，尋找隱藏在森林深處的壞人。火鷹俠要點樣分工？",
        "choices": [
            "A. 🦅 派飛鷹小隊飛上高空，做全空域 360 度偵查！",
            "B. 🐺 讓狼群憑嗅覺在地面灌木叢仔細搜尋！",
            "C. 🐿️ 讓小松鼠們在樹冠之間穿梭，尋找秘密基地入口！"
        ]
    },
    3: {
        "title": "第 3 關：發現神秘山洞基地",
        "story": "動物手下們終於在懸崖下方找到了一個冒著紫煙的神秘山洞！壞人就在裡面，但山洞口有激光防禦網。火鷹俠決定：",
        "choices": [
            "A. 💥 用「火鷹烈焰衝擊」直接轟開激光防禦網！",
            "B. 鑽進小松鼠挖的秘密地道，偷偷溜進山洞！",
            "C. 讓大象手下搬來巨石，把激光發射器砸爛！"
        ]
    },
    4: {
        "title": "第 4 關：壞人的黑科技武器",
        "story": "衝進山洞後，壞人首領「時光黑影」推出了龐大的黑科技大砲，準備向城市發射「時間倒轉光束」！火鷹俠如何應對？",
        "choices": [
            "A. 🛡️ 展開「火鷹超級防護罩」，死守大砲射線！",
            "B. ⚡ 啟動「光影翅膀超光速」，飛過去拔掉大砲的電源線！",
            "C. 讓獵豹手下快速奪走壞人手中的發射遙控器！"
        ]
    },
    5: {
        "title": "第 5 關：萬獸之王登場！",
        "story": "壞人見大砲無效，啟動了緊急備用能源，發射出強大的能量波！就在危急關頭，森林深處傳來一聲震撼山谷的獅吼——百獸之王「金獅」衝了進來！火鷹俠要做什麼？",
        "choices": [
            "A. 🦁 與金獅進行「終極合體」，變成【獅王火鷹俠】！",
            "B. 🤝 給金獅穿上 Firebird Protection 護甲，雙人並肩作戰！",
            "C. 讓金獅掩護其他動物手下撤退，自己獨自對決壞人！"
        ]
    },
    6: {
        "title": "第 6 關：合體形態的試煉",
        "story": "火鷹俠與金獅成功合體！【獅王火鷹俠】身上閃耀著金紅色的霸氣烈焰！壞人嚇得派出了一群鋼鐵機械蜘蛛包圍過來！獅王火鷹俠會用哪招？",
        "choices": [
            "A. 🐾 發動「獅王火焰爪」，把機械蜘蛛瞬間切成碎片！",
            "B. 🦁 喊出「獅王咆哮彈」，用音波將所有蜘蛛震飛！",
            "C. 🪶 揮動火焰翅膀，刮起烈焰風暴將蜘蛛全部燒融！"
        ]
    },
    7: {
        "title": "第 7 關：壞人的最後掙紮",
        "story": "機械蜘蛛全滅！壞人首領「時光黑影」眼看要敗，決定按下一鍵自爆按鈕，想把山洞和周圍森林一起炸毀！火鷹俠該怎麼辦？",
        "choices": [
            "A. 凍結！用智能手環發射「零度冰封光束」凍結自爆計時器！",
            "B. 💨 用超高速把自爆裝置一把抓起，扔向無人的高空爆炸！",
            "C. 🛡️ 用最大功率的防護罩籠罩整個自爆裝置，吸收爆炸威力！"
        ]
    },
    8: {
        "title": "第 8 關：發動終極絕招！",
        "story": "自爆危機解除！壞人已經無路可逃，但還在垂死掙紮。獅王火鷹俠積蓄了全身最強的力量，準備一擊必殺！他大喊一聲發動的絕招是：",
        "choices": [
            "A. 🌈「—— 顏色沙漠土 ！！！」（把壞人全變成五彩沙土）",
            "B. ✨「—— 彩虹星辰塵 ！！！」（把壞人全變成閃耀星塵）",
            "C. 💎「—— 五彩水晶砂 ！！！」（把壞人全封印成彩色水晶）"
        ]
    },
    9: {
        "title": "第 9 關：淨化與拯救成功！",
        "story": "絕招發射！耀眼的光芒籠罩了整個山洞，壞人和他們的邪惡武器全部變成了五彩繽紛的沙土，徹底被淨化！森林恢復了平靜，動物手下們紛紛歡呼！火鷹俠接下來要做咩？",
        "choices": [
            "A. 🎺 帶領動物大軍舉辦一場「森林勝利狂歡派對」！",
            "B. 🚁 叫總部派出飛艇，把彩色的沙土運回去研究做藝術品！",
            "C. 飛回市中心大鐘樓，向全城市民宣告和平回歸！"
        ]
    },
    10: {
        "title": "第 10 關：英雄歸來與傳奇誕生",
        "story": "火鷹俠完成了任務，回到了總部。智囊隊長和全城市民給他送上了最高榮譽勳章！Jarvis（火鷹俠）對大家說的英雄名言是：",
        "choices": [
            "A. 💬「只要有 Firebird Protection，正義永遠不會失敗！」",
            "B. 💬「團結就是力量！感謝我的森林動物好夥伴！」",
            "C. 💬「保護城市是我的職責！下一場冒險我們再見！」"
        ]
    }
}

# 遊戲流程控制
current_step = st.session_state.step

if current_step <= 10:
    # 顯示進度條
    st.progress(current_step / 10, text=f"冒險進度：第 {current_step} / 10 關")
    
    stage_info = stages[current_step]
    st.header(stage_info["title"])
    
    st.markdown(f"""
    <div class="story-card">
    {stage_info["story"]}
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("請仔仔做出選擇：")
    selected_option = st.radio("選擇你的劇情走向：", stage_info["choices"], key=f"choice_{current_step}")
    
    if st.button("🔥 確定選擇，進入下一關！"):
        # 記錄選擇
        st.session_state.story_history.append((stage_info["title"], selected_option))
        st.session_state.step += 1
        st.rerun()

else:
    # 通關，生成完整故事 Print 版
    st.balloons()
    st.success("🎉 恭喜通關！火鷹俠 successfully 完成了 10 關大冒險！")
    
    st.header("📜 火鷹俠傳奇冒險：完整故事 Print 版")
    st.caption("你可以直接複製以下框裡面的完整故事，印出來留念或存檔！")
    
    full_story_text = "【火鷹俠：Firebird Protection 10關大冒險】\n\n"
    full_story_text += "創作者：Jarvis (火鷹俠) & 爸爸\n"
    full_story_text += "----------------------------------------\n\n"
    
    for i, (title, choice) in enumerate(st.session_state.story_history, 1):
        full_story_text += f"{title}\n"
        full_story_text += f"【火鷹俠的抉擇】：{choice}\n\n"
        
    full_story_text += "----------------------------------------\n"
    full_story_text += "🎉 結局：火鷹俠成功拯救森林與城市，成為傳奇英雄！"
    
    # 展示 Print 框
    st.markdown(f"""
    <div class="print-box">
    <pre style="white-space: pre-wrap; word-wrap: break-word;">{full_story_text}</pre>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 重新玩一次（重新選擇劇情）"):
        st.session_state.step = 1
        st.session_state.story_history = []
        st.rerun()

# 頁尾
st.markdown("---")
st.caption("🔥 Firebird Protection App v3.0 | 版權所有：Jarvis & 爸爸")
