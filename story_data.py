# ==============================================================================
# 🦸‍♂️ 火鷹俠全人教育繪本資料庫 (標準書面語 × 雙語並行版)
# 適合即將升讀小學的小朋友，同步建立中文書面語與英文語感。
# ==============================================================================

def get_ending_key(stats):
    b, c, e = stats.get("bravery", 0), stats.get("creativity", 0), stats.get("empathy", 0)
    if b >= 3 and e >= 3:
        return "6_LEADER"
    elif b >= 4 and c >= 2:
        return "6_HERO"
    elif c >= 4 and e >= 2:
        return "6_INVENTOR"
    elif e >= 4 and b >= 2:
        return "6_CARER"
    elif b >= 5:
        return "6_BRAVE"
    elif c >= 5:
        return "6_CREATIVE"
    elif e >= 5:
        return "6_EMPATHY"
    else:
        return "6_DEFAULT"

STORY_1_SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：玩具失竊大危機！", "title_en": "Page 1: The Great Toy Crisis!",
        "sfx": "🚨 嗚哇！WEE WOO!",
        "images": ["https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Lego_Color_Bricks.jpg/800px-Lego_Color_Bricks.jpg"],
        "story_tc": "大事不好了！「糖果外星人」偷走了全城小朋友最喜愛的玩具！火鷹俠必須前往外星基地奪回玩具，展現勇氣與承擔，他決定：",
        "story_en": "Oh no! The 'Candy Aliens' stole all the kids' favorite toys! Firebird must show courage and commitment to get them back. He decides to:",
        "choices": {
            "A": {"text": "🚀 坐上「超級彩虹推進火箭」飛上太空！ (Ride the Super Rainbow Rocket into space!)", "next": "2_A", "effect": {"bravery": 1}, "is_bad": False},
            "B": {"text": "🦆 召喚一隻跟大廈一樣高的「超級黃色膠鴨」！ (Summon a building-sized Super Rubber Duck!)", "next": "2_B", "effect": {"creativity": 1}, "is_bad": False},
            "C": {"text": "📦 跳進神奇紙皮箱，動手改造成宇宙飛船 (STEAM)！ (Jump into a magic cardboard box and build a spaceship!)", "next": "2_C", "effect": {"creativity": 2}, "is_bad": False}
        }
    },

    # ===== 分支 A：火箭路線 =====
    "2_A": {
        "title_tc": "第 2 頁：會飛的披薩隕石！", "title_en": "Page 2: Flying Pizza Meteors!",
        "sfx": "🍕 砰！BAM!",
        "images": ["https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Eq_it-na_pizza-margherita_sep2005_smn.jpg/800px-Eq_it-na_pizza-margherita_sep2005_smn.jpg"],
        "story_tc": "火箭飛到一半，遇到了一陣會飛的披薩隕石雨！面對困難，火鷹俠決定展現堅毅：",
        "story_en": "Halfway to space, the rocket meets a storm of flying Pizza Meteors! Showing perseverance, Firebird decides to:",
        "choices": {
            "A": {"text": "🔥 噴出火鷹烈焰，把披薩烤成脆脆的餅乾！ (Use Firebird flames to bake the pizzas into crispy crackers!)", "next": "3_A1", "effect": {"bravery": 1}, "is_bad": False},
            "B": {"text": "💦 拿出超級大水槍，用水把披薩沖走！ (Use a giant water gun to wash the pizzas away!)", "next": "BAD_END_WATER", "effect": {"creativity": -1}, "is_bad": True,
                  "bad_reason": "水槍的水倒流，導致火箭引擎短路，整艘飛船墜落地球！幸好火鷹俠有降落傘，但任務失敗了……\n(The water backfired and short-circuited the engine! The ship crashed. Mission failed...)"},
            "C": {"text": "🤤 張大嘴巴，一邊飛一邊把披薩全部吃掉！ (Open your mouth wide and eat all the pizzas while flying!)", "next": "3_A2", "effect": {"bravery": -1}, "is_bad": False}
        }
    },
    "3_A1": {
        "title_tc": "第 3 頁：外星人的 STEAM 扭蛋機", "title_en": "Page 3: The Alien STEAM Machine",
        "sfx": "🎰 叮噹！DING DONG!",
        "story_tc": "火鷹俠成功抵達外星基地，發現玩具被關在一個山一樣大的扭蛋機裡！門上有個數學邏輯鎖 (STEAM 挑戰)：",
        "story_en": "Firebird reaches the base and finds toys trapped in a giant capsule machine! The door has a math puzzle lock:",
        "effect": {"bravery": 1},
        "choices": {
            "A": {"text": "🧮 動腦筋算出正確的數學密碼開門 (STEAM)！ (Use your brain to calculate the correct math password!)", "next": "4_A1", "effect": {"creativity": 2, "bravery": 1}, "is_bad": False},
            "B": {"text": "🔨 拿出神奇充氣大錘子，把扭蛋機敲開！ (Take out a magic inflatable hammer to smash the machine open!)", "next": "BAD_END_HAMMER", "effect": {"bravery": 0}, "is_bad": True,
                  "bad_reason": "大錘敲下去，扭蛋機直接裂開，裡面的玩具全部散落宇宙，找不回來了！要重新來過……\n(The hammer smashed the machine. The toys scattered across space and are lost!)"},
            "C": {"text": "🤸‍♂️ 跳進扭蛋機裡，跟著玩具一起轉圈圈！ (Jump into the machine and spin around with the toys!)", "next": "4_A2", "effect": {"creativity": 1, "empathy": 1}, "is_bad": False}
        }
    },
    "3_A2": {
        "title_tc": "第 3 頁：好飽好飽，飛不動！", "title_en": "Page 3: Too Full to Fly!",
        "sfx": "🤢 嘔！BURP!",
        "story_tc": "你吃光了所有披薩，結果太飽，火箭都飛不動了！火鷹俠決定緊急降落到一個神秘星球，怎料……",
        "story_en": "You ate all the pizzas, now you're too full to fly! Firebird crash-lands on a mysterious planet...",
        "choices": {
            "A": {"text": "🌳 下去找東西吃，順便探索這個星球有沒有外星人！ (Go down to find food and explore for aliens!)", "next": "3_A2_EXPLORE", "effect": {"creativity": 1}, "is_bad": False},
            "B": {"text": "📡 用火箭剩餘的能量發送求救訊號，等待救援！ (Use the remaining energy to send an SOS signal!)", "next": "3_A2_SOS", "effect": {"bravery": 1}, "is_bad": False}
        }
    },
    "3_A2_EXPLORE": {
        "title_tc": "第 3b 頁：會跳舞的外星青蛙", "title_en": "Page 3b: Dancing Alien Frogs",
        "sfx": "🐸 呱呱！RIBBIT!",
        "images": ["https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Agalychnis_callidryas_%28a_red-eyed_tree_frog%29.jpg/800px-Agalychnis_callidryas_%28a_red-eyed_tree_frog%29.jpg"],
        "story_tc": "你發現一群戴着耳機的外星青蛙在跳街舞！牠們很熱情，邀請你一起玩！",
        "story_en": "You find a group of alien frogs wearing headphones and breakdancing! They invite you to join!",
        "choices": {
            "A": {"text": "🕺 接受邀請，一起跳舞，順便問牠們怎麼去糖果基地！ (Accept the invite, dance, and ask for directions!)", "next": "4_B1", "effect": {"empathy": 2, "creativity": 1}, "is_bad": False},
            "B": {"text": "🎤 搶走牠們的耳機，大聲唱歌嚇走牠們！ (Steal their headphones and sing loudly to scare them away!)", "next": "BAD_END_FROG", "effect": {"empathy": -2}, "is_bad": True,
                  "bad_reason": "你嚇到了青蛙，牠們全部跳走了，還帶走了你的火箭鑰匙！你被困在這個星球……任務失敗。\n(You scared the frogs. They jumped away and took your rocket key!)"}
        }
    },
    "3_A2_SOS": {
        "title_tc": "第 3c 頁：收到求救的海盜船", "title_en": "Page 3c: Pirate Ship Receives SOS",
        "sfx": "🏴‍☠️ 呵呵！HEHE!",
        "story_tc": "你的求救訊號被太空海盜收到了，他們來到，說可以幫你，但要你交出所有糖果！",
        "story_en": "Your SOS is picked up by space pirates! They offer to help, but demand all your candy!",
        "choices": {
            "A": {"text": "⚔️ 勇敢拒絕，跟海盜決鬥，搶走他們的飛船！ (Bravely refuse, duel the pirates, and take their ship!)", "next": "4_C1", "effect": {"bravery": 2}, "is_bad": False},
            "B": {"text": "🍬 交出糖果，換取他們帶你去糖果基地。 (Hand over the candy so they take you to the base.)", "next": "4_C2", "effect": {"bravery": -1}, "is_bad": False}
        }
    },

    # ===== 分支 B：膠鴨路線 =====
    "2_B": {
        "title_tc": "第 2 頁：膠鴨大暴走！", "title_en": "Page 2: Rubber Duck Rampage!",
        "sfx": "🦆 呱呱！QUACK!",
        "images": ["https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Rubber_duckies_SO.jpg/800px-Rubber_duckies_SO.jpg"],
        "story_tc": "超級膠鴨太重了，結果一屁股壓扁了外星人的果凍飛船！火鷹俠決定對外星人展現同理心：",
        "story_en": "The Super Rubber Duck is so heavy, it squashed the alien's jelly spaceship! Showing empathy, Firebird decides to:",
        "choices": {
            "A": {"text": "💨 用力拍動翅膀，颳起大風吹走外星人！ (Flap the wings hard to blow the aliens away!)", "next": "3_B1", "effect": {"bravery": 1}, "is_bad": False},
            "B": {"text": "🤝 幫外星人一起修理飛船，教他們機械知識 (STEAM)！ (Help the aliens fix the ship and teach them mechanics!)", "next": "3_B2", "effect": {"creativity": 2, "empathy": 1}, "is_bad": False},
            "C": {"text": "🧴 噴出香噴噴的草莓香水讓外星人打噴嚏！ (Spray sweet strawberry perfume to make them sneeze!)", "next": "BAD_END_SMELL", "effect": {"empathy": -1}, "is_bad": True,
                  "bad_reason": "香水令外星人狂打噴嚏，結果他們將你彈飛到銀河的另一邊，完全迷路了！任務失敗……\n(The sneeze blew you across the galaxy and you got completely lost!)"}
        }
    },
    "3_B1": {
        "title_tc": "第 3 頁：外星人發火了！", "title_en": "Page 3: Aliens Get Angry!",
        "sfx": "😡 吼！GRRR!",
        "story_tc": "你吹走了外星人，他們很生氣，召喚了一群機械蜜蜂來攻擊你！",
        "story_en": "The aliens are angry and summon robot bees to attack you!",
        "choices": {
            "A": {"text": "💪 硬接機械蜜蜂，用身體保護膠鴨！ (Block the robot bees to protect the rubber duck!)", "next": "4_B1", "effect": {"bravery": 2}, "is_bad": False},
            "B": {"text": "🍯 用蜂蜜引開蜜蜂，趁機逃走！ (Use honey to distract the bees and escape!)", "next": "4_B2", "effect": {"creativity": 1}, "is_bad": False}
        }
    },
    "3_B2": {
        "title_tc": "第 3 頁：齊心就事成！", "title_en": "Page 3: Teamwork Works!",
        "sfx": "🔧 叮叮！CLANK!",
        "story_tc": "你跟外星人一起修好飛船，他們非常感激，主動帶你去糖果基地！",
        "story_en": "You and the aliens fix the ship together. They are grateful and lead you to the candy base!",
        "choices": {
            "A": {"text": "🏃‍♂️ 跟他們走捷徑，快速到達！ (Follow their shortcut to arrive quickly!)", "next": "4_B1", "effect": {"bravery": 0}, "is_bad": False},
            "B": {"text": "🔍 沿途研究外星科技，收集數據 (STEAM)！ (Study alien tech and collect data along the way!)", "next": "4_B2", "effect": {"creativity": 2}, "is_bad": False}
        }
    },

    # ===== 分支 C：紙皮箱路線 =====
    "2_C": {
        "title_tc": "第 2 頁：紙皮箱裡的奇怪世界！", "title_en": "Page 2: The Weird Cardboard World!",
        "sfx": "📦 咻——！WHOOSH!",
        "story_tc": "紙皮箱飛到了外星花園，這裡有一隻戴着耳機的巨大青蛙在跳舞！火鷹俠決定展現尊重：",
        "story_en": "The box lands in an alien garden. A giant frog wearing headphones is dancing! Showing respect, Firebird decides to:",
        "choices": {
            "A": {"text": "🕺 尊重青蛙的喜好，跟青蛙一起跳街舞！ (Respect the frog's hobby and breakdance together!)", "next": "3_C1", "effect": {"empathy": 1, "creativity": 1}, "is_bad": False},
            "B": {"text": "🎤 搶走青蛙的麥克風，唱出超級難聽的歌嚇跑牠！ (Steal the mic and sing terribly to scare the frog!)", "next": "BAD_END_FROG2", "effect": {"empathy": -2}, "is_bad": True,
                  "bad_reason": "你搶走了麥克風，青蛙發火，用大腳板把你踩扁！雖然火鷹俠救了你，但任務失敗了……\n(You stole the mic. The frog got angry and stomped you flat!)"},
            "C": {"text": "🪰 變出一隻超級大蒼蠅，讓青蛙追着蒼蠅跑！ (Create a giant fly for the frog to chase!)", "next": "3_C2", "effect": {"creativity": 1}, "is_bad": False}
        }
    },
    "3_C1": {
        "title_tc": "第 3 頁：青蛙帶路", "title_en": "Page 3: Frog Guide",
        "sfx": "🐸 呱呱！",
        "story_tc": "青蛙很開心，帶你穿過秘密地道，直接去到糖果大王的皇宮！",
        "story_en": "The frog is happy and leads you through a secret tunnel straight to the Candy King's palace!",
        "choices": {
            "A": {"text": "👑 直接衝入皇宮，跟糖果大王談判！ (Rush into the palace and reason with the Candy King!)", "next": "4_C1", "effect": {"bravery": 1}, "is_bad": False},
            "B": {"text": "🕵️ 先在皇宮外圍偵查，收集情報！ (Scout outside the palace to gather intelligence!)", "next": "4_C2", "effect": {"creativity": 1}, "is_bad": False}
        }
    },
    "3_C2": {
        "title_tc": "第 3 頁：蒼蠅引發大混亂", "title_en": "Page 3: Fly Chaos",
        "sfx": "🪰 嗡嗡！BUZZ!",
        "story_tc": "大蒼蠅引來了許多青蛙追趕，場面一片混亂！你趁機偷走了一架外星飛碟！",
        "story_en": "The giant fly attracts many frogs, causing chaos! You steal an alien spaceship!",
        "choices": {
            "A": {"text": "🚀 駕駛飛碟直接去糖果基地！ (Pilot the spaceship straight to the candy base!)", "next": "4_A1", "effect": {"bravery": 1}, "is_bad": False},
            "B": {"text": "📞 用飛碟的通訊器聯絡火鷹俠，叫他來會合！ (Use the communicator to call Firebird for backup!)", "next": "4_B1", "effect": {"empathy": 1}, "is_bad": False}
        }
    },

    # ===== 第 4 頁匯合 =====
    "4_A1": {
        "title_tc": "第 4 頁：解鎖機關！", "title_en": "Page 4: Lock Solved!",
        "sfx": "🎉 叮！DING!",
        "story_tc": "你成功開啟機關，所有玩具飛出來了！但糖果大王突然出現！",
        "story_en": "You crack the code and all toys fly out! But the Candy King appears!",
        "choices": {
            "A": {"text": "🤝 主動跟糖果大王握手，邀請他一起玩！ (Shake hands with the Candy King and invite him to play!)", "next": "5_A1", "effect": {"empathy": 2}, "is_bad": False},
            "B": {"text": "⚔️ 擺出戰鬥姿態，逼他歸還玩具！ (Take a combat stance and force him to return the toys!)", "next": "5_B1", "effect": {"bravery": 2}, "is_bad": False}
        }
    },
    "4_A2": {
        "title_tc": "第 4 頁：轉到頭暈眼花！", "title_en": "Page 4: Dizzy Spinning!",
        "sfx": "🌀 轉轉！SPIN!",
        "story_tc": "你跟玩具轉了很久，頭暈眼花，但發現了一個秘密出口！",
        "story_en": "You spun with the toys for so long, you found a secret exit!",
        "choices": {
            "A": {"text": "🚪 穿過出口，直接去到糖果大王的寢室！ (Go through the exit straight to the Candy King's bedroom!)", "next": "5_A2", "effect": {"bravery": 0}, "is_bad": False},
            "B": {"text": "📦 拿走幾個玩具，用紙皮箱砌成武器！ (Take some toys and build cardboard weapons!)", "next": "5_B2", "effect": {"creativity": 2}, "is_bad": False}
        }
    },
    "4_B1": {
        "title_tc": "第 4 頁：外星人朋友帶路", "title_en": "Page 4: Alien Friends Lead the Way",
        "sfx": "🤝 感謝！THANKS!",
        "story_tc": "外星人帶你到糖果基地的後門，裡面有個巨型糖果噴泉！",
        "story_en": "The aliens lead you to the back door of the candy base, where there's a giant candy fountain!",
        "choices": {
            "A": {"text": "🍭 品嚐糖果噴泉，順便收集情報！ (Taste the candy fountain and gather information!)", "next": "5_A1", "effect": {"creativity": 1}, "is_bad": False},
            "B": {"text": "🔧 關閉噴泉，令基地停電，趁黑潛入！ (Turn off the fountain to cause a blackout and sneak in!)", "next": "5_B1", "effect": {"bravery": 1, "creativity": 1}, "is_bad": False}
        }
    },
    "4_B2": {
        "title_tc": "第 4 頁：STEAM 數據收集", "title_en": "Page 4: STEAM Data Collection",
        "sfx": "📊 數據！DATA!",
        "story_tc": "你記錄了外星科技的數據，發現他們的防禦系統有個漏洞！",
        "story_en": "You recorded alien tech data and found a flaw in their defense system!",
        "choices": {
            "A": {"text": "💻 利用漏洞入侵系統，直接打開所有閘門！ (Hack the system using the flaw to open all doors!)", "next": "5_A2", "effect": {"creativity": 2}, "is_bad": False},
            "B": {"text": "📢 將漏洞情報廣播出去，引發外星人內亂！ (Broadcast the flaw to cause chaos among the aliens!)", "next": "5_B2", "effect": {"bravery": 1}, "is_bad": False}
        }
    },
    "4_C1": {
        "title_tc": "第 4 頁：海盜決鬥！", "title_en": "Page 4: Pirate Duel!",
        "sfx": "⚔️ 鏗鏘！CLANG!",
        "story_tc": "你跟對手決鬥贏了，搶到了去糖果大王皇宮的地圖！",
        "story_en": "You duel the leader and win, grabbing his star map!",
        "choices": {
            "A": {"text": "🗺️ 跟着地圖去糖果基地的秘密入口！ (Follow the map to the candy base's secret entrance!)", "next": "5_A1", "effect": {"bravery": 0}, "is_bad": False},
            "B": {"text": "📡 用地圖訊號引導火鷹俠來幫忙！ (Use the map to signal Firebird for help!)", "next": "5_B1", "effect": {"empathy": 1}, "is_bad": False}
        }
    },
    "4_C2": {
        "title_tc": "第 4 頁：情報交換", "title_en": "Page 4: Intel Exchange",
        "sfx": "🏴‍☠️ 嘻嘻！HEHE!",
        "story_tc": "你用糖果換取了情報，得知糖果大王最害怕的弱點！",
        "story_en": "You traded candy for intel, learning the King's weakness!",
        "choices": {
            "A": {"text": "🤫 利用弱點，扮成糖果大王的樣子潛入！ (Use the weakness and disguise yourself as the Candy King!)", "next": "5_A2", "effect": {"creativity": 2}, "is_bad": False},
            "B": {"text": "💥 直接引爆炸彈，炸開大門！ (Detonate the bomb to blow open the door!)", "next": "5_B2", "effect": {"bravery": 2}, "is_bad": False}
        }
    },

    # ===== 第 5 頁 (決戰前夕) =====
    "5_A1": {
        "title_tc": "第 5 頁：糖果大王的心聲", "title_en": "Page 5: Confession",
        "sfx": "😢 嗚嗚！WAAAH!",
        "story_tc": "糖果大王哭着說，他偷玩具只是因為太寂寞，沒有人陪他玩。火鷹俠決定：",
        "story_en": "The Candy King cries, saying he stole toys because he's lonely. Firebird decides to:",
        "choices": {
            "A": {"text": "🫂 擁抱他，告訴他朋友可以到處找，不用偷東西！ (Hug him and tell him making friends doesn't require stealing!)", "next": "6_LEADER", "effect": {"empathy": 3}, "is_bad": False},
            "B": {"text": "🎮 送他一部遊戲機，告訴他可以在虛擬世界交朋友！ (Give him a console to make friends in the virtual world!)", "next": "6_INVENTOR", "effect": {"creativity": 3}, "is_bad": False}
        }
    },
    "5_A2": {
        "title_tc": "第 5 頁：寢室裡的秘密", "title_en": "Page 5: Secret in the Bedroom",
        "sfx": "🛏️ 呼呼！SNORE!",
        "story_tc": "你潛入寢室，發現糖果大王在做夢，夢話中提到他很掛念地球的朋友。",
        "story_en": "You sneak into the bedroom and find the King dreaming about missing his Earth friends.",
        "choices": {
            "A": {"text": "📸 拍下他的夢話，然後叫醒他，跟他講道理！ (Record his sleep talk, wake him up, and reason with him!)", "next": "6_CARER", "effect": {"empathy": 2}, "is_bad": False},
            "B": {"text": "🌙 用魔法將他的夢變成現實，讓他在夢中見到朋友！ (Use magic to make his dream real so he sees his friends!)", "next": "6_EMPATHY", "effect": {"empathy": 3}, "is_bad": False}
        }
    },
    "5_B1": {
        "title_tc": "第 5 頁：對決時刻！", "title_en": "Page 5: Showdown!",
        "sfx": "⚡ 啪！POW!",
        "story_tc": "火鷹俠跟糖果大王展開激戰，你趁機偷走玩具，但大王用糖果攻擊你！",
        "story_en": "Firebird fights the Candy King, and you steal the toys, but the King attacks with candy!",
        "choices": {
            "A": {"text": "🍬 用糖果反擊，做一個「超級太妃糖」困住他！ (Counterattack with candy and trap him in Super Toffee!)", "next": "6_HERO", "effect": {"bravery": 2}, "is_bad": False},
            "B": {"text": "🏃‍♂️ 拿着玩具馬上逃走，不理大王！ (Grab the toys and run away immediately!)", "next": "6_DEFAULT", "effect": {"bravery": 0}, "is_bad": False}
        }
    },
    "5_B2": {
        "title_tc": "第 5 頁：武器對決", "title_en": "Page 5: Weapon Duel",
        "sfx": "🗡️ 鏘！SWISH!",
        "story_tc": "你用紙皮箱武器跟糖果大王的糖果劍對打，打得難分難解！",
        "story_en": "You duel the King with your cardboard weapon against his candy sword!",
        "choices": {
            "A": {"text": "🎨 用創意將武器變成糖果，跟他鬥甜！ (Use creativity to turn weapons into candy and fight!)", "next": "6_CREATIVE", "effect": {"creativity": 3}, "is_bad": False},
            "B": {"text": "💪 用蠻力打斷他的劍，贏了！ (Use strength to break his sword and win the duel!)", "next": "6_BRAVE", "effect": {"bravery": 3}, "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_WATER": {
        "title_tc": "💥 任務失敗：水槍回彈", "title_en": "Mission Failed: Water Backfire",
        "sfx": "💥 BOOM!", "is_bad_ending": True,
        "story_tc": "水槍倒流導致火箭爆炸，幸好火鷹俠保護了你。不過玩具還在外星人手上，你要返回上一頁重新選擇！",
        "story_en": "The water backfired and the rocket exploded. Luckily Firebird saved you. But the toys are still gone. Go back and try again!"
    },
    "BAD_END_HAMMER": {
        "title_tc": "🔨 任務失敗：打爛扭蛋機", "title_en": "Mission Failed: Smashed Machine",
        "sfx": "💔 CRASH!", "is_bad_ending": True,
        "story_tc": "大錘打爛了扭蛋機，玩具散落宇宙，找不回來。你只好回去再想辦法。",
        "story_en": "The hammer smashed the machine and toys scattered across space. You must go back and think again."
    },
    "BAD_END_FROG": {
        "title_tc": "🐸 任務失敗：青蛙報復", "title_en": "Mission Failed: Frog Revenge",
        "sfx": "😤 呱！", "is_bad_ending": True,
        "story_tc": "你激怒了青蛙，牠用大腳板踢走了你的飛船鑰匙，你被困在外星，任務失敗。",
        "story_en": "You angered the frog, he kicked away your ship key, and you're stranded. Mission failed."
    },
    "BAD_END_SMELL": {
        "title_tc": "🧴 任務失敗：香水噴嚏", "title_en": "Mission Failed: Perfume Sneeze",
        "sfx": "🤧 ACHOO!", "is_bad_ending": True,
        "story_tc": "香水令外星人狂打噴嚏，將你彈飛到銀河另一端，完全迷失方向。任務失敗。",
        "story_en": "The perfume made the aliens sneeze so hard they blew you across the galaxy. Mission failed."
    },
    "BAD_END_FROG2": {
        "title_tc": "🎤 任務失敗：青蛙踩扁", "title_en": "Mission Failed: Frog Stomp",
        "sfx": "🦶 STOMP!", "is_bad_ending": True,
        "story_tc": "你搶走了麥克風，青蛙發火一腳把你踩扁，火鷹俠救了你但任務失敗了。",
        "story_en": "You stole the mic, the frog stomped you flat. Firebird saved you but mission failed."
    }
}

# 備用故事佔位符
STORY_2_SCENES = STORY_1_SCENES  
STORY_3_SCENES = STORY_1_SCENES

STORIES = {
    "Story1": {"name_tc": "📕 火鷹俠 1：玩具星球大冒險 (Toy Planet)", "nodes": STORY_1_SCENES},
    "Story2": {"name_tc": "📘 火鷹俠 2：恐龍樂園大暴走 (Dinosaur Park)", "nodes": STORY_2_SCENES},
    "Story3": {"name_tc": "📗 火鷹俠 3：深海龍宮大拯救 (Deep Sea Rescue)", "nodes": STORY_3_SCENES}
}
