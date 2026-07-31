# ==============================================================================
# 🌩️ 火鷹俠 5：天空之城氣象危機 (Sky City Weather Crisis)
# 融入 PERCCI 品格 (誠信、同理心) + STEAM (氣象科學、雷達、避雷原理)
# ==============================================================================

STORY_INFO = {
    "id": "Story5",
    "name_tc": "🌩️ 火鷹俠 5：天空之城氣象危機",
    "name_en": "Firebird 5: Sky City Weather Crisis"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：失控的雷暴！", "title_en": "Page 1: Out of Control Thunderstorm!",
        "sfx": "⚡ 轟隆！KABOOM!",
        "story_tc": "大事不好了！負責控制天氣的「氣象機械人」突然失控，天空之城正下著可怕的暴風雨！火鷹俠決定飛上天空解決危機：",
        "story_en": "Oh no! The 'Weather Robot' is out of control, causing a massive thunderstorm over Sky City! Firebird decides to fly up and stop it:",
        "choices": {
            "A": {"text": "🚁 駕駛「超級太陽能直升機」穿過雲層 (STEAM)！ (Fly the Super Solar Helicopter through the clouds!)", "next": "2_A", "effect": {"creativity": 2}, "is_bad": False},
            "B": {"text": "🦅 召喚巨大的「神風老鷹」帶你飛上去！ (Summon the Giant Wind Eagle to carry you up!)", "next": "2_B", "effect": {"empathy": 1}, "is_bad": False},
            "C": {"text": "🎈 吹起一個巨大的防雷氣球升空！ (Blow up a giant lightning-proof balloon to float up!)", "next": "2_C", "effect": {"bravery": 1}, "is_bad": False}
        }
    },

    # ===== 分支 A：直升機路線 =====
    "2_A": {
        "title_tc": "第 2 頁：伸手不見五指的濃霧！", "title_en": "Page 2: The Thick Fog!",
        "sfx": "🌫️ 呼呼... WHOOSH...",
        "story_tc": "直升機飛到一半，遇上了超濃的白霧，完全看不見前方的路！火鷹俠決定：",
        "story_en": "Halfway up, the helicopter enters a thick fog. You can't see anything! Firebird decides to:",
        "choices": {
            "A": {"text": "📡 啟動超聲波雷達，利用聲波探測前方障礙物 (STEAM)！ (Use ultrasonic radar to detect obstacles!)", "next": "3_A", "effect": {"creativity": 2}, "is_bad": False},
            "B": {"text": "💨 開到最大馬力，用螺旋槳把濃霧吹散！ (Use full power to blow the fog away with the propeller!)", "next": "3_A", "effect": {"bravery": 1}, "is_bad": False},
            "C": {"text": "🙈 閉上眼睛，隨便亂飛碰運氣！ (Close your eyes and fly blindly!)", "next": "BAD_END_FOG", "effect": {"creativity": -1}, "is_bad": True,
                  "bad_reason": "駕駛時亂衝亂撞非常危險！直升機撞到了山峰！任務失敗……\n(Flying blindly is dangerous! The helicopter crashed into a mountain! Mission failed...)"}
        }
    },

    # ===== 分支 B：老鷹路線 =====
    "2_B": {
        "title_tc": "第 2 頁：害怕打雷的老鷹", "title_en": "Page 2: The Scared Eagle",
        "sfx": "🦅 吱吱... CHIRP...",
        "story_tc": "天空突然打了一個響雷，神風老鷹嚇得不敢往前飛！火鷹俠展現同理心：",
        "story_en": "A loud thunder strikes, and the Wind Eagle is too scared to fly! Firebird shows empathy:",
        "choices": {
            "A": {"text": "🎧 運用創意，為老鷹製作一副「防噪音耳罩」！ (Create noise-canceling earmuffs for the eagle!)", "next": "3_A", "effect": {"empathy": 2, "creativity": 1}, "is_bad": False},
            "B": {"text": "🎶 溫柔地抱著牠，唱一首充滿勇氣的歌鼓勵牠！ (Hug it gently and sing a courageous song!)", "next": "3_A", "effect": {"empathy": 1, "bravery": 1}, "is_bad": False},
            "C": {"text": "😡 大聲責罵老鷹，強迫牠繼續飛！ (Scold the eagle and force it to keep flying!)", "next": "BAD_END_EAGLE", "effect": {"empathy": -2}, "is_bad": True,
                  "bad_reason": "缺乏同理心！老鷹感到很傷心，直接飛走了，把你留在半空中！任務失敗……\n(Lack of empathy! The sad eagle flew away and left you in mid-air! Mission failed...)"}
        }
    },

    # ===== 分支 C：氣球路線 =====
    "2_C": {
        "title_tc": "第 2 頁：閃電劈過來了！", "title_en": "Page 2: Lightning Strikes!",
        "sfx": "⚡ 劈啪！CRACK!",
        "story_tc": "糟糕！一道巨大的閃電正朝著氣球劈過來！火鷹俠運用 STEAM 科學知識：",
        "story_en": "Oh no! A giant lightning bolt is striking towards the balloon! Firebird uses STEAM knowledge:",
        "choices": {
            "A": {"text": "⚡ 拋出一根「避雷針」把電流引導到旁邊的雲層！ (Throw a lightning rod to divert the electricity!)", "next": "3_A", "effect": {"creativity": 2}, "is_bad": False},
            "B": {"text": "🪂 展現勇氣，立刻穿上降落傘跳出氣球！ (Show courage, put on a parachute and jump out!)", "next": "3_A", "effect": {"bravery": 2}, "is_bad": False},
            "C": {"text": "🌳 躲在半空中的一根高大金屬柱子旁邊！ (Hide near a tall metal pole in the sky!)", "next": "BAD_END_LIGHTNING", "effect": {"creativity": -2}, "is_bad": True,
                  "bad_reason": "金屬會導電！在雷暴中靠近金屬柱子是非常危險的！任務失敗……\n(Metal conducts electricity! Hiding near a metal pole during a storm is dangerous! Mission failed...)"}
        }
    },

    # ===== 第 3 頁匯合 =====
    "3_A": {
        "title_tc": "第 3 頁：氣象塔的強風大門", "title_en": "Page 3: The Windy Door of the Tower",
        "sfx": "💨 呼呼！HOWL!",
        "story_tc": "你終於來到了氣象塔！但是大門前有一陣強風，把你吹得無法靠近。火鷹俠決定：",
        "story_en": "You finally reached the Weather Tower! But a strong wind blocks the door. Firebird decides to:",
        "choices": {
            "A": {"text": "⚙️ 調整門口的風車葉片角度，抵消強風 (STEAM)！ (Adjust the windmill blades to counter the wind!)", "next": "4_A", "effect": {"creativity": 2}, "is_bad": False},
            "B": {"text": "🛡️ 舉起超級防護盾，頂著強風硬闖進去！ (Raise the Super Shield and push through the wind!)", "next": "4_A", "effect": {"bravery": 2}, "is_bad": False},
            "C": {"text": "🚪 用盡全力亂踢大門！ (Kick the door as hard as you can!)", "next": "BAD_END_DOOR", "effect": {"bravery": -1}, "is_bad": True,
                  "bad_reason": "使用蠻力解決不了問題，反而把自己的腳弄痛了！任務失敗……\n(Brute force doesn't solve problems, it only hurts your foot! Mission failed...)"}
        }
    },

    # ===== 第 4 頁 (反派現身 / 核心衝突) =====
    "4_A": {
        "title_tc": "第 4 頁：哭泣的氣象機械人", "title_en": "Page 4: The Crying Weather Robot",
        "sfx": "😭 嗚嗚！SOB!",
        "story_tc": "進入氣象塔後，你發現氣象機械人躲在角落哭泣。牠承認自己不小心按錯按鈕引發了雷暴，但因為害怕被罵而隱瞞了真相。火鷹俠決定：",
        "story_en": "Inside the tower, the Weather Robot is crying. It admits it accidentally caused the storm but hid the truth because it was scared. Firebird decides to:",
        "choices": {
            "A": {"text": "🤝 教導牠「誠信」的重要性，鼓勵牠一起把錯誤修好！ (Teach it about Integrity and encourage it to fix the mistake together!)", "next": "5_A", "effect": {"empathy": 2, "bravery": 1}, "is_bad": False},
            "B": {"text": "🔧 不理會牠的哭泣，自己動手修理機器！ (Ignore its crying and fix the machine yourself!)", "next": "5_B", "effect": {"creativity": 2}, "is_bad": False}
        }
    },

    # ===== 第 5 頁 (決戰與結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：誠實與合作的力量！", "title_en": "Page 5: The Power of Honesty and Teamwork!",
        "sfx": "🌈 閃亮！SHINE!",
        "story_tc": "機械人明白了誠實的重要 (Integrity)，牠主動交出了控制密碼，和你一起修理氣象塔：",
        "story_en": "The robot learned the value of Integrity. It gave you the password and helped you fix the tower:",
        "choices": {
            "A": {"text": "☀️ 輸入密碼，為天空之城編寫一道美麗的彩虹！ (Program a beautiful rainbow for Sky City!)", "next": "6_LEADER", "effect": {"empathy": 2}, "is_bad": False},
            "B": {"text": "🛡️ 加上「安全鎖」程式，防止以後再按錯！ (Add a 'Safety Lock' to prevent future mistakes!)", "next": "6_INVENTOR", "effect": {"creativity": 2}, "is_bad": False}
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：獨自修理的挑戰！", "title_en": "Page 5: The Solo Repair Challenge!",
        "sfx": "⚙️ 咔嚓！CLICK!",
        "story_tc": "你獨自修理機器，但有一條電線太高了，你構不到！",
        "story_en": "You fix the machine alone, but a wire is too high to reach!",
        "choices": {
            "A": {"text": "🫂 主動邀請機械人幫忙，展現團隊合作精神！ (Invite the robot to help, showing teamwork!)", "next": "6_CARER", "effect": {"empathy": 2}, "is_bad": False},
            "B": {"text": "💪 展現過人的勇氣與體力，用力跳上去接駁電線！ (Show great courage and jump high to connect the wire!)", "next": "6_HERO", "effect": {"bravery": 2}, "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_FOG": {
        "title_tc": "💥 任務失敗：盲目飛行", "title_en": "Mission Failed: Blind Flying",
        "sfx": "💥 BOOM!", "is_bad_ending": True,
        "story_tc": "閉上眼睛亂飛是不負責任的行為！我們應該運用科學方法解決問題。",
        "story_en": "Flying blindly is irresponsible! We should use science to solve problems."
    },
    "BAD_END_EAGLE": {
        "title_tc": "💥 任務失敗：失去盟友", "title_en": "Mission Failed: Lost Ally",
        "sfx": "💨 WHOOSH!", "is_bad_ending": True,
        "story_tc": "遇到別人害怕時，我們應該展現同理心去鼓勵他，而不是責罵！",
        "story_en": "When others are scared, we should show empathy and encourage them, not scold them!"
    },
    "BAD_END_LIGHTNING": {
        "title_tc": "💥 任務失敗：雷電危險", "title_en": "Mission Failed: Lightning Danger",
        "sfx": "⚡ ZAP!", "is_bad_ending": True,
        "story_tc": "金屬是導電體！我們必須學習 STEAM 常識來保護自己！",
        "story_en": "Metal conducts electricity! We must learn STEAM knowledge to stay safe!"
    },
    "BAD_END_DOOR": {
        "title_tc": "💥 任務失敗：蠻力無用", "title_en": "Mission Failed: Brute Force Fails",
        "sfx": "🤕 OUCH!", "is_bad_ending": True,
        "story_tc": "遇到難關時，用蠻力發脾氣是無法解決問題的，冷靜思考才是好隊長！",
        "story_en": "Losing your temper and using brute force doesn't solve problems. A good captain thinks calmly!"
    }
}
