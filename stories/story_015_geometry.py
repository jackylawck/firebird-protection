# ==============================================================================
# 📐 火鷹俠 15：幾何積木城的地震危機 (The Earthquake Crisis in Geometry City)
# 融入 PERCCI 品格 (堅毅、承擔) + KLA (數學教育、科學教育、科技教育)
# ==============================================================================

STORY_INFO = {
    "id": "Story15",
    "name_tc": "📐 火鷹俠 15：幾何積木城的地震危機",
    "name_en": "Firebird 15: The Earthquake Crisis in Geometry City"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：積木城大地震！", "title_en": "Page 1: The Great Geometry Quake!",
        "sfx": "🫨 轟隆隆！RUMBLE!",
        "story_tc": "大事不好了！由各種幾何形狀組成的「積木城」發生了強烈地震！原來是一隻「搖晃怪獸」在地下亂動，導致高樓大廈搖搖欲墜。火鷹俠決定展現承擔精神，拯救城市：",
        "story_en": "Oh no! A massive earthquake hit 'Geometry City', a place built with geometric shapes! A 'Wobbly Monster' is shaking underground, making skyscrapers sway. Firebird shows commitment to save the city:",
        "choices": {
            "A": {"text": "🏗️ 運用科技與科學，為大樓底部安裝「避震彈簧基座」(STEAM)！ (Use tech and science to install 'Shock-Absorbing Spring Bases' under buildings!)", "next": "2_A", "effect": {"creativity": 2}, "kla": ["TECH", "SCIENCE"], "is_bad": False},
            "B": {"text": "🦅 展現勇氣，飛上天空把快要掉下來的積木接住！ (Show courage, fly into the sky and catch the falling blocks!)", "next": "2_B", "effect": {"bravery": 1}, "kla": ["PE"], "is_bad": False},
            "C": {"text": "🧴 拿出超級萬能膠，把所有建築物死死地黏在地上！ (Take out Super Glue and stick all buildings rigidly to the ground!)", "next": "BAD_END_GLUE", "effect": {"creativity": -1}, "kla": ["SCIENCE"], "is_bad": True,
                  "bad_reason": "遇到地震時，建築物太過僵硬反而更容易斷裂！我們需要「柔性避震」的科學設計。任務失敗……\n(Rigid buildings break easily during earthquakes! We need flexible shock-absorbing designs. Mission failed...)"}
        }
    },

    # ===== 分支 A：避震路線 (數學圖形挑戰) =====
    "2_A": {
        "title_tc": "第 2 頁：斷裂的跨海大橋", "title_en": "Page 2: The Broken Bay Bridge",
        "sfx": "🌉 喀啦！CRACK!",
        "story_tc": "大樓穩住了！但連接市中心的「跨海大橋」斷裂了，市民無法逃生。你必須用積木重建橋樑的支撐結構，火鷹俠運用數學幾何知識：",
        "story_en": "The buildings are stable! But the Bay Bridge connecting the city center broke, trapping citizens. You must rebuild the bridge's support structure using blocks. Firebird uses math geometry:",
        "choices": {
            "A": {"text": "🔺 選擇「三角形」積木來搭建，因為它是所有幾何圖形中最堅固、最不易變形的 (STEAM)！ (Choose 'Triangle' blocks to build, as it's the strongest and most stable geometric shape!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["MATH", "SCIENCE"], "is_bad": False},
            "B": {"text": "🎨 發揮藝術創意，用美麗的「圓形」和「星形」積木拼成一座藝術彩虹橋！ (Use artistic creativity to build a beautiful rainbow bridge with 'Circle' and 'Star' blocks!)", "next": "3_A", "effect": {"creativity": 1, "empathy": 1}, "kla": ["ARTS"], "is_bad": False},
            "C": {"text": "🟦 選擇「正方形」積木來搭建支撐架！ (Choose 'Square' blocks to build the support frame!)", "next": "BAD_END_SQUARE", "effect": {"creativity": -2}, "kla": ["MATH", "SCIENCE"], "is_bad": True,
                  "bad_reason": "正方形受力時很容易變形變成平行四邊形！橋樑承受不住重量垮掉了！任務失敗……\n(Squares deform easily under pressure! The bridge collapsed under the weight! Mission failed...)"}
        }
    },

    # ===== 分支 B：接住積木路線 (物理挑戰) =====
    "2_B": {
        "title_tc": "第 2 頁：拯救被困的圓柱市長", "title_en": "Page 2: Saving Mayor Cylinder",
        "sfx": "🆘 救命！HELP!",
        "story_tc": "你接住了很多積木，但「圓柱市長」被一塊超級巨大的長方體積木壓住了，你用手根本搬不動！火鷹俠運用物理力學：",
        "story_en": "You caught many blocks, but 'Mayor Cylinder' is trapped under a massive rectangular block that's too heavy to lift by hand! Firebird uses physics:",
        "choices": {
            "A": {"text": "📏 找來一根長木條和一塊小石頭，利用「槓桿原理」輕鬆撬起巨石 (STEAM)！ (Find a long plank and a small stone, using the 'Principle of Leverage' to easily pry the heavy block up!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "TECH"], "is_bad": False},
            "B": {"text": "🤝 展現同理心，一邊安撫市長，一邊召集 100 個市民一起合力把積木推開！ (Show empathy, calm the Mayor, and gather 100 citizens to push the block together!)", "next": "3_A", "effect": {"empathy": 2, "bravery": 1}, "kla": ["HUMANITIES", "PE"], "is_bad": False}
        }
    },

    # ===== 第 3 頁匯合 =====
    "3_A": {
        "title_tc": "第 3 頁：搖晃怪獸的秘密", "title_en": "Page 3: The Wobbly Monster's Secret",
        "sfx": "🥺 嗝！HICCUP!",
        "story_tc": "你潛入地底找到了「搖晃怪獸」，發現他其實不是故意搞破壞的，而是因為吃太快導致了「超級大打嗝」，每打一個嗝，地面就會地震！火鷹俠決定：",
        "story_en": "You dove underground and found the Wobbly Monster. He wasn't destroying things on purpose; he ate too fast and got 'Super Hiccups'! Each hiccup causes an earthquake! Firebird decides to:",
        "choices": {
            "A": {"text": "💧 教導他科學止嗝法：大口喝溫水並閉氣 10 秒鐘！ (Teach him a scientific hiccup cure: Drink warm water and hold his breath for 10 seconds!)", "next": "4_A", "effect": {"creativity": 1, "empathy": 1}, "kla": ["SCIENCE", "PE"], "is_bad": False},
            "B": {"text": "🫂 給他一個溫暖的大擁抱，輕拍他的背幫他順氣 (Empathy)！ (Give him a warm big hug and gently pat his back to soothe him!)", "next": "4_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 第 4 頁 (最終挑戰) =====
    "4_A": {
        "title_tc": "第 4 頁：重建積木地標", "title_en": "Page 4: Rebuilding the Geometry Landmark",
        "sfx": "✨ 閃耀！SHINE!",
        "story_tc": "怪獸的打嗝停了！地震也結束了。為了彌補過失，怪獸想幫忙重建倒塌的城市地標「幾何高塔」。火鷹俠決定如何帶領大家：",
        "story_en": "The hiccups stopped! The earthquake is over. To make up for his mistake, the monster wants to help rebuild the fallen landmark, 'Geometry Tower'. Firebird decides how to lead:",
        "choices": {
            "A": {"text": "📐 指揮怪獸運用他的巨大力量，配合數學計算，建造一座結合了三角支撐與避震技術的「防震超級塔」！ (Direct the monster's strength with math calculations to build an 'Earthquake-Proof Super Tower' using triangular supports!)", "next": "5_A", "effect": {"creativity": 2}, "kla": ["MATH", "SCIENCE", "TECH"], "is_bad": False},
            "B": {"text": "🤝 展現包容，讓怪獸、圓柱市長和所有幾何市民一起手牽手，共同設計一座象徵團結的「友誼之塔」！ (Show inclusivity. Have the monster, Mayor, and all citizens hold hands to design a 'Tower of Friendship' symbolizing unity!)", "next": "5_B", "effect": {"empathy": 2, "bravery": 1}, "kla": ["HUMANITIES", "ARTS"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：最堅固的城市！", "title_en": "Page 5: The Strongest City!",
        "sfx": "🏆 屹立不搖！STABLE!",
        "story_tc": "全新的幾何高塔建成了！它運用了最頂尖的數學與科學知識，現在積木城再也不怕任何地震了！",
        "story_en": "The new Geometry Tower is built! It uses top-tier math and science knowledge. Now Geometry City fears no earthquakes!",
        "choices": {
            "A": {"text": "🌟 成為帶領城市進步的「創意發明家」！ (Become a 'Creative Inventor' who leads the city forward!)", "next": "6_INVENTOR", "effect": {"creativity": 3}, "kla": ["MATH", "TECH"], "is_bad": False}
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：充滿愛與包容的積木城！", "title_en": "Page 5: A City of Love and Inclusion!",
        "sfx": "🎉 歡呼！CHEERS!",
        "story_tc": "友誼之塔成為了城市裡最美麗的風景。怪獸也成為了積木城的榮譽市民，大家都學會了互相包容與幫助。",
        "story_en": "The Tower of Friendship became the most beautiful sight. The monster became an honorary citizen, and everyone learned inclusion and mutual help.",
        "choices": {
            "A": {"text": "🏅 成為守護和平與友誼的「全人小領袖」！ (Become a 'Whole-person Leader' who guards peace and friendship!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_GLUE": {
        "title_tc": "💥 任務失敗：僵硬的建築", "title_en": "Mission Failed: Rigid Buildings",
        "sfx": "💥 CRACK!", "is_bad_ending": True,
        "story_tc": "科學告訴我們，建築物在地震時需要有「彈性」來吸收震動。用膠水黏死反而更容易斷裂！",
        "story_en": "Science tells us buildings need 'flexibility' to absorb shocks during earthquakes. Gluing them rigidly makes them break easily!"
    },
    "BAD_END_SQUARE": {
        "title_tc": "💥 任務失敗：變形的橋樑", "title_en": "Mission Failed: Deformed Bridge",
        "sfx": "📉 COLLAPSE!", "is_bad_ending": True,
        "story_tc": "在幾何學中，正方形受力時很容易變形成平行四邊形。建造穩固的支架必須使用「三角形」！",
        "story_en": "In geometry, squares easily deform into parallelograms under pressure. You must use 'triangles' for a stable frame!"
    }
}
