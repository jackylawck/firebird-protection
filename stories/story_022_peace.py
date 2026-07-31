# ==============================================================================
# 🕊️ 火鷹俠 22：和平村的雙子嘉年華 (The Twin Carnival of Peace Village)
# 融入 PERCCI 品格 (同理心、尊重) + KLA (人文教育-公民與調解、藝術、數學)
# ==============================================================================

STORY_INFO = {
    "id": "Story22",
    "name_tc": "🕊️ 火鷹俠 22：和平村的雙子嘉年華",
    "name_en": "Firebird 22: The Twin Carnival of Peace Village"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：即將取消的慶典", "title_en": "Page 1: The Canceled Festival",
        "sfx": "🗣️ 吵鬧！ARGUE!",
        "story_tc": "「和平村」正準備舉辦年度嘉年華，但「太陽族」和「月亮族」卻吵得不可開交！太陽族想要在白天舉辦熱鬧的火焰舞會，月亮族卻想在夜晚舉辦寧靜的花燈晚會。雙方互不相讓，村長氣得準備取消嘉年華。火鷹俠決定化身「調解員」：",
        "story_en": "Peace Village is preparing for its annual carnival, but the 'Sun Tribe' and 'Moon Tribe' are arguing fiercely! The Sun Tribe wants a loud, fiery daytime dance, while the Moon Tribe wants a quiet, glowing nighttime lantern festival. Neither will compromise, and the Mayor is about to cancel it. Firebird steps in as a 'Mediator':",
        "choices": {
            "A": {"text": "🤝 運用調解技巧，邀請雙方坐下來，鼓勵他們說出心中的感受與需要 (Humanities)！ (Use mediation skills, invite both sides to sit down, and encourage them to express their feelings and needs!)", "next": "2_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES", "LANG_CH"], "is_bad": False},
            "B": {"text": "💡 運用創意，提議發明一個能同時發出火焰與柔光的「日夜魔法球」(STEAM)！ (Use creativity, propose inventing a 'Day-Night Magic Sphere' that emits both fire and soft light!)", "next": "2_B", "effect": {"creativity": 2}, "kla": ["TECH", "ARTS"], "is_bad": False},
            "C": {"text": "😡 大聲責罵他們：「你們太吵了！全部聽我的，不准再辦嘉年華！」 (Scold them loudly: 'You are too noisy! Listen to me, no more carnival!')", "next": "BAD_END_SCOLD", "effect": {"empathy": -2}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "以暴易暴是無法解決衝突的！調解紛爭需要中立與耐心，責罵只會讓大家更生氣。任務失敗……\n(Fighting fire with fire doesn't solve conflicts! Mediation requires neutrality and patience. Scolding makes it worse. Mission failed...)"}
        }
    },

    # ===== 分支 A：調解路線 (數學時間分配) =====
    "2_A": {
        "title_tc": "第 2 頁：時間的公平分配", "title_en": "Page 2: Fair Distribution of Time",
        "sfx": "⏱️ 滴答！TICK TOCK!",
        "story_tc": "雙方冷靜下來後，發現其實大家都希望能擁有 12 個小時的表演時間。但廣場只有一個，一天也只有 24 小時。火鷹俠運用數學思維：",
        "story_en": "After calming down, both sides realize they just want 12 hours of performance time. But there is only one square and 24 hours in a day. Firebird uses math logic:",
        "choices": {
            "A": {"text": "🧮 提出「雙贏 (Win-Win)」方案：將 24 小時平分，早上 12 小時歸太陽族，晚上 12 小時歸月亮族！ (Propose a 'Win-Win' solution: Divide 24 hours equally, 12 morning hours for the Sun Tribe, 12 night hours for the Moon Tribe!)", "next": "3_A", "effect": {"creativity": 1, "empathy": 1}, "kla": ["MATH", "HUMANITIES"], "is_bad": False},
            "B": {"text": "🎭 建議他們互相學習，月亮族白天參與火焰舞，太陽族晚上欣賞花燈！ (Suggest they learn from each other: Moon Tribe joins the day dance, Sun Tribe enjoys the night lanterns!)", "next": "3_A", "effect": {"empathy": 2}, "kla": ["ARTS", "HUMANITIES"], "is_bad": False},
            "C": {"text": "🪙 覺得太麻煩了，直接丟硬幣決定誰可以使用廣場！ (Think it's too much trouble, just flip a coin to decide who gets the square!)", "next": "BAD_END_COIN", "effect": {"creativity": -2}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "丟硬幣會讓其中一方完全失去機會，這不是「雙贏」，而是「零和遊戲 (Zero-sum game)」！任務失敗……\n(Flipping a coin makes one side lose entirely. This is a 'Zero-sum game', not a 'Win-win'! Mission failed...)"}
        }
    },

    # ===== 分支 B：魔法球路線 (科學/藝術挑戰) =====
    "2_B": {
        "title_tc": "第 2 頁：融合的光芒", "title_en": "Page 2: The Blended Light",
        "sfx": "✨ 閃耀！GLOW!",
        "story_tc": "你決定製作「日夜魔法球」來象徵兩族的融合。你有一塊代表太陽的「高溫紅寶石」和一塊代表月亮的「冰冷藍水晶」。火鷹俠運用科學與藝術：",
        "story_en": "You decide to build the 'Day-Night Magic Sphere' to symbolize their unity. You have a 'Hot Ruby' for the sun and a 'Cold Blue Crystal' for the moon. Firebird uses science and art:",
        "choices": {
            "A": {"text": "📐 運用熱力學原理，製作一個隔熱玻璃球將兩者安全地包裹在一起 (STEAM)！ (Use thermodynamics to make a thermal-insulated glass sphere to safely wrap both together!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "TECH"], "is_bad": False},
            "B": {"text": "🎨 利用色彩學的原理，讓紅光與藍光交織，折射出美麗的「紫色」和平之光！ (Use color theory, letting red and blue light intertwine to refract a beautiful 'Purple' light of peace!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["ARTS", "SCIENCE"], "is_bad": False}
        }
    },

    # ===== 第 3 頁匯合：斷裂的友誼之橋 =====
    "3_A": {
        "title_tc": "第 3 頁：修復友誼的橋樑", "title_en": "Page 3: Repairing the Bridge of Friendship",
        "sfx": "🌉 嘎吱！CREAK!",
        "story_tc": "兩族終於達成了共識！但連接兩個部落的「友誼之橋」因為之前長期的爭吵而年久失修，斷裂了。大家無法走到廣場參加嘉年華。火鷹俠決定：",
        "story_en": "The two tribes finally reached a consensus! But the 'Bridge of Friendship' connecting them is broken due to long-term neglect from their arguments. They can't reach the square. Firebird decides to:",
        "choices": {
            "A": {"text": "🤝 發揮領導力，號召兩族人民組成「人力輸送帶」，團結一致搬運木材修橋！ (Show leadership, call both tribes to form a 'Human Conveyor Belt' and work together to carry wood to fix the bridge!)", "next": "4_A", "effect": {"empathy": 2, "bravery": 1}, "kla": ["HUMANITIES", "PE"], "is_bad": False},
            "B": {"text": "🏗️ 運用工程學，設計一座擁有超強承重力的「幾何拱橋 (Arch Bridge)」 (STEAM)！ (Use engineering to design a highly load-bearing 'Geometric Arch Bridge'!)", "next": "4_A", "effect": {"creativity": 2}, "kla": ["TECH", "MATH"], "is_bad": False}
        }
    },

    # ===== 第 4 頁 (最終挑戰) =====
    "4_A": {
        "title_tc": "第 4 頁：嘉年華開幕！", "title_en": "Page 4: The Carnival Opens!",
        "sfx": "🎆 砰！FIREWORKS!",
        "story_tc": "橋樑修好了！嘉年華正式開始。白天，大家一起跳著充滿活力的火焰舞；夜晚，大家點起溫柔的花燈。作為最重要的調解人，村長邀請火鷹俠上台發表開幕演說：",
        "story_en": "The bridge is fixed! The carnival officially begins. By day, everyone dances the energetic fire dance; by night, they light gentle lanterns. As the key mediator, the Mayor invites Firebird to give the opening speech:",
        "choices": {
            "A": {"text": "🎤 發表一篇關於「包容與尊重」的演說，告訴大家不同的文化可以創造更美的世界！ (Give a speech on 'Inclusion and Respect', telling everyone that diverse cultures create a more beautiful world!)", "next": "5_A", "effect": {"empathy": 2, "bravery": 1}, "kla": ["HUMANITIES", "LANG_CH"], "is_bad": False},
            "B": {"text": "🚁 啟動無人機編隊，在夜空中排成太陽與月亮牽手的壯觀圖案 (STEAM)！ (Launch a drone fleet to form a spectacular image of the Sun and Moon holding hands in the night sky!)", "next": "5_B", "effect": {"creativity": 2}, "kla": ["TECH", "ARTS"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：最偉大的調解員！", "title_en": "Page 5: The Greatest Mediator!",
        "sfx": "👏 掌聲如雷！APPLAUSE!",
        "story_tc": "你的演說感動了所有人！太陽族和月亮族從此成為了最好的朋友。你用智慧和溝通化解了危機，大家都稱你為「和平村的最佳調解員」！",
        "story_en": "Your speech moved everyone! The Sun and Moon tribes became best friends forever. You resolved the crisis with wisdom and communication. Everyone calls you the 'Best Mediator of Peace Village'!",
        "choices": {
            "A": {"text": "🌟 繼續運用同理心與溝通技巧，成為化解衝突的「全人小領袖」！ (Continue using empathy and communication skills, becoming a 'Whole-person Leader' who resolves conflicts!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：科技點亮和平！", "title_en": "Page 5: Tech Lights Up Peace!",
        "sfx": "✨ 驚嘆！WOW!",
        "story_tc": "無人機的壯觀圖案照亮了夜空，將科學與藝術完美結合，為這場嘉年華畫上了最完美的句號！",
        "story_en": "The spectacular drone image lit up the night sky, perfectly blending science and art, bringing a perfect end to the carnival!",
        "choices": {
            "A": {"text": "🏆 成為用科技促進和平與藝術的「創意大師」！ (Become a 'Creative Master' who promotes peace and art through technology!)", "next": "6_CREATIVE", "effect": {"creativity": 3}, "kla": ["TECH", "ARTS"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_SCOLD": {
        "title_tc": "💥 任務失敗：缺乏中立與耐心", "title_en": "Mission Failed: Lack of Neutrality",
        "sfx": "📉 FALL!", "is_bad_ending": True,
        "story_tc": "調解紛爭最重要的就是「中立 (Neutrality)」和「積極聆聽 (Active Listening)」。發脾氣只會破壞溝通的橋樑！",
        "story_en": "The keys to mediation are 'Neutrality' and 'Active Listening'. Losing your temper only destroys the bridge of communication!"
    },
    "BAD_END_COIN": {
        "title_tc": "💥 任務失敗：零和遊戲", "title_en": "Mission Failed: Zero-Sum Game",
        "sfx": "❌ WRONG!", "is_bad_ending": True,
        "story_tc": "丟硬幣決定勝負會讓另一方完全失去權益。優秀的調解員會努力尋找滿足雙方需求的「雙贏 (Win-Win)」方案！",
        "story_en": "Flipping a coin makes one side lose everything. A great mediator strives for a 'Win-Win' solution that meets everyone's needs!"
    }
}
