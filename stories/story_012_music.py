# ==============================================================================
# 🎨 火鷹俠 12：音樂之都的失聲危機 (The Silenced City of Music)
# 融入 PERCCI 品格 (同理心、尊重) + KLA (藝術教育、科學教育、數學)
# ==============================================================================

STORY_INFO = {
    "id": "Story12",
    "name_tc": "🎨 火鷹俠 12：音樂之都的失聲危機",
    "name_en": "Firebird 12: The Silenced City of Music"
}

SCENES = {
    # ===== 起始 =====
    "1_START": {
        "title_tc": "第 1 頁：消失的旋律", "title_en": "Page 1: The Vanishing Melody",
        "sfx": "🔇 嗡嗡... BUZZ...",
        "story_tc": "大事不好了！音樂之都的「旋律水晶」被一隻名叫『刺耳怪獸』的巨獸搶走了！現在整個城市只剩下難聽的噪音，沒有人能唱歌。火鷹俠決定前往怪獸的噪音洞穴奪回水晶：",
        "story_en": "Oh no! The 'Melody Crystal' of the City of Music has been stolen by the 'Screeching Monster'! Now the city is filled with terrible noise, and no one can sing. Firebird decides to head to the monster's Noise Cave:",
        "choices": {
            "A": {"text": "🎧 運用 STEAM 知識，發明一副「聲波中和降噪耳機」保護耳朵！ (Use STEAM knowledge to invent 'Active Noise Cancelling Headphones' to protect your ears!)", "next": "2_A", "effect": {"creativity": 2}, "kla": ["TECH", "SCIENCE"], "is_bad": False},
            "B": {"text": "🛡️ 戴上厚厚的安全頭盔，勇敢地直接衝進噪音洞穴！ (Put on a thick safety helmet and bravely charge straight into the Noise Cave!)", "next": "2_B", "effect": {"bravery": 1}, "kla": ["PE"], "is_bad": False},
            "C": {"text": "📢 拿出超級大喇叭，用更大的噪音跟怪獸對吵！ (Take out a giant megaphone and shout back with even louder noise!)", "next": "BAD_END_NOISE", "effect": {"bravery": -1}, "kla": ["HUMANITIES"], "is_bad": True,
                  "bad_reason": "以暴易暴是無法解決問題的！更大的噪音引發了山洞共振，差點導致塌方！任務失敗……\n(Fighting noise with more noise doesn't solve the problem! It caused an echo that almost collapsed the cave! Mission failed...)"}
        }
    },

    # ===== 分支 A：降噪耳機路線 =====
    "2_A": {
        "title_tc": "第 2 頁：音樂密碼門", "title_en": "Page 2: The Musical Password Door",
        "sfx": "🎹 叮叮！DING DING!",
        "story_tc": "你來到了洞穴深處，被一扇巨大的鋼琴鍵盤門擋住了。門上寫著一段未完成的音階規律：「Do, Re, Mi, Fa, ？」",
        "story_en": "Deep in the cave, a giant piano keyboard door blocks your way. It shows an incomplete musical scale pattern: 'Do, Re, Mi, Fa, ?'",
        "choices": {
            "A": {"text": "🎵 彈奏下一個音符「So」，完成音階規律解開大門！ (Play the next note 'So' to complete the scale and unlock the door!)", "next": "3_A", "effect": {"creativity": 1}, "kla": ["MATH", "ARTS"], "is_bad": False},
            "B": {"text": "🔨 用拳頭隨便亂砸鋼琴琴鍵！ (Smash the piano keys randomly with your fists!)", "next": "BAD_END_RANDOM", "effect": {"creativity": -2}, "kla": ["ARTS"], "is_bad": True,
                  "bad_reason": "亂砸樂器是錯誤的行為！密碼門因為輸入錯誤而被永久鎖上了。任務失敗……\n(Smashing instruments is wrong! The door permanently locked due to wrong inputs. Mission failed...)"}
        }
    },

    # ===== 分支 B：衝鋒路線 =====
    "2_B": {
        "title_tc": "第 2 頁：聲波衝擊波！", "title_en": "Page 2: Sonic Shockwaves!",
        "sfx": "〰️ 呼嘯！WHOOSH!",
        "story_tc": "你衝進洞穴，但怪獸發出了強大的環形聲波，震得你寸步難行。火鷹俠運用科學觀察力：",
        "story_en": "You charge into the cave, but the monster releases powerful circular sonic waves, making it hard to move. Firebird uses scientific observation:",
        "choices": {
            "A": {"text": "👀 觀察聲波擴散的頻率與間隙，像跳繩一樣靈活閃避！ (Observe the frequency and gaps of the waves, dodging nimbly like jumping rope!)", "next": "3_A", "effect": {"bravery": 1, "creativity": 1}, "kla": ["SCIENCE", "PE"], "is_bad": False},
            "B": {"text": "🏃‍♂️ 閉著眼睛，不顧一切地硬撞過去！ (Close your eyes and recklessly crash through!)", "next": "BAD_END_CRASH", "effect": {"bravery": -2}, "kla": ["PE"], "is_bad": True,
                  "bad_reason": "遇到危險時不能盲目硬闖！你被強大的聲波彈飛了出去。任務失敗……\n(Never charge blindly into danger! The sonic wave bounced you away. Mission failed...)"}
        }
    },

    # ===== 第 3 頁匯合 =====
    "3_A": {
        "title_tc": "第 3 頁：刺耳怪獸的秘密", "title_en": "Page 3: The Monster's Secret",
        "sfx": "😢 嗚嗚... WAAAH...",
        "story_tc": "你終於找到了怪獸！但你發現他躲在角落偷偷哭泣。原來他天生嗓音沙啞，大家都嘲笑他唱歌難聽，他一生氣才偷走水晶，想讓所有人都不能唱歌。火鷹俠決定：",
        "story_en": "You found the monster! But he is crying secretly in the corner. His voice is naturally raspy, and everyone laughed at him. He stole the crystal out of anger so no one could sing. Firebird decides to:",
        "choices": {
            "A": {"text": "❤️ 展現同理心與尊重，告訴他每種聲音都有特色，邀請他嘗試「敲擊樂」！ (Show empathy and respect, tell him every voice is unique, and invite him to try 'Percussion'!)", "next": "4_A", "effect": {"empathy": 2}, "kla": ["HUMANITIES", "ARTS"], "is_bad": False},
            "B": {"text": "📦 不聽他解釋，立刻丟出「超級靜音網」把他抓住！ (Ignore his explanation and throw the 'Super Mute Net' to trap him!)", "next": "4_B", "effect": {"bravery": 2}, "kla": ["TECH"], "is_bad": False}
        }
    },

    # ===== 第 4 頁 (同理心路線) =====
    "4_A": {
        "title_tc": "第 4 頁：尋找新節奏", "title_en": "Page 4: Finding a New Rhythm",
        "sfx": "🥁 咚噠咚！DUM DUM!",
        "story_tc": "怪獸很感動，但他不知道怎麼控制力度，一敲鼓就差點把鼓打爛。火鷹俠決定教導他：",
        "story_en": "The monster is moved, but he doesn't know how to control his strength and almost breaks the drum. Firebird decides to teach him:",
        "choices": {
            "A": {"text": "🌬️ 運用科學知識，教他深呼吸，感受力量的傳遞與控制！ (Use science knowledge, teach him deep breathing to feel and control the transfer of power!)", "next": "5_A", "effect": {"creativity": 1, "empathy": 1}, "kla": ["SCIENCE", "PE"], "is_bad": False},
            "B": {"text": "🤝 溫柔地握住他的手，帶著他慢慢地一起打出穩定的節拍！ (Gently hold his hands and guide him slowly to play a steady beat together!)", "next": "5_A", "effect": {"empathy": 2}, "kla": ["ARTS", "HUMANITIES"], "is_bad": False}
        }
    },

    # ===== 第 4 頁 (靜音網路線) =====
    "4_B": {
        "title_tc": "第 4 頁：破裂的旋律水晶", "title_en": "Page 4: The Cracked Melody Crystal",
        "sfx": "💔 喀啦... CRACK...",
        "story_tc": "雖然抓住了怪獸，但在混亂中，旋律水晶掉在地上裂開了！音樂之都的聲音正在迅速消失。火鷹俠必須緊急修復：",
        "story_en": "Although the monster is caught, the Melody Crystal fell and cracked during the struggle! The city's sound is fading fast. Firebird must repair it:",
        "choices": {
            "A": {"text": "🔧 使用「聲波共振焊接儀」，用精準的頻率修補裂縫 (STEAM)！ (Use the 'Sonic Resonance Welder' to repair the crack with precise frequencies!)", "next": "5_B", "effect": {"creativity": 2}, "kla": ["SCIENCE", "TECH"], "is_bad": False}
        }
    },

    # ===== 第 5 頁 (圓滿結局) =====
    "5_A": {
        "title_tc": "第 5 頁：最棒的交響樂！", "title_en": "Page 5: The Best Symphony!",
        "sfx": "🌟 歡呼！BRAVO!",
        "story_tc": "怪獸學會了打鼓，他沙啞的吼聲竟然變成了超酷的重低音伴奏！你們一起把旋律水晶送回城市，舉辦了一場最棒的交響樂會！",
        "story_en": "The monster learned to play drums, and his raspy voice became a cool bass accompaniment! You returned the crystal together and held the best symphony concert!",
        "choices": {
            "A": {"text": "🏆 成為包容與藝術的「全人小領袖」！ (Become a 'Whole-person Leader' of inclusivity and arts!)", "next": "6_LEADER", "effect": {"empathy": 3}, "kla": ["ARTS", "HUMANITIES"], "is_bad": False}
        }
    },
    
    # ===== 第 5 頁 (英雄結局) =====
    "5_B": {
        "title_tc": "第 5 頁：恢復寧靜的城市", "title_en": "Page 5: The Restored Peaceful City",
        "sfx": "🎶 悠揚... MELODIOUS...",
        "story_tc": "你成功修復了水晶並交還給城市，美妙的音樂再次響起。雖然怪獸被關了起來，但城市恢復了和平。",
        "story_en": "You successfully repaired the crystal and returned it. Beautiful music plays again. Though the monster is locked up, the city is at peace.",
        "choices": {
            "A": {"text": "🎖️ 成為守護規則與和平的「勇氣英雄」！ (Become a 'Courage Hero' who guards rules and peace!)", "next": "6_HERO", "effect": {"bravery": 3}, "kla": ["TECH"], "is_bad": False}
        }
    },

    # ===== 壞結局 =====
    "BAD_END_NOISE": {
        "title_tc": "💥 任務失敗：以暴易暴", "title_en": "Mission Failed: Fighting Fire with Fire",
        "sfx": "💥 CRASH!", "is_bad_ending": True,
        "story_tc": "用更大的噪音對罵是解決不了問題的，只會讓情況變得更糟。我們要學會冷靜溝通！",
        "story_en": "Yelling back with louder noise doesn't solve problems, it makes things worse. We must learn to communicate calmly!"
    },
    "BAD_END_RANDOM": {
        "title_tc": "💥 任務失敗：破壞樂器", "title_en": "Mission Failed: Instrument Destruction",
        "sfx": "❌ ERROR!", "is_bad_ending": True,
        "story_tc": "樂器需要被溫柔對待。遇到不懂的規律時，應該靜下心來思考，而不是發脾氣亂砸！",
        "story_en": "Instruments must be treated gently. When facing an unknown pattern, calm down and think, don't throw a tantrum!"
    },
    "BAD_END_CRASH": {
        "title_tc": "💥 任務失敗：盲目硬闖", "title_en": "Mission Failed: Reckless Charge",
        "sfx": "💫 DIZZY!", "is_bad_ending": True,
        "story_tc": "遇到危險的物理現象（如聲波衝擊）時，要運用科學觀察找出弱點，不能只靠蠻力！",
        "story_en": "When facing dangerous physical phenomena (like shockwaves), use scientific observation to find weak points, not just brute force!"
    }
}
