# ==============================================================================
# 🌟 火鷹俠 29：2034 未來之城的 EPOCH 密碼 (The EPOCH Code of the 2034 Future City)
# 融入 MIT Sloan 提出的未來 5 大不可取代能力 (EPOCH)：
# E (同理心)、P (人際連結)、O (倫理判斷)、C (創造力)、H (願景領導力)
# KLA: 人文教育(哲學與價值觀)、科技教育、藝術教育
# ==============================================================================

STORY_INFO = {
    "id": "Story29",
    "name_tc": "🌟 火鷹俠 29：2034 未來之城的 EPOCH 密碼",
    "name_en": "Firebird 29: The EPOCH Code of the 2034 Future City"
}

SCENES = {
    # ===== 起始：缺乏願景與領導力 (H - Hope, vision, and leadership) =====
    "1_START": {
        "title_tc": "第 1 頁：迷惘的超級電腦", "title_en": "Page 1: The Lost Supercomputer",
        "sfx": "💻 嗡嗡... BUZZ...",
        "story_tc": "時間來到 2034 年。在「極速之城」，AI 機器人能在 2 秒內完成所有工作。但今天，管理城市的超級 AI 突然當機了！它在螢幕上不斷閃爍著：「我不知道接下來該做甚麼？人類為什麼要活著？」AI 缺乏了設定目標的能力。火鷹俠決定展現 EPOCH 的第一種力量：",
        "story_en": "The year is 2034. In 'Speed City', AI robots finish all work in 2 seconds. But today, the Super AI running the city crashed! Its screen flashes: 'I don't know what to do next? Why do humans live?' The AI lacks the ability to set goals. Firebird decides to show the first EPOCH power:",
        "choices": {
            "A": {"text": "🔭 展現「希望、願景與領導力 (Hope, Vision & Leadership)」：畫出一幅充滿快樂與夢想的未來藍圖，帶領 AI 找到前進的方向！ (Show 'Hope, Vision & Leadership': Draw a future blueprint full of joy and dreams, leading the AI to find its direction!)", "next": "2_A", "effect": {"bravery": 2, "creativity": 1}, "kla": ["HUMANITIES", "ARTS"], "is_bad": False},
            "B": {"text": "⌨️ 敲打鍵盤，輸入更複雜的數學公式，逼迫 AI 自己計算出人生的意義！ (Hit the keyboard and input complex math formulas, forcing the AI to calculate the meaning of life itself!)", "next": "BAD_END_CALCULATE", "effect": {"creativity": -2}, "kla": ["TECH"], "is_bad": True,
                  "bad_reason": "AI 只能執行指令，它沒有生命，無法自己決定要追求什麼。尋找「為什麼」和「願景」，是人類獨有的價值！任務失敗……\n(AI only executes commands. It has no life and can't decide what to pursue. Finding 'Why' and 'Vision' is uniquely human! Mission failed...)"}
        }
    },

    # ===== 分支 A：人際連結與同理心 (E - Empathy & P - Presence/Networking) =====
    "2_A": {
        "title_tc": "第 2 頁：低效但快樂的農場", "title_en": "Page 2: The Inefficient But Happy Farm",
        "sfx": "🌱 挖土聲！DIGGING!",
        "story_tc": "AI 有了新目標，但它給出了一個提議：「為了最高效率，全體市民以後只需吃 1 秒鐘就能吞下的『化學營養丸』，不需要再花時間煮飯了！」火鷹俠搖搖頭，決定帶領市民展現 EPOCH 的第二與第三種力量：",
        "story_en": "The AI has a new goal, but proposes: 'For maximum efficiency, all citizens will only eat 1-second 'Chemical Nutrient Pills'. No more time wasted cooking!' Firebird shakes his head, leading citizens to show the second and third EPOCH powers:",
        "choices": {
            "A": {"text": "🤝 展現「同理心與人際連結 (Empathy & Presence)」：邀請大家一起在後院親手種菜！雖然又慢又辛苦 (低效)，但大家能聊天、互相幫忙，充滿了溫度！ (Show 'Empathy & Presence': Invite everyone to plant vegetables in the backyard! It's slow and hard (inefficient), but people can chat, help each other, and feel the warmth!)", "next": "3_A", "effect": {"empathy": 3}, "kla": ["HUMANITIES", "PE"], "is_bad": False},
            "B": {"text": "💊 為了追求極致的效率，同意 AI 的做法，每天只吃化學營養丸！ (To pursue extreme efficiency, agree with the AI and only eat chemical nutrient pills every day!)", "next": "BAD_END_EFFICIENCY", "effect": {"empathy": -2}, "kla": ["SCIENCE"], "is_bad": True,
                  "bad_reason": "工作與生活不僅僅是為了溫飽！親自動手的過程雖然低效，卻能帶來深層的滿足感和人際連結。任務失敗……\n(Work and life are not just about survival! The inefficient process of doing things hands-on brings deep satisfaction and human connection. Mission failed...)"}
        }
    },

    # ===== 第 3 頁匯合：倫理道德與判斷 (O - Opinion, judgment, and ethics) =====
    "3_A": {
        "title_tc": "第 3 頁：遊樂場的危機", "title_en": "Page 3: The Playground Crisis",
        "sfx": "🚧 拆除警報！DEMOLITION ALERT!",
        "story_tc": "大家在菜園裡笑得非常開心。但這時，AI 為了修建一條最快的高速公路，派出了推土機，準備拆除城市裡唯一的一座兒童遊樂場！AI 的數據顯示：「遊樂場沒有經濟效益。」火鷹俠決定展現 EPOCH 的第四種力量：",
        "story_en": "Everyone is laughing in the garden. But then, to build the fastest highway, the AI sends bulldozers to destroy the city's only children's playground! AI's data says: 'The playground has no economic benefit.' Firebird decides to show the fourth EPOCH power:",
        "choices": {
            "A": {"text": "⚖️ 展現「觀點、判斷與倫理道德 (Opinion, Judgment & Ethics)」：勇敢擋在推土機前，告訴 AI：「孩子們的快樂回憶是無價的，不能用冰冷的數據來衡量！」 (Show 'Opinion, Judgment & Ethics': Bravely stand before the bulldozer and tell the AI: 'Children's happy memories are priceless and cannot be measured by cold data!')", "next": "4_A", "effect": {"bravery": 2, "empathy": 2}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "📈 盲目聽從 AI 的數據分析，看著遊樂場被拆掉。 (Blindly follow the AI's data analysis and watch the playground get destroyed.)", "next": "BAD_END_ETHICS", "effect": {"empathy": -3}, "kla": ["MATH"], "is_bad": True,
                  "bad_reason": "AI 處理道德兩難的表現很差！人類的價值在於我們懂得判斷什麼是真正有意義的事物，而不只是看數據。任務失敗……\n(AI handles moral dilemmas poorly! Human value lies in judging what is truly meaningful, not just looking at data. Mission failed...)"}
        }
    },

    # ===== 第 4 頁：創造力與想像力 (C - Creativity and imagination) =====
    "4_A": {
        "title_tc": "第 4 頁：解鎖未來的密碼", "title_en": "Page 4: Unlocking the Future Code",
        "sfx": "✨ 閃耀！GLOW!",
        "story_tc": "AI 停止了推土機，它終於明白了人類的特別之處！為了解鎖未來之城的最高權限，讓 AI 成為人類出色的「助手」而不是「主人」，火鷹俠必須輸入最後一種力量作為密碼：",
        "story_en": "The AI stops the bulldozer; it finally understands what makes humans special! To unlock the highest access of the Future City, making AI a great 'assistant' instead of a 'master', Firebird must enter the last power as a password:",
        "choices": {
            "A": {"text": "🎨 展現「創造力與想像力 (Creativity & Imagination)」：在空中畫出一道繽紛的彩虹，將看似無關的科技與藝術跨界融合，輸入『EPOCH』密碼！ (Show 'Creativity & Imagination': Draw a colorful rainbow in the air, cross-blending seemingly unrelated tech and art, and enter the 'EPOCH' code!)", "next": "5_A", "effect": {"creativity": 3}, "kla": ["ARTS", "TECH"], "is_bad": False}
        }
    },

    # ===== 第 5 頁：結局 =====
    "5_A": {
        "title_tc": "第 5 頁：無可取代的人類！", "title_en": "Page 5: The Irreplaceable Human!",
        "sfx": "🎉 歡呼！CHEERS!",
        "story_tc": "密碼輸入成功！未來之城變得無比美好：AI 幫忙處理無聊的瑣事，而人類則專注於交朋友、創作藝術、種植美麗的花園。你證明了，擁有「EPOCH」能力的人類，永遠不會被取代！",
        "story_en": "Password accepted! The Future City becomes wonderful: AI handles boring chores, while humans focus on making friends, creating art, and planting beautiful gardens. You proved that humans with 'EPOCH' abilities will never be replaced!",
        "choices": {
            "A": {"text": "🌟 帶著 EPOCH 五大能力，成為探索未來的「全人小領袖」！ (Take the 5 EPOCH abilities and become a 'Whole-person Leader' exploring the future!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_CALCULATE": {
        "title_tc": "💥 任務失敗：失去願景", "title_en": "Mission Failed: Lost Vision",
        "sfx": "📉 ERROR!", "is_bad_ending": True,
        "story_tc": "AI 只是把人類想做的事做得更快，它無法自己決定「為什麼」要做。提出願景和領導方向，是人類的工作！",
        "story_en": "AI only does what humans want faster; it can't decide 'Why' to do it. Proposing a vision and leading the way is human work!"
    },
    "BAD_END_EFFICIENCY": {
        "title_tc": "💥 任務失敗：冰冷的效率", "title_en": "Mission Failed: Cold Efficiency",
        "sfx": "🤖 ROBOTIC!", "is_bad_ending": True,
        "story_tc": "有些事情雖然低效（例如親手種菜、和朋友聊天），但正是這些人際連結與臨場感，彰顯了身為人類的價值與快樂！",
        "story_en": "Some things are inefficient (like planting a garden or chatting with friends), but this connection and presence highlight the value and joy of being human!"
    },
    "BAD_END_ETHICS": {
        "title_tc": "💥 任務失敗：放棄道德判斷", "title_en": "Mission Failed: Abandoning Moral Judgment",
        "sfx": "❌ WRONG!", "is_bad_ending": True,
        "story_tc": "當面對道德兩難時，AI 的表現會很差。人類必須運用「觀點、判斷與倫理道德」來守護真正重要的事物。",
        "story_en": "AI performs poorly in moral dilemmas. Humans must use 'Opinion, Judgment, and Ethics' to protect what truly matters."
    }
}
