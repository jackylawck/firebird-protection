# ==============================================================================
# 🦄 火鷹俠 27：獨角獸學院的極速挑戰 (The Fast-Track Trial at Unicorn Academy)
# 融入 頂尖人才 12 個獨角獸習慣：迅速反應、先發制人、準備充分、處事靈活等
# KLA: 人文教育(軟技巧與領導力)、科技教育、數學教育
# ==============================================================================

STORY_INFO = {
    "id": "Story27",
    "name_tc": "🦄 火鷹俠 27：獨角獸學院的極速挑戰",
    "name_en": "Firebird 27: The Fast-Track Trial at Unicorn Academy"
}

SCENES = {
    # ===== 起始：迅速反應 (習慣一) =====
    "1_START": {
        "title_tc": "第 1 頁：機會敲門的一瞬間", "title_en": "Page 1: The Moment Opportunity Knocks",
        "sfx": "⚡ 咚咚咚！KNOCK KNOCK!",
        "story_tc": "火鷹俠來到傳說中的「獨角獸學院」。大門口突然亮起紅燈，發布了一個緊急的「拯救星球任務」！周圍的學員還在猶豫、想等別人先動身時，火鷹俠決定展現第一個獨角獸習慣：",
        "story_en": "Firebird arrives at the legendary 'Unicorn Academy'. A red light flashes at the gate, posting an urgent 'Planet Rescue Mission'! While other students hesitate, waiting for others to move first, Firebird decides to show the first unicorn habit:",
        "choices": {
            "A": {"text": "⚡ 展現「迅速反應 (Speed to Respond)」：不遲疑、不拖延，自信且積極地立刻推開大門接下任務！ (Show 'Speed to Respond': Without hesitation or delay, confidently and actively push open the door to accept the mission!)", "next": "2_A", "effect": {"bravery": 2}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "🔍 展現「先發制人 (Anticipation)」：迅速掃描任務背后的微小跡象，預測可能遇到的危機並提前擬定對策！ (Show 'Anticipation': Quickly scan subtle signs behind the mission, predict crises, and prepare countermeasures in advance!)", "next": "2_B", "effect": {"creativity": 2}, "kla": ["SCIENCE", "TECH"], "is_bad": False},
            "C": {"text": "⏳ 聽信長輩的話「欲速則不達」，故意坐在原地等個幾天再考慮要不要回覆！ (Follow the old saying 'more haste, less speed', deliberately sit and wait a few days before deciding to reply!)", "next": "BAD_END_WAIT", "effect": {"bravery": -2}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "在瞬息萬變的時代裡，「速度快的贏」！盲目等待只會讓機會溜走。任務失敗……\n(In a fast-changing era, 'speed wins'! Waiting blindly lets opportunities slip away. Mission failed...)"}
        }
    },

    # ===== 分支 A：準備充分與好奇心 (習慣六、八) =====
    "2_A": {
        "title_tc": "第 2 頁：迷霧森林的未知難題", "title_en": "Page 2: The Unknown Riddle of the Foggy Forest",
        "sfx": "🌫️ 呼嘯... WHOOSH!",
        "story_tc": "你迅速出發，很快就抵達了充滿危險的「迷霧森林」。前方被一道上鎖的智能密碼門擋住。此時，運氣總是青睞有準備的人。火鷹俠決定：",
        "story_en": "You departed swiftly and soon reached the dangerous 'Foggy Forest'. Ahead is a locked smart password gate. As luck favors the prepared, Firebird decides:",
        "choices": {
            "A": {"text": "🎒 展現「準備充分 (Preparedness)」：拿出早已準備好的工具箱與密碼邏輯手冊，冷靜地將大門解鎖！ (Show 'Preparedness': Take out the pre-prepared toolkit and password logic manual, calmly unlocking the gate!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["MATH", "TECH"], "is_bad": False},
            "B": {"text": "🌱 展現「充滿好奇 (Curiosity)」：謙遜地多問、多聽，向森林裡的守護精靈請教這座門的歷史背景！ (Show 'Curiosity': Humbly ask more, listen well, and learn the gate's history from the forest sprites!)", "next": "3_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES", "LANG_CH"], "is_bad": False},
            "C": {"text": "🎲 覺得準備工具太麻煩，直接閉著眼睛用力猛踹大門！ (Think preparing tools is too much trouble, and just close your eyes and kick the door hard!)", "next": "BAD_END_KICK", "effect": {"bravery": -1}, "kla": ["PE"], "is_bad": True,
                  "bad_reason": "運氣總是留給準備好的人。沒有準備就用蠻力，只會讓自己受傷。任務失敗……\n(Luck favors the prepared. Using brute force without prep only gets you hurt. Mission failed...)"}
        }
    },

    # ===== 分支 B：處事靈活與解決問題 (習慣三、四) =====
    "2_B": {
        "title_tc": "第 2 頁：突發的能量斷層", "title_en": "Page 2: The Sudden Energy Fault",
        "sfx": "💥 滋滋！CRACKLE!",
        "story_tc": "透過先發制人的預測，你避開了第一波陷阱。但飛船的能量核心突然發生故障，原本的計劃行不通了！面對唯一的定律就是「變」的環境，火鷹俠決定：",
        "story_en": "Through anticipation, you avoided the first trap. But the spaceship's energy core suddenly malfunctions, and the original plan fails! Facing an environment where change is the only constant, Firebird decides:",
        "choices": {
            "A": {"text": "🌊 展現「處事靈活 (Flexibility)」：打破既有框架，靈活地調整飛行軌道，利用周圍的星光作為替代能源！ (Show 'Flexibility': Break existing frameworks, flexibly adjust the flight path, and use surrounding starlight as alternative energy!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["SCIENCE", "TECH"], "is_bad": False},
            "B": {"text": "🛠️ 展現「解決問題 (Problem Solving)」：不抱怨環境，立刻研究引擎故障的本質，動手把核心修好 (STEAM)！ (Show 'Problem Solving': Don't complain, immediately study the core's failure and fix it hands-on!)", "next": "3_A", "effect": {"bravery": 1, "creativity": 1}, "kla": ["MATH", "SCIENCE"], "is_bad": False},
            "C": {"text": "😭坐在地上大哭：「計劃失敗了！都是機器的錯！」然後放棄任務。 (Sit on the ground crying: 'The plan failed! It's all the machine's fault!' and give up the mission.)", "next": "BAD_END_COMPLAIN", "effect": {"creativity": -2}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "頂尖人才從不抱怨問題，而是研究如何解決問題。放棄就甚麼都沒有了！任務失敗……\n(Top talents never complain about problems; they figure out how to solve them. Giving up leaves you with nothing! Mission failed...)"}
        }
    },

    # ===== 第 3 頁匯合：廣結善緣與討人喜歡 (習慣九、十) =====
    "3_A": {
        "title_tc": "第 3 頁：遇見迷路的小精靈", "title_en": "Page 3: Meeting the Lost Sprite",
        "sfx": "🥺 嗚嗚... SOB...",
        "story_tc": "突破難關後，你遇到了幾隻因為害怕而迷路的小精靈。他們既不是評審，也不是能幫你加分的關鍵人物。火鷹俠展現了頂尖人才的待人哲學：",
        "story_en": "After clearing the hurdles, you meet some frightened and lost sprites. They are neither judges nor key figures who can boost your score. Firebird shows the interpersonal philosophy of top talents:",
        "choices": {
            "A": {"text": "💖 展現「廣結善緣 (Networking)」與「真誠 (Authenticity)」：善待每一個人，不只是善待「對」的人，溫柔地把他們護送回安全的地方！ (Show 'Networking' & 'Authenticity': Treat everyone well, not just the 'right' people, and gently escort them to safety!)", "next": "4_A", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "🗣️ 展現「討人喜歡 (Likability)」：用深思熟慮、清晰有禮的語調，耐心地給予他們鼓勵和指引！ (Show 'Likability': Use thoughtful, clear, and polite tones to patiently encourage and guide them!)", "next": "4_A", "effect": {"empathy": 2, "bravery": 1}, "kla": ["LANG_EN", "HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 第 4 頁 (最終挑戰：高生產力與目標導向) =====
    "4_A": {
        "title_tc": "第 4 頁：獨角獸的終極峰會", "title_en": "Page 4: The Unicorn Ultimate Summit",
        "sfx": "🌟 閃亮！SHINE!",
        "story_tc": "你帶著小精靈順利抵達了星球核心，完成了拯救任務！獨角獸學院的校長現身了，他稱讚你展現了迅速反應、靈活變通與廣結善緣。現在，迎向最後的目標：",
        "story_en": "You successfully reached the planetary core with the sprites and completed the rescue! The Unicorn Academy Headmaster appears, praising your speed, flexibility, and networking. Now, facing the final goal:",
        "choices": {
            "A": {"text": "🚀 展現「高生產力 (High Productivity)」與「目標導向 (Goal-Oriented)」：找到最適合自己的高效模式，帶著清晰的使命感，成為新一代的獨角獸人才！ (Show 'High Productivity' & 'Goal-Oriented': Find the most efficient personal mode, carry a clear sense of mission, and become a next-gen unicorn talent!)", "next": "5_A", "effect": {"creativity": 3}, "kla": ["TECH", "MATH"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (圓滿結局) =====
    "5_A": {
        "title_tc": "第 5 頁：真正的獨角獸領袖！", "title_en": "Page 5: The True Unicorn Leader!",
        "sfx": "🦄 嘶鳴！NEIGH!",
        "story_tc": "恭喜你！你集齊了 12 個獨角獸習慣的精髓。校長為你戴上了象徵頂尖卓越的「獨角獸徽章」。你明白了：成功不是偶然，而是把這些平凡卻難能可貴的好習慣融入生活中！",
        "story_en": "Congratulations! You gathered the essence of all 12 unicorn habits. The Headmaster pins the 'Unicorn Badge' symbolizing top excellence on you. You realize: success is no accident, but integrating these simple yet precious habits into daily life!",
        "choices": {
            "A": {"text": "🌟 帶著 12 個獨角獸習慣，成為一位追求卓越的「全人小領袖」！ (Carry the 12 unicorn habits and become an excellence-seeking 'Whole-person Leader'!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_WAIT": {
        "title_tc": "💥 任務失敗：錯失先機", "title_en": "Mission Failed: Missing the Window",
        "sfx": "📉 FALL!", "is_bad_ending": True,
        "story_tc": "盲目等待和刻意「冷處理」會讓你錯失黃金機會。在變動的時代中，速度往往決定了高度！",
        "story_en": "Blind waiting and deliberate 'cold treatment' make you miss golden opportunities. In a changing era, speed often determines height!"
    },
    "BAD_END_KICK": {
        "title_tc": "💥 任務失敗：毫無準備", "title_en": "Mission Failed: Unprepared",
        "sfx": "❌ OUCH!", "is_bad_ending": True,
        "story_tc": "運氣總是青睞有準備的人。沒有做好知識和工具的準備就盲目動手，只會招致失敗。",
        "story_en": "Luck favors the prepared. Acting blindly without knowledge and tool preparation only leads to failure."
    },
    "BAD_END_COMPLAIN": {
        "title_tc": "💥 任務失敗：抱怨代替解決", "title_en": "Mission Failed: Complaining Instead of Solving",
        "sfx": "🔊 COMPLAINT!", "is_bad_ending": True,
        "story_tc": "頂尖人才從不抱怨環境，而是研究如何解決問題。遇到變化時，保持靈活與彈性才是王道！",
        "story_en": "Top talents never complain about environments; they figure out how to solve problems. Staying flexible when facing changes is key!"
    }
}
