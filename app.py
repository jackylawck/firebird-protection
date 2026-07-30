import streamlit as st

# 頁面配置
st.set_page_config(
    page_title="火鷹俠故事庫 | Firebird Protection",
    page_icon="🦸‍♂️",
    layout="centered"
)

# 🎨 雙語超大字體 & 完美側邊欄 CSS
st.markdown("""
    <style>
    /* 全局背景 */
    .stApp { background-color: #E0F7FA; color: #000000 !important; }
    
    /* 主介面文字 */
    p, span, label, div, h1, h2, h3, h4 { color: #000000 !important; font-family: 'Comic Sans MS', sans-serif; }
    .kids-title { font-size: 2.6rem !important; color: #00838F !important; font-weight: 900; text-align: center; margin-bottom: 5px; text-shadow: 2px 2px 0px #B2EBF2; }
    .en-title { font-size: 1.8rem !important; color: #006064 !important; font-weight: 900; text-align: center; margin-bottom: 15px; }
    .kids-sfx { font-size: 2rem !important; color: #E65100 !important; font-weight: 900; text-align: center; margin: 10px 0; }
    .kids-speech-bubble { background: #FFFFFF; border: 5px solid #000000; border-radius: 25px; padding: 25px; margin: 15px 0; box-shadow: 8px 8px 0px #000000; }
    .tc-story { font-size: 1.6rem !important; line-height: 1.6; font-weight: bold; margin-bottom: 15px; }
    .en-story { font-size: 1.3rem !important; line-height: 1.5; color: #37474F !important; font-style: italic; }
    
    /* 💥 側邊欄 (Sidebar) 背景與標題修復 */
    [data-testid="stSidebar"] {
        background-color: #1E293B !important;
    }
    [data-testid="stSidebar"] h2 {
        color: #FFEB3B !important;
        font-size: 1.5rem !important;
    }
    [data-testid="stSidebar"] label p {
        color: #000000 !important; /* 側邊欄選單文字為純黑色 */
        font-size: 1.05rem !important;
        font-weight: 900 !important;
    }
    
    /* 💥 修正 Selectbox (下拉選單) 隱形字問題 */
    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 3px solid #000000 !important;
        border-radius: 12px !important;
    }
    div[data-baseweb="select"] span {
        color: #000000 !important;
        font-weight: bold !important;
    }
    ul[data-baseweb="menu"] { background-color: #FFFFFF !important; }
    ul[data-baseweb="menu"] li { color: #000000 !important; font-weight: bold !important; font-size: 1.1rem !important; }

    /* Radio 選項樣式（主介面與側邊欄通用：白底黑字） */
    .stRadio label { font-size: 1.3rem !important; font-weight: bold !important; color: #000000 !important; padding: 8px 0; }
    .stRadio { background-color: #FFFFFF; padding: 15px; border: 4px solid #000000; border-radius: 20px; box-shadow: 6px 6px 0px #000000; margin-bottom: 20px; }
    .stRadio p { color: #000000 !important; }

    /* 按鈕樣式：黃色醒目底色 + 黑色文字 */
    div.stButton > button {
        background-color: #FFEB3B !important;
        color: #000000 !important;
        font-size: 1.4rem !important;
        font-weight: 900 !important;
        border: 4px solid #000000 !important;
        border-radius: 18px !important;
        padding: 12px 20px !important;
        box-shadow: 5px 5px 0px #000000 !important;
        width: 100% !important;
    }
    div.stButton > button:hover {
        background-color: #FFD600 !important;
        color: #000000 !important;
    }

    .comic-panel { background-color: #FFFFFF; border: 5px solid #000000; padding: 20px; margin-bottom: 20px; border-radius: 15px; box-shadow: 6px 6px 0px #FF9800; }
    </style>
""", unsafe_allow_html=True)

# ================= 故事 1：玩具星球大冒險 =================
STORY_1_SCENES = {
    "1_START": {
        "title_tc": "第 1 頁：玩具失竊大危機！", "title_en": "Page 1: The Great Toy Crisis!",
        "sfx": "🚨 嗚哇！WEE WOO!", "image": "https://images.pexels.com/photos/168866/pexels-photo-168866.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "大件事啦！「糖果外星人」偷走了全城小朋友最喜歡的玩具！火鷹俠必須去外星基地奪回玩具，他決定：",
        "story_en": "Oh no! The 'Candy Aliens' stole all the kids' favorite toys! Firebird must get them back. He decides to:",
        "choices": {"A": "🚀 坐上「超級彩虹推進火箭」飛上太空！ (Ride the Super Rainbow Rocket!)", "B": "🦆 召喚一隻跟大廈一樣高的「超級黃色膠鴨」！ (Summon a building-sized Super Rubber Duck!)", "C": "📦 跳進神奇紙皮箱，變成宇宙飛船！ (Jump into a magic cardboard box spaceship!)"}
    },
    "2_A": {
        "title_tc": "第 2 頁：會飛的披薩隕石！", "title_en": "Page 2: Flying Pizza Meteors!",
        "sfx": "🍕 砰！BAM!", "image": "https://images.pexels.com/photos/315755/pexels-photo-315755.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "火箭飛到一半，遇到了一陣會飛的披薩隕石雨！", "story_en": "Halfway to space, the rocket meets a storm of flying Pizza Meteors!",
        "choices": {"A": "🔥 噴出火鷹烈焰，把披薩烤成脆脆的餅乾！ (Use Firebird flames to bake them into crispy crackers!)", "B": "💦 拿出超級大水槍，用水把披薩沖走！ (Use a giant water gun to wash the pizzas away!)", "C": "🤤 張大嘴巴，一邊飛一邊把披薩全部吃掉！ (Open wide and EAT all the pizzas while flying!)"}
    },
    "2_B": {
        "title_tc": "第 2 頁：膠鴨大暴走！", "title_en": "Page 2: Rubber Duck Rampage!",
        "sfx": "🦆 呱呱！QUACK!", "image": "https://images.pexels.com/photos/1321151/pexels-photo-1321151.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "超級膠鴨太重了，結果一屁股壓扁了外星人的果凍飛船！", "story_en": "The Super Rubber Duck is so heavy, it squashed the alien's jelly spaceship!",
        "choices": {"A": "💨 用力拍動翅膀，颳起大風吹走外星人！ (Flap wings hard to blow the aliens away!)", "B": "🕶️ 戴上超酷墨鏡，假裝什麼事都沒發生！ (Wear cool sunglasses and pretend nothing happened!)", "C": "🧴 噴出香噴噴的草莓香水讓外星人打噴嚏！ (Spray strawberry perfume to make them sneeze!)"}
    },
    "2_C": {
        "title_tc": "第 2 頁：紙皮箱裡的奇怪世界！", "title_en": "Page 2: The Weird Cardboard World!",
        "sfx": "📦 咻——！WHOOSH!", "image": "https://images.pexels.com/photos/70083/frog-macro-amphibian-green-70083.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "紙皮箱飛到了外星花園，這裡有一隻戴著耳機的巨大青蛙在跳 Disco 舞！", "story_en": "The box lands in an alien garden. There is a giant frog wearing headphones dancing to Disco!",
        "choices": {"A": "🕺 跟青蛙一起跳舞，跳到牠頭暈！ (Dance with the frog until it gets dizzy!)", "B": "🎤 搶走青蛙的麥克風，唱出超級難聽的歌嚇跑牠！ (Steal the microphone and sing terribly to scare it!)", "C": "🪰 變出一隻超級大蒼蠅，讓青蛙追著蒼蠅跑！ (Create a giant fly so the frog chases it away!)"}
    },
    "3_A": {
        "title_tc": "第 3 頁：外星人的巨型扭蛋機", "title_en": "Page 3: The Giant Alien Capsule Machine",
        "sfx": "🎰 叮噹！DING DONG!", "image": "https://images.pexels.com/photos/163036/mario-luigi-yoshi-figures-163036.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "火鷹俠發現所有的玩具都被關在一個像山一樣大的扭蛋機裡！", "story_en": "Firebird finds all the toys trapped inside a capsule machine as big as a mountain!",
        "choices": {"A": "🪙 變出一個超級巨大的硬幣投進去！ (Create a giant coin and put it in!)", "B": "🔨 拿出神奇充氣大錘子，把扭蛋機敲開！ (Use a magic inflatable hammer to crack it open!)", "C": "🤸‍♂️ 跳進扭蛋機裡，跟著玩具一起轉圈圈！ (Jump inside and spin around with the toys!)"}
    },
    "3_B": {
        "title_tc": "第 3 頁：黏呼呼棉花糖迷宮", "title_en": "Page 3: The Sticky Marshmallow Maze",
        "sfx": "🍬 咕嚕！GLUG!", "image": "https://images.pexels.com/photos/1028714/pexels-photo-1028714.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "前面出現了一個白色的迷宮，牆壁居然是用黏黏的棉花糖做的！", "story_en": "Ahead is a white maze. The walls are made of sticky marshmallows!",
        "choices": {"A": "🧊 吐出冷凍氣息，把棉花糖全部凍硬！ (Breathe freezing air to make the marshmallows hard!)", "B": "🧻 拿出一大卷超級保鮮紙，包住牆壁一路行！ (Take out giant plastic wrap to cover the walls!)", "C": "🛹 拿出一塊滑板，在黏黏的牆壁上滑行！ (Use a skateboard to slide on the sticky walls!)"}
    },
    "3_C": {
        "title_tc": "第 3 頁：肚餓的怪獸", "title_en": "Page 3: The Hungry Monster",
        "sfx": "🍔 嗷嗚！NOM NOM!", "image": "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "大門口有一隻長了三個頭的怪獸，牠們一邊流口水一邊大叫肚子餓！", "story_en": "A three-headed monster is guarding the door, drooling and yelling that they are hungry!",
        "choices": {"A": "🥦 逼牠們吃最討厭的超級綠色西蘭花！ (Force them to eat the super green broccoli they hate!)", "B": "🍔 變出三個無敵大漢堡塞住牠們的嘴！ (Create 3 mega burgers to stuff their mouths!)", "C": "🤪 扮成一隻會跳舞的熱狗，把牠們引開！ (Dress up as a dancing hot dog and lure them away!)"}
    },
    "4_A": {
        "title_tc": "第 4 頁：糖果大王出現！", "title_en": "Page 4: The Candy King Appears!",
        "sfx": "🍌 哈哈！HAHA!", "image": "https://images.pexels.com/photos/2872755/pexels-photo-2872755.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "扭蛋機打開了，外星人的首領「糖果大王」出現！他居然穿著一套超搞笑的香蕉人衣服！", "story_en": "The machine opens. The alien boss, 'Candy King', appears! He is wearing a hilarious banana suit!",
        "choices": {"A": "🤣 指著他的衣服哈哈大笑，笑到他覺得尷尬！ (Point at his suit and laugh so hard he blushes!)", "B": "📸 拿出相機拍下他的搞笑樣子，準備給所有人看！ (Take a picture of his funny look to show everyone!)", "C": "🍌 火鷹俠也變出一套蘋果人衣服，跟他進行「水果對決」！ (Firebird wears an apple suit for a fruit showdown!)"}
    },
    "4_B": {
        "title_tc": "第 4 頁：雪糕雪人軍團！", "title_en": "Page 4: Ice Cream Snowman Army!",
        "sfx": "🍦 呼呼！BRRR!", "image": "https://images.pexels.com/photos/1362534/pexels-photo-1362534.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "糖果大王揮揮手，召喚出 50 個用融化雪糕做的黏呼呼雪人來攻擊！", "story_en": "The King waves his hand and summons 50 sticky snowmen made of melted ice cream to attack!",
        "choices": {"A": "🔥 開啟火鷹加熱器，把雪人全部融化成糖水！ (Turn on the Firebird Heater to melt them into syrup!)", "B": "🥄 拿出一支巨大的超級湯匙，把雪人全部吃光光！ (Take out a giant spoon and eat all the snowmen!)", "C": "🍒 在他們頭上放上櫻桃，把他們變成美味的甜品！ (Put cherries on their heads and turn them into nice desserts!)"}
    },
    "4_C": {
        "title_tc": "第 4 頁：滑溜溜溜冰場", "title_en": "Page 4: The Slippery Ice Rink",
        "sfx": "🍌 哎呀！WHOOPS!", "image": "https://images.pexels.com/photos/1093837/pexels-photo-1093837.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "地板上灑滿了香蕉皮，變得超級滑！糖果大王滑著太空步衝過來了！", "story_en": "The floor is covered with banana peels, making it super slippery! The King moonwalks towards you!",
        "choices": {"A": "⛸️ 穿上火焰溜冰鞋，跟他比拼花式溜冰！ (Put on Flame Ice Skates and challenge him to figure skating!)", "B": "🧲 啟動鞋底的超級磁鐵，穩穩地站在地上！ (Activate super magnets in your shoes to stand firmly!)", "C": "🍌 踢出更多的香蕉皮，讓他滑個四腳朝天！ (Kick more banana peels so he slips and falls flat!)"}
    },
    "5_A": {
        "title_tc": "第 5 頁：發動搞笑絕招！(魔法系)", "title_en": "Page 5: Hilarious Ultimate Move! (Magic)",
        "sfx": "✨ 閃閃！SPARKLE!", "image": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop",
        "story_tc": "糖果大王跌倒了！火鷹俠準備發動最厲害的搞笑絕招來淨化他！", "story_en": "The Candy King falls! Firebird gets ready to use his most hilarious ultimate move to purify him!",
        "choices": {"A": "🌈「—— 顏色沙漠土魔法 ！！！」 (Desert Sand of Color Magic!!!)", "B": "✨「—— 超級痕癢羽毛雨 ！！！」 (Super Itchy Feather Rain!!!)", "C": "🎈「—— 變成大氣球魔法 ！！！」 (Turn Into a Big Balloon Magic!!!)"}
    },
    "5_B": {
        "title_tc": "第 5 頁：發動搞笑絕招！(物理系)", "title_en": "Page 5: Hilarious Ultimate Move! (Physical)",
        "sfx": "💨 咻——！BOOM!", "image": "https://images.unsplash.com/photo-1509114397022-ed747cca3f65?w=800&auto=format&fit=crop",
        "story_tc": "糖果大王逃不掉了！火鷹俠積蓄能量，大叫一聲使出絕招：", "story_en": "The Candy King can't escape! Firebird charges up and shouts his ultimate move:",
        "choices": {"A": "🌈「—— 顏色沙漠土衝擊波 ！！！」 (Desert Sand of Color Shockwave!!!)", "B": "💨「—— 無敵超級大風吹 ！！！」 (Invincible Super Wind Blow!!!)", "C": "🥊「—— 搞笑百裂拳 ！！！」 (Hilarious Hundred Crack Fist!!!)"}
    },
    "5_C": {
        "title_tc": "第 5 頁：發動搞笑絕招！(食物系)", "title_en": "Page 5: Hilarious Ultimate Move! (Food)",
        "sfx": "🍰 咕嚕！YUMMY!", "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=800&auto=format&fit=crop",
        "story_tc": "糖果大王舉手投降！火鷹俠決定請他吃一招美味的絕招：", "story_en": "The Candy King surrenders! Firebird decides to serve him a delicious ultimate move:",
        "choices": {"A": "🌈「—— 顏色沙漠土蛋糕 ！！！」 (Desert Sand of Color Cake!!!)", "B": "🍔「—— 漢堡包大雪崩 ！！！」 (Hamburger Avalanche!!!)", "C": "🍕「—— 飛天披薩滿天飛 ！！！」 (Flying Pizzas Everywhere!!!)"}
    },
    "6_A": {
        "title_tc": "第 6 頁：大結局！(彩色沙子結局)", "title_en": "Page 6: The End! (Color Sand Ending)",
        "sfx": "🎉 耶！HOORAY!", "image": "https://images.pexels.com/photos/1078850/pexels-photo-1078850.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "絕招命中！外星人變成了五顏六色的沙子隨風飄走！所有玩具都安全找回來了，火鷹俠又拯救了世界！", "story_en": "Direct hit! The alien turns into colorful sand and blows away! All toys are saved. Firebird saved the world again!",
        "choices": {"A": "🎉 任務完成！帶著玩具去開派對！ (Mission Complete! Let's have a toy party!)"}
    },
    "6_B": {
        "title_tc": "第 6 頁：大結局！(超大風吹結局)", "title_en": "Page 6: The End! (Super Wind Ending)",
        "sfx": "🌬️ 吹走啦！BYE BYE!", "image": "https://images.pexels.com/photos/1563256/pexels-photo-1563256.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "超級大風把外星人直接吹飛到了太陽系外面！玩具都得救了！大家笑到流眼淚！", "story_en": "The super wind blows the alien out of the solar system! Toys are saved! Everyone laughs until they cry!",
        "choices": {"A": "🎉 任務完成！跟小動物一起跳舞！ (Mission Complete! Dance with the animals!)"}
    },
    "6_C": {
        "title_tc": "第 6 頁：大結局！(肚皮脹脹結局)", "title_en": "Page 6: The End! (Full Tummy Ending)",
        "sfx": "🎈 飄上天！FLOATING!", "image": "https://images.pexels.com/photos/1543762/pexels-photo-1543762.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "外星人吃到肚皮脹得像氣球，直接飄上了天空！大家拿回了玩具，還開了一個超級美食派對！", "story_en": "The alien's tummy gets so full it floats into the sky like a balloon! Everyone gets their toys back and throws a food party!",
        "choices": {"A": "🎉 任務完成！大家一齊食大餐！ (Mission Complete! Let's have a big feast!)"}
    }
}

# ================= 故事 2：恐龍樂園大暴走 =================
STORY_2_SCENES = {
    "1_START": {
        "title_tc": "第 1 頁：恐龍大暴走！", "title_en": "Page 1: Dinosaur Rampage!",
        "sfx": "🦖 吼吼！ROAR!", "image": "https://images.pexels.com/photos/12105156/pexels-photo-12105156.jpeg?auto=compress&cs=tinysrgb&w=800", # 恐龍玩具
        "story_tc": "不好了！主題樂園的調皮暴龍偷走了園長的「超級金盃」！火鷹俠要入去樂園找回金盃，他決定：",
        "story_en": "Oh no! The cheeky T-Rex at the theme park stole the 'Super Golden Trophy'! Firebird must get it back. He decides to:",
        "choices": {"A": "🚀 啟動「超級火箭推進器」直接飛進樂園！ (Use Super Rocket Boosters to fly in!)", "B": "🤖 騎上一隻「超級機械三角龍」衝進去！ (Ride a Super Robot Triceratops!)", "C": "🏀 變成一個巨大的彈彈球，彈過樂園大門！ (Turn into a giant bouncy ball and bounce over the gate!)"}
    },
    "2_A": {
        "title_tc": "第 2 頁：長頸龍的噴水攻擊！", "title_en": "Page 2: Brachiosaurus Water Attack!",
        "sfx": "💦 嘩啦！SPLASH!", "image": "https://images.pexels.com/photos/8009210/pexels-photo-8009210.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "飛到一半，一隻超巨大的長頸龍以為你是蟲子，噴出大水柱攻擊你！", "story_en": "Halfway there, a giant Brachiosaurus thinks you are a bug and sprays a huge water column at you!",
        "choices": {"A": "🛡️ 打開防護傘，把水全部擋住！ (Open a shield umbrella to block the water!)", "B": "🧼 拿出超級肥皂，趁機洗個泡泡浴！ (Take out super soap and take a bubble bath!)", "C": "🦅 發揮超快速度，在水柱之間穿梭閃避！ (Use super speed to dodge between the water!)"}
    },
    "2_B": {
        "title_tc": "第 2 頁：機械三角龍沒電了！", "title_en": "Page 2: Robot Triceratops Out of Battery!",
        "sfx": "🪫 嗶嗶... BEEP...", "image": "https://images.pexels.com/photos/255567/pexels-photo-255567.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "衝到一半，機械三角龍的電池用光了，停在路中間！", "story_en": "Halfway there, the robot Triceratops runs out of battery and stops in the middle of the road!",
        "choices": {"A": "⚡ 發射火鷹閃電，幫三角龍極速充電！ (Shoot Firebird Lightning to fast-charge it!)", "B": "🥕 拿出一根巨大的機械蘿蔔，引誘牠繼續走！ (Use a giant robot carrot to lure it!)", "C": "🏃‍♂️ 跳下來自己跑，順便做運動！ (Jump off and run by yourself for some exercise!)"}
    },
    "2_C": {
        "title_tc": "第 2 頁：彈進翼龍的鳥巢！", "title_en": "Page 2: Bounced into a Pterodactyl Nest!",
        "sfx": "🪺 哎呀！OUCH!", "image": "https://images.unsplash.com/photo-1590494444558-888e2858b92b?w=800&auto=format&fit=crop",
        "story_tc": "彈彈球彈得太高，竟然掉進了懸崖上的翼龍鳥巢裡！", "story_en": "The bouncy ball went too high and landed right inside a Pterodactyl nest on the cliff!",
        "choices": {"A": "🥚 假裝自己是一顆巨大的恐龍蛋，保持安靜！ (Pretend to be a giant dino egg and stay quiet!)", "B": "🎤 大聲唱歌，把翼龍嚇得飛走！ (Sing loudly to scare the Pterodactyl away!)", "C": "🪂 拿出降落傘，直接跳下懸崖！ (Take out a parachute and jump off the cliff!)"}
    },
    "3_A": {
        "title_tc": "第 3 頁：遇到暴龍！", "title_en": "Page 3: Meeting the T-Rex!",
        "sfx": "🦖 吼吼！ROAR!", "image": "https://images.pexels.com/photos/12028682/pexels-photo-12028682.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "終於找到了調皮的暴龍！他拿著金盃，張開大嘴巴大吼！", "story_en": "Finally found the cheeky T-Rex! He holds the trophy and roars with a wide open mouth!",
        "choices": {"A": "🦷 拿出一支巨大的牙刷，幫暴龍刷牙！ (Take out a giant toothbrush and brush his teeth!)", "B": "💪 擺出最威武的英雄姿勢，嚇唬他！ (Strike the most powerful hero pose to scare him!)", "C": "🍖 變出一塊無敵大雞腿丟給他吃！ (Create a mega chicken drumstick and throw it to him!)"}
    },
    "3_B": {
        "title_tc": "第 3 頁：泥漿沼澤擋路！", "title_en": "Page 3: Mud Swamp Blocks the Way!",
        "sfx": "💩 噗滋！SQUISH!", "image": "https://images.unsplash.com/photo-1500468756762-a401b6f17b46?w=800&auto=format&fit=crop",
        "story_tc": "暴龍逃進了泥漿沼澤，泥漿黏呼呼的，根本走不過去！", "story_en": "The T-Rex escapes into a mud swamp. The mud is so sticky, you can't walk through!",
        "choices": {"A": "🔥 噴出高溫烈焰，把泥漿全部烤乾變成硬地！ (Breathe fire to bake the mud into hard ground!)", "B": "🚁 頭頂變出直升機螺旋槳，飛過去！ (Grow a helicopter propeller on your head and fly over!)", "C": "🐸 穿上超級青蛙鞋，在泥漿上跳來跳去！ (Put on Super Frog Shoes and jump across!)"}
    },
    "3_C": {
        "title_tc": "第 3 頁：恐龍在跳舞？", "title_en": "Page 3: Dancing Dinosaurs?",
        "sfx": "🕺 咚咚！BUMP BUMP!", "image": "https://images.unsplash.com/photo-1540324155974-7523202daa3f?w=800&auto=format&fit=crop",
        "story_tc": "奇怪！樂園裡的恐龍竟然全部排好隊，在跳搞笑的扭屁股舞！", "story_en": "Weird! All the dinosaurs in the park are lined up, dancing a hilarious butt-wiggling dance!",
        "choices": {"A": "🕵️‍♂️ 拿出放大鏡，找出是誰在背後搞鬼！ (Take out a magnifying glass to find who is behind this!)", "B": "🕺 加入他們一起扭屁股，趁機混進去！ (Join the butt-wiggling dance to sneak in!)", "C": "🎺 吹響巨大的喇叭，打破他們的節奏！ (Blow a giant trumpet to break their rhythm!)"}
    },
    "4_A": {
        "title_tc": "第 4 頁：搗蛋魔法師現身！", "title_en": "Page 4: The Cheeky Wizard Appears!",
        "sfx": "🪄 嘻嘻！HEE HEE!", "image": "https://images.pexels.com/photos/15506048/pexels-photo-15506048.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "原來是一隻戴著高帽子的「搗蛋魔法師」控制了恐龍，他還搶走了金盃！", "story_en": "It turns out a 'Cheeky Wizard' in a tall hat controlled the dinos, and he took the trophy!",
        "choices": {"A": "🎩 用火鷹烈焰燒掉他的帽子！ (Use Firebird flames to burn his hat!)", "B": "🪞 拿出反射鏡，把他的魔法全部反彈！ (Take out a mirror to reflect all his magic!)", "C": "🤪 對他做一個超級醜的鬼臉，嚇他一跳！ (Make a super ugly funny face to scare him!)"}
    },
    "4_B": {
        "title_tc": "第 4 頁：水果流星雨！", "title_en": "Page 4: Fruit Meteor Shower!",
        "sfx": "🍎 砰砰！BAM BAM!", "image": "https://images.pexels.com/photos/1128678/pexels-photo-1128678.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "魔法師揮動魔杖，天空中掉下了無數巨大的蘋果和西瓜！", "story_en": "The Wizard waves his wand, and countless giant apples and watermelons fall from the sky!",
        "choices": {"A": "⚔️ 拿出火鷹雙劍，把水果全部切成水果沙律！ (Use twin swords to slice them into a fruit salad!)", "B": "🛡️ 打開防護罩，讓水果全部彈開！ (Open a shield to bounce all the fruits away!)", "C": "😋 張開嘴巴，把它們全部吃進肚子裡！ (Open your mouth and eat them all!)"}
    },
    "4_C": {
        "title_tc": "第 4 頁：魔法師滑倒了！", "title_en": "Page 4: The Wizard Slips!",
        "sfx": "🍌 哎呀！OOPS!", "image": "https://images.pexels.com/photos/1093837/pexels-photo-1093837.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "魔法師跑得太快，踩到香蕉皮滑個四腳朝天，金盃飛到了半空中！", "story_en": "The Wizard runs too fast, slips on a banana peel, and the trophy flies into the air!",
        "choices": {"A": "🦅 展開翅膀，以最快速度衝過去接住金盃！ (Spread wings and fly at top speed to catch the trophy!)", "B": "🕸️ 發射超級蜘蛛網，把金盃黏回來！ (Shoot a super spider web to pull the trophy back!)", "C": "🛏️ 變出一張柔軟的大床，讓金盃安全掉在上面！ (Create a soft bed for the trophy to land safely!)"}
    },
    "5_A": {
        "title_tc": "第 5 頁：發動搞笑絕招！(魔法系)", "title_en": "Page 5: Hilarious Ultimate Move! (Magic)",
        "sfx": "✨ 閃閃！SPARKLE!", "image": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop",
        "story_tc": "魔法師跌倒了！火鷹俠準備發動最厲害的搞笑絕招來收服他！", "story_en": "The Wizard falls! Firebird gets ready to use his most hilarious ultimate move to capture him!",
        "choices": {"A": "🦆「—— 變成黃色小鴨魔法 ！！！」 (Turn Into Yellow Ducks Magic!!!)", "B": "✨「—— 超級開心跳舞雨 ！！！」 (Super Happy Dancing Rain!!!)", "C": "🎈「—— 變成大氣球魔法 ！！！」 (Turn Into a Big Balloon Magic!!!)"}
    },
    "5_B": {
        "title_tc": "第 5 頁：發動搞笑絕招！(物理系)", "title_en": "Page 5: Hilarious Ultimate Move! (Physical)",
        "sfx": "💨 咻——！BOOM!", "image": "https://images.unsplash.com/photo-1509114397022-ed747cca3f65?w=800&auto=format&fit=crop",
        "story_tc": "魔法師無路可逃！火鷹俠深呼吸，大叫一聲使出絕招：", "story_en": "The Wizard has nowhere to run! Firebird takes a deep breath and shouts his ultimate move:",
        "choices": {"A": "🌪️「—— 無敵超級大風吹 ！！！」 (Invincible Super Wind Blow!!!)", "B": "🤧「—— 火鷹俠超級大噴嚏 ！！！」 (Firebird Super Giant Sneeze!!!)", "C": "🥊「—— 搞笑百裂拳 ！！！」 (Hilarious Hundred Crack Fist!!!)"}
    },
    "5_C": {
        "title_tc": "第 5 頁：發動搞笑絕招！(食物系)", "title_en": "Page 5: Hilarious Ultimate Move! (Food)",
        "sfx": "🍉 咕嚕！YUMMY!", "image": "https://images.unsplash.com/photo-1587049352847-4d4b137a5b3a?w=800&auto=format&fit=crop",
        "story_tc": "魔法師舉手投降！火鷹俠決定請他吃一招美味的絕招：", "story_en": "The Wizard surrenders! Firebird decides to serve him a delicious ultimate move:",
        "choices": {"A": "🍉「—— 巨大西瓜大雪崩 ！！！」 (Giant Watermelon Avalanche!!!)", "B": "🍦「—— 雪糕山鎮壓 ！！！」 (Ice Cream Mountain Crush!!!)", "C": "🍩「—— 甜甜圈金鋼圈 ！！！」 (Donut Golden Ring Trap!!!)"}
    },
    "6_A": {
        "title_tc": "第 6 頁：大結局！(小鴨結局)", "title_en": "Page 6: The End! (Duck Ending)",
        "sfx": "🦆 呱呱！QUACK!", "image": "https://images.pexels.com/photos/1321151/pexels-photo-1321151.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "絕招命中！魔法師和可怕的暴龍全部變成了可愛的黃色小鴨！火鷹俠成功奪回超級金盃，拯救了恐龍樂園！", "story_en": "Direct hit! The Wizard and T-Rex all turn into cute yellow ducks! Firebird got the trophy back and saved the park!",
        "choices": {"A": "🎉 任務完成！帶小鴨回家洗澡！ (Mission Complete! Take the ducks home for a bath!)"}
    },
    "6_B": {
        "title_tc": "第 6 頁：大結局！(大噴嚏結局)", "title_en": "Page 6: The End! (Sneeze Ending)",
        "sfx": "🌬️ 吹走啦！BYE BYE!", "image": "https://images.pexels.com/photos/1563256/pexels-photo-1563256.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "超級大噴嚏把魔法師直接吹飛到了月球上！恐龍們恢復了清醒，開心得圍著火鷹俠跳舞！", "story_en": "The super sneeze blows the Wizard to the moon! The dinos wake up and dance happily around Firebird!",
        "choices": {"A": "🎉 任務完成！跟恐龍一起跳舞！ (Mission Complete! Dance with the dinosaurs!)"}
    },
    "6_C": {
        "title_tc": "第 6 頁：大結局！(大食會結局)", "title_en": "Page 6: The End! (Food Party Ending)",
        "sfx": "🍉 好飽！FULL!", "image": "https://images.pexels.com/photos/1543762/pexels-photo-1543762.jpeg?auto=compress&cs=tinysrgb&w=800",
        "story_tc": "魔法師和恐龍吃到肚皮脹得像氣球，完全動不了！大家拿回了金盃，還在樂園開了一個超級美食派對！", "story_en": "The Wizard and dinos get so full they can't move! Everyone gets the trophy and throws a food party!",
        "choices": {"A": "🎉 任務完成！大家一齊食大餐！ (Mission Complete! Let's have a big feast!)"}
    }
}

# 集合所有故事
STORIES = {
    "Story1": {
        "name": "📕 火鷹俠 1：玩具星球大冒險",
        "nodes": STORY_1_SCENES
    },
    "Story2": {
        "name": "📘 火鷹俠 2：恐龍樂園大暴走",
        "nodes": STORY_2_SCENES
    }
}

# ================= 引擎邏輯與狀態管理 =================
if 'current_story' not in st.session_state:
    st.session_state.current_story = "Story1"
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'story_history' not in st.session_state:
    st.session_state.story_history = []
if 'current_node' not in st.session_state:
    st.session_state.current_node = "1_START"

# 🚩 側邊欄（Sidebar）
st.sidebar.markdown("## 📚 選擇故事 (Select Story)")
story_options = {k: v["name"] for k, v in STORIES.items()}
selected_story_name = st.sidebar.selectbox("今日想聽邊個故事？ (Which story today?)", list(story_options.values()))

# 如果切換了故事，重置所有進度
selected_story_key = [k for k, v in story_options.items() if v == selected_story_name][0]
if st.session_state.current_story != selected_story_key:
    st.session_state.current_story = selected_story_key
    st.session_state.step = 1
    st.session_state.story_history = []
    st.session_state.current_node = "1_START"
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("## 📖 快速跳頁 (Jump to Page)")
page_options = [
    "第 1 頁 (Page 1)", "第 2 頁 (Page 2)", "第 3 頁 (Page 3)", 
    "第 4 頁 (Page 4)", "第 5 頁 (Page 5)", "第 6 頁 (Page 6)"
]

selected_page_str = st.sidebar.radio("選擇頁數 (Select Page)：", page_options, index=st.session_state.step - 1, key="sidebar_jump_radio")
jump_page_num = page_options.index(selected_page_str) + 1

if st.sidebar.button("🚀 跳轉到此頁 (Jump Now)"):
    st.session_state.step = jump_page_num
    if jump_page_num == 1:
        st.session_state.current_node = "1_START"
    else:
        st.session_state.current_node = f"{jump_page_num}_A" # 預設切換至 A 路線
    st.rerun()

st.sidebar.markdown("---")
if st.sidebar.button("🔄 重頭開始 (Start Over)"):
    st.session_state.step = 1
    st.session_state.story_history = []
    st.session_state.current_node = "1_START"
    st.rerun()

# ================= 主介面渲染 =================
CURRENT_SCENES = STORIES[st.session_state.current_story]["nodes"]
story_title = STORIES[st.session_state.current_story]["name"]
story_title_en = "Firebird Protection 1: Toy Planet" if "1" in story_title else "Firebird Protection 2: Dinosaur Park"

st.markdown(f'<p class="kids-title">🦸‍♂️ {story_title} 🦸‍♂️</p>', unsafe_allow_html=True)
st.markdown(f'<p class="en-title">{story_title_en}</p>', unsafe_allow_html=True)
st.caption("Son & Dad Exclusive | 雙語爆笑繪本 App (Bilingual Comic App)")
st.markdown("---")

current_step = st.session_state.step
node_key = st.session_state.current_node

if current_step <= 6:
    stage = CURRENT_SCENES.get(node_key)
    
    # 容錯處理
    if not stage:
        node_key = f"{current_step}_A"
        stage = CURRENT_SCENES[node_key]
        
    st.progress(current_step / 6, text=f"📖 故事進度 Story Progress：{current_step} / 6")
    
    st.markdown(f'<p class="kids-sfx">{stage["title_tc"]}<br><span style="font-size:1.1rem;">{stage["title_en"]}</span></p>', unsafe_allow_html=True)
    if "sfx" in stage:
        st.markdown(f'<p class="kids-sfx" style="color:#D32F2F !important;">{stage["sfx"]}</p>', unsafe_allow_html=True)

    if "image" in stage:
        st.image(stage["image"], use_column_width=True)

    st.markdown(f"""
    <div class="kids-speech-bubble">
    <p class="tc-story">💬 {stage["story_tc"]}</p>
    <p class="en-story">{stage["story_en"]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if current_step < 6:
        option_keys = list(stage["choices"].keys())
        option_texts = [f"{k}. {stage['choices'][k]}" for k in option_keys]
        
        selected_text = st.radio("👉 請做出超搞笑抉擇 (Choose your action):", option_texts, key=f"radio_{st.session_state.current_story}_{current_step}")
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
    st.success("🎉 恭喜！成功解鎖了爆笑雙語結局！ Congratulations!")
    
    st.header("🖼️ 專屬雙語故事繪本 (Our Bilingual Storybook)")
    
    for i, (title, choice) in enumerate(st.session_state.story_history, 1):
        st.markdown(f"""
        <div class="comic-panel">
        <h2 style="font-size: 1.6rem; color: #00838F;">📖 {title}</h2>
        <p style="font-size: 1.3rem; color: #000000; font-weight: bold;"><b>💥 我們的行動 (Action)：</b><br>{choice}</p>
        </div>
        """, unsafe_allow_html=True)
        
    if st.button("🔄 再玩一次！探索其他結局！ (Play Again!)"):
        st.session_state.step = 1
        st.session_state.story_history = []
        st.session_state.current_node = "1_START"
        st.rerun()

st.markdown("---")
st.caption("🔥 Firebird Protection App | Son & Dad Exclusive 雙語純淨版")
