# ==============================================================================
# 📕 火鷹俠 1：玩具星球大冒險 (Toy Planet)
# ==============================================================================

STORY_INFO = {
    "id": "Story1",
    "name_tc": "📕 火鷹俠 1：玩具星球大冒險",
    "name_en": "Firebird 1: Toy Planet Adventure"
}

SCENES = {
    "1_START": {
        "title_tc": "第 1 頁：玩具失竊大危機！", "title_en": "Page 1: The Great Toy Crisis!",
        "sfx": "🚨 嗚哇！WEE WOO!",
        "story_tc": "大事不好了！「糖果外星人」偷走了全城小朋友最喜愛的玩具！火鷹俠必須前往外星基地奪回玩具，展現勇氣與承擔，他決定：",
        "story_en": "Oh no! The 'Candy Aliens' stole all the kids' favorite toys! Firebird must show courage and commitment to get them back. He decides to:",
        "choices": {
            "A": {"text": "🚀 坐上「超級彩虹推進火箭」飛上太空！ (Ride the Super Rainbow Rocket into space!)", "next": "2_A", "effect": {"bravery": 1}, "is_bad": False},
            "B": {"text": "🦆 召喚一隻跟大廈一樣高的「超級黃色橡皮鴨」！ (Summon a building-sized Super Rubber Duck!)", "next": "2_B", "effect": {"creativity": 1}, "is_bad": False},
            "C": {"text": "📦 跳進神奇紙皮箱，動手改造成宇宙飛船 (STEAM)！ (Jump into a magic cardboard box and build a spaceship!)", "next": "2_C", "effect": {"creativity": 2}, "is_bad": False}
        }
    },
    "2_A": {
        "title_tc": "第 2 頁：會飛的披薩隕石！", "title_en": "Page 2: Flying Pizza Meteors!",
        "sfx": "🍕 砰！BAM!",
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
        "title_tc": "第 3 頁：肚子太飽，飛不動！", "title_en": "Page 3: Too Full to Fly!",
        "sfx": "🤢 嘔！BURP!",
        "story_tc": "你吃光了所有披薩，結果太飽，火箭都飛不動了！火鷹俠決定緊急降落到一個神秘星球，怎料……",
        "story_en": "You ate all the pizzas, now you're too full to fly! Firebird crash-lands on a mysterious planet...",
        "choices": {
            "A": {"text": "🌳 下去找東西吃，順便探索這個星球有沒有外星人！ (Go down to find food and explore for aliens!)", "next": "4_A1", "effect": {"creativity": 1}, "is_bad": False},
            "B": {"text": "📡 用火箭剩餘的能量發送求救訊號，等待救援！ (Use the remaining energy to send an SOS signal!)", "next": "4_A2", "effect": {"bravery": 1}, "is_bad": False}
        }
    },
    "2_B": {
        "title_tc": "第 2 頁：膠鴨大暴走！", "title_en": "Page 2: Rubber Duck Rampage!",
        "sfx": "🦆 呱呱！QUACK!",
        "story_tc": "超級膠鴨太重了，結果一屁股壓扁了外星人的果凍飛船！火鷹俠決定對外星人展現同理心：",
        "story_en": "The Super Rubber Duck is so heavy, it squashed the alien's jelly spaceship! Showing empathy, Firebird decides to:",
        "choices": {
            "A": {"text": "💨 用力拍動翅膀，颳起大風吹走外星人！ (Flap the wings hard to blow the aliens away!)", "next": "4_A1", "effect": {"bravery": 1}, "is_bad": False},
            "B": {"text": "🤝 幫外星人一起修理飛船，教他們機械知識 (STEAM)！ (Help the aliens fix the ship and teach them mechanics!)", "next": "4_A2", "effect": {"creativity": 2, "empathy": 1}, "is_bad": False},
            "C": {"text": "🧴 噴出香噴噴的草莓香水讓外星人打噴嚏！ (Spray sweet strawberry perfume to make them sneeze!)", "next": "BAD_END_SMELL", "effect": {"empathy": -1}, "is_bad": True,
                  "bad_reason": "香水令外星人狂打噴嚏，結果他們將你彈飛到銀河的另一邊，完全迷路了！任務失敗……\n(The sneeze blew you across the galaxy and you got completely lost!)"}
        }
    },
    "2_C": {
        "title_tc": "第 2 頁：紙皮箱裡的奇怪世界！", "title_en": "Page 2: The Weird Cardboard World!",
        "sfx": "📦 咻——！WHOOSH!",
        "story_tc": "紙皮箱飛到了外星花園，這裡有一隻戴着耳機的巨大青蛙在跳舞！火鷹俠決定展現尊重：",
        "story_en": "The box lands in an alien garden. A giant frog wearing headphones is dancing! Showing respect, Firebird decides to:",
        "choices": {
            "A": {"text": "🕺 尊重青蛙的喜好，跟青蛙一起跳街舞！ (Respect the frog's hobby and breakdance together!)", "next": "4_A1", "effect": {"empathy": 1, "creativity": 1}, "is_bad": False},
            "B": {"text": "🎤 搶走青蛙的麥克風，唱出超級難聽的歌嚇跑牠！ (Steal the mic and sing terribly to scare the frog!)", "next": "BAD_END_FROG2", "effect": {"empathy": -2}, "is_bad": True,
                  "bad_reason": "你搶走了麥克風，青蛙發火，用大腳板把你踩扁！雖然火鷹俠救了你，但任務失敗了……\n(You stole the mic. The frog got angry and stomped you flat!)"},
            "C": {"text": "🪰 變出一隻超級大蒼蠅，讓青蛙追着蒼蠅跑！ (Create a giant fly for the frog to chase!)", "next": "4_A2", "effect": {"creativity": 1}, "is_bad": False}
        }
    },
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
            "A": {"text": "🚪 穿過出口，直接去到糖果大王的寢室！ (Go through the exit straight to the Candy King's bedroom!)", "next": "5_A1", "effect": {"bravery": 0}, "is_bad": False},
            "B": {"text": "📦 拿走幾個玩具，用紙皮箱砌成武器！ (Take some toys and build cardboard weapons!)", "next": "5_B1", "effect": {"creativity": 2}, "is_bad": False}
        }
    },
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
    "BAD_END_WATER": {"title_tc": "💥 任務失敗：水槍回彈", "title_en": "Mission Failed: Water Backfire", "sfx": "💥 BOOM!", "is_bad_ending": True, "story_tc": "水槍倒流導致火箭爆炸，幸好火鷹俠保護了你。你要返回上一頁重新選擇！", "story_en": "Water backfired and rocket exploded. Go back and try again!"},
    "BAD_END_HAMMER": {"title_tc": "🔨 任務失敗：打爛扭蛋機", "title_en": "Mission Failed: Smashed Machine", "sfx": "💔 CRASH!", "is_bad_ending": True, "story_tc": "大錘打爛了扭蛋機，玩具散落宇宙。你只好回去再想辦法。", "story_en": "Hammer smashed the machine. Think again!"},
    "BAD_END_SMELL": {"title_tc": "🧴 任務失敗：香水噴嚏", "title_en": "Mission Failed: Perfume Sneeze", "sfx": "🤧 ACHOO!", "is_bad_ending": True, "story_tc": "香水令外星人狂打噴嚏，將你彈飛到銀河另一端！任務失敗。", "story_en": "Sneeze blew you across galaxy!"},
    "BAD_END_FROG2": {"title_tc": "🎤 任務失敗：青蛙踩扁", "title_en": "Mission Failed: Frog Stomp", "sfx": "🦶 STOMP!", "is_bad_ending": True, "story_tc": "你搶走了麥克風，青蛙發火一腳把你踩扁！任務失敗。", "story_en": "Frog stomped you flat!"}
}
