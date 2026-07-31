# ==============================================================================
# 💰 火鷹俠 11：金幣島的理財大挑戰 (The Financial Challenge on Gold Coin Island)
# 融入 PERCCI 品格 (堅毅、誠信) + KLA (數學教育、人文教育-經濟與社會)
# ==============================================================================

STORY_INFO = {
    "id": "Story11",
    "name_tc": "💰 火鷹俠 11：金幣島的理財大挑戰",
    "name_en": "Firebird 11: The Financial Challenge on Gold Coin Island"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：貪心妖精的搶劫！", "title_en": "Page 1: The Greedy Goblin's Heist!",
        "sfx": "🪙 叮叮噹！CHING CHING!",
        "story_tc": "大事不好了！金幣島上的「貪心妖精」偷走了大家的「財富之樹」，準備坐船逃跑！火鷹俠口袋裡只有 10 枚金幣的預算，他必須去碼頭買一艘船去追捕妖精。火鷹俠決定：",
        "story_en": "Oh no! The Greedy Goblin on Gold Coin Island stole the 'Tree of Wealth' and is escaping by boat! Firebird only has a budget of 10 gold coins. He must buy a boat at the dock to chase him. Firebird decides to:",
        "choices": {
            "A": {"text": "⛵ 花 4 枚金幣買一艘堅固實用的「基礎快艇」(Needs)，把剩下的 6 枚金幣存起來！ (Spend 4 coins on a sturdy, practical 'Basic Speedboat' and save the remaining 6 coins!)", "next": "2_A", "effect": {"creativity": 1, "bravery": 1}, "kla": ["MATH", "HUMANITIES"], "is_bad": False},
            "B": {"text": "🚢 花光 10 枚金幣，買一艘超級豪華但耗油的「黃金派對遊艇」(Wants)！ (Spend all 10 coins on a super luxurious but gas-guzzling 'Golden Party Yacht'!)", "next": "BAD_END_SPEND", "effect": {"bravery": -1}, "kla": ["MATH", "HUMANITIES"], "is_bad": True,
                  "bad_reason": "分不清「需要」和「想要」！你花光了所有錢，結果遊艇開到一半沒油了，你也沒有錢買汽油！任務失敗……\n(Confusing 'needs' and 'wants'! You spent all your money, the yacht ran out of gas, and you have no money to buy fuel! Mission failed...)"}
        }
    },

    # ===== 分支 A：聰明消費路線 =====
    "2_A": {
        "title_tc": "第 2 頁：神秘商人的投資選擇", "title_en": "Page 2: The Mysterious Merchant's Investment",
        "sfx": "🛒 歡迎光臨！WELCOME!",
        "story_tc": "你開著快艇追蹤妖精，途中遇到了一個神秘商人。商人說：「你現在有 6 枚金幣，你可以花 5 枚金幣買這個會發光的『超級炫酷陀螺』，或者花 3 枚金幣買一顆『投資種子』，明天它會長出 5 枚金幣哦！」火鷹俠展現理財智慧：",
        "story_en": "Chasing the goblin, you meet a mysterious merchant. He says: 'You have 6 coins. You can spend 5 coins on this glowing 'Super Cool Spinning Top', or 3 coins on an 'Investment Seed' that will grow into 5 coins tomorrow!' Firebird shows financial wisdom:",
        "choices": {
            "A": {"text": "🌱 展現堅毅 (延遲滿足)，花 3 枚金幣買「投資種子」，讓財富增長！ (Show perseverance/delayed gratification. Buy the 'Investment Seed' for 3 coins to grow your wealth!)", "next": "3_A", "effect": {"creativity": 2}, "kla": ["MATH", "HUMANITIES"], "is_bad": False},
            "B": {"text": "✨ 忍不住誘惑 (即時滿足)，花 5 枚金幣買下超級炫酷陀螺來玩！ (Can't resist instant gratification. Spend 5 coins to buy the Super Cool Spinning Top to play!)", "next": "BAD_END_TOY", "effect": {"bravery": -1}, "kla": ["MATH"], "is_bad": True,
                  "bad_reason": "只顧著眼前的享樂，沒有為未來打算！結果你的快艇壞了，你剩下的 1 枚金幣根本不夠付修理費！任務失敗……\n(Only focusing on instant pleasure without planning for the future! Your boat broke down, and 1 coin isn't enough for repairs! Mission failed...)"}
        }
    },

    # ===== 第 3 頁匯合 =====
    "3_A": {
        "title_tc": "第 3 頁：豐收與誠信的考驗", "title_en": "Page 3: Harvest and the Test of Integrity",
        "sfx": "📈 登登！GROWTH!",
        "story_tc": "第二天，你的投資種子長出了 5 枚金幣！加上你昨天剩下的 3 枚，你現在有 8 枚金幣了！你用這些錢買了「正義追捕網」，成功抓住了貪心妖精！但妖精偷偷對你說：",
        "story_en": "The next day, your investment seed grew into 5 coins! Adding your remaining 3 coins, you now have 8! You bought the 'Net of Justice' and caught the Greedy Goblin! But the goblin whispers to you:",
        "choices": {
            "A": {"text": "🙅‍♂️ 嚴詞拒絕！堅守誠信，把妖精交給島長，並把財富之樹還給島民！ (Refuse strictly! Uphold integrity, hand the goblin to the Island Chief, and return the Tree of Wealth to the islanders!)", "next": "4_A", "effect": {"empathy": 2, "bravery": 1}, "kla": ["HUMANITIES"], "is_bad": False},
            "B": {"text": "💰 「如果你放了我，我就給你 100 枚假金幣，你可以去買好多玩具！」 ('If you let me go, I will give you 100 fake coins to buy lots of toys!') 接受他的賄賂！ (Accept his bribe!)", "next": "BAD_END_BRIBE", "effect": {"empathy": -3}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "這是不誠實的行為 (Lack of Integrity)！假金幣被商店識破了，你被當成了妖精的同夥！任務失敗……\n(This is dishonest! The fake coins were exposed by shops, and you were treated as the goblin's accomplice! Mission failed...)"}
        }
    },

    # ===== 第 4 頁 (圓滿結局) =====
    "4_A": {
        "title_tc": "第 4 頁：財富分配的智慧", "title_en": "Page 4: The Wisdom of Wealth Distribution",
        "sfx": "🌳 閃閃發光！SPARKLE!",
        "story_tc": "妖精被抓住了，財富之樹重新在島中心種下，結出了許多金幣果實。島長為了感謝你，送給你一大袋金幣。火鷹俠決定如何運用這筆財富：",
        "story_en": "The goblin is caught. The Tree of Wealth is replanted and bears many gold coin fruits. To thank you, the Island Chief gives you a big bag of gold coins. Firebird decides how to use this wealth:",
        "choices": {
            "A": {"text": "🏦 建立「智慧銀行」：一部分儲蓄，一部分用來發明新科技幫助別人！ (Build a 'Bank of Wisdom': Save a portion, and use the rest to invent new tech to help others!)", "next": "6_INVENTOR", "effect": {"creativity": 3}, "kla": ["TECH", "MATH"], "is_bad": False},
            "B": {"text": "❤️ 建立「慈善基金」：把金幣用來幫助島上貧窮的孤兒，教他們讀書和理財！ (Build a 'Charity Fund': Use the coins to help poor orphans on the island, teaching them to read and manage money!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_SPEND": {
        "title_tc": "💥 任務失敗：過度消費", "title_en": "Mission Failed: Overspending",
        "sfx": "💸 破產！BANKRUPT!",
        "story_tc": "理財的第一步是分清「想要 (Wants)」和「需要 (Needs)」。買東西前要做好預算規劃！",
        "story_en": "The first step in financial literacy is distinguishing 'Wants' and 'Needs'. Make a budget before buying!"
    },
    "BAD_END_TOY": {
        "title_tc": "💥 任務失敗：缺乏延遲滿足", "title_en": "Mission Failed: Lack of Delayed Gratification",
        "sfx": "🧸 BROKEN!", "is_bad_ending": True,
        "story_tc": "為了一時的開心而花光積蓄是不明智的。我們要學會「延遲滿足」，為未來做準備！",
        "story_en": "Spending all savings for instant happiness is unwise. We must learn 'Delayed Gratification' to prepare for the future!"
    },
    "BAD_END_BRIBE": {
        "title_tc": "💥 任務失敗：失去誠信", "title_en": "Mission Failed: Lost Integrity",
        "sfx": "⚖️ GUILTY!", "is_bad_ending": True,
        "story_tc": "「誠信 (Integrity)」比任何金錢都重要。我們絕不能為了金錢而做壞事！",
        "story_en": "'Integrity' is more important than any amount of money. We must never do bad things for money!"
    }
}
