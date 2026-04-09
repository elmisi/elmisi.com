---
title: "The Queue That Isn't a Queue"
date: 2026-04-09
description: "How online waiting rooms actually work, why they feel unfair, and what it would take to build something better."
tags: ["system-design", "ticketing", "analysis"]
---

*How online waiting rooms actually work, why they feel unfair, and what it would take to build something better.*

---

## It started at a festival in the mountains

I've been to the Montelago Celtic Festival twice. Both times, buying tickets was straightforward — you went to the site, you paid, you got your ticket. The festival is small, fiercely independent, set in a crater lake in the Marche region of central Italy. The kind of place where the production director publishes a public post calling himself an asshole and then proceeds to explain, in detail, exactly how the ticketing system screwed over his audience.

That post landed a few weeks ago, after the second batch of 2026 tickets sold out in minutes. The complaints were all the same: people who connected at noon sharp — or earlier — found themselves behind people who showed up five minutes late. Estimated wait times that went up instead of down. The feeling of having done everything right and still losing.

The culprit wasn't the festival or the ticketing platform. It was Queue-it, a Danish company that builds virtual waiting rooms. Ciaotickets uses it, as does most of the ticketing industry worldwide. The system works exactly as designed: when tickets go on sale, everyone in the waiting room gets a random position. First come, first served does not apply.

The director's post ended with a challenge: if any of you think you're good programmers, build something better. There are billions of dollars waiting.

I'm a programmer. I took the challenge seriously.

## Why the queue is random

To understand Queue-it's design, imagine what happens when 50,000 people click "Buy" in the same second.

In a physical line, the first person to arrive is the first to enter. Online, "first to arrive" is a slippery concept. It depends on connection latency — fiber beats 4G. It depends on browser speed. It depends on geographic distance from the server. And above all, it depends on whether you're a human still looking for the right button or a bot that fired an HTTP request in 3 milliseconds.

A pure first-come-first-served (FCFS) system under this kind of load becomes a millisecond race where bots always win and humans on slow connections always lose. Queue-it chose randomization as the fix: if everyone who connects before the sale opens gets shuffled randomly, it doesn't matter whether you arrived 3 days early or 2 minutes early. Doesn't matter if you have fiber or 3G. Doesn't matter if you're a bot.

It's a rational choice. But it has an enormous cost: it violates perceived fairness. A line that doesn't respect arrival order doesn't feel like a line. It feels like a lottery.

## The online queue trilemma

Every online queuing system has to balance three things that pull against each other:

- **Scalability**: handle tens or hundreds of thousands of simultaneous connections without the server collapsing
- **Fairness**: reward people who show up on time and penalize latecomers, without giving advantages to bots or fast connections
- **Transparency**: be understandable to the user, who needs to know why they're in that position and how long they'll wait

Queue-it picks scalability and transparency, sacrificing temporal fairness. Pure FCFS picks fairness and transparency, sacrificing resilience under extreme load. The question is: can you have all three?

## Who does what: the competitive landscape

I analyzed every major virtual queue system currently on the market. The landscape is more varied than I expected.

### Queue-it: the randomized giant

Market leader. Used by Ticketmaster, AXS, StubHub, and over 500 ticketing companies. The model is hybrid: during the pre-queue (before the sale opens), all users are collected in a waiting room. When the clock strikes, positions are assigned completely at random — a lottery. Users who arrive after the sale starts go to the back in FIFO order.

Bot protection includes Proof-of-Work (an invisible cryptographic puzzle that's trivial for a single browser but expensive to run at scale), CAPTCHA, device fingerprinting, and behavioral analysis. In real-world tests, PoW blocked between 11% and 39% of automated traffic.

### Cloudflare Waiting Room: infrastructure-level flexibility

Cloudflare offers a waiting room built into its CDN, available to Business and Enterprise customers. The key differentiator is configurability: the operator can choose between FIFO mode (with one-minute bucket grouping) and random mode. Pre-queue with optional shuffle is also supported.

Cloudflare's FIFO works by time windows: all users arriving in the same minute are in the same bucket. Bucket N must drain before bucket N+1 begins. Within the same bucket, order is not guaranteed. An interesting compromise, but the one-minute granularity is still coarse.

### CrowdHandler: transparency as a weapon

Used by the Royal Albert Hall and other British venues, CrowdHandler shows every user their exact position — "Position 247 of 3,412" — not a vague estimate. The model is strict FIFO after activation, with randomization only at the instant the queue opens. A much narrower randomization window than Queue-it.

Bot mitigation includes algorithmic anomaly detection and a session-clearing function that identifies and removes suspicious sessions (scrapers, users with no real purchase intent), freeing spots for real users.

### Queue-Fair: the FIFO purist

The industry's dissenter. Founded on a patent from 2004, Queue-Fair offers exclusively pure FIFO queues. First to arrive, first to enter. No randomization, no compromise. Their argument is simple: an online queue should work like a physical line, because that's what people expect and find intuitively fair.

The limitation is vulnerability to bots in the fractions of a second after the sale opens. Queue-Fair argues it's better to fight bots with dedicated tools than to penalize every legitimate user with a lottery system.

### SeatGeek: the proprietary approach

SeatGeek built a custom system on AWS (Lambda + DynamoDB + Fastly), publicly documented in enough detail to replicate. The model is configurable: standard FIFO but also VIP priority, where subscribers or fan club members skip the line. A pragmatic approach that acknowledges not all users have the same claim to a ticket.

## The comparison

```
+------------------+---------------------------+-----------------------+--------------------------+-----------------------+
| Feature          | Queue-it                  | Cloudflare WR         | CrowdHandler             | Queue-Fair            |
+------------------+---------------------------+-----------------------+--------------------------+-----------------------+
| Queue model      | Random + FIFO             | Configurable          | FIFO (rand. at activ.)   | Pure FIFO             |
| Pre-queue        | Yes, countdown            | Yes, opt. shuffle     | Yes, random at drop      | No                    |
| Position shown   | Estimated                 | Estimated             | Exact                    | Exact                 |
| Bot protection   | PoW/CAPTCHA/fprint/beh.   | Rate limit, CF bots   | IP intel, fprint, anom.  | Basic rate limiting   |
| Open source      | No (connectors only)      | No                    | No                       | CF/Akamai workers OSS |
| Pricing          | Enterprise (not public)   | Incl. Biz/Ent plans   | Free tier available      | Free tier available   |
+------------------+---------------------------+-----------------------+--------------------------+-----------------------+
```

## What's missing

After mapping the entire landscape, four gaps stand out. No current system addresses them well.

### 1. Granular time windows

Every system thinks in binary: either total randomization (Queue-it's pre-queue) or total FIFO (Queue-Fair). Nobody implements a time-window approach: random within the same one-minute window, but FIFO between windows. Someone who arrives at 11:55 would have priority over someone arriving at 12:02, but within the 11:55-11:56 window, positions would be random. This preserves the advantage of showing up early without rewarding the millisecond differences that favor bots.

Cloudflare comes close with its minute-based buckets, but the granularity is fixed and there's no internal randomization within the bucket — it's "order not guaranteed," which is different from "fair randomization."

### 2. Proof-of-humanity as a priority mechanism

Queue-it has Proof-of-Work, which is excellent for filtering bots. But PoW is used only as an entry filter, not as a priority mechanism. Imagine a system where completing a small challenge — not a frustrating CAPTCHA, but a lightweight cognitive micro-task — earns you a better position within your time window. Bots running thousands of parallel sessions face prohibitive computational costs. Humans, completing just one, get a small meritocratic edge.

### 3. Verifiable transparency

No system lets users verify that their position was assigned fairly. When Ticketmaster uses Queue-it, users have to trust that the randomization is actually random. And they don't trust it — accusations of manipulation and favoritism are recurring, even when the system is working correctly.

A system with cryptographic auditing — where the assignment algorithm is verifiable after the fact, like a public lottery — would eliminate suspicion at the root. The technology exists: commitment schemes and verifiable random functions (VRFs) have been used for years in blockchains and certified lotteries.

### 4. Load distribution over time

Every system accepts the noon spike as a given and focuses on surviving it. Nobody asks: what if the spike wasn't necessary?

A slot-booking mechanism — where users choose in advance when to connect and receive an advantage for picking a less crowded window — would distribute load naturally. Less popular slots become more attractive, crowded ones thin out. The server handles the load better, users wait less, and the system stays fair.

## Open source starting points

For anyone who wants to take the Montelago director's challenge seriously, open-source foundations already exist:

- **Pretix** (Python/Django + Redis + Celery): a complete ticketing system with built-in waiting room, used by the Chaos Communication Congress and thousands of events. The most mature starting point for an end-to-end system.
- **Upstash Waiting Room** (Cloudflare Workers + serverless Redis): lightweight and modern, ideal as a base for a standalone waiting room.
- **Queue-Fair Cloudflare Worker**: a pure FIFO implementation that runs for free on Cloudflare's edge network.

SeatGeek's architecture (AWS Lambda + DynamoDB + CDN) is another valuable reference — not open source, but documented in enough detail to replicate.

## The perfect queue doesn't exist yet

The problem the Montelago Celtic Festival surfaced is neither isolated nor trivial. It sits at the intersection of queueing theory, computer security, game theory, and the psychology of perceived fairness.

The current market offers solutions that work but force a choice: perceived fairness (FIFO, with its bot vulnerability) or abuse resistance (random, with the frustration it generates). The hybrid model adopted by the majority is a reasonable compromise, but it isn't the last word.

The space to innovate is real and concrete. A system combining granular time windows, proof-of-humanity as a priority mechanism, cryptographically verifiable transparency, and incentives for load distribution would be something genuinely new. It wouldn't solve the problem of people who don't get a ticket — when 50,000 people want 5,000 spots, 45,000 will be left out regardless. But it would ensure that those left out can at least say: the queue was fair.

I've been on both sides of this. Twice at Montelago, back when buying tickets meant buying tickets. And now, as a programmer, staring at a system that trades fairness for scalability and wondering if that trade is really necessary.

The director said there are billions of dollars waiting. He's probably right. The question is whether the solution comes from the companies already in the market — or from someone who's been stuck in the wrong position in a queue and decided to do something about it.
