# ==============================================================================
# 🚄 火鷹俠 21：智能磁浮列車大危機 (The Maglev Train Crisis)
# 融入 PERCCI 品格 (同理心、創意) + KLA (科學教育、數學、科技、人文)
# ==============================================================================

STORY_INFO = {
    "id": "Story21",
    "name_tc": "🚄 火鷹俠 21：智能磁浮列車大危機",
    "name_en": "Firebird 21: The Maglev Train Crisis"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：卡在半空的特快車！", "title_en": "Page 1: The Express Train Stuck in Mid-air!",
        "sfx": "🚨 嗚嗚！SIREN WAILES!",
        "story_tc": "大事不好了！未來城市的「超級磁浮列車」因為中央導航系統故障，卡在半空中的軌道上動彈不得！車上還有好多準備去上學的小朋友。火鷹俠立刻飛到現場，他決定：",
        "story_en": "Oh no! The future city's 'Super Maglev Train' is stuck on the mid-air tracks because the central navigation system failed! Many children heading to school are trapped inside. Firebird flies to the scene and decides to:",
        "choices": {
            "A": {"text": "💻 飛到控制塔，運用編程思維重新規劃列車的安全行駛路線 (STEAM)！ (Fly to the control tower and use coding logic to reprogram the train's safe route!)", "next": "2_A", "effect": {"creativity": 2}, "kla": ["MATH", "TECH"], "is_bad": False},
            "B": {"text": "🧲 運用科學知識，啟動戰衣上的「超級電磁鐵」，在車頭牽引列車前進！ (Use science knowledge, activate the suit's 'Super Electromagnet' to pull the train from the front!)", "next": "2_B", "effect": {"bravery": 1, "creativity": 1}, "kla": ["SCIENCE", "PE"], "is_bad": False},
            "C": {"text": "💪 甚麼都不管，直接飛到車尾用蠻力硬推列車！ (Ignore everything, fly to the back and push the train with sheer brute force!)", "next": "BAD_END_PUSH", "effect": {"bravery": -2}, "kla": ["SCIENCE"], "is_bad": True,
                  "bad_reason": "磁浮列車是懸浮在軌道上的，沒有啟動磁力就硬推，會刮壞底盤引發大火！任務失敗……\n(Maglev trains float on tracks. Pushing without activating the magnets will scratch the bottom and cause a fire! Mission failed...)"}
        }
    },

    # ===== 分支 A：編程與路徑規劃 (數學挑戰) =====
    "2_A": {
        "title_tc": "第 2 頁：迷宮般的軌道路線", "title_en": "Page 2: The Maze-like Track Routes",
        "sfx": "🗺️ 嗶嗶！CALCULATING!",
        "story_tc": "你進入了控制塔，但螢幕上的軌道圖亂成一團。前方有三條路：A 路線有斷橋，B 路線大塞車，C 路線是暢通的後備軌道。火鷹俠必須運用空間與邏輯數學：",
        "story_en": "You enter the control tower, but the track map on the screen is a mess. There are three paths ahead: Route A has a broken bridge, Route B has a traffic jam, Route C is a clear backup track. Firebird uses spatial and logical math:",
        "choices": {
            "A": {"text": "🛤️ 輸入指令，將道岔切換到 C 路線，讓列車避開危險安全前進！ (Input commands to switch the junction to Route C, letting the train proceed safely away from danger!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["MATH", "TECH"], "is_bad": False},
            "B": {"text": "🚦 強行開啟 B 路線的綠燈，叫所有前面的車子立刻讓路！ (Force the green light on Route B and tell all cars ahead to yield immediately!)", "next": "BAD_END_TRAFFIC", "effect": {"empathy": -1}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "這樣會造成更嚴重的交通意外！城市交通需要有秩序的規劃，不能只顧自己。任務失敗……\n(This will cause a worse traffic accident! City traffic requires orderly planning, you can't just think of yourself. Mission failed...)"}
        }
    },

    # ===== 分支 B：電磁牽引 (科學挑戰) =====
    "2_B": {
        "title_tc": "第 2 頁：同極相斥的奧秘", "title_en": "Page 2: The Mystery of Repelling Poles",
        "sfx": "⚡ 劈啪！ZAP!",
        "story_tc": "你飛到車頭準備用電磁鐵牽引，但你發現列車的車頭是「N 極（北極）」。火鷹俠回憶起科學課學過的磁鐵原理：",
        "story_en": "You fly to the front to pull with your electromagnet, but you notice the train's front is 'North Pole (N)'. Firebird recalls the science lesson about magnets:",
        "choices": {
            "A": {"text": "🧲 將戰衣的電磁鐵設定為「S 極（南極）」，利用「異極相吸」的原理穩穩拉動列車 (STEAM)！ (Set your suit's electromagnet to 'South Pole (S)', using the 'opposites attract' principle to pull the train steadily!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["SCIENCE"], "is_bad": False},
            "B": {"text": "🛡️ 將戰衣的電磁鐵設定為「N 極（北極）」！ (Set your suit's electromagnet to 'North Pole (N)'!)", "next": "BAD_END_MAGNET", "effect": {"creativity": -2}, "kla": ["SCIENCE"], "is_bad": True,
                  "bad_reason": "科學常識錯誤！「同極相斥」，兩塊 N 極會互相推開，你不但拉不動列車，還把自己彈飛了！任務失敗……\n(Science error! 'Like poles repel', two N poles will push each other away. You bounced yourself off! Mission failed...)"}
        }
    },

    # ===== 第 3 頁匯合：安撫乘客 (同理心挑戰) =====
    "3_A": {
        "title_tc": "第 3 頁：車廂裡的恐慌", "title_en": "Page 3: Panic in the Carriages",
        "sfx": "😭 嗚嗚！CRYING!",
        "story_tc": "列車終於重新移動了！但因為剛才停了很久，車廂裡的小朋友都嚇哭了，有人還想強行打開車門逃跑。身為超級英雄，火鷹俠決定展現公民責任與同理心：",
        "story_en": "The train is moving again! But after being stuck for so long, the children inside are crying in fear, and some want to force the doors open. As a superhero, Firebird shows civic duty and empathy:",
        "choices": {
            "A": {"text": "🎤 接通車廂廣播，用溫柔堅定的聲音安撫大家：「我是火鷹俠，大家很安全，請坐在座位上一起唱首歌！」 (Connect to the intercom, use a gentle but firm voice to comfort them: 'I am Firebird, you are safe. Please stay seated and let's sing a song!')", "next": "4_A", "effect": {"empathy": 2, "bravery": 1}, "kla": ["HUMANITIES", "ARTS"], "is_bad": False},
            "B": {"text": "👮‍♂️ 嚴厲地透過廣播大吼：「誰敢亂動我就把他抓起來！」 (Yell strictly through the intercom: 'Whoever moves will be arrested!')", "next": "BAD_END_SCOLD", "effect": {"empathy": -2}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "恐慌時大吼大叫只會讓大家更害怕！真正的英雄會用同理心帶來安全感。任務失敗……\n(Yelling during a panic makes everyone more scared! A true hero brings safety through empathy. Mission failed...)"}
        }
    },

    # ===== 第 4 頁：安全進站 (最終挑戰) =====
    "4_A": {
        "title_tc": "第 4 頁：煞車失靈的危機", "title_en": "Page 4: The Brake Failure Crisis",
        "sfx": "💨 呼嘯！SPEEDING!",
        "story_tc": "小朋友們平靜下來了，但列車即將進站時，煞車系統卻因為剛才的故障無法完全啟動！列車速度太快了！火鷹俠必須立刻想辦法減速：",
        "story_en": "The children calmed down, but as the train approaches the station, the brakes can't fully deploy due to the earlier glitch! It's too fast! Firebird must slow it down immediately:",
        "choices": {
            "A": {"text": "🪂 啟動軌道兩旁的「緊急空氣阻力傘」，利用風的阻力安全減速 (STEAM)！ (Deploy 'Emergency Air Drag Parachutes' along the track, using wind resistance to slow down safely!)", "next": "5_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "TECH"], "is_bad": False},
            "B": {"text": "🦸‍♂️ 飛到列車正前方，用雙手頂住車頭，用盡全身的力氣把車停下來！ (Fly right to the front, press both hands against the train, and use all your strength to stop it!)", "next": "5_B", "effect": {"bravery": 3}, "kla": ["PE"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：智慧守護的車站！", "title_en": "Page 5: The Station Guarded by Wisdom!",
        "sfx": "🚉 嘶——停！HALT!",
        "story_tc": "降落傘成功產生了巨大的空氣阻力，列車平穩且安全地停在了月台上！家長們在車站歡呼，感謝你的聰明才智。",
        "story_en": "The parachutes successfully created massive air resistance, stopping the train smoothly and safely at the platform! Parents cheer at the station, thanking you for your wisdom.",
        "choices": {
            "A": {"text": "🏆 成為運用科學與科技拯救城市的「創意發明家」！ (Become a 'Creative Inventor' who saves the city with science and tech!)", "next": "6_INVENTOR", "effect": {"creativity": 3}, "kla": ["TECH", "SCIENCE"], "is_bad": False}
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：愛心與勇氣的英雄！", "title_en": "Page 5: Hero of Love and Courage!",
        "sfx": "👏 掌聲如雷！APPLAUSE!",
        "story_tc": "你用驚人的體力和勇氣把列車安全停下！小朋友們衝出車廂抱住你，感謝你在廣播中給予他們的安全感。",
        "story_en": "You stopped the train safely with amazing physical strength and courage! The children rush out to hug you, thanking you for the sense of safety from your broadcast.",
        "choices": {
            "A": {"text": "🌟 成為具備同理心與勇敢承擔的「全人小領袖」！ (Become a 'Whole-person Leader' with empathy and courageous commitment!)", "next": "6_LEADER", "effect": {"empathy": 2, "bravery": 2}, "kla": ["HUMANITIES", "PE"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_PUSH": {
        "title_tc": "💥 任務失敗：缺乏科學常識", "title_en": "Mission Failed: Lack of Science Knowledge",
        "sfx": "🔥 FIRE!", "is_bad_ending": True,
        "story_tc": "解決工程問題不能只靠蠻力，必須了解交通工具的科學運作原理！",
        "story_en": "Engineering problems can't be solved by brute force alone. You must understand the scientific principles of vehicles!"
    },
    "BAD_END_TRAFFIC": {
        "title_tc": "💥 任務失敗：引發混亂", "title_en": "Mission Failed: Causing Chaos",
        "sfx": "🚗 CRASH!", "is_bad_ending": True,
        "story_tc": "城市規劃和交通燈的存在是為了保護所有人。強行改變規則會引發更大的災難！",
        "story_en": "City planning and traffic lights exist to protect everyone. Forcing rule changes causes bigger disasters!"
    },
    "BAD_END_MAGNET": {
        "title_tc": "💥 任務失敗：磁極錯誤", "title_en": "Mission Failed: Wrong Magnetic Pole",
        "sfx": "⚡ REPEL!", "is_bad_ending": True,
        "story_tc": "基礎科學常識：磁鐵是『同極相斥，異極相吸』。要拉動 N 極，必須使用 S 極！",
        "story_en": "Basic science: Magnets 'repel like poles and attract opposite poles'. To pull an N pole, you must use an S pole!"
    },
    "BAD_END_SCOLD": {
        "title_tc": "💥 任務失敗：缺乏同理心", "title_en": "Mission Failed: Lack of Empathy",
        "sfx": "😭 CRY LOUDER!", "is_bad_ending": True,
        "story_tc": "面對驚慌失措的人，大吼大叫只會讓情況惡化。我們應該用溫和的語氣安撫他們。",
        "story_en": "Yelling at panicking people only makes things worse. We should soothe them with a gentle tone."
    }
}
