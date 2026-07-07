# 木こりの森（PWA）

木を切って集め、加工して販売し、効率化していく放置系ゲームの Android アプリ版（PWA）です。

## 含まれるファイル

| ファイル | 役割 |
|---|---|
| `index.html` | ゲーム本体（単体で動作） |
| `manifest.json` | アプリ名・アイコン・全画面表示などの設定 |
| `service-worker.js` | オフライン動作用のキャッシュ |
| `icon-192.png` / `icon-512.png` / `icon-512-maskable.png` | アプリアイコン |
| `make_icons.py` | アイコン再生成用スクリプト（任意） |

## PCで動作確認する

`index.html` をダブルクリックしてブラウザで開けば、ゲーム自体は遊べます。
（この開き方だと Service Worker とアプリインストールは無効です。動作確認だけなら十分です。）

より正確に試すには、このフォルダで簡易サーバを立てます：

```
cd C:\Users\atsuj\Desktop\Testfolder
python -m http.server 8000
```

ブラウザで `http://localhost:8000` を開きます。

## Androidアプリとして入れる（PWA）

Android の「ホーム画面に追加」でアプリ化するには、ファイルを **HTTPS で公開**する必要があります（`file://` では不可）。無料の方法：

### 方法A: Netlify Drop（最も簡単・アカウント任意）
1. https://app.netlify.com/drop をPCで開く
2. この `Testfolder` フォルダごとドラッグ＆ドロップ
3. 発行された `https://〜.netlify.app` のURLを Android の Chrome で開く

### 方法B: GitHub Pages
1. GitHubにリポジトリを作り、このフォルダの中身をアップロード
2. Settings → Pages で公開ブランチを指定
3. 発行URLを Android の Chrome で開く

### ホーム画面に追加する手順（Android / Chrome）
1. 公開URLを Chrome で開く
2. 右上のメニュー（⋮）→「ホーム画面に追加」または「アプリをインストール」
3. ホーム画面のアイコンから、全画面・オフラインで起動できます

## セーブについて
- 進行状況はブラウザ／アプリ内（localStorage）に保存されます。
- 公開URLが変わると別データ扱いになります。同じURLで使い続けてください。

## アイコンを変えたいとき
`make_icons.py` の色やモチーフを編集して、以下を実行：

```
python make_icons.py
```
