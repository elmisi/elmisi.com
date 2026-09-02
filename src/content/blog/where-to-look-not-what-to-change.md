---
title: "Where to Look, Not What to Change"
date: 2026-05-09
description: "Why asking Claude for refactorings kept producing surface-level answers, and what changed when I asked it to find places worth investigating."
tags: ["claude-code", "ai", "refactoring", "workflow", "code-quality"]
asciiImage:
  src: "/where-to-look-not-what-to-change-ascii.html"
  alt: "A luminous green eye with a faceted iris floating in a perfectly uniform dark void."
---

*Why I stopped asking Claude for refactorings and started asking it for places worth investigating.*

---

## I asked Claude to suggest refactorings

I had a codebase open. Not mine — a codebase I've been working on for a client. Big enough that I can't hold it all in my head. Old enough that nobody fully remembers why some parts look the way they do.

I asked: *find refactorings in this repo*.

It gave me ten items. Eight were true. None mattered.

Rename a variable from `data` to `userData`. Extract a small helper for a four-line block. Split a 200-line function into three smaller ones. All correct. Any senior reviewer would nod along. I read the list twice and felt nothing.

What I wanted in that list — what I'd been hoping for since I typed the prompt — wasn't in it. Not the function I knew could disappear entirely because nothing real depended on it anymore. Not the two modules sitting in different folders, with different names, doing the same job. Not the policy hidden in three switch statements, repeated with small mutations, that nobody had ever named.

The list had refactorings. It just didn't have the ones I'd actually do.

I sat with that for a minute. The model wasn't wrong. The items were valid. But the gap between what it returned and what I wanted was exactly the gap that mattered. The boring items were free; the interesting ones were the whole reason I'd asked.

So the first thing I did was assume it was my fault.

## Maybe it doesn't know what *good* means to me

I figured the gap was taste. Claude didn't know what I considered beautiful code. It had a generic sense of "clean", but generic isn't useful here.

So I tried the obvious fix. I added: *"refactor according to clean code best practices"*. The kind of phrasing any senior reviewer would invoke without thinking.

The list got longer. The character didn't change. SOLID-shaped renames. "Extract method" three times. A polite suggestion that maybe I should consider an interface here. Still no mention of the function that could disappear, the two modules under different names, the policy spread across three switch statements.

I deleted that and tried something more honest. I wrote out, in my own words, what I find beautiful in code. A short list, in the rough vocabulary I'd use talking to a colleague, not a manifesto:

- code I can delete
- a name that removes a whole comment
- one place that owns the decision
- no theatre around errors

I gave that to Claude as the standard. Asked again.

The output got slightly more interesting around the edges. A few more "consider removing this layer" notes. But the items I could see at a glance — the duplicated patterns under different names, the wrappers around a single call, the dead branches — still didn't show up.

That's when the dissonance hit. The criteria were clear. The code was sitting in front of it. And still I didn't get the items I'd see myself in five minutes of reading. Even with my own taste written down, the list stayed shallow.

Something else was wrong, and it wasn't taste.

## Where to look, not what to change

I sat with the disappointment a bit longer this time. What was the *pattern* in the items that were missing?

They all had one thing in common: deciding whether to act on them required understanding the code, not just looking at it. *"This function can disappear"* — that's not a refactoring. That's a claim. It rests on knowing what the function is for, who calls it, what would break, whether the abstraction it carries has weight elsewhere in the system. The action — delete it — is the easy part. The hard part is the judgment that comes before.

The items I *was* getting were different. Renaming `data` to `userData` doesn't require a model of the codebase. The action and the answer are the same thing. Once you see the variable, the rename is the entire decision.

So a list of *actions to perform* can only ever surface items where the action itself is the answer. Renames, extracts, splits. That's a real category — but it's the boring category. The interesting items aren't actions. They're suspicions. Tensions. Places where something is off and someone needs to think about it.

That was the part that changed.

> *I was asking Claude to give me the answer. What I needed was a map of where to look.*

The agent is good at breadth. It can read every file. It can compare patterns across the repo. It can notice that the same four-step sequence appears in seven places, or that a name and a behaviour have drifted apart. I'm good at judgment in context. I know what this code is for. I know what we're trying not to break. I know which abstractions are load-bearing and which are scaffolding nobody cleaned up.

When I asked Claude for actions, I was asking it to do my job — to make the call. Of course it stuck to safe items, the ones where the call is trivial. When I started asking it for signals — places where something looks suspicious, with the evidence that makes it suspicious — I was asking it to do its job. Surface the tension. Leave the verdict to me.

This is the same shape as something I wrote about a few months ago, in the first article in this series. Every session started without knowing how I think. The fix there was to write down the compass. The fix here is different: it's not about teaching the agent more about me. It's about asking for a different kind of output. Not a verdict. A map.

## Ways of looking at the code

The reframe is easy to state and hard to operate. *"Find suspicious places"* on its own is too vague — you get back a list of things that "could be improved", which is the same shallow output dressed up.

What worked was giving the model specific angles to inspect against. Not "look for problems", but "look at this code through this particular lens, and tell me what stands out." Different angles surface different kinds of tension.

I ended up with eight. Four of them, with one-line examples:

- **Temporal coupling** — files that keep changing together in commits, even though there's no code dependency between them. Often a hidden policy that lives across modules.
- **Change amplification** — a small conceptual change forces edits in many places. Usually a missing name or a missing owner for the concept.
- **Shotgun ceremony** — the same mental sequence (parse, validate, map, register) repeats across many call sites with small mutations. The shape is begging for a name.
- **Semantic drift** — the function name says one thing, the comment says another, the test asserts a third, and the behaviour does a fourth. Pick the one that's actually true and the rest is a refactor.

The other four sit in the same family: asymmetric abstractions, hidden policy, test gravity, negative space. Each one is a question you ask the code rather than an action you take on it.

The output of each angle isn't a refactor. It's a *smell lead*: a one-line label, a sentence saying why this is suspicious, a piece of evidence quoted from the code, and a *promotion condition* — the thing that would have to be true for this lead to become a real candidate. The promotion condition is the gate. Without it, every lead becomes a refactor by inertia, and we're back where we started.

Then there are four states a lead can end up in:

- **smell lead** — interesting tension, judgment still pending
- **refactor candidate** — promoted after the "why" check holds up
- **research task** — needs evidence the agent can't see locally (a meeting, a runtime trace, a question for someone)
- **document-intent** — the code is fine, but the reason it's fine isn't visible. Leave it. Add a comment that captures the intent.

That last state matters more than it sounds. A lot of "smells" turn out to be load-bearing on closer inspection. The output of the loop, in those cases, isn't a code change. It's a comment that prevents the next person — me, in three months — from filing the same false alarm.

A few rules keep the output trustworthy. Every lead is anchored to a specific commit and a file:line piece of evidence, so it doesn't rot the moment someone touches the file. Universal claims like *"nothing else uses this"* require an enumeration, not a vibe. Duplication claims require a behaviour comparison, not a visual one — two functions that look similar can do very different things, and the loop has to know the difference.

I eventually put all of this into a skill called refactor-discovery. The link is at the end of the post. I don't want to dwell on the tool here — the article is about the kind of output, not the package that produces it.

## What changed in the output

Imagine a validation flow repeated in seven handlers. Same four steps in slightly different order. Same intent. No shared name.

The action-list approach surfaces this as: *"rename `data` to `userData` in handler 3 for consistency."* True. Boring. Misses everything.

The lens-based approach surfaces it as: *"validation logic appears in 7 sites with the same 4-step ceremony but no name. Suspicion: a missing named policy. Evidence: handlers/a.ts:42, handlers/b.ts:38, handlers/c.ts:50… Promotion condition: confirm the four steps mean the same thing in all seven sites — same error semantics, same ordering constraints — before extracting."*

Two things changed. The interesting item is now visible. And it shows up with the evidence I need to decide whether to act on it. The verdict is still mine — I might look at the seven sites and conclude that they only *look* the same, that the small differences carry weight nobody named yet, and that the right move is to leave the duplication and write the comment that explains why. That's a fine outcome. It's a *decided* outcome.

The new approach also surfaces the boring renames. They're still there. They're just at the bottom of the list, marked as low-priority, where they belong.

I should be honest about the limits. This isn't *"Claude is now good at refactoring."* The action-list failure mode has been swapped for a different, smaller one: this approach only sees what the eight angles can see. Anything outside them is invisible. That's a real limitation, and it's the next thing to work on.

## Where else this might apply

I've only run this loop on refactoring. So I want to be careful here.

I suspect the same shape helps for any task where the interesting output requires judgment in context. Code review, where the verdict depends on knowing what the team has already agreed to. Architectural review, where "is this a good boundary" rests on what the next year of work probably looks like. Security review, where exploitability depends on the threat model. Library selection, where "this looks fine" hides assumptions about who else uses it and how it'll be maintained.

In all of those, the default phrasing of every prompt nudges the agent toward a verdict. *Propose a fix. Recommend an approach. What should I do?* The verdict-shaped output is the cheap output. It's what you get if you don't ask for anything else. And it's almost always too shallow to act on, because the agent doesn't have the context that turns a candidate into a decision.

The candidate-shaped output — *here are the suspicious places, with evidence, and the conditions under which they'd matter* — is the expensive one. The agent has to do real reading, real comparing, real evidence-gathering. But the output is something I can use, because the part that's missing — my judgment — is exactly the part the agent shouldn't be faking.

This might generalize, or it might not. I'd want to run the same loop in two or three other domains before claiming more than that. What I can say is that, in the one domain I've run it in, the change wasn't in the model. It was in what I asked for.

## Where I am

The new approach is working. The output I get is something I can sit with for an hour and end up with three real refactors, two intent-comments, and a couple of research questions for the team. That's a good day's input from a tool. I couldn't say that about the action lists.

The obvious limit is the eight angles. They're mine, refined from a few real passes, and they cover what I've personally tripped over. They're not exhaustive. New work surfaces shapes I haven't named yet, and when that happens the loop misses them silently.

The open question I keep going back to: is the right move to keep adding angles, or to add a meta-question — *what's a structural smell I haven't given a name to in this repo?* — and let the agent suggest the next lens. I don't know yet.

What I do know is what I want from the tool now, and it's not what I started with.

I don't need Claude to decide the refactoring. I need it to show me where my judgment is worth spending.

---

*Fourth article in an unplanned series. The [first](/blog/claude-code-retrospective) was about discovering that Claude knew the map but not the compass. The [second](/blog/self-improving-tools) was about building tools that keep the compass accurate. The [third](/blog/npm-install-intelligence) was about realizing those tools are software. This one is about the kind of output you should ask for when the work is judgment in context.*

*The skill mentioned in §4: [refactor-discovery on GitHub](https://github.com/elmisi/claude-code-automation/tree/main/plugins/refactor-discovery).*
