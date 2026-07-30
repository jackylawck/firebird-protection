import streamlit as st
import time

# 頁面基本設定
st.set_page_config(
    page_title="火鷹俠 Firebird Protection 故事總部",
    page_icon="🔥",
    layout="centered"
)

# 自訂樣式美化
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; color: #FF4B4B; font-weight: bold; text-align: center; }
    .story-card { background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #FF4B4B; margin-bottom: 20px; }
    .choice-result { background-color: #e8f4f8; padding: 20px; border-radius: 10px; border-left: 5px solid #1E88E5; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🔥🦅 火鷹俠：Firebird Protection 傳奇</p>', unsafe_allow_html=True)
st.caption("Jarvis 與爸爸聯合創作 — 互動式英雄故事 App")

st.markdown("---")

# 側邊欄：英雄與系統狀態
st.sidebar.header("🛡️ 火鷹俠 (Firebird) 檔案")
st.sidebar.info("**主角：** Jarvis (火鷹俠)")
st.sidebar.success("**系統：** Firebird Protection v1.0")
st.sidebar.progress(100, text="能量值：100% 滿格")

st.sidebar.markdown("---")
st.sidebar.subheader("🎒 裝備與招式庫")
st.sidebar.write("• **光影翅膀 (Firebird Wings)：** 超光速飛行與空中避障")
st.sidebar.write("• **火鷹防護罩 (Fire Shield)：** 阻擋一切物理與能量攻擊")
st.sidebar.write("• **智能手環 (Smart Band)：** 連線總部並進行數據分析")

# 故事分頁
tab1, tab2 = st.tabs(["📖 閱讀完整故事", "⚙️ 裝備測試"])

with tab1:
    st.header("📜 故事正篇")
    
    # 第一章
    with st.expander("📖 第一章：怪異的符號 (點擊展開閱讀)", expanded=True):
        st.markdown("""
        <div class="story-card">
        <b>【第一章：怪異的符號】</b><br><br>
        在一個平靜的星期六早晨，太陽剛剛升起。小英雄正在總部吃著最喜歡的早餐，突然，桌上的「超人通訊器」發出了急促的嗶嗶聲！<br><br>
        螢幕上顯示，市中心的大鐘樓頂端出現了一個巨大的閃光符號，整座城市的通訊設備都開始播出一陣奇怪的聲音：<i>「嘰嘰……咕咕……」</i>。<br><br>
        城市的居民們都很慌張，不知道發生了什麼事。智囊隊長立刻轉身喊道：<b>「情況緊急！市中心需要你！」</b>
        </div>
        """, unsafe_allow_html=True)

    # 第二章
    with st.expander("📖 第二章：火鷹俠出擊！(點擊展開閱讀)", expanded=True):
        st.markdown("""
        <div class="story-card">
        <b>【第二章：火鷹俠出擊！】</b><br><br>
        聽到急促的通訊器響聲，小英雄立刻按下手環上的按鈕，大聲喊出變身口號：<br>
        <b>「火鷹俠，Firebird Protection，全面啟動！」</b><br><br>
        瞬間，一道耀眼的火紅色光芒包圍了他，背後展開一雙閃耀著火焰光芒的光影翅膀（Firebird Wings），胸前亮起了熾熱的鷹形標誌！<br><br>
        火鷹俠展翅高飛，劃破長空，幾秒鐘就飛到了市中心大鐘樓的上空。到了鐘樓頂端，火鷹俠低頭一看，發現大鐘樓的指針居然在倒著轉！而在鐘樓下方，有一個全身包得像黑洞、手持怪異儀器的神秘怪客<b>「時光黑影」</b>！
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🎮 決定第三章的戰鬥發展！")
    st.write("面對神秘怪客「時光黑影」，請仔仔決定火鷹俠第一時間要做咩：")

    choice = st.radio(
        "請選擇火鷹俠的戰術：",
        [
            "1. 🛡️ 開啟「火鷹防護罩」：優先保護現場慌亂的市民！",
            "2. 🔥 使用「火鷹俯衝」：發動烈焰加速，直接衝向時光黑影！",
            "3. 🔊 啟動「智能手環分析」：破解「嘰嘰……咕咕……」聲波的秘密！"
        ]
    )

    if st.button("🔥 確定選擇，生成第三章！"):
        st.success("戰術已發送至火鷹俠系統！故事生成中...")
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        
        st.balloons()
        st.markdown("### 📖 第三章：最終決戰（專屬結局）")
        
        if "1." in choice:
            st.markdown("""
            <div class="choice-result">
            <b>【第三章：防護罩之光】</b><br><br>
            火鷹俠看到鐘樓附近的市民被倒轉的時間波及、走起路來東倒西歪，他毫不猶豫大喊：<b>「 Firebird Protection，火鷹防護罩，最大功率！」</b><br><br>
            一道巨大的半透明紅色光罩瞬間籠罩了整座廣場，擋住了時光黑影發射出的倒轉光束！市民們安全了，紛紛為火鷹俠歡呼！<br><br>
            時光黑影見怪招無效，急得手忙腳亂。火鷹俠趁機利用防護罩折射太陽光，產生耀眼的光芒，直接讓時光黑影睜不開眼。火鷹俠迅速飛上前，一把奪下了他的時間倒轉儀器！<br><br>
            <b>🎉 結局：大鐘樓恢復正常運作，火鷹俠成功拯救了城市，成為大家心中的守護英雄！</b>
            </div>
            """, unsafe_allow_html=True)
            
        elif "2." in choice:
            st.markdown("""
            <div class="choice-result">
            <b>【第三章：烈焰衝擊】</b><br><br>
            火鷹俠雙翅一振，背後的火焰發射器全開：<b>「火鷹俯衝！衝啊！」</b><br><br>
            他化作一道紅色的閃電從天而降，速度快到連時光黑影都來不及反應！時光黑影驚慌地舉起儀器發射時間光束，但火鷹俠高超地在空中做了一個「360度大翻滾」，靈巧地避開了所有攻擊！<br><br>
            「砰！」火鷹俠精準地降落在時光黑影面前，強大的氣流直接將怪客手中的儀器吹飛落在地上。時光黑影看到火鷹俠威風凜凜的樣子，嚇得連忙舉手投降！<br><br>
            <b>🎉 結局：時光黑影被繩之以法，火鷹俠的敏捷與勇氣贏得了全城人的讚賞！</b>
            </div>
            """, unsafe_allow_html=True)
            
        else:
            st.markdown("""
            <div class="choice-result">
            <b>【第三章：智慧破敵】</b><br><br>
            火鷹俠保持冷靜，抬起手腕按下了智能手環：<b>「Firebird Protection 數據分析，啟動！」</b><br><br>
            手環發出一道藍光，快速掃描那陣<i>「嘰嘰……咕咕……」</i>的聲音。智囊隊長在總部傳來訊息：「火鷹俠，找到了！這個聲音是怪客控制時間儀器的聲波頻率！」<br><br>
            火鷹俠立刻將手環調至相反的音頻，大聲播放「反向聲波」！奇蹟發生了——時光黑影的時間倒轉儀器開始冒出陣陣白煙，最後「啪噠」一聲故障熄火！大鐘樓的指針終於恢復了正常運轉。<br><br>
            <b>🎉 結局：火鷹俠用智慧不費一兵一卒就解除了危機，證明了 Firebird Protection 系統是最頂尖科技！</b>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.header("⚡ 裝備防禦測試")
    st.write("點擊按鈕，測試火鷹俠各項系統性能：")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔥 測試光影翅膀"):
            st.write("🚀 飛行速度達到 5 馬赫！狀態良好！")
            st.snow()
    with col2:
        if st.button("🛡️ 測試火鷹防護罩"):
            st.write("🛡️ 防護力 100%！可抵擋巨石撞擊！")
            st.balloons()

# 頁尾
st.markdown("---")
st.caption("🔥 Firebird Protection App | 版權所有：Jarvis & 爸爸")
