---
title: "Claude Code Retrospective"
date: 2026-03-25
description: "What I learned by having Claude Code analyze the way I work — and why 80% of AI plans failed wasn't the model's fault."
tags: ["claude-code", "ai", "workflow"]
---

*What I learned by having Claude Code analyze the way I work.*

---

I've been using Claude Code for over a year. 77 projects, an automation plugin I built myself, Max account, high effort level, open permissions, voice enabled. I'm not a user who's learning — I build on top of the tool.

Yet there's a problem that's been nagging me for months: **80% of the plans Claude produces don't satisfy me**. They focus on irrelevant details and miss what actually matters. I always thought it was a model limitation. Then I did something I'd never done: I asked Claude to run a retrospective on how I work.

## The setup

I took the [Claude Code Ultimate Guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) — 23,000 lines of documentation, 219 templates, guides on architecture, security, workflows — and asked: "based on what you know about me and this reference, what could improve the way I work?"

The idea was simple: use the guide as a benchmark to see if I was missing something.

The result wasn't what I expected.

## The discovery: Claude knows the map but not the compass

I had Claude read all my memory files — 22 MEMORY.md files distributed across projects. They're detailed: architectures, deploy commands, SSH paths, bugs resolved with root causes, cross-repo dependencies. I use them as operational runbooks and they work well for that purpose.

But Claude spotted a pattern I wasn't seeing: **my memory files document WHAT things are, never WHY they matter to me**.

A concrete example. I have an ecosystem of interconnected microservices. The memory documents each service: stack, port, database, deploy command. When I ask Claude to plan an infrastructure change, it knows *how* to deploy — it has all the technical details. But it doesn't know that my priority is **verifying the impact on connected services before writing a single line of code**. So the plan focuses on configuration (which it does well) rather than impact verification (which is what I actually care about).

The plan is technically correct. But it's not the plan I would make.

## Feedback that dies with the session

There's one project — a complex IoT system with hardware, firmware, backend, and mobile app — where memory works particularly well. The reason is that I've saved **specific feedback** there: "never propose solutions without verified preliminary tests", "always read the ecosystem documentation before answering".

That feedback is the kind of context that makes plans better. It tells Claude not just what to do, but how to reason.

The problem? The other 20 projects don't have feedback. The corrections I give Claude — "no, not like that", "verify first", "that's irrelevant" — die with the session. And the pattern that frustrates me is the same everywhere: Claude proposes before verifying, focuses on "how to do it" instead of "what matters".

I always blamed the model. In reality, the model doesn't have the context to do otherwise.

## My global CLAUDE.md: 2 lines

When I looked at my global configuration file — the one Claude loads in every session, on every project — there were two rules:

1. Handle semantic versioning
2. Don't credit yourself as co-author in commits

That's it. No indication of how I reason, what I prioritize, which mistakes waste my time. Claude starts every session knowing I use semver and that I don't want its name in commits. Nothing else about me.

## What I found useful in the guide

Out of 23,000 lines, the concretely relevant content for my case is about 200 lines spread across 3 files. The rest is for people who are learning the tool.

**The "Annotation Cycle" pattern** (`guide/workflows/plan-driven.md`). Instead of asking for a plan and then verbally explaining what's wrong, the plan is written to a shared markdown file. I annotate directly in the file — comment, delete, add questions. Claude reads my annotations and rewrites. The loop continues until there are no open questions. The file becomes shared state between me and the agent, not a conversation that gets lost.

**The FIRE framework for incident response** (`guide/ops/devops-sre.md`). Four steps designed for someone who's alone with 15 services in production at 3 AM. Symptom in 30 seconds, guided diagnostics, approval gate before any action, automated postmortem. It's not an abstract workflow — it's an operational checklist I can put in my CLAUDE.md and have available when needed.

**Modular context engineering** (`guide/core/context-engineering.md`). Instead of a monolithic CLAUDE.md per project, rules that load only when you're working in a specific directory. The backend has its rules, the infrastructure has its own, the frontend has its own. Claude loads only the context relevant to what you're doing right now.

## My philosophy, confirmed

My position has always been: **I shouldn't have to learn to use the tool. The tool should adapt to me.**

This retrospective didn't change that — it refined it. The tool adapts to me to the extent that I tell it who I am. I'm not talking about reading guides or learning commands. I'm talking about writing 10 lines in the right file:

- When planning, always start with: what could break?
- Never propose a plan without verifying impact on connected services
- My priorities: working > elegant > optimized
- If you're not sure, ask me. Don't make it up.
- Plans should be short: 3-5 steps. If you need more, the task is too big.

These aren't technical instructions. They're my way of reasoning, externalized into a file that Claude reads before every session. It's the difference between having a collaborator who knows how to deploy and having one who knows what I care about.

## The takeaway

After a year of intensive use, my real bottleneck wasn't a missing feature or a pattern I didn't know. It was that **every session started without knowing how I think**.

My memory files documented the world. But they didn't document my compass.

---

*Guide used as reference: [Claude Code Ultimate Guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) (v3.37.5)*
