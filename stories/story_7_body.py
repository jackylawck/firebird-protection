# ==============================================================================
# 🔬 火鷹俠 7：微觀人體大探險 (Microscopic Body Adventure)
# 融入 PERCCI 品格 (同理心、勇氣) + KLA (科學教育、體育與健康、人文)
# ==============================================================================

STORY_INFO = {
    "id": "Story7",
    "name_tc": "🔬 火鷹俠 7：微觀人體大探險",
    "name_en": "Firebird 7: Microscopic Body Adventure"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：巨人波波生病了！", "title_en": "Page 1: Giant Bobo is Sick!",
        "sfx": "🤧 哈啾！ACHOO!",
        "story_tc": "大事不好了！好朋友「巨人波波」感染了可怕的「哈啾病毒」，發高燒躺在床上。火鷹俠決定進入波波的身體裡，幫他打敗病毒：",
        "story_en": "Oh no! Good friend Giant Bobo caught the terrible 'Achoo Virus' and is in bed with a fever. Firebird decides to enter his body to defeat the virus:",
        "choices": {
            "A": {"text": "🔦 走進「超級縮小隧道」，把自己縮小到像螞蟻一樣！ (Walk into the Super Shrink Tunnel and become as small as an ant!)", "next": "2_A", "effect": {"creativity": 1, "bravery": 1}, "kla": ["TECH", "SCIENCE"], "is_bad": False},
            "B": {"text": "💊 變身成一顆「無敵維他命膠囊」，讓波波吞下去！ (Transform into an Invincible Vitamin Capsule for Bobo to swallow!)", "next": "2_B", "effect": {"empathy": 1}, "kla": ["PE", "SCIENCE"], "is_bad": False},
            "C": {"text": "🏃‍♂️ 不縮小，直接捏著鼻子跳進波波的嘴巴裡！ (Don't shrink, just pinch your nose and jump into his mouth!)", "next": "BAD_END_SHRINK", "effect": {"bravery": -1}, "kla": ["SCIENCE"], "is_bad": True,
                  "bad_reason": "你太大了，卡在波波的喉嚨裡，讓他咳得更厲害！做科學探險必須做好準備。任務失敗……\n(You are too big and got stuck in his throat, making him cough more! Mission failed...)"}
        }
    },

    # ===== 分支 A：血管與白血球路線 =====
    "2_A": {
        "title_tc": "第 2 頁：沉睡的白血球守衛", "title_en": "Page 2: The Sleepy White Blood Cells",
        "sfx": "💤 呼嚕... ZZZ...",
        "story_tc": "你來到了波波的血管裡，卻發現負責抵抗病毒的「白血球守衛」們因為太累，全都睡著了！火鷹俠決定：",
        "story_en": "You arrive in Bobo's blood vessels, but the 'White Blood Cell Guards' are so tired they fell asleep! Firebird decides to:",
        "choices": {
            "A": {"text": "🎵 播放充滿活力的健康早操音樂，叫醒他們一起做運動！ (Play energetic morning exercise music to wake them up for a workout!)", "next": "3_A", "effect": {"creativity": 1, "empathy": 1}, "kla": ["PE", "ARTS"], "is_bad": False},
            "B": {"text": "🍎 分發超級水果，給守衛們補充維他命能量！ (Distribute super fruits to give the guards vitamin energy!)", "next": "3_A", "effect": {"empathy": 2}, "kla": ["SCIENCE", "PE"], "is_bad": False},
            "C": {"text": "😡 大聲責罵守衛偷懶，命令他們馬上起床！ (Scold the guards loudly and order them to wake up!)", "next": "BAD_END_SCOLD", "effect": {"empathy": -2}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "生病時細胞已經很虛弱了，責罵只會讓他們更沒有力氣！我們需要同理心。任務失敗……\n(Cells are weak when sick. Scolding drains their energy! We need empathy. Mission failed...)"}
        }
    },

    # ===== 分支 B：喉嚨滑水道路線 =====
    "2_B": {
        "title_tc": "第 2 頁：喉嚨滑水道大冒險", "title_en": "Page 2: Throat Waterslide Adventure",
        "sfx": "🌊 嘩啦！SPLASH!",
        "story_tc": "你像坐過山車一樣滑進波波的喉嚨，但這裡非常滑，還有陣陣的咳嗽狂風！火鷹俠運用 STEAM 知識：",
        "story_en": "You slide down Bobo's throat like a rollercoaster, but it's slippery with coughing wind storms! Firebird uses STEAM:",
        "choices": {
            "A": {"text": "🧲 啟動鞋底的「電磁吸盤」，穩穩地吸在喉嚨壁上！ (Activate electromagnetic suction shoes to stick firmly to the wall!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["TECH", "SCIENCE"], "is_bad": False},
            "B": {"text": "🪂 打開特製的減震降落傘，順著咳嗽的風慢慢降落！ (Open a shock-absorbing parachute and glide down with the coughing wind!)", "next": "3_A", "effect": {"bravery": 1}, "kla": ["SCIENCE"], "is_bad": False}
        }
    },

    # ===== 第 3 頁匯合 =====
    "3_A": {
        "title_tc": "第 3 頁：遇見哈啾病毒", "title_en": "Page 3: Meeting the Achoo Virus",
        "sfx": "👾 嘻嘻！HEE HEE!",
        "story_tc": "你終於找到了「哈啾病毒」！它正一邊吃著炸薯條和糖果，一邊分裂出更多小病毒。火鷹俠決定：",
        "story_en": "You found the 'Achoo Virus'! It is eating fries and candy while splitting into more mini-viruses. Firebird decides to:",
        "choices": {
            "A": {"text": "🥦 變出巨大的西蘭花和胡蘿蔔盾牌，擋住它的攻擊！ (Create a giant broccoli and carrot shield to block its attacks!)", "next": "4_A", "effect": {"creativity": 1, "bravery": 1}, "kla": ["PE", "SCIENCE"], "is_bad": False},
            "B": {"text": "🏃‍♂️ 挑戰它進行一場短跑比賽，消耗它的體力！ (Challenge it to a sprint race to drain its energy!)", "next": "4_A", "effect": {"bravery": 2}, "kla": ["PE"], "is_bad": False},
            "C": {"text": "🍩 丟給它更多甜甜圈，希望它吃飽了就會離開！ (Throw more donuts at it, hoping it will leave when full!)", "next": "BAD_END_JUNKFOOD", "effect": {"creativity": -1}, "kla": ["SCIENCE", "PE"], "is_bad": True,
                  "bad_reason": "大錯特錯！吃太多不健康的零食只會讓病毒變得更強壯！任務失敗……\n(Huge mistake! Eating junk food only makes the virus stronger! Mission failed...)"}
        }
    },

    # ===== 第 4 頁 (核心衝突) =====
    "4_A": {
        "title_tc": "第 4 頁：冰火交加的考驗", "title_en": "Page 4: The Test of Ice and Fire",
        "sfx": "🔥 呼呼！❄️ 嘶嘶！",
        "story_tc": "病毒見打不過你，便開始搗亂體溫調節中心，讓波波一會兒發冷，一會兒發熱！",
        "story_en": "Failing to beat you, the virus messes with the temperature center, making Bobo shiver then sweat!",
        "choices": {
            "A": {"text": "💦 運用科學原理，用溫水幫細胞們抹身降溫！ (Use science principles to wipe the cells with warm water to cool down!)", "next": "5_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "PE"], "is_bad": False},
            "B": {"text": "🫂 展現愛心，緊緊抱住發冷的細胞們給他們溫暖！ (Show love and tightly hug the shivering cells to keep them warm!)", "next": "5_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (決戰與結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：消滅與轉化", "title_en": "Page 5: Destroy or Transform",
        "sfx": "✨ 閃閃發光！SPARKLE!",
        "story_tc": "波波的體溫恢復正常了！哈啾病毒變得非常虛弱，趴在地上求饒。火鷹俠準備處置病毒：",
        "story_en": "Bobo's temperature is normal! The Achoo Virus is very weak and begging for mercy. Firebird prepares to deal with it:",
        "choices": {
            "A": {"text": "🧼 教導病毒「洗手防菌七部曲」，將它轉化為愛乾淨的益生菌！ (Teach the virus the '7-step hand washing' and turn it into a clean probiotic!)", "next": "6_LEADER", "effect": {"empathy": 2, "creativity": 1}, "kla": ["PE", "HUMANITIES"], "is_bad": False},
            "B": {"text": "🫧 堅守健康原則，用超級肥皂泡泡把它永遠鎖起來並排出體外！ (Stick to health rules, lock it in a super soap bubble and expel it!)", "next": "6_HERO", "effect": {"bravery": 3}, "kla": ["SCIENCE"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_SHRINK": {
        "title_tc": "💥 任務失敗：忘記縮小", "title_en": "Mission Failed: Forgot to Shrink",
        "sfx": "💥 BOOM!", "is_bad_ending": True,
        "story_tc": "科學探險必須經過嚴謹的計算與準備！我們不能不顧後果地亂闖。",
        "story_en": "Science adventures require careful calculation and preparation!"
    },
    "BAD_END_SCOLD": {
        "title_tc": "💥 任務失敗：缺乏同理心", "title_en": "Mission Failed: Lack of Empathy",
        "sfx": "📉 FALL!", "is_bad_ending": True,
        "story_tc": "當朋友生病虛弱時，責罵是沒有用的，我們應該給予鼓勵和營養！",
        "story_en": "When friends are sick and weak, scolding doesn't help. We should give encouragement and nutrition!"
    },
    "BAD_END_JUNKFOOD": {
        "title_tc": "💥 任務失敗：零食危機", "title_en": "Mission Failed: Junk Food Crisis",
        "sfx": "🤢 OUCH!", "is_bad_ending": True,
        "story_tc": "生病時吃太多不健康的零食會讓身體更難受！我們要多吃蔬菜水果和多喝水。",
        "story_en": "Eating junk food when sick makes the body feel worse! We must eat veggies, fruits, and drink water."
    }
}
