# ==============================================================================
# 💻 火鷹俠 18：數碼城市的網絡幻境 (The Cyber Illusion Mystery)
# 融入 PERCCI 品格 (誠信、尊重) + KLA (科技教育、人文教育-資訊素養)
# ==============================================================================

STORY_INFO = {
    "id": "Story18",
    "name_tc": "💻 火鷹俠 18：數碼城市的網絡幻境",
    "name_en": "Firebird 18: The Cyber Illusion Mystery"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：不明連結的危機！", "title_en": "Page 1: The Suspicious Link Crisis!",
        "sfx": "📱 叮咚！DING DONG!",
        "story_tc": "大事不好了！數碼城市裡出現了一隻「標題黨怪獸 (Clickbait Monster)」，他到處發送「免費送 100 萬顆鑽石，快點擊這裡！」的詐騙訊息。很多市民點擊後，電腦都中了病毒！火鷹俠決定進入網絡世界阻止他：",
        "story_en": "Oh no! A 'Clickbait Monster' is sending scam messages like 'Free 1,000,000 diamonds, click here!' in the Digital City. Many citizens clicked and got computer viruses! Firebird decides to enter the cyber world to stop him:",
        "choices": {
            "A": {"text": "🛡️ 啟動「超級防毒防火牆」，安全地掃描病毒來源 (STEAM)！ (Activate the 'Super Antivirus Firewall' to safely scan for the virus source!)", "next": "2_A", "effect": {"creativity": 2}, "kla": ["TECH"], "is_bad": False},
            "B": {"text": "🔍 運用邏輯追蹤 IP 地址，找出怪獸的藏身點！ (Use logic to trace the IP address and find the monster's hideout!)", "next": "2_B", "effect": {"bravery": 1, "creativity": 1}, "kla": ["MATH", "TECH"], "is_bad": False},
            "C": {"text": "🎁 覺得 100 萬顆鑽石太吸引了，忍不住點擊連結看看！ (Think 1,000,000 diamonds is too tempting and click the link to see!)", "next": "BAD_END_CLICK", "effect": {"bravery": -1}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "貪小便宜是很容易受騙的！你的系統中了病毒，裝備全部失效了！任務失敗……\n(Greed makes you an easy target for scams! Your system got a virus and all gear failed! Mission failed...)"}
        }
    },

    # ===== 分支 A：防火牆路線 (密碼學挑戰) =====
    "2_A": {
        "title_tc": "第 2 頁：安全大門的密碼", "title_en": "Page 2: The Security Gate Password",
        "sfx": "🔒 登入要求！LOGIN REQUIRED!",
        "story_tc": "你找到了怪獸的巢穴，但大門需要設定一個「全新且安全的強密碼 (Strong Password)」才能破解進入。火鷹俠運用科技知識：",
        "story_en": "You found the monster's lair, but the gate requires setting a 'Strong Password' to hack into it. Firebird uses tech knowledge:",
        "choices": {
            "A": {"text": "🔠 設定包含大草、小草字母、數字和特殊符號的長密碼 (如 F!reB1rd_88)！ (Set a long password with uppercase, lowercase, numbers, and symbols!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["TECH", "MATH"], "is_bad": False},
            "B": {"text": "👁️ 啟動生物辨識技術，利用獨一無二的「指紋和虹膜掃描」安全解鎖！ (Activate biometric tech, using unique fingerprint and iris scans to unlock safely!)", "next": "3_A", "effect": {"bravery": 1, "creativity": 1}, "kla": ["SCIENCE", "TECH"], "is_bad": False},
            "C": {"text": "🔢 為了方便記住，輸入最簡單的「123456」！ (To remember it easily, input the simplest '123456'!)", "next": "BAD_END_PASSWORD", "effect": {"creativity": -2}, "kla": ["TECH"], "is_bad": True,
                  "bad_reason": "密碼太簡單了！怪獸瞬間就猜中了你的密碼，把你反鎖在門外！任務失敗……\n(The password is too simple! The monster guessed it instantly and locked you out! Mission failed...)"}
        }
    },

    # ===== 分支 B：追蹤路線 (假新聞挑戰) =====
    "2_B": {
        "title_tc": "第 2 頁：真假難辨的謠言", "title_en": "Page 2: The Confusing Rumor",
        "sfx": "📰 突發新聞！BREAKING NEWS!",
        "story_tc": "在追蹤途中，你收到一條訊息：「數碼城市明天即將大爆炸！立刻轉發給 10 個人，否則你也會遭殃！」火鷹俠展現資訊素養 (Information Literacy)：",
        "story_en": "While tracking, you receive a message: 'Digital City will explode tomorrow! Forward to 10 people immediately or you will be doomed!' Firebird shows Information Literacy:",
        "choices": {
            "A": {"text": "🛑 保持冷靜，先去官方新聞網站查證消息是否真實！ (Stay calm and check official news websites to verify if the information is true!)", "next": "3_A", "effect": {"creativity": 1, "empathy": 1}, "kla": ["HUMANITIES", "LANG_CH"], "is_bad": False},
            "B": {"text": "💻 使用圖片分析程式，發現這張「爆炸圖片」是用電腦合成的假圖！ (Use image analysis software and discover the 'explosion image' is a fake CGI edit!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["TECH", "ARTS"], "is_bad": False},
            "C": {"text": "😱 太可怕了！立刻在沒有查證的情況下轉發給所有朋友！ (Too scary! Immediately forward it to all friends without verifying!)", "next": "BAD_END_RUMOR", "effect": {"bravery": -2}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "未經證實就轉發訊息，會製造社會恐慌，成為散播謠言的幫兇！任務失敗……\n(Forwarding unverified messages causes panic and makes you an accomplice to rumors! Mission failed...)"}
        }
    },

    # ===== 第 3 頁匯合 =====
    "3_A": {
        "title_tc": "第 3 頁：標題黨怪獸的孤單", "title_en": "Page 3: The Loneliness of the Clickbait Monster",
        "sfx": "👤 嘆息... SIGH...",
        "story_tc": "你突破了重重網絡陷阱，終於找到了怪獸！原來他是一個剛剛被寫出來的小程式，因為沒有人願意關注他，他才用「騙人的標題和假連結」來吸引大家的注意 (Likes)。火鷹俠決定：",
        "story_en": "You broke through the cyber traps and found the monster! He's just a newly coded program. Because no one paid attention to him, he used 'fake titles and scam links' to get Likes. Firebird decides to:",
        "choices": {
            "A": {"text": "⚖️ 嚴肅地教導他「誠信 (Integrity)」，告訴他用欺騙換來的關注是沒有意義的！ (Sternly teach him 'Integrity', explaining that attention gained through deception is meaningless!)", "next": "4_A", "effect": {"bravery": 2}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "❤️ 展現同理心，教導他寫出真正有用、有趣的內容，用實力獲得別人的「讚 (Likes)」！ (Show empathy, teach him to create genuinely useful and interesting content to earn real 'Likes'!)", "next": "4_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES", "LANG_CH"], "is_bad": False}
        }
    },

    # ===== 第 4 頁 (最終挑戰) =====
    "4_A": {
        "title_tc": "第 4 頁：修復網絡世界", "title_en": "Page 4: Fixing the Cyber World",
        "sfx": "⌨️ 劈哩啪啦！TYPING!",
        "story_tc": "怪獸明白自己錯了，並對造成病毒傳播感到很抱歉。他需要向全城市民發送一個「安全更新檔」來清除病毒。火鷹俠決定幫助他：",
        "story_en": "The monster realizes his mistake and feels sorry for spreading the virus. He needs to send a 'Security Patch' to all citizens to clear the virus. Firebird decides to help:",
        "choices": {
            "A": {"text": "🔐 運用編程技術，編寫一個帶有「官方加密認證」的發送系統，確保更新檔不會被篡改！ (Use coding skills to build a delivery system with 'Official Encrypted Certification' to ensure the patch isn't tampered with!)", "next": "5_A", "effect": {"creativity": 2}, "kla": ["TECH", "MATH"], "is_bad": False},
            "B": {"text": "🎨 為了讓老人家和小朋友都看懂，設計一張清晰又美麗的「網絡安全懶人包」圖文說明！ (To help elders and kids understand, design a clear and beautiful 'Cyber Security Infographic'!)", "next": "5_B", "effect": {"empathy": 1, "creativity": 1}, "kla": ["ARTS", "HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (結局分歧) =====
    "5_A": {
        "title_tc": "第 5 頁：頂尖的網絡守護者！", "title_en": "Page 5: The Top Cyber Guardian!",
        "sfx": "🛡️ 系統安全！SYSTEM SECURED!",
        "story_tc": "安全更新檔成功發送！市民的電腦全部恢復正常。你用高超的技術證明了科技可以用來保護大家！",
        "story_en": "The security patch was sent successfully! Citizens' computers are back to normal. You proved that technology can be used to protect everyone!",
        "choices": {
            "A": {"text": "🏆 成為捍衛數碼安全的「科技守護英雄」！ (Become a 'Tech Guardian Hero' who defends cyber security!)", "next": "6_INVENTOR", "effect": {"creativity": 3}, "kla": ["TECH"], "is_bad": False}
        }
    },
    "5_B": {
        "title_tc": "第 5 頁：優良的數碼公民！", "title_en": "Page 5: The Excellent Digital Citizen!",
        "sfx": "🌟 點讚！LIKE!",
        "story_tc": "你設計的懶人包廣受好評，所有市民都學會了如何分辨假新聞和設定強密碼。怪獸也成為了推廣網絡安全的吉祥物！",
        "story_en": "Your infographic is highly praised! All citizens learned how to spot fake news and set strong passwords. The monster became the cyber security mascot!",
        "choices": {
            "A": {"text": "🏅 成為推廣資訊素養與誠信的「全人小領袖」！ (Become a 'Whole-person Leader' promoting information literacy and integrity!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_CLICK": {
        "title_tc": "💥 任務失敗：貪心惹禍", "title_en": "Mission Failed: Greed Causes Trouble",
        "sfx": "☠️ VIRUS!", "is_bad_ending": True,
        "story_tc": "網絡上沒有免費的午餐！不要貪心點擊不明連結，這通常是駭客騙取個人資料的陷阱。",
        "story_en": "There's no free lunch on the internet! Don't greedily click unknown links; they are usually hackers' traps to steal personal info."
    },
    "BAD_END_PASSWORD": {
        "title_tc": "💥 任務失敗：密碼太弱", "title_en": "Mission Failed: Weak Password",
        "sfx": "🔓 HACKED!", "is_bad_ending": True,
        "story_tc": "像「123456」或「生日日期」這種密碼太容易被猜中了！為了保護網絡安全，我們必須學會設定強密碼。",
        "story_en": "Passwords like '123456' or 'birthdays' are too easy to guess! To protect cyber security, we must learn to set strong passwords."
    },
    "BAD_END_RUMOR": {
        "title_tc": "💥 任務失敗：散播假新聞", "title_en": "Mission Failed: Spreading Fake News",
        "sfx": "📉 PANIC!", "is_bad_ending": True,
        "story_tc": "在網絡世界中，我們要做一個負責任的數碼公民。收到驚悚的消息時，必須「停一停，諗一諗」，先查證後轉發！",
        "story_en": "In the cyber world, we must be responsible digital citizens. When receiving shocking news, 'Stop and Think', verify before forwarding!"
    }
}
