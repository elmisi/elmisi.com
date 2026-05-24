# The wiki Karpathy had already built for me

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

It worked because it separated capture (cheap, sync) from reconciliation (batched, async). Same pattern as GTD inboxes, software issue trackers, errata in publishing, event sourcing. I didn't know it then but I'd reinvented a very old idea.

The pattern has an extension I only saw after using it. `MISS` should split into two: information that's genuinely missing (a content gap) and information that *is* there but the agent couldn't find it via the index (a findability gap). They have different fixes. One adds content; one improves the router. Confusing them is how indexes rot.

## Then I found Karpathy's LLM Wiki

I started researching what tools existed before committing to build. Most of the AI-memory landscape was over-engineered for my case — Mem0, Letta, Zep are great for runtime agent memory across user sessions, not for one developer's lessons learned. RAG with a vector DB is a heavy hammer for a few megabytes of markdown. Pinecone is lock-in for free.

Then I read Andrej Karpathy's [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). And it was the strange experience of reading something that named, in clearer language, what I had been trying to design.

Three layers:

- `sources/` — immutable raw evidence. Snapshots of what you thought when.
- `wiki/` — synthesized current truth. LLM-owned. Rewritten as new sources arrive.
- A schema file (`AGENTS.md` or `CLAUDE.md`) — the router. Tells the agent the rules.

Three operations: ingest (new source → propagated to all relevant wiki pages), query (read the index, open the page), lint (periodic cleanup).

And the central insight, in Karpathy's words: *the tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping*. Humans abandon wikis because of cross-references and consistency checks, not because of writing. LLMs are perfect for exactly that work.

`WRONG_OR_MISS.md` fit into his model cleanly — as input to the lint pass.

The "router vs content" resolution I had extracted from the findability-vs-tokens tension turned out to be his `index.md` plus `AGENTS.md`, by another name.

My snapshot-with-changelog-header idea for handling opinion changes mapped to his immutable sources with `supersedes:` links in the frontmatter.

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

The split between `MISS` and `HARD_TO_FIND` was the single deviation from Karpathy's model that I felt strongly about. They have different costs and different fixes, and conflating them is exactly the failure mode that makes a knowledge base quietly stop being searchable over time.

## What I learned about asking the right questions

I committed to the architecture in one sitting because the questions had done most of the work. By the time I was reading Karpathy's gist, I already knew what I needed to see. The shape of a solution that fits is unmistakable when you've spent the time naming what you want.

Most of my early attempts at personal infrastructure failed because I started with the tool and worked backwards. This time I started with the four properties I wanted the system to have, derived the tension between them, and the right pattern surfaced almost on its own.

The repo is called `ambidextrous`. Two hands, one brain. We'll see if it stays alive longer than my last three attempts.
