# 📘 Assignment 1: Dimensionality Reduction and Visualization

## 🎯 作業目標
- 使用 **PCA（Principal Component Analysis）** 將高維資料降維至 2 維並進行視覺化。
- **禁止使用現成 PCA 函數**，需自行實作 PCA 演算法。

---

## 📂 資料集說明
提供三個資料集：
- `Iris`
- `Cho`
- `Iyer`

> 每筆資料的最後一欄為 cluster label，其餘為屬性。

---

## 🧑‍💻 實作要求
使用提供的 Python 模板，完成以下函數：

### 1. `loadDataSet`
- 讀取 CSV 檔案
- 輸出 `dataMat`（資料矩陣）與 `labelMat`（標籤）

### 2. `pca`
- 實作 PCA，將資料降維至 2 維

### 3. `plot`
- 繪製散點圖
- 根據標籤上色
- 儲存圖檔

### 4. `main`
- 呼叫上述函數
- 支援命令列或 IDE 執行

---

## 📊 作業步驟
1. 完成模板程式碼
2. 對 `Iris` 資料集執行 PCA 並繪製散點圖，與範例圖比對
3. 若 `Iris` 成功，則對 `Cho` 和 `Iyer` 資料集執行相同操作
4. 準備提交內容

---

## 📦 提交內容
請打包為 `Assignment1.zip`，包含以下檔案：

- Python 程式碼
- 報告（`Assignment1.docx` 或 `Assignment1.pdf`），內容包括：
  1. `Cho` 和 `Iyer` 的散點圖（含軸刻度與標籤）
  2. PCA 與繪圖程式碼
  3. AI 工具使用聲明（是否使用 ChatGPT、Copilot 等工具）

---

## ⏰ 截止時間
- **2025 年 10 月 3 日 11:59PM**
