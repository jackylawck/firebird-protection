# ==============================================================================
# 🎓 火鷹俠 10：IB 魔法學院 (一) - 三大核心的試煉
# 視覺化 IBDP 核心架構：TOK (思考)、EE (獨立研究)、CAS (全人發展)
# ==============================================================================

STORY_INFO = {
    "id": "Story10_Ep1",
    "name_tc": "🎓 火鷹俠 10：IB 魔法學院 (一) 三大核心",
    "name_en": "Firebird 10: IB Magic Academy (Part 1)"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：神秘的雲端學院", "title_en": "Page 1: The Cloud Academy",
        "sfx": "✨ 閃耀！SPARKLE!",
        "story_tc": "火鷹俠收到了一封會發光的邀請函，來到了漂浮在雲端的「IB 魔法學院」。貓頭鷹校長說：「要成為頂尖魔法師，你必須先收集『三大核心寶物』！」火鷹俠看著眼前的三條岔路，決定先挑戰：",
        "story_en": "Firebird received a glowing invitation to the floating 'IB Magic Academy'. The Owl Headmaster says: 'To become a top wizard, you must first collect the Three Core Relics!' Firebird looks at three paths and chooses:",
        "choices": {
            "A": {"text": "🪞 走向迷霧森林，尋找會問問題的「真理之鏡 (TOK)」！ (Walk into the misty forest to find the questioning 'Mirror of Truth'!)", "next": "2_A", "effect": {"creativity": 1}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "📜 爬上古老的高塔，尋找空白的「探險長卷 (EE)」！ (Climb the ancient tower to find the blank 'Explorer's Scroll'!)", "next": "2_B", "effect": {"bravery": 1}, "kla": ["LANG_CH", "TECH"], "is_bad": False},
            "C": {"text": "🎮 覺得找寶物太累了，坐在門口玩魔法遊戲機！ (Think finding relics is too tiring, sit at the gate and play magical video games!)", "next": "BAD_END_LAZY", "effect": {"bravery": -2}, "kla": [], "is_bad": True,
                  "bad_reason": "魔法學院的訓練需要堅毅 (Perseverance)！放棄挑戰就永遠無法獲得強大的魔法力量了。任務失敗……\n(Magic training requires perseverance! Giving up means you'll never gain the magic power. Mission failed...)"}
        }
    },

    # ===== 分支 A：真理之鏡 (TOK 知識理論) =====
    "2_A": {
        "title_tc": "第 2 頁：真理之鏡的謎語", "title_en": "Page 2: Riddle of the Truth Mirror",
        "sfx": "🤔 嗡嗡... HUMMM...",
        "story_tc": "你找到了「真理之鏡」。鏡子沒有照出你的樣子，反而問你：「你怎麼知道蘋果是甜的？是因為別人告訴你，還是你親自咬過？」火鷹俠展現批判性思考 (Critical Thinking)：",
        "story_en": "You found the 'Mirror of Truth'. Instead of your reflection, it asks: 'How do you know an apple is sweet? Did someone tell you, or did you bite it?' Firebird shows critical thinking:",
        "choices": {
            "A": {"text": "🍎 勇敢回答：「我不盲目相信，我會親自去吃一口來驗證真相！」 (Answer bravely: 'I don't blindly believe. I will take a bite to verify the truth myself!')", "next": "3_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "HUMANITIES"], "is_bad": False},
            "B": {"text": "📚 回答：「我會去圖書館查閱 100 本關於蘋果的書來找出證據！」 (Answer: 'I will read 100 books about apples in the library to find evidence!')", "next": "3_A", "effect": {"creativity": 1, "bravery": 1}, "kla": ["LANG_CH"], "is_bad": False},
            "C": {"text": "🙉 摀住耳朵說：「我不想思考，你直接把答案告訴我吧！」 (Cover your ears and say: 'I don't want to think, just tell me the answer!')", "next": "BAD_END_THINK", "effect": {"creativity": -2}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "真理之鏡最討厭不肯自己思考的人！鏡子起了一層大霧，把你困在森林裡了。任務失敗……\n(The Mirror dislikes those who won't think for themselves! A thick fog trapped you in the forest. Mission failed...)"}
        }
    },

    # ===== 分支 B：探險長卷 (EE 延伸論文) =====
    "2_B": {
        "title_tc": "第 2 頁：空白的探險長卷", "title_en": "Page 2: The Blank Explorer's Scroll",
        "sfx": "📜 嘩啦！FLUTTER!",
        "story_tc": "你找到了「探險長卷」，但上面一個字都沒有！守護精靈說：「你必須自己選一個感興趣的題目，親自去調查，並在上面畫滿 4000 個魔法印記 (字) 才能過關！」火鷹俠決定：",
        "story_en": "You found the 'Explorer's Scroll', but it's completely blank! The sprite says: 'You must choose a topic you love, research it yourself, and fill it with 4,000 magic marks (words)!' Firebird decides to:",
        "choices": {
            "A": {"text": "🔍 選擇研究「火山為甚麼會噴火」，帶上放大鏡親自去火山口收集資料！ (Choose to research 'Why volcanoes erupt', and take a magnifying glass to the crater!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["SCIENCE"], "is_bad": False},
            "B": {"text": "🤖 選擇研究「機器人歷史」，訪問學院裡所有的機械工匠並仔細記錄！ (Choose to research 'Robot History', interview all the mechanics in the academy and take notes!)", "next": "3_A", "effect": {"empathy": 1, "creativity": 1}, "kla": ["TECH", "HUMANITIES"], "is_bad": False},
            "C": {"text": "📋 偷偷抄寫旁邊同學的卷軸交功課！ (Secretly copy the scroll of the student next to you!)", "next": "BAD_END_COPY", "effect": {"empathy": -3}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "這是不誠實 (Lack of Integrity) 的行為！魔法卷軸發現你抄襲，立刻變成了一堆灰燼！任務失敗……\n(This is dishonest! The magic scroll detected cheating and turned into ashes immediately! Mission failed...)"}
        }
    },

    # ===== 第 3 頁匯合：全能勇者 (CAS 創意、行動、服務) =====
    "3_A": {
        "title_tc": "第 3 頁：全能勇者的三個徽章", "title_en": "Page 3: The Three Badges of the All-Rounder",
        "sfx": "🛡️ 噹！CLANG!",
        "story_tc": "你成功取得了前兩件寶物！最後，你遇到了「行動巨人 (CAS)」。他要求你在離開學院前，必須集齊三個徽章：畫一幅畫 (創意)、跑一圈操場 (行動)、幫助一個朋友 (服務)。",
        "story_en": "You got the first two relics! Finally, you meet the 'Action Golem (CAS)'. He requires you to collect three badges before leaving: Paint a picture (Creativity), Run a lap (Activity), and Help a friend (Service).",
        "choices": {
            "A": {"text": "🎨🏃‍♂️🤝 充滿活力地完成畫畫、跑步，並扶起跌倒的小魔法師，寫下開心的反思日記！ (Energetically complete the painting, running, help a fallen wizard, and write a happy reflection diary!)", "next": "4_A", "effect": {"empathy": 2, "bravery": 1}, "kla": ["ARTS", "PE", "HUMANITIES"], "is_bad": False},
            "B": {"text": "抱怨說：「我只喜歡看書，不想運動也不想畫畫！」 (Complain: 'I only like reading. I don't want to exercise or paint!')", "next": "BAD_END_CAS", "effect": {"bravery": -1}, "kla": ["PE", "ARTS"], "is_bad": True,
                  "bad_reason": "頂尖魔法師必須是「全人發展」的！只顧著讀書而忽略運動和幫助別人，是無法拿到徽章的。任務失敗……\n(Top wizards must be 'well-rounded'! Only reading while ignoring sports and helping others won't earn the badges. Mission failed...)"}
        }
    },

    # ===== 第 4 頁：結算 =====
    "4_A": {
        "title_tc": "第 4 頁：核心力量的覺醒", "title_en": "Page 4: Awakening of the Core Power",
        "sfx": "🌟 轟動！WHOOSH!",
        "story_tc": "太棒了！真理之鏡、探險長卷和全能勇者徽章在你的手中融合，爆發出強大的「核心魔法光芒」！你獲得了額外的 3 分獎勵魔力！",
        "story_en": "Excellent! The Mirror, the Scroll, and the Badges merge in your hands, bursting with powerful 'Core Magic Light'! You gained 3 bonus magic points!",
        "choices": {
            "A": {"text": "🚪 帶著這股核心力量，準備推開下一關「六大元素學科之門」！ (Take this core power and prepare to open the next stage: The Six Elemental Subject Doors!)", "next": "5_A", "effect": {"bravery": 2}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 第 5 頁：圓滿結局 =====
    "5_A": {
        "title_tc": "第 5 頁：首部曲通關！", "title_en": "Page 5: Part 1 Cleared!",
        "sfx": "🎉 歡呼！CHEERS!",
        "story_tc": "你學會了獨立思考、深入研究和全方位發展！貓頭鷹校長為你鼓掌，你已經打好了成為頂尖學者的最強基礎！",
        "story_en": "You learned independent thinking, deep research, and all-round development! The Headmaster claps for you. You've built the strongest foundation to be a top scholar!",
        "choices": {
            "A": {"text": "🏆 成為具備批判思考與關懷精神的「全人小領袖」！ (Become a 'Whole-person Leader' with critical thinking and a caring spirit!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_LAZY": {
        "title_tc": "💥 任務失敗：半途而廢", "title_en": "Mission Failed: Giving Up",
        "sfx": "📉 FALL!", "is_bad_ending": True,
        "story_tc": "魔法學院的訓練需要堅毅的精神。貪圖安逸就永遠無法獲得強大的魔法力量！",
        "story_en": "Magic training requires perseverance. Giving up for comfort means you'll never gain the magic power!"
    },
    "BAD_END_THINK": {
        "title_tc": "💥 任務失敗：拒絕思考", "title_en": "Mission Failed: Refusing to Think",
        "sfx": "🌫️ FOG!", "is_bad_ending": True,
        "story_tc": "「知識理論 (TOK)」教導我們要主動質疑和尋找真相，不能總是等別人給我們答案！",
        "story_en": "'Theory of Knowledge (TOK)' teaches us to question and seek truth actively, not just wait for answers!"
    },
    "BAD_END_COPY": {
        "title_tc": "💥 任務失敗：抄襲作弊", "title_en": "Mission Failed: Plagiarism",
        "sfx": "🔥 ASHES!", "is_bad_ending": True,
        "story_tc": "做學問最重要的就是「誠信 (Integrity)」。抄襲別人的心血是絕對不容許的！",
        "story_en": "The most important thing in learning is 'Integrity'. Copying others' hard work is strictly forbidden!"
    },
    "BAD_END_CAS": {
        "title_tc": "💥 任務失敗：缺乏全人發展", "title_en": "Mission Failed: Lack of Well-roundedness",
        "sfx": "❌ ERROR!", "is_bad_ending": True,
        "story_tc": "我們不僅要讀書，還要多做運動保持健康，並且用創意和愛心去服務社會！這就是 CAS 的精神。",
        "story_en": "We must not only study but also exercise, and use creativity and love to serve society! This is the spirit of CAS."
    }
}
