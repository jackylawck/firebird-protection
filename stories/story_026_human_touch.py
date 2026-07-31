# ==============================================================================
# 🏥 火鷹俠 26：科技醫院的溫暖之手 (The Warm Hand at the Tech Hospital)
# 融入 AI教父智慧：人類的溫度(愛與同理心)、實體勞動(水管維修)、扎實基礎(數學/物理)
# KLA: 人文教育(品德與價值觀)、科學教育、數學教育
# ==============================================================================

STORY_INFO = {
    "id": "Story26",
    "name_tc": "🏥 火鷹俠 26：科技醫院的溫暖之手",
    "name_en": "Firebird 26: The Warm Hand at the Tech Hospital"
}

SCENES = {
    # ===== 起始：冰冷的科技醫院 =====
    "1_START": {
        "title_tc": "第 1 頁：冰冷的醫療機器人", "title_en": "Page 1: The Cold Medical Robots",
        "sfx": "🏥 滴...滴... BEEP... BEEP...",
        "story_tc": "火鷹俠來到未來的「星際科技醫院」。這裡的超級 AI 瞬間就能用鍵盤處理完所有病歷！但病床上有一隻生病的小星狐，正害怕得發抖大哭。醫療機器人只會發出冰冷的機械音：「數據正常，請停止哭泣。」火鷹俠決定：",
        "story_en": "Firebird visits the future 'Star Tech Hospital'. The Super AI handles all medical records instantly via keyboards! But on a bed, a sick little Star-Fox is trembling and crying in fear. The robot only says coldly: 'Data normal. Please stop crying.' Firebird decides to:",
        "choices": {
            "A": {"text": "🤝 展現「人類的溫度」：走上前，溫柔地緊緊握住小星狐的手，給予牠愛與關懷！ (Show 'Human Warmth': Step forward, gently and tightly hold the little Star-Fox's hand, giving love and care!)", "next": "2_A", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "🔧 展現「實體行動力」：發現病房的水管突然破裂，立刻動手進行複雜的維修！ (Show 'Physical Action': Notice a water pipe burst in the room and immediately start complex manual repairs!)", "next": "2_B", "effect": {"bravery": 1, "creativity": 1}, "kla": ["SCIENCE", "PE"], "is_bad": False},
            "C": {"text": "⌨️ 坐在電腦前，試圖用鍵盤輸入更快的醫療代碼來幫助牠！ (Sit at the computer, trying to type faster medical codes to help!)", "next": "BAD_END_KEYBOARD", "effect": {"creativity": -1}, "kla": ["TECH"], "is_bad": True,
                  "bad_reason": "依賴鍵盤操作的工作很容易被 AI 替代！生病焦慮時，患者需要的是人類的溫度，而不是更快的代碼。任務失敗……\n(Keyboard jobs are easily replaced by AI! In anxiety, a patient needs human warmth, not faster code. Mission failed...)"}
        }
    },

    # ===== 分支 A：人類的溫度 (解決實體危機) =====
    "2_A": {
        "title_tc": "第 2 頁：突發的水管危機", "title_en": "Page 2: The Sudden Pipe Crisis",
        "sfx": "💦 嘩啦啦！SPLASH!",
        "story_tc": "感受到你溫暖的手，小星狐立刻不哭了，安靜地睡著了。但突然，病房牆壁裡的「冷卻水管」破裂了！機器人因為肢體不協調，在積水中不斷滑倒，無法進行現場作業。火鷹俠決定：",
        "story_en": "Feeling your warm hand, the Star-Fox stops crying and falls asleep peacefully. But suddenly, the room's 'Cooling Water Pipe' bursts! The robots lack physical coordination, slipping in the water and failing to work. Firebird decides to:",
        "choices": {
            "A": {"text": "📐 運用扎實的「數學與物理」基礎，精準計算水壓並靈活地爬進狹窄空間修好水管 (STEAM)！ (Use a solid 'Math and Physics' foundation to calculate water pressure and nimbly crawl into the tight space to fix the pipe!)", "next": "3_A", "effect": {"creativity": 2, "bravery": 1}, "kla": ["MATH", "SCIENCE", "PE"], "is_bad": False},
            "B": {"text": "🌟 盲目追逐科技潮流，試圖用語音命令 AI 發明一個全新的修水管機器人！ (Blindly chase tech trends, trying to voice-command the AI to invent a brand new pipe-fixing robot!)", "next": "BAD_END_FAD", "effect": {"creativity": -2}, "kla": ["TECH"], "is_bad": True,
                  "bad_reason": "緩不濟急！與其盲目追逐流行的 AI 技術，不如擁有扎實的物理基礎和親自動手解決問題的能力。任務失敗……\n(Too slow! Instead of chasing trendy AI tech, having a solid physics foundation and hands-on skills is better. Mission failed...)"}
        }
    },

    # ===== 分支 B：實體行動力 (補足人類情感) =====
    "2_B": {
        "title_tc": "第 2 頁：修復與陪伴", "title_en": "Page 2: Repair and Companionship",
        "sfx": "🔧 喀啦！CLICK!",
        "story_tc": "你運用靈活的肢體協調和物理知識，成功修好了連 AI 都無法勝任的破裂水管！但小星狐還是因為害怕機器人而哭個不停。火鷹俠決定：",
        "story_en": "Using nimble physical coordination and physics knowledge, you fixed the burst pipe that AI couldn't handle! But the little Star-Fox is still crying, afraid of the robots. Firebird decides to:",
        "choices": {
            "A": {"text": "❤️ 放下工具，走到床邊給予他一個充滿「愛與責任感」的深深擁抱！ (Put down tools, walk to the bed, and give a deep hug full of 'Love and Responsibility'!)", "next": "3_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "🎶 在病房裡跳一支好笑的舞，用人類獨有的幽默感逗牠開心！ (Do a funny dance in the room, using unique human humor to make it happy!)", "next": "3_A", "effect": {"empathy": 1, "creativity": 1}, "kla": ["ARTS", "PE"], "is_bad": False}
        }
    },

    # ===== 第 3 頁匯合：AI 教父的讚賞 =====
    "3_A": {
        "title_tc": "第 3 頁：AI 教父的全息投影", "title_en": "Page 3: Hologram of the AI Godfather",
        "sfx": "✨ 嗡—— HUMMM...",
        "story_tc": "病房恢復了溫暖與寧靜。這時，發明這家醫院的「AI 教父」全息投影出現了。他微笑著說：「機器可以取代大部分工作，但永遠無法取代人與人之間的觸碰與共情。」火鷹俠回應：",
        "story_en": "The room is warm and peaceful again. The hologram of the 'AI Godfather' who built this hospital appears. He smiles: 'Machines can replace most jobs, but can never replace human touch and empathy.' Firebird replies:",
        "choices": {
            "A": {"text": "誓言永遠將重心放在「成為一個真正美好、充滿愛與責任感的人」！ (Vow to always focus on 'becoming a truly beautiful human being full of love and responsibility'!)", "next": "4_A", "effect": {"empathy": 2, "bravery": 1}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "承諾不盲目追逐科技潮流，會優先打好「數學與物理」等基礎學科的根基！ (Promise not to blindly chase tech trends, but prioritize building a solid foundation in 'Math and Physics'!)", "next": "4_A", "effect": {"creativity": 2}, "kla": ["MATH", "SCIENCE"], "is_bad": False}
        }
    },

    # ===== 第 4 頁 (最終結局) =====
    "4_A": {
        "title_tc": "第 4 頁：無可複製的核心價值", "title_en": "Page 4: The Irreplaceable Core Value",
        "sfx": "🌟 閃亮！SHINE!",
        "story_tc": "AI 教父點點頭：「沒錯，因幫助他人而產生的深層滿足感，是機器無法模擬的核心價值。」你成功證明了人類靈魂的珍貴！",
        "story_en": "The AI Godfather nods: 'Exactly. The deep satisfaction from helping others is a core value machines cannot simulate.' You successfully proved the preciousness of the human soul!",
        "choices": {
            "A": {"text": "🏆 帶著人類獨有的溫度，成為一位懂得愛與關懷的「全人小領袖」！ (Carry the unique human warmth and become a 'Whole-person Leader' who knows love and care!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_KEYBOARD": {
        "title_tc": "💥 任務失敗：被替代的鍵盤", "title_en": "Mission Failed: Replaced Keyboard",
        "sfx": "📉 ERROR!", "is_bad_ending": True,
        "story_tc": "AI 教父提醒過我們：依賴鍵盤操作的工作很容易被 AI 替代。人類應該提供機器無法提供的關懷與溫度！",
        "story_en": "The AI Godfather warned: Keyboard-based jobs are easily replaced by AI. Humans should provide the care and warmth that machines cannot!"
    },
    "BAD_END_FAD": {
        "title_tc": "💥 任務失敗：盲目追逐潮流", "title_en": "Mission Failed: Chasing Fads Blindly",
        "sfx": "❌ WRONG!", "is_bad_ending": True,
        "story_tc": "與其盲目追逐流行的 AI 應用，不如優先打好數學、物理等基礎學科的根基，以及培養動手解決實體問題的能力！",
        "story_en": "Instead of blindly chasing trendy AI apps, prioritize building a solid foundation in math and physics, and hands-on problem-solving skills!"
    }
}
