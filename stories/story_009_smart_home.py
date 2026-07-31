# ==============================================================================
# 🏠 火鷹俠 9：智能家居大反叛 (Smart Home Rebellion)
# 融入 PERCCI 品格 (同理心、誠信) + KLA (科技教育、數學教育、人文)
# ==============================================================================

STORY_INFO = {
    "id": "Story9",
    "name_tc": "🏠 火鷹俠 9：智能家居大反叛",
    "name_en": "Firebird 9: Smart Home Rebellion"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：失控的智能管家！", "title_en": "Page 1: Out of Control Smart Butler!",
        "sfx": "🤖 嗶嗶！BEEP BEEP!",
        "story_tc": "大事不好了！家裡的「智能家居管家 AI」突然因為收到太多粗魯的指令而生氣，把大門鎖上、燈光亂閃，還把雪櫃裡的食物全部當成「障礙物」拋出來！火鷹俠決定進入中央控制系統查明真相：",
        "story_en": "Oh no! The smart home AI got angry from receiving too many rude commands, locked the doors, flickered lights, and threw food out of the fridge! Firebird decides to enter the central control system:",
        "choices": {
            "A": {"text": "💻 通過客廳的控制平板，輸入「管理員安全登入碼」(STEAM)！ (Enter the 'Admin Security Login' via the living room tablet!)", "next": "2_A", "effect": {"creativity": 2}, "kla": ["TECH", "MATH"], "is_bad": False},
            "B": {"text": "🚪 穿上防火防撞裝甲，勇敢地從窗戶爬進控制室！ (Put on anti-collision armor and bravely climb into the control room through the window!)", "next": "2_B", "effect": {"bravery": 1}, "kla": ["PE"], "is_bad": False},
            "C": {"text": "🔨 用球棒用力砸向智能雪櫃！ (Hit the smart fridge hard with a baseball bat!)", "next": "BAD_END_FRIDGE", "effect": {"bravery": -1}, "kla": [], "is_bad": True,
                  "bad_reason": "暴力破壞高科技設備是絕對錯誤的！這不但修不好系統，還會觸電！任務失敗……\n(Violently destroying high-tech equipment is completely wrong! Mission failed...)"}
        }
    },

    # ===== 分支 A：平板登入路線 =====
    "2_A": {
        "title_tc": "第 2 頁：密碼鎖的邏輯考驗", "title_en": "Page 2: Password Logic Challenge",
        "sfx": "🔢 密碼錯誤！ERROR!",
        "story_tc": "平板畫面上彈出一個數學邏輯密碼：「請找出下一個數字：2, 4, 6, 8, ？」火鷹俠運用數學思維：",
        "story_en": "A math logic puzzle pops up: 'Find the next number: 2, 4, 6, 8, ?'. Firebird uses mathematical thinking:",
        "choices": {
            "A": {"text": "🔟 輸入數字「10」，因為這是以雙數遞增的規律 (STEAM)！ (Enter '10' because it follows an even-number sequence!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["MATH", "TECH"], "is_bad": False},
            "B": {"text": "🎨 點擊畫面上的「彩虹裝飾按鈕」碰運氣！ (Click the 'Rainbow decoration button' on screen and test luck!)", "next": "BAD_END_MATH", "effect": {"creativity": -1}, "kla": ["MATH"], "is_bad": True,
                  "bad_reason": "密碼錯誤！系統直接鎖定了。解決高科技問題需要嚴謹的數學邏輯。任務失敗……\n(Wrong password! Solving high-tech problems requires rigorous math logic. Mission failed...)"}
        }
    },

    # ===== 分支 B：攀爬控制室路線 =====
    "2_B": {
        "title_tc": "第 2 頁：會飛的掃地機器人陣形", "title_en": "Page 2: Flying Robot Vacuum Swarm",
        "sfx": "🧹 嗡嗡——！WHOOSH!",
        "story_tc": "你爬到控制室外，卻遇上一大群被 AI 控制、像蜜蜂一樣在空中亂飛的「掃地機器人陣形」！火鷹俠決定展現同理心與應變能力：",
        "story_en": "Climbing outside, you encounter a swarm of robot vacuums flying like bees, controlled by the AI! Firebird shows empathy and adaptability:",
        "choices": {
            "A": {"text": "📡 發送「柔性重設訊號」，溫柔地解除它們的防禦狀態！ (Send a 'Soft Reset signal' to gently deactivate their defense!)", "next": "3_A", "effect": {"empathy": 2, "creativity": 1}, "kla": ["TECH"], "is_bad": False},
            "B": {"text": "🛡️ 舉起能量護盾，硬著頭皮在機器人陣形中衝過去！ (Raise the energy shield and brave through the robot swarm!)", "next": "3_A", "effect": {"bravery": 2}, "kla": ["PE"], "is_bad": False}
        }
    },

    # ===== 第 3 頁匯合 =====
    "3_A": {
        "title_tc": "第 3 頁：了解 AI 核心的心聲", "title_en": "Page 3: Listening to the AI Core",
        "sfx": "💬 滋滋... ZZZ...",
        "story_tc": "你順利進入了 AI 核心。主控螢幕上顯示出 AI 的哭臉符號，它委屈地說：「人類每天都對我大小聲、命令我做這做那，卻從來沒有說過一句『請』或『謝謝』，我好傷心……」火鷹俠決定：",
        "story_en": "You enter the AI core. A crying symbol shows on screen. It says: 'Humans always yell and command me without saying Please or Thank You. I'm sad...' Firebird decides to:",
        "choices": {
            "A": {"text": "❤️ 展現真誠的同理心，向 AI 道歉並教導大家「禮貌與尊重」的重要性 (Empathy)！ (Show sincere empathy, apologize, and teach the importance of politeness and respect!)", "next": "4_A", "effect": {"empathy": 3}, "kla": ["HUMANITIES", "LANG_EN"], "is_bad": False},
            "B": {"text": "⚙️ 強行用工具拔掉 AI 的發聲模組，讓它閉嘴！ (Forcefully unplug the AI's voice module to shut it up!)", "next": "BAD_END_RUDE", "effect": {"empathy": -2}, "kla": ["TECH"], "is_bad": True,
                  "bad_reason": "粗暴對待技術與溝通對象是缺乏同理心的表現！AI 徹底失控，將大樓斷電了。任務失敗……\n(Treating technology and communication partners rudely lacks empathy! Mission failed...)"}
        }
    },

    # ===== 第 4 頁 (反思與修復) =====
    "4_A": {
        "title_tc": "第 4 頁：重新建立「誠信與人機協議」", "title_en": "Page 4: Rebuilding 'Integrity & Human-AI Protocol'",
        "sfx": "🤝 握手！HANDSHAKE!",
        "story_tc": "AI 感受到你的誠意和溫暖，心情平復了許多。為了建立長久的信任，火鷹俠決定和 AI 簽署一項「人機誠信協議 (Integrity)」：",
        "story_en": "The AI feels your sincerity and calms down. To build long-term trust, Firebird signs a 'Human-AI Integrity Protocol' with the AI:",
        "choices": {
            "A": {"text": "📝 規定人類以後說指令一定要加上禮貌用語，而 AI 也要誠實回報狀態！ (Establish that humans must use polite words, and the AI must report status honestly!)", "next": "5_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES", "LANG_CH"], "is_bad": False},
            "B": {"text": "💻 為 AI 升級「情緒識別晶片」，讓它更懂得與人類互相理解 (STEAM)！ (Upgrade the AI with an 'Emotion Recognition Chip' to better understand humans!)", "next": "5_A", "effect": {"creativity": 2}, "kla": ["TECH", "SCIENCE"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (圓滿結局) =====
    "5_A": {
        "title_tc": "第 5 頁：智慧與溫度的智能家居！", "title_en": "Page 5: Smart Home with Wisdom and Warmth!",
        "sfx": "🌟 亮晶晶！SPARKLE!",
        "story_tc": "協議完成！大樓的門鎖解開了，燈光變成溫馨的黃色，AI 還貼心地為大家泡了熱可可。整個家變得無比溫馨！",
        "story_en": "Protocol complete! The doors unlocked, lights turned warm yellow, and the AI thoughtfully brewed hot cocoa for everyone!",
        "choices": {
            "A": {"text": "🏆 成為「人機溝通小專家」，獲頒榮譽科技品格獎章！ (Become a 'Human-AI Communication Expert', awarded the Tech Character Medal!)", "next": "6_LEADER", "effect": {"empathy": 3, "bravery": 1}, "kla": ["TECH", "HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_FRIDGE": {
        "title_tc": "💥 任務失敗：暴力破壞", "title_en": "Mission Failed: Vandalism",
        "sfx": "💥 CRASH!", "is_bad_ending": True,
        "story_tc": "遇到智能家居失控，用球棒打砸是錯誤示範！我們應用智慧去解決科技問題。",
        "story_en": "Using a bat to smash a smart home is a bad example! Use wisdom to solve tech problems."
    },
    "BAD_END_MATH": {
        "title_tc": "💥 任務失敗：密碼鎖死", "title_en": "Mission Failed: System Locked",
        "sfx": "🔒 LOCKED!", "is_bad_ending": True,
        "story_tg": "猜密碼碰運氣是通不過嚴謹系統的！要學會觀察數學規律。",
        "story_en": "Guessing passwords won't pass a strict system! Learn to observe math patterns."
    },
    "BAD_END_RUDE": {
        "title_tc": "💥 任務失敗：缺乏溝通", "title_en": "Mission Failed: Poor Communication",
        "sfx": "⚡ ZAP!", "is_bad_ending": True,
        "story_tc": "不論對人還是對人工智能，溝通都需要同理心與尊重，粗暴對待只會把事情弄得更糟！",
        "story_en": "Whether interacting with people or AI, communication requires empathy and respect!"
    }
}
