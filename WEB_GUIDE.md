# WEB_GUIDE.md — 教育ポータル制作ガイド（Claude 作業用）

このリポジトリを「DeSFE Lab 教育ポータル」としてWeb公開する作業の規約。
**どのモデル・どのセッションで作業しても、このガイドに従うこと。**

## 公開の仕組みとレビューゲート（最重要）

- GitHub Pages は **gh-pages ブランチ**から配信される
- **main に push しても公開されない** → 作業は main に push し、鈴木先生のレビュー後に
  `git checkout gh-pages && git merge main && git push origin gh-pages` で公開する
- 公開URL: `https://anna-suzuki-tu.github.io/lab-materials/<パス>`

## サイト構造（計画）

```
index.html / en/           ← ポータル表紙【完成】
orientation/               ← Lab OS 導入＋6章目次【未】
  what-is-research/ (+en/) ← 01 研究とは何か【未】
  research-as-design/      ← 02 研究は設計で進める【未】
  paper-types/             ← 03 論文タイプと責任【未】
  five-layers/             ← 04 研究活動の5階層構造【未】
  grade-goals/             ← 05 学年別の責任と計画【未】
  habits-culture/          ← 06 必須習慣と文化【未】
lab-tools/
  paper-card/ (+en/)       ← 【未・新規創作。Fable推奨】
  quarter-plan/ (+en/)     ← 【未。ソース: quarter-plan/old/0409*.html】
writing-papers/ (+en/)     ← 【未。ソース: 20260709Labforum_writingpaper/build_slides*.py】
design-for-research/ (+en/)← 【未。ソース: 同フォルダの build_slides*_design4research_backup.py（内容はそのまま移植）】
career-design/ (+en/)      ← 【完成・公開済み】
```

各ページ完成時は、ポータル（index.html / en/index.html）の該当タイルを
`div.tile.soon` → `a.tile`（badge を `live` に）へ更新すること。

## デザイン規約

- 共通CSS: `assets/style.css` を `<link>` で読み込む（コピーしない）。
  ページ固有の微調整のみ `<style>` で追加可
- トーン: アイスブルー #E7F2F6 / Primary #207A91 / Accent #C6A44A（多用禁止）
- 構成テンプレ: career-design/index.html を手本にする
  （lang-sw → kicker → title-row → 本文カード → footer）
- 全ページ: スマホ最適化・日英相互リンク（lang-sw）・パンくず（.breadcrumb でポータルへ）
- 検証: Chrome headless でスクショ確認
  `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --screenshot=... --window-size=500,H --hide-scrollbars file://...`
  （幅500未満はヘッドレスの最小幅の都合で右が切れて見えるが実機では正常）

## コンテンツ規約（スライド→読み物化）

- スライドの主張文 → 見出し（h2/h3）に、語る内容 → 本文の段落に展開する
- **内容の追加・解釈は最小限に**。行間を埋める文章はスライドの文脈から自然に導けるものだけ
- 各ページ末尾: 発表スライド（PDF）ダウンロードリンク＋関連ページへのリンク
- 「準備中」ページへのリンクは張らない（ポータルのタイルは div.soon のまま）
- 日本語版を先に作り先生レビュー → 英語版は英語スライド原文＋日本語Web版を突き合わせて作成

## モデル割り当て（コスト最適化）

| 作業 | モデル |
|---|---|
| Orientation日本語の文章化 / paper-card新規作成 / ポータル文言 | Fable / Opus |
| Orientation英語版 / quarter-plan移植・英訳 / writing-papers / design-for-research | Sonnet |
| スクショ検証・リンクチェック・git・PDF出力 | Haiku |

## 注意

- `orientation/`（pptxビルド一式）・`quarter-plan/old/` はソース資材。
  push してよいが `__pycache__/`・`~$*.pptx` は除外（.gitignore 済みか確認）
- Notionテンプレへのリンク: lab-tools 各ページは「なぜ使うか→どう使うか→テンプレリンク」の3部構成。
  テンプレの公開リンクは先生に確認して取得する
- **lab-tools 完成時の宿題**: orientation/research-as-design（Paper Card節）と
  orientation/grade-goals（Quarter Plan節）の末尾にある
  「Lab Tools「◯◯」で詳しく解説します（準備中）」の文を、実リンクに変換すること
