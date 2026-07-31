# ==============================================================================
# 📘 火鷹俠 2：恐龍樂園大暴走 (Dinosaur Park Rampage)
# 融入 PERCCI 品格 (誠信、尊重) + STEAM (綠色能源、科學安全)
# ==============================================================================

STORY_INFO = {
    "id": "Story2",
    "name_tc": "📘 火鷹俠 2：恐龍樂園大暴走",
    "name_en": "Firebird 2: Dinosaur Park Rampage"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：恐龍樂園大暴走！", "title_en": "Page 1: Dinosaur Park Rampage!",
        "sfx": "🦖 吼吼！ROAR!",
        "story_tc": "大事不好了！主題樂園裡調皮的暴龍偷走了園長代表誠信與榮譽的「超級金盃」！火鷹俠決定進入樂園奪回金盃：",
        "story_en": "Oh no! The cheeky T-Rex stole the park director's 'Super Golden Trophy'! Firebird decides to retrieve it:",
        "choices": {
            "A": {"text": "🚀 啟動「超級火箭推進器」直接飛進樂園！ (Use Super Rocket Boosters to fly in!)", "next": "2_A", "effect": {"bravery": 1}, "is_bad": False},
            "B": {"text": "🤖 駕駛「超級機械三角龍」衝進樂園 (STEAM)！ (Ride a Super Robot Triceratops!)", "next": "2_B", "effect": {"creativity": 2}, "is_bad": False},
            "C": {"text": "🏀 變成一個巨大的彈力球，直接彈過樂園大門！ (Turn into a giant bouncy ball and bounce over the gate!)", "next": "2_C", "effect": {"creativity": 1}, "is_bad": False}
        }
    },

    # ===== 分支 A：火箭路線 =====
    "2_A": {
        "title_tc": "第 2 頁：長頸龍的噴水困境！", "title_en": "Page 2: Brachiosaurus Water Crisis!",
        "sfx": "💦 嘩啦！SPLASH!",
        "story_tc": "飛到一半，長頸龍因為耳朵進水不舒服，正在到處亂噴水柱！火鷹俠決定展現同理心：",
        "story_en": "Halfway there, a Brachiosaurus sprays water everywhere because its ears hurt! Firebird shows empathy:",
        "choices": {
            "A": {"text": "🩺 拿出巨型醫療工具，溫柔地幫長頸龍清理耳朵！ (Gently clean its ears using giant medical tools!)", "next": "3_A", "effect": {"empathy": 2}, "is_bad": False},
            "B": {"text": "🛡️ 打開防護傘，把水全部擋住並衝過去！ (Open a shield umbrella to block the water and rush through!)", "next": "3_A", "effect": {"bravery": 1}, "is_bad": False},
            "C": {"text": "⚡ 發射超級雷射光射向長頸龍！ (Shoot a super laser at the Brachiosaurus!)", "next": "BAD_END_DINO", "effect": {"empathy": -2}, "is_bad": True,
                  "bad_reason": "傷害動物是不對的行為！長頸龍大發雷霆，一腳把火箭踩扁了！任務失敗……\n(Hurting animals is wrong! The angry dino stomped your rocket! Mission failed...)"}
        }
    },

    # ===== 分支 B：機械三角龍路線 =====
    "2_B": {
        "title_tc": "第 2 頁：機械三角龍沒電了！", "title_en": "Page 2: Robot Triceratops Out of Battery!",
        "sfx": "🪫 嗶嗶... BEEP...",
        "story_tc": "衝到一半，機械三角龍的電池用光，停了下來！火鷹俠運用 STEAM 綠色能源知識：",
        "story_en": "Halfway there, the robot Triceratops runs out of battery! Firebird uses green energy knowledge:",
        "choices": {
            "A": {"text": "☀️ 展開太陽能板，吸收陽光轉化為電能 (STEAM)！ (Deploy solar panels to recharge with sunlight!)", "next": "3_A", "effect": {"creativity": 2}, "is_bad": False},
            "B": {"text": "🥕 拿出一根巨大的機械蘿蔔引誘牠繼續走！ (Use a giant robot carrot to lure it forward!)", "next": "3_A", "effect": {"creativity": 1}, "is_bad": False},
            "C": {"text": "⚡ 拿出高壓電線隨便亂接！ (Connect high-voltage wires randomly!)", "next": "BAD_END_ELEC", "effect": {"creativity": -1}, "is_bad": True,
                  "bad_reason": "亂接電線導致機械短路起火了！做科學實驗必須注意安全！任務失敗……\n(Random wiring caused a fire! Always practice safety in science! Mission failed...)"}
        }
    },

    # ===== 分支 C：彈力球路線 =====
    "2_C": {
        "title_tc": "第 2 頁：彈進翼龍的鳥巢！", "title_en": "Page 2: Bounced into a Pterodactyl Nest!",
        "sfx": "🪺 哎呀！OUCH!",
        "story_tc": "彈力球不小心掉進了懸崖上的翼龍鳥巢裡！火鷹俠決定尊重自然生態：",
        "story_en": "The bouncy ball lands in a Pterodactyl nest on the cliff! Firebird respects nature:",
        "choices": {
            "A": {"text": "🥚 小心地保持安靜，避免打擾恐龍蛋孵化！ (Stay quiet to avoid disturbing the hatching eggs!)", "next": "3_A", "effect": {"empathy": 1, "bravery": 1}, "is_bad": False},
            "B": {"text": "🪂 拿出降落傘，直接跳下懸崖前往樂園中心！ (Take out a parachute and jump off the cliff!)", "next": "3_A", "effect": {"bravery": 1}, "is_bad": False}
        }
    },

    # ===== 第 3 頁匯合 =====
    "3_A": {
        "title_tc": "第 3 頁：遇到調皮暴龍！", "title_en": "Page 3: Meeting the Cheeky T-Rex!",
        "sfx": "🦖 吼吼！ROAR!",
        "story_tc": "終於找到暴龍了！原來暴龍是因為蛀牙痛得發脾氣，才拿走金盃。火鷹俠決定：",
        "story_en": "Finally found the T-Rex! He took the trophy because of a painful toothache. Firebird decides to:",
        "choices": {
            "A": {"text": "🦷 展現勇氣，幫暴龍檢查蛀牙並教他刷牙！ (Show courage, check his toothache and teach him dental care!)", "next": "4_A", "effect": {"empathy": 2, "bravery": 1}, "is_bad": False},
            "B": {"text": "🍖 變出一塊無敵大雞腿送給他吃！ (Create a mega chicken drumstick for him!)", "next": "4_A", "effect": {"creativity": 1}, "is_bad": False}
        }
    },

    # ===== 第 4 頁 (反派現身) =====
    "4_A": {
        "title_tc": "第 4 頁：搗蛋魔法師現身！", "title_en": "Page 4: The Cheeky Wizard Appears!",
        "sfx": "🪄 嘻嘻！HEE HEE!",
        "story_tc": "原來是一名「搗蛋魔法師」在背後控制恐龍！他搶走了金盃並向你施法：",
        "story_en": "A Cheeky Wizard was controlling the dinos! He grabbed the trophy and cast a spell:",
        "choices": {
            "A": {"text": "🪞 拿出神奇反射鏡，把魔法全部反彈回去！ (Use a magic mirror to reflect all his magic!)", "next": "5_A", "effect": {"creativity": 2}, "is_bad": False},
            "B": {"text": "🤝 誠懇地跟他講道理，告訴他拿走別人的東西是不對的！ (Reason with him sincerely that stealing is wrong!)", "next": "5_A", "effect": {"empathy": 2}, "is_bad": False}
        }
    },

    # ===== 第 5 頁 (決戰與結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：奪回榮譽金盃！", "title_en": "Page 5: Recovering the Trophy!",
        "sfx": "🏆 閃閃發光！SPARKLE!",
        "story_tc": "魔法師知錯並道歉了！暴龍也恢復了健康。火鷹俠準備帶金盃回樂園：",
        "story_en": "The Wizard apologized and the T-Rex feels better. Firebird recovers the trophy:",
        "choices": {
            "A": {"text": "🎉 邀請魔法師和恐龍一起參加樂園和諧派對！ (Invite the Wizard and dinos to a park harmony party!)", "next": "6_LEADER", "effect": {"empathy": 3}, "is_bad": False},
            "B": {"text": "🏆 勇敢地將金盃歸還給園長，守護誠信！ (Bravely return the trophy to the park director, upholding integrity!)", "next": "6_HERO", "effect": {"bravery": 3}, "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_DINO": {
        "title_tc": "💥 任務失敗：暴龍大發雷霆", "title_en": "Mission Failed: Dino Rage",
        "sfx": "💥 BOOM!", "is_bad_ending": True,
        "story_tc": "傷害小動物是不對的！我們應該用同理心去了解他們的需求。",
        "story_en": "Hurting animals is wrong! We should use empathy to understand their needs."
    },
    "BAD_END_ELEC": {
        "title_tc": "💥 任務失敗：電線起火", "title_en": "Mission Failed: Electrical Fire",
        "sfx": "🔥 FIRE!", "is_bad_ending": True,
        "story_tc": "亂接電線非常危險！做科學實驗一定要注意安全規則！",
        "story_en": "Connecting wires randomly is dangerous! Always follow safety rules in science!"
    }
}
