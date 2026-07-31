# ==============================================================================
# 🍽️ 火鷹俠 14：魔法廚房的化學大作戰 (The Magic Kitchen Chemistry Battle)
# 融入 PERCCI 品格 (承擔、同理心) + KLA (科學、數學、體育與健康)
# ==============================================================================

STORY_INFO = {
    "id": "Story14",
    "name_tc": "🍽️ 火鷹俠 14：魔法廚房的化學大作戰",
    "name_en": "Firebird 14: The Magic Kitchen Chemistry Battle"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：皇家廚房大混亂！", "title_en": "Page 1: The Royal Kitchen Chaos!",
        "sfx": "🍳 劈啪！SIZZLE!",
        "story_tc": "今晚是國王的大宴會，但「油膩搗蛋鬼」闖進了皇家廚房，把到處都弄得油膩膩的！如果不趕快清理並重新煮菜，宴會就要泡湯了。火鷹俠決定展現承擔精神 (Commitment)：",
        "story_en": "Tonight is the King's grand banquet, but the 'Greasy Goblin' messed up the royal kitchen! If it's not cleaned and cooked soon, the banquet is ruined. Firebird shows commitment:",
        "choices": {
            "A": {"text": "🍋 運用化學知識，混合熱水與檸檬酸，產生天然去污反應來清洗 (STEAM)！ (Use chemistry: mix hot water and citric acid for a natural cleaning reaction!)", "next": "2_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "TECH"], "is_bad": False},
            "B": {"text": "👨‍🍳 穿上主廚圍裙，勇敢地拿起大拖把和抹布，用汗水把廚房打掃乾淨！ (Put on a chef's apron and bravely clean the kitchen with a mop, cloth, and sweat!)", "next": "2_B", "effect": {"bravery": 1}, "kla": ["PE", "HUMANITIES"], "is_bad": False},
            "C": {"text": "🧪 把架子上所有五顏六色的化學清潔劑全部混合在一起噴灑！ (Mix all the colorful chemical cleaners on the shelf and spray everywhere!)", "next": "BAD_END_CHEMICAL", "effect": {"creativity": -1}, "kla": ["SCIENCE"], "is_bad": True,
                  "bad_reason": "隨便混合化學清潔劑非常危險，會產生有毒氣體！做科學實驗必須遵守安全守則。任務失敗……\n(Mixing chemical cleaners randomly is dangerous and creates toxic gas! Always follow safety rules. Mission failed...)"}
        }
    },

    # ===== 分支 A：化學清理路線 (數學挑戰) =====
    "2_A": {
        "title_tc": "第 2 頁：破裂的魔法食譜", "title_en": "Page 2: The Torn Magic Recipe",
        "sfx": "📜 撕啦！RIP!",
        "story_tc": "廚房變乾淨了！但你要烤的「勇氣蛋糕」，食譜被撕破了！上面寫著：「需要 1/2 杯麵粉，再加上 1/4 杯麵粉」。火鷹俠運用數學知識 (Fractions)：",
        "story_en": "The kitchen is clean! But the recipe for the 'Courage Cake' is torn! It says: 'Need 1/2 cup of flour, plus 1/4 cup of flour'. Firebird uses math:",
        "choices": {
            "A": {"text": "🧮 經過通分計算：1/2 加上 1/4 等於 3/4 杯麵粉！ (Calculate the fractions: 1/2 + 1/4 equals 3/4 cup of flour!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["MATH"], "is_bad": False},
            "B": {"text": "🤝 謙虛地向旁邊有經驗的老烘焙師請教正確的份量！ (Humbly ask the experienced old baker nearby for the correct amount!)", "next": "3_A", "effect": {"empathy": 1, "bravery": 1}, "kla": ["HUMANITIES"], "is_bad": False},
            "C": {"text": "🌪️ 不管了，把整整三大袋麵粉全部倒進攪拌機裡！ (Whatever! Pour three whole bags of flour into the mixer!)", "next": "BAD_END_MATH", "effect": {"creativity": -2}, "kla": ["MATH", "SCIENCE"], "is_bad": True,
                  "bad_reason": "烘焙是一門精密的科學！比例錯誤會讓蛋糕變成堅硬的石頭，攪拌機也卡壞了！任務失敗……\n(Baking is a precise science! Wrong ratios turned the cake into a rock and broke the mixer! Mission failed...)"}
        }
    },

    # ===== 分支 B：勞力打掃路線 (營養學挑戰) =====
    "2_B": {
        "title_tc": "第 2 頁：不均衡的七彩火鍋", "title_en": "Page 2: The Unbalanced Rainbow Hotpot",
        "sfx": "🍲 咕嚕嚕！BOILING!",
        "story_tc": "辛苦打掃完後，你要準備主菜「七彩火鍋」。但油膩搗蛋鬼在裡面加了太多油和肉，火鷹俠決定運用健康教育知識 (Nutrition)：",
        "story_en": "After hard cleaning, you prepare the main dish 'Rainbow Hotpot'. But the Goblin added too much oil and meat! Firebird uses health knowledge:",
        "choices": {
            "A": {"text": "🥦 加入大量的蔬菜、菇類和豆腐，讓食物金字塔的營養恢復均衡！ (Add lots of veggies, mushrooms, and tofu to balance the food pyramid nutrition!)", "next": "3_A", "effect": {"creativity": 1, "empathy": 1}, "kla": ["PE", "SCIENCE"], "is_bad": False},
            "B": {"text": "💪 展現體力，快速攪拌火鍋，利用離心力把多餘的油份撈出來 (STEAM)！ (Use physical strength to stir quickly, using centrifugal force to scoop out excess oil!)", "next": "3_A", "effect": {"bravery": 2, "creativity": 1}, "kla": ["SCIENCE", "PE"], "is_bad": False},
            "C": {"text": "🍭 為了讓湯變好喝，倒進 100 湯匙的白糖和彩色糖果！ (To make it tasty, pour in 100 spoons of sugar and colorful candies!)", "next": "BAD_END_HEALTH", "effect": {"empathy": -1}, "kla": ["PE"], "is_bad": True,
                  "bad_reason": "吸收過多糖分會導致蛀牙和肥胖！這完全不符合健康飲食原則，國王吃了一定會肚子痛。任務失敗……\n(Too much sugar causes cavities and obesity! This violates healthy eating rules. Mission failed...)"}
        }
    },

    # ===== 第 3 頁匯合 =====
    "3_A": {
        "title_tc": "第 3 頁：肚痛的搗蛋鬼", "title_en": "Page 3: The Goblin with a Stomachache",
        "sfx": "🤢 哎喲... OUCH...",
        "story_tc": "大餐快做好了！這時你發現「油膩搗蛋鬼」倒在角落，捂著肚子喊痛。原來他平時只吃垃圾食物，從不吃蔬菜，導致消化不良。火鷹俠決定：",
        "story_en": "The feast is almost ready! You find the Greasy Goblin in the corner, clutching his stomach in pain. He only eats junk food and no veggies, causing indigestion. Firebird decides to:",
        "choices": {
            "A": {"text": "❤️ 展現同理心，盛一碗富含膳食纖維的熱湯給他喝，教他健康飲食的重要性！ (Show empathy, serve him a bowl of fiber-rich hot soup, and teach him about healthy eating!)", "next": "4_A", "effect": {"empathy": 2}, "kla": ["PE", "HUMANITIES"], "is_bad": False},
            "B": {"text": "🛡️ 嚴厲地告訴他這就是偏食的後果，並要求他幫忙洗碗作為懲罰！ (Sternly tell him this is the consequence of picky eating, and make him wash dishes as punishment!)", "next": "4_A", "effect": {"bravery": 2}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 第 4 頁 (最終挑戰) =====
    "4_A": {
        "title_tc": "第 4 頁：完美上菜時間", "title_en": "Page 4: Perfect Serving Time",
        "sfx": "⏰ 叮！DING!",
        "story_tc": "搗蛋鬼喝了湯後舒服多了，也答應以後會均衡飲食。現在宴會時間到了，數百道菜需要完美無瑕地端上國王的餐桌！",
        "story_en": "The goblin feels better after the soup and promises to eat a balanced diet. It's banquet time! Hundreds of dishes must be served perfectly to the King's table!",
        "choices": {
            "A": {"text": "🤖 啟動編程系統，指揮「自動化送餐機械人」精準且快速地上菜 (STEAM)！ (Activate the coding system to command 'Automated Delivery Robots' to serve precisely and quickly!)", "next": "5_A", "effect": {"creativity": 2}, "kla": ["TECH", "MATH"], "is_bad": False},
            "B": {"text": "🤝 邀請搗蛋鬼和廚房裡的所有人組成接力隊伍，團結一致親手把菜端上去！ (Invite the goblin and everyone in the kitchen to form a relay team, serving the dishes together!)", "next": "5_B", "effect": {"empathy": 2, "bravery": 1}, "kla": ["HUMANITIES", "PE"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：高科技的魔法大宴會！", "title_en": "Page 5: The High-Tech Magic Banquet!",
        "sfx": "✨ 驚嘆！WOW!",
        "story_tc": "高科技送餐讓國王和賓客們大開眼界！食物不僅美味，營養比例也完美無缺，你成為了皇家御用的 STEAM 總廚！",
        "story_en": "The high-tech serving amazed the King and guests! The food was delicious with perfect nutritional balance. You became the Royal STEAM Executive Chef!",
        "choices": {
            "A": {"text": "🏆 繼續研發更多結合科技與健康的未來美食！ (Continue to invent more future cuisine combining tech and health!)", "next": "6_INVENTOR", "effect": {"creativity": 3}, "kla": ["TECH", "SCIENCE"], "is_bad": False}
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：充滿人情味的晚餐！", "title_en": "Page 5: A Heartwarming Dinner!",
        "sfx": "👏 鼓掌！APPLAUSE!",
        "story_tc": "團隊合作讓上菜充滿了人情味。國王知道搗蛋鬼改過自新後，邀請大家一起坐下來享用這頓充滿健康與包容的大餐！",
        "story_en": "Teamwork made the serving heartwarming. Knowing the goblin reformed, the King invited everyone to sit down and enjoy this healthy and inclusive feast!",
        "choices": {
            "A": {"text": "🌟 成為一位懂得包容與團隊合作的「全人小領袖」！ (Become a 'Whole-person Leader' who understands inclusivity and teamwork!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_CHEMICAL": {
        "title_tc": "💥 任務失敗：化學危機", "title_en": "Mission Failed: Chemical Crisis",
        "sfx": "☠️ TOXIC!", "is_bad_ending": True,
        "story_tc": "千萬不能隨便混合清潔劑！這樣會產生危險的化學反應，做科學實驗安全第一！",
        "story_en": "Never mix cleaning agents randomly! It causes dangerous chemical reactions. Safety first in science!"
    },
    "BAD_END_MATH": {
        "title_tc": "💥 任務失敗：食譜大暴走", "title_en": "Mission Failed: Recipe Disaster",
        "sfx": "🪨 CLUNK!", "is_bad_ending": True,
        "story_tc": "烘焙是一門講究精準比例的科學，需要好好運用數學（如分數）來計算，不能憑感覺亂倒！",
        "story_en": "Baking is a science of precise ratios. You must use math (like fractions) to calculate, not just pour blindly!"
    },
    "BAD_END_HEALTH": {
        "title_tc": "💥 任務失敗：糖分超標", "title_en": "Mission Failed: Sugar Overload",
        "sfx": "🦷 TOOTHACHE!", "is_bad_ending": True,
        "story_tc": "飲食要遵守食物金字塔的原則！攝取過多糖分會讓人肥胖和蛀牙，缺乏營養。",
        "story_en": "Follow the food pyramid rules! Consuming too much sugar causes obesity, cavities, and lacks nutrition."
    }
}
