"""
build_orientation_slides_en.py — Suzuki-A. Lab Orientation Day 1 (English)

English edition of build_orientation_slides.py (same 70-slide structure).

Structure note (mirrors the Japanese deck):
  - Lab Policy / Lab Values / "Culture is designed" are declared right
    after the agenda (opening declaration), and reprised at the end
    (P67-69) before the closing slide.
  - Lab Values uses the detailed 4-card version in both places.

Fonts (per Anna's request — no Avenir Next Heavy):
  headings / bold : Avenir Next Bold   (plain "Avenir" has no Bold face)
  body / caption  : Avenir Book
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import slide_framework as sf
from slide_framework import SlideFramework

# Latin font override for the "en" mode (must be set before instantiation)
sf._LATIN_FOR_EN = {
    sf.FONT_HEAVY: "Avenir Next Bold",
    sf.FONT_BOLD:  "Avenir Next Bold",
    sf.FONT_BODY:  "Avenir Book",
    sf.FONT_LIGHT: "Avenir Book",
}

IMG_DIR = os.path.join(os.path.dirname(__file__), "images", "png")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def img(filename):
    path = os.path.join(IMG_DIR, filename)
    return path if os.path.exists(path) else None


def build_deck():
    fw = SlideFramework(lang="en")

    # ============ Opening (Part 0) ============

    # 1. Cover
    fw.cover(
        title=["Welcome to Suzuki-A. Lab:", "Installing the Research OS"],
        subtitle="Research runs on design, not luck",
        event="SUZUKI-A. LAB ORIENTATION — DAY 1",
        affiliation="Suzuki-A. Laboratory, Institute of Fluid Science, "
                    "Tohoku University",
        name="UPDATE STARTING NOW",
    )

    # 2. Agenda
    fw.agenda(
        items=[
            ("What is Research?", "Part 1"),
            ("Research as Design", "Part 2"),
            ("Paper Types & Responsibilities", "Part 3"),
            ("The 5-Layer Structure", "Part 4"),
            ("Grade-Specific Goals", "Part 5"),
            ("Habits & Culture", "Part 6"),
        ],
        question="Is research Luck — or Design?",
        title="Today's Agenda",
        question_label="TODAY'S QUESTION",
    )

    # 3. [Opening declaration] Lab Policy — reprised at the end
    fw.key_message(
        "We value who you become through research\n"
        "more than the results",
        supplement="Lab Policy — we start with what matters most. "
                   "Results → Human Growth. Research is a device for "
                   "character building. We will come back to this "
                   "at the very end of today.",
    )

    # 4. [Opening declaration] Lab Values (detailed version)
    fw.cards_2x2(
        "Lab Values — the four values of Suzuki-A. Lab",
        "The criteria behind every activity. Everything today is an "
        "implementation of these four",
        [
            ("Self-management",
             "Ownership of your research is yours. Design your own "
             "time, plans, and health. The Research Log and Quarter "
             "Plan are tools of self-management. Don't wait to be "
             "managed."),
            ("Integrity",
             "Be honest with the data, with people, and with yourself. "
             "Share unsuccessful results and stagnation openly. "
             "\"Silence when stuck\" is the opposite of integrity."),
            ("Respect",
             "Respect for people, ideas, and time. In discussion, "
             "critique the Work — never attack the Peer. Come "
             "prepared, out of respect for others' time."),
            ("Collective Inquiry",
             "Research is not a solo game. Paper Card and Inquiry "
             "Cycle form a common language that accelerates each "
             "other's inquiry. Culture is built by everyone."),
        ],
        takeaway="Values are shown in daily actions, not on posters",
    )

    # 5. [Opening declaration] Culture is designed
    fw.key_message(
        "Culture is not accidental.\nIt is designed.",
        supplement="Research is Culture — Structure → Habit → Culture. "
                   "The \"Research OS\" we install today is the "
                   "blueprint of this culture.",
    )

    # 6. Luck or Design?
    fw.problem_solution(
        "Is research Luck — or Design?",
        "Passive research vs intentional research",
        problem_items=[
            "Waiting for inspiration",
            "Trial and error only",
            "Results are random",
        ],
        solution_items=[
            "Intentional inquiry",
            "Structured process",
            "Reproducible results",
        ],
        problem_label="Luck",
        solution_label="Design",
        takeaway="Blaming luck for your results ends today",
    )

    # 4. Why is there a gap?
    fw.two_column(
        "Same hours, different outcomes — why?",
        "The Lost vs The Focused",
        ("The Lost", [
            "Data without a claim",
            "Low contribution",
        ]),
        ("The Focused", [
            "They live and die by question design",
            "High impact",
        ]),
        takeaway="It's not about Talent. It's the OS.",
    )

    # 5. The Data-First trap
    fw.steps_horizontal(
        "The \"Data-First\" trap: experiments first, meaning later",
        "How research quietly goes off the rails",
        [
            ("Collect data", "Gather data first, without a question"),
            ("Just run it", "Exp / Sim — figure out the meaning later"),
            ("Get lost", "No direction, no claim — wandering"),
        ],
        takeaway="Entering the forest without a map ends today",
    )

    # 6. New standard: Suzuki-A. Lab OS
    fw.cards_3(
        "The new standard: Suzuki-A. Lab OS",
        "From talent-based to system-based",
        [
            (img("iconmonstr-gear-11.png"), "Systematization",
             "Replace individual sense with a system anyone can run."),
            (img("iconmonstr-speech-bubble-26.png"), "Common Language",
             "Paper Card, Inquiry Cycle — one vocabulary for every "
             "lab member."),
            (img("iconmonstr-redo-7.png"), "Reproducibility",
             "Anyone can reproduce high-quality outcomes."),
        ],
        takeaway="Aiming for overwhelming reproducibility",
    )

    # 7. Goal of Day 1
    fw.key_message(
        "A paper is not the end result.\n"
        "It is a medium to receive \"error\".",
        supplement="Goal of Day 1: shake your attitude toward research — "
                   "accept the gap, and take on the responsibility of "
                   "continuous updating",
    )

    # 8. Day 1 / Day 2
    fw.two_column(
        "Are you ready to update?",
        "How this orientation is structured",
        ("DAY 1: Soul", [
            "Philosophy",
            "Expectations",
            "Responsibility",
        ]),
        ("DAY 2: Action", [
            "Implementation",
            "Tools",
            "Practice",
        ]),
        takeaway="Mixing dilutes. Today, we start with the soul.",
    )

    # ============ SECTION 1: What is Research? ============

    # 9. Divider
    fw.section(1, "What is Research?",
               "Inquiry — not answer collection")

    # 10. Research is Inquiry
    fw.key_message(
        "Inquiry is never \"finished\".\nIt keeps being updated.",
        supplement="Research is Inquiry — not a project with a deadline, "
                   "but a living, iterative cycle. There is no linear goal "
                   "(Research ≠ linear path)",
    )

    # 11. The essence of research
    fw.before_after(
        "Research is not collecting answers — it refines questions",
        "The Essence of Research",
        before_items=[
            "Piling up answers — Answer Pile",
            "Aiming for a final answer",
        ],
        after_items=[
            "Sharpening the question — **Refined Question**",
            "Toward a sharper, better-framed question",
        ],
        before_label="✕ Collecting answers",
        after_label="○ Refining questions",
        takeaway="The goal is not a final answer — it is a sharper question",
    )

    # 12. From Doubt to Belief
    fw.steps_horizontal(
        "Inquiry turns doubt into belief",
        "From Doubt to Belief",
        [
            ("Doubt", "\"Something feels off…\""),
            ("Inquiry Cycle", "Question → Hypothesis → Test, "
             "again and again"),
            ("Belief", "Probabilistic, provisional, updatable"),
        ],
        takeaway="Keep the Inquiry Cycle turning ↺",
    )

    # 13. Inquiry Cycle
    fw.steps_horizontal(
        "Inquiry Cycle: updating is the essence",
        "\"Theory ≠ Observation\"",
        [
            ("Misalignment", "A sense that something is off"),
            ("Question", "Frame it"),
            ("Hypothesis", "Commit to a guess"),
            ("Test", "Iterate"),
            ("Belief", "Provisional"),
        ],
        takeaway="Provisional Belief — always open to revision",
    )

    # 14. Mismatch as a beginning
    fw.two_column(
        "Mismatch is the beginning — the gap generates inquiry",
        "The gap is the starting point",
        ("Observation ≠ Understanding", [
            "The gap between what we observe and what we understand "
            "generates questions",
        ]),
        ("Ideal ≠ Reality", [
            "The gap between the ideal and the real "
            "generates questions",
        ]),
        takeaway="GAP → Inquiry starts here",
    )

    # 15. Cognition and Inquiry
    fw.steps_horizontal(
        "Cognition shares the same structure",
        "The brain works the same way",
        [
            ("Prediction", "The brain predicts the world"),
            ("Error", "It detects the mismatch with observation"),
            ("Update", "It updates itself"),
        ],
        takeaway="Cognition and Inquiry share one structure — "
                 "Free Energy Principle (K. Friston)",
    )

    # 16. Free Energy Principle
    fw.key_message(
        "The brain strives to minimize prediction error",
        supplement="Free Energy Principle (intuitive version) — "
                   "large error → discomfort → action & update ／ "
                   "small error → stable belief. Beyond the update lies "
                   "a refined belief",
    )

    # 17. What is a Belief?
    fw.cards_3(
        "Belief is not \"Truth\". It is Probability.",
        "What is a Belief?",
        [
            (img("iconmonstr-time-20.png"), "Always provisional",
             "The best estimate at this moment — nothing more."),
            (img("iconmonstr-redo-7.png"), "Always updatable",
             "New evidence rewrites it."),
            (img("iconmonstr-bar-chart-thin.png"),
             "Strength varies with evidence",
             "A probability distribution over hypothesis space."),
        ],
        takeaway="Hold the most probable belief — and keep updating it",
    )

    # 18. What is a research paper?
    fw.key_message(
        "A paper is a medium that fixes\nquestions and beliefs",
        supplement="Not a \"final answer\" — a snapshot of the best belief "
                   "at this moment. Doubt → Inquiry → Paper (Fixed Belief)",
    )

    # 19. Consequences of fixing
    fw.steps_horizontal(
        "What happens when you fix a belief — why publishing matters",
        "Consequences of Fixing",
        [
            ("Paper", "Fixing the belief — \"This is our current "
             "best belief.\""),
            ("Critique", "Peers can challenge, test, and verify"),
            ("Next Question", "On to the next inquiry"),
        ],
        takeaway="Each paper opens new inquiry cycles",
    )

    # 20. Inquiry as responsibility
    fw.key_message(
        "Inquiry is submitting provisional belief\nfor public update",
        supplement="Inquiry as Responsibility — research never ends; "
                   "it keeps updating. \"A paper is a medium to receive "
                   "Feedback & Error.\"",
    )

    # ============ SECTION 2: Research as Design ============

    # 21. Divider
    fw.section(2, "Research as Design",
               "Research stops not because of lack of ability, "
               "but because of lack of order and structure")

    # 22. Research stagnation
    fw.key_message(
        "Research stalls not from lack of data,\n"
        "but from lack of direction",
        supplement="Research Stagnation — data increases, analysis "
                   "proceeds, but what you want to show stays vague "
                   "(no question)",
    )

    # 23. Failure pattern: Data-First
    fw.steps_horizontal(
        "Failure pattern: Data-First",
        "Start with data. Hope meaning emerges later.",
        [
            ("Just experiment", "🧪 Move your hands first"),
            ("Just analyze", "📊 Analyze whatever came out"),
            ("Meaning later", "❓ Exploration without direction — "
             "the wandering loop"),
        ],
        takeaway="This is not design. This is wandering.",
    )

    # 24. The correct order
    fw.steps_horizontal(
        "The correct order: Framing is the blueprint",
        "Order is everything",
        [
            ("Idea", "Where it starts"),
            ("Framing ★", "KEY STEP — everything downstream "
             "depends on it"),
            ("Figures", "Design the figures"),
            ("Draft", "Write"),
        ],
        takeaway="Order is everything — Framing is the blueprint of "
                 "your research",
    )

    # 25. What is Framing?
    fw.numbered_cards(
        "What is Framing?",
        "Only three things to write",
        [
            ("Core Question in one sentence", None),
            ("State the difference: \"Compared to X, we Y.\"", None),
            ("Key contributions — three at most", None),
        ],
        takeaway="Don't write results. Don't write methods.",
    )

    # 26. Vague vs structured question
    fw.before_after(
        "Weak framing = total collapse",
        "The same study, two questions",
        before_items=[
            "\"We studied X and found something interesting...\"",
            "What's new? Under what conditions? Unclear.",
        ],
        after_items=[
            "\"Compared to prior method X, our approach Y achieves "
            "**Z** under condition C.\"",
            "Difference, result, and condition — all in one sentence",
        ],
        before_label="✕ Vague question",
        after_label="○ Structured question",
        takeaway="State your question in the \"Compared to X, we Y\" form",
    )

    # 27. Question archetypes
    fw.table_compare(
        "Every good research question fits a type",
        "Question Archetypes",
        col_headers=["Archetype", "Form of the question"],
        rows=[
            ["Estimation", "How much / many?"],
            ["Mechanism", "How / why does it work?"],
            ["Validity", "Does method X work?"],
            ["Uncertainty", "What are the limits?"],
            ["Scale", "Does it scale?"],
            ["Dynamics", "How does it change?"],
            ["Design", "How should we build X?"],
        ],
        takeaway="A question that cannot choose an archetype is vague",
    )

    # 28. Research as design
    fw.steps_vertical(
        "Once the question is fixed, the required data is decided",
        "Question determines everything — data follows structure",
        [
            ("Question", "Fixed first — structure calls in the data"),
            ("Required Data", "Back-calculated from the question"),
            ("Method / Experiment",
             ("Methods and experiments", "Data comes later.")),
        ],
        takeaway="✕ Data → hope for meaning ／ "
                 "○ Question → required data",
    )

    # 29. 1 figure = 1 claim
    fw.before_after(
        "1 figure = 1 claim — figures are the claim itself",
        "Figures are arguments, not illustrations",
        before_items=[
            "Claim A and Claim B crammed into one figure",
            "Readers can't tell what to take away",
        ],
        after_items=[
            "**One** claim per figure",
            "Claim B goes to the next figure",
        ],
        before_label="BAD ✕",
        after_label="GOOD ○",
        takeaway="Read papers via figures first",
    )

    # 30. Structure defines productivity
    fw.two_column(
        "Structure defines productivity — not ability",
        "It's architecture, not talent",
        ("High Structure", [
            "Framing → Figures → Draft → Submit",
            "Design quality determines output",
        ]),
        ("Low Structure", [
            "Data → ??? → Repeat",
            "Same hours, no output",
        ]),
        takeaway="Same time investment, different output — "
                 "back to why we need an OS",
    )

    # 31. Paper Card
    fw.numbered_cards(
        "Paper Card: the device that fixes structure",
        "From uncertain idea (Doubt) to confident design (Belief)",
        [
            ("Core Question", "One sentence"),
            ("Compared to X, we Y", "State the difference from prior work"),
            ("Key Contributions", "Three at most"),
            ("Main Figures (sketch)", "Layout of the figures"),
            ("Contribution Statement", "Summary of the contribution"),
        ],
        takeaway="Structure before data — No Card → No Paper",
    )

    # ============ SECTION 3: Paper Types & Responsibilities ============

    # 32. Divider
    fw.section(3, "Paper Types & Responsibilities",
               "Belief takes multiple forms")

    # 33. Multiple forms of belief
    fw.key_message(
        "Paper types are not ranks.\n"
        "They differ only in scope of belief.",
        supplement="Original / Review / Technical / Short — equal "
                   "standing, no hierarchy. Same \"belief\", "
                   "different zoom levels.",
    )

    # 34. Four basic formats
    fw.cards_2x2(
        "Four basic formats",
        "Four ways to fix a belief",
        [
            ("Original", "A new claim"),
            ("Review", "Reframing the questions"),
            ("Technical", "Methodological"),
            ("Short", "A limited claim"),
        ],
        takeaway="Formats are tools, not status",
    )

    # 35. Venues of publication
    fw.cards_3(
        "Venues differ: one axis is speed, the other is rigor",
        "Venues of Publication",
        [
            (img("iconmonstr-speech-bubble-26.png"), "Conference",
             "Start a discussion. Speed first."),
            (img("iconmonstr-file-5.png"), "Journal",
             "Rigorous verification. Rigor first."),
            (img("iconmonstr-school-27.png"), "Thesis",
             "Integrated accountability."),
        ],
        takeaway="Different venues, different roles — use them accordingly",
    )

    # 36. Why a journal is necessary
    fw.key_message(
        "A thesis is internal accountability.\n"
        "A journal is external verification.",
        supplement="Why a journal is necessary — Inquiry completes in "
                   "public space. Lab → Scientific Community",
    )

    # 37. Research phase and paper type
    fw.steps_horizontal(
        "The paper type follows the research phase",
        "Research Phase and Paper Type",
        [
            ("Exploration", "Fix small pieces with Short / Technical"),
            ("Stability", "Put out new claims with Original"),
            ("Establishment", "Redesign the questions with a Review"),
        ],
        takeaway="A PhD holds an axis — a Review is one form of it",
    )

    # 38. What is a thesis?
    fw.key_message(
        "A thesis is not a page count.\n"
        "It is a coherent belief system.",
        supplement="Paper 1 → Paper 2 → Paper 3, connected into a "
                   "Research Arc — details in the Quarter Plan",
    )

    # 39. Don't choose by format
    fw.steps_horizontal(
        "Don't choose by format. Choose from your question.",
        "The map-like order",
        [
            ("Question", "Hold the map"),
            ("Format", "Pick the format that fits the question"),
            ("Venue", "Decide the venue last"),
        ],
        takeaway="Question → Format → Venue — reverse the order and "
                 "you get lost",
    )

    # 40. Research ethics
    fw.cards_3(
        "Ethics is the qualification for submitting belief",
        "What is Research Ethics? — Ethics as the Foundation of Belief",
        [
            (img("iconmonstr-shield-28.png"), "Data Integrity",
             "Honest data and reproducibility."),
            (img("iconmonstr-copyright-5.png"), "Attribution",
             "Credit and citation — show whose contribution it is."),
            (img("iconmonstr-glasses-3.png"), "Transparency",
             "Disclose in a verifiable form."),
        ],
        takeaway="A paper is an ethically submitted, verifiable belief — "
                 "Claim, Ethics, Verify",
    )

    # ============ SECTION 4: The 5-Layer Structure ============

    # 41. Divider
    fw.section(4, "The 5-Layer Structure",
               "Strategic organization of lab activities")

    # 42. The five layers
    fw.numbered_cards(
        "Lab activities are designed in five layers",
        "The 5 Layers",
        [
            ("Lab Forum", "Value refinement space"),
            ("Team Meeting", "Tactical decision space"),
            ("Student Interaction", "Autonomy training space"),
            ("Individual Meeting", "Identity alignment space"),
            ("Individual Work", "The only place research moves"),
        ],
        takeaway="Each layer has its own role. Don't mix them.",
    )

    # 43. Layers 1–4
    fw.icon_list(
        "Four meetings, four roles",
        "Layers 1 – 4",
        [
            (img("iconmonstr-idea-11.png"),
             "1. Lab Forum — where we polish the Why",
             "Refine value and positioning. Constructive doubt and "
             "philosophical deep dives from diverse perspectives."),
            (img("iconmonstr-target-4.png"),
             "2. Team Meeting — decisions that move research forward",
             "Paper Card → decision → next action"),
            (img("iconmonstr-networking-7.png"),
             "3. Student-only interaction — autonomy training",
             "Technical consultation, verbalization training, pre-review"),
            (img("iconmonstr-user-21.png"),
             "4. Individual Meeting — confirming your research axis",
             "Growth direction and career design. **Not** for technical "
             "details or minor manuscript edits."),
        ],
    )

    # 44. Decisions vs sparring
    fw.two_column(
        "The place for decisions, the place for sparring",
        "Idea → Framing → Figures → Draft → Submission",
        ("Team Meeting = Decision", [
            "Decides GO / NO-GO",
            "Move to the next phase, or go back",
        ]),
        ("Lab Forum = Sparring", [
            "Break and polish questions, positions, expressions",
            "Not a place for conclusions",
        ]),
        takeaway="Decisions move the phases; sparring polishes them",
    )

    # 45. Individual Work
    fw.key_message(
        "Research doesn't move in meetings.\nIt moves at your desk.",
        supplement="5. Individual Work — required habits: daily Research "
                   "Log ／ weekly Paper Card ／ monthly Core Question. "
                   "Meeting is for alignment. Work is for progress.",
    )

    # 46. Core principle
    fw.cards_2x2(
        "Core Principle — four places, four purposes",
        "Always know what each place is for",
        [
            ("Team Meeting", "Tactics — Tactical Decision"),
            ("Lab Forum", "Value — Value Refinement"),
            ("Individual Meeting", "Axis — Identity Alignment"),
            ("Individual Work", "Progress"),
        ],
        takeaway="Never mix the purposes — that is how the five "
                 "layers run",
    )

    # ============ SECTION 5: Grade-Specific Goals ============

    # 47. Divider
    fw.section(5, "Grade-Specific Goals",
               "Academic responsibility & grade-specific goals")

    # 48. Dual-axis model
    fw.key_message(
        "More responsibility brings more freedom",
        supplement="Dual-axis model — horizontal: research responsibility "
                   "／ vertical: community responsibility. "
                   "B4 → Master → PhD moves toward the upper right",
    )

    # 49. Responsibilities by grade
    fw.cards_3(
        "Responsibilities by grade",
        "B4 / Master / PhD",
        [
            (img("iconmonstr-rocket-20.png"), "B4: Experience & Honesty",
             "Run one full research cycle. Share results and struggles "
             "honestly. Completion over perfection."),
            (img("iconmonstr-flag-18.png"),
             "Master: Completion & Mentorship",
             "Submit one Original article. Support and guide the B4s. "
             "The responsibility to finish the race."),
            (img("iconmonstr-award-11.png"), "PhD: Definition & Culture",
             "Define a unique research axis. Protect and evolve the lab "
             "culture. A Review is one way to establish the axis."),
        ],
        takeaway="Grow along both axes — research and community",
    )

    # 50. Clear expectations
    fw.kpi_3(
        "Expectations are explicit",
        "Clear Expectations — This is NOT optional. This is the baseline.",
        [
            ("1 full cycle", "B4",
             "Experience the whole research cycle once"),
            ("1 Original", "Master",
             "Submit one first-author paper"),
            ("Axis + Culture", "PhD",
             "Define the axis, carry the culture"),
        ],
        takeaway="Baseline, not stretch goals",
    )

    # 51. Quarter Plan
    fw.two_column(
        "Quarter Plan: not a progress report — structural visualization",
        "Structural Reflection — design in 90-day units",
        ("What it is", [
            "Strategy designed in 90-day quarters",
            "The one-year Research Arc split into Q1–Q4",
            "A visualization of your thinking structure",
        ]),
        ("Why 90 days", [
            "Research is a marathon; design in sprints",
            "For B4, the goal is one full cycle, not perfection",
            "Short spans expose structural drift early",
        ]),
        takeaway="Strategy is quarterly — run the marathon on "
                 "sprint-sized designs",
    )

    # 52. Identity Snapshot
    fw.key_message(
        "Locate yourself before moving",
        supplement="Identity Snapshot — YOU ARE HERE. Forward progress "
                   "cannot be designed from a vague location.",
    )

    # 53. The B4 year
    fw.steps_vertical(
        "The B4 year: back-calculate from the deadlines",
        "Not a year of research only — external events squeeze research",
        [
            ("Q1 Apr–Jun", "Fix the theme — in parallel with coursework"),
            ("Q2 Jul–Sep", "Framing — entrance exams and job hunting "
             "squeeze research"),
            ("Q3 Oct–Dec", "Figures — finalize the figures"),
            ("Q4 Jan–Feb",
             ("Thesis wrap-up",
              "Submit the thesis — one full Research Arc completed")),
        ],
        takeaway="APR → FEB: design backwards from the external events",
    )

    # 54. B4 failure patterns
    fw.numbered_cards(
        "Typical B4 failure patterns",
        "B4 Failure Patterns",
        [
            ("Stalled by graduate entrance exams", None),
            ("Silence when stuck", None),
            ("Waiting for \"perfection\" to share", None),
            ("Total collapse from multi-tasking", None),
        ],
        takeaway="The Quarter Plan exists to prevent exactly this",
    )

    # 55. Evaluation criteria
    fw.numbered_cards(
        "Evaluation is a by-product of structural thinking",
        "Evaluation Criteria — what is evaluated",
        [
            ("Understanding", None),
            ("Logical presentation", None),
            ("Q&A performance", None),
            ("Document structure", None),
        ],
        takeaway="Complete the Arc → skills will follow",
    )

    # 56. The Master's two years
    fw.two_column(
        "The Master's two years are an extended Arc",
        "The race is decided in M1",
        ("M1: Exploration & Design", [
            "Exploration and strategy",
            "Focus on Framing",
            "**Axis fixed** by mid-M1",
        ]),
        ("M2: Convergence & Completion", [
            "The acceleration zone",
            "Those who panic in M2 didn't design in M1",
        ]),
        takeaway="Focus on Framing in M1. Fix your Axis.",
    )

    # 57. Reality of M2
    fw.steps_horizontal(
        "The reality of M2: time disappears suddenly",
        "Reality of M2",
        [
            ("SEP", "Draft"),
            ("NOV", "Mid-term presentation"),
            ("JAN", "Submission deadline"),
        ],
        takeaway="Time disappears suddenly — that is why you design in M1",
    )

    # 58. The PhD's three years
    fw.steps_vertical(
        "The PhD's three years: build, expand, integrate",
        "PhD: Axis Construction (3 Years)",
        [
            ("D1: Build the axis",
             "Axis construction — Review paper "
             "(externalize the hypothesis)"),
            ("D2: Expand",
             "Original expansion — deepen methods, gain independence"),
            ("D3: Integrate",
             ("Integration & positioning",
              "Structural design of the thesis")),
        ],
        takeaway="\"Axis-less PhDs will drift.\"",
    )

    # ============ SECTION 6: Habits & Culture ============

    # 59. Divider
    fw.section(6, "Essential Habits & Culture",
               "Research moves through daily practice")

    # 60. Essential habits
    fw.numbered_cards(
        "The difference is not talent — it is the density of "
        "daily routine",
        "Essential Habits — you are the one who accumulates the days",
        [
            ("Research Log & Thinking Log", "Every day"),
            ("Paper Card (Paper Board)",
             "Every week — keep updating the claim"),
            ("Team Meeting / Lab Forum",
             "Regular — decisions and sparring"),
            ("Individual Meeting", "Periodic — axis check"),
            ("Quarter Plan", "Every 90 days — structural visualization"),
        ],
        takeaway="Research moves through daily practice",
    )

    # 61. Research Log and Thinking Log
    fw.two_column(
        "Research Log and Thinking Log",
        "What is the Research & Thinking Log?",
        ("Research Log", [
            "**What you did** today",
            "Facts",
        ]),
        ("Thinking Log", [
            "**What you thought** today",
            "Interpretation",
        ]),
        takeaway="Research progresses through: Fact → Interpretation",
    )

    # 62. Why log?
    fw.steps_horizontal(
        "Thinking happens outside the brain",
        "Why log? — research runs on external records, not memory",
        [
            ("Brain", "Thoughts evaporate"),
            ("Note", "Write them down, outside"),
            ("Update", "Records drive the next thought"),
        ],
        takeaway="Those who do not write repeat the same mistakes",
    )

    # 63. How to log
    fw.numbered_cards(
        "How to log",
        "Log → Paper Arc",
        [
            ("One entry every day", None),
            ("No need for perfection", None),
            ("Write hypotheses, facts & interpretation", None),
        ],
        takeaway="Writing drives the research forward — demo next week",
    )

    # 67. [Reprise] Lab Policy — back to the opening promise
    fw.key_message(
        "We value who you become through research\n"
        "more than the results",
        supplement="Lab Policy (reprise) — back to the promise we made "
                   "at the start. Results → Human Growth. Research is "
                   "a device for character building.",
    )

    # 68. [Reprise] Lab Values (detailed version) — how to act from tomorrow
    fw.cards_2x2(
        "Lab Values — once more, what matters most",
        "Your standard of action from tomorrow. Everything today was an "
        "implementation of these four",
        [
            ("Self-management",
             "Ownership of your research is yours. Design your own "
             "time, plans, and health. The Research Log and Quarter "
             "Plan are tools of self-management. Don't wait to be "
             "managed."),
            ("Integrity",
             "Be honest with the data, with people, and with yourself. "
             "Share unsuccessful results and stagnation openly. "
             "\"Silence when stuck\" is the opposite of integrity."),
            ("Respect",
             "Respect for people, ideas, and time. In discussion, "
             "critique the Work — never attack the Peer. Come "
             "prepared, out of respect for others' time."),
            ("Collective Inquiry",
             "Research is not a solo game. Paper Card and Inquiry "
             "Cycle form a common language that accelerates each "
             "other's inquiry. Culture is built by everyone."),
        ],
        takeaway="Values are shown in daily actions, not on posters",
    )

    # 69. [Reprise] Research is culture
    fw.key_message(
        "Culture is not accidental.\nIt is designed.",
        supplement="Research is Culture (reprise) — Structure → Habit → "
                   "Culture. Everything we discussed today is a "
                   "component for designing this culture.",
    )

    # 70. Closing
    fw.closing(
        "Are you ready to update?",
        sub="The Research OS is installed — now keep updating, every day",
        contact="Questions anytime: Lab Forum / Team Meeting / "
                "Individual Meeting",
    )

    out = fw.save(os.path.join(OUTPUT_DIR, "lab_orientation_day1_en.pptx"))
    print("Saved:", out, "| slides:", fw._page)


if __name__ == "__main__":
    build_deck()
