---
name: lesson-study-jumping-task
description: 學習共同體（SLC）公開課教案與 Jumping Task 伸展跳躍任務簡報全套設計技能。包含：1. 國教院課綱檢索與新北公版教案/學習單、2. 配合頁面內容的動漫插圖生成、3. RWD 響應式 HTML 互動導學簡報（含計時器）、4. 16:9 大字版 PowerPoint 簡報、5. 高解析度向量 PDF 簡報、6. 理答六策略對話引導。當使用者說「製作公開課教案」、「設計 Jumping Task」、「公開課準備」、「做跳躍任務教案」、「做課例研究簡報」、「觀課議課簡報」或任何公開課設計需求時載入。
---

# 學習共同體公開課教案與 Jumping Task 全套設計技能 (lesson-study-jumping-task)

本技能提供標準化、自動化且具備教育哲學深度的學習共同體（SLC）公開課全套課例設計流程。產出包含符合新北市標準之 **Word 正式教案（#3F98DE 主題色、含四大維度 13 項理據、逐字流程、六大理答、觀課表與學習單）**、**16:9 大字版引導簡報 (PPTX)**、**RWD 響應式離線互動導學簡報 (HTML)**、**高解析度向量 PDF 簡報** 以及 **配合頁面內容的動漫風格課堂插圖**。

---

## 📖 使用說明與快速開始 (Quick Guide)

當您需要準備一堂學習共同體公開課時，只需告知：
1. **年級與學科**（如：六年級數學、三年級國語）
2. **單元名稱與版本**（如：南一版 115-1 第六單元 扇形的周長和面積）
3. **想設計的幾何題目或任務構想**（文字描述、課本截圖或手繪草稿）

本技能將自動依照六大標準工作流程，產出全套教材包並自動同步至 GitHub 與雲端硬碟！

---

## 🧭 六大標準工作流程 (6-Step Workflow)

### 步驟 1：確認公開課基本資訊與素材
- 於 `E:\2026AI_agent\2026學習共同體課例分享\` 下建立子目錄：`[民國年月]_[年級]_[領域]_[單元簡稱]`（例如：`11510_6年級數學_扇形面積跳躍任務`）。

### 步驟 2：課綱指標檢索與確認 (嚴格執行)
- 參考 `references/curriculum_guidelines.md`，連線至**國家教育研究院課程綱要網站**：
  🔗 [國家教育研究院 領域/科目課程綱要](https://www.naer.edu.tw/PageSyllabus?fid=52)
- 檢索並提取核心素養、學習表現與學習內容。向教師完整回報課綱指標，確認無誤後再進入教案撰寫。

### 步驟 3：Jumping Task 挑戰任務與認知衝突設計
- **跳躍任務核心四要素**：
  1. **低門檻（Low Floor，暖身基礎題）**：每位學生皆能在個人自學階段看懂題意並動筆嘗試（如邊長 10cm 正方形求弓形面積 28.5 cm²）。
  2. **高天花板（High Ceiling，跳躍伸展題）**：存在多元解題路徑與深層結構（如邊長 20m 正方形對角線四葉草面積 228 m²；邊長 16cm 雙半圓交疊面積 128 cm²）。
  3. **認知衝突與經驗遷移**：未知的大圖形能否拆解為已知的暖身小圖形？（分割法 vs 容斥原理與守恆）。
  4. **全組合算式窮舉與六大理答預想**：參考 `references/dialogue_strategies.md`，窮舉學生可能的解題策略，規劃「轉引、轉問、反問、提示、釐清、深究」等理答對話。

### 步驟 4：動漫風格課堂情境插圖生成 (Anime Illustrations)
- 使用 `scripts/illustration_helper.py` 產出符合日系吉卜力/新海誠水彩繪本風格的 Prompt，調用 `generate_image` 生成插圖：
  - **封面插圖**：左上思考小孩（圓形）、左下 4 人小組討論（矩形）。
  - **課堂常規約定插圖**：👂 專注傾聽（兩人並坐溫和注視）、💬 耳語對話、🙋 勇於提問、🧩 互惠協同（50% 圖片寬度排版）。
  - **反思總結插圖**：📝 孩子們在柔和陽光下安靜書寫學習單札記。

### 步驟 5：執行 Scripts 產出五大核心教材成果
1. **📄 Word 正式教案與學生學習單 (DOCX / MD)**：執行 `scripts/docx_builder.py`（#3F98DE 主題色、固定 13 項理據表）。
2. **🌐 RWD 響應式 HTML 互動導學簡報**：執行 `scripts/html_builder.py`（左右分欄封面零重疊、50% 圖片卡片、純題目布題無爆雷、內建計時器）。
3. **📊 16:9 大字版 PowerPoint 簡報 (PPTX)**：執行 `scripts/pptx_builder.py`（大字體、圖文分離排版）。
4. **📄 16:9 高解析度向量 PDF 簡報**：執行 `scripts/pdf_builder.py`（Edge Headless 向量無失真輸出）。

### 步驟 6：專案歸檔與 GitHub 同步規範
- 將教材包依照標準目錄結構整理：
  - `01_簡報與互動導學/`（佈題思考版第3版_最新推薦/、正式教學完整版_含解題/）
  - `02_教案與學習單/`（DOCX、MD）
  - `03_題目圖檔與幾何素材/`（PNG 題目圖、手繪原稿）
  - `assets/`（動漫情境插圖）
  - `README.md`（完整手冊與導覽）
- 執行 Git commit 與 push，同步推播至 GitHub 儲存庫與 GitHub Pages。

---

## 🛠️ Scripts 工具模組清單

- `scripts/docx_builder.py`：新北學習共同體公版教案（#3F98DE）與學習單生成器。
- `scripts/html_builder.py`：RWD 響應式 HTML 互動簡報生成器（零重疊封面、50% 卡片）。
- `scripts/pptx_builder.py`：16:9 寬螢幕大字版 PPTX 生成器。
- `scripts/pdf_builder.py`：Edge Headless 高解析 16:9 PDF 輸出模組。
- `scripts/illustration_helper.py`：日系動漫課堂情境插圖 Prompt 產生器。

---

## 📚 References 知識庫

- `references/dialogue_strategies.md`：學習共同體六大理答對話策略（轉引、轉問、反問、提示、釐清、深究）詳解。
- `references/curriculum_guidelines.md`：國家教育研究院課程綱要檢索指引與素養代碼對照表。
- `references/lesson_plan_template.md`：新北市學習共同體標準教案範本與 13 項理據結構規範。
