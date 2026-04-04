---
title: "Self-Improving Tools"
date: 2026-04-04
description: "How I went from using AI coding agents to building tools that get better every time I use them — through structured feedback loops, not fine-tuning."
tags: ["claude-code", "ai", "workflow", "plugins"]
---

*How I went from using AI coding agents to building tools that get better every time I use them.*

---

A few days ago I wrote about a realization I had after a year of using Claude Code: my memory files documented the world but not my compass. They told Claude *what* things are — stacks, ports, deploy commands — but never *why* they matter to me. Every session started without knowing how I think.

That article ended with a fix: write 10 lines in the right file. Externalize your reasoning, not just your knowledge.

It worked. But it was only the first step. What I didn't see coming was where that line of thinking would take me.

## From compass to process

After the retrospective, I built a plugin called plan-cycle. The idea came directly from something I'd found in a guide: the "annotation cycle" pattern. Instead of asking Claude for a plan and then arguing about it in chat, the plan lives in a markdown file. I annotate it. Claude reads the annotations, rewrites the sections, removes the notes. We iterate until there are no open questions.

It solved a real problem. Chat-based planning is lossy — context leaks, feedback gets buried in the conversation, and by the third correction Claude has forgotten the first one. A shared file is state that persists. Both sides can see it, edit it, and know exactly where we are.

I was happy with it. Then I started using Codex.

## The second pair of eyes

I use Codex in parallel with Claude Code. Not for the same tasks — I use it to review plans that Claude wrote, or to build independent projects from scratch. It's a different model with different strengths, and having both is like having two senior engineers who don't always agree.

When I started feeding plan-cycle outputs to Codex for review, something uncomfortable happened: Codex kept finding gaps. Not in the implementation details — Claude is good at those. The gaps were always in the same places: edge cases with no concrete thresholds, failure modes described as "handle gracefully" with no actual fallback, constraints stated as absolutes with no exit clause.

The first time, I thought the plan was just weak. The second time, I noticed the pattern. By the third time, I had the data: the tool itself was consistently producing plans that looked complete but weren't.

The quality problem wasn't in any individual plan. It was in the instructions that generated all of them.

## Looking at my own annotations

I went back and looked at the annotations I'd been writing across multiple plan-cycle sessions. Almost all of them were asking the same question, phrased differently: *"What happens when this doesn't go as expected?"*

The plans described the happy path well. Architecture, data flows, component boundaries — all solid. But they were always vague on edges. No timeouts. No retry counts. No "if this fails, we do that instead." No numbers where numbers were needed.

This wasn't Claude being lazy. The SKILL.md that drives plan-cycle simply didn't ask for those things. The template had a section called "Edge Cases and Risks" with a one-line prompt: *"What could go wrong. What needs careful handling."* That's a question that invites vague answers. And vague answers are exactly what I got.

## Fixing the tool, not the output

Here's where the shift happened. My old instinct would have been to write better annotations next time — to compensate for the tool's blind spots with my own attention. That works, but it doesn't scale. I'd be patching the same gaps in every plan, forever.

Instead, I changed the tool.

I added three guidelines to plan-cycle's SKILL.md:

- **Concrete numbers over qualitative descriptions.** Don't write "should be fast" — write "< 200ms p95". Don't write "handles large files" — write "up to 50MB, rejects above with error X".
- **Exit clauses over absolute constraints.** For each significant decision, state the condition under which you'd abandon the approach and what alternative you'd switch to.
- **Explicit degradation over implicit assumptions.** "Graceful degradation" is not a plan — "returns cached data from last successful fetch, shows stale-data banner, retries every 30s up to 5 times" is.

I restructured the Edge Cases section to require likelihood, impact, concrete mitigation, and a plan B. I added a new section — Failure Modes and Degradation — that forces the plan to describe what happens when each critical component fails, with specific thresholds and fallback steps.

The next plan was noticeably better. Not because Claude suddenly got smarter, but because the instructions no longer allowed vagueness where precision was needed.

## The recursive realization

After fixing plan-cycle, I caught myself thinking: I just did something interesting. I used the output of a tool to diagnose a flaw in the tool's instructions, then changed the instructions to fix the flaw. And the process I followed — observe patterns, identify root causes, propose specific changes — is itself a repeatable process.

So I built another plugin: takeaway.

Takeaway does one thing. It interviews me about what I learned from using a skill or tool, identifies patterns in my observations, and produces a structured feedback file with specific, agent-ready improvement instructions. The output isn't vague notes — it's a document that an agent can consume directly to make changes. Exactly what I did manually with plan-cycle, but formalized into a repeatable workflow.

The loop is: use a tool → notice what's off → run takeaway → get structured improvements → apply them → use the tool again. The tool gets better every cycle.

And yes, I plan to run takeaway on takeaway itself. The recursion is the point.

## The evolution in hindsight

Looking back at a year of building on AI coding agents, I can see three distinct phases:

**Phase 1: The tool works for me.** I used Claude Code as-is. Wrote prompts, got outputs, fixed what was wrong manually. Every session started from zero context. This is where most people are.

**Phase 2: The tool knows me.** After the retrospective, I started writing memory files that capture not just facts but reasoning. CLAUDE.md files that encode my priorities, not just my stack. Claude stopped making the same mistakes because it finally had my compass. This is where the power users are.

**Phase 3: The tools improve themselves.** I'm building tools whose output quality increases over time because the feedback from using them flows back into their own instructions. Not through fine-tuning or training — through structured feedback loops that modify the prompts, templates, and guidelines that drive the tools. This is where I am now.

Each phase emerged from the previous one. You can't build self-improving tools if the tools don't know your compass. And the tools can't know your compass if you haven't externalized it.

## This isn't just for programmers

The pattern I'm describing — use a tool, extract lessons, feed them back into the tool's instructions — isn't limited to coding. I see it emerging among technical users who build workflows on top of AI: people running consulting practices with custom GPTs, operations teams with automation pipelines, analysts with report-generation workflows.

The common thread is that these are people who have moved past "how do I use this tool" to "how do I make this tool get better at the specific thing I need it to do." They're not waiting for the next model release to fix their problems. They're fixing their tools' instructions.

This is a different kind of skill. It's not prompt engineering — that's about crafting individual requests. It's not fine-tuning — that's about changing the model. It's something in between: engineering the feedback loops that sit between you and the model, so that each iteration builds on the last.

## Finding the compass

The retrospective ended with a realization: every session started without knowing how I think.

Building plan-cycle was the first attempt to fix that for planning specifically. Using Codex to review the output showed me the fix was incomplete. Analyzing my own annotations revealed the systematic gap. Fixing plan-cycle's instructions closed that gap. Building takeaway generalized the fix into a repeatable process.

Each step came from the previous one. Not from a grand plan — from paying attention to what wasn't working and asking why.

I said I was finding my compass. I think what I'm actually finding is something more useful: a way to keep calibrating it.

---

*This is the second article in an unplanned series. The [first](/blog/claude-code-retrospective) was about discovering that Claude knew the map but not the compass. This one is about building tools that keep the compass accurate.*
