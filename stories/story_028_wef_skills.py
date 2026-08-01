# ==============================================================================
# 🌟 火鷹俠 28：WEF聯盟：2030 未來人才競技場 (The 2030 Future Talent Arena)
# 融入 WEF 未來 10 大關鍵技能：分析性思維、韌性靈活性、同理心、終身學習、技術素養等
# KLA: 人文教育(生涯規劃與品格)、科技教育、數學教育
# ==============================================================================

STORY_INFO = {
    "id": "Story28",
    "name_tc": "🌟 火鷹俠 28：2030 未來人才競技場",
    "name_en": "Firebird 28: The 2030 Future Talent Arena"
}

SCENES = {
    # ===== 起始：應對變化的韌性 (Top 1 & 2 技能) =====
    "1_START": {
        "title_tc": "第 1 頁：不斷變形的迷宮", "title_en": "Page 1: The Shape-Shifting Maze",
        "sfx": "🔄 喀啦喀啦！SHIFTING!",
        "story_tc": "火鷹俠收到了「世界探索聯盟 (WEF)」的邀請，來到 2030 未來人才競技場！第一關是『變革迷宮』，這裡的牆壁每秒鐘都在改變形狀，過去的舊地圖完全失效了。廣播說：「近 40% 的技能將迎來重大變革！」火鷹俠決定：",
        "story_en": "Firebird is invited by the 'World Exploration Federation (WEF)' to the 2030 Future Talent Arena! The first stage is the 'Maze of Change'. The walls shift every second, making old maps useless. The broadcast says: 'Nearly 40% of skills will face major changes!' Firebird decides to:",
        "choices": {
            "A": {"text": "🧠 展現「分析性思維 (Analytical Thinking)」：冷靜觀察牆壁移動的規律，用邏輯推理出正確的出口！ (Show 'Analytical Thinking': Calmly observe the wall movement patterns and use logic to deduce the correct exit!)", "next": "2_A", "effect": {"creativity": 2}, "kla": ["MATH", "SCIENCE"], "is_bad": False},
            "B": {"text": "🏃‍♂️ 展現「韌性、靈活性與敏捷性 (Resilience & Agility)」：不害怕失敗，即使走錯路也立刻彈性調整策略，迅速找到新路線！ (Show 'Resilience & Agility': Unafraid of failure, flexibly adjust strategies even if on the wrong path, quickly finding a new route!)", "next": "2_A", "effect": {"bravery": 2, "creativity": 1}, "kla": ["PE", "HUMANITIES"], "is_bad": False},
            "C": {"text": "😡 生氣地大叫：「為什麼地圖沒用了！」然後坐在原地拒絕前進。 (Yell angrily: 'Why is the map useless?!' and sit there refusing to move.)", "next": "BAD_END_RESILIENCE", "effect": {"bravery": -2}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "未來的環境變化極快，缺乏「韌性與適應力」的人會被淘汰。你被困在迷宮裡了，任務失敗……\n(Future environments change rapidly. Those lacking 'resilience and adaptability' will be eliminated. You are trapped. Mission failed...)"}
        }
    },

    # ===== 分支 A：軟硬技能的平衡 (Top 4 & 6 技能) =====
    "2_A": {
        "title_tc": "第 2 頁：癱瘓的中央數據塔", "title_en": "Page 2: The Paralyzed Central Data Tower",
        "sfx": "💻 嗶嗶... ERROR...",
        "story_tc": "你成功走出迷宮！接著你發現競技場的中央數據塔遭到病毒攻擊，系統癱瘓。大會提示：「未來競爭力的關鍵，在於軟硬技能兼具！」火鷹俠必須修復它：",
        "story_en": "You escaped the maze! Next, you find the Central Data Tower paralyzed by a virus. The system hints: 'The key to future competitiveness is balancing hard and soft skills!' Firebird must fix it:",
        "choices": {
            "A": {"text": "🤖 運用「技術素養 (Tech Literacy)」：使用 AI 與大數據工具，快速掃描並清除病毒代碼 (硬技能)！ (Use 'Tech Literacy': Use AI and Big Data tools to quickly scan and clear the virus code!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["TECH", "MATH"], "is_bad": False},
            "B": {"text": "💡 運用「創意思維 (Creative Thinking)」：發明一種全新的光波傳導方式，繞過受損的系統重新啟動數據塔 (軟技能)！ (Use 'Creative Thinking': Invent a new light-wave conduction method to bypass the damaged system and reboot the tower!)", "next": "3_A", "effect": {"creativity": 2, "bravery": 1}, "kla": ["ARTS", "SCIENCE"], "is_bad": False},
            "C": {"text": "🔨 拿出大鐵鎚，試圖用敲打的方式把電腦修好！ (Take out a big hammer, trying to fix the computer by smashing it!)", "next": "BAD_END_HARD_SKILLS", "effect": {"creativity": -2}, "kla": ["TECH"], "is_bad": True,
                  "bad_reason": "只靠舊有的體力方法是無法解決未來科技問題的！你需要提升「技術素養 (Tech Literacy)」。任務失敗……\n(Old physical methods can't solve future tech problems! You need to improve your 'Tech Literacy'. Mission failed...)"}
        }
    },

    # ===== 第 3 頁：跨世代與團隊管理 (Top 3, 7, 9 技能) =====
    "3_A": {
        "title_tc": "第 3 頁：吵架的跨世代小隊", "title_en": "Page 3: The Arguing Cross-Generational Squad",
        "sfx": "🗣️ 爭吵聲！ARGUING!",
        "story_tc": "系統修復了！最後一關是「團隊合作」。大會分配給你一支隊伍：裡面有年長的高齡魔法師，也有年輕的科技小精靈。他們因為代溝和做事方法不同而吵了起來。火鷹俠決定展現未來領袖的特質：",
        "story_en": "System restored! The final stage is 'Teamwork'. You are assigned a squad: older senior wizards and young tech sprites. They are arguing over generation gaps and different methods. Firebird decides to show future leadership traits:",
        "choices": {
            "A": {"text": "❤️ 展現「同理心與積極傾聽」：耐心聽取長輩的經驗與年輕人的創意，讓雙方互相理解！ (Show 'Empathy & Active Listening': Patiently listen to the elders' experience and the youth's creativity, helping them understand each other!)", "next": "4_A", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "👑 展現「領導力與人才管理」：發現每個人的優點，將高齡魔法師的智慧與小精靈的科技完美結合，發揮最大戰力！ (Show 'Leadership & Talent Management': Discover everyone's strengths, perfectly combining the elders' wisdom with the sprites' tech for max power!)", "next": "4_A", "effect": {"empathy": 2, "bravery": 1}, "kla": ["HUMANITIES", "TECH"], "is_bad": False}
        }
    },

    # ===== 第 4 頁：終極提問 (Top 5 & 8 技能) =====
    "4_A": {
        "title_tc": "第 4 頁：終身學習的誓言", "title_en": "Page 4: The Vow of Lifelong Learning",
        "sfx": "✨ 聖光！HOLY LIGHT!",
        "story_tc": "小隊團結一致，成功抵達了終點！WEF 聯盟主席現身，問了你最後一個問題：「火鷹俠，未來的科技會不斷淘汰舊技能，當你今天學會的知識明天變得沒用時，你該怎麼辦？」",
        "story_en": "The united squad successfully reaches the finish line! The WEF President appears and asks one last question: 'Firebird, future tech will obsolete old skills. What will you do when what you learned today becomes useless tomorrow?'",
        "choices": {
            "A": {"text": "📖 展現「好奇心與終身學習 (Lifelong Learning)」：我會永遠保持好奇心，不斷學習新技能，不怕從頭開始！ (Show 'Curiosity & Lifelong Learning': I will always stay curious, continuously learn new skills, and never fear starting over!)", "next": "5_A", "effect": {"creativity": 2, "empathy": 1}, "kla": ["HUMANITIES", "SCIENCE"], "is_bad": False},
            "B": {"text": "🔥 展現「動機與自我意識 (Motivation & Self-awareness)」：我會清楚認識自己的價值，保持強大的內在動力，迎接所有未知的挑戰！ (Show 'Motivation & Self-awareness': I will clearly know my value, keep strong internal motivation, and embrace all unknown challenges!)", "next": "5_B", "effect": {"bravery": 3}, "kla": ["HUMANITIES", "PE"], "is_bad": False}
        }
    },

    # ===== 第 5 頁：結局 =====
    "5_A": {
        "title_tc": "第 5 頁：終身學習的頂尖人才！", "title_en": "Page 5: The Lifelong Learning Top Talent!",
        "sfx": "🏆 頒獎音樂！VICTORY MUSIC!",
        "story_tc": "主席讚賞地點點頭：「沒錯！好奇心與終身學習，才是永遠不會被淘汰的終極武器！」你獲得了 2030 年未來人才的最高榮譽！",
        "story_en": "The President nods in approval: 'Exactly! Curiosity and lifelong learning are the ultimate weapons that will never be obsolete!' You received the highest honor for 2030 Future Talents!",
        "choices": {
            "A": {"text": "🌟 帶著 10 大關鍵技能，成為引領未來的「全人小領袖」！ (Take the Top 10 Key Skills and become a 'Whole-person Leader' guiding the future!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：充滿動力的變革引領者！", "title_en": "Page 5: The Motivated Change Leader!",
        "sfx": "👏 掌聲如雷！APPLAUSE!",
        "story_tc": "主席激動地說：「擁有強大自我意識與動機的人，不僅能適應變革，更能『創造』變革！」你帶領著跨世代團隊，成為了新時代的英雄。",
        "story_en": "The President says excitedly: 'Those with strong self-awareness and motivation don't just adapt to change, they create it!' You led the cross-generational team and became a hero of the new era.",
        "choices": {
            "A": {"text": "🏅 繼續平衡軟硬技能，成為最搶手的「創意大師」！ (Continue balancing hard and soft skills, becoming the most sought-after 'Creative Master'!)", "next": "6_CREATIVE", "effect": {"creativity": 3}, "kla": ["TECH", "HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_RESILIENCE": {
        "title_tc": "💥 任務失敗：缺乏韌性", "title_en": "Mission Failed: Lack of Resilience",
        "sfx": "📉 GAME OVER!", "is_bad_ending": True,
        "story_tc": "在快速變遷的環境中，『韌性、靈活性與敏捷性』的重要性不亞於專業技能。遇到挫折就放棄，是無法成為搶手人才的！",
        "story_en": "In a fast-changing environment, 'Resilience, Flexibility & Agility' are as important as professional skills. Giving up at setbacks won't make you a sought-after talent!"
    },
    "BAD_END_HARD_SKILLS": {
        "title_tc": "💥 任務失敗：缺乏技術素養", "title_en": "Mission Failed: Lack of Tech Literacy",
        "sfx": "❌ ERROR!", "is_bad_ending": True,
        "story_tc": "未來競爭力的關鍵是『軟硬技能兼具』。面對 AI 和大數據時代，我們必須具備足夠的『技術素養』來解決問題！",
        "story_en": "The key to future competitiveness is 'Balancing Hard & Soft Skills'. In the age of AI and Big Data, we must have enough 'Tech Literacy' to solve problems!"
    }
}
