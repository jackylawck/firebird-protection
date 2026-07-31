# ==============================================================================
# 📗 火鷹俠 3：深海龍宮大拯救 (Deep Sea Rescue)
# 融入 PERCCI 品格 (承擔、同理心) + STEAM (環保科技、海洋生態)
# ==============================================================================

STORY_INFO = {
    "id": "Story3",
    "name_tc": "📗 火鷹俠 3：深海龍宮大拯救",
    "name_en": "Firebird 3: Deep Sea Rescue"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：海洋珍珠不見了！", "title_en": "Page 1: The Missing Ocean Pearl!",
        "sfx": "🫧 咕嚕！GLUG!",
        "story_tc": "大事不好了！「八爪魚大王」拿走了能淨化海水的「超級珍珠」！海洋變得十分混濁。火鷹俠決定潛入深海拯救海洋生態，展現承擔精神：",
        "story_en": "Oh no! The Octopus took the Pearl that purifies the ocean! Firebird decides to dive deep to protect nature, showing commitment:",
        "choices": {
            "A": {"text": "⛴️ 駕駛利用水壓原理設計的「STEAM 潛水艇」！ (Pilot a STEAM Submarine based on water pressure!)", "next": "2_A", "effect": {"creativity": 2}, "is_bad": False},
            "B": {"text": "🐬 變身為太陽能「機械海豚」游入深海！ (Transform into a Solar Robot Dolphin!)", "next": "2_B", "effect": {"creativity": 1}, "is_bad": False},
            "C": {"text": "🍬 吞下神奇水泡糖，直接在水底呼吸！ (Eat a Magic Bubblegum to breathe underwater!)", "next": "2_C", "effect": {"bravery": 1}, "is_bad": False}
        }
    },

    # ===== 分支 A：潛水艇路線 =====
    "2_A": {
        "title_tc": "第 2 頁：遇見大白鯊！", "title_en": "Page 2: Meeting the Great White Shark!",
        "sfx": "🦈 咔嚓！CHOMP!",
        "story_tc": "潛水艇遇到一隻張開大嘴的鯊魚擋住了去路！火鷹俠決定展現同理心去了解原因：",
        "story_en": "A Great White Shark blocks the way with its mouth wide open! Firebird shows empathy to understand why:",
        "choices": {
            "A": {"text": "🩺 發現鯊魚只是牙齒卡住了木頭，溫柔地幫他拔除！ (Help remove a stick stuck in his teeth gently!)", "next": "3_A", "effect": {"empathy": 2}, "is_bad": False},
            "B": {"text": "🎶 打開廣播，播放溫柔的音樂哄他睡覺！ (Play a gentle lullaby to help him sleep!)", "next": "3_A", "effect": {"creativity": 1}, "is_bad": False},
            "C": {"text": "⚔️ 發射魚雷攻擊大白鯊！ (Shoot torpedoes at the Great White Shark!)", "next": "BAD_END_SHARK", "effect": {"empathy": -2}, "is_bad": True,
                  "bad_reason": "傷害海洋生物是不對的！大白鯊非常生氣，一口咬壞了潛水艇的螺旋槳！任務失敗……\n(Hurting marine life is wrong! The angry shark bit your submarine! Mission failed...)"}
        }
    },

    # ===== 分支 B：機械海豚路線 =====
    "2_B": {
        "title_tc": "第 2 頁：迷失發光水母森林！", "title_en": "Page 2: Lost in the Jellyfish Forest!",
        "sfx": "⚡ 滋滋！ZAP!",
        "story_tc": "機械海豚不小心衝進了發電水母森林！火鷹俠決定展現尊重與禮貌：",
        "story_en": "Crashed into an electric jellyfish forest! Firebird shows respect and politeness:",
        "choices": {
            "A": {"text": "🙏 有禮貌地向水母說明來意，請求讓路！ (Politely explain your quest and request passage!)", "next": "3_A", "effect": {"empathy": 2}, "is_bad": False},
            "B": {"text": "🧽 變出超級海綿裝甲，把靜電全部吸走！ (Equip Super Sponge Armor to absorb the electricity!)", "next": "3_A", "effect": {"creativity": 1}, "is_bad": False},
            "C": {"text": "💨 仗著自己速度快，不理會水母直接硬闖！ (Ignore the jellyfish and dash through blindly!)", "next": "BAD_END_CRASH", "effect": {"bravery": -1}, "is_bad": True,
                  "bad_reason": "在未知水域亂衝亂撞是很危險的！你不小心撞到水母，被靜電電暈了！任務失敗……\n(Reckless swimming is dangerous! You got zapped by jellyfish! Mission failed...)"}
        }
    },

    # ===== 分支 C：水泡糖路線 =====
    "2_C": {
        "title_tc": "第 2 頁：黑漆漆的海底裂縫！", "title_en": "Page 2: The Dark Ocean Trench!",
        "sfx": "🦇 呼呼！WHOOSH!",
        "story_tc": "前面是黑漆漆的海底裂縫！火鷹俠決定展現勇氣與 STEAM 技能：",
        "story_en": "Ahead is a pitch-black trench! Firebird shows courage and STEAM skills:",
        "choices": {
            "A": {"text": "💡 利用 LED 燈組裝超亮頭燈照射前路 (STEAM)！ (Build a bright LED headlight to light the way!)", "next": "3_A", "effect": {"creativity": 2}, "is_bad": False},
            "B": {"text": "🦑 呼叫一百隻會發光的螢火魷魚來幫忙照路！ (Call 100 glowing firefly squids to light the way!)", "next": "3_A", "effect": {"empathy": 1}, "is_bad": False}
        }
    },

    # ===== 第 3 頁匯合 =====
    "3_A": {
        "title_tc": "第 3 頁：八爪魚大王的心事", "title_en": "Page 3: The Octopus's Secret",
        "sfx": "🐙 噗嚕嚕！BLUB BLUB!",
        "story_tc": "終於找到八爪魚大王了！原來他是因為人類亂丟垃圾，令海洋變得很髒而生氣，才拿走珍珠的。火鷹俠決定：",
        "story_en": "Found the Octopus! He took the pearl because the ocean is full of human trash. Firebird decides to:",
        "choices": {
            "A": {"text": "🧹 號召全體海洋生物，進行垃圾分類與海洋大清潔！ (Organize sealife to recycle and clean up the ocean!)", "next": "4_A", "effect": {"bravery": 1, "empathy": 2}, "is_bad": False},
            "B": {"text": "🤖 設計自動過濾清理機器人吸走垃圾 (STEAM)！ (Build an automatic cleaning robot to absorb the trash!)", "next": "4_A", "effect": {"creativity": 2}, "is_bad": False},
            "C": {"text": "😡 不問原因，大聲責罵八爪魚大王偷東西！ (Scold the Octopus for stealing without asking why!)", "next": "BAD_END_OCTOPUS", "effect": {"empathy": -2}, "is_bad": True,
                  "bad_reason": "不先了解原因就責罵別人，缺乏同理心！八爪魚大王生氣地噴出黑墨汁逃跑了！任務失敗……\n(Scolding without understanding lacks empathy! The octopus fled in ink! Mission failed...)"}
        }
    },

    # ===== 第 4 頁 (大結局分歧) =====
    "4_A": {
        "title_tc": "第 4 頁：超級珍珠回歸！", "title_en": "Page 4: The Pearl Returns!",
        "sfx": "✨ 晶瑩剔透！CLEAN!",
        "story_tc": "看到海洋恢復乾淨，八爪魚大王非常感動，把「超級珍珠」還給了火鷹俠，海水瞬間閃閃發亮！",
        "story_en": "Moved by the clean ocean, the Octopus returned the Pearl! The ocean becomes crystal clear and sparkling!",
        "choices": {
            "A": {"text": "🌊 攜手成為海洋環保大使，承諾一起守護地球生態！ (Partner up to become Ocean Eco-Ambassadors!)", "next": "6_LEADER", "effect": {"empathy": 3}, "is_bad": False},
            "B": {"text": "🎉 在龍宮開一個歡樂清潔慶功派對！ (Throw a joyful clean-up celebration party in the palace!)", "next": "6_INVENTOR", "effect": {"creativity": 3}, "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_SHARK": {
        "title_tc": "💥 任務失敗：惹怒大白鯊", "title_en": "Mission Failed: Angry Shark",
        "sfx": "💥 BOOM!", "is_bad_ending": True,
        "story_tc": "我們應該愛護海洋生物，用和平的方法解決問題。",
        "story_en": "We should protect marine life and solve problems peacefully."
    },
    "BAD_END_CRASH": {
        "title_tc": "💥 任務失敗：水母觸電", "title_en": "Mission Failed: Jellyfish Zap",
        "sfx": "⚡ ZAP!", "is_bad_ending": True,
        "story_tc": "做事不能只靠橫衝直撞，要懂得尊重環境和保護自己！",
        "story_en": "Don't just dash blindly. Respect the environment and stay safe!"
    },
    "BAD_END_OCTOPUS": {
        "title_tc": "💥 任務失敗：八爪魚逃跑", "title_en": "Mission Failed: Furious Octopus",
        "sfx": "💨 WHOOSH!", "is_bad_ending": True,
        "story_tc": "溝通時要先聆聽對方的感受，展現同理心才能化解衝突！",
        "story_en": "Listen to others' feelings first. Empathy resolves conflicts!"
    }
}
