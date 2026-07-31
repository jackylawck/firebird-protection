# ==============================================================================
# 🤖 火鷹俠 6：編程迷宮之城 (The Coding Maze City)
# 融入 PERCCI 品格 (堅毅、同理心) + KLA (科技教育、數學、小學人文)
# ==============================================================================

STORY_INFO = {
    "id": "Story6",
    "name_tc": "🤖 火鷹俠 6：編程迷宮之城",
    "name_en": "Firebird 6: The Coding Maze City"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：大擠塞！失控的交通", "title_en": "Page 1: Traffic Jam! Out of Control",
        "sfx": "🚗 叭叭！BEEP BEEP!",
        "story_tc": "大事不好了！「迷宮之城」的交通人工智能（AI）感染了「搗蛋病毒」，所有的紅綠燈亂閃，無人駕駛汽車撞成一團！火鷹俠決定將自己數碼化，進入電腦世界除錯（Debugging）：",
        "story_en": "Oh no! The Traffic AI of Maze City is infected by a 'Prankster Bug'. Traffic lights are flashing wildly and self-driving cars are crashing! Firebird digitizes himself to enter the computer world for debugging:",
        "choices": {
            "A": {"text": "🛹 踩上「光速數據滑板」，順著電路網滑進去！ (Ride the Light-speed Data Hoverboard into the circuits!)", "next": "2_A", "effect": {"bravery": 1}, "kla": ["TECH", "PE"], "is_bad": False},
            "B": {"text": "🔍 拿出超級放大鏡，找出病毒留下的隱藏入口！ (Use a super magnifying glass to find the bug's hidden entrance!)", "next": "2_B", "effect": {"creativity": 1}, "kla": ["SCIENCE"], "is_bad": False},
            "C": {"text": "🔨 用大錘子用力敲打電腦螢幕！ (Hit the computer screen hard with a giant hammer!)", "next": "BAD_END_SCREEN", "effect": {"bravery": -1}, "kla": [], "is_bad": True,
                  "bad_reason": "用蠻力破壞電腦是無法解決問題的！螢幕碎了，你也進不去電腦世界了。任務失敗……\n(Brute force doesn't fix computers! The screen broke and you can't enter. Mission failed...)"}
        }
    },

    # ===== 分支 A：滑板路線 =====
    "2_A": {
        "title_tc": "第 2 頁：斷掉的代碼橋", "title_en": "Page 2: The Broken Code Bridge",
        "sfx": "🧩 咔噠！CLICK!",
        "story_tc": "滑板飛到一半，遇到了一條斷掉的代碼橋！橋面上有著「紅、黃、藍、紅、黃、？」的顏色規律，火鷹俠必須補上正確的方塊：",
        "story_en": "Halfway there, you find a broken code bridge! It has a color pattern: 'Red, Yellow, Blue, Red, Yellow, ?'. Firebird must place the correct block:",
        "choices": {
            "A": {"text": "🟦 放入「藍色方塊」，完成規律重建橋樑！ (Place the 'Blue Block' to complete the pattern and fix the bridge!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["MATH", "TECH"], "is_bad": False},
            "B": {"text": "🎨 發揮創意，用彩虹油漆自己畫一條全新的橋！ (Use creativity to paint a brand new rainbow bridge!)", "next": "3_A", "effect": {"creativity": 2, "bravery": 1}, "kla": ["ARTS"], "is_bad": False},
            "C": {"text": "🟥 隨便放入「紅色方塊」碰碰運氣！ (Just place a 'Red Block' and test your luck!)", "next": "BAD_END_PATTERN", "effect": {"creativity": -1}, "kla": ["MATH"], "is_bad": True,
                  "bad_reason": "規律錯誤！代碼橋承受不住重量塌陷了，你掉了下去！任務失敗……\n(Wrong pattern! The code bridge collapsed and you fell! Mission failed...)"}
        }
    },

    # ===== 分支 B：放大鏡尋找路線 =====
    "2_B": {
        "title_tc": "第 2 頁：防毒牆的數學挑戰", "title_en": "Page 2: The Firewall's Math Challenge",
        "sfx": "🧱 嗡嗡！HUMMM!",
        "story_tc": "你找到了隱藏入口，但有一道嚴格的「防火牆」擋住去路。防火牆問：「要通過這裡，請回答 2 + 3 等於多少？」",
        "story_en": "You found the hidden entrance, but a strict Firewall blocks the way. It asks: 'To pass, answer what is 2 + 3?'",
        "choices": {
            "A": {"text": "🔢 大聲且自信地回答：「答案是 5！」 (Answer loudly and confidently: 'The answer is 5!')", "next": "3_A", "effect": {"bravery": 1}, "kla": ["MATH"], "is_bad": False},
            "B": {"text": "🤝 有禮貌地向防火牆打招呼，並請求他通融一下。 (Politely greet the Firewall and ask for a favor to pass.)", "next": "3_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES", "LANG_EN"], "is_bad": False},
            "C": {"text": "🏃‍♂️ 不理會問題，低著頭直接硬闖過去！ (Ignore the question and dash through blindly!)", "next": "BAD_END_FIREWALL", "effect": {"bravery": -2}, "kla": ["TECH"], "is_bad": True,
                  "bad_reason": "防火牆啟動了防禦機制，把你彈飛出了電腦世界！我們應該遵守系統規則。任務失敗……\n(The firewall activated its defense and bounced you out! We must follow system rules. Mission failed...)"}
        }
    },

    # ===== 第 3 頁匯合 =====
    "3_A": {
        "title_tc": "第 3 頁：暈頭轉向的人工智能", "title_en": "Page 3: The Dizzy AI",
        "sfx": "🌀 轉轉轉！SPIN!",
        "story_tc": "成功進入核心！你發現交通 AI 正被病毒困在一個「無限迴圈 (Infinite Loop)」裡，不停地原地轉圈圈，頭都暈了！火鷹俠決定：",
        "story_en": "You reached the core! The Traffic AI is trapped in an 'Infinite Loop' by the bug, spinning endlessly and getting dizzy! Firebird decides to:",
        "choices": {
            "A": {"text": "🛑 找出鍵盤上的「暫停 (Break)」按鈕，解除迴圈！ (Find the 'Break' button on the keyboard to stop the loop!)", "next": "4_A", "effect": {"creativity": 1, "bravery": 1}, "kla": ["TECH", "SCIENCE"], "is_bad": False},
            "B": {"text": "🫂 衝進去緊緊抱住 AI，用體溫與愛心讓他冷靜下來！ (Rush in and hug the AI tightly, using warmth to calm it down!)", "next": "4_A", "effect": {"empathy": 2}, "kla": ["PE", "HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 第 4 頁 (反派現身) =====
    "4_A": {
        "title_tc": "第 4 頁：搗蛋病毒的分身術！", "title_en": "Page 4: The Bug's Clones!",
        "sfx": "👾 嘻嘻！HEE HEE!",
        "story_tc": "AI 得救了！但搗蛋病毒出現，變出好多個分身，把城市紅綠燈的程式碼全部弄亂了！",
        "story_en": "The AI is saved! But the Prankster Bug appears, cloning itself and messing up all the traffic light codes!",
        "choices": {
            "A": {"text": "💻 運用編程思維，重新排列「紅燈停、綠燈行」的正確順序！ (Use coding logic to rearrange the 'Red for stop, Green for go' sequence!)", "next": "5_A", "effect": {"creativity": 2}, "kla": ["TECH", "HUMANITIES"], "is_bad": False},
            "B": {"text": "🎵 播放強勁的音樂，讓病毒跟著節奏跳舞，趁機奪回控制權！ (Play loud music to make the bugs dance, taking back control!)", "next": "5_A", "effect": {"creativity": 1, "empathy": 1}, "kla": ["ARTS"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (決戰與結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：重寫程式碼！", "title_en": "Page 5: Rewrite the Code!",
        "sfx": "✨ 滴答！BINGO!",
        "story_tc": "交通燈恢復正常了，搗蛋病毒也失去了力氣，跌坐在地上。火鷹俠準備處置這個病毒：",
        "story_en": "The traffic lights are back to normal. The Prankster Bug lost its power and sat on the ground. Firebird prepares to deal with it:",
        "choices": {
            "A": {"text": "♻️ 展現包容與創意，將它改寫成「防毒小助手」，一起保護城市！ (Show inclusivity and rewrite it into an 'Anti-Virus Helper' to protect the city!)", "next": "6_LEADER", "effect": {"empathy": 3, "creativity": 1}, "kla": ["HUMANITIES", "TECH"], "is_bad": False},
            "B": {"text": "🛡️ 堅守原則，勇敢地將病毒永久刪除，徹底消滅威脅！ (Stick to the rules and bravely delete the bug permanently!)", "next": "6_HERO", "effect": {"bravery": 3}, "kla": ["SCIENCE", "TECH"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_SCREEN": {
        "title_tc": "💥 任務失敗：破壞公物", "title_en": "Mission Failed: Vandalism",
        "sfx": "💥 BOOM!", "is_bad_ending": True,
        "story_tc": "遇到科技問題時，用暴力破壞硬體是解決不了軟件問題的！我們要冷靜思考。",
        "story_en": "Using violence on hardware doesn't solve software problems! We must think calmly."
    },
    "BAD_END_PATTERN": {
        "title_tc": "💥 任務失敗：邏輯錯誤", "title_en": "Mission Failed: Logic Error",
        "sfx": "📉 FALL!", "is_bad_ending": True,
        "story_tc": "編程與數學都需要仔細觀察規律（Pattern）。請返回上一頁再數一次顏色吧！",
        "story_en": "Coding and math require careful observation of patterns. Go back and check the colors again!"
    },
    "BAD_END_FIREWALL": {
        "title_tc": "💥 任務失敗：硬闖防線", "title_en": "Mission Failed: Bypassing Security",
        "sfx": "🛡️ ZAP!", "is_bad_ending": True,
        "story_tc": "網絡安全是很重要的，我們不能硬闖不明的防火牆。要用智慧解開密碼！",
        "story_en": "Cybersecurity is important. We can't force our way through firewalls. Use your wisdom!"
    }
}
