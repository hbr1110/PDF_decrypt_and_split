# Pdf Utilities

本儲存庫 (Repository) 提供一個 Python 腳本 `decrypt_and_split.py`，主要功能：

1. **PDF 解密**：利用已知密碼解鎖加密的 PDF 檔案。
2. **PDF 分割**：將解密後的 PDF 根據指定頁碼區間切分成多個章節檔案。

---

## 檔案說明 (Files)

- **decrypt_and_split.py**：主程式模組，包含兩個函式：
  - `decrypt_pdf(input_path, output_path, password)`：對加密 PDF 解密並儲存。
  - `split_pdf_by_pages(input_pdf, output_prefix, start_page, end_page)`：按頁碼範圍切分 PDF。

- **requirements.txt**：列出執行此腳本所需的 Python 套件。

- **README.md**：本使用說明檔。

---

## 安裝步驟 (Installation)

1. **Clone 此儲存庫**：
   ```bash
   git clone https://github.com/hbr1110/PDF_decrypt_and_split.git
   cd PDF_decrypt_and_split
   ```

2. **建立虛擬環境 (建議，但非必要)**：
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **安裝相依套件**：
   ```bash
   pip install -r requirements.txt
   ```

---

## 使用範例 (Usage)

### 1. 解密 PDF

```python
from decrypt_and_split import decrypt_pdf

encrypted_path = "/path/to/encrypted.pdf"
decrypted_path = "/path/to/decrypted.pdf"
pdf_password   = "yourPassword"

decrypt_pdf(encrypted_path, decrypted_path, pdf_password)
```
執行後，會在 `decrypted_path` 產生解密後的 PDF 檔案。

### 2. 分割 PDF

```python
from decrypt_and_split import split_pdf_by_pages

source_pdf = "/path/to/decrypted.pdf"
prefix     = "chapter"
# 範例：切出第 1~12 頁
split_pdf_by_pages(source_pdf, prefix, 1, 12)
# 範例：切出第 13~32 頁
split_pdf_by_pages(source_pdf, prefix, 13, 32)
```
可依需求調整 `start_page` 與 `end_page`。

---

## requirements.txt

以下為 `requirements.txt` 內容：
```text
pikepdf
PyPDF2
```
- **pikepdf**：處理 PDF 解密與儲存。
- **PyPDF2**：進行 PDF 讀取與分頁。

---

## 授權條款 (License)

請於此處填寫專案授權，如 MIT License、Apache 2.0 等。
