# 創世記・蒙召者的行程

依《恢復本・創世記綱目》「參　耶和華的呼召」，呈現亞伯拉罕、以撒、雅各（連同約瑟）的經歷。完整版包含 124 幕，約 31 分鐘，提供地圖動畫、人物動態、經文與綱目小點、播放進度，以及可選擇顯示的已完成事件圖示。

## 線上觀看

[開啟完整互動動畫](https://nomival.github.io/genesis-journey/)

網站由 GitHub Pages 提供，從 `main` 分支的根目錄發布。觀看者不需要 GitHub、Notion 或 ChatGPT 帳號。你也可以把此網址嵌入 Notion 訓練教材。

## 在自己的電腦預覽

在 GitHub 按 `Code → Download ZIP`，解壓縮後用桌面瀏覽器開啟 `index.html`。

也可以在資料夾內啟動本機預覽：

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

然後開啟 `http://127.0.0.1:8000/`。停止預覽時，在終端機按 `Ctrl+C`。

主程式、故事、地圖資料和樣式都包含在 HTML 內；圖示與提示工具仍會從 unpkg 載入，因此目前預覽需要網路。經文與參考資料連結也需要網路。

## 修改與重建

- `index.html`：可直接使用的完整網頁。
- `player-source.html`：故事資料、動畫和互動控制。
- `page-template.html`：播放器外框、共用樣式、瀏覽器進度儲存及手機捲動設定。
- `build.py`：以 Python 標準函式庫重新組合網頁，不需要 Node、Sites 或其他安裝套件。
- `.nojekyll`：未來使用 GitHub Pages 時，讓靜態網頁直接提供。

修改來源後執行：

```sh
python3 build.py
```

播放進度與地圖選項儲存在各瀏覽器的本機儲存空間，不會同步到 GitHub。動畫目前預設關閉已完成事件圖示，保留手機版整頁捲動修正。

## 停止公開存取

1. 到 `Settings → Pages`，把發布分支改成 `None`，按 `Save`，關閉網站。
2. 若原始檔案也不再公開，到 `Settings → General → Danger Zone → Change visibility`，把儲存庫改回 `Private`。

若日後重新發布，依適用方案調整儲存庫可見性，再到 `Settings → Pages → Deploy from a branch`，選擇 `main` 和 `/(root)`。私人儲存庫與私人網站的權限不同；一般 GitHub Pages 發布後會成為公開網站。已被下載或 fork 的副本不會隨可見性變更而收回。

## 內容與參考資料

- [恢復本・創世記綱目與經文](https://churchinmontereypark.org/Docs/RecoveryBible/bookid_1.htm)
- [OpenBible.info 地名資料（CC BY）](https://www.openbible.info/geo/)
- [Natural Earth 底圖](https://www.naturalearthdata.com/downloads/50m-physical-vectors/)
- [GitHub Pages 發布設定](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [GitHub Pages 私人發布限制](https://docs.github.com/en/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site)

地圖中的地名、區域示意及傳統比定依各幕註記辨識；經文未提供確切地點時，不將示意位置當作確定史實。故事與綱目的詳細出處可在播放器內查閱。
