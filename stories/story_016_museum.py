# ==============================================================================
# 🎨 火鷹俠 16：魔法美術館的色彩危機 (The Color Crisis at the Magic Art Museum)
# 融入 PERCCI 品格 (同理心、尊重) + KLA (藝術教育、科學教育、人文)
# ==============================================================================

STORY_INFO = {
    "id": "Story16",
    "name_tc": "🎨 火鷹俠 16：魔法美術館的色彩危機",
    "name_en": "Firebird 16: The Color Crisis at the Magic Art Museum"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：變成黑白的世界！", "title_en": "Page 1: The Black-and-White World!",
        "sfx": "🎨 唰唰！SWISH!",
        "story_tc": "大事不好了！魔法美術館裡的「色彩大盜」偷走了所有名畫的顏色！現在蒙娜麗莎和梵高的星夜都變成了灰暗的黑白兩色。火鷹俠決定展現承擔精神，把美麗的色彩找回來：",
        "story_en": "Oh no! The 'Color Thief' at the Magic Art Museum has stolen all the colors from the famous paintings! Now the Mona Lisa and Starry Night are just dull black and white. Firebird takes responsibility to bring the beautiful colors back:",
        "choices": {
            "A": {"text": "📐 運用科學知識，拿出「三稜鏡」將白光折射成七色彩虹 (STEAM)！ (Use science, take out a 'Prism' to refract white light into a 7-color rainbow!)", "next": "2_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "TECH"], "is_bad": False},
            "B": {"text": "🖌️ 拿起一支與身高一樣大的「超級水彩筆」，準備親自為名畫重新上色！ (Grab a 'Super Paintbrush' as tall as you, ready to repaint the masterpieces yourself!)", "next": "2_B", "effect": {"bravery": 1}, "kla": ["ARTS", "PE"], "is_bad": False},
            "C": {"text": "🖤 覺得黑白太無聊了，直接把整桶黑墨水潑在畫上蓋住它們！ (Think black and white is boring, and just splash a bucket of black ink over them!)", "next": "BAD_END_INK", "effect": {"creativity": -1}, "kla": ["ARTS"], "is_bad": True,
                  "bad_reason": "破壞藝術品是非常不尊重的行為！這不但沒有解決問題，還把名畫徹底毀了。任務失敗……\n(Destroying artworks is highly disrespectful! This ruined the paintings completely. Mission failed...)"}
        }
    },

    # ===== 分支 A：科學光學路線 =====
    "2_A": {
        "title_tc": "第 2 頁：鏡子迷宮的光線反射", "title_en": "Page 2: Light Reflection in the Mirror Maze",
        "sfx": "✨ 閃耀！GLEAM!",
        "story_tc": "你用三稜鏡製造出了彩虹光束，但色彩大盜在走廊佈置了一個「鏡子迷宮」擋住光線！火鷹俠運用科學與數學知識：",
        "story_en": "You created a rainbow beam with the prism, but the Color Thief set up a 'Mirror Maze' to block the light! Firebird uses science and math:",
        "choices": {
            "A": {"text": "📐 計算「入射角等於反射角」的物理定律，精準轉動鏡子引導光線 (STEAM)！ (Calculate the physics law 'Angle of Incidence equals Angle of Reflection' to guide the light!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["MATH", "SCIENCE"], "is_bad": False},
            "B": {"text": "🛡️ 舉起火鷹俠防護盾，把光線像打乒乓球一樣直接反彈過去！ (Raise the Firebird Shield and bounce the light back like playing table tennis!)", "next": "3_A", "effect": {"bravery": 2}, "kla": ["PE", "SCIENCE"], "is_bad": False},
            "C": {"text": "🔨 覺得太麻煩了，直接把所有鏡子全部敲碎！ (Think it's too troublesome and smash all the mirrors!)", "next": "BAD_END_MIRROR", "effect": {"creativity": -2}, "kla": ["SCIENCE"], "is_bad": True,
                  "bad_reason": "碎掉的鏡子無法反射光線！你不但受傷了，彩虹光束也消失了。任務失敗……\n(Broken mirrors can't reflect light! You got hurt and the rainbow beam vanished. Mission failed...)"}
        }
    },

    # ===== 分支 B：藝術調色路線 =====
    "2_B": {
        "title_tc": "第 2 頁：尋找綠色的挑戰", "title_en": "Page 2: The Challenge of Finding Green",
        "sfx": "🎨 滴答！DRIP!",
        "story_tc": "你準備為大樹重新塗上「綠色」，但你的調色盤上只有紅 (Red)、黃 (Yellow) 和藍 (Blue) 這三種「三原色」！火鷹俠運用藝術知識：",
        "story_en": "You are ready to repaint the tree 'Green', but your palette only has the Primary Colors: Red, Yellow, and Blue! Firebird uses art knowledge:",
        "choices": {
            "A": {"text": "💙💛 知道「藍色 + 黃色 = 綠色」，精準地把兩種顏料混合起來 (STEAM)！ (Know that 'Blue + Yellow = Green', and mix the two paints precisely!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["ARTS", "SCIENCE"], "is_bad": False},
            "B": {"text": "🤝 展現尊重，禮貌地向畫中的人物借一點他們衣服上的綠色顏料！ (Show respect and politely ask the characters in the painting to borrow some green from their clothes!)", "next": "3_A", "effect": {"empathy": 1, "bravery": 1}, "kla": ["HUMANITIES", "ARTS"], "is_bad": False},
            "C": {"text": "🌪️ 不管了，把紅、黃、藍三種顏色全部亂混在一起！ (Whatever! Just mix Red, Yellow, and Blue all together randomly!)", "next": "BAD_END_MUD", "effect": {"creativity": -2}, "kla": ["ARTS"], "is_bad": True,
                  "bad_reason": "三原色全部混在一起會變成髒髒的泥巴咖啡色 (Brown)！美麗的大樹變成了一團爛泥。任務失敗……\n(Mixing all primary colors creates muddy brown! The beautiful tree turned into mud. Mission failed...)"}
        }
    },

    # ===== 第 3 頁匯合 =====
    "3_A": {
        "title_tc": "第 3 頁：色彩大盜的心聲", "title_en": "Page 3: The Color Thief's Confession",
        "sfx": "😢 嘆氣... SIGH...",
        "story_tc": "你終於追上了色彩大盜！但他並沒有逃跑，而是對著一堆顏色發呆。原來他患有「色弱 (Color blindness)」，分不清紅綠色，因為太羨慕別人能看到繽紛的世界，才衝動偷走色彩。火鷹俠決定：",
        "story_en": "You finally caught the Color Thief! But he isn't running; he's staring blankly at the colors. He actually has 'Color blindness' and can't distinguish red and green. He stole them out of envy. Firebird decides to:",
        "choices": {
            "A": {"text": "👓 運用科技發明一副「色彩校正智能眼鏡」，幫助他看到真實的顏色！ (Use tech to invent 'Color-correcting Smart Glasses' to help him see true colors!)", "next": "4_A", "effect": {"creativity": 2, "empathy": 1}, "kla": ["TECH", "SCIENCE", "HUMANITIES"], "is_bad": False},
            "B": {"text": "🎨 展現同理心，教導他「黑白素描 (Sketching)」與「光影」同樣是一門極高深的藝術！ (Show empathy, teach him that black-and-white sketching and lighting are also profound arts!)", "next": "4_A", "effect": {"empathy": 2}, "kla": ["ARTS", "HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 第 4 頁 (最終挑戰) =====
    "4_A": {
        "title_tc": "第 4 頁：修復蒙娜麗莎", "title_en": "Page 4: Restoring the Mona Lisa",
        "sfx": "🖼️ 閃閃發光！SPARKLE!",
        "story_tc": "大盜感動得哭了，他主動交出了所有色彩，並向美術館道歉。現在，只剩下最後一幅名畫《蒙娜麗莎》需要修復，火鷹俠決定帶領大家一起完成：",
        "story_en": "The thief cried with joy, returned all colors, and apologized. Now, only the final masterpiece 'Mona Lisa' needs restoration. Firebird leads the team:",
        "choices": {
            "A": {"text": "👨‍🎨 邀請色彩大盜一起動手，用同理心與合作精神為蒙娜麗莎畫上最美的微笑！ (Invite the thief to join, using empathy and teamwork to paint Mona Lisa's beautiful smile!)", "next": "5_A", "effect": {"empathy": 2, "bravery": 1}, "kla": ["ARTS", "HUMANITIES"], "is_bad": False},
            "B": {"text": "💻 使用高科技的光學投影技術，把色彩 100% 精準地還原到畫布上 (STEAM)！ (Use high-tech optical projection to restore the colors 100% accurately onto the canvas!)", "next": "5_B", "effect": {"creativity": 2}, "kla": ["TECH", "SCIENCE"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：最包容的美術館！", "title_en": "Page 5: The Most Inclusive Museum!",
        "sfx": "👏 掌聲如雷！APPLAUSE!",
        "story_tc": "名畫全部恢復了色彩！色彩大盜成為了美術館的「特別藝術導賞員」，專門教導大家欣賞不同視角的美。你成為了包容與愛的英雄！",
        "story_en": "All masterpieces are restored! The thief became a 'Special Art Guide', teaching everyone to appreciate beauty from different perspectives. You are a hero of inclusion!",
        "choices": {
            "A": {"text": "🌟 成為一位懂得包容與藝術欣賞的「全人小領袖」！ (Become a 'Whole-person Leader' who understands inclusion and art appreciation!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES", "ARTS"], "is_bad": False}
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：科技與藝術的完美結合！", "title_en": "Page 5: Perfect Blend of Tech and Art!",
        "sfx": "✨ 奇蹟！MIRACLE!",
        "story_tc": "高科技的投影讓名畫比以前更加鮮豔動人！你成功證明了科學與藝術結合，能創造出無限的奇蹟。",
        "story_en": "The high-tech projection made the paintings more vibrant than ever! You proved that blending science and art creates infinite miracles.",
        "choices": {
            "A": {"text": "🏆 成為結合美感與科學的「創意大師」！ (Become a 'Creative Master' who combines aesthetics and science!)", "next": "6_CREATIVE", "effect": {"creativity": 3}, "kla": ["TECH", "ARTS"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_INK": {
        "title_tc": "💥 任務失敗：毀壞藝術品", "title_en": "Mission Failed: Destroying Art",
        "sfx": "🖤 SPLASH!", "is_bad_ending": True,
        "story_tc": "藝術品是人類珍貴的歷史文化，我們必須學會尊重和保護它們，絕對不能搞破壞！",
        "story_en": "Artworks are precious human heritage. We must learn to respect and protect them, never destroy them!"
    },
    "BAD_END_MIRROR": {
        "title_tc": "💥 任務失敗：失去反射", "title_en": "Mission Failed: Lost Reflection",
        "sfx": "🔨 CRASH!", "is_bad_ending": True,
        "story_tc": "在科學中，鏡子利用「反射」來傳遞光線。敲碎了鏡子，光線就無法到達目的地了！",
        "story_en": "In science, mirrors use 'reflection' to transmit light. Breaking them means light can't reach its destination!"
    },
    "BAD_END_MUD": {
        "title_tc": "💥 任務失敗：變成爛泥色", "title_en": "Mission Failed: Muddy Colors",
        "sfx": "🎨 MESSY!", "is_bad_ending": True,
        "story_tc": "藝術色彩學告訴我們：紅、黃、藍三原色全部混在一起，就會變成髒髒的深啡色！要小心調色。",
        "story_en": "Art color theory tells us: mixing all primary colors (Red, Yellow, Blue) makes a muddy dark brown! Mix carefully."
    }
}
