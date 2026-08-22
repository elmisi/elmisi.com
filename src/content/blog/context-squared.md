---
title: "Context Squared"
date: 2026-08-22
description: "We talk a lot about the context humans give AI. The other direction matters just as much: the context an agent gives us before asking us to decide."
tags: ["ai", "coding-agents", "context-engineering", "workflow"]
image: "/images/blog/context-squared.png"
imageAlt: "A green ASCII infinity loop with two cursors moving in opposite directions."
---

*The context we give an AI is only half of the conversation. The other half is the context it gives back to us.*

---

You can have an LLM with trillions of parameters, but if it doesn't know what you're talking about, it's useless.

You can have the most sophisticated attention mechanism, but if it doesn't know what matters to you, it's useless.

You can have the fastest GPU in the world, but if the model doesn't know what you need, it's useless.

We learn this quickly when we start working with AI. Give it the problem, the constraints, the codebase, and the goal. The better the context, the better the answer.

That is the usual direction: **the human gives context to the LLM**.

But there is another direction that we talk about much less.

## The context we need back

As a project evolves, the decisions become more detailed. Should this logic live here or somewhere else? Should we add another dependency? Which option will be easier to maintain six months from now?

When a coding agent asks me one of these questions, the question alone is not enough. I need to know why the decision matters, what the real options are, what each option would cost, and what the codebase tells us about them.

In other words, I need the agent to give context back to me.

That context can change a decision. It can also change how difficult the project will be and how long it will take to reach the goal. And producing it is not always easy. Sometimes the agent has to inspect the code. Sometimes it has to compare several paths. Sometimes it has to build something.

## A decision I didn't want to make

I am building a rule engine for a client. It takes a list of rules — some of them quite complex — and decides whether a configuration is valid.

The engine needs to run in two places: in a web application, on the client, and on the server. The client made TypeScript the obvious choice in the browser. For the server, my first instinct was Python. I know it better, I like it more, and I expected the implementation to be cleaner.

But using Python on the server would mean building the same non-trivial engine twice. Both versions would have to interpret every rule in exactly the same way. Every new rule, bug fix, and edge case would have to be implemented twice and kept aligned over time.

The alternative was to use TypeScript on the server too and share as much of the engine as possible.

This was not a debate about which language is better. The real question was: **how much could we actually reuse, and what would the two choices look like after the engine became more complex?**

I asked the coding agent to help me create the context I was missing. It implemented a representative subset of the engine in both languages. Then I asked it to extend both versions with new rule types and explore some of the situations we were likely to meet later.

I could finally see the two possible futures instead of discussing them in the abstract. I could compare readability, duplication, extension points, and the cost of keeping the client and server behavior identical.

TypeScript won.

I still prefer Python. But preference was only one part of the decision. Two separate implementations would create a real maintenance problem, while the TypeScript version was not nearly as ugly as I had expected. Once I had enough context, accepting the answer I didn't want became easy.

The prototype was not just an early implementation. It was a way to produce evidence for a decision. **The code itself became context.**

## Trying somebody else's idea

This is one of the things I find wonderful about this moment. Trying an idea used to be expensive. Advice could sound convincing, but validating it might require hours or days of work.

Now you can often describe an idea in natural language, give a coding agent some time, and turn those words into something you can inspect. It does not prove that the idea is right, but it gives you evidence much faster than before.

It also makes it easier to test other people's ideas.

The original version of Matt Pocock's <a href="https://www.aihero.dev/5-agent-skills-i-use-every-day" target="_blank" rel="noopener"><code>/grill-me</code> skill</a> was only three sentences long. Its purpose was to make the agent interview you about a plan, walk through the design decisions one by one, and explore the codebase instead of asking questions it could answer itself.

Pocock has since turned it into a much more elaborate workflow. What I tried — and what I am talking about here — is that original three-sentence version, not the current skill.

I liked the idea as soon as I read it. After trying it once, I knew it was useful. But I also noticed something missing. The agent was asking me to choose without always giving me what I needed to make the choice.

So I added one rule:

> Before asking each question, explain why the decision matters, the viable options, their concrete trade-offs, and any relevant evidence from the codebase. Then recommend one option.

The change is small, but it changes the conversation. The agent no longer acts only as an interviewer. It has to do the work required to make the question answerable.

## Context squared

The loop now looks like this:

1. I give the agent enough context to understand the problem.
2. The agent explores, compares, or prototypes what is still unclear.
3. It gives me enough context to make an informed decision.
4. That decision becomes new context for the next question.

Context from the human to the LLM. Context from the LLM to the human. Each side builds the context the other side needs.

Context for context. Context squared.

---

*This is the sixth article in an unplanned series. The [first](/blog/claude-code-retrospective) was about discovering that Claude knew the map but not my compass. The [second](/blog/self-improving-tools) was about building tools that keep the compass accurate. The [third](/blog/npm-install-intelligence) was about realizing those tools are software. The [fourth](/blog/where-to-look-not-what-to-change) was about asking agents for evidence instead of verdicts. The [fifth](/blog/the-wheel-was-already-round) was about defining what I needed before choosing the tool. This one is about context moving in both directions.*
