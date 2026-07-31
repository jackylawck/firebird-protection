# ==============================================================================
# 🤝 火鷹俠 25：未來科技營的慷慨大賽 (The Generosity Contest at Future Tech Camp)
# 融入 輝達(NVIDIA) CEO 黃仁勳哲學：慷慨(Generosity)、由衷祝福他人、專注當下(Now)
# KLA: 人文教育(品德與價值觀)、科技教育、體育(體育精神)
# ==============================================================================

STORY_INFO = {
    "id": "Story25",
    "name_tc": "🤝 火鷹俠 25：未來科技營的慷慨大賽",
    "name_en": "Firebird 25: The Generosity Contest at Future Tech Camp"
}

SCENES = {
    # ===== 起始：競爭與意外 =====
    "1_START": {
        "title_tc": "第 1 頁：故障的對手機甲", "title_en": "Page 1: The Rival's Broken Mech",
        "sfx": "🔧 哐啷！CLANK!",
        "story_tc": "火鷹俠參加了「未來科技營」的機甲賽車總決賽！你的機甲狀態完美，但就在比賽快開始時，旁邊「閃電隊」的機甲突然引擎故障了，他們急得快哭了。火鷹俠決定：",
        "story_en": "Firebird is at the 'Future Tech Camp' Mech Racing Finals! Your mech is in perfect condition, but right before the race, the rival 'Lightning Team's' engine breaks down. They are almost crying. Firebird decides to:",
        "choices": {
            "A": {"text": "❤️ 展現「慷慨 (Generosity)」：主動走過去，拿出自己的備用零件和工具幫助他們修理！ (Show 'Generosity': Walk over, bring your spare parts and tools, and help them fix it!)", "next": "2_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES", "TECH"], "is_bad": False},
            "B": {"text": "🤝 展現「攜手共進」：邀請他們加入你的維修團隊，一起找出引擎故障的科學原因！ (Show 'Collaboration': Invite them to your pit stop to figure out the scientific cause of the engine failure together!)", "next": "2_A", "effect": {"creativity": 1, "empathy": 1}, "kla": ["SCIENCE", "HUMANITIES"], "is_bad": False},
            "C": {"text": "😈 心裡暗爽：「太好了，少了一個對手！」然後站在旁邊嘲笑他們。 (Secretly feel happy: 'Great, one less rival!' and stand aside to laugh at them.)", "next": "BAD_END_NARROW", "effect": {"empathy": -3}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "這就是「心胸狹隘」！看到別人失敗而感到開心，是無法成為真正受人尊敬的領袖的。任務失敗……\n(This is being 'narrow-minded'! Rejoicing in others' failures won't make you a respected leader. Mission failed...)"}
        }
    },

    # ===== 分支 A：專注當下 (Power of Now) =====
    "2_A": {
        "title_tc": "第 2 頁：倒數計時的壓力", "title_en": "Page 2: The Pressure of the Countdown",
        "sfx": "⏱️ 滴答滴答！TICK TOCK!",
        "story_tc": "你決定幫忙，但比賽只剩最後 3 分鐘了！大螢幕上的倒數計時器不斷閃爍，廣播一直催促，讓大家都感到非常恐慌。火鷹俠決定展現領袖特質：",
        "story_en": "You decide to help, but there are only 3 minutes left! The countdown timer on the big screen flashes, and the announcements cause panic. Firebird shows leadership traits:",
        "choices": {
            "A": {"text": "🧘‍♂️ 脫下手錶，告訴大家：「不要管時間，『此時此刻 (Now)』才是最重要的，專注把眼前的零件鎖好！」 (Take off your watch and say: 'Ignore the time. The 'Now' is what matters most. Just focus on fixing this part!')", "next": "3_A", "effect": {"bravery": 2, "creativity": 1}, "kla": ["HUMANITIES", "PE"], "is_bad": False},
            "B": {"text": "🛡️ 啟動「靜音防護罩」，把外界吵鬧的倒數聲隔絕，讓團隊能冷靜地完成最後的修理 (STEAM)！ (Activate a 'Mute Shield' to block the noisy countdown, letting the team calmly finish the final repairs!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["TECH", "SCIENCE"], "is_bad": False},
            "C": {"text": "😱 盯著時鐘大喊：「來不及了！我們死定了！」然後急得把零件弄掉一地。 (Stare at the clock and scream: 'It's too late! We are doomed!' and drop all the parts in panic.)", "next": "BAD_END_PANIC", "effect": {"bravery": -2}, "kla": ["PE"], "is_bad": True,
                  "bad_reason": "過度擔憂未來的時間，反而會搞砸現在的事情！我們必須專注於「此時此刻」。任務失敗……\n(Worrying too much about future time ruins the present! We must focus on the 'Here and Now'. Mission failed...)"}
        }
    },

    # ===== 第 3 頁：比賽結果與慷慨的考驗 =====
    "3_A": {
        "title_tc": "第 3 頁：衝線的瞬間！", "title_en": "Page 3: The Finish Line Moment!",
        "sfx": "🏁 衝線！SWOOSH!",
        "story_tc": "修好了！兩台機甲同時衝出起跑線！在激烈的比賽後，閃電隊的機甲竟然比你快了 0.1 秒，贏得了冠軍！面對自己幫助過的對手拿了第一名，火鷹俠決定：",
        "story_en": "Fixed! Both mechs dash from the start line! After a fierce race, Lightning Team's mech is 0.1 seconds faster and wins the championship! Facing the rival you helped winning first place, Firebird decides to:",
        "choices": {
            "A": {"text": "👏 展現最珍貴的「慷慨 (Generosity)」：打從心底為他們感到高興，真誠地鼓掌並祝福他們！ (Show the most precious 'Generosity': Feel happy for them from the bottom of your heart, sincerely clap and congratulate them!)", "next": "4_A", "effect": {"empathy": 3}, "kla": ["HUMANITIES", "PE"], "is_bad": False},
            "B": {"text": "🤝 走過去與他們握手，表示：「這是一場很棒的比賽，下次我們再一起攜手進步！」 (Walk over, shake hands and say: 'That was a great race! Let's improve together next time!')", "next": "4_A", "effect": {"bravery": 1, "empathy": 2}, "kla": ["HUMANITIES", "PE"], "is_bad": False},
            "C": {"text": "😡 生氣地大罵：「早知道我就不幫你們修了！把冠軍還給我！」 (Yell angrily: 'I shouldn't have helped you fix it! Give me back the championship!')", "next": "BAD_END_REGRET", "effect": {"empathy": -3}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "這不是真正的慷慨！如果你只在自己能贏的時候才幫人，那叫做施捨。真正的慷慨是由衷希望別人成功。任務失敗……\n(This isn't true generosity! Helping only when you can win is charity. True generosity is sincerely wishing others success. Mission failed...)"}
        }
    },

    # ===== 第 4 頁 (最終挑戰：無價的特質) =====
    "4_A": {
        "title_tc": "第 4 頁：神秘營長的頒獎", "title_en": "Page 4: Award from the Mysterious Camp Director",
        "sfx": "🏆 閃耀！SHINING!",
        "story_tc": "這時，穿著黑色皮衣的科技營營長走了出來。他說：「在 AI 時代，高智商並不稀奇。但你展現了『由衷希望別人成功』的善良品格，這才是無價的資產！」營長決定頒發一個特別獎項給你：",
        "story_en": "A Camp Director wearing a black leather jacket walks out. He says: 'In the AI era, high IQ isn't rare. But you showed the kind character of sincerely wishing others success, which is a priceless asset!' The Director decides to give you a special award:",
        "choices": {
            "A": {"text": "🎖️ 謙虛地接受「無價之星獎章」，並承諾未來會讓自己周圍充滿這樣善良、慷慨的人！ (Humbly accept the 'Priceless Star Medal' and promise to surround yourself with kind and generous people in the future!)", "next": "5_A", "effect": {"empathy": 2, "bravery": 1}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "🚀 邀請閃電隊一起上台領獎，表示「攜手共進」比打敗別人更重要！ (Invite the Lightning Team to the stage, showing that 'collaboration' is more important than defeating others!)", "next": "5_B", "effect": {"empathy": 2}, "kla": ["HUMANITIES", "PE"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：無價的領袖！", "title_en": "Page 5: The Priceless Leader!",
        "sfx": "🌟 歡呼！CHEERS!",
        "story_tc": "你的慷慨感動了所有人。大家發現，雖然你沒有拿到賽車冠軍，但你贏得了所有人的尊敬與友誼，你才是最偉大的贏家！",
        "story_en": "Your generosity moved everyone. People realized that although you didn't win the race, you won everyone's respect and friendship. You are the greatest winner!",
        "choices": {
            "A": {"text": "🌟 帶著這份無價的品格，成為一位心胸廣闊的「全人小領袖」！ (Take this priceless character and become a broad-minded 'Whole-person Leader'!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：攜手共進的未來！", "title_en": "Page 5: A Collaborative Future!",
        "sfx": "🤝 團結！UNITY!",
        "story_tc": "閃電隊決定把他們贏得的獎金與你平分，邀請你一起研發下一代的超級機甲！這就是慷慨帶來的無限奇蹟。",
        "story_en": "The Lightning Team decides to split their prize with you and invites you to develop the next-gen super mech together! This is the infinite miracle brought by generosity.",
        "choices": {
            "A": {"text": "🏆 成為懂得合作與分享的「創意發明家」！ (Become a 'Creative Inventor' who knows how to cooperate and share!)", "next": "6_INVENTOR", "effect": {"creativity": 3}, "kla": ["TECH", "HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_NARROW": {
        "title_tc": "💥 任務失敗：心胸狹隘", "title_en": "Mission Failed: Narrow-mindedness",
        "sfx": "📉 FALL!", "is_bad_ending": True,
        "story_tc": "有些心胸狹隘的人，看到別人成功或失敗時心裡會有惡意的想法。我們應該做一個心胸寬廣的人！",
        "story_en": "Narrow-minded people have malicious thoughts about others' successes or failures. We should be broad-minded!"
    },
    "BAD_END_PANIC": {
        "title_tc": "💥 任務失敗：被時間綁架", "title_en": "Mission Failed: Kidnapped by Time",
        "sfx": "😵 DIZZY!", "is_bad_ending": True,
        "story_tc": "不要一直盯著手錶看。我們應該放下對時間的焦慮，「此時此刻 (Now)」才是最重要的時間！",
        "story_en": "Don't keep staring at your watch. Let go of time anxiety. The 'Now' is the most important time!"
    },
    "BAD_END_REGRET": {
        "title_tc": "💥 任務失敗：虛假的慷慨", "title_en": "Mission Failed: Fake Generosity",
        "sfx": "❌ WRONG!", "is_bad_ending": True,
        "story_tc": "真正的慷慨是「我由衷希望你成功」，而不是「我幫你，但我必須贏」。學會真誠地為別人的成功鼓掌！",
        "story_en": "True generosity is 'I sincerely hope you succeed', not 'I help you, but I must win'. Learn to sincerely applaud others' success!"
    }
}
