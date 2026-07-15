"""
build_orientation_slides.py — 鈴木研オリエンテーション Day 1（統合版）

orientation/old/ の旧HTML資料（part0〜part6）の内容を1つのデッキに統合。
  - part0 後半は part1 の圧縮版、part3-1 は part2 の再スタイル版のため統合
  - デザインは slide_framework v2（SLIDE-md-20260703エンジニアリング協会）

構成
  オープニング（Part 0） → 6セクション
    1. 研究とは何か（Part 1）
    2. 研究は設計で進める（Part 2/3）
    3. 論文タイプと責任（Part 2.5）
    4. 研究活動の5階層構造（Part 4）
    5. 学年別の責任と計画（Part 5）
    6. 必須習慣と文化（Part 6）
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from slide_framework import SlideFramework

IMG_DIR = os.path.join(os.path.dirname(__file__), "images", "png")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def img(filename):
    path = os.path.join(IMG_DIR, filename)
    return path if os.path.exists(path) else None


def build_deck():
    fw = SlideFramework(lang="ja-en")

    # ============ オープニング（Part 0） ============

    # 1. 表紙
    fw.cover(
        title="鈴木研へようこそ：研究用OSのインストール",
        subtitle="Welcome to Suzuki-A. Lab — Installing the Research OS",
        event="SUZUKI-A. LAB ORIENTATION — DAY 1",
        affiliation="東北大学 流体科学研究所 鈴木杏奈研究室",
        name="UPDATE STARTING NOW — アップデートを開始します",
    )

    # 2. アジェンダ
    fw.agenda(
        items=[
            ("研究とは何か", "What is Research?"),
            ("研究は設計で進める", "Research as Design"),
            ("論文タイプと責任", "Paper Types & Responsibilities"),
            ("研究活動の5階層構造", "5 Layer Structure"),
            ("学年別の責任と計画", "Grade-Specific Goals"),
            ("必須習慣と文化", "Habits & Culture"),
        ],
        question="研究は「運」か？「設計」か？ — Luck or Design?",
    )

    # 3. 【冒頭宣言】Lab Policy — 最後に再掲する
    fw.key_message(
        "研究成果よりも、研究を通じて\nどう成長するかを重視する",
        supplement="Lab Policy — 最初に、いちばん大事なことから話す。"
                   "Results → Human Growth（人格形成）。研究は人格形成の装置。"
                   "今日の最後に、もう一度この話に戻る。",
    )

    # 4. 【冒頭宣言】Lab Values（詳細版）
    fw.cards_2x2(
        "Lab Values — 鈴木研の4つの価値",
        "すべての活動の判断基準。今日の話はすべて、この4つの実装である",
        [
            ("自己管理 / Self-management",
             "研究の主導権は自分にある。時間・計画・体調を自分で設計する。"
             "Research Log と Quarter Plan は自己管理の道具。"
             "管理されるのを待たない。"),
            ("誠実さ / Integrity",
             "データにも、人にも、自分にも正直であること。"
             "うまくいかない結果や停滞も隠さず共有する。"
             "「詰まって沈黙」は誠実さの反対。"),
            ("敬意 / Respect",
             "人・アイデア・時間への敬意。議論では Work（研究）を批判し、"
             "Peer（人）を攻撃しない。相手の時間を尊重した準備をして臨む。"),
            ("共創的探究 / Collective Inquiry",
             "研究は個人戦ではない。Paper Card・Inquiry Cycle という"
             "共通言語で、互いの探究を加速させる。文化は全員でつくる。"),
        ],
        takeaway="価値は貼り紙ではなく、日常の行動で示すもの",
    )

    # 5. 【冒頭宣言】文化は設計する
    fw.key_message(
        "文化は偶然ではない。設計する。",
        supplement="Research is Culture — 構造（Structure）→ 習慣（Habit）→ "
                   "文化（Culture）。今日インストールする「研究OS」は、"
                   "この文化の設計図である。",
    )

    # 6. Luck or Design?
    fw.problem_solution(
        "研究は「運」か？「設計」か？",
        "Luck or Design? — 受け身の研究と意図的な研究",
        problem_items=[
            "ひらめき待ち — Waiting for inspiration",
            "当てずっぽうの試行錯誤 — Trial and error only",
            "成果は運次第 — Results are random",
        ],
        solution_items=[
            "意図的な問い — Intentional Inquiry",
            "構造化された工程 — Structured Process",
            "再現性のある成果 — Reproducible results",
        ],
        problem_label="Luck / 運",
        solution_label="Design / 設計",
        takeaway="成果を運のせいにするのは、今日で終わり",
    )

    # 4. なぜ差が出るのか
    fw.two_column(
        "同じ時間を使っているのに、なぜ差が出るのか",
        "Why is there a gap? — The Lost vs The Focused",
        ("迷走 / The Lost", [
            "データはあるが、主張がない",
            "貢献が薄い — Low Contribution",
        ]),
        ("突破 / The Focused", [
            "問いの設計に命をかけている",
            "インパクトが大きい — High Impact",
        ]),
        takeaway="才能ではなく「型」の差 — It's not about Talent. It's the OS.",
    )

    # 5. データ先行の罠
    fw.steps_horizontal(
        "「データ先行」の罠：とりあえず実験、とりあえず計算",
        'The "Data-First" Trap',
        [
            ("データ取得", "Data — まずデータを集める"),
            ("とりあえず実験", "Exp / Sim — 意味は後で考える"),
            ("迷走", "Lost — 何を示したいのか分からなくなる"),
        ],
        takeaway="地図を持たずに森に入るような研究は、今日で終わり",
    )

    # 6. 新基準：鈴木研OS
    fw.cards_3(
        "新基準：鈴木研OS",
        "New Standard: Suzuki-A. Lab OS",
        [
            (img("iconmonstr-gear-11.png"), "体系化 / Systematization",
             "個人のセンスをシステムに置き換える。From talent-based to system-based."),
            (img("iconmonstr-speech-bubble-26.png"), "共通言語 / Common Language",
             "Paper Card・Inquiry Cycle。ラボメンバー全員の共通言語を持つ。"),
            (img("iconmonstr-redo-7.png"), "再現性 / Reproducibility",
             "誰でも高い品質の成果を再現できる。Anyone can achieve quality."),
        ],
        takeaway="目指すのは「圧倒的な再現性」",
    )

    # 7. Day 1 のゴール
    fw.key_message(
        "論文は成果ではない。\n「誤差」を受け取るための媒体である。",
        supplement="Day 1のゴール：研究への姿勢を揺らす — "
                   "「ズレ」を許容し、更新し続ける責任を受け取る",
    )

    # 8. Day 1 / Day 2
    fw.two_column(
        "Are you ready to update?",
        "オリエンテーションの全体構成",
        ("DAY 1：Soul / 思想", [
            "Philosophy — 哲学",
            "Expectations — 期待値",
            "Responsibility — 覚悟",
        ]),
        ("DAY 2：Action / 実践", [
            "Implementation — 実装",
            "Tools — 行動",
            "Practice — 再現性",
        ]),
        takeaway="混ぜると薄まる。今日はまず、思想から入る。",
    )

    # ============ SECTION 1：研究とは何か（Part 1） ============

    # 9. 章扉
    fw.section(1, "研究とは何か",
               "What is Research? — 答え集めではなく、探究である")

    # 10. 研究とは探究だ
    fw.key_message(
        "探究は「完了」しない。\n探究は「更新」され続ける。",
        supplement="Research is Inquiry — 締切がある仕事ではなく、永続する探究サイクル。"
                   "直線的なゴールはない（Research ≠ linear path）",
    )

    # 11. 研究の本質
    fw.before_after(
        "研究は答え集めではない。問いの精緻化である",
        "The Essence of Research",
        before_items=[
            "答えを積み上げる — Answer Pile",
            "最終答えを目指す",
        ],
        after_items=[
            "問いを研ぎ澄ます — **Refined Question**",
            "より精緻な、より良く枠づけられた問いへ",
        ],
        before_label="✕ Collecting answers",
        after_label="○ Refining questions",
        takeaway="ゴールは最終答えではなく、より精緻な問い",
    )

    # 12. 疑念から信念へ
    fw.steps_horizontal(
        "「疑念」を「信念」に変えるプロセス",
        "Inquiry: From Doubt to Belief",
        [
            ("Doubt / 疑念", "違和感 — \"Something feels off…\""),
            ("Inquiry Cycle", "Question → Hypothesis → Test を回し続ける"),
            ("Belief / 信念", "確率的・暫定的・更新可能"),
        ],
        takeaway="Inquiry Cycle ↺ — 問いを回し続ける",
    )

    # 13. Inquiry Cycle
    fw.steps_horizontal(
        "Inquiry Cycle：更新こそ本質",
        "Updating is the essence — \"Theory ≠ Observation\"",
        [
            ("ズレ・違和感", "misalignment"),
            ("Question", "問い"),
            ("Hypothesis", "仮説"),
            ("Test", "検証 — iterate"),
            ("Belief", "暫定的信念"),
        ],
        takeaway="Provisional Belief — always open to revision（常に更新に開かれている）",
    )

    # 14. ズレが始まり
    fw.two_column(
        "ズレが始まり — ズレが問いを生む",
        "Mismatch as a Beginning — The gap is the starting point",
        ("観測 ≠ 理解", [
            "Observation ≠ Understanding",
            "観測と理解のズレが問いを生む",
        ]),
        ("理想 ≠ 現実", [
            "Ideal ≠ Reality",
            "理想と現実のズレが問いを生む",
        ]),
        takeaway="GAP → Inquiry starts here — ズレこそ探究の出発点",
    )

    # 15. 認知も同じ構造
    fw.steps_horizontal(
        "認知も同じ構造 — 脳も誤差で自分を更新する",
        "Cognition and Inquiry — The brain works the same way",
        [
            ("Prediction / 予測", "脳は世界を予測する"),
            ("Error / 誤差", "予測と観測のズレを見つける"),
            ("Update / 更新", "自分自身を更新する"),
        ],
        takeaway="認知とInquiryは同じ構造を持つ — 自由エネルギー原理（K. Friston）",
    )

    # 16. 自由エネルギー原理
    fw.key_message(
        "脳は予測誤差（ズレ）を最小化しようとする",
        supplement="自由エネルギー原理（直感版）— 誤差が大きい → 不快感 → 行動・更新 ／ "
                   "誤差が小さい → 安定した信念。更新の先に精緻化された信念がある",
    )

    # 17. Beliefとは何か
    fw.cards_3(
        "Beliefは「正しさ」ではない。確率である",
        "What is a Belief? — Probability, not Truth",
        [
            (img("iconmonstr-time-20.png"), "常に暫定的",
             "Always provisional — 現時点の最良推定にすぎない。"),
            (img("iconmonstr-redo-7.png"), "常に更新可能",
             "Always updatable — 新しい証拠で書き換えられる。"),
            (img("iconmonstr-bar-chart-thin.png"), "証拠で強さが変わる",
             "Strength varies with evidence — 仮説空間の中の確率分布。"),
        ],
        takeaway="Most probable belief — 現時点の最良推定を持ち続ける",
    )

    # 18. 論文とは何か
    fw.key_message(
        "論文は、問いと信念を固定する媒体である",
        supplement="「最終答え」ではなく「現時点の最良信念のスナップショット」— "
                   "Doubt → Inquiry → Paper（Fixed Belief）",
    )

    # 19. 固定すると何が起こるか
    fw.steps_horizontal(
        "固定すると何が起こるか — なぜ出版するのか",
        "Consequences of Fixing — Why publishing matters",
        [
            ("Paper", "信念の固定 — \"This is our current best belief.\""),
            ("Critique", "批判可能になる — 査読・検証が可能になる"),
            ("Next Question", "次の探究へ — 論文が次の問いを生む"),
        ],
        takeaway="Each paper opens new inquiry cycles — 論文が次の問いを生む",
    )

    # 20. 探究としての責任
    fw.key_message(
        "論文とは、確率的信念を\n公共空間に提出すること",
        supplement="Inquiry as Responsibility — 研究は終わらない。更新し続ける。"
                   "\"A paper is a medium to receive Feedback & Error.\"",
    )

    # ============ SECTION 2：研究は設計で進める（Part 2/3） ============

    # 21. 章扉
    fw.section(2, "研究は設計で進める",
               "Research as Design — 研究が止まる理由は能力ではない。"
               "順番と構造の欠如である")

    # 22. 研究が止まる瞬間
    fw.key_message(
        "止まる原因はデータ不足ではない。\n方向性の欠如である。",
        supplement="Research Stagnation — データは増える。解析も進む。"
                   "でも、何を示したいのかが曖昧なまま（問い不在）",
    )

    # 23. 失敗パターン：データ先行
    fw.steps_horizontal(
        "失敗パターン：データ先行",
        "Failure Pattern: Data-First — Start with data, hope meaning emerges later",
        [
            ("とりあえず実験", "🧪 まず手を動かす"),
            ("とりあえず解析", "📊 出たデータを解析する"),
            ("あとで意味を考える", "❓ 方向なき探索 — 迷走のループ"),
        ],
        takeaway="これは設計ではない。探索の迷走。",
    )

    # 24. 正しい順番
    fw.steps_horizontal(
        "正しい順番：Framingが研究全体の設計図",
        "The Correct Order — Order is everything",
        [
            ("Idea", "アイデア"),
            ("Framing ★", "構造化 — KEY STEP。すべてはここから決まる"),
            ("Figures", "図の設計"),
            ("Draft", "執筆"),
        ],
        takeaway="順番がすべて — Everything downstream depends on Framing",
    )

    # 25. Framingとは何か
    fw.numbered_cards(
        "Framingとは何か",
        "What is Framing? — 書くのは3つだけ",
        [
            ("問いを1文で書く", "Core Question in 1 sentence"),
            ("先行研究との差分を明示する", "\"Compared to X, we Y.\""),
            ("貢献を最大3点に絞る", "Key contributions (3 max)"),
        ],
        takeaway="結果を書くな。手法を書くな。— Don't write results. Don't write methods.",
    )

    # 26. 曖昧な問い vs 構造化された問い
    fw.before_after(
        "Framingが弱いと、全て崩れる",
        "Weak framing = Total collapse",
        before_items=[
            "\"We studied X and found something interesting...\"",
            "何が新しいのか、条件は何かが不明",
        ],
        after_items=[
            "\"Compared to prior method X, our approach Y "
            "achieves **Z** under condition C.\"",
            "差分・成果・条件が1文で明確",
        ],
        before_label="✕ 曖昧な問い",
        after_label="○ 構造化された問い",
        takeaway="問いは「Compared to X, we Y」の型で言い切る",
    )

    # 27. 問いの型
    fw.table_compare(
        "良い研究の問いは、必ず「型」に収まる",
        "Question Archetypes — Every good research question fits a type",
        col_headers=["問いの型", "問いの形"],
        rows=[
            ["推定型 / Estimation", "How much / many?"],
            ["機構型 / Mechanism", "How / why does it work?"],
            ["妥当性型 / Validity", "Does method X work?"],
            ["不確実型 / Uncertainty", "What are the limits?"],
            ["スケール型 / Scale", "Does it scale?"],
            ["動態型 / Dynamics", "How does it change?"],
            ["設計型 / Design", "How should we build X?"],
        ],
        takeaway="型を選べない問いは曖昧 — Vague questions lack an archetype",
    )

    # 28. 設計としての研究
    fw.steps_vertical(
        "問いが決まると、必要なデータが決まる",
        "Research as Design — Question determines everything",
        [
            ("Question", "問い（確定）— 構造がデータを呼び込む"),
            ("Required Data", "必要なデータ — 問いから逆算される"),
            ("Method / Experiment", ("手法・実験", "データは後 — Data comes later.")),
        ],
        takeaway="✕ Data → Hope for meaning ／ ○ Question → Required Data",
    )

    # 29. 1図＝1主張
    fw.before_after(
        "1図＝1主張 — 図は説明ではない。主張そのものである",
        "Figures are arguments, not illustrations",
        before_items=[
            "1つの図に主張Aと主張Bを詰め込む",
            "何を読み取ればいいのか分からない",
        ],
        after_items=[
            "1つの図に主張は**1つ**",
            "主張Bは次の図へ — Claim B → next figure",
        ],
        before_label="BAD ✕",
        after_label="GOOD ○",
        takeaway="論文は図で読む — Read papers via figures first",
    )

    # 30. 構造が生産性を決める
    fw.two_column(
        "構造が生産性を決める — 能力差ではない。構造差である",
        "Structure Defines Productivity — It's architecture, not ability",
        ("High Structure", [
            "Framing → Figures → Draft → Submit",
            "設計の質が成果を決める",
        ]),
        ("Low Structure", [
            "Data → ??? → Repeat",
            "同じ時間でも成果が出ない",
        ]),
        takeaway="同じ時間投資でも、構造が違えば成果が変わる — OSの必要性に回帰",
    )

    # 31. Paper Card
    fw.numbered_cards(
        "Paper Card：構造を固定する装置",
        "Fix the Structure — 不確かなアイデア（Doubt）を確信ある設計（Belief）へ",
        [
            ("Core Question", "問いを1文で — 1 sentence"),
            ("Compared to X, we Y", "先行研究との差分の明示"),
            ("Key Contributions", "貢献は3点以内"),
            ("Main Figures (sketch)", "図の配置スケッチ"),
            ("Contribution Statement", "貢献の要約"),
        ],
        takeaway="Structure before data — No Card → No Paper",
    )

    # ============ SECTION 3：論文タイプと責任（Part 2.5） ============

    # 32. 章扉
    fw.section(3, "論文タイプと責任",
               "Paper Types & Responsibilities — 信念の形式は複数ある")

    # 33. 信念の形式は複数ある
    fw.key_message(
        "論文タイプは「格」ではない。\n信念のスコープが違うだけ。",
        supplement="Original / Review / Technical / Short — 横並び・上下関係なし。"
                   "Same \"belief,\" different zoom levels.",
    )

    # 34. 4つの基本形式
    fw.cards_2x2(
        "4つの基本形式",
        "Four Basic Formats",
        [
            ("Original", "新しい主張 — New Claim"),
            ("Review", "問いの再設計 — Reframing Questions"),
            ("Technical", "方法の提示 — Methodological"),
            ("Short", "限定的主張 — Limited Claim"),
        ],
        takeaway="形式は道具であって序列ではない — Formats are tools, not status",
    )

    # 35. 発表の場の違い
    fw.cards_3(
        "発表の場の違い — 片方の軸はスピード、片方は厳密さ",
        "Venues of Publication — Speed vs Verification",
        [
            (img("iconmonstr-speech-bubble-26.png"), "Conference",
             "議論を始める — Start a discussion。スピード重視。"),
            (img("iconmonstr-file-5.png"), "Journal",
             "厳密に検証する — Rigorous verification。厳密さ重視。"),
            (img("iconmonstr-school-27.png"), "Thesis",
             "統合された説明責任 — Integrated accountability。"),
        ],
        takeaway="場によって役割が違う。使い分ける。",
    )

    # 36. なぜJournalが必要か
    fw.key_message(
        "Thesisは内部責任。\nJournal は外部検証。",
        supplement="Why a Journal is Necessary — Inquiryは公共空間で完結する。"
                   "Lab → Scientific Community",
    )

    # 37. 研究フェーズと論文タイプ
    fw.steps_horizontal(
        "研究フェーズによって、出す論文タイプは変わる",
        "Research Phase and Paper Type",
        [
            ("探索 / Exploration", "Short・Technical で小さく固定する"),
            ("安定 / Stability", "Original で新しい主張を出す"),
            ("軸確立 / Establishment", "Review で問いを再設計する"),
        ],
        takeaway="博士は軸を持つ。その一つの形がReview。",
    )

    # 38. Thesisとは何か
    fw.key_message(
        "Thesisは枚数ではない。\n一貫した信念体系である。",
        supplement="A thesis is a coherent belief system — Paper 1 → Paper 2 → Paper 3 を"
                   "つなぐ Research Arc。詳細は Quarter Plan で説明",
    )

    # 39. 形式から選ぶな
    fw.steps_horizontal(
        "形式から選ぶな。問いから選べ。",
        "Don't Choose by Format — Choose from your Question",
        [
            ("Question", "問い — MAP（地図）を持つ"),
            ("Format", "形式 — 問いに合う形式を選ぶ"),
            ("Venue", "発表の場 — 最後に場を決める"),
        ],
        takeaway="Question → Format → Venue — 順番が逆だと、だいたい迷う",
    )

    # 40. 研究倫理
    fw.cards_3(
        "倫理とは、信念を出す資格の条件である",
        "What is Research Ethics? — Ethics as the Foundation of Belief",
        [
            (img("iconmonstr-shield-28.png"), "Data Integrity",
             "データの誠実さ・再現性 — Reproducibility。"),
            (img("iconmonstr-copyright-5.png"), "Attribution",
             "帰属・引用の明示 — 誰の貢献かを正しく示す。"),
            (img("iconmonstr-glasses-3.png"), "Transparency",
             "透明性 — 検証できる形で開示する。"),
        ],
        takeaway="論文は「検証可能な信念」を倫理的に提出する行為 — Claim・Ethics・Verify",
    )

    # ============ SECTION 4：研究活動の5階層構造（Part 4） ============

    # 41. 章扉
    fw.section(4, "研究活動の5階層構造",
               "5 Layer Structure — Strategic Organization of Lab Activities")

    # 42. 5つの階層
    fw.numbered_cards(
        "研究活動は5つの階層で設計されている",
        "The 5 Layers",
        [
            ("Lab Forum", "価値を磨く場 — Value Refinement Space"),
            ("Team Meeting", "判断の場 — Tactical Decision Space"),
            ("Student Interaction", "自律の訓練場 — Autonomy Training Space"),
            ("Individual Meeting", "軸合わせの場 — Identity Alignment Space"),
            ("Individual Work", "研究が進む唯一の場所 — The Only Place Research Moves"),
        ],
        takeaway="それぞれ役割が違う。混ぜない。",
    )

    # 43. ①〜④の役割
    fw.icon_list(
        "4つのミーティング、4つの役割",
        "Layers ① – ④",
        [
            (img("iconmonstr-idea-11.png"), "① Lab Forum — 研究のWhyを磨く場",
             "価値と位置づけを磨く。多様な視点からの建設的懐疑と哲学的深掘り。"),
            (img("iconmonstr-target-4.png"), "② Team Meeting — 研究を前に進める判断の場",
             "Paper Card → 判断 → 次のアクション"),
            (img("iconmonstr-networking-7.png"), "③ 学生だけの相互作用 — 自律の訓練",
             "技術相談・言語化トレーニング・プレレビュー"),
            (img("iconmonstr-user-21.png"), "④ Individual Meeting — 研究軸の確認",
             "成長方向の確認・キャリア設計。技術判断や原稿の細部修正には**使わない**。"),
        ],
    )

    # 44. 判断の場と壁打ちの場
    fw.two_column(
        "判断の場と、壁打ちの場",
        "Decisions vs Sparring — Idea → Framing → Figures → Draft → Submission",
        ("Team Meeting = Decision", [
            "GO / NO-GO を決める",
            "次のフェーズに進むか、戻るかの判断",
        ]),
        ("Lab Forum = Sparring", [
            "壁打ち：問い・立場・表現を壊して磨く",
            "結論を出す場ではない",
        ]),
        takeaway="フェーズを進めるのは判断、磨くのは壁打ち",
    )

    # 45. Individual Work
    fw.key_message(
        "研究はミーティングでは進まない。\n個人作業で進む。",
        supplement="⑤ Individual Work — 必須習慣：Daily Research Log ／ Weekly Paper Card ／ "
                   "Monthly Core Question。Meeting is for alignment. Work is for progress.",
    )

    # 46. Core Principle
    fw.cards_2x2(
        "Core Principle — 4つの場の使い分け",
        "何のための場かを、常に意識する",
        [
            ("Team Meeting", "戦術 — Tactical Decision"),
            ("Lab Forum", "価値 — Value Refinement"),
            ("Individual Meeting", "軸 — Identity Alignment"),
            ("Individual Work", "前進 — Progress"),
        ],
        takeaway="場の目的を混ぜない — それが5階層構造の運用ルール",
    )

    # ============ SECTION 5：学年別の責任と計画（Part 5） ============

    # 47. 章扉
    fw.section(5, "学年別の責任と計画",
               "Academic Responsibility & Grade-Specific Goals")

    # 48. 二軸モデル
    fw.key_message(
        "責任が増えるほど、自由も増える",
        supplement="責任の二軸モデル — 横軸：研究責任（Research Responsibility）／ "
                   "縦軸：共同体責任（Community Responsibility）。B4 → M → PhD と右上へ",
    )

    # 49. 学年別の責任
    fw.cards_3(
        "学年別の責任",
        "B4 / Master / PhD — それぞれの責任",
        [
            (img("iconmonstr-rocket-20.png"), "B4：経験と誠実さ",
             "研究を1周回す。結果も苦労も誠実に共有する。"
             "完璧はいらない。回すことが責任。"),
            (img("iconmonstr-flag-18.png"), "修士：完走と後輩支援",
             "Original 1本投稿。B4を支え導く。完走する責任。"),
            (img("iconmonstr-award-11.png"), "博士：軸の定義と文化",
             "独自の研究軸を定義する。ラボの文化を守り育てる。"
             "軸確立の一つの形がReview。"),
        ],
        takeaway="More responsibility brings more freedom",
    )

    # 50. 期待値は明示する
    fw.kpi_3(
        "期待値は明示する",
        "Clear Expectations — This is NOT optional. This is the baseline.",
        [
            ("1周完走", "B4", "研究サイクルを1周、経験しきる"),
            ("Original 1本", "Master", "筆頭論文を1本投稿する"),
            ("軸 ＋ 文化", "PhD", "研究軸の定義と、文化の継承"),
        ],
        takeaway="これはオプションではない。ベースラインである。",
    )

    # 51. Quarter Plan
    fw.two_column(
        "Quarter Plan：進捗報告ではなく、思考構造の可視化",
        "Structural Reflection — 設計は90日単位で行う",
        ("何をするか", [
            "戦略は四半期（90日）単位で設計する",
            "Research Arc（1年）を Q1〜Q4 に分割する",
            "進捗報告ではなく、思考構造の可視化",
        ]),
        ("なぜ90日か", [
            "研究は長距離走。設計は短距離で行う",
            "B4のゴールは完璧ではなく「1周の経験」",
            "短い区間なら、構造のズレにすぐ気づける",
        ]),
        takeaway="Strategy is quarterly — 長距離走を短距離の設計で走る",
    )

    # 52. Identity Snapshot
    fw.key_message(
        "動く前に、現在地を特定する",
        supplement="Identity Snapshot — YOU ARE HERE。"
                   "曖昧な現在地では、前進は設計できない。",
    )

    # 53. B4の1年
    fw.steps_vertical(
        "B4の1年：締切からの逆算",
        "Back-calculation — 研究だけやっていればいい年ではない。外的イベントが研究を圧迫する",
        [
            ("Q1 4-6月", "テーマ固定 — カリキュラム（授業）と並走する"),
            ("Q2 7-9月", "Framing — 院試・就活が研究を圧迫する時期"),
            ("Q3 10-12月", "Figures — 図を確定させる"),
            ("Q4 1-2月", ("卒論まとめ", "Thesis 提出 — Research Arc 1周完走")),
        ],
        takeaway="APR → FEB：外的イベントから逆算して設計する",
    )

    # 54. B4の崩れパターン
    fw.numbered_cards(
        "B4の典型的な崩れパターン",
        "B4 Failure Patterns",
        [
            ("院試で停止", "Stalled by Graduate Exams"),
            ("詰まって沈黙", "Silence when stuck"),
            ("完成待ちで共有しない", "Waiting for \"perfection\" to share"),
            ("全部同時進行で崩壊", "Total collapse from multi-tasking"),
        ],
        takeaway="Quarter Plan はこれを防ぐための装置",
    )

    # 55. 評価項目とArcの一致
    fw.numbered_cards(
        "評価は結果ではない。構造的思考の副産物である",
        "Evaluation Criteria — What is evaluated",
        [
            ("理解度", "Understanding"),
            ("論理的発表力", "Logical Presentation"),
            ("質疑応答", "Q&A performance"),
            ("資料構造", "Document structure"),
        ],
        takeaway="Complete the ARC → Skills will follow — Arcを完走すればスキルは付いてくる",
    )

    # 56. 修士の2年間
    fw.two_column(
        "修士2年間は「拡張されたArc」である",
        "The Extended Arc — 勝負はM1で決まる",
        ("M1：探索と設計", [
            "Exploration & Strategy（Design）",
            "Framingに集中する",
            "M1中盤に「**Axis fixed**」— 軸を固定する",
        ]),
        ("M2：収束と完走", [
            "Convergence & Completion",
            "加速区間 — Acceleration",
            "M2で焦る人は、M1で設計していない",
        ]),
        takeaway="Focus on Framing in M1. Fix your Axis.",
    )

    # 57. M2の現実
    fw.steps_horizontal(
        "修士2年目の現実：時間は急に消える",
        "Reality of M2",
        [
            ("9月", "Draft — 初稿"),
            ("11月", "Mid-term — 中間発表"),
            ("1月", "Deadline — 提出締切"),
        ],
        takeaway="Time disappears suddenly — だからM1で設計する",
    )

    # 58. 博士3年間
    fw.steps_vertical(
        "博士3年間の構造：作る・広げる・統合する",
        "PhD: Axis Construction (3 Years)",
        [
            ("D1：軸を作る", "Axis Construction — Review Paper（仮説の外部化）"),
            ("D2：拡張する", "Original Expansion — 手法深化・独立性"),
            ("D3：統合する", ("Integration & Positioning", "Thesis の構造設計")),
        ],
        takeaway="\"Axis-less PhDs will drift.\" — 軸がない博士は漂流する",
    )

    # ============ SECTION 6：必須習慣と文化（Part 6） ============

    # 59. 章扉
    fw.section(6, "必須習慣と文化",
               "Research Habits & Culture — 研究は「日常」で進む")

    # 60. 必須習慣
    fw.numbered_cards(
        "研究の差は「才能」ではなく「日常の密度」",
        "Essential Habits — 日常を積み重ねるのは、あなた",
        [
            ("Research Log & Thinking Log", "毎日 — Every day"),
            ("Paper Card（Paper Board）", "毎週 — 主張を更新し続ける"),
            ("Team Meeting / Lab Forum", "定例 — 判断と壁打ち"),
            ("Individual Meeting", "定期 — 軸の確認"),
            ("Quarter Plan", "90日 — 構造の可視化"),
        ],
        takeaway="Research moves through daily practice",
    )

    # 61. Research Log と Thinking Log
    fw.two_column(
        "Research Log と Thinking Log",
        "What is Research & Thinking Log?",
        ("Research Log", [
            "今日、**何をやったか**",
            "Facts — 事実を記録する",
        ]),
        ("Thinking Log", [
            "今日、**何を考えたか**",
            "Interpretation — 解釈を記録する",
        ]),
        takeaway="Research progresses through: Fact → Interpretation",
    )

    # 62. なぜ記録するのか
    fw.steps_horizontal(
        "思考は脳の外で起こる — 研究は記憶ではなく外部記録で進む",
        "Why Log? — Thinking happens outside the brain",
        [
            ("Brain / 頭", "考えたことは消える"),
            ("Note / 記録", "外部に書き出す"),
            ("Update / 思考更新", "記録を見て思考が進む"),
        ],
        takeaway="書かない人間は必ず同じ失敗を繰り返す",
    )

    # 63. 記録の方法
    fw.numbered_cards(
        "記録の方法",
        "How to Log — Log → Paper Arc",
        [
            ("毎日1回書く", "One entry every day"),
            ("完璧は不要", "No need for perfection"),
            ("仮説・事実・解釈を書く", "Hypotheses, Facts & Interpretation"),
        ],
        takeaway="書くことで研究が前に進む — デモは来週",
    )

    # 【再掲】Lab Policy — 冒頭の約束に戻る
    fw.key_message(
        "研究成果よりも、研究を通じて\nどう成長するかを重視する",
        supplement="Lab Policy（再掲）— 冒頭の約束に戻る。"
                   "Results → Human Growth（人格形成）。研究は人格形成の装置。",
    )

    # 【再掲】Lab Values（詳細版）— 明日からの行動基準
    fw.cards_2x2(
        "Lab Values — もう一度、いちばん大事なこと",
        "明日からの行動基準として。今日の話はすべて、この4つの実装だった",
        [
            ("自己管理 / Self-management",
             "研究の主導権は自分にある。時間・計画・体調を自分で設計する。"
             "Research Log と Quarter Plan は自己管理の道具。"
             "管理されるのを待たない。"),
            ("誠実さ / Integrity",
             "データにも、人にも、自分にも正直であること。"
             "うまくいかない結果や停滞も隠さず共有する。"
             "「詰まって沈黙」は誠実さの反対。"),
            ("敬意 / Respect",
             "人・アイデア・時間への敬意。議論では Work（研究）を批判し、"
             "Peer（人）を攻撃しない。相手の時間を尊重した準備をして臨む。"),
            ("共創的探究 / Collective Inquiry",
             "研究は個人戦ではない。Paper Card・Inquiry Cycle という"
             "共通言語で、互いの探究を加速させる。文化は全員でつくる。"),
        ],
        takeaway="価値は貼り紙ではなく、日常の行動で示すもの",
    )

    # 【再掲】研究は文化である
    fw.key_message(
        "文化は偶然ではない。設計する。",
        supplement="Research is Culture（再掲）— 構造（Structure）→ "
                   "習慣（Habit）→ 文化（Culture）。今日話したすべては、"
                   "この文化を設計するための部品である。",
    )

    # 67. 結び
    fw.closing(
        "Are you ready to update?",
        sub="研究用OSのインストールは完了 — あとは毎日、更新し続けるだけ",
        contact="質問・相談はいつでも：Lab Forum / Team Meeting / Individual Meeting",
    )

    out = fw.save(os.path.join(OUTPUT_DIR, "lab_orientation_day1.pptx"))
    print("Saved:", out, "| slides:", fw._page)


if __name__ == "__main__":
    build_deck()
