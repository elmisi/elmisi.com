---
title: "npm install intelligence"
date: 2026-04-30
description: "Skills look like prose but behave like software. We have the same problems — quality, testing, maintenance, discovery — and none of the infrastructure."
tags: ["claude-code", "ai", "skills", "software-engineering", "workflow"]
---

*Skills look like prose but behave like software. We have the same problems — and none of the infrastructure.*

---

## The moment it clicked

A few weeks ago I was looking at the test file for my [automate](https://github.com/elmisi/claude-code-automation) plugin — a Claude Code plugin that helps you create automations. The file had 21 test cases. Each one describes a scenario, the interview questions and answers, the expected output files, and a verification block with the exact JSON or markdown the skill should produce.

Then I looked at the GitHub Action I'd set up. It runs every morning at 6 AM. It scrapes three pages from the Claude Code documentation, extracts every hook event, every tool name, every frontmatter field, and diffs them against my local schemas. If Claude shipped a change overnight, I get an issue by breakfast.

Then I looked at the takeaway document I'd written after running the skill through a second model's review. Eight pages of lessons, each one structured as: what was observed, what principle it reveals, how to apply it to the skill's instructions, what was rejected as too specific.

I stopped and counted. 21 test cases. A CI pipeline. A daily upstream-compatibility check. Versioned schemas. A structured post-mortem that feeds back into the instructions. Release notes in a CHANGELOG.

I was doing software engineering on a markdown file.

## The artifact nobody named

A skill — whether it's a Claude Code SKILL.md, a custom GPT's system prompt, a Codex agent's instructions, or any structured text that drives an LLM — is an artifact that looks like prose but behaves like code.

It has inputs: the user's request, the conversation context, the files in scope. It has outputs: the agent's behavior, the files it creates, the decisions it makes. It has a specification — the text itself. And it has bugs. When the output doesn't match what you expected, you go back to the instructions and figure out what was ambiguous, what was missing, what was wrong.

It has versions. I update my skills regularly — the plan-cycle skill alone has been through at least six significant rewrites. Each rewrite came from observing a pattern of failures, diagnosing the root cause in the instructions, and changing the text. That's debugging.

It has dependencies. My automate plugin depends on schemas that track Claude's tool API. When Claude adds a new hook event or a new tool, my schemas go out of date, my skill produces wrong advice, and my tests fail. That's a breaking upstream change.

It has maintenance burden. The GitHub Action exists because I can't manually check the Claude docs every day. Skills rot when the platform they target evolves. That's dependency drift.

These are all software problems. We've spent fifty years building infrastructure to handle them — package managers, test frameworks, CI pipelines, semantic versioning, code review. Skills have none of it.

## The discovery problem

Go to the Claude Code plugin marketplace. Or browse custom GPTs. Or search GitHub for "system prompt." You'll find the same thing you found on npm in 2013: a thousand packages doing vaguely similar things, no way to tell which ones are good, and nobody maintaining most of them.

My automate plugin does one thing: it interviews you about what you want to automate, decides which Claude Code mechanism to use (hook, skill, subagent, permission, MCP server...), and creates the files. There are probably twenty plugins that do something similar. How do you pick? Star count? Last commit date? Whether the README sounds competent?

This is the npm problem. The signal-to-noise ratio is terrible. The cost of trying a bad package is high — not in money, but in time and trust. You install a skill, use it for a week, realize it produces vague outputs, and wonder if the problem is the skill or you. With code, you can read the source and decide. With a skill, you read the instructions and still don't know how the model will interpret them.

Discovery is harder for skills than for code. Code has type signatures, API docs, benchmarks, test coverage reports. A skill has a description. Maybe an example. The quality signal is almost entirely social: someone you trust told you it works.

## The testing paradox

This is where skills diverge from software in a way that matters.

My plugin has three types of tests. Structure tests are deterministic — they check that files exist, JSON is valid, schemas are consistent. Fixture tests create expected outputs in a sandbox and validate structure. Both run in CI, both are reliable, both cost nothing.

The third type is the interesting one. Interactive tests actually invoke Claude with a scenario and check whether the output is reasonable. These tests consume tokens. They produce non-deterministic results. The same test, run twice with the same input, can give different outputs. Not wildly different — usually — but different enough that you can't write `assertEquals(expected, actual)`.

You can't unit-test a skill the way you unit-test a function. The test is not "does this produce output X" — it's "does this produce output that falls within an acceptable range of behaviors." That's not a test. That's a statistical experiment. You need multiple runs, you need to define what "acceptable" means, and you need to pay for every single execution.

This creates a real constraint on quality. Running my 5 interactive tests costs money and time. Running them ten times each for statistical confidence costs ten times more. Imagine a world where every `npm test` charges you $2 and sometimes fails randomly. Nobody would write tests. And in fact, almost nobody writes real tests for their skills.

The irony: the only way to know if a skill works is to use it. And by the time you've used it enough to know, you've already paid the cost of just building the thing yourself.

## Can we normalize a skill?

In databases, normal forms eliminate redundancy and ambiguity. First normal form: every field is atomic. Second: no partial dependencies. Third: no transitive dependencies. You take messy, redundant data and reduce it to a minimal, unambiguous structure where every fact is stated once.

Can we do the same for skills? Given a skill S that produces behavior B on input I, is there a shorter formulation S' that produces the same B?

The answer is probably no, and the reason is interesting.

Natural language is not a formal system. Two people read the same sentence and extract different meaning. The model's interpretation depends on its training data, its context window, the other instructions loaded alongside yours. "Be concise" means one thing to Claude and another to GPT. "Handle edge cases" means different things depending on what the model considers an edge case. The same words, different behavior.

A true normal form would need a formal language — something unambiguous by construction. But then you're writing code, not a skill. And the whole point of skills is that they're written in natural language because that's how humans express intent.

There might be something in between, though. Not full normalization, but structural conventions that reduce ambiguity. The takeaway lessons I extracted from plan-cycle are an example: "every empirical claim used as a premise for a decision must be either verified inline or marked as an assumption." That's a constraint that narrows the output space. Add enough constraints like this and the skill becomes more predictable.

But there's a tension: too many constraints and the skill gets brittle. It handles the cases the author thought of and breaks on everything else. The sweet spot is somewhere between "do a code review" (too vague, infinite output space) and a 500-line procedure that specifies every step (too rigid, breaks on the first unexpected input).

Finding that sweet spot is itself an unsolved problem. We don't even have a vocabulary for it. What's the "coverage" of a skill? What's its "specificity"? Where's the threshold between "flexible enough to generalize" and "vague enough to be useless"?

## The scientific paper parallel

Scientific papers have infrastructure we could steal.

A paper has a methods section: detailed enough that another researcher can reproduce the experiment. A skill has... its own text, which is both the method and the execution environment. If you share your skill and I run it on a different model, with different context, I get different results. There's no controlled environment.

A paper goes through peer review before publication. Reviewers check methodology, logic, claims. A skill goes through nothing. You write it, you publish it, whoever downloads it trusts you. Or doesn't.

Papers are published in journals that stake their reputation on quality. Nature, Science, JMLR — the name carries a signal. Skills are published on GitHub, or in a marketplace, or on a Twitter thread. The signal is the author's follower count.

Papers have citations. You can trace the lineage of an idea — who built on whom, what was confirmed, what was retracted. Skills have no lineage. If my plan-cycle skill was inspired by Boris Tane's annotation cycle workflow, you'd only know because I wrote it in the README. There's no formal dependency graph for ideas.

Papers get retracted when they're wrong. Skills just sit there. Nobody issues a retraction for a prompt that stopped working after a model update.

What if we built something like this? A registry where skills are submitted with test cases and expected behaviors. A review process — not by humans necessarily, but by other agents running the skill against a benchmark. A lineage system that tracks which skills build on which. A deprecation mechanism that flags skills whose target model has changed.

## Would it actually be better?

The honest answer: I don't know.

Scientific publishing has its own crisis. The replication crisis showed that a large fraction of published results don't reproduce. Peer review is slow, expensive, and misses things. Impact factor creates bad incentives — people game the system. Journals become gatekeepers, and gatekeepers develop biases.

If we built the same infrastructure for skills, we might get quality control. Or we might get bureaucracy that kills the one thing skills have going for them: anyone can write one in ten minutes and start using it right away.

npm solved discovery but created a different problem: deep dependency trees where a single broken package — left-pad, 11 lines of code — takes down thousands of projects. A skill registry might solve discovery and create the same fragility: everyone depending on the same foundational skills, maintained by someone who gets bored and walks away.

The formal-language approach — making skills less ambiguous by making them more structured — might improve reproducibility but kill the flexibility that makes them useful. Code is unambiguous and deterministic, but nobody writes a 200-line Python script to describe how they want a plan structured. They write ten lines of natural language because it captures intent at the right level of abstraction.

Maybe the answer isn't to copy what worked for software or for science. Maybe skills are a new kind of artifact that needs its own infrastructure — something we haven't built because we don't fully understand what we're building.

## Where I am

I build skills. I test them — imperfectly, expensively, non-deterministically. I version them. I maintain them against upstream changes. I run takeaway sessions that extract lessons and feed them back into the instructions. I have CI for the deterministic parts and manual smoke tests for the rest.

It works. But it doesn't scale. I can maintain three or four skills this way. I can't maintain thirty. And the moment someone else tries to use my skills, all my implicit knowledge — what "reasonable output" means, which edge cases matter, why I phrased that sentence that way — disappears. The skill works for me because I know what it's supposed to do. For everyone else, it's a black box with a README.

This is where every kind of software was before we built the infrastructure. Before package managers, before test frameworks, before code review. We shared code by emailing tar files. It worked, but it didn't scale.

Skills are at that stage. Version 0.1.0 of a new kind of artifact. The infrastructure is missing. The question is what shape it takes when it arrives — and whether we'll recognize it.

---

*Third article in an unplanned series. The [first](/blog/claude-code-retrospective) was about discovering that Claude knew the map but not the compass. The [second](/blog/self-improving-tools) was about building tools that keep the compass accurate. This one is about the realization that those tools are software — and we're still writing them like it's 1995.*
