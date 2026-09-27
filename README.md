# 🌸 學習共同體公開課與 Jumping Task 全套設計技能 (lesson-study-jumping-task)

[![GitHub Release](https://img.shields.io/badge/Release-v3.0-blue.svg)](https://github.com/amiaoyeh-arch/lesson-study-jumping-task)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Theme Color](https://img.shields.io/badge/Theme-%233F98DE-brightgreen.svg)](https://github.com/amiaoyeh-arch/lesson-study-jumping-task)

本儲存庫為 **Google Antigravity** 專用之「學習共同體（SLC）公開課教案與 Jumping Task 伸展跳躍任務全套設計技能」。引導教師從真實課堂實踐與幾何挑戰出發，自動化產出標準 Word 正式教案、RWD 響應式網頁簡報、16:9 大字版 PowerPoint、向量 PDF 簡報與日系動漫課堂插圖。

---

## 📦 核心五合一交付成果

1. 📄 **新北市標準 Word 正式教案 (`.docx`)**：統一採用 `#3F98DE` 主題藍色，內建基本資料、教學理念、課綱對照、四大維度 13 項理據、40分鐘四階段逐字流程、六大理答預想表、觀課表與學生專用學習單。
2. 🌐 **RWD 響應式 HTML 互動導學簡報 (`.html`)**：零依賴單檔（Base64 內嵌）、左右分欄封面零重疊、卡片插圖 50% 寬度適配排版、內建四階段倒數計時器、全螢幕與鍵盤快捷鍵切換。
3. 📊 **16:9 大字版 PowerPoint 簡報 (`.pptx`)**：16:9 寬螢幕、高對比大字排版、高解析幾何題目圖嵌入、文字完全可編輯。
4. 📄 **16:9 高解析向量 PDF 簡報 (`.pdf`)**：Edge Headless 向量渲染輸出，投影無鋸齒、列印無失真。
5. 🎨 **日系動漫水彩繪本風格課堂插圖**：專注傾聽、耳語對話、勇於提問、互惠協同、安靜書寫反思。

---

## 🚀 快速安裝與使用 (Installation & Usage)

### 1. 安裝至 Antigravity 技能目錄
將本儲存庫 Clone 或複製至您的 Antigravity Skills 目錄：
```bash
git clone https://github.com/amiaoyeh-arch/lesson-study-jumping-task.git "C:\Users\<YourUsername>\.gemini\config\skills\lesson-study-jumping-task"
```

### 2. 喚醒語 (Prompt Triggers)
在對話中輸入以下任一指令即可自動載入：
- 「製作公開課教案」
- 「設計 Jumping Task」
- 「做跳躍任務教案」
- 「公開課準備」
- 「做課例研究簡報」

---

## 🛠️ 工具模組清單 (Scripts)

| 模組檔案 | 說明 |
| :--- | :--- |
| `scripts/docx_builder.py` | 產出標準格式 Word 正式教案與學習單（#3F98DE 主題色） |
| `scripts/html_builder.py` | 產出 RWD 響應式 HTML 互動導學簡報（含計時器與全螢幕） |
| `scripts/pptx_builder.py` | 產出 16:9 大字版 PowerPoint 簡報檔 |
| `scripts/pdf_builder.py` | 調用 Edge Headless 輸出 16:9 向量 PDF 簡報 |
| `scripts/illustration_helper.py` | 生成日系水彩動漫課堂情境插圖之 Prompt |

---

## 📚 知識庫 (References)

- `references/dialogue_strategies.md`：學習共同體六大理答對話策略（轉引、轉問、反問、提示、釐清、深究）。
- `references/curriculum_guidelines.md`：國家教育研究院課程綱要檢索指引與核心素養代碼庫。
- `references/lesson_plan_template.md`：新北市學習共同體標準教案公版範本與 13 項理據規範。

---

## 🌟 課例示範 (Demo)
- 六年級數學「扇形面積跳躍任務：四葉草綠地的秘密」公開課線上簡報：  
  👉 [https://amiaoyeh-arch.github.io/lesson-study-11510-g6-math-sector-area/](https://amiaoyeh-arch.github.io/lesson-study-11510-g6-math-sector-area/)
