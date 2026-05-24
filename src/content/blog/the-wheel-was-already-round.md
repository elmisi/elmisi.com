---
title: "The Wheel Was Already Round"
date: 2026-05-24
description: "Designing a knowledge base for AI agents from four questions, then realizing Karpathy had already published the right answer."
tags: ["claude-code", "ai", "workflow", "knowledge-management", "agents"]
---

*Designing a knowledge base for AI agents from four questions, then realizing Karpathy had already published the right answer.*

---

*Fifth article in an unplanned series. The [first](/blog/claude-code-retrospective) was about discovering that Claude knew the map but not the compass. The [second](/blog/self-improving-tools) was about building tools that keep the compass accurate. The [third](/blog/npm-install-intelligence) was about realizing those tools are software. The [fourth](/blog/where-to-look-not-what-to-change) was about asking better questions of those tools. This one is about giving those tools a knowledge base I almost reinvented from scratch.*

---

Every new Claude Code conversation started the same way. Me, re-explaining how I like things — error handling, the patterns I've stopped using, the libraries I've burned on, the conventions I settled on after too many arguments with my past self.

So I decided to build a knowledge base. One place. Plain markdown, gitable, that any agent could read at the start of a task.

The interesting part wasn't deciding to build it. It was the four questions I asked before writing a single file.

## The four questions

I sat down and refused to start with tools or structure. I started with what I wanted to be true:

1. If something is in the KB, an agent must be able to find it.
2. The agent must use as few tokens as possible to find it.
3. The KB must reflect connections between ideas — not just be a pile of files.
4. The KB must stay up to date as I change my mind.

Four questions. Each one rules out a class of solutions.

## Findability vs token cost — the tension

Questions 1 and 2 pull in opposite directions.

To guarantee findability, the safest move is to load everything into the prompt. Reliable, predictable, expensive forever — you pay for those tokens every turn, on every project.

To minimize tokens, you push everything to disk and hope the agent finds it. Cheap, until the agent doesn't trigger a search and confidently invents an answer you would have caught.

The resolution — once I forced myself to name it — is to make the always-loaded part a *router*, not content. The router doesn't hold knowledge. It holds *addresses*. Where things live, how they're named, when to consult them. The router can be tiny because it doesn't have to know what's in the files, only that they exist.

It's RAM vs disk in computer architecture, applied to a context window.

## WRONG_OR_MISS — the first intuition that worked

Question 4 — keeping the KB current — is the one most projects get wrong. Knowledge bases die from neglect, not from bad design. The friction of "stop what you're doing and fix the doc" wins.

I'd already prototyped a pattern I called `WRONG_OR_MISS.md`: an append-only file where, as I navigated my KB, I'd add a one-line entry whenever I noticed an error (`WRONG: this should say X`) or a gap (`MISS: this topic isn't here`). Periodically, a process — me or an agent — would walk the file and apply the fixes.

It worked because it separated capture (cheap, sync) from reconciliation (batched, async). Same pattern as GTD inboxes, software issue trackers, errata in publishing, event sourcing — and the [self-improving plugin I wrote about a few weeks ago](/blog/self-improving-tools). I didn't know it then but I'd reinvented a very old idea.

The pattern has an extension I only saw after using it. `MISS` should split into two: information that's genuinely missing (a content gap) and information that *is* there but the agent couldn't find it via the index (a findability gap). They have different fixes. One adds content; one improves the router. Confusing them is how indexes rot.

## Then I sat down with Karpathy's LLM Wiki

Before committing, I looked at what existed. Most of the AI-memory landscape was over-engineered for my case — Mem0, Letta, Zep are great for runtime agent memory across user sessions, not for one developer's lessons learned. RAG with a vector DB is a heavy hammer for a few megabytes of markdown. Pinecone is lock-in for free.

I already knew, vaguely, that Karpathy had something called an LLM Wiki — I'd seen YouTube videos about it scroll past, but the titles read like clickbait and I never watched any. I hadn't read the gist either. When I finally sat down with [it](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), I was reading it cold. The surprise wasn't that his approach was sound. It was how exactly his model matched what I'd been circling around — three layers, the same operations, the same handoff between human input and LLM bookkeeping. No merit on my part for the intuition. I just recognize a good idea when I finally sit down with it.

Three layers:

- `sources/` — immutable raw evidence. Snapshots of what you thought when.
- `wiki/` — synthesized current truth. LLM-owned. Rewritten as new sources arrive.
- A schema file (`AGENTS.md` or `CLAUDE.md`) — the router. Tells the agent the rules.

Three operations: ingest (new source → propagated to all relevant wiki pages), query (read the index, open the page), lint (periodic cleanup).

And the central insight, in Karpathy's words: *the tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping*. Humans abandon wikis because of cross-references and consistency checks, not because of writing. LLMs are perfect for exactly that work.

`WRONG_OR_MISS.md` fit into his model cleanly — as input to the lint pass.

What I'd called "router vs content" was his `index.md` plus `AGENTS.md`, with cleaner naming.

My snapshot-with-changelog-header idea for handling opinion changes was his immutable `sources/` files with `supersedes:` links in the frontmatter — and that same `supersedes:` mechanism, combined with cross-references between wiki pages, is also how question 3 (connections between ideas) gets answered. The KB isn't a pile of files; it's a graph whose edges live in the frontmatter and in the wiki page bodies themselves.

I had been designing the same thing, less coherently. So I stopped designing and adopted his model.

## What I built

The whole schema lives in a single ~140-line `AGENTS.md`. Every LLM agent that visits the repo loads it automatically. The most load-bearing part of the file is the trigger section — what the agent does *when*:

```markdown
## Behavioral triggers for the agent

Always consult this KB when:
- You start a new task
- You're about to make a design decision
- You need to answer "how do I usually do X?"

Append to WRONG_OR_MISS.md when:
- You find a contradiction between two wiki pages
- You can't find info you reasonably expected to be there
- The user corrects something you said based on the wiki
```

Without triggers, the rest is decoration. An agent that doesn't know *when* to consult the KB will never consult it, no matter how beautifully you've structured the contents.

The other piece I care about is the categorization of `WRONG_OR_MISS` entries. The taxonomy I landed on:

| Tag | Meaning |
|---|---|
| `WRONG` | Wiki says something false |
| `OUTDATED` | Was true, no longer is |
| `UNCLEAR` | Exists but is ambiguous |
| `MISS` | Genuinely missing — needs a new source |
| `HARD_TO_FIND` | Info IS there — fix the index, not the content |
| `CONFLICTING` | Two pages disagree |

The split between `MISS` and `HARD_TO_FIND` was the single deviation from Karpathy's model that I felt strongly about. They have different costs and different fixes, and mixing them up is exactly the failure mode that makes a knowledge base quietly stop being searchable over time.

## What I learned about asking the right questions

The questions did most of the work. By the time I sat down with Karpathy's gist, I already knew what I needed to see — and seeing it meant I could stop designing and start copying.

Most of my early attempts at personal infrastructure failed because I started with the tool and worked backwards. This time I started with the four properties I wanted the system to have, found the tension between them, and the right pattern showed up almost on its own — already named, already explained, already published.

The pattern I want to remember isn't the architecture. It's that, once you've named what you want, the answer often turns out to already exist, written by someone who got there first. The wheel was already round. Better to use it well than to carve a new one badly.
