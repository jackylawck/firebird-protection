# ==============================================================================
# 📙 火鷹俠 4：恐龍化石之謎 (Dinosaur Fossil Mystery)
# 書面語版本 | 適合 6 歲升小學兒童
# ==============================================================================

STORY_INFO = {
    "id": "Story4",
    "name_tc": "📙 火鷹俠 4：恐龍化石之謎",
    "name_en": "Firebird 4: Dinosaur Fossil Mystery"
}

SCENES = {
    # ===================== 起始 =====================
    "1_START": {
        "title_tc": "第 1 頁：珍貴化石不見了！", "title_en": "Page 1: The Precious Fossil is Missing!",
        "sfx": "🦴 什麼？！WHAT?!",
        "story_tc": "博物館剛出土的「恐龍之王」化石，竟然在展覽前夜離奇消失！館長急得大哭。火鷹俠承擔責任 (Commitment)，決心找出真相。他決定：",
        "story_en": "The newly unearthed 'King Dinosaur' fossil disappeared overnight from the museum! The curator is in tears. Firebird shows commitment to find the truth. He decides to:",
        "choices": {
            "A": {"text": "🔦 帶上紅外線探測器，搜索博物館的每個角落！ (Take an infrared detector to search every corner!)", "next": "2_A", "effect": {"creativity": 1}, "is_bad": False},
            "B": {"text": "🕵️ 扮成清潔工，暗中觀察可疑人物！ (Disguise as a cleaner to spy on suspicious people!)", "next": "2_B", "effect": {"empathy": 1}, "is_bad": False},
            "C": {"text": "📡 用衛星圖像分析博物館周邊的最近移動痕跡！ (Use satellite images to analyze recent movements!)", "next": "2_C", "effect": {"bravery": 1}, "is_bad": False}
        }
    },

    # ================= 分支 A：科技搜查 =================
    "2_A": {
        "title_tc": "第 2 頁：發現奇怪腳印！", "title_en": "Page 2: Strange Footprints Found!",
        "sfx": "👣 腳印！PRINTS!",
        "story_tc": "紅外線探測器在展覽廳後門發現了一串發光的腳印，腳印比人類大很多，形狀像鳥爪。火鷹俠運用科學知識推測：",
        "story_en": "The infrared detector finds glowing footprints at the back door, huge and bird-like. Firebird uses science to infer:",
        "choices": {
            "A": {"text": "🔬 用3D掃描複製腳印，與恐龍腳印資料庫比對！ (3D-scan the footprints and compare with dinosaur databases!)", "next": "3_A1", "effect": {"creativity": 2}, "is_bad": False},
            "B": {"text": "🏃‍♂️ 立刻順着腳印追出去，看看通向哪裏！ (Follow the footprints immediately to see where they lead!)", "next": "3_A2", "effect": {"bravery": 1}, "is_bad": False},
            "C": {"text": "📸 拍攝腳印照片，發布到網上尋找線索！ (Post the photo online to seek clues!)", "next": "BAD_END_LEAK", "effect": {"creativity": -1}, "is_bad": True,
                  "bad_reason": "照片在網上瘋傳，小偷警覺並轉移了化石，線索中斷！任務失敗。\n(The photo went viral, the thief moved the fossil. Trail gone.)"}
        }
    },
    "3_A1": {
        "title_tc": "第 3 頁：比對結果——翼龍腳印！", "title_en": "Page 3: Match Found — Pterodactyl Prints!",
        "sfx": "🦅 叮！DING!",
        "story_tc": "數據庫顯示，腳印屬於一種罕見的夜行性翼龍，牠們在博物館附近的山洞築巢。你決定前往山洞探索。",
        "story_en": "The database shows the prints belong to a rare nocturnal Pterodactyl nesting in nearby caves. You head to the caves.",
        "choices": {
            "A": {"text": "🧗 帶上攀岩工具，爬進山洞深處！ (Take climbing gear to go deep into the cave!)", "next": "4_A1", "effect": {"bravery": 1}, "is_bad": False},
            "B": {"text": "🤖 派出一台小型無人機先進去偵查！ (Deploy a drone for reconnaissance first!)", "next": "4_A2", "effect": {"creativity": 1}, "is_bad": False}
        }
    },
    "3_A2": {
        "title_tc": "第 3 頁：追到森林邊緣", "title_en": "Page 3: Followed to the Forest Edge",
        "sfx": "🌳 沙沙！RUSTLE!",
        "story_tc": "你追着腳印來到一片黑暗的森林，腳印在這裏消失了。你聽到一陣奇怪的聲音，好像有人在挖掘。",
        "story_en": "You follow the prints into a dark forest, where they disappear. You hear strange digging sounds.",
        "choices": {
            "A": {"text": "🔦 打開手電筒，朝聲音來源走去！ (Turn on a flashlight and head to the sound!)", "next": "4_A1", "effect": {"bravery": 1}, "is_bad": False},
            "B": {"text": "🦉 模仿貓頭鷹叫聲，試探對方反應！ (Imitate an owl call to test a response!)", "next": "4_A2", "effect": {"creativity": 1}, "is_bad": False},
            "C": {"text": "📡 用手機定位發送位置給火鷹俠，要求支援！ (Send location to Firebird for backup!)", "next": "BAD_END_SIGNAL", "effect": {"bravery": -1}, "is_bad": True,
                  "bad_reason": "信號被干擾，你暴露了位置，被人從背後擊暈！火鷹俠趕到時，化石已被運走。\n(Your signal was jammed, and you were knocked out.)"}
        }
    },

    # ================= 分支 B：卧底觀察 =================
    "2_B": {
        "title_tc": "第 2 頁：清潔工發現可疑人物", "title_en": "Page 2: Cleaner Spots a Suspicious Figure",
        "sfx": "🧹 掃掃！SWEEP!",
        "story_tc": "你扮成清潔工，在展廳打掃時，發現一個穿黑斗篷的人鬼鬼祟祟地在化石展櫃附近徘徊。你決定：",
        "story_en": "Disguised as a cleaner, you spot a cloaked figure lurking near the fossil display. You decide to:",
        "choices": {
            "A": {"text": "🗣️ 假裝問路，試探對方的身份！ (Pretend to ask for directions to test their identity!)", "next": "3_B1", "effect": {"empathy": 1}, "is_bad": False},
            "B": {"text": "📸 偷偷拍下對方的照片，留作證據！ (Secretly take a photo as evidence!)", "next": "3_B2", "effect": {"creativity": 1}, "is_bad": False},
            "C": {"text": "🚨 直接呼叫警衛，把可疑人物抓住！ (Call the guards immediately to arrest them!)", "next": "BAD_END_ALARM", "effect": {"bravery": -1}, "is_bad": True,
                  "bad_reason": "警衛衝進來時，可疑人物已經逃走，還打碎了一個展櫃。你被館長責備，調查暫停。\n(Guards scared the suspect away and broke a display.)"}
        }
    },
    "3_B1": {
        "title_tc": "第 3 頁：交談中的破綻", "title_en": "Page 3: A Slip in Conversation",
        "sfx": "🗨️ 嗯？HMM?",
        "story_tc": "你跟黑斗篷對話，他自稱是古生物學家，卻說不出一種常見恐龍的名字。你懷疑他在說謊，決定跟蹤他。",
        "story_en": "The cloaked figure claims to be a paleontologist, but can't name a common dinosaur. You suspect a lie and decide to follow.",
        "choices": {
            "A": {"text": "🕵️ 不動聲色地跟蹤他到博物館外！ (Stealthily follow him outside the museum!)", "next": "4_B1", "effect": {"bravery": 1}, "is_bad": False},
            "B": {"text": "📱 用手機錄下對話，分析他的口音和用詞！ (Record the conversation to analyze accent and wording!)", "next": "4_B2", "effect": {"creativity": 1}, "is_bad": False}
        }
    },
    "3_B2": {
        "title_tc": "第 3 頁：照片裡的細節", "title_en": "Page 3: Details in the Photo",
        "sfx": "📷 咔嚓！CLICK!",
        "story_tc": "你拍到的照片中，黑斗篷的袖口露出一張地圖的邊角，上面標記着一個位置——「霸王龍峽谷」。你決定前往探險。",
        "story_en": "The photo reveals a map edge in his sleeve, marked 'T-Rex Canyon'. You decide to go there.",
        "choices": {
            "A": {"text": "🗺️ 帶上地圖和指南針，徒步前往峽谷！ (Take map and compass to hike to the canyon!)", "next": "4_B1", "effect": {"bravery": 1}, "is_bad": False},
            "B": {"text": "🚁 租一架直升機，快速飛到峽谷上空偵察！ (Rent a helicopter for an aerial reconnaissance!)", "next": "4_B2", "effect": {"creativity": 1}, "is_bad": False}
        }
    },

    # ================= 分支 C：衛星分析 =================
    "2_C": {
        "title_tc": "第 2 頁：衛星拍到可疑車輛", "title_en": "Page 2: Satellite Captures Suspicious Vehicle",
        "sfx": "🛰️ 衛星！SATELLITE!",
        "story_tc": "衛星圖像顯示，昨晚午夜有一輛沒有車牌的貨車停在博物館後門，之後向東北方向駛去。你鎖定目標區域。",
        "story_en": "Satellite images show an unmarked van parked at the back door at midnight, then heading northeast. You lock on the target area.",
        "choices": {
            "A": {"text": "🚗 開車追蹤貨車的痕跡，沿途查看監控！ (Drive to track the van, checking CCTV along the way!)", "next": "3_C1", "effect": {"bravery": 1}, "is_bad": False},
            "B": {"text": "💻 分析貨車的輪胎壓痕，推算其載重和去向！ (Analyze tire tracks to estimate load and direction!)", "next": "3_C2", "effect": {"creativity": 2}, "is_bad": False},
            "C": {"text": "📢 在社交媒體發布懸賞，尋找目擊者！ (Post a reward on social media for witnesses!)", "next": "BAD_END_HOAX", "effect": {"creativity": -1}, "is_bad": True,
                  "bad_reason": "懸賞引來大量假消息，浪費了寶貴時間，真正的線索已經消失。\n(Fake tips wasted time. The real trail went cold.)"}
        }
    },
    "3_C1": {
        "title_tc": "第 3 頁：貨車進入廢棄礦場", "title_en": "Page 3: Van Entered an Abandoned Mine",
        "sfx": "⛏️ 礦場！MINE!",
        "story_tc": "你追蹤貨車來到一個廢棄的礦場，礦場入口有新鮮的車胎痕跡。你決定潛入調查。",
        "story_en": "You track the van to an abandoned mine with fresh tire marks. You decide to infiltrate.",
        "choices": {
            "A": {"text": "🔦 帶上手電筒和繩索，小心進入礦洞！ (Enter the mine with flashlight and rope!)", "next": "4_C1", "effect": {"bravery": 1}, "is_bad": False},
            "B": {"text": "🤖 放出一台小型機器人先行探路！ (Deploy a robot to scout ahead!)", "next": "4_C2", "effect": {"creativity": 1}, "is_bad": False}
        }
    },
    "3_C2": {
        "title_tc": "第 3 頁：輪胎印指向秘密倉庫", "title_en": "Page 3: Tire Marks Lead to a Secret Warehouse",
        "sfx": "🏚️ 倉庫！WAREHOUSE!",
        "story_tc": "數據分析顯示，貨車的載重與一塊大型化石相符，並推算出藏匿地點——郊區一個廢棄倉庫。你前往偵查。",
        "story_en": "Data analysis matches the load to a large fossil and pinpoints a secret warehouse in the suburbs. You go there.",
        "choices": {
            "A": {"text": "🕵️ 從通風管道潛入倉庫，尋找化石！ (Sneak in through the ventilation ducts!)", "next": "4_C1", "effect": {"creativity": 1}, "is_bad": False},
            "B": {"text": "📦 假扮送貨員，敲門進入倉庫！ (Disguise as a delivery person to enter!)", "next": "4_C2", "effect": {"empathy": 1}, "is_bad": False}
        }
    },

    # ================= 第四頁：匯合點（找到化石和反派） =================
    "4_A1": {
        "title_tc": "第 4 頁：洞穴中的化石寶藏", "title_en": "Page 4: Fossil Treasure in the Cave",
        "sfx": "✨ 閃閃！SPARKLE!",
        "story_tc": "你深入洞穴，赫然發現「恐龍之王」化石被整齊地擺放在一個石台上，旁邊站着一個戴眼鏡的老人，自稱是「化石收藏家」。",
        "story_en": "Deep in the cave, you find the 'King Dinosaur' fossil neatly placed on a stone platform. An old man in glasses claims to be a 'fossil collector'.",
        "choices": {
            "A": {"text": "🤝 跟他對話，了解他偷化石的真正動機！ (Talk to him to understand his real motive!)", "next": "5_A1", "effect": {"empathy": 1}, "is_bad": False},
            "B": {"text": "📡 悄悄用通訊器通知火鷹俠，準備包圍！ (Quietly notify Firebird via radio to prepare an ambush!)", "next": "5_A2", "effect": {"bravery": 1}, "is_bad": False},
            "C": {"text": "💪 直接衝過去搶回化石！ (Charge in and grab the fossil directly!)", "next": "BAD_END_GRAB", "effect": {"bravery": -1}, "is_bad": True,
                  "bad_reason": "老人觸發了陷阱，你被網住，化石被轉移。火鷹俠後來救了你，但化石已不見蹤影。\n(You triggered a trap and the fossil was moved.)"}
        }
    },
    "4_A2": {
        "title_tc": "第 4 頁：無人機發現秘密實驗室", "title_en": "Page 4: Drone Finds a Secret Lab",
        "sfx": "🔬 實驗室！LAB!",
        "story_tc": "無人機拍攝到一個地下實驗室，裡面有多個化石展櫃，還有一個正在進行DNA提取的設備。你決定潛入。",
        "story_en": "The drone reveals an underground lab with fossil cabinets and DNA extraction equipment. You decide to enter.",
        "choices": {
            "A": {"text": "🔧 從電力管道爬進去，關閉電源引發混亂！ (Crawl through power conduits to cut the power!)", "next": "5_A1", "effect": {"creativity": 1}, "is_bad": False},
            "B": {"text": "👨‍🔬 扮成研究員，混入實驗室內部！ (Disguise as a researcher to blend in!)", "next": "5_A2", "effect": {"empathy": 1}, "is_bad": False}
        }
    },

    "4_B1": {
        "title_tc": "第 4 頁：峽谷裡的挖掘現場", "title_en": "Page 4: Dig Site in the Canyon",
        "sfx": "🔨 敲打！TAP TAP!",
        "story_tc": "你到達霸王龍峽谷，發現一群人正在用工具挖掘，旁邊停着那輛無牌貨車。你看到化石被包裹在布中，準備裝車。",
        "story_en": "You arrive at T-Rex Canyon and find a team digging with tools. The van is there, and the fossil is wrapped and ready to be loaded.",
        "choices": {
            "A": {"text": "📷 拍下證據，然後報警！ (Take photos as evidence, then call the police!)", "next": "5_A1", "effect": {"bravery": 0}, "is_bad": False},
            "B": {"text": "💥 製造干擾（例如放煙火），趁亂搶走化石！ (Create a distraction with fireworks to grab the fossil!)", "next": "5_A2", "effect": {"creativity": 1}, "is_bad": False},
            "C": {"text": "📞 聯繫火鷹俠，讓他從空中攔截！ (Call Firebird for an aerial interception!)", "next": "BAD_END_INTERCEPT", "effect": {"bravery": -1}, "is_bad": True,
                  "bad_reason": "信號延遲，火鷹俠來遲了，貨車已經離開。任務失敗。\n(Signal delayed, the van escaped.)"}
        }
    },
    "4_B2": {
        "title_tc": "第 4 頁：直升機發現地下通道", "title_en": "Page 4: Helicopter Spots Underground Tunnel",
        "sfx": "🚁 螺旋槳！ROTOR!",
        "story_tc": "直升機飛過峽谷，熱成像顯示地下有一條通往山腹的通道，通道內有大量金屬物體——可能是化石支架。",
        "story_en": "Thermal imaging shows an underground tunnel with many metal objects — likely fossil supports.",
        "choices": {
            "A": {"text": "🪂 從直升機跳傘降落，在通道入口降落！ (Parachute down to the tunnel entrance!)", "next": "5_A1", "effect": {"bravery": 1}, "is_bad": False},
            "B": {"text": "📡 用偵測器掃描通道結構，繪製立體地圖！ (Scan the tunnel to make a 3D map!)", "next": "5_A2", "effect": {"creativity": 1}, "is_bad": False}
        }
    },

    "4_C1": {
        "title_tc": "第 4 頁：礦洞裡的恐龍墓園", "title_en": "Page 4: Dinosaur Graveyard in the Mine",
        "sfx": "🦴 骷髏！SKULL!",
        "story_tc": "礦洞深處是一個巨大的地下恐龍墓園，無數化石堆積如山。你找到了「恐龍之王」的頭骨，卻被一群人包圍了。",
        "story_en": "Deep in the mine is a huge dinosaur graveyard. You find the King's skull but are surrounded by a group.",
        "choices": {
            "A": {"text": "📢 高舉雙手，展示你並無惡意，想與他們溝通！ (Raise hands to show you mean no harm, and talk!)", "next": "5_A1", "effect": {"empathy": 2}, "is_bad": False},
            "B": {"text": "💪 擺出戰鬥姿態，準備突圍！ (Take a combat stance to break out!)", "next": "5_A2", "effect": {"bravery": 2}, "is_bad": False},
            "C": {"text": "🕯️ 點燃煙霧彈，趁煙霧逃走！ (Use smoke bombs to escape!)", "next": "BAD_END_SMOKE", "effect": {"bravery": -1}, "is_bad": True,
                  "bad_reason": "煙霧觸發了粉塵爆炸，你被困在倒塌的礦洞中。火鷹俠救出你時，化石已被轉移。\n(You caused a dust explosion and got trapped.)"}
        }
    },
    "4_C2": {
        "title_tc": "第 4 頁：機器人發現交易現場", "title_en": "Page 4: Robot Finds a Transaction Site",
        "sfx": "💵 金錢！MONEY!",
        "story_tc": "機器人拍到一群黑衣人在倉庫中交易，他們正在交接「恐龍之王」化石，買家是一個外國富商。你決定阻止。",
        "story_en": "The robot films a transaction between a group in black and a foreign merchant for the King fossil. You decide to stop it.",
        "choices": {
            "A": {"text": "📞 聯繫警方，同時設法拖延時間！ (Call police and try to stall!)", "next": "5_A1", "effect": {"bravery": 0, "empathy": 1}, "is_bad": False},
            "B": {"text": "💣 用小型干擾器破壞他們的通訊，製造混亂！ (Use a jammer to disrupt their comms, create chaos!)", "next": "5_A2", "effect": {"creativity": 2}, "is_bad": False},
            "C": {"text": "💸 冒充富商，出更高價買下化石，然後交還博物館！ (Fake being a merchant to buy the fossil and return it!)", "next": "BAD_END_FRAUD", "effect": {"empathy": -1}, "is_bad": True,
                  "bad_reason": "對方識破了你的身份，將你綁架，並帶着化石逃離。火鷹俠後來救了你，但化石已被賣到海外。\n(You were exposed, kidnapped, and the fossil was sold overseas.)"}
        }
    },

    # ================= 第五頁：最終對決或理解 =================
    "5_A1": {
        "title_tc": "第 5 頁：揭開真相——守護者的使命", "title_en": "Page 5: The Truth — Guardians' Mission",
        "sfx": "💡 原來如此！I SEE!",
        "story_tc": "老人告訴你，他是化石守護者，擔心博物館無法妥善保護化石，所以暫時「借」走，計劃在展覽開幕前歸還。你理解了他的善意，決定：",
        "story_en": "The old man reveals he is a fossil guardian who feared the museum couldn't protect it properly, so he 'borrowed' it. You understand his goodwill and decide:",
        "choices": {
            "A": {"text": "🫂 原諒他，並承諾協助博物館加強保安，共同守護歷史！ (Forgive him and help improve museum security together!)", "next": "6_LEADER", "effect": {"empathy": 3, "bravery": 1}, "is_bad": False},
            "B": {"text": "📜 說服他公開身份，成為博物館的榮譽顧問，以誠信解決問題！ (Persuade him to become an honorary consultant with integrity!)", "next": "6_HERO", "effect": {"empathy": 2, "creativity": 1}, "is_bad": False}
        }
    },
    "5_A2": {
        "title_tc": "第 5 頁：圍捕與談判", "title_en": "Page 5: Capture and Negotiation",
        "sfx": "🔫 放下武器！DROP IT!",
        "story_tc": "火鷹俠及時趕到，包圍了現場。你與對方頭目對話，發現他們是非法化石販賣集團。你決定：",
        "story_en": "Firebird arrives and surrounds the scene. You talk to the leader and find out they are an illegal fossil trafficking ring. You decide:",
        "choices": {
            "A": {"text": "⚖️ 用法律和道理說服他們自首，並交出化石！ (Use legal reasoning to persuade them to surrender!)", "next": "6_LEADER", "effect": {"empathy": 2, "bravery": 1}, "is_bad": False},
            "B": {"text": "💪 與火鷹俠聯手，將他們一網打盡，強行奪回化石！ (Team up with Firebird to defeat them and retrieve the fossil!)", "next": "6_HERO", "effect": {"bravery": 3}, "is_bad": False}
        }
    },

    # ================= 壞結局 =================
    "BAD_END_LEAK": {
        "title_tc": "📱 任務失敗：線索中斷", "title_en": "Mission Failed: Trail Lost",
        "sfx": "🔌 斷線！DISCONNECT!", "is_bad_ending": True,
        "story_tc": "你在網上發布照片，驚動了小偷，化石被迅速轉移，再也找不到蹤跡。任務失敗。",
        "story_en": "Your photo alerted the thief. The fossil was moved and lost forever. Mission failed."
    },
    "BAD_END_SIGNAL": {
        "title_tc": "📡 任務失敗：信號暴露", "title_en": "Mission Failed: Signal Exposed",
        "sfx": "💤 暈倒！KNOCKOUT!", "is_bad_ending": True,
        "story_tc": "你的信號被干擾並暴露位置，被人從背後擊暈。醒來時化石已無影無蹤。",
        "story_en": "Your signal was jammed and you were knocked out. The fossil was gone."
    },
    "BAD_END_ALARM": {
        "title_tc": "🚨 任務失敗：打草驚蛇", "title_en": "Mission Failed: False Alarm",
        "sfx": "🔔 鈴鈴！RING!", "is_bad_ending": True,
        "story_tc": "你呼叫警衛，可疑人物逃走並打碎展櫃，館長責備你，調查被迫暫停。",
        "story_en": "Guards scared the suspect away, and the investigation was halted."
    },
    "BAD_END_HOAX": {
        "title_tc": "💬 任務失敗：假線索氾濫", "title_en": "Mission Failed: Hoax Overload",
        "sfx": "📨 訊息！MESSAGE!", "is_bad_ending": True,
        "story_tc": "懸賞引來大量假消息，浪費了時間，真正的線索已經消失。",
        "story_en": "Fake tips flooded in, wasting time. The real lead went cold."
    },
    "BAD_END_GRAB": {
        "title_tc": "🥅 任務失敗：陷阱中伏", "title_en": "Mission Failed: Trapped",
        "sfx": "🕸️ 網住！NET!", "is_bad_ending": True,
        "story_tc": "你衝向化石，觸發了陷阱，被網住，化石被轉移。火鷹俠救了你但任務失敗。",
        "story_en": "You triggered a trap and were netted. The fossil was moved."
    },
    "BAD_END_INTERCEPT": {
        "title_tc": "📞 任務失敗：通訊延遲", "title_en": "Mission Failed: Delayed Call",
        "sfx": "📵 無訊號！NO SIGNAL!", "is_bad_ending": True,
        "story_tc": "你聯絡火鷹俠時信號延遲，貨車已經逃離，任務失敗。",
        "story_en": "Signal delay allowed the van to escape."
    },
    "BAD_END_SMOKE": {
        "title_tc": "💥 任務失敗：粉塵爆炸", "title_en": "Mission Failed: Dust Explosion",
        "sfx": "💣 轟！BOOM!", "is_bad_ending": True,
        "story_tc": "煙霧彈引發粉塵爆炸，礦洞倒塌，你被埋。火鷹俠救出你但化石已失。",
        "story_en": "You caused a dust explosion and got buried. The fossil was lost."
    },
    "BAD_END_FRAUD": {
        "title_tc": "💰 任務失敗：假買家被識破", "title_en": "Mission Failed: Fake Buyer Exposed",
        "sfx": "🔗 手銬！CUFFS!", "is_bad_ending": True,
        "story_tc": "你冒充富商被識破，被綁架，化石被賣往海外。火鷹俠救了你但任務失敗。",
        "story_en": "You were exposed, kidnapped, and the fossil was sold overseas."
    }
}
