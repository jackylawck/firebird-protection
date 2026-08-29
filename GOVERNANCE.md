# 🏛️ Compliance, Data Privacy & AI Governance Statement
# 合規、數據隱私與人工智能治理聲明

**Last Updated / 最後更新日期:** August 2026  
**Document Version / 文件版本:** v1.0.0  
**Target Standards / 適用標準:** EU AI Act (Regulation (EU) 2024/1689), GDPR (Regulation (EU) 2016/679), Hong Kong PDPO (Cap. 486), ISO/IEC 42001:2023, ISO/IEC 27001:2022.

---

## 1. Executive Summary & Regulatory Scoping (概述與法規適用性界定)

### English
This project is an open-source, client-side educational interactive software designed with **Privacy by Design**, **Local-First Architecture**, and **Deterministic Logic**. 

To maintain the highest level of regulatory transparency and compliance:
- **EU AI Act Exemption / Classification:** Pursuant to Article 3(1) of the EU AI Act (Regulation (EU) 2024/1689), an AI system is defined as an engineered system that infers how to generate outputs for explicit or implicit objectives using machine learning and/or logic- and knowledge-based approaches. This project operates strictly on **deterministic finite-state automata (FSM) and pre-scripted pedagogical logic**. It does not utilize self-learning, adaptive machine-learning weights, unconstrained generative models, or autonomous decision-making inference engines in its runtime. Therefore, it falls **outside the scope of High-Risk AI Systems** under Annex III and General-Purpose AI (GPAI) systemic obligations.
- **Data Privacy & GDPR / HK PDPO Compliance:** The application processes zero telemetry and zero personal data on remote servers. All evaluations and progress states are processed strictly client-side.

### 中文 (繁體)
本項目為採用「預設隱私 (Privacy by Design)」、「本地優先 (Local-First Architecture)」與「確定性邏輯 (Deterministic Logic)」設計的開源互動教育軟件。

為貫徹最高規格的監管透明度與合規治理：
- **歐盟《人工智能法案》(EU AI Act) 適用性界定：** 根據歐盟 AI Act 第 3(1) 條定義，AI 系統係指能透過機器學習或特定邏輯演算法推導輸出之系統。本項目之底層邏輯嚴格採用**「確定性有限狀態機 (Deterministic FSM)」與預設教育情境腳本**，在運行時（Runtime）不涉及自主權重演化、黑盒機器學習模型或無約束生成式推理引擎。因此，本項目**依法豁免於高風險 AI 系統（Annex III）及通用人工智能（GPAI）之高階監管限制**。
- **數據隱私（GDPR / 香港 PDPO）合規性：** 系統絕不上傳任何使用者遙測數據或個人資料至遠端伺服器，所有評估運算均於前端即時完成。

---

## 2. Global Compliance & Standards Alignment Matrix (全球合規與標準對標矩陣)

| Framework / Standard <br> 監管框架 / 標準 | Applicability & Classification <br> 適用性與分類 | Technical Implementation & Safeguards <br> 技術實現與防護措施 | Compliance Status <br> 合規狀態 |
| :--- | :--- | :--- | :--- |
| **EU AI Act** <br> (Regulation 2024/1689) | **Minimal Risk / Deterministic Logic** <br> (最低風險 / 確定性邏輯系統) | • No autonomous unmonitored inference<br>• Fully transparent rule-based transitions<br>• Zero biometric or discriminatory profiling | ✅ **Exempt / Compliant by Design** <br> (預設合規 / 免除高風險負擔) |
| **GDPR** <br> (Regulation 2016/679) | **Data Minimization (Art. 5)** <br> **Privacy by Design (Art. 25)** | • Zero server-side data retention<br>• No tracking cookies or behavioral analytics<br>• Ephemeral browser memory / LocalStorage only | ✅ **Full Compliance** <br> (完全合規) |
| **Hong Kong PDPO** <br> (Cap. 486 香港私隱條例) | **Data Protection Principles (DPP 1-6)** <br> (保障資料原則) | • No collection of Personal Identifiable Information (PII)<br>• Absolute user data sovereignty (Local-only) | ✅ **Full Compliance** <br> (完全合規) |
| **ISO/IEC 42001:2023** <br> (AI Management System) | **AI Governance Controls Alignment** <br> (AI 管理體系控制項對標) | • Continuous algorithmic transparency<br>• Documented dataset integrity for educational prompts<br>• Explicit human-in-the-loop validation | 🛡️ **Aligned with Best Practices** <br> (符合最佳實踐) |
| **ISO/IEC 27001:2022** <br> (Information Security) | **Client-Side Security Architecture** <br> (客戶端資訊安全架構) | • No backend API attack surface<br>• Zero remote database vulnerabilities<br>• Open-source verifiable source code | 🛡️ **Zero Remote Threat Surface** <br> (零遠端威脅面) |

---

## 3. Data Flow & Zero-Retention Technical Architecture (數據流與零留存技術架構)


```

[ User Interaction / 用戶操作 ]
│
▼
┌────────────────────────────────────────────────────────┐
│            CLIENT BROWSER SANDBOX (前端沙盒)            │
│                                                        │
│  ┌────────────────────────┐  ┌───────────────────────┐ │
│  │  PWA / Service Worker  │  │ Deterministic Engine  │ │
│  │   (Local Resources)    │  │   (FSM Story Logic)   │ │
│  └────────────────────────┘  └───────────────────────┘ │
│                             │                          │
│                             ▼                          │
│               [ LocalStorage / IndexedDB ]              │
│               (User Device ONLY / 純本地儲存)           │
└────────────────────────────────────────────────────────┘
│
✕  NO DATA OUTBOUND (完全無外部數據傳輸)
▼
[ Remote Cloud Servers / Third-Party Trackers / Analytics ]

```

### Architectural Commitments (架構核心承諾):
1. **Local-First & Client-Side Execution (本地優先與客戶端運算):**  
   The application runs entirely within the client's web browser environment. Storage is confined to the user's sandboxed `localStorage` or `IndexedDB`.
2. **Zero Remote Data Retention (遠端零資料留存):**  
   No user profiles, assessment logs, choices, or educational responses are transmitted, collected, stored, or processed on external servers.
3. **No Third-Party Telemetry (無第三方遙測):**  
   The source code contains no third-party behavioral trackers, marketing pixels, or covert fingerprinting scripts.

---

## 4. Educational Content & Algorithmic Safety (教育內容與演算法安全)

- **Pedagogical Alignment (教育架構對齊):**  
  Scenarios are curated to align with Key Learning Areas (KLAs) and positive character development frameworks (e.g., PERCCI: Perseverance, Empathy, Respect, Courage, Creativity, Integrity).
- **Bias Prevention & Algorithmic Fairness (偏見防範與公平性):**  
  Educational options and feedback paths are audited to ensure fairness, ethical sound judgment, and avoidance of cultural, socioeconomic, or gender biases.
- **Transparency & Verifiability (透明度與可驗證性):**  
  All pedagogical branches and deterministic calculation paths are fully documented in the open-source repository for community and institutional scrutiny.

---

## 5. Disclaimer & Legal Limitation of Liability (免責聲明與法律責任限制)

### English
1. **Educational Purpose Only:** This repository and software are provided solely for open-source educational, research, and interactive pedagogical demonstration purposes.
2. **No Fiduciary or Professional Warranty:** The content provided does not constitute formal legal, psychological, or certified educational assessment advice.
3. **"AS IS" Basis:** Pursuant to the open-source licensing terms governing this repository, this software is provided "AS IS", without warranty of any kind, express or implied, including but not limited to fitness for a particular purpose or non-infringement.

### 中文 (繁體)
1. **僅供教育用途：** 本儲存庫與軟件僅作為開源教育、學術研究及互動教學展示之用。
2. **非專業或法律諮詢保證：** 本項目所提供之情境評估與內容，不構成任何正式法律、心理學或具備法定效力之教育評估建議。
3. **按現狀提供 (AS IS)：** 依據本開源項目之授權條款，軟件均按「現狀」提供，原作者不承擔任何明示或暗示之擔保責任，亦不對因使用或無法使用本軟件所產生之衍生性後果負責。

---

## 6. Governance & Compliance Contact (合規與治理聯繫)

If you have inquiries regarding the algorithmic logic, regulatory scoping, or data privacy practices of this project, please open an Issue on the official repository or contact the project maintainer.

如對本項目之演算法邏輯、法規界定或數據隱私設計有任何查詢，歡迎於本項目儲存庫提交 Issue 或聯繫專案維護者。
