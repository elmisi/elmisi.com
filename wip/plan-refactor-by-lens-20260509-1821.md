# Plan: Blog article — "Where to Look, Not What to Change" (Series 1, #4)

## Context

A new blog article for `https://elmisi.com`, fourth in the "AI workflow / compass" series. Narrates the user's track trying to use Claude (and Codex) for refactoring on a client codebase he can't name, and the realization that came out of it.

The arc:

1. Asked Claude to propose refactorings → disappointing.
2. Realized he hadn't told Claude what "good code" means to him → tried "industry best practices" → disappointing.
3. Wrote out his own personal criteria of beautiful code → still disappointing. Claude kept missing things he could see at a glance: similar functions under different names, repeated patterns, functions that wrap one call and could go.
4. Realized the request itself was wrong: a list of *actions to perform* never produces the interesting items, only the surface ones.
5. Reframed: don't ask for actions, ask for *places worth investigating*.
6. Gave Claude a set of "ways of looking at the code" — eight angles to inspect against, each one producing leads with evidence; the human does the judgment.
7. Output started being good. (More refinement to come.)

The eight ways of looking and the triage they feed into are implemented in the `refactor-discovery` skill, repo at `https://github.com/elmisi/claude-code-automation/tree/main/plugins/refactor-discovery`. The methodology behind it (verified by reading `~/.claude/plugins/cache/elmisi/refactor-discovery/1.1.0/docs/methodology.md`):

- **Pinned commit + pass ID** — stable evidence anchors.
- **Per-area investigation** with parallel subagents.
- **Eight ways of looking**: temporal coupling, change amplification, shotgun ceremony, semantic drift, asymmetric abstractions, hidden policy, test gravity, negative space.
- **Four-state triage**: smell lead (`SL`), refactor candidate (`R`), research task (`RT`), document-intent (`DI`).
- **"Why" gate** before promoting any lead to a candidate.
- **Discipline of preserving uncertainty** — do not flatten leads into advice.

Series 1 published articles (verified by reading each file in `src/content/blog/`):

1. `claude-code-retrospective` (2026-03-25) — Claude knew the map but not the compass.
2. `self-improving-tools` (2026-04-04) — building tools that keep the compass accurate via feedback loops.
3. `npm-install-intelligence` (2026-04-30) — skills look like prose but behave like software.

This new article is **#4** in Series 1. The footer of `npm-install-intelligence` self-identifies as "Third article in an unplanned series" (`src/content/blog/npm-install-intelligence.md` line 122), confirming the count.

The point of the article: in tasks where the interesting output requires judgment in context, asking the agent for actions produces shallow output; asking it for candidates with evidence produces a workable input for human judgment. Refactoring is the case study; the article is reflective in tone — close to "thinking out loud" — not a checklist.

### Style fingerprint (verified against the three published Series 1 articles)

- **Italic kicker line** below the title repeating/extending the description.
- **First-person, present-tense narrative** — the realization is staged, not summarized up front.
- **Concrete objects to anchor the opening** — published articles open with countable things (77 projects, 21 tests, a CI job, 22 memory files). The new article opens on a prompt and a result.
- **Slightly rough English** — short sentences, contractions, no academic vocabulary.
- **Reflective register, not technical-essay register** — per the user: "è più un articolo quasi filosofico, quasi di pensieri tra me e me." Keep the technical content sparse and the reasoning visible.
- **Section headers as story beats** — H2s mark moments of realization, not topic taxonomies.
- **Footer with series link** — "Nth in an unplanned series" pointing to siblings.

### Vocabulary discipline

Two lists apply during drafting and the final pass:

1. *Standing list* (from `~/.claude/projects/-home-alessandro-elmisi-elmisi-com/memory/feedback_writing_style.md`): avoid "hand-waving", "compounds" (metaphorical), "measurably", "systematically", "nagging", "leverage" (verb), "robust" (metaphorical).
2. *Soft-watch list specific to this article*: avoid words that sound like a writing assistant explaining the essay from outside. These are fine in this plan but must not appear in the final prose: "epiphany", "failure-driven", "methodological", "artefact" / "artifact", "device" (in the meta sense), "foreground" (verb), "demote" (metaphorical). Replace with user-shaped phrasing: "the part that changed", "the method", "the tool", "the reason it worked", "what I was really asking for".

Length target: ~3,000 words. Reference points: `self-improving-tools` 1,750 words, `npm-install-intelligence` 2,400 words, `claude-code-retrospective` 1,400 words. The reflective tone tolerates more wandering, but not at the cost of focus.

## How to work with this plan

Read the entire plan before acting. Context, approach, edge cases, and open questions are all load-bearing.

For operational instructions (how to annotate, review, finalize): see the companion file `plan-refactor-by-lens-20260509-1821.ops.md` in the same directory.

## Approach

The article narrates the user's track in first person: "I noticed X, then Y was weird, then it clicked." The lesson is not announced upfront — it arrives only after the concrete failures have been described. The reader walks the same staircase the user walked.

Three structures were considered:

- **A. Pure chronological narrative.** Strength: matches the user's voice. Risk: gets repetitive — multiple "still disappointing" beats read as whining.
- **B. Two-act structure** ("the wrong question" / "the right question"). Strength: punchy. Risk: collapses the gradient of failures, which is where the insight lives.
- **C. Chronological with an explicit pivot.** Narrate failures 1-3 quickly, dwell on the pivot moment, then unpack the alternative with one example. **Chosen.** Keeps the user's voice and the staircase, but compresses the early failures so the realization isn't preceded by tedium.

The pivot sentence is load-bearing. It must be direct and in the user's voice, not abstract. Working version (refine during draft, do not rewrite into something more polished):

> *I was asking Claude to give me the answer. What I needed was a map of where to look.*

The article must not read as marketing for `refactor-discovery`. The skill is named once in the body (without an inline link) and linked once in the footer block at the end. This matches the user's choice in the open-question pass: *"nominata e se vuoi linkata (magari al fondo)."*

The point of the article is about the *kind of output* you should ask for in a class of tasks where human judgment must remain in the loop: refactoring is the case study; the same shape probably helps for code review, architecture review, security review. The agent's job is to surface candidates with evidence; the verdict is the user's.

## Detailed Changes

### File to create

`src/content/blog/where-to-look-not-what-to-change.md`. Slug derived from the confirmed title.

Convention from `CLAUDE.md`: blog articles live in `src/content/blog/` as markdown with frontmatter; the Astro content collection picks them up automatically. The site URL is hardcoded as `https://elmisi.com`. No code changes elsewhere.

### Files NOT to touch

- `articles/` — confirmed WIP/scratch folder by the user. Do not drop a copy there.
- `astro.config.mjs`, `src/layouts/*`, `src/pages/blog/*` — no structural changes needed; the content collection auto-discovers the new file.

### Frontmatter (final)

```yaml
---
title: "Where to Look, Not What to Change"
date: 2026-05-09
description: "Why asking Claude for refactorings kept producing surface-level answers, and what changed when I asked it to find places worth investigating."
tags: ["claude-code", "ai", "refactoring", "workflow", "code-quality"]
---
```

Tag rationale: matches conventions from prior articles (`claude-code`, `ai`, `workflow` are recurring across Series 1; `refactoring` and `code-quality` are new and topic-specific).

### Article skeleton — section by section

Each section below specifies its **purpose**, **target length**, **key beats**, and **what NOT to do**. Word counts are approximate and additive to ~3,000.

#### Italic kicker (below title, ~25 words)

```
*Why I stopped asking Claude for refactorings and started asking it
for places worth investigating.*

---
```

#### §1 — "I asked Claude to suggest refactorings" (~250 words)

**Purpose:** open in the user's voice, on a concrete prompt-and-result moment. Like prior articles, anchor on a countable thing — not a broad summary.

**Project framing:** the user is working on a client codebase he can't name. Reference it neutrally as *"a codebase I've been working on"* or *"the code I had open"*. Do not name the client, project, or domain. Keep the **shape** concrete (size, kind of code) only if it can be described without identifying detail. If even that risks identification, stay generic.

**Beats:**
- Open with a prompt-and-result moment in the user's voice. Working draft (refine, do not over-polish): *"I asked: find refactorings in this repo. It gave me ten items. Eight were true. None mattered."*
- The kind of items the list contained: rename a variable, extract a small helper, split a 200-line function. All "correct," all surface.
- The kind of items it *didn't* contain: a function that could disappear entirely, two modules doing the same thing under different names, a policy hidden in three switch statements.
- The thought at the end of the section: *"what's missing isn't refactorings — it's the ones I'd actually do."*

**Avoid:**
- Naming the client codebase, the domain, or any identifying detail.
- Ranting at the model. The article's argument depends on the user being fair to the tool.

#### §2 — "Maybe it doesn't know what *good* means to me" (~300 words)

**Purpose:** stage the first wrong fix. The user assumes the gap is taste — Claude doesn't know what good code is *to him* — so he tries to teach it.

**Beats:**
- Pass 1: asks Claude to refactor "according to clean code best practices" — the kind any senior reviewer would invoke. Result: longer list, same surface character. SOLID-shaped renames, "extract method", a few "consider an interface here". Still no mention of the items the user could see at a glance.
- Pass 2: writes out **his own** criteria of beautiful code, in his own rough vocabulary — a short list, not a manifesto. Final list (4-5 bullets, in the same plain register, no expansion):
  - *code I can delete*
  - *a name that removes a whole comment*
  - *one place that owns the decision*
  - *no theatre around errors*
  - *(one more if it lands in the same register; otherwise stop at four)*
- The point isn't to argue for these criteria. The point is that even with them in hand, Claude still missed the same kind of items.
- Repeat the same observation: duplicated patterns under different names, functions that wrap one call and could go, dead branches.
- End on the dissonance: *"the criteria are clear, the code is in front of it, and still I don't see the items I'd see myself."*

**Avoid:** turning into "what is good code", which is a different essay. The criteria are a list, not an argument; the article moves on as soon as they fail to unlock the missing items. Hard cap: 6 bullets. If the list grows past that, cut everything except the bullets and one sentence saying "even with these, the same things were missed."

#### §3 — The pivot: "Where to look, not what to change" (~400 words)

**Purpose:** the realization. This is the load-bearing section — the rest of the article depends on it being a clear, complete shift. The section heading reuses the title language so the reader feels the article landing where it promised it would.

**Beats:**
- Name the pattern in the disappointment: the items he *wanted* aren't items the agent can decide. "Function F can disappear" requires understanding what F is for in the broader system, who calls it, what would break, and whether the abstraction it carries has weight elsewhere. That's not a refactoring — that's a judgment.
- The pivot, in the user's words: *"I was asking Claude to give me the answer. What I needed was a map of where to look."*
- The reframe: a list of actions only ever surfaces items where the action itself is the answer (rename, extract, split). The interesting items aren't actions — they're signals worth chasing. The agent can find the signal. The judgment is mine.
- A short principle, distilled in the same plain register: *the agent is good at breadth; I'm good at judgment in context. When I ask it for actions, I'm asking it to do my job. When I ask it for signals, I'm asking it to do its job.*
- Tie back to article 1 ("the compass") in one sentence. This is another instance of "every session started without knowing how I think" — but the fix isn't a memory file, it's a different shape of output.

**Avoid:** abstracting too early. The realization should arrive concrete: §1-2 showed what was missing; §3 names what *kind* of thing was missing; only then does the alternative follow.

**Quality test:** if a reader can summarize the article without using the words *"actions vs. signals"* or *"where to look"*, this section needs more weight.

#### §4 — "Ways of looking at the code" (~550 words)

**Purpose:** describe the alternative. Concrete, not promotional. Reflective tone, not skill-README tone — per the user, the article is "quasi filosofico, quasi di pensieri tra me e me", so the technical content is sparse and the reasoning is visible.

**Vocabulary note:** the word "lenses" sounds like a framework name if used too much. Introduce it once, then mostly say *"ways of looking at the code"* or *"questions I ask the code"*. Hard cap on the word "lens"/"lenses" combined: 3 occurrences in this section.

**Beats:**
- Introduce the idea: instead of "give me a list of refactorings", "look at the code through these eight angles and tell me what each one flags as suspicious."
- Walk through 3-4 of the eight with one-line examples each. Use these (verified in `~/.claude/plugins/cache/elmisi/refactor-discovery/1.1.0/docs/methodology.md`):
  - **Temporal coupling** — files that change together repeatedly without a code dependency. Often a hidden policy.
  - **Change amplification** — a small conceptual change requires edits in many places. Often a missing name or owner.
  - **Shotgun ceremony** — the same mental sequence (parse, validate, map, register) repeats across many sites.
  - **Semantic drift** — names, comments, tests, and behaviour disagree.
  - Mention the other four in one line each: asymmetric abstractions, hidden policy, test gravity, negative space.
- The output of each one is a *smell lead*, not a refactor. A lead has: a label, a one-line "why is this suspicious", a piece of evidence quoted from the code, and a *promotion condition* — the thing that would turn it into an actionable candidate.
- The four-state triage in plain language (introduce IDs only when the example needs them, in plain English first):
  - **smell lead** — interesting tension, judgment still pending
  - **refactor candidate** — promoted after the "why" check
  - **research task** — needs evidence the agent can't see locally
  - **document-intent** — leave the code, just add a comment that captures the load-bearing intent
- Mention the discipline that makes the output trustworthy, in one short sentence each: each lead is anchored to a pinned commit SHA with file:line evidence; universal claims ("nothing else uses this") require an enumeration; duplication claims require a behaviour diff, not a visual one.
- Name the skill once, in passing, with no link in the body: *"I eventually put this into a skill called refactor-discovery — the link is at the end of the post."* No more than one short paragraph (~40 words). Then back to what changed in the output.

**Avoid:**
- Reading like a skill README.
- Listing all eight angles with equal weight. Three or four with examples beats eight in a table.
- Repeating "lens" / "lenses" so often the article starts to sound like a framework being marketed (cap: 3).
- Inline GitHub link to the skill — the link goes in the footer.

**Quality test:** if §4 has more than 250 words with no concrete file/function reference (even synthetic, marked), rewrite around one example.

#### §5 — "What changed in the output" (~250 words)

**Purpose:** show the difference, with one concrete contrast. This is the payoff for the reader. Reflective tone, not benchmark tone — keep it light per the user's note ("non esagerare, è più un articolo quasi filosofico").

**Synthetic-example discipline:** the user has no real example to share (client codebase). Use one synthetic example, marked plainly as illustrative. The opening word "Imagine" or "Picture" makes this explicit. Do not write "I saw" or "in the project". Working frame:

> *Imagine a validation flow repeated in seven handlers, each with the same four steps in slightly different order. The action-list approach surfaces it as "rename `data` to `userData` in handler 3". The new approach surfaces it as: "validation logic appears in 7 sites with the same 4-step ceremony but no name. Suspicion: a missing named policy. Promotion condition: confirm the four steps mean the same thing in all seven sites."*

**Beats:**
- The synthetic before/after pair, exactly as framed above (or a tighter version of it).
- The difference isn't quality of writing — it's *what's pointed at*.
- Note: the new approach also surfaces the boring renames, but as low-priority items. The interesting items are now visible *and* triaged.
- Honest caveat: this is not "Claude is now good at refactoring." It's that the failure mode of action-listing has been swapped for a different, smaller failure mode: this approach misses things outside the eight pre-defined angles. Worth saying explicitly.

**Avoid:** pretending the synthetic example was real. One illustrative example only — do not stack two or three.

#### §6 — "Where else this might apply" (~300 words)

**Purpose:** lift to the broader idea that ties the article into Series 1 — but framed as a hypothesis, not a claim. The user's tone is stronger when he separates what he saw from what he infers.

**Beats:**
- The pattern, framed as a suspicion: *"I suspect this is true for any task where the interesting output requires judgment in context."* Refactoring is the one I've run the loop on. The same shape might help for code review, architectural review, security review, library selection — places where asking the agent for a verdict produces shallow verdicts, and asking it to surface candidates with evidence produces a workable input for human judgment.
- Why this matters more than it looks: the default phrasing of every prompt nudges the agent toward a verdict ("propose...", "fix...", "what should I...?"). The verdict-shaped output is the cheap output. The candidate-shaped output is the expensive but useful one. You have to ask for it explicitly.
- One sentence connecting to the previous articles in the series: this is the same arc one more time. The agent isn't bad at refactoring. The default ask is wrong for this class of problem. Once the ask matches the work, the output is usable.

**Avoid:**
- "This applies to..." phrasing. Use *"I suspect"*, *"the same shape might help"*, *"this might generalize to"*.
- Turning into a recipe or checklist. The article is one example I've run, not a method to apply everywhere.

#### §7 — "Where I am" (~150 words)

**Purpose:** modest closing. Match the rhythm of `self-improving-tools` ("Where I am") and `npm-install-intelligence` ("Where I am"). Both end with "it works for me, it doesn't yet scale, here's what I'm still figuring out." End on one compact sentence with the rhythm of `claude-code-retrospective`'s closing line *"My memory files documented the world. But they didn't document my compass."*

**Beats:**
- The new approach is working, with the obvious limitation: the eight angles are mine, refined from a few real passes. They're not exhaustive. New work will surface ones I haven't named yet.
- One open question, flagged but not answered: is the right move to keep adding more angles, or to add a meta-question — *"what's a structural smell I haven't given a name to?"*
- Land on one compact sentence in the user's voice. Working version (refine during draft, do not over-polish): *"I don't need Claude to decide the refactoring. I need it to show me where my judgment is worth spending."*

#### Closing footer (~50 words)

```
---

*Fourth article in an unplanned series. The
[first](/blog/claude-code-retrospective) was about discovering that Claude
knew the map but not the compass. The
[second](/blog/self-improving-tools) was about building tools that keep
the compass accurate. The
[third](/blog/npm-install-intelligence) was about realizing those tools
are software. This one is about the kind of output you should ask for
when the work is judgment in context.*

*The skill mentioned in §4: [refactor-discovery on
GitHub](https://github.com/elmisi/claude-code-automation/tree/main/plugins/refactor-discovery).*
```

The skill link lives only in the footer (per the user's choice). It does not appear inline in §4.

Verified internal links (read each file in `src/content/blog/`):
- `/blog/claude-code-retrospective` → `src/content/blog/claude-code-retrospective.md` ✓
- `/blog/self-improving-tools` → `src/content/blog/self-improving-tools.md` ✓
- `/blog/npm-install-intelligence` → `src/content/blog/npm-install-intelligence.md` ✓

External link to verify before publish: `https://github.com/elmisi/claude-code-automation/tree/main/plugins/refactor-discovery` (T6 covers this).

### Cross-references and consistency

- The article must not contradict the framing of prior articles. Verified by reading `src/content/blog/claude-code-retrospective.md`: the user's quoted volume is "80% of plans don't satisfy me" — the new article is about a *different* class of bad output (refactoring lists), not contradicting that earlier framing.
- `self-improving-tools` introduces `plan-cycle` and `takeaway`. This article introduces `refactor-discovery`. Same pattern — name the tool only as the embodiment of the realization, link once (in this article's case, only in the footer).
- `npm-install-intelligence` already established the skills-as-software framing. This article doesn't need to re-explain it; one sentence of nod is enough.

## Edge Cases and Risks

### R1 — Risk: article reads as "ad" for refactor-discovery

- **Likelihood:** medium. The skill is a real tool the user built, and articles in this series do name their tools.
- **Impact:** the user's voice is "I noticed something, here's what I did, here's what I learned" — not "use my plugin". A promotional cast undermines the reader's trust and the series' tone.
- **Mitigation (concrete):** the skill is named exactly once in the body, in §4 (~40-word paragraph, no inline link). The GitHub link appears once, in the footer block. No mention of the skill in §1, §2, §3, §5, §6, or §7. Cap on skill-mechanics word count across the whole article: 80 words.
- **Exit clause:** if a draft has the skill mentioned more than once in the body, or with an inline GitHub link, cut every mention except the §4 one.

### R2 — Risk: §2 turns into "what is good code"

- **Likelihood:** high. The user has strong opinions and the natural pull is to make the case for them.
- **Impact:** dilutes the actual point (the criteria don't matter — even good ones didn't fix the failure mode). Adds 1,000 words, costs the article its argument.
- **Mitigation (concrete):** the personal criteria appear as a list of 4-5 bullets in §2, in rough vocabulary, with no expansion paragraphs. The article moves on as soon as the bullets are listed.
- **Exit clause:** if the criteria list grows past 6 bullets or any bullet has an expansion paragraph, cut everything except the bullets and one sentence saying "even with these, the same things were missed."

### R3 — Risk: chronology becomes repetitive

- **Likelihood:** medium-high. The user's track has 4-5 failures before the pivot.
- **Impact:** a reader gives up before §3.
- **Mitigation (concrete):** structure C compresses §1-2 into two failures with accelerating beats; the third "still bad" is the pivot itself, not a fourth instance.
- **Exit clause:** if a draft has more than two "still disappointing" beats before §3, rewrite §1-2 as a single section.

### R4 — Risk: technical jargon overload in §4

- **Likelihood:** medium. The vocabulary around the eight angles is dense (`SL<N>`, "why gate", "promoted candidate", "document-intent"...).
- **Impact:** Series 1 readers are not all skill-system experts. The reflective tone ("quasi filosofico") cannot survive a vocabulary dump.
- **Mitigation (concrete):** introduce IDs once, in plain English first ("smell lead", "refactor candidate"), use abbreviations only when an example requires them. Skip `RT` and `DI` abbreviations entirely in the body. Say "ways of looking at the code" / "questions I ask the code" more than "lenses" — hard cap of 3 on the word "lens"/"lenses" in §4.
- **Exit clause:** if §4 has more than 6 distinct technical labels (lens names + ID abbreviations + jargon nouns), cut to the four named lenses and the four-state triage in plain English only.

### R5 — Risk: the "this generalizes to..." section overreaches

- **Likelihood:** medium. The broader pattern is *the* point — but it's also the easiest place to overstate.
- **Impact:** undermines trust if §6 claims more than the user has evidence for.
- **Mitigation (concrete):** §6 names other domains where the pattern *might* apply (code review, security review, architecture review, library selection) — not domains where the user has run the same loop. The phrasing must be "I suspect" / "the same shape might help" / "this might generalize to" — never "this applies to".
- **Exit clause:** if any sentence in §6 makes a claim without one of the hedge phrases, rewrite that sentence with a hedge.

### R6 — Risk: writing-assistant vocabulary leaks into the prose

- **Likelihood:** medium. This plan itself uses "epiphany", "methodological", "foreground", "demote", "device", "artefact/artifact". Fine in a plan; not fine in the final prose.
- **Impact:** the article stops sounding like the user and starts sounding like a writing assistant explaining the user's experience from outside.
- **Mitigation (concrete):** during the final pass, grep the draft for both lists:
  - Standing list: `hand-waving`, `compounds`, `measurably`, `systematically`, `nagging`, `leverage`, `robust` (metaphorical uses).
  - Soft-watch list: `epiphany`, `failure-driven`, `methodological`, `artefact`, `artifact`, `device`, `foreground`, `demote`.
  - Replace with user-shaped phrasing: "the part that changed", "the method", "the tool", "the reason it worked", "what I was really asking for".
- **Exit clause:** any flagged word in the draft = rewrite that sentence. No exceptions.

### R7 — Risk: client codebase identifying detail leaks into §1

- **Likelihood:** low-to-medium. The opening pulls toward a concrete project, and the user is currently working on a client codebase he can't name.
- **Impact:** confidentiality breach with the client.
- **Mitigation (concrete):** §1 references the codebase neutrally ("a codebase I've been working on" / "the code I had open"). No domain, no language, no framework, no service name, no business detail. Concrete shape (size, file count) only if it can be stated without identifying detail; otherwise stay generic.
- **Exit clause:** if a reviewer can guess the client or domain from §1, strip every concrete detail and rebuild the section around the prompt-and-result moment alone.

## Failure Modes and Degradation

### Failure: the user disagrees with structure C after seeing a draft

- **Symptom:** annotation in §"Approach" or §3 saying "this isn't how I want to tell it".
- **Degraded behaviour:** swap to structure A (pure chronology) or structure B (two-act). The §-level skeleton can be rearranged without rewriting most paragraphs — beats are independent of the order they appear in.
- **Cost:** ~1 hour of restructuring; no information lost.
- **Threshold:** if structure choice changes more than once in a single review pass, ask for a one-line description of the *reading experience* the user wants, then rebuild from that.

### Failure: the article reads like a recap of self-improving-tools

- **Symptom:** reviewer says "this is just self-improving-tools again."
- **Degraded behaviour:** the article shares Series 1 DNA — that's intentional, not a defect. But if the *content* is genuinely a recap, the article fails. Reinforce §3: the actions-vs-signals distinction is the load-bearing original idea. If §3 is weak, the article is weak.
- **Threshold:** if a reviewer can summarize the article without using the words "actions vs. signals" or "where to look", §3 needs more weight.

### Failure: §4 is abstract or technical-essay-shaped

- **Symptom:** §4 reads like a methodology summary, not a reflection. Examples sound right but a reader can't picture the code.
- **Degraded behaviour:** swap to one fully worked synthetic example — pick one of the four named angles (e.g., shotgun ceremony) and show suspicion + evidence shape + promotion condition in the user's reflective voice. Better one concrete worked example than four abstract ones.
- **Threshold:** if §4 has more than 250 words with no concrete file/function reference (even synthetic, marked), rewrite around one example.

### Failure: writing style drifts to polished English

- **Symptom:** flagged words appear in the draft (both lists in R6).
- **Degraded behaviour:** during the final pass, grep the draft for the flagged words and replace with the user's substitutions. Keep contractions. Re-read sentences that feel "too smooth" and roughen them.
- **Threshold:** any flagged word = rewrite that sentence.

### Failure: client identifying detail in §1 (post-draft)

- **Symptom:** §1 contains a specific framework, language, domain, or scale that could identify the client codebase.
- **Degraded behaviour:** strip the detail down to the prompt-and-result moment alone. The opening still works without the project shape.
- **Threshold:** any specific tech name (framework, language, service), any domain noun (e.g., "trading", "logistics", "fintech"), any business detail = rewrite §1 to remove it.

## Resolved Decisions

These were Open Questions in the prior pass. Locked in based on user input:

- **Title:** *"Where to Look, Not What to Change"* — confirmed.
- **Project anchor (§1):** client codebase, can't be named. Reference neutrally as "a codebase I've been working on" / "the code I had open". No identifying detail. Codified in R7.
- **Concrete example in §4-§5:** synthetic, marked plainly as illustrative ("Imagine...", "Picture..."). Single example, no stacking. Tone kept light per user's note: "non esagerare, è più un articolo quasi filosofico". Codified in §5 beats.
- **Skill mention:** named once in §4 body (no inline link); GitHub link only in the footer block at the end. Codified in §4 beats and R1 mitigation.
- **Series numbering:** #4 in Series 1 ("AI workflow / compass"). Confirmed.
- **Date:** `2026-05-09` (today). Locked in frontmatter.
- **`articles/` folder:** WIP/scratch only. Article goes directly to `src/content/blog/where-to-look-not-what-to-change.md`. No copy in `articles/`.
- **VERSION / CHANGELOG bump:** **PATCH**. New content article, no functional change.

## Task Breakdown

Tasks are ordered. T1 has no dependencies; each subsequent task depends on the prior ones unless noted.

- [ ] **T1.** Draft the full article in `src/content/blog/where-to-look-not-what-to-change.md` per "Article skeleton" (§1-§7 + kicker + footer). Target ~3,000 words. Use the user's voice — short sentences, contractions, reflective tone, no flagged vocabulary. Stage the realization in first person; do not announce the lesson upfront. Open §1 with the prompt-and-result moment. Reference the client codebase neutrally per R7.
- [ ] **T2.** Self-review against §"Vocabulary discipline" and R6: grep the draft for both lists (standing list + soft-watch list). Replace every hit with user-shaped phrasing. Re-read sentences that feel "too smooth" and roughen them.
- [ ] **T3.** Self-review against R1-R7 in order:
  - **R1**: skill named exactly once in §4 body, no inline link, GitHub link only in footer, total skill-mechanics word count ≤ 80.
  - **R2**: §2 criteria ≤ 6 bullets, no expansion paragraphs.
  - **R3**: ≤ 2 "still disappointing" beats before §3.
  - **R4**: vocabulary introduced in plain English first; "lens"/"lenses" combined ≤ 3 in §4; `RT`/`DI` abbreviations not in the body.
  - **R5**: §6 uses "I suspect" / "the same shape might help" / "this might generalize to"; never "this applies to".
  - **R6**: no flagged vocabulary remains.
  - **R7**: §1 has no client-identifying detail (no framework, language, domain noun, business detail).
- [ ] **T4.** Verify all internal links resolve by reading the target files in `src/content/blog/`: `claude-code-retrospective.md`, `self-improving-tools.md`, `npm-install-intelligence.md`.
- [ ] **T5.** Verify the GitHub link in the footer is reachable: `https://github.com/elmisi/claude-code-automation/tree/main/plugins/refactor-discovery`. (WebFetch or curl.)
- [ ] **T6.** Word-count check: target 2,500-3,500 total; section ratios roughly: §1 250 / §2 300 / §3 400 / §4 550 / §5 250 / §6 300 / §7 150. If any section is more than 30% over its target, rewrite to the target before submitting.
- [ ] **T7.** Update `VERSION` (PATCH bump) and `CHANGELOG.md` per the project's semver convention. Read current `VERSION` to know the next number; read prior entries in `CHANGELOG.md` to match format.
- [ ] **T8.** Build the site locally to confirm the new article renders: `npm run build` (or `npm run dev` and check `http://localhost:4321/blog/where-to-look-not-what-to-change`). Verify the article appears in the blog listing and the detail page renders cleanly.
- [ ] **T9.** Hand off draft for the user's annotation pass. The user reviews the markdown directly; annotations are inline `> **NOTE**:` lines per the `plan-cycle` ops convention.
- [ ] **T10.** Apply user annotations, iterate until approved, then commit the article + `VERSION` + `CHANGELOG.md` in a single commit. No Claude co-author (per global rules in `~/.claude/CLAUDE.md`).
