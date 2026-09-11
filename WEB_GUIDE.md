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
index.html / en/                ← ポータル表紙【完成】
orientation/                    ← Lab OS 導入＋3部10章＋付録2本【完成・JAのみ。EN未対応（旧6章構成のまま）】

  第Ⅰ部 探究の原理｜Principles
  what-is-research/ (+en/)      ← 01 研究とは何か【完成】
  science-framework/            ← 02 探究のプロセスと科学の枠組み【完成・EN未】

  第Ⅱ部 研究の設計｜Design
  question-design/               ← 03 問いの設計（旧 research-as-design を分割）【完成・EN未】
    question-archetypes/         ← 付録03-A 問いの型【完成・EN未】
  claim-design/                  ← 04 主張の設計（旧 research-as-design を分割）【完成・EN未】
  paper-types/ (+en/)            ← 05 論文タイプ｜信念のスコープと形式（旧03を改訂）【完成】
    paper-type-requirements/     ← 付録05-A 論文タイプ別の要件【完成・EN未】
  responsibility/                ← 06 研究の責任【完成・EN未】

  第Ⅲ部 研究室の運用｜Practice
  mission/                       ← 07 私たちは何を、なぜ研究するか【完成・EN未】
  five-layers/ (+en/)            ← 08 研究活動の5階層構造（旧04）【完成】
  grade-goals/ (+en/)            ← 09 学年別のゴールと計画（旧05）【完成】
  habits-culture/ (+en/)         ← 10 必須習慣と文化（旧06）【完成】

  research-as-design/           ← 旧02。question-design/ への meta refresh リダイレクトのみ残置（外部リンクを切らないため）
lab-tools/
  paper-card/ (+en/)            ← 【完成】
  quarter-plan/ (+en/)          ← 【完成】
writing-paper/ (+en/)           ← 【完成】
design-for-research/ (+en/)     ← 【完成】
career-design/ (+en/)           ← 【完成・公開済み】
```

Lab OS の EN版（`orientation/en/`）は旧6章構成のまま据え置き。JA側の3部10章化に伴う
EN側の対応方針は別途決定（現状は英語話者向けに「日本語版が改訂された」旨の注記を
各章に入れる案を検討中）。

各ページ完成時は、ポータル（index.html / en/index.html）の該当タイルを
`div.tile.soon` → `a.tile`（badge を `live` に）へ更新すること。

## デザイン規約（2026-07-16 ダークテーマに刷新）

- 共通CSS: `assets/style.css` を `<link>` で読み込む（コピーしない）。
  ページ固有の微調整のみ `<style>` で追加可
- トーン: **濃グレー地 #2E333A ＋ 白カード**。地の上の文字は #E6E9ED／補助 #9AA3AD。
  強調色は くすんだ青（塗り=#207A91・ダーク地の文字/リンク=#6FB9CC）と くすんだ金 #C6A44A（多用禁止）
- カード（白面）内の文字は濃色（--text #1F2937 / --muted #5D5D5D）。カード内の薄面は --panel #F1F3F5
- クリックできない情報（Lab Values等）は白カードにせず `.value`（金の左ライン銘板）を使う
- ※ スライド（slide_framework/SLIDE.md）は投影可読性のため**ライトテーマのまま**。Webのみダーク
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
