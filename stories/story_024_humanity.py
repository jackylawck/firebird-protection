# ==============================================================================
# 🌟 火鷹俠 24：未來方舟的四大試煉 (The Four Trials of the Future Ark)
# 融入 未來四大核心特質：同理心、批判思考(提問)、適應力、創造力(美學)
# KLA: 人文教育、藝術教育、科學教育、科技教育
# ==============================================================================

STORY_INFO = {
    "id": "Story24",
    "name_tc": "🌟 火鷹俠 24：未來方舟的四大試煉",
    "name_en": "Firebird 24: The Four Trials of the Future Ark"
}

SCENES = {
    # ===== 起始：第一試煉 (深度同理心與連結力) =====
    "1_START": {
        "title_tc": "第 1 頁：冰冷的完美指令", "title_en": "Page 1: The Cold Perfect Commands",
        "sfx": "🤖 系統運作中... SYSTEM RUNNING...",
        "story_tc": "在未來的「星際方舟」上，超級 AI 負責處理所有工作。但今天，方舟上的居民因為資源分配發生了嚴重的爭吵。AI 只是不斷發出「請遵守標準規則」的冰冷廣播，讓大家更生氣了，完全失去了信任！火鷹俠決定展現第一特質：",
        "story_en": "On the future 'Star Ark', a Super AI handles all tasks. But today, a serious argument broke out among citizens over resources. The AI just coldly broadcasts 'Please follow standard rules', making everyone angrier and destroying trust! Firebird decides to show the first trait:",
        "choices": {
            "A": {"text": "❤️ 展現「深度同理心與連結力」：親自走進人群，聆聽他們的情感與委屈，用溫暖的關懷重建信任！ (Show 'Deep Empathy & Connection': Walk into the crowd, listen to their feelings, and rebuild trust with warm care!)", "next": "2_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "💡 展現「高度適應力」：立刻學習新的資源分配法，手動調整機器的設定！ (Show 'Adaptability': Quickly learn a new resource allocation method and manually adjust the machines!)", "next": "2_B", "effect": {"creativity": 1, "bravery": 1}, "kla": ["TECH", "HUMANITIES"], "is_bad": False},
            "C": {"text": "📢 讓 AI 派出機器人警察，強行要求所有人安靜並回到房間！ (Let the AI send robot police to forcefully demand everyone to be quiet and return to their rooms!)", "next": "BAD_END_EMPATHY", "effect": {"empathy": -2}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "AI 可以給出最有效率的指令，但無法理解人類的情感！缺乏同理心的強硬手段只會讓衝突爆發。任務失敗……\n(AI gives efficient commands but cannot understand human emotions! Lacking empathy causes conflicts to explode. Mission failed...)"}
        }
    },

    # ===== 分支 A/B：第二試煉 (批判性思考與提問力) =====
    "2_A": {
        "title_tc": "第 2 頁：被數據淹沒的真相", "title_en": "Page 2: Truth Drowned in Data",
        "sfx": "📊 數據超載！DATA OVERLOAD!",
        "story_tc": "居民們平靜下來了。這時，方舟外部傳來警報！超級 AI 瞬間生成了 10,000 份標準化的數據報告，但卻無法決定該怎麼做。在唾手可得的龐大資訊中，火鷹俠決定展現第二特質：",
        "story_en": "The citizens calmed down. Suddenly, an external alarm rings! The Super AI instantly generates 10,000 standardized data reports but cannot decide what to do. Amidst this massive information, Firebird shows the second trait:",
        "choices": {
            "A": {"text": "🤔 展現「批判性思考與提問力」：不盲從數據，精準看穿問題本質，向 AI 提出最關鍵的好問題！ (Show 'Critical Thinking & Questioning': Don't follow blindly. See through the core and ask the AI the most crucial good question!)", "next": "3_A", "effect": {"creativity": 2, "bravery": 1}, "kla": ["SCIENCE", "HUMANITIES"], "is_bad": False},
            "C": {"text": "😵 盲目相信 AI，決定從第一份報告開始，把 10,000 份報告全部讀完再說！ (Blindly trust the AI and decide to read all 10,000 reports from the beginning!)", "next": "BAD_END_CRITICAL", "effect": {"creativity": -2}, "kla": ["TECH"], "is_bad": True,
                  "bad_reason": "未來的資訊唾手可得，盲目閱讀會錯失黃金時機！「定義問題」比「尋找答案」更重要。任務失敗……\n(Information is everywhere. Reading blindly misses the golden window! 'Defining the problem' is more important than finding answers. Mission failed...)"}
        }
    },
    
    "2_B": {
        "title_tc": "第 2 頁：被數據淹沒的真相", "title_en": "Page 2: Truth Drowned in Data",
        "sfx": "📊 數據超載！DATA OVERLOAD!",
        "story_tc": "你調整了機器，但方舟外部傳來警報！超級 AI 瞬間生成了 10,000 份標準化的數據報告，但卻無法決定該怎麼做。在唾手可得的龐大資訊中，火鷹俠決定展現第二特質：",
        "story_en": "You adjusted the machines, but an external alarm rings! The Super AI instantly generates 10,000 standardized data reports but cannot decide what to do. Amidst this massive information, Firebird shows the second trait:",
        "choices": {
            "A": {"text": "🤔 展現「批判性思考與提問力」：不盲從數據，精準看穿問題本質，向 AI 提出最關鍵的好問題！ (Show 'Critical Thinking & Questioning': Don't follow blindly. See through the core and ask the AI the most crucial good question!)", "next": "3_A", "effect": {"creativity": 2, "bravery": 1}, "kla": ["SCIENCE", "HUMANITIES"], "is_bad": False},
            "C": {"text": "😵 盲目相信 AI，決定從第一份報告開始，把 10,000 份報告全部讀完再說！ (Blindly trust the AI and decide to read all 10,000 reports from the beginning!)", "next": "BAD_END_CRITICAL", "effect": {"creativity": -2}, "kla": ["TECH"], "is_bad": True,
                  "bad_reason": "未來的資訊唾手可得，盲目閱讀會錯失黃金時機！「定義問題」比「尋找答案」更重要。任務失敗……\n(Information is everywhere. Reading blindly misses the golden window! 'Defining the problem' is more important than finding answers. Mission failed...)"}
        }
    },

    # ===== 第 3 頁：第三試煉 (高度適應力與終身學習) =====
    "3_A": {
        "title_tc": "第 3 頁：未知的千變星雲", "title_en": "Page 3: The Shifting Nebula",
        "sfx": "🌌 空間扭曲！WARPING!",
        "story_tc": "透過精準的提問，你發現方舟駛入了一個物理規則每秒都在改變的「千變星雲」。AI 的舊有數據全部失效，飛船即將失控！面對變動極快的未知環境，火鷹俠展現第三特質：",
        "story_en": "Through precise questioning, you found the Ark entered a 'Shifting Nebula' where physics rules change every second. AI's old data is useless! Facing this rapid unknown change, Firebird shows the third trait:",
        "choices": {
            "A": {"text": "🏃‍♂️ 展現「高度適應力與終身學習」：迅速打破既有認知，主動在變動中彈性學習新的駕駛技巧！ (Show 'Adaptability & Learning Agility': Break old mindsets, and flexibly learn new piloting skills in the midst of change!)", "next": "4_A", "effect": {"bravery": 2, "creativity": 1}, "kla": ["PE", "SCIENCE"], "is_bad": False},
            "B": {"text": "🤝 與方舟上的所有人建立深度的溝通網絡，集結所有人的智慧一起隨機應變！ (Build a deep communication network with everyone on the Ark, combining all wisdom to adapt on the fly!)", "next": "4_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES", "TECH"], "is_bad": False},
            "C": {"text": "📖 死守著古老的飛船駕駛手冊，拒絕改變任何操作方式！ (Stubbornly cling to the ancient spaceship manual and refuse to change any operations!)", "next": "BAD_END_ADAPT", "effect": {"creativity": -2}, "kla": ["SCIENCE"], "is_bad": True,
                  "bad_reason": "未來的環境變化極快，單一專業與死板的舊認知無法受用一生。不畏懼失敗的「終身學習」才是關鍵！任務失敗……\n(Future environments change fast. Rigid old knowledge won't last a lifetime. 'Lifelong learning' without fear of failure is key! Mission failed...)"}
        }
    },

    # ===== 第 4 頁：第四試煉 (創造力與美學感知) =====
    "4_A": {
        "title_tc": "第 4 頁：觸動靈魂的護盾", "title_en": "Page 4: The Soul-Touching Shield",
        "sfx": "✨ 閃亮！SPARKLE!",
        "story_tc": "你成功穩住了方舟！但要徹底穿越星雲，防護罩需要輸入一種「充滿靈魂與情感」的獨特能量波。生成式 AI 只能產出千篇一律的標準化波長，無法突破。火鷹俠展現第四特質：",
        "story_en": "You stabilized the Ark! But to pass through, the shield needs a unique energy wave 'full of soul and emotion'. GenAI can only produce standardized wavelengths. Firebird shows the fourth trait:",
        "choices": {
            "A": {"text": "🎨 展現「創造力與美學感知」：跨界融合音樂與色彩，創造出打破常規、觸動人心的獨特藝術波長！ (Show 'Creativity & Aesthetic Intuition': Cross-blend music and colors to create an unconventional, soul-touching artistic wavelength!)", "next": "5_A", "effect": {"creativity": 3}, "kla": ["ARTS", "TECH"], "is_bad": False},
            "B": {"text": "🌟 結合全人類的情感記憶，將大家最溫暖的故事轉化為強大的破局能量！ (Combine humanity's emotional memories, turning everyone's warmest stories into a powerful breakthrough energy!)", "next": "5_B", "effect": {"empathy": 2, "creativity": 1}, "kla": ["HUMANITIES", "ARTS"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：無可取代的人類靈魂！", "title_en": "Page 5: The Irreplaceable Human Soul!",
        "sfx": "🚀 突破！BREAKTHROUGH!",
        "story_tc": "美麗無雙的能量波點亮了整個星雲！方舟成功脫險。超級 AI 對你深感敬佩，因為它知道，這些特質是它永遠無法複製的。",
        "story_en": "The uniquely beautiful energy wave lit up the nebula! The Ark safely passed. The Super AI deeply respects you, knowing it can never replicate these traits.",
        "choices": {
            "A": {"text": "🏆 成為具備四大核心競爭力的「未來超級領袖」！ (Become a 'Future Super Leader' possessing the four core competencies!)", "next": "6_CREATIVE", "effect": {"creativity": 3}, "kla": ["ARTS", "SCIENCE"], "is_bad": False}
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：真正的人性光輝！", "title_en": "Page 5: The True Brilliance of Humanity!",
        "sfx": "👏 歡呼！CHEERS!",
        "story_tc": "溫暖的情感能量引導方舟航向了美麗的新世界。全體居民緊緊擁抱在一起，這是任何高效的 AI 都無法帶來的情感連結。",
        "story_en": "Warm emotional energy guided the Ark to a beautiful new world. Citizens embraced each other tightly—a connection no efficient AI could ever bring.",
        "choices": {
            "A": {"text": "🌟 成為擁有深度同理心與連結力的「全人小領袖」！ (Become a 'Whole-person Leader' with deep empathy and connection!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_EMPATHY": {
        "title_tc": "💥 任務失敗：冰冷的邏輯", "title_en": "Mission Failed: Cold Logic",
        "sfx": "📉 FALL!", "is_bad_ending": True,
        "story_tc": "AI 可以給出最有效率的指令，但無法理解人類的情感！高難度的溝通需要極高的人際感應力與同理心。",
        "story_en": "AI gives efficient commands but cannot understand human emotions! High-level communication requires extreme interpersonal sensing and empathy."
    },
    "BAD_END_CRITICAL": {
        "title_tc": "💥 任務失敗：迷失於數據", "title_en": "Mission Failed: Lost in Data",
        "sfx": "😵 DIZZY!", "is_bad_ending": True,
        "story_tc": "未來的答案唾手可得，但「如何定義問題」和「判別資訊真偽」的決策能力，才是決定成敗的關鍵。",
        "story_en": "Answers are everywhere in the future. 'Defining the problem' and 'distinguishing truth' are the keys to success."
    },
    "BAD_END_ADAPT": {
        "title_tc": "💥 任務失敗：拒絕改變", "title_en": "Mission Failed: Refusing to Change",
        "sfx": "❌ ERROR!", "is_bad_ending": True,
        "story_tc": "未來的產業更迭速度極快！「學習如何學習」且不畏懼失敗的適應力，才能讓你持續保持競爭力。",
        "story_en": "Future industries change rapidly! 'Learning how to learn' and adaptability without fear of failure keep you competitive."
    }
}
