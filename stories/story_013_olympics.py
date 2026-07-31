# ==============================================================================
# 🏅 火鷹俠 13：動物奧運會的公平競技 (The Animal Olympics Fair Play)
# 融入 PERCCI 品格 (誠信、尊重) + KLA (體育、科學教育、數學、人文)
# ==============================================================================

STORY_INFO = {
    "id": "Story13",
    "name_tc": "🏅 火鷹俠 13：動物奧運會的公平競技",
    "name_en": "Firebird 13: The Animal Olympics Fair Play"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：動物奧運會的作弊危機！", "title_en": "Page 1: The Cheating Crisis at the Animal Olympics!",
        "sfx": "🏁 哨聲！TWEET!",
        "story_tc": "四年一度的「動物奧運會」開幕了！但「搗蛋狐狸」為了贏得金牌，竟然在百米賽跑的跑道上倒滿了滑溜溜的機油！選手們全都摔得四腳朝天。火鷹俠決定展現誠信與體育精神，上前解決問題：",
        "story_en": "The Animal Olympics has begun! But the 'Prankster Fox' poured slippery oil all over the 100m track to win the gold medal! Athletes are slipping and falling. Firebird decides to show integrity and sportsmanship to fix this:",
        "choices": {
            "A": {"text": "👟 運用科學原理，發明「超強摩擦力防滑釘鞋」(STEAM)！ (Use science to invent 'High-Friction Anti-Slip Spikes'!)", "next": "2_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "TECH"], "is_bad": False},
            "B": {"text": "🧹 號召所有動物，團結一致用沙子把機油清理乾淨！ (Call all animals to unite and clean the oil with sand!)", "next": "2_B", "effect": {"empathy": 2}, "kla": ["PE", "HUMANITIES"], "is_bad": False},
            "C": {"text": "⛸️ 不管那麼多，當作溜冰比賽直接滑過去！ (Ignore the danger and just skate across the oil!)", "next": "BAD_END_SLIP", "effect": {"bravery": -1}, "kla": ["PE"], "is_bad": True,
                  "bad_reason": "體育運動首重安全！在充滿機油的跑道上強行奔跑會嚴重受傷的。任務失敗……\n(Safety first in sports! Running on an oily track causes severe injuries. Mission failed...)"}
        }
    },

    # ===== 分支 A：防滑鞋路線 (射箭比賽) =====
    "2_A": {
        "title_tc": "第 2 頁：狂風中的射箭賽", "title_en": "Page 2: Archery in the Gale",
        "sfx": "💨 呼嘯！WHOOSH!",
        "story_tc": "防滑鞋非常成功！但接下來是射箭比賽，搗蛋狐狸偷偷在靶場旁邊開啟了巨大的工業風扇，吹出狂風干擾大家！火鷹俠運用數學與物理：",
        "story_en": "The anti-slip shoes worked! But next is the archery competition. The Fox secretly turned on giant industrial fans to blow away the arrows! Firebird uses math and physics:",
        "choices": {
            "A": {"text": "📐 計算風速和角度，調整射擊的「拋物線」完美命中紅心 (STEAM)！ (Calculate wind speed and angle to adjust the trajectory for a bullseye!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["MATH", "SCIENCE"], "is_bad": False},
            "B": {"text": "🛡️ 勇敢地站在選手旁邊，舉起巨大的防護盾擋住狂風！ (Bravely stand by the athletes and raise a giant shield to block the wind!)", "next": "3_A", "effect": {"bravery": 2}, "kla": ["PE", "TECH"], "is_bad": False},
            "C": {"text": "🏹 閉上眼睛，隨便把箭射出去碰運氣！ (Close your eyes and shoot the arrow blindly!)", "next": "BAD_END_WIND", "effect": {"creativity": -2}, "kla": ["PE"], "is_bad": True,
                  "bad_reason": "射箭需要精準的計算與冷靜的判斷，亂射一通非常危險！任務失敗……\n(Archery requires precise calculation and calm judgment. Shooting blindly is dangerous! Mission failed...)"}
        }
    },

    # ===== 分支 B：清理跑道路線 (舉重比賽) =====
    "2_B": {
        "title_tc": "第 2 頁：舉重比賽的磁鐵陰謀", "title_en": "Page 2: The Magnet Conspiracy in Weightlifting",
        "sfx": "🏋️‍♂️ 哐噹！CLANK!",
        "story_tc": "跑道清理乾淨了！但在舉重比賽中，狐狸在別人的槓鈴下裝了超強電磁鐵，讓大象和黑熊都舉不起來！火鷹俠決定維護比賽的公平：",
        "story_en": "The track is clean! But in weightlifting, the Fox hid super electromagnets under everyone's barbells. Even the elephant can't lift them! Firebird steps up for fair play:",
        "choices": {
            "A": {"text": "🧲 拿出「磁場探測器」，用科學證據揭穿狐狸的作弊機關！ (Use a 'Magnetic Detector' to expose the cheating trap with scientific evidence!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "TECH"], "is_bad": False},
            "B": {"text": "⚖️ 向裁判舉報，要求根據比賽規則重新檢查器材 (Integrity)！ (Report to the referee and request an equipment check based on the rules!)", "next": "3_A", "effect": {"empathy": 1, "bravery": 1}, "kla": ["HUMANITIES", "PE"], "is_bad": False},
            "C": {"text": "💪 鼓勵大象用盡全身的蠻力，硬生生地把磁鐵拔起來！ (Encourage the elephant to use brute force to rip the magnet off the ground!)", "next": "BAD_END_LIFT", "effect": {"bravery": -1}, "kla": ["PE", "SCIENCE"], "is_bad": True,
                  "bad_reason": "遇到不合理的重量時，不要用蠻力硬舉，這樣會拉傷肌肉的！我們應該找出原因。任務失敗……\n(Don't use brute force to lift unreasonable weight, it causes muscle injury! Find the root cause instead. Mission failed...)"}
        }
    },

    # ===== 第 3 頁匯合 =====
    "3_A": {
        "title_tc": "第 3 頁：狐狸的眼淚", "title_en": "Page 3: The Fox's Tears",
        "sfx": "😢 嗚嗚！SOB!",
        "story_tc": "狐狸的作弊計畫被識破了！他坐在草地上大哭：「我只是跑得不夠快，力氣也不夠大，我太想拿金牌證明自己了……」火鷹俠決定：",
        "story_en": "The Fox's cheating plans are exposed! He cries on the grass: 'I'm just not fast or strong enough. I wanted a gold medal so badly to prove myself...' Firebird decides to:",
        "choices": {
            "A": {"text": "🤝 展現同理心，告訴他「超越自己」比拿金牌更重要，並答應當他的教練！ (Show empathy, tell him 'beating yourself' is more important than gold, and offer to coach him!)", "next": "4_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES", "PE"], "is_bad": False},
            "B": {"text": "📜 嚴肅地教導他「誠信 (Integrity)」，告訴他作弊得來的金牌毫無意義！ (Sternly teach him about Integrity, saying a cheated medal means nothing!)", "next": "4_A", "effect": {"bravery": 2}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 第 4 頁 (最終挑戰) =====
    "4_A": {
        "title_tc": "第 4 頁：真正的體育精神", "title_en": "Page 4: True Sportsmanship",
        "sfx": "🔥 燃燒！FIRED UP!",
        "story_tc": "狐狸明白了誠信的重要，主動交出了所有作弊工具，並向大家道歉。現在，奧運會的壓軸項目「4x100 接力賽」要開始了！火鷹俠決定：",
        "story_en": "The Fox learned the value of integrity, handed over all cheating tools, and apologized. Now, the finale event '4x100 Relay Race' is starting! Firebird decides to:",
        "choices": {
            "A": {"text": "🏃‍♂️ 邀請狐狸加入你的接力隊，一起用真正的實力與汗水完成比賽！ (Invite the Fox to join your relay team and finish the race with true skill and sweat!)", "next": "5_A", "effect": {"empathy": 2, "bravery": 1}, "kla": ["PE", "HUMANITIES"], "is_bad": False},
            "B": {"text": "⏱️ 擔任比賽的公平裁判，運用高科技感測器確保比賽 100% 公平！ (Serve as a fair referee, using high-tech sensors to ensure a 100% fair race!)", "next": "5_B", "effect": {"creativity": 2}, "kla": ["TECH", "SCIENCE"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：最閃亮的汗水！", "title_en": "Page 5: The Shining Sweat!",
        "sfx": "🏆 衝線！FINISH LINE!",
        "story_tc": "你們雖然沒有拿到第一名，但狐狸拼盡全力跑出了他有史以來最快的成績！觀眾們為你們響起了最熱烈的掌聲！",
        "story_en": "Though you didn't win first place, the Fox ran his fastest time ever! The audience gave you the loudest applause!",
        "choices": {
            "A": {"text": "🌟 成為傳遞體育精神與友誼的「全人小領袖」！ (Become a 'Whole-person Leader' who spreads sportsmanship and friendship!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["PE", "HUMANITIES"], "is_bad": False}
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：公正的守護者！", "title_en": "Page 5: The Guardian of Fairness!",
        "sfx": "⚖️ 公平！FAIR PLAY!",
        "story_tc": "在你的嚴格監督下，這場接力賽成為了動物奧運會有史以來最公平、最精彩的比賽！大家都非常尊敬你。",
        "story_en": "Under your strict supervision, the relay race became the fairest and most exciting in Animal Olympics history! Everyone respects you deeply.",
        "choices": {
            "A": {"text": "🏅 成為捍衛誠信與規則的「勇氣英雄」！ (Become a 'Courage Hero' who defends integrity and rules!)", "next": "6_HERO", "effect": {"bravery": 3}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_SLIP": {
        "title_tc": "💥 任務失敗：滑溜溜的陷阱", "title_en": "Mission Failed: Slippery Trap",
        "sfx": "🤕 OUCH!", "is_bad_ending": True,
        "story_tc": "體育運動首重安全！在充滿機油的跑道上強行奔跑會嚴重受傷的。",
        "story_en": "Safety first in sports! Running on an oily track causes severe injuries."
    },
    "BAD_END_WIND": {
        "title_tc": "💥 任務失敗：亂飛的箭", "title_en": "Mission Failed: Stray Arrows",
        "sfx": "❌ MISS!", "is_bad_ending": True,
        "story_tc": "射箭需要精準的計算與冷靜的判斷，亂射一通不但中不了靶，還會發生危險！",
        "story_en": "Archery requires precise calculation. Shooting blindly is not only inaccurate but dangerous!"
    },
    "BAD_END_LIFT": {
        "title_tc": "💥 任務失敗：肌肉拉傷", "title_en": "Mission Failed: Muscle Strain",
        "sfx": "💪 CRACK!", "is_bad_ending": True,
        "story_tc": "遇到不合理的重量時，不要用蠻力硬舉，這樣會拉傷肌肉的！我們應該用科學找出原因。",
        "story_en": "Don't use brute force to lift unreasonable weight, it causes muscle injury! Use science to find the cause."
    }
}
