# ==============================================================================
# 🎓 火鷹俠 30：IB 魔法學院 (三) - 內外雙龍的終極戰役
# 視覺化 IBDP 核心架構：內部評估 (IA) 與外部評估 (EA) 雙重考核
# ==============================================================================

STORY_INFO = {
    "id": "Story30_Ep3",
    "name_tc": "🎓 火鷹俠 30：IB 魔法學院 (三) 雙龍之戰",
    "name_en": "Firebird 30: IB Magic Academy (Part 3)"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：雙龍競技場的呼喚", "title_en": "Page 1: Call of the Twin Dragon Arena",
        "sfx": "🐉 吼叫！ROAR!",
        "story_tc": "帶著「45 分至尊光環」的資格，火鷹俠踏入了最終的競技場。天空中盤旋著兩條遠古巨龍：一條是講究實驗細節的「內部守護龍 (IA)」，另一條是掌握全球大考的「外部終極龍 (EA)」。火鷹俠決定先發制人：",
        "story_en": "With the '45-Point Supreme Halo' qualification, Firebird enters the final arena. Two ancient dragons circle the sky: the 'Internal Guardian Dragon (IA)' demanding precise experiments, and the 'External Ultimate Dragon (EA)' controlling the global exams. Firebird decides to strike first:",
        "choices": {
            "A": {"text": "🔬 先挑戰「內部守護龍 (IA)」，準備提交一份完美的科學探究報告！ (Challenge the 'Internal Guardian Dragon (IA)' first by submitting a perfect scientific exploration report!)", "next": "2_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "TECH"], "is_bad": False},
            "B": {"text": "📝 先迎戰「外部終極龍 (EA)」，準備用強大的數據分析與論述魔法回擊！ (Battle the 'External Ultimate Dragon (EA)' first, fighting back with powerful data analysis and essay magic!)", "next": "2_B", "effect": {"bravery": 1}, "kla": ["LANG_CH", "MATH"], "is_bad": False},
            "C": {"text": "🎲 以為巨龍只會問「選擇題 (MC)」，打算隨便猜 A、B、C、D 敷衍過去！ (Think the dragons only ask Multiple Choice questions, and plan to just guess A, B, C, D!)", "next": "BAD_END_MC", "effect": {"bravery": -1}, "kla": [], "is_bad": True,
                  "bad_reason": "大錯特錯！EA 終極大考極少使用選擇題，全都是高難度的論述題和簡答題。靠猜運氣是贏不了巨龍的！任務失敗……\n(Huge mistake! The EA exam rarely uses MCQs; it's all tough essays and short answers. Guessing won't defeat the dragons! Mission failed...)"}
        }
    },

    # ===== 分支 A：IA 內部評估挑戰 (20%-30%) =====
    "2_A": {
        "title_tc": "第 2 頁：內部守護龍的精密考驗", "title_en": "Page 2: The Precise Trial of the IA Dragon",
        "sfx": "⚖️ 滴答！TICK TOCK!",
        "story_tc": "內部守護龍 (IA) 降落下來，牠的力量佔據了你 20% 到 30% 的總成績。牠要求你在導師的指導下，親自完成一項實驗，並將成果交給校外的神秘長老進行「外部調整 (Moderation)」。火鷹俠決定：",
        "story_en": "The Internal Guardian Dragon (IA) lands, holding 20%-30% of your total score. It demands you complete a personal experiment under a mentor's guidance, and send it to mysterious external elders for 'Moderation'. Firebird decides to:",
        "choices": {
            "A": {"text": "🧪 進行嚴謹的「化學實驗室探究」，仔細記錄每一個數據，寫出完美的 IA 報告 (STEAM)！ (Conduct a strict 'Chemistry Lab Exploration', recording every detail for a perfect IA report!)", "next": "3_A", "effect": {"creativity": 2, "bravery": 1}, "kla": ["SCIENCE", "MATH"], "is_bad": False},
            "B": {"text": "📊 運用經濟學理論，寫出一篇深入分析社會現象的「經濟學評論文章」！ (Use economic theories to write a deep 'Economics Commentary' analyzing social phenomena!)", "next": "3_A", "effect": {"creativity": 1, "empathy": 1}, "kla": ["HUMANITIES"], "is_bad": False},
            "C": {"text": "📋 為了快點過關，偷偷抄襲網路上其他魔法師的實驗報告！ (To pass quickly, secretly copy an experiment report from another wizard online!)", "next": "BAD_END_PLAGIARISM", "effect": {"empathy": -3}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "學術誠信 (Academic Integrity) 是 IB 的底線！抄襲會立刻被 IA 守護龍識破，並直接取消你的文憑資格。任務失敗……\n(Academic Integrity is the bottom line of IB! Copying will be instantly detected by the IA Dragon, disqualifying your diploma. Mission failed...)"}
        }
    },

    # ===== 分支 B：EA 外部評估挑戰 (70%-80%) =====
    "2_B": {
        "title_tc": "第 2 頁：外部終極龍的全球大考", "title_en": "Page 2: The Global Exam of the EA Dragon",
        "sfx": "🌪️ 狂風！WIND HOWLS!",
        "story_tc": "外部終極龍 (EA) 帶來了巨大的壓力！牠掌握著 70% 到 80% 的分數，並召喚出名為「5月全球統一大考」的魔法風暴。火鷹俠必須運用平時累積的實力：",
        "story_en": "The External Ultimate Dragon (EA) brings immense pressure! It holds 70%-80% of the score and summons a magic storm called 'The May Global Exam'. Firebird must use his accumulated strength:",
        "choices": {
            "A": {"text": "✍️ 頂住壓力，揮舞「論述魔法筆」，寫出結構嚴謹、邏輯清晰的長篇論文魔法！ (Endure the pressure, wave the 'Essay Magic Pen' to cast well-structured and highly logical long essay spells!)", "next": "3_A", "effect": {"bravery": 2, "creativity": 1}, "kla": ["LANG_CH", "LANG_EN"], "is_bad": False},
            "B": {"text": "📈 展開「數據分析護盾」，冷靜拆解終極龍噴出的圖表與數據難題 (STEAM)！ (Deploy the 'Data Analysis Shield', calmly breaking down the chart and data puzzles spat by the ultimate dragon!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["MATH", "SCIENCE"], "is_bad": False}
        }
    },

    # ===== 第 3 頁匯合：時間管理的極限 =====
    "3_A": {
        "title_tc": "第 3 頁：沙漏中的最後衝刺", "title_en": "Page 3: The Final Sprint in the Hourglass",
        "sfx": "⏳ 沙沙... HISS...",
        "story_tc": "雙龍同時發動了最後的考驗！天空中出現了一個巨大的魔法沙漏。你必須在時間結束前完成所有論述與實驗，這是一場對「堅毅 (Perseverance)」的極限考驗！",
        "story_en": "Both dragons launch their final trial together! A giant magic hourglass appears in the sky. You must complete all essays and experiments before time runs out. It's the ultimate test of 'Perseverance'!",
        "choices": {
            "A": {"text": "⌚ 展現極佳的「時間管理能力」，冷靜分配每道題目的時間，不慌不忙地戰鬥！ (Show excellent 'Time Management', calmly allocating time for each question, fighting without panic!)", "next": "4_A", "effect": {"bravery": 2, "creativity": 1}, "kla": ["HUMANITIES", "MATH"], "is_bad": False},
            "B": {"text": "💪 咬緊牙關，就算手寫到發酸，也堅持用強大的意志力把答案寫到最後一秒！ (Grind your teeth. Even with sore hands, use sheer willpower to write answers until the very last second!)", "next": "4_A", "effect": {"bravery": 3}, "kla": ["PE"], "is_bad": False}
        }
    },

    # ===== 第 4 頁：結算 =====
    "4_A": {
        "title_tc": "第 4 頁：45 分的奇蹟誕生", "title_en": "Page 4: Birth of the 45-Point Miracle",
        "sfx": "🎓 榮耀！GLORY!",
        "story_tc": "沙漏漏完了最後一粒沙。內部守護龍 (IA) 與外部終極龍 (EA) 低下了頭，化作兩道金光融入了你的光環中。你成功滿足了 24 分的及格線，更一舉衝破了 45 分的滿分極限！",
        "story_en": "The hourglass empties. The IA and EA dragons bow their heads, turning into golden light and merging into your halo. You easily surpassed the 24-point passing mark and broke through to the perfect 45-point limit!",
        "choices": {
            "A": {"text": "🌟 走向貓頭鷹校長，雙手接過那張閃耀著智慧光芒的「IB 頂尖文憑」！ (Walk to the Owl Headmaster and receive the shining 'IB Top Diploma' with both hands!)", "next": "5_A", "effect": {"empathy": 1, "bravery": 1}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 第 5 頁：圓滿結局 =====
    "5_A": {
        "title_tc": "第 5 頁：最頂尖的魔法學者！", "title_en": "Page 5: The Ultimate Magic Scholar!",
        "sfx": "🎉 掌聲如雷！APPLAUSE!",
        "story_tc": "恭喜你通關了整個 IB 魔法學院！你不僅學會了艱深的學科知識，更學會了時間管理、學術誠信與全球視野。未來的世界，正等著你去改變！",
        "story_en": "Congratulations on clearing the entire IB Magic Academy! You learned deep subjects, time management, academic integrity, and a global worldview. The future world awaits you to change it!",
        "choices": {
            "A": {"text": "🏆 成為結合學術實力與高尚品格的「全人小領袖」！ (Become a 'Whole-person Leader' combining academic strength and noble character!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_MC": {
        "title_tc": "💥 任務失敗：低估外部評估", "title_en": "Mission Failed: Underestimating EA",
        "sfx": "📝 WRONG!", "is_bad_ending": True,
        "story_tc": "IB 的外部評估 (EA) 佔分極重，而且非常考驗論述與深度分析能力，不能靠猜選擇題過關！",
        "story_en": "IB's External Assessment carries heavy weight and tests deep analysis and essay skills. You can't just guess multiple choices!"
    },
    "BAD_END_PLAGIARISM": {
        "title_tc": "💥 任務失敗：學術不端", "title_en": "Mission Failed: Academic Misconduct",
        "sfx": "⚖️ GUILTY!", "is_bad_ending": True,
        "story_tc": "內部評估 (IA) 要求學生獨立探究。抄襲別人的作品嚴重違反學術誠信，絕對不可取！",
        "story_en": "Internal Assessment (IA) requires independent exploration. Copying others violates academic integrity completely!"
    }
}
