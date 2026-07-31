# ==============================================================================
# ⏳ 火鷹俠 8：時空古城綠化危機 (Time-Travel Eco-Crisis)
# 融入 PERCCI 品格 (承擔、尊重) + KLA (人文教育、科學教育、科技教育)
# ==============================================================================

STORY_INFO = {
    "id": "Story8",
    "name_tc": "⏳ 火鷹俠 8：時空古城綠化危機",
    "name_en": "Firebird 8: Time-Travel Eco-Crisis"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：歷史古城的枯萎危機！", "title_en": "Page 1: The Withered Ancient City!",
        "sfx": "📜 呼呼... WHOOSH...",
        "story_tc": "大事不好了！穿越時空來到古代的「未來綠化古城」突然失去了所有的植物，變成了一片灰色的黃土沙漠！歷史紀錄正在消失。火鷹俠決定啟動時空穿梭器：",
        "story_en": "Oh no! The ancient-future 'Green City' has suddenly lost all its plants, turning into a gray dust desert! History records are vanishing. Firebird decides to activate the time-traveler:",
        "choices": {
            "A": {"text": "🕰️ 駕駛「STEAM 時空飛行器」，設定座標飛回綠化消失的那一天 (STEAM)！ (Pilot the STEAM Time-Flyer to the day the greenery vanished!)", "next": "2_A", "effect": {"creativity": 2}, "kla": ["TECH", "SCIENCE"], "is_bad": False},
            "B": {"text": "🗺️ 拿著古代地圖，勇敢地徒步走進神祕的時空裂縫！ (Take the ancient map and bravely walk into the mysterious time rift!)", "next": "2_B", "effect": {"bravery": 1}, "kla": ["HUMANITIES"], "is_bad": False},
            "C": {"text": "🏃‍♂️ 閉上眼睛，盲目地亂跑進任何一個時空旋渦！ (Close your eyes and run blindly into any time vortex!)", "next": "BAD_END_VORTEX", "effect": {"bravery": -2}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "時空旅行必須有精準的科學計算，盲目亂闖會讓你迷失在時間的長河中！任務失敗……\n(Time travel requires precise scientific calculation. Blind running gets you lost in time! Mission failed...)"}
        }
    },

    # ===== 分支 A：時空飛行器路線 =====
    "2_A": {
        "title_tc": "第 2 頁：古代水利工程的難題", "title_en": "Page 2: Ancient Water Management Puzzle",
        "sfx": "💧 滴答... DRIP...",
        "story_tc": "飛行器成功降落在古代古城。你發現這裡的河流因為水閘損壞而乾涸，植物才會枯萎。火鷹俠運用科學原理：",
        "story_en": "The flyer lands safely. You find the river dried up because a sluice gate is broken, causing plants to wither. Firebird uses science:",
        "choices": {
            "A": {"text": "📐 利用槓桿原理與重力，設計一套「自動蓄水水車」修復水利 (STEAM)！ (Design an automatic water wheel using leverage and gravity!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "TECH", "MATH"], "is_bad": False},
            "B": {"text": "🪣 發動全城居民，用木桶接力把遠處的水搬過來！ (Mobilize residents to relay water using wooden buckets!)", "next": "3_A", "effect": {"empathy": 1, "bravery": 1}, "kla": ["HUMANITIES", "PE"], "is_bad": False},
            "C": {"text": "🔥 用大火把乾涸的河床燒得更深！ (Use a big fire to burn the dry riverbed deeper!)", "next": "BAD_END_FIRE", "effect": {"creativity": -2}, "kla": ["SCIENCE"], "is_bad": True,
                  "bad_reason": "火上加油只會破壞土壤結構，讓環境變得更糟！科學探究需要正確的方法。任務失敗……\n(Adding fire destroys soil structure and worsens the environment! Mission failed...)"}
        }
    },

    # ===== 分支 B：徒步古城路線 =====
    "2_B": {
        "title_tc": "第 2 頁：古代建築的保護迷宮", "title_en": "Page 2: Ancient Architecture Maze",
        "sfx": "🏛️ 喀吱... CREAK...",
        "story_tc": "你走進了一座歷史悠久的古代宮殿，但走廊充滿了保護機關。火鷹俠展現人文尊重與歷史智慧：",
        "story_en": "You enter a historic ancient palace, but the corridors are full of security mechanisms. Firebird shows respect and historical wisdom:",
        "choices": {
            "A": {"text": "🔍 觀察石壁上的古老文字提示，解開歷史智慧鎖！ (Observe the ancient text on the stone wall and unlock the history puzzle!)", "next": "3_A", "effect": {"creativity": 1, "empathy": 1}, "kla": ["HUMANITIES", "LANG_CH"], "is_bad": False},
            "B": {"text": "🧱 用力推倒古老的石牆走捷徑！ (Push down the ancient stone wall to take a shortcut!)", "next": "BAD_END_WALL", "effect": {"respect": -2}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "破壞歷史文物是不尊重的行為！古城失去了保護，機關全部塌下了！任務失敗……\n(Destroying historical heritage is disrespectful! The ancient city collapsed! Mission failed...)"}
        }
    },

    # ===== 第 3 頁匯合 =====
    "3_A": {
        "title_tc": "第 3 頁：遇見「時間破壞獸」", "title_en": "Page 3: Meeting the 'Time Destroyer'",
        "sfx": "🦖 吼！ROAR!",
        "story_tc": "終於找到了元兇！一隻代表「過度開發與浪費」的時間破壞獸正在偷走古城的綠色能量。火鷹俠決定：",
        "story_en": "You found the culprit! A 'Time Destroyer' representing overdevelopment and waste is stealing the green energy. Firebird decides to:",
        "choices": {
            "A": {"text": "🌱 聯手居民種下「永續發展樹苗」，用大自然的生命力淨化怪獸！ (Team up with residents to plant 'Sustainability Saplings' to purify the monster!)", "next": "4_A", "effect": {"empathy": 2, "bravery": 1}, "kla": ["SCIENCE", "HUMANITIES"], "is_bad": False},
            "B": {"text": "⚡ 發射「環保高科技網」，把怪獸困住並重新編程 (STEAM)！ (Fire an eco-tech net to trap and reprogram the monster!)", "next": "4_A", "effect": {"creativity": 2}, "kla": ["TECH", "SCIENCE"], "is_bad": False}
        }
    },

    # ===== 第 4 頁 (核心衝突) =====
    "4_A": {
        "title_tc": "第 4 頁：歷史的抉擇", "title_en": "Page 4: The Historical Choice",
        "sfx": "⚖️ 噹噹... CHIME...",
        "story_tc": "怪獸被感化了，但時空飛行器的能源快要耗盡。如果要回到現代，必須做出一個關於「歷史承擔」的抉擇：",
        "story_en": "The monster is reformed, but your time-flyer is running out of energy. To return to the present, you must make a choice about historical commitment:",
        "choices": {
            "A": {"text": "🤝 留下來協助古代居民建立「環保守則」，確保歷史不再重演 (Commitment)！ (Stay to help residents establish 'Eco-Rules' to ensure history doesn't repeat!)", "next": "5_A", "effect": {"empathy": 2, "bravery": 1}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "🔋 利用所學的 STEAM 知識，發明「太陽能時空補給器」順利返回現代！ (Use STEAM knowledge to invent a 'Solar Time Charger' and return safely!)", "next": "5_B", "effect": {"creativity": 2}, "kla": ["TECH", "SCIENCE"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：守護歷史的永恆綠洲！", "title_en": "Page 5: Protecting the Eternal Oasis!",
        "sfx": "🌳 蒼翠欲滴！LUSH!",
        "story_tc": "因為你的承擔，古代古城變成了永不枯萎的綠色文明，現代的歷史書上也出現了你的名字！",
        "story_en": "Because of your commitment, the ancient city became an eternal green civilization, and your name appears in modern history books!",
        "choices": {
            "A": {"text": "🌟 成為時空歷史守護者，繼續穿梭保護各個年代的地球！ (Become a Time-History Guardian, protecting Earth across eras!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：英雄凱旋！", "title_en": "Page 5: Hero's Triumph!",
        "sfx": "🚀 咻——！WHOOSH!",
        "story_tc": "你成功修復了時空，帶著寶貴的環保智慧回到了現代，讓現代城市變得更翠綠！",
        "story_en": "You successfully repaired time and returned to the present with precious eco-wisdom, making modern cities greener!",
        "choices": {
            "A": {"text": "🏆 成為頂尖的環保發明家，帶領大家迎向綠色未來！ (Become a top eco-inventor, leading everyone to a green future!)", "next": "6_INVENTOR", "effect": {"creativity": 3}, "kla": ["TECH", "SCIENCE"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_VORTEX": {
        "title_tc": "💥 任務失敗：時空迷失", "title_en": "Mission Failed: Lost in Time",
        "sfx": "🌀 LOST!", "is_bad_ending": True,
        "story_tc": "時空旅行不能隨心所欲地亂闖，我們需要冷靜規劃與科學計算！",
        "story_en": "Time travel requires calm planning and scientific calculation, not random wandering!"
    },
    "BAD_END_FIRE": {
        "title_tc": "💥 任務失敗：生態浩劫", "title_en": "Mission Failed: Eco-Disaster",
        "sfx": "🔥 BURN!", "is_bad_ending": True,
        "story_tc": "用錯誤的方法破壞大自然，只會帶來更大的災難。保護環境需要正確的科學知識！",
        "story_en": "Using wrong methods to harm nature brings disaster. Protecting the environment requires correct science!"
    },
    "BAD_END_WALL": {
        "title_tc": "💥 任務失敗：破壞文物", "title_en": "Mission Failed: Heritage Damage",
        "sfx": "🏛️ CRASH!", "is_bad_ending": True,
        "story_tc": "歷史文化遺產是珍貴的寶藏，我們必須學會尊重過去，而不是粗魯破壞！",
        "story_en": "Cultural heritage is precious. We must learn to respect the past, not destroy it!"
    }
}
