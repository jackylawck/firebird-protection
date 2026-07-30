import streamlit as st
from gtts import gTTS
import io

# 頁面配置
st.set_page_config(
    page_title="火鷹俠 1 | Firebird Protection",
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
    .stRadio label { font-size: 1.3rem !important; font-weight: bold !important; padding: 8px 0; }
    .stRadio { background-color: #FFFFFF; padding: 20px; border: 4px solid #000000; border-radius: 20px; box-shadow: 6px 6px 0px #000000; margin-bottom: 20px; }
    .comic-panel { background-color: #FFFFFF; border: 5px solid #000000; padding: 20px; margin-bottom: 20px; border-radius: 15px; box-shadow: 6px 6px 0px #FF9800; }
    </style>
""", unsafe_allow_html=True)

# 🔊 語音生成函數 (Text-to-Speech)
def play_audio(text, lang='zh-TW'):
    try:
        tts = gTTS(text=text, lang=lang)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        st.audio(fp, format='audio/mp3')
    except Exception as e:
        st.error("語音讀取失敗，請確保已連接網絡。")

# ----------------- 健康爆笑雙語 30 分支場景庫 -----------------
SCENES = {
    "1_START": {
        "title_tc": "第 1 頁：玩具失竊大危機！",
        "title_en": "Page 1: The Great Toy Crisis!",
        "sfx": "🚨 嗚哇！WEE WOO!",
        "story_tc": "大件事啦！「糖果外星人」偷走了全城小朋友最喜歡的玩具！火鷹俠必須去外星基地奪回玩具，他決定：",
        "story_en": "Oh no! The 'Candy Aliens' stole all the kids' favorite toys! Firebird must get them back. He decides to:",
        "choices": {
            "A": "🚀 坐上「超級彩虹推進火箭」飛上太空！ (Ride the Super Rainbow Rocket!)", 
            "B": "🦆 召喚一隻跟大廈一樣高的「超級黃色膠鴨」！ (Summon a building-sized Super Rubber Duck!)", 
            "C": "📦 跳進神奇紙皮箱，變成宇宙飛船！ (Jump into a magic cardboard box spaceship!)"
        }
    },
    
    # Layer 2
    "2_A": {
        "title_tc": "第 2 頁：會飛的披薩隕石！",
        "title_en": "Page 2: Flying Pizza Meteors!",
        "sfx": "🍕 砰！BAM!",
        "story_tc": "火箭飛到一半，遇到了一陣會飛的披薩隕石雨！",
        "story_en": "Halfway to space, the rocket meets a storm of flying Pizza Meteors!",
        "choices": {
            "A": "🔥 噴出火鷹烈焰，把披薩烤成脆脆的餅乾！ (Use Firebird flames to bake them into crispy crackers!)", 
            "B": "💦 拿出超級大水槍，用水把披薩沖走！ (Use a giant water gun to wash the pizzas away!)", 
            "C": "🤤 張大嘴巴，一邊飛一邊把披薩全部吃掉！ (Open wide and EAT all the pizzas while flying!)"
        }
    },
    "2_B": {
        "title_tc": "第 2 頁：膠鴨大暴走！",
        "title_en": "Page 2: Rubber Duck Rampage!",
        "sfx": "🦆 呱呱！QUACK!",
        "story_tc": "超級膠鴨太重了，結果一屁股壓扁了外星人的果凍飛船！",
        "story_en": "The Super Rubber Duck is so heavy, it squashed the alien's jelly spaceship!",
        "choices": {
            "A": "💨 用力拍動翅膀，颳起大風吹走外星人！ (Flap wings hard to blow the aliens away!)", 
            "B": "🕶️ 戴上超酷墨鏡，假裝什麼事都沒發生！ (Wear cool sunglasses and pretend nothing happened!)", 
            "C": "🧴 噴出香噴噴的草莓香水讓外星人打噴嚏！ (Spray strawberry perfume to make them sneeze!)"
        }
    },
    "2_C": {
        "title_tc": "第 2 頁：紙皮箱裡的奇怪世界！",
        "title_en": "Page 2: The Weird Cardboard World!",
        "sfx": "📦 咻——！WHOOSH!",
        "story_tc": "紙皮箱飛到了外星花園，這裡有一隻戴著耳機的巨大青蛙在跳 Disco 舞！",
        "story_en": "The box lands in an alien garden. There is a giant frog wearing headphones dancing to Disco!",
        "choices": {
            "A": "🕺 跟青蛙一起跳舞，跳到牠頭暈！ (Dance with the frog until it gets dizzy!)", 
            "B": "🎤 搶走青蛙的麥克風，唱出超級難聽的歌嚇跑牠！ (Steal the microphone and sing terribly to scare it!)", 
            "C": "🪰 變出一隻超級大蒼蠅，讓青蛙追著蒼蠅跑！ (Create a giant fly so the frog chases it away!)"
        }
    },

    # Layer 3
    "3_A": {
        "title_tc": "第 3 頁：外星人的巨型扭蛋機",
        "title_en": "Page 3: The Giant Alien Capsule Machine",
        "story_tc": "火鷹俠發現所有的玩具都被關在一個像山一樣大的扭蛋機裡！",
        "story_en": "Firebird finds all the toys trapped inside a capsule machine as big as a mountain!",
        "choices": {
            "A": "🪙 變出一個超級巨大的硬幣投進去！ (Create a giant coin and put it in!)", 
            "B": "🔨 拿出神奇充氣大錘子，把扭蛋機敲開！ (Use a magic inflatable hammer to crack it open!)", 
            "C": "🤸‍♂️ 跳進扭蛋機裡，跟著玩具一起轉圈圈！ (Jump inside and spin around with the toys!)"
        }
    },
    "3_B": {
        "title_tc": "第 3 頁：黏呼呼棉花糖迷宮",
        "title_en": "Page 3: The Sticky Marshmallow Maze",
        "story_tc": "前面出現了一個白色的迷宮，牆壁居然是用黏黏的棉花糖做的！",
        "story_en": "Ahead is a white maze. The walls are made of sticky marshmallows!",
        "choices": {
            "A": "🧊 吐出冷凍氣息，把棉花糖全部凍硬！ (Breathe freezing air to make the marshmallows hard!)", 
            "B": "🧻 拿出一大卷超級保鮮紙，包住牆壁一路行！ (Take out giant plastic wrap to cover the walls!)", 
            "C": "🛹 拿出一塊滑板，在黏黏的牆壁上滑行！ (Use a skateboard to slide on the sticky walls!)"
        }
    },
    "3_C": {
        "title_tc": "第 3 頁：肚餓的怪獸",
        "title_en": "Page 3: The Hungry Monster",
        "story_tc": "大門口有一隻長了三個頭的怪獸，牠們一邊流口水一邊大叫肚子餓！",
        "story_en": "A three-headed monster is guarding the door, drooling and yelling that they are hungry!",
        "choices": {
            "A": "🥦 逼牠們吃最討厭的超級綠色西蘭花！ (Force them to eat the super green broccoli they hate!)", 
            "B": "🍔 變出三個無敵大漢堡塞住牠們的嘴！ (Create 3 mega burgers to stuff their mouths!)", 
            "C": "🤪 扮成一隻會跳舞的熱狗，把牠們引開！ (Dress up as a dancing hot dog and lure them away!)"
        }
    },

    # Layer 4 
    "4_A": {
        "title_tc": "第 4 頁：糖果大王出現！",
        "title_en": "Page 4: The Candy King Appears!",
        "story_tc": "扭蛋機打開了，外星人的首領「糖果大王」出現！他居然穿著一套超搞笑的香蕉人衣服！",
        "story_en": "The machine opens. The alien boss, 'Candy King', appears! He is wearing a hilarious banana suit!",
        "choices": {
            "A": "🤣 指著他的衣服哈哈大笑，笑到他覺得尷尬！ (Point at his suit and laugh so hard he blushes!)", 
            "B": "📸 拿出相機拍下他的搞笑樣子，準備給所有人看！ (Take a picture of his funny look to show everyone!)", 
            "C": "🍌 火鷹俠也變出一套蘋果人衣服，跟他進行「水果對決」！ (Firebird wears an apple suit for a fruit showdown!)"
        }
    },
    "4_B": {
        "title_tc": "第 4 頁：雪糕雪人軍團！",
        "title_en": "Page 4: Ice Cream Snowman Army!",
        "story_tc": "糖果大王揮揮手，召喚出 50 個用融化雪糕做的黏呼呼雪人來攻擊！",
        "story_en": "The King waves his hand and summons 50 sticky snowmen made of melted ice cream to attack!",
        "choices": {
            "A": "🔥 開啟火鷹加熱器，把雪人全部融化成糖水！ (Turn on the Firebird Heater to melt them into syrup!)", 
            "B": "🥄 拿出一支巨大的超級湯匙，把雪人全部吃光光！ (Take out a giant spoon and eat all the snowmen!)", 
            "C": "🍒 在他們頭上放上櫻桃，把他們變成美味的甜品！ (Put cherries on their heads and turn them into nice desserts!)"
        }
    },
    "4_C": {
        "title_tc": "第 4 頁：滑溜溜溜冰場",
        "title_en": "Page 4: The Slippery Ice Rink",
        "story_tc": "地板上灑滿了香蕉皮，變得超級滑！糖果大王滑著太空步衝過來了！",
        "story_en": "The floor is covered with banana peels, making it super slippery! The King moonwalks towards you!",
        "choices": {
            "A": "⛸️ 穿上火焰溜冰鞋，跟他比拼花式溜冰！ (Put on Flame Ice Skates and challenge him to figure skating!)", 
            "B": "🧲 啟動鞋底的超級磁鐵，穩穩地站在地上！ (Activate super magnets in your shoes to stand firmly!)", 
            "C": "🍌 踢出更多的香蕉皮，讓他滑個四腳朝天！ (Kick more banana peels so he slips and falls flat!)"
        }
    },

    # Layer 5 (Ultimate Move 終極絕招)
    "5_A": {
        "title_tc": "第 5 頁：發動搞笑絕招！(魔法系)",
        "title_en": "Page 5: Hilarious Ultimate Move! (Magic)",
        "story_tc": "糖果大王跌倒了！火鷹俠準備發動最厲害的搞笑絕招來淨化他！",
        "story_en": "The Candy King falls! Firebird gets ready to use his most hilarious ultimate move to purify him!",
        "choices": {
            "A": "🌈「—— 顏色沙漠土魔法 ！！！」 (Desert Sand of Color Magic!!!)", 
            "B": "✨「—— 超級痕癢羽毛雨 ！！！」 (Super Itchy Feather Rain!!!)", 
            "C": "🎈「—— 變成大氣球魔法 ！！！」 (Turn Into a Big Balloon Magic!!!)"
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：發動搞笑絕招！(物理系)",
        "title_en": "Page 5: Hilarious Ultimate Move! (Physical)",
        "story_tc": "糖果大王逃不掉了！火鷹俠積蓄能量，大叫一聲使出絕招：",
        "story_en": "The Candy King can't escape! Firebird charges up and shouts his ultimate move:",
        "choices": {
            "A": "🌈「—— 顏色沙漠土衝擊波 ！！！」 (Desert Sand of Color Shockwave!!!)", 
            "B": "💨「—— 無敵超級大風吹 ！！！」 (Invincible Super Wind Blow!!!)", 
            "C": "🥊「—— 搞笑百裂拳 ！！！」 (Hilarious Hundred Crack Fist!!!)"
        }
    },
    "5_C": {
        "title_tc": "第 5 頁：發動搞笑絕招！(食物系)",
        "title_en": "Page 5: Hilarious Ultimate Move! (Food)",
        "story_tc": "糖果大王舉手投降！火鷹俠決定請他吃一招美味的絕招：",
        "story_en": "The Candy King surrenders! Firebird decides to serve him a delicious ultimate move:",
        "choices": {
            "A": "🌈「—— 顏色沙漠土蛋糕 ！！！」 (Desert Sand of Color Cake!!!)", 
            "B": "🍔「—— 漢堡包大雪崩 ！！！」 (Hamburger Avalanche!!!)", 
            "C": "🍕「—— 飛天披薩滿天飛 ！！！」 (Flying Pizzas Everywhere!!!)"
        }
    },

    # Layer 6 (Ending)
    "6_A": {
        "title_tc": "第 6 頁：大結局！(彩色沙子結局)",
        "title_en": "Page 6: The End! (Color Sand Ending)",
        "story_tc": "絕招命中！外星人變成了五顏六色的沙子隨風飄走！所有玩具都安全找回來了，火鷹俠又拯救了世界！",
        "story_en": "Direct hit! The alien turns into colorful sand and blows away! All toys are saved. Firebird saved the world again!",
        "choices": {"A": "🎉 任務完成！帶著玩具去開派對！ (Mission Complete! Let's have a toy party!)"}
    },
    "6_B": {
        "title_tc": "第 6 頁：大結局！(超大風吹結局)",
        "title_en": "Page 6: The End! (Super Wind Ending)",
        "story_tc": "超級大風把外星人直接吹飛到了太陽系外面！玩具都得救了！大家笑到流眼淚！",
        "story_en": "The super wind blows the alien out of the solar system! Toys are saved! Everyone laughs until they cry!",
        "choices": {"A": "🎉 任務完成！跟小動物一起跳舞！ (Mission Complete! Dance with the animals!)"}
    },
    "6_C": {
        "title_tc": "第 6 頁：大結局！(肚皮脹脹結局)",
        "title_en": "Page 6: The End! (Full Tummy Ending)",
        "story_tc": "外星人吃到肚皮脹得像氣球，直接飄上了天空！大家拿回了玩具，還開了一個超級美食派對！",
        "story_en": "The alien's tummy gets so full it floats into the sky like a balloon! Everyone gets their toys back and throws a food party!",
        "choices": {"A": "🎉 任務完成！大家一齊食大餐！ (Mission Complete! Let's have a big feast!)"}
    }
}

# ----------------- 引擎邏輯 -----------------
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'story_history' not in st.session_state:
    st.session_state.story_history = []
if 'current_node' not in st.session_state:
    st.session_state.current_node = "1_START"

st.markdown('<p class="kids-title">🦸‍♂️ 火鷹俠 1：玩具星球大冒險 🦸‍♂️</p>', unsafe_allow_html=True)
st.markdown('<p class="en-title">Firebird Protection 1: Toy Planet Adventure</p>', unsafe_allow_html=True)
st.caption("雙語發聲版 | 為 Jarvis 量身打造的健康爆笑冒險")
st.markdown("---")

current_step = st.session_state.step
node_key = st.session_state.current_node

if current_step <= 6:
    stage = SCENES.get(node_key)
    
    if not stage:
        node_key = f"{current_step}_A"
        stage = SCENES[node_key]
        
    st.progress(current_step / 6, text=f"📖 故事進度 Story Progress：{current_step} / 6")
    
    st.markdown(f'<p class="kids-sfx">{stage["title_tc"]}<br><span style="font-size:1.2rem;">{stage["title_en"]}</span></p>', unsafe_allow_html=True)
    if "sfx" in stage:
        st.markdown(f'<p class="kids-sfx" style="color:#D32F2F !important;">{stage["sfx"]}</p>', unsafe_allow_html=True)
    
    # 🔊 TTS 發聲按鈕
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔊 聽中文故事 (Listen in Chinese)", key=f"tts_tc_{current_step}"):
            play_audio(stage["story_tc"], lang='zh-TW')
    with col2:
        if st.button("🔊 聽英文故事 (Listen in English)", key=f"tts_en_{current_step}"):
            play_audio(stage["story_en"], lang='en')

    st.markdown(f"""
    <div class="kids-speech-bubble">
    <p class="tc-story">💬 {stage["story_tc"]}</p>
    <p class="en-story">{stage["story_en"]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if current_step < 6:
        option_keys = list(stage["choices"].keys())
        option_texts = [f"{k}. {stage['choices'][k]}" for k in option_keys]
        
        selected_text = st.radio("👉 請 Jarvis 做出超搞笑抉擇 (Choose your action):", option_texts, key=f"radio_{current_step}")
        selected_letter = selected_text[0] 
        
        if st.button("🔥 確定！翻去下一頁！ (Next Page!)"):
            st.session_state.story_history.append((stage["title_tc"], selected_text))
            st.session_state.step += 1
            st.session_state.current_node = f"{st.session_state.step}_{selected_letter}"
            st.rerun()
    else:
        if st.button("🎉 看完了！印出專屬雙語故事書！ (Print Storybook!)"):
            st.session_state.story_history.append((stage["title_tc"], "故事圓滿結束！ The End!"))
            st.session_state.step += 1
            st.rerun()

else:
    st.balloons()
    st.success("🎉 恭喜！Jarvis 成功解鎖了爆笑雙語結局！ Congratulations!")
    
    st.header("🖼️ Jarvis 的專屬雙語故事繪本 (My Bilingual Storybook)")
    
    for i, (title, choice) in enumerate(st.session_state.story_history, 1):
        st.markdown(f"""
        <div class="comic-panel">
        <h2 style="font-size: 1.6rem; color: #00838F;">📖 {title}</h2>
        <p style="font-size: 1.3rem; color: #000000; font-weight: bold;"><b>💥 Jarvis 的行動 (Action)：</b><br>{choice}</p>
        </div>
        """, unsafe_allow_html=True)
        
    if st.button("🔄 再玩一次！探索其他結局！ (Play Again!)"):
        st.session_state.step = 1
        st.session_state.story_history = []
        st.session_state.current_node = "1_START"
        st.rerun()

st.markdown("---")
st.caption("🔥 Firebird Protection App 1 | Jarvis & Daddy Exclusive 雙語發聲版")
