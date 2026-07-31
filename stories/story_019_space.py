# ==============================================================================
# 🚀 火鷹俠 19：星際迷航大救援 (Interstellar Rescue Mission)
# 融入 PERCCI 品格 (勇氣、尊重) + KLA (科學教育、數學教育、人文)
# ==============================================================================

STORY_INFO = {
    "id": "Story19",
    "name_tc": "🚀 火鷹俠 19：星際迷航大救援",
    "name_en": "Firebird 19: Interstellar Rescue Mission"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：隕石迷宮的求救信號！", "title_en": "Page 1: SOS from the Meteorite Maze!",
        "sfx": "📡 嗶嗶嗶！BEEP BEEP!",
        "story_tc": "總部收到緊急求救信號！「星際郵差」的飛船被困在危險的「隕石迷宮」裡失去了動力。火鷹俠立刻駕駛宇宙飛船前往救援，面對迎面而來的巨大隕石群，他決定：",
        "story_en": "Headquarters received an SOS! The 'Interstellar Postman' is trapped in the dangerous 'Meteorite Maze' without power. Firebird flies his spaceship to the rescue. Facing the giant meteorites, he decides to:",
        "choices": {
            "A": {"text": "📐 運用數學與編程，計算隕石的運行軌道，找出最安全的穿梭路線 (STEAM)！ (Use math and coding to calculate the meteorites' orbits and find the safest path!)", "next": "2_A", "effect": {"creativity": 2}, "kla": ["MATH", "TECH"], "is_bad": False},
            "B": {"text": "🕹️ 展現過人的反應神經，手動駕駛飛船左閃右避衝過去！ (Show great reflexes and manually pilot the ship to dodge left and right!)", "next": "2_B", "effect": {"bravery": 2}, "kla": ["PE"], "is_bad": False},
            "C": {"text": "💥 開啟飛船的雷射炮，把所有擋路的隕石全部炸碎！ (Use the laser cannons to blast all meteorites in the way!)", "next": "BAD_END_DEBRIS", "effect": {"creativity": -1}, "kla": ["SCIENCE"], "is_bad": True,
                  "bad_reason": "在太空中亂開火會製造大量危險的「太空垃圾 (Space Debris)」！飛船被碎片擊中，引擎故障了。任務失敗……\n(Blasting creates dangerous 'Space Debris'! The ship was hit by fragments and the engine failed. Mission failed...)"}
        }
    },

    # ===== 分支 A：計算軌道路線 (能源挑戰) =====
    "2_A": {
        "title_tc": "第 2 頁：被遮蔽的太陽能", "title_en": "Page 2: The Blocked Solar Energy",
        "sfx": "🔋 能源不足！LOW BATTERY!",
        "story_tc": "你安全抵達了郵差飛船的旁邊，發現他們的「太陽能板」被厚厚的宇宙塵埃覆蓋了，所以才失去動力。火鷹俠運用科學常識：",
        "story_en": "You safely reached the postman's ship, but its 'Solar Panels' are covered in thick cosmic dust, causing the power loss. Firebird uses science knowledge:",
        "choices": {
            "A": {"text": "🧲 發射「電磁吸塵無人機」，利用靜電把宇宙塵埃全部吸走 (STEAM)！ (Deploy an 'Electromagnetic Drone' to vacuum the cosmic dust using static electricity!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "TECH"], "is_bad": False},
            "B": {"text": "👨‍🚀 勇敢地穿上太空衣，飛出艙外用特製抹布親手擦乾淨！ (Bravely put on a spacesuit, float outside, and wipe it clean with a special cloth!)", "next": "3_A", "effect": {"bravery": 2}, "kla": ["PE", "SCIENCE"], "is_bad": False},
            "C": {"text": "💦 噴射大量的水去清洗太陽能板！ (Spray lots of water to wash the solar panels!)", "next": "BAD_END_WATER", "effect": {"creativity": -2}, "kla": ["SCIENCE"], "is_bad": True,
                  "bad_reason": "太空中溫度極低，水一噴出去就結成了堅硬的冰塊，把太陽能板徹底凍壞了！任務失敗……\n(Space is extremely cold. The water instantly froze into solid ice, damaging the panels completely! Mission failed...)"}
        }
    },

    # ===== 分支 B：手動駕駛路線 (引力挑戰) =====
    "2_B": {
        "title_tc": "第 2 頁：黑洞的強大引力", "title_en": "Page 2: The Black Hole's Gravity",
        "sfx": "🌀 呼呼！SWOOSH!",
        "story_tc": "你成功閃避了隕石，卻發現郵差飛船正被附近一個微型黑洞的「強大引力 (Gravity)」慢慢吸進去！火鷹俠決定運用物理學知識：",
        "story_en": "You dodged the meteorites, but the postman's ship is slowly being pulled by the 'Gravity' of a nearby micro black hole! Firebird uses physics:",
        "choices": {
            "A": {"text": "🪐 利用附近行星的「引力彈弓效應」，加速把郵差飛船拉出來 (STEAM)！ (Use the 'Slingshot Effect' from a nearby planet's gravity to accelerate and pull the ship out!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "MATH"], "is_bad": False},
            "B": {"text": "🔗 發射超強鈦金屬拖車索，啟動所有引擎拼盡全力跟黑洞拔河！ (Fire a Titanium Tow Cable, ignite all engines, and play tug-of-war with the black hole!)", "next": "3_A", "effect": {"bravery": 2, "creativity": 1}, "kla": ["PE", "TECH"], "is_bad": False},
            "C": {"text": "🛑 立刻踩下煞車，試圖讓飛船停在原地！ (Slam on the brakes instantly, trying to stop the ship in place!)", "next": "BAD_END_GRAVITY", "effect": {"bravery": -1}, "kla": ["SCIENCE"], "is_bad": True,
                  "bad_reason": "在強大的引力下，踩煞車是沒有用的，你反而失去了逃脫的動力，一起被吸進去了！任務失敗……\n(Braking is useless against strong gravity. You lost escape momentum and got pulled in together! Mission failed...)"}
        }
    },

    # ===== 第 3 頁匯合 =====
    "3_A": {
        "title_tc": "第 3 頁：飄走的和平信件", "title_en": "Page 3: The Floating Peace Letter",
        "sfx": "✉️ 飄浮... FLOAT...",
        "story_tc": "郵差得救了！但他急得哭了起來：「我在混亂中弄丟了要送給外星國王的『星際和平信』，它飄到外面去了！」火鷹俠決定：",
        "story_en": "The postman is saved! But he cries: 'In the chaos, I lost the Interstellar Peace Letter for the Alien King! It floated outside!' Firebird decides to:",
        "choices": {
            "A": {"text": "❤️ 安慰郵差不要哭，展現同理心，答應一定會幫他找回來！ (Comfort the postman, show empathy, and promise to find it back!)", "next": "4_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "🔍 立刻啟動飛船的「光譜掃描儀」，冷靜地搜索信件的蹤跡！ (Immediately activate the ship's 'Spectrum Scanner' to calmly search for the letter!)", "next": "4_A", "effect": {"creativity": 2}, "kla": ["TECH", "SCIENCE"], "is_bad": False}
        }
    },

    # ===== 第 4 頁 (最終挑戰) =====
    "4_A": {
        "title_tc": "第 4 頁：沉睡的太空巨鯨", "title_en": "Page 4: The Sleeping Space Whale",
        "sfx": "🐋 呼嚕嚕... SNORE...",
        "story_tc": "你發現信件飄到了一隻巨大的「太空星鯨」的鼻子上！星鯨正在睡覺，如果吵醒牠，可能會引發危險的太空海嘯。火鷹俠決定：",
        "story_en": "You found the letter floating on the nose of a giant 'Space Whale'! It is sleeping. Waking it up might cause a dangerous space tsunami. Firebird decides to:",
        "choices": {
            "A": {"text": "🤝 展現對宇宙生命的尊重，輕輕發送溫柔的腦電波音樂，請牠幫忙把信吹過來！ (Show respect for cosmic life. Send gentle brainwave music and ask it politely to blow the letter over!)", "next": "5_A", "effect": {"empathy": 2, "bravery": 1}, "kla": ["ARTS", "HUMANITIES"], "is_bad": False},
            "B": {"text": "🤖 操控無聲的微型機械蜘蛛，靜悄悄地爬過去把信件夾回來 (STEAM)！ (Control a silent micro robo-spider to sneak over and grab the letter back quietly!)", "next": "5_B", "effect": {"creativity": 2}, "kla": ["TECH", "PE"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：宇宙的友誼之歌！", "title_en": "Page 5: The Cosmic Song of Friendship!",
        "sfx": "🎶 悠揚！MELODIC!",
        "story_tc": "星鯨很喜歡你的音樂，牠不僅把信件還給了你，還親自護送你們穿越了危險區域！和平信順利送達，你成為了宇宙的和平大使。",
        "story_en": "The Space Whale loved your music. It returned the letter and safely escorted you out! The peace letter was delivered. You became a cosmic peace ambassador.",
        "choices": {
            "A": {"text": "🌟 成為尊重自然與生命的「全人小領袖」！ (Become a 'Whole-person Leader' who respects nature and life!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES", "SCIENCE"], "is_bad": False}
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：完美的極密任務！", "title_en": "Page 5: Perfect Stealth Mission!",
        "sfx": "✨ 成功！SUCCESS!",
        "story_tc": "機械蜘蛛成功取回了信件，星鯨完全沒有被吵醒！你用冷靜和高超的科技化解了危機，外星國王非常感謝你們的專業。",
        "story_en": "The robo-spider retrieved the letter without waking the whale! You solved the crisis with calmness and tech. The Alien King is very grateful for your professionalism.",
        "choices": {
            "A": {"text": "🏆 成為結合科技與冷靜判斷的「創意發明家」！ (Become a 'Creative Inventor' combining tech and calm judgment!)", "next": "6_INVENTOR", "effect": {"creativity": 3}, "kla": ["TECH"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_DEBRIS": {
        "title_tc": "💥 任務失敗：太空垃圾危機", "title_en": "Mission Failed: Space Debris Crisis",
        "sfx": "💥 CRASH!", "is_bad_ending": True,
        "story_tc": "在太空中亂開火會製造大量危險的「太空垃圾 (Space Debris)」！我們必須保護宇宙環境，不能隨意破壞。",
        "story_en": "Blasting creates dangerous 'Space Debris'! We must protect the cosmic environment and not destroy it recklessly."
    },
    "BAD_END_WATER": {
        "title_tc": "💥 任務失敗：瞬間結冰", "title_en": "Mission Failed: Instant Freeze",
        "sfx": "❄️ FREEZE!", "is_bad_ending": True,
        "story_tc": "太空的科學常識：宇宙是真空且極度寒冷的，水一暴露在太空中就會瞬間結冰！",
        "story_en": "Space science fact: Space is a cold vacuum. Water freezes instantly when exposed to space!"
    },
    "BAD_END_GRAVITY": {
        "title_tc": "💥 任務失敗：無法逃脫的引力", "title_en": "Mission Failed: Inescapable Gravity",
        "sfx": "🌀 SUCKED IN!", "is_bad_ending": True,
        "story_tc": "面對黑洞強大的「引力 (Gravity)」，停在原地只會被吸進去，必須利用加速度逃離！",
        "story_en": "Against a black hole's strong 'Gravity', staying still means getting pulled in. You must use acceleration to escape!"
    }
}
