# ==============================================================================
# 🎓 火鷹俠 10：國際文憑魔法學院 (The IB Magic Academy)
# 融入 IBDP 核心架構：三大核心 (TOK, EE, CAS) + 六大學科 + IA/EA 評估
# 訓練 KLA：人文教育、科學教育、科技教育與全人發展
# ==============================================================================

STORY_INFO = {
    "id": "Story10",
    "name_tc": "🎓 火鷹俠 10：國際文憑魔法學院",
    "name_en": "Firebird 10: The IB Magic Academy"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：45 分的終極傳說！", "title_en": "Page 1: The 45-Point Legend!",
        "sfx": "✨ 閃耀！SPARKLE!",
        "story_tc": "歡迎來到「國際文憑 (IB) 魔法學院」！這裡有一張傳說中的「45 分至尊文憑」，但要拿到它，火鷹俠必須在六大魔法學科中取得 42 分，並在「三大核心 (Core)」試煉中拿滿 3 分。最低及格線是 24 分！火鷹俠決定首先挑戰：",
        "story_en": "Welcome to the IB Magic Academy! To earn the legendary '45-Point Diploma', Firebird must score 42 points in 6 magic subjects and 3 points in the 'Core' trials. The passing mark is 24! Firebird decides to first challenge:",
        "choices": {
            "A": {"text": "🧠 前往「三大核心神殿」，挑戰 TOK、EE 與 CAS 試煉！ (Go to the 'Core Temple' to challenge TOK, EE, and CAS!)", "next": "2_A", "effect": {"bravery": 1}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "📚 前往「六大學科之門」，選擇高級 (HL) 與標準 (SL) 難度！ (Go to the '6 Subject Doors' to pick Higher Level and Standard Level paths!)", "next": "2_B", "effect": {"creativity": 1}, "kla": ["SCIENCE", "TECH"], "is_bad": False},
            "C": {"text": "😴 覺得兩年 (18個月) 的課程太長了，決定回家睡覺！ (Think the 2-year course is too long and go home to sleep!)", "next": "BAD_END_GIVEUP", "effect": {"bravery": -2}, "kla": [], "is_bad": True,
                  "bad_reason": "IBDP 是一個高強度的全面預科課程，放棄就無法獲得文憑了！堅毅 (Perseverance) 是成功的關鍵。任務失敗……\n(IBDP is a high-intensity program. Giving up means no diploma! Perseverance is key. Mission failed...)"}
        }
    },

    # ===== 分支 A：三大核心 (The Core) =====
    "2_A": {
        "title_tc": "第 2 頁：三大核心神殿的考驗", "title_en": "Page 2: The Core Temple Trials",
        "sfx": "🏛️ 轟隆... RUMBLE...",
        "story_tc": "神殿裡有三個守護者：\n1.「知識人面獅身」(TOK)：要求你反思『我們如何得知知識』，並完成 1,600 字論文與展覽。\n2.「研究精靈」(EE)：要求你獨立完成 4,000 字的學術研究。\n3.「行動巨人」(CAS)：要求你在藝術、體育與志工服務中實踐 18 個月。火鷹俠決定：",
        "story_en": "Three guardians await:\n1. Sphinx of TOK: Reflect on 'how we know' (1,600-word essay & exhibition).\n2. Sprite of EE: 4,000-word independent research.\n3. Golem of CAS: 18 months of Creativity, Activity, and Service. Firebird decides to:",
        "choices": {
            "A": {"text": "🤔 展現批判性思維，與 TOK 獅身人面獸辯論知識的本質！ (Show critical thinking and debate the nature of knowledge with the TOK Sphinx!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["HUMANITIES", "LANG_CH"], "is_bad": False},
            "B": {"text": "❤️ 帶領團隊完成 CAS 社區志工服務，提交完美的反思日誌 (Portfolio)！ (Lead a team for a CAS community service and submit a perfect reflection portfolio!)", "next": "3_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES", "PE", "ARTS"], "is_bad": False}
        }
    },

    # ===== 分支 B：六大學科 (6 Subject Groups) =====
    "2_B": {
        "title_tc": "第 2 頁：學科組別的戰略選擇", "title_en": "Page 2: Strategic Subject Choices",
        "sfx": "🚪 喀嚓！CLICK!",
        "story_tc": "你必須從語言文學、語言習得、個人與社會、科學、數學、藝術這 6 個組別中各選一科。規定必須有 3 科是「高級程度 (HL)」，3 科是「標準程度 (SL)」。火鷹俠的戰略是：",
        "story_en": "You must pick one subject from Language & Lit, Language Acquisition, Individuals & Societies, Sciences, Math, and Arts. You need 3 Higher Level (HL) and 3 Standard Level (SL). Firebird's strategy is:",
        "choices": {
            "A": {"text": "🔢 挑戰「第五組：數學 AA (HL)」，運用微積分與代數理論證明擊敗敵人！ (Challenge 'Group 5: Math AA HL' using calculus and algebraic proofs!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["MATH", "TECH"], "is_bad": False},
            "B": {"text": "🎨 選擇「第六組：視覺藝術 (HL)」，提交超大規模的個人創作展覽 (Exhibition)！ (Choose 'Group 6: Visual Arts HL' and submit a massive personal exhibition!)", "next": "3_A", "effect": {"creativity": 1, "empathy": 1}, "kla": ["ARTS"], "is_bad": False},
            "C": {"text": "📚 逃避難題，把所有科目都選成簡單的 SL！ (Avoid hard problems and pick all easy SL subjects!)", "next": "BAD_END_SL", "effect": {"bravery": -2}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "違反 IB 規則！你必須至少選擇 3 科 HL (高級程度) 才能獲得文憑！任務失敗……\n(Rule violation! You must choose at least 3 HL subjects to get the diploma! Mission failed...)"}
        }
    },

    # ===== 第 3 頁匯合：評估制度 (IA vs EA) =====
    "3_A": {
        "title_tc": "第 3 頁：內外夾擊的雙重評估", "title_en": "Page 3: The Dual Assessment (IA & EA)",
        "sfx": "⚖️ 噹噹！CHIME!",
        "story_tc": "課程來到了尾聲！每科的成績由兩部分組成：校內老師指導的「內部評估 (IA)」(佔 20%-30%)，以及全球統一筆試的「外部評估 (EA)」(佔 70%-80%)。終極大魔王在 5 月份的全球大考等著你！",
        "story_en": "The course nears its end! Each subject score has two parts: Internal Assessment (IA, 20-30%) and External Assessment global exams (EA, 70-80%). The final boss waits in the May global exams!",
        "choices": {
            "A": {"text": "🔬 專注於 IA：寫出一篇完美的科學實驗報告與經濟學評論文章！ (Focus on IA: Write a perfect science experiment report and economics commentary!)", "next": "4_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "HUMANITIES"], "is_bad": False},
            "B": {"text": "📝 專注於 EA：狂刷論述題與數據分析題，迎接佔分 80% 的全球筆試！ (Focus on EA: Drill essay and data analysis questions for the 80% global exam!)", "next": "4_A", "effect": {"bravery": 2}, "kla": ["MATH", "LANG_EN"], "is_bad": False},
            "C": {"text": "🎲 以為考試全是選擇題 (MC)，隨便亂猜！ (Think the exam is all Multiple Choice and just guess blindly!)", "next": "BAD_END_MC", "effect": {"bravery": -1}, "kla": [], "is_bad": True,
                  "bad_reason": "大錯特錯！IBDP 的 EA 極少使用選擇題，全都是高難度的論述與結構化簡答題！任務失敗……\n(Huge mistake! IBDP EA rarely uses multiple choice. It's all tough essays and structured answers! Mission failed...)"}
        }
    },

    # ===== 第 4 頁：結算與矩陣加分 =====
    "4_A": {
        "title_tc": "第 4 頁：矩陣加分的奇蹟", "title_en": "Page 4: The Matrix Bonus Miracle",
        "sfx": "🌟 閃亮！SHINE!",
        "story_tc": "你的 6 個學科全部拿到了滿分 7 分 (6 × 7 = 42 分)！現在，只要你的 TOK (知識理論) 和 EE (延伸論文) 達到 A 級別，透過神奇的「矩陣折算」，就能獲得額外 3 分的獎勵分！",
        "story_en": "You scored a perfect 7 in all 6 subjects (6 × 7 = 42 points)! Now, if your TOK and EE reach Grade A, the magical 'Matrix calculation' will grant you 3 bonus points!",
        "choices": {
            "A": {"text": "🎓 提交 4000 字的 EE 論文與 TOK 展覽，奪取最後 3 分！ (Submit the 4000-word EE and TOK exhibition to claim the final 3 points!)", "next": "5_A", "effect": {"creativity": 2, "bravery": 1}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "🤝 確認 CAS (創意、行動與服務) 的 7 項學習成果已全部達標！ (Ensure all 7 learning outcomes of CAS are fully achieved!)", "next": "5_B", "effect": {"empathy": 3}, "kla": ["PE", "ARTS", "HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 第 5 頁：圓滿結局 =====
    "5_A": {
        "title_tc": "第 5 頁：45 分滿分狀元！", "title_en": "Page 5: The 45-Point Top Scholar!",
        "sfx": "🎉 歡呼！CHEERS!",
        "story_tc": "奇蹟出現了！你成功跨越了 24 分的及格線，甚至拿到了滿分 45 分！你成為了具備批判性思維與世界觀的頂尖學者！",
        "story_en": "A miracle! You passed the 24-point mark and achieved a perfect 45 points! You became a top scholar with critical thinking and a global worldview!",
        "choices": {
            "A": {"text": "🏆 帶著這張至尊文憑，前往世界頂尖大學繼續探索知識！ (Take this supreme diploma and head to world top universities to explore more knowledge!)", "next": "6_LEADER", "effect": {"empathy": 2, "bravery": 1}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：CAS 全人發展大使！", "title_en": "Page 5: CAS Whole-Person Ambassador!",
        "sfx": "🌈 榮耀！GLORY!",
        "story_tc": "你不僅成績優異，在長達兩年的 CAS 實踐中，你展現了極高的藝術創意、體育精神與社區服務熱誠，成為了真正的全人領袖！",
        "story_en": "Not only did you excel academically, but your 2-year CAS journey showed great creativity, sportsmanship, and community service. A true whole-person leader!",
        "choices": {
            "A": {"text": "🌟 運用你在 IB 學到的知識，貢獻社會，幫助更多有需要的人！ (Use the knowledge learned in IB to contribute to society and help others!)", "next": "6_CARER", "effect": {"empathy": 3}, "kla": ["HUMANITIES", "PE"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_GIVEUP": {
        "title_tc": "💥 任務失敗：半途而廢", "title_en": "Mission Failed: Giving Up",
        "sfx": "📉 FALL!", "is_bad_ending": True,
        "story_tc": "IBDP 是一個高強度的全面課程，需要強大的時間管理與堅毅精神。我們不能輕言放棄！",
        "story_en": "IBDP is a high-intensity comprehensive program requiring strong time management and perseverance. Never give up!"
    },
    "BAD_END_SL": {
        "title_tc": "💥 任務失敗：選科策略錯誤", "title_en": "Mission Failed: Wrong Subject Strategy",
        "sfx": "❌ ERROR!", "is_bad_ending": True,
        "story_tc": "根據 IB 規則，你必須挑戰至少 3 門難度更高的 HL（高級程度）科目。勇敢接受挑戰吧！",
        "story_en": "According to IB rules, you must challenge at least 3 tougher HL subjects. Be brave and accept the challenge!"
    },
    "BAD_END_MC": {
        "title_tc": "💥 任務失敗：低估外部評估", "title_en": "Mission Failed: Underestimating EA",
        "sfx": "📝 WRONG!", "is_bad_ending": True,
        "story_tc": "IB 的外部評估 (EA) 佔分極重，而且非常考驗論述與深度分析能力，不能靠猜選擇題過關！",
        "story_en": "IB's External Assessment carries heavy weight and tests deep analysis and essay skills. You can't just guess multiple choices!"
    }
}
