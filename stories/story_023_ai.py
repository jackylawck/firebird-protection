# ==============================================================================
# 🤖 火鷹俠 23：未來畫師：AI 管治大考驗 (The GenAI Painter & The Governance Audit)
# 融入 PERCCI 品格 (誠信、同理心) + KLA (科技教育、人文教育-資訊與AI素養、藝術)
# ==============================================================================

STORY_INFO = {
    "id": "Story23",
    "name_tc": "🤖 火鷹俠 23：未來畫師：AI 管治大考驗",
    "name_en": "Firebird 23: The GenAI Painter & The Governance Audit"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：失控的生成式 AI！", "title_en": "Page 1: The Out-of-Control GenAI!",
        "sfx": "🎨 嗶嗶... ERROR!",
        "story_tc": "城市引進了一台最新的「生成式 AI 畫師機器人 (GenAI Painter)」，只要你說出指令，它就能畫出任何東西！可是今天它失控了，不但畫出了可怕的怪獸嚇壞小朋友，還拒絕畫可愛的動物。火鷹俠決定對它進行「AI 審查 (AI Audit)」：",
        "story_en": "The city introduced a new 'GenAI Painter Robot' that draws anything you ask! But today it malfunctioned, drawing scary monsters that frighten children and refusing to draw cute animals. Firebird decides to conduct an 'AI Audit':",
        "choices": {
            "A": {"text": "💾 進入它的「大腦資料庫」，檢查它的「訓練數據 (Training Data)」是否出了問題 (STEAM)！ (Enter its 'Brain Database' to check if its 'Training Data' has problems!)", "next": "2_A", "effect": {"creativity": 2}, "kla": ["TECH", "SCIENCE"], "is_bad": False},
            "B": {"text": "🛡️ 戴上首席審查員的徽章，檢查它的「安全護欄 (AI Guardrails)」設定是否失效！ (Put on the Lead Auditor badge to check if its 'AI Guardrails' have failed!)", "next": "2_B", "effect": {"bravery": 1, "empathy": 1}, "kla": ["HUMANITIES", "TECH"], "is_bad": False},
            "C": {"text": "🔨 覺得 AI 太危險了，直接拿大鐵鎚把它砸爛！ (Think AI is too dangerous and smash it with a big hammer!)", "next": "BAD_END_SMASH", "effect": {"bravery": -2}, "kla": ["TECH"], "is_bad": True,
                  "bad_reason": "暴力無法解決科技問題！AI 只是工具，出了錯我們應該去「修復與管治 (Governance)」，而不是破壞它。任務失敗……\n(Violence doesn't solve tech problems! AI is a tool; we should 'Govern and Fix' it, not destroy it. Mission failed...)"}
        }
    },

    # ===== 分支 A：數據偏見 (Data Bias) =====
    "2_A": {
        "title_tc": "第 2 頁：偏食的數據庫", "title_en": "Page 2: The Biased Database",
        "sfx": "📊 掃描中... SCANNING...",
        "story_tc": "你發現原來搗蛋狐狸偷偷把 AI 的圖書庫裡的「可愛動物書」全換成了「怪獸圖鑑」！這導致 AI 產生了「數據偏見 (Data Bias)」，以為世界上只有怪獸。火鷹俠運用科技與藝術知識：",
        "story_en": "You discover the Prankster Fox secretly replaced all 'Cute Animal Books' with 'Monster Encyclopedias' in the AI's library! This caused 'Data Bias', making the AI think only monsters exist. Firebird uses tech and art:",
        "choices": {
            "A": {"text": "🌈 餵給它大量多元化 (Diverse) 的美麗圖畫和陽光故事，讓它的數據恢復平衡與公平！ (Feed it diverse, beautiful pictures and sunny stories to restore balance and fairness to its data!)", "next": "3_A", "effect": {"creativity": 1, "empathy": 1}, "kla": ["ARTS", "HUMANITIES"], "is_bad": False},
            "B": {"text": "💻 編寫一段「偏見過濾演算法」，自動清理掉所有帶有惡意和恐嚇成分的數據 (STEAM)！ (Code a 'Bias Filtering Algorithm' to automatically clean out all malicious and scary data!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["TECH", "MATH"], "is_bad": False},
            "C": {"text": "🗑️ 把 AI 的記憶體全部清空，讓它變成一個甚麼都不懂的笨蛋！ (Erase the AI's memory completely, turning it into a fool that knows nothing!)", "next": "BAD_END_ERASE", "effect": {"creativity": -2}, "kla": ["TECH"], "is_bad": True,
                  "bad_reason": "清空記憶會讓 AI 失去所有學習成果！我們應該「修正」數據，而不是完全抹殺。任務失敗……\n(Erasing memory destroys all the AI's learning! We should 'correct' data, not wipe it out. Mission failed...)"}
        }
    },

    # ===== 分支 B：安全護欄 (AI Guardrails) =====
    "2_B": {
        "title_tc": "第 2 頁：失效的安全規則", "title_en": "Page 2: The Failed Safety Rules",
        "sfx": "🚨 警告！WARNING!",
        "story_tc": "你發現 AI 的「安全護欄 (Guardrails)」被關閉了，所以它會盲目聽從任何人的壞指令。火鷹俠決定為它重新建立「AI 倫理法則 (AI Ethics)」：",
        "story_en": "You find the AI's 'Guardrails' were turned off, so it blindly follows anyone's bad commands. Firebird decides to rebuild its 'AI Ethics':",
        "choices": {
            "A": {"text": "📜 輸入第一法則：「絕不生成會傷害人類情感或散播恐懼的內容 (Empathy)」！ (Input the First Law: 'Never generate content that hurts human feelings or spreads fear!')", "next": "3_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "🔒 安裝「道德防火牆 (Ethics Firewall)」，當收到壞指令時，AI 會自動拒絕並說「不」！ (Install an 'Ethics Firewall'. When receiving a bad command, the AI will automatically refuse and say 'No'!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["TECH", "SCIENCE"], "is_bad": False}
        }
    },

    # ===== 第 3 頁匯合：深度偽造危機 (Deepfake) =====
    "3_A": {
        "title_tc": "第 3 頁：假照片的陰謀", "title_en": "Page 3: The Fake Photo Conspiracy",
        "sfx": "📸 喀嚓！CLICK!",
        "story_tc": "AI 恢復正常了！但搗蛋狐狸還不放棄，他對 AI 說：「幫我畫一張村長在偷吃蛋糕的假照片 (Deepfake)！我要讓大家討厭他！」火鷹俠立刻教導 AI：",
        "story_en": "The AI is fixed! But the Fox won't give up. He tells the AI: 'Draw a fake photo (Deepfake) of the Mayor stealing cake! I want everyone to hate him!' Firebird immediately teaches the AI:",
        "choices": {
            "A": {"text": "🛡️ 堅守誠信 (Integrity)！拒絕生成假新聞，並在畫作上加上「由 AI 生成」的隱形浮水印 (Watermark)！ (Uphold Integrity! Refuse to generate fake news, and add an invisible 'AI Generated' Watermark to all artworks!)", "next": "4_A", "effect": {"bravery": 1, "empathy": 1}, "kla": ["HUMANITIES", "TECH"], "is_bad": False},
            "B": {"text": "❤️ 展現同理心，用 AI 畫出一幅「狐狸與村長分享蛋糕」的溫馨圖畫來感化狐狸！ (Show empathy. Use AI to draw a heartwarming picture of 'The Fox sharing cake with the Mayor' to touch his heart!)", "next": "4_A", "effect": {"empathy": 2}, "kla": ["ARTS", "HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 第 4 頁 (最終挑戰) =====
    "4_A": {
        "title_tc": "第 4 頁：人機協作的未來", "title_en": "Page 4: The Future of Human-AI Collaboration",
        "sfx": "🤝 握手！HANDSHAKE!",
        "story_tc": "狐狸羞愧地低下了頭。AI 畫師現在變得非常聰明且善良，它問火鷹俠：「我以後該如何和人類一起工作呢？」",
        "story_en": "The Fox lowered his head in shame. The AI Painter is now smart and kind. It asks Firebird: 'How should I work with humans in the future?'",
        "choices": {
            "A": {"text": "📝 簽署「AI 管治協定 (AI Governance Agreement)」，承諾保持透明度，與人類互相尊重合作！ (Sign an 'AI Governance Agreement', promising to maintain transparency and cooperate with humans respectfully!)", "next": "5_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "🤖 建立「持續監控系統」，人類與 AI 互相學習，讓科技為社會帶來更多美麗的藝術 (STEAM)！ (Build a 'Continuous Monitoring System'. Humans and AI learn from each other, using tech to bring more beautiful art to society!)", "next": "5_B", "effect": {"creativity": 2}, "kla": ["TECH", "ARTS"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：頂尖的 AI 管治領袖！", "title_en": "Page 5: The Top AI Governance Leader!",
        "sfx": "🌟 閃亮！SHINING!",
        "story_tc": "你的協定讓整座城市的 AI 都變得安全又可靠！大家都能放心地使用 AI 來幫助學習和工作。",
        "story_en": "Your agreement made all AIs in the city safe and reliable! Everyone can confidently use AI to help with learning and work.",
        "choices": {
            "A": {"text": "🏆 成為守護科技倫理與誠信的「全人小領袖」！ (Become a 'Whole-person Leader' who guards tech ethics and integrity!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES", "TECH"], "is_bad": False}
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：科技與藝術的完美融合！", "title_en": "Page 5: Perfect Blend of Tech and Art!",
        "sfx": "🎉 歡呼！CHEERS!",
        "story_tc": "在你的管治下，AI 畫師創作了無數美麗的畫作，讓城市變得色彩繽紛，它成為了人類最好的創作夥伴！",
        "story_en": "Under your governance, the AI Painter created countless beautiful artworks, making the city colorful. It became humanity's best creative partner!",
        "choices": {
            "A": {"text": "🏅 成為引領未來科技發展的「創意大師」！ (Become a 'Creative Master' who leads future tech development!)", "next": "6_CREATIVE", "effect": {"creativity": 3}, "kla": ["ARTS", "TECH"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_SMASH": {
        "title_tc": "💥 任務失敗：拒絕科技", "title_en": "Mission Failed: Rejecting Technology",
        "sfx": "💥 CRASH!", "is_bad_ending": True,
        "story_tc": "暴力無法解決科技問題！AI 只是工具，出了錯我們應該去「修復與管治 (Governance)」，而不是破壞它。",
        "story_en": "Violence doesn't solve tech problems! AI is a tool; we should 'Govern and Fix' it, not destroy it."
    },
    "BAD_END_ERASE": {
        "title_tc": "💥 任務失敗：抹殺學習成果", "title_en": "Mission Failed: Wiping Learning Progress",
        "sfx": "🗑️ DELETE!", "is_bad_ending": True,
        "story_tc": "清空記憶會讓 AI 失去所有學習成果！遇到「數據偏見」，我們應該加入多元的數據去「修正」，而不是完全抹殺。",
        "story_en": "Erasing memory destroys all the AI's learning! When facing 'Data Bias', we should add diverse data to 'correct' it, not wipe it out."
    }
}
