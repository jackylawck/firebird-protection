# ==============================================================================
# 🎓 火鷹俠 20：IB 魔法學院 (二) - 六大元素之門
# 視覺化 IBDP 核心架構：六大學科組別 (6 Subjects) + 高低難度 (HL vs SL)
# ==============================================================================

STORY_INFO = {
    "id": "Story20_Ep2",
    "name_tc": "🎓 火鷹俠 20：IB 魔法學院 (二) 元素之門",
    "name_en": "Firebird 20: IB Magic Academy (Part 2)"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：六大元素的考驗", "title_en": "Page 1: Trial of the Six Elements",
        "sfx": "🚪 轟隆... RUMBLE...",
        "story_tc": "帶著「三大核心」的魔力，火鷹俠來到了『六大元素大廳』。這裡有 6 扇魔法門，分別代表：母語、外語、社會、科學、數學和藝術。貓頭鷹校長說：「你必須每種元素各學一門！其中至少要有 3 門是沉重但強大的『黃金大門 (HL 高級程度)』！」火鷹俠決定：",
        "story_en": "With the Core magic, Firebird enters the 'Hall of Six Elements'. There are 6 doors: Mother Tongue, Foreign Language, Society, Science, Math, and Arts. The Headmaster says: 'You must learn one of each! At least 3 must be the heavy but powerful Golden Doors (HL Higher Level)!' Firebird decides to:",
        "choices": {
            "A": {"text": "💪 展現勇氣與堅毅，勇敢推開 3 扇黃金大門 (HL) 和 3 扇白銀大門 (SL)！ (Show courage and perseverance, bravely push open 3 Golden HL doors and 3 Silver SL doors!)", "next": "2_A", "effect": {"bravery": 2}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "😰 覺得黃金大門太重了，偷偷把 6 扇門全部換成輕巧的白銀大門 (SL)！ (Think Golden doors are too heavy, secretly change all 6 to light Silver SL doors!)", "next": "BAD_END_SL", "effect": {"bravery": -2}, "kla": [], "is_bad": True,
                  "bad_reason": "魔法學院的規定很嚴格！沒有挑戰至少 3 門 HL，你的魔力將無法支撐畢業證書。任務失敗……\n(The academy's rules are strict! Without challenging at least 3 HL subjects, your magic can't support the diploma. Mission failed...)"}
        }
    },

    # ===== 分支 A：數理科學的高級挑戰 (Math & Science HL) =====
    "2_A": {
        "title_tc": "第 2 頁：數學與科學的黃金挑戰", "title_en": "Page 2: The Golden Challenge of Math & Science",
        "sfx": "🔢 滴答！TICK TOCK!",
        "story_tc": "你選擇了「數學」和「科學」作為黃金大門 (HL) 的挑戰！門後出現了一隻巨大的『微積分機械龍』，牠要求你解開複雜的運算，並完成高難度的科學實驗。火鷹俠運用 STEAM 知識：",
        "story_en": "You chose 'Math' and 'Science' as your Golden Door (HL) challenges! A giant 'Calculus Mech-Dragon' appears, demanding complex calculations and a high-level science experiment. Firebird uses STEAM:",
        "choices": {
            "A": {"text": "📐 運用高級代數與幾何知識，精準計算出機械龍的弱點並安撫牠 (STEAM)！ (Use advanced algebra and geometry to precisely calculate the dragon's weak point and calm it!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["MATH", "TECH"], "is_bad": False},
            "B": {"text": "🧪 調配出「超級擴展 (AHL) 化學藥水」，將機械龍變成溫柔的小蜥蜴！ (Mix a 'Super Extension (AHL) Chemical Potion' to turn the dragon into a gentle lizard!)", "next": "3_A", "effect": {"creativity": 1, "bravery": 1}, "kla": ["SCIENCE"], "is_bad": False},
            "C": {"text": "🎲 覺得計算太麻煩，隨便丟一顆骰子猜答案！ (Think calculating is too much trouble, just roll a dice to guess the answer!)", "next": "BAD_END_GUESS", "effect": {"creativity": -2}, "kla": ["MATH"], "is_bad": True,
                  "bad_reason": "黃金大門 (HL) 的考驗非常嚴謹，絕對不能靠猜運氣！機械龍生氣了，把你彈出門外。任務失敗……\n(The HL golden trial is strict. You can never rely on guessing! The dragon got angry and bounced you out. Mission failed...)"}
        }
    },

    # ===== 第 3 頁：人文與藝術的標準挑戰 (Language/Arts SL/HL) =====
    "3_A": {
        "title_tc": "第 3 頁：語文與藝術的魔法", "title_en": "Page 3: The Magic of Language & Arts",
        "sfx": "📖 嘩啦！FLIP!",
        "story_tc": "數理挑戰成功！接著你走進了「語言文學」與「藝術」的房間。這裡有滿滿的古老詩集，還有需要你創作的大型壁畫。為了湊齊 6 大學科，火鷹俠決定：",
        "story_en": "Math and Science conquered! Next, you enter the 'Language & Literature' and 'Arts' rooms. There are ancient poetry books and giant murals to paint. To complete the 6 subjects, Firebird decides to:",
        "choices": {
            "A": {"text": "🗣️ 展現優秀的語文能力，朗誦至少 6 部文學巨著，解開文字的封印！ (Show excellent language skills, recite at least 6 literary masterpieces to unlock the text seals!)", "next": "4_A", "effect": {"creativity": 1, "empathy": 1}, "kla": ["LANG_CH", "LANG_EN"], "is_bad": False},
            "B": {"text": "🎨 展現藝術才華，舉辦一場超大規模的個人視覺藝術展覽 (Exhibition)！ (Show artistic talent, host a massive personal Visual Arts Exhibition!)", "next": "4_A", "effect": {"creativity": 2}, "kla": ["ARTS"], "is_bad": False}
        }
    },

    # ===== 第 4 頁：結算 42 分 (6 科 x 7 分) =====
    "4_A": {
        "title_tc": "第 4 頁：凝聚 42 顆魔法寶石", "title_en": "Page 4: Forging 42 Magic Gems",
        "sfx": "✨ 閃亮！SHINE!",
        "story_tc": "太厲害了！你成功通過了 6 大元素之門（包含 3 門艱苦的 HL）！每扇門都給了你 7 顆魔法寶石，6 扇門總共結成了 42 顆耀眼的元素寶石！",
        "story_en": "Amazing! You passed all 6 Elemental Doors (including 3 tough HLs)! Each door gave you 7 magic gems, totaling 42 dazzling Elemental Gems from the 6 doors!",
        "choices": {
            "A": {"text": "🛡️ 拿出第一集獲得的「三大核心力量 (3分)」，與這 42 顆寶石完美融合！ (Take the '3 Core Powers' from Part 1 and perfectly merge them with the 42 gems!)", "next": "5_A", "effect": {"bravery": 1, "creativity": 1}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 第 5 頁：圓滿結局 (為第三集鋪墊) =====
    "5_A": {
        "title_tc": "第 5 頁：45 分滿分的預兆！", "title_en": "Page 5: The Omen of a Perfect 45!",
        "sfx": "🌈 奇蹟光芒！MIRACLE LIGHT!",
        "story_tc": "42 顆元素寶石與 3 點核心魔力融合，變成了傳說中的「45 分至尊光環」！但貓頭鷹校長說：「這只是資格，最後你還必須擊敗兩條遠古巨龍——『內部評估 (IA)』與『外部評估 (EA)』，才能真正畢業！」",
        "story_en": "The 42 Elemental Gems and 3 Core Magic points merged into the legendary '45-Point Supreme Halo'! But the Headmaster says: 'This is just the qualification. You must finally defeat two ancient dragons: Internal Assessment (IA) and External Assessment (EA) to graduate!'",
        "choices": {
            "A": {"text": "⚔️ 握緊至尊光環，準備迎戰最終的 IA 與 EA 雙龍試煉 (進入第三集)！ (Grasp the Supreme Halo and prepare for the final IA & EA Dragon Trial in Part 3!)", "next": "6_LEADER", "effect": {"bravery": 3}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_SL": {
        "title_tc": "💥 任務失敗：逃避困難", "title_en": "Mission Failed: Escaping Difficulties",
        "sfx": "📉 FALL!", "is_bad_ending": True,
        "story_tc": "在學習的道路上不能只挑簡單的做。IB 規則要求我們必須勇敢挑戰至少 3 門 HL (高級) 學科，才能發揮潛力！",
        "story_en": "We can't just pick easy tasks in learning. IB rules require us to bravely challenge at least 3 HL (Higher Level) subjects to reach our potential!"
    },
    "BAD_END_GUESS": {
        "title_tc": "💥 任務失敗：靠猜運氣", "title_en": "Mission Failed: Relying on Luck",
        "sfx": "❌ WRONG!", "is_bad_ending": True,
        "story_tc": "無論是數學還是科學的高級挑戰，都需要嚴謹的邏輯與努力計算。靠丟骰子猜答案是無法學到真知識的！",
        "story_en": "Advanced math and science challenges require strict logic and hard work. Guessing with dice won't help you learn true knowledge!"
    }
}
