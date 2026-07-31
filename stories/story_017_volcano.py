# ==============================================================================
# 🌋 火鷹俠 17：文字島的火山危機 (The Volcano Crisis on Lexicon Island)
# 融入 PERCCI 品格 (堅毅、尊重) + KLA (語文教育、人文-地理、科學教育)
# ==============================================================================

STORY_INFO = {
    "id": "Story17",
    "name_tc": "🌋 火鷹俠 17：文字島的火山危機",
    "name_en": "Firebird 17: The Volcano Crisis on Lexicon Island"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：語無倫次的精靈", "title_en": "Page 1: The Gibberish Sprites",
        "sfx": "🌋 轟隆隆！RUMBLE!",
        "story_tc": "大事不好了！「文字島」上的知識火山即將爆發！島上的「文字精靈」因為太久沒有人讀書，忘記了怎麼說完整的句子，只能語無倫次地慌亂奔跑。火鷹俠決定尋找進入火山核心的路線，阻止爆發：",
        "story_en": "Oh no! The Knowledge Volcano on 'Lexicon Island' is about to erupt! The 'Word Sprites' haven't read books in so long that they forgot how to speak properly and are running around in gibberish. Firebird must find a way to the volcano core:",
        "choices": {
            "A": {"text": "📖 運用「語文知識」，幫精靈把顛倒的句子重新排好，問出秘密通道！ (Use 'Language skills' to rearrange the sprites' jumbled sentences and ask for the secret path!)", "next": "2_A", "effect": {"creativity": 2}, "kla": ["LANG_CH", "LANG_EN"], "is_bad": False},
            "B": {"text": "📡 運用「地理科學」，拿出地質探測雷達尋找地下的岩漿流向！ (Use 'Geography', take out a geological radar to find the underground magma flow!)", "next": "2_B", "effect": {"bravery": 1}, "kla": ["SCIENCE", "TECH"], "is_bad": False},
            "C": {"text": "😡 嫌精靈說話太慢，大聲責罵他們並自己亂跑！ (Get impatient, scold the sprites for speaking too slowly, and run blindly!)", "next": "BAD_END_RUDE", "effect": {"empathy": -2}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "遇到別人表達不清楚時，我們應該耐心聆聽。大聲責罵只會讓精靈嚇哭！你迷路了，任務失敗……\n(When others struggle to speak, we should listen patiently. Scolding made them cry! You got lost. Mission failed...)"}
        }
    },

    # ===== 分支 A：語文解謎路線 =====
    "2_A": {
        "title_tc": "第 2 頁：成語木橋的考驗", "title_en": "Page 2: The Idiom Bridge Challenge",
        "sfx": "🌉 嘎吱！CREAK!",
        "story_tc": "精靈告訴了你捷徑，但這條捷徑必須經過一座「成語木橋」。橋上的守衛要求你填寫正確的字才能過橋：「一箭雙 _ (Two birds with one stone)」",
        "story_en": "The sprites told you the shortcut, but it crosses the 'Idiom Bridge'. The guard requires you to fill in the blank to pass: '一箭雙 _ (Two birds with one stone)'",
        "choices": {
            "A": {"text": "🦅 充滿自信地回答：「一箭雙雕」！ (Answer confidently: '一箭雙雕' (Eagle/Vulture)!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["LANG_CH", "HUMANITIES"], "is_bad": False},
            "B": {"text": "🤝 誠實地表示自己還沒學過，有禮貌地向守衛請教答案！ (Honestly admit you haven't learned it yet, and politely ask the guard for the answer!)", "next": "3_A", "effect": {"empathy": 2, "bravery": 1}, "kla": ["HUMANITIES", "LANG_CH"], "is_bad": False},
            "C": {"text": "🦆 隨便亂猜：「一箭雙鴨」！ (Guess randomly: '一箭雙鴨' (Two Ducks)!)", "next": "BAD_END_IDIOM", "effect": {"creativity": -2}, "kla": ["LANG_CH"], "is_bad": True,
                  "bad_reason": "成語是前人留下的語文智慧，不能隨便亂改哦！木橋收起了踏板，你過不去了。任務失敗……\n(Idioms are historical linguistic wisdom and shouldn't be changed randomly! The bridge retracted. Mission failed...)"}
        }
    },

    # ===== 分支 B：地質科學路線 =====
    "2_B": {
        "title_tc": "第 2 頁：阻擋熾熱岩漿", "title_en": "Page 2: Blocking the Scorching Magma",
        "sfx": "🔥 嘶嘶！SIZZLE!",
        "story_tc": "你用雷達找到了火山口，但發現熾熱的岩漿已經開始沿著山坡流下來了！火鷹俠必須運用地理與科學知識阻止岩漿蔓延到村莊：",
        "story_en": "You found the crater with the radar, but scorching magma is flowing down the slope! Firebird must use geography and science to stop it from reaching the village:",
        "choices": {
            "A": {"text": "📐 計算坡度，利用挖土機在旁邊挖一條深溝，將岩漿引流到大海冷卻 (STEAM)！ (Calculate the slope and dig a trench to divert the magma into the ocean to cool down!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "MATH", "TECH"], "is_bad": False},
            "B": {"text": "🛡️ 啟動超強冰凍防護盾，勇敢地站在村莊前擋住高溫！ (Activate the Super Freeze Shield and bravely stand before the village to block the heat!)", "next": "3_A", "effect": {"bravery": 2}, "kla": ["PE"], "is_bad": False},
            "C": {"text": "💨 用超級大風扇對著岩漿用力吹！ (Use a giant fan to blow hard at the magma!)", "next": "BAD_END_WIND", "effect": {"creativity": -2}, "kla": ["SCIENCE"], "is_bad": True,
                  "bad_reason": "岩漿溫度極高，吹風不但無法冷卻，還會讓火勢蔓延得更厲害！任務失敗……\n(Magma is extremely hot. Blowing wind won't cool it, it will spread the fire! Mission failed...)"}
        }
    },

    # ===== 第 3 頁匯合 =====
    "3_A": {
        "title_tc": "第 3 頁：知識守護神的心事", "title_en": "Page 3: The Knowledge Guardian's Sorrow",
        "sfx": "😔 唉... SIGH...",
        "story_tc": "你抵達了火山核心，遇到了「知識守護神」。原來，因為現在的小朋友只愛玩手機，不愛看故事書，文字的力量減弱了，導致地殼板塊變得不穩定，火山才會爆發。火鷹俠決定：",
        "story_en": "You reached the core and met the 'Knowledge Guardian'. The volcano is erupting because kids only play on phones and don't read books anymore, weakening the power of words and making tectonic plates unstable. Firebird decides to:",
        "choices": {
            "A": {"text": "📜 運用想像力，即席朗誦一首美麗的詩歌，讓守護神重新感受到文字的溫度！ (Use imagination to recite a beautiful poem on the spot, letting the Guardian feel the warmth of words again!)", "next": "4_A", "effect": {"creativity": 2, "empathy": 1}, "kla": ["LANG_CH", "ARTS"], "is_bad": False},
            "B": {"text": "誓言成為「閱讀推廣大使」，承諾每天都會堅持閱讀 20 分鐘 (Perseverance)！ (Vow to become a 'Reading Ambassador' and commit to reading 20 minutes every day!)", "next": "4_A", "effect": {"bravery": 1, "empathy": 1}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 第 4 頁 (最終挑戰) =====
    "4_A": {
        "title_tc": "第 4 頁：地熱壓力的釋放", "title_en": "Page 4: Releasing Geothermal Pressure",
        "sfx": "💨 噗嘶！HISS!",
        "story_tc": "守護神被你的真誠感動了！但他表示火山內部的壓力已經太高了，如果不安全釋放，還是會有危險。火鷹俠運用地理知識：",
        "story_en": "The Guardian is moved by your sincerity! But he says the pressure inside is too high, it must be released safely. Firebird uses geography knowledge:",
        "choices": {
            "A": {"text": "⛲ 引導地底的地下水與熱能結合，轉化成美麗又安全的「間歇泉 (Geyser)」噴發！ (Guide underground water to meet the heat, creating a beautiful and safe 'Geyser'!)", "next": "5_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "TECH"], "is_bad": False},
            "B": {"text": "📚 號召全世界的小朋友一起打開書本大聲朗讀，用閱讀的正能量平息地震！ (Call children worldwide to open books and read aloud, using the positive energy of reading to calm the quake!)", "next": "5_B", "effect": {"empathy": 2, "bravery": 1}, "kla": ["LANG_EN", "LANG_CH", "HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：科學與文學的奇蹟！", "title_en": "Page 5: The Miracle of Science and Literature!",
        "sfx": "🌈 壯觀！SPECTACULAR!",
        "story_tc": "間歇泉噴出了高高的水柱，在陽光下化作了一道彩虹！火山的危機解除了，文字島再次充滿了生機。",
        "story_en": "The geyser shot a high water column, creating a rainbow in the sun! The volcano crisis is over, and Lexicon Island is lively again.",
        "choices": {
            "A": {"text": "🏆 成為結合地質科學與語文智慧的「創意大師」！ (Become a 'Creative Master' combining geological science and language wisdom!)", "next": "6_CREATIVE", "effect": {"creativity": 3}, "kla": ["SCIENCE", "LANG_CH"], "is_bad": False}
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：閱讀力量的甦醒！", "title_en": "Page 5: Awakening the Power of Reading!",
        "sfx": "📖 朗朗讀書聲！READING!",
        "story_tc": "全世界傳來的朗讀聲化作了金色的光芒，徹底平息了地殼的震動！精靈們重新學會了說話，大家又開始愛上閱讀了。",
        "story_en": "The sound of reading from all over the world turned into golden light, completely calming the tectonic plates! The sprites relearned how to speak, and everyone loves reading again.",
        "choices": {
            "A": {"text": "🌟 成為推廣閱讀與文化傳承的「全人小領袖」！ (Become a 'Whole-person Leader' promoting reading and cultural heritage!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES", "LANG_CH", "LANG_EN"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_RUDE": {
        "title_tc": "💥 任務失敗：缺乏耐心", "title_en": "Mission Failed: Lack of Patience",
        "sfx": "😭 CRY!", "is_bad_ending": True,
        "story_tc": "當別人表達有困難時，我們應該展現同理心耐心聆聽，而不是發脾氣責罵。",
        "story_en": "When others struggle to express themselves, show empathy and listen patiently, do not scold them."
    },
    "BAD_END_IDIOM": {
        "title_tc": "💥 任務失敗：成語亂用", "title_en": "Mission Failed: Misused Idiom",
        "sfx": "❌ WRONG!", "is_bad_ending": True,
        "story_tc": "「一箭雙雕」是比喻做一件事達到兩個目的。我們平時要多看書，才能學會正確的成語哦！",
        "story_en": "'一箭雙雕' (Two birds with one stone) means achieving two goals with one action. We must read more to learn idioms correctly!"
    },
    "BAD_END_WIND": {
        "title_tc": "💥 任務失敗：火上加油", "title_en": "Mission Failed: Adding Fuel to Fire",
        "sfx": "🔥 BLAZE!", "is_bad_ending": True,
        "story_tc": "地理與科學常識告訴我們：岩漿溫度極高，用風扇吹不但無法冷卻，還會助長火勢！",
        "story_en": "Geography and science tell us: Magma is extremely hot. Blowing wind won't cool it, but will fan the flames!"
    }
}
