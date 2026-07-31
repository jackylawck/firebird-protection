# ==============================================================================
# 🏫 幼小銜接教育框架 (Hong Kong EDB KLA Framework)
# 統整八大學習領域與 PERCCI 品格教育
# ==============================================================================

# 1. 官方八大學習領域 (Eight Key Learning Areas)
KLA_DICT = {
    "LANG_CH": {"name_tc": "中國語文教育", "icon": "📖", "desc": "書面語閱讀、成語與語感"},
    "LANG_EN": {"name_tc": "英國語文教育", "icon": "🔤", "desc": "英文詞彙、雙語對照"},
    "MATH": {"name_tc": "數學教育", "icon": "🔢", "desc": "邏輯推理、空間與數字"},
    "SCIENCE": {"name_tc": "科學教育 (小學科學)", "icon": "🔬", "desc": "自然現象、物理法則、環保"},
    "TECH": {"name_tc": "科技教育", "icon": "🤖", "desc": "計算思維、編程邏輯、STEAM"},
    "HUMANITIES": {"name_tc": "人文教育 (小學人文)", "icon": "🌍", "desc": "個人成長、社會責任、文化"},
    "ARTS": {"name_tc": "藝術教育", "icon": "🎨", "desc": "音樂、色彩、視覺創意"},
    "PE": {"name_tc": "體育", "icon": "🏃‍♂️", "desc": "健康知識、動作與協調"}
}

# 2. 全人品格教育核心 (PERCCI)
PERCCI_DICT = {
    "Perseverance": {"name_tc": "堅毅", "icon": "💪"},
    "Empathy": {"name_tc": "同理心", "icon": "❤️"},
    "Respect": {"name_tc": "尊重", "icon": "🤝"},
    "Courage": {"name_tc": "勇氣", "icon": "🦁"},
    "Commitment": {"name_tc": "承擔", "icon": "🛡️"},
    "Integrity": {"name_tc": "誠信", "icon": "⚖️"}
}

# 未來擴充：在每個故事選項的 "effect" 中，除了 "bravery", "creativity" 外，
# 可以加上 "kla": ["SCIENCE", "TECH"] 來精準追蹤學習進度！
