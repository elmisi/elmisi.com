# Plan: Follow-up article — "A Fistful of Token$"

## Title and slug (locked)

- **Title**: *A Fistful of Token$*
- **Subtitle (optional)**: *The Currency the Missing Variable Missed*
- **Slug / filename**: `a-fistful-of-tokens.md` → `src/content/blog/a-fistful-of-tokens.md`
- **Publish date**: the day the plan is approved (set at commit time).

The title is a direct nod to Sergio Leone's *Per un pugno di dollari* (1964). The whole article inherits that movie's frame — see "Voice and structural metaphor" below.

## Goal (what this article is)

A direct sequel to `the-missing-variable.md` that adds a **third scenario** the first article didn't consider:

1. **Scenario A** (from the first article): consumer capitalism saved by some form of redistribution (UBI, credits, vouchers) — "digital feudalism with Prime delivery."
2. **Scenario B** (from the first article): oligarchies bifurcate the economy — an automated circuit for owners of real assets, subsistence for everyone else.
3. **Scenario C (NEW)**: money itself mutates. The primary unit of value stops being fiat currency and starts being **tokens** — the input/output units of LLM inference. Not as a metaphor ("tokens are the new oil") but as an actual medium of exchange, settlement, and account.

The article extends the missing-variable frame rather than replacing it: Scenario C is **compatible** with the oligarchic transition — it could actually be the **settlement layer** of Scenario B.

## Voice and structural metaphor: Sergio Leone

The article is narrated with the voice of a spaghetti western. Not as decoration — as scaffolding. Leone's *Fistful of Dollars* is the structural backbone:

**Film → Article mapping**

- **Small Mexican town at war** → the 2028 transition.
- **The Baxters and the Rojos** (two rival families burning the town to the ground) → the two scenarios of the first article. Scenario A vs. Scenario B. Two factions convinced they are opposites; both paying in the same old currency.
- **The Stranger (Man with No Name)** → the compute owner / oligarch. Rides into town, sizes up both factions, sells his services to each, profits from both.
- **The chest of gold** (taken from the Mexican soldiers) → token production capacity. Whoever controls it sets the terms.
- **The fistful of dollars** (what the Stranger takes from both sides) → the new currency. Paid in by both factions, accumulated by one actor.
- **The steel chest plate under the poncho** → the conversion of financial wealth into real assets (farmland, energy, compute). Ramón empties his Winchester into the Stranger's chest and nothing happens. Same mechanic as Phase 2 of the missing-variable article: the crash destroys the middle class, bounces off the oligarchy.
- **Ramón's Winchester running out of ammo** → fiat-denominated consumer demand running out of referent once labor stops being the productive input.
- **The Stranger vanishing at the end** → the post-crisis repositioning. The town is ash, the Stranger is gone, the new rules arrive with whoever rides in next.

Voice: taciturn, cinematic, dry, a little cold. Per memory: rough and direct, not academic. Morricone in the background, not a Davos keynote.

**Hard constraint: readable without the movie.** A reader who has never seen *A Fistful of Dollars* must still follow the whole argument. The Leone names (Baxters, Rojos, the Stranger, Ramón) are introduced once with a parenthetical gloss and then used as shorthand. Every Leone beat is also stated in plain economic terms in the same paragraph. The frame colors the prose; it is never load-bearing on its own.

## Relationship to `the-missing-variable.md`

- Open by explicitly naming it as a follow-up and restating the two-scenario frame of the original in ~2 short paragraphs — framed as "the two families."
- Reuse the data vocabulary: "$300-350B AI capex", "tokens-per-watt", "AI factory", "who owns the output of machine intelligence?"
- Keep the original's roman-numeral section structure, data tables, and data-dense anchoring. The Leone register is in the prose, not in a loss of rigor.
- The closing line of the original — *"who owns the mine?"* — gets a matching closing line here in a movie-paraphrase register.

## The source of the idea (user asked me to find it)

The "tokens = currency" idea is **not original** and the article should say so explicitly. The primary articulation is by **Jensen Huang (Nvidia CEO)**, developed across 2024-2026:

- **GTC keynote (March 2026)**: "tokens are the new commodity", "AI factory revenues = tokens-per-watt", "every unused watt is revenue lost."
- **Dwarkesh Podcast (2026)**: compressed the business to one sentence — *"The input is electron, the output is tokens. That is in the middle Nvidia."*
- **Nvidia blog**: "AI tokens: the language and currency powering modern AI."
- **Huang's internal framing**: engineers earning $500K/year should consume ~$250K/year of tokens, or they're underutilizing the tool. He is **already treating tokens as a unit of labor budget.**

Adjacent voices that built the discourse (the supporting chorus — we should credit them):

- **Morgan Stanley (2026)**: "NVIDIA's Jensen Huang on compute as a new economic engine."
- **Deloitte Insights**: "AI tokens: how to navigate AI's new spend dynamics" (frames tokens as a new line item in corporate budgets, climbing the hierarchy relative to hourly human labor).
- **AEI**: "Algorithms, Compute, and the Rise of 'Tokenomics'."
- **SemiAnalysis**: "Tokenomics Model" — economic model of token production costs.
- **SDxCentral / BuildShift / RCRWireless**: inference economy / tokens as the new currency of AI.
- **Medium long-form**: Eduardo Alvarez "What are LLM tokens worth?", Gilad Barkan (Wix Engineering) "The Emerging Economy of LLMs", zhaolongzhong "Summary of LLM Token Economies", "Peerism: Skill Token Economy for Post-Capitalism" (crypto-flavored take).
- **Crypto-native angle**: "AI-Agent Economy" / autonomous wallets — machine-to-machine payment between AI agents.

The article will **take the idea, drop the commercials**: credit Huang as the person who articulated it clearly, then move on. No Nvidia marketing framing, no "is this a sales pitch?" meta-commentary. The idea stands on its own once lifted out of the keynote deck.

## Approach

Structure mirrors the original article: numbered sections, data-dense, short. Roughly **2,500-3,500 words** (the original is ~3,000).

**Voice**: Leone-inflected. Short sentences. Dry. A little coldness. The narrator is the Stranger, not the lecturer. Keep it rough and direct (per memory), don't sand the edges. No academic hedging.

**Core arc:**

1. Restate the missing-variable dichotomy → identify the unexamined assumption both scenarios share: *that money remains fiat.*
2. Introduce the token-as-currency thesis, credit Huang/Nvidia explicitly, summarize the discourse.
3. Stress-test: could tokens actually function as money? Apply the three classical functions (unit of account / medium of exchange / store of value) + a fourth (unit of *cognitive work*, which fiat never had).
4. Can you buy bread with tokens? Can you buy a house? Walk through the concrete cases the user asked about.
5. The flow: who produces, who consumes, who clears, who settles. Map the actors.
6. One token or many? Monetary pluralism — different "token classes" with different powers (reasoning tokens, image tokens, agent-action tokens, verification tokens).
7. Plug back into the missing-variable scenario: is token-money Scenario A-compatible (saves consumers) or Scenario B-compatible (accelerates concentration)? Argue it's structurally **Scenario B's settlement layer**.
8. Closing aphorism matching the original's cadence.

## Detailed Changes

### File location

- Create: `src/content/blog/a-fistful-of-tokens.md`
- Frontmatter must match the schema in `src/content.config.ts` (title, date, description, tags).

### Frontmatter (draft)

```yaml
---
title: "A Fistful of Token$"
date: <approval date>
description: "A follow-up to The Missing Variable. The 2028 transition doesn't just rewrite the economy — it may rewrite money itself. Two families, a stranger, and a currency nobody was counting."
tags: ["ai", "economics", "money", "tokens", "oligarchy"]
---
```

### Section outline with talking points

Below, each section lists what goes in it, with evidence/data already collected. This is the skeleton I will flesh out after the plan is approved.

---

#### Preface — "The town had two families" (4-6 sentences)

- Open with the Leone cold-open: a town, two families at war (the Baxters and the Rojos), a stranger on the ridge.
- Name the Baxters = Scenario A, the Rojos = Scenario B from `the-missing-variable.md`.
- Flag that the first article mapped the war but didn't ask what currency the bodies were being counted in.
- Announce the thesis: a third reading of the town, one where the currency itself changes while the two families are still shooting at each other.
- One-line credit: *the "tokens as currency" idea belongs to Jensen Huang.* Move on.

**Disambiguation block (first 500 words, mandatory)**: state plainly that "token" in this article means **LLM input/output tokens**, not ERC-20 crypto tokens. Crypto has borrowed the word; we are not talking about coins on a chain.

#### I. What Both Families Assumed

- Scenario A (Baxters) assumes UBI / consumption credits, denominated in dollars.
- Scenario B (Rojos) assumes the bifurcation still settles in dollars — land deeds, energy contracts, compute leases, all in fiat.
- Both assume the **unit of account** survives the transition. They disagree about who owns what; they agree on what "what" is priced in.
- But fiat is a *claim on labor-hours in a labor economy*. Take the labor economy away and the claim loses its referent. The bullet still comes out of the gun, but there's nothing on the other end of it.
- This is the gap the stranger rides into.

#### II. Electricity In, Tokens Out

- Quote the Dwarkesh line: *"The input is electron, the output is tokens."* — then get out of the way.
- Nvidia GTC 2026: AI factory revenue = tokens-per-watt. Every unused watt is revenue lost.
- Huang's $500K / $250K ratio: an engineer earning half a million a year should consume a quarter million in tokens. **Tokens are already a budget line inside a major company.** That's the part to linger on — not Huang himself.
- Morgan Stanley, Deloitte, AEI: all operationalizing this in corporate and policy finance.
- Don't meta-comment on Nvidia's incentive to push the frame. Use the idea, drop the commercial.

**Cited artifacts table** (mirror the Nvidia/Walmart table from the original):

```
+-------------------+-------------------------+------------------------+
| Actor             | Claim                   | Source                 |
+-------------------+-------------------------+------------------------+
| Jensen Huang      | tokens = new commodity  | GTC 2026 keynote       |
| Jensen Huang      | electrons -> tokens     | Dwarkesh Podcast 2026  |
| Deloitte Insights | tokens climbing the     | "AI tokens spend       |
|                   | corp budget hierarchy   |  dynamics" report      |
| Nvidia blog       | tokens = AI currency    | blogs.nvidia.com       |
| SemiAnalysis      | tokenomics cost model   | semianalysis.com       |
| AEI               | "rise of tokenomics"    | aei.org                |
+-------------------+-------------------------+------------------------+
```

All URLs go into the Data Sources footer at the bottom, not inline — keeps the prose clean (same pattern as the original article).

#### III. Is a Token Actually Money?

Test the idea against the classical three functions, then add a fourth:

- **Unit of account**: already happening. API pricing, enterprise budgets, corporate capex all contain token line items. ✓
- **Medium of exchange**: partial. Currently B2B only (you pay a vendor in dollars who pays for tokens). The machine-to-machine economy (autonomous agents with wallets) is the first case of tokens moving *between* entities as actual payment. Mostly theoretical as of 2026, but concrete prototypes exist.
- **Store of value**: fails. Tokens are perishable — they expire when consumed and have no natural storage form. But: **prepaid token balances are becoming a storage form** (OpenAI credits, Anthropic workspace budgets). Compare to prepaid minutes in mobile-telephony economies of the 2000s (Kenya's M-Pesa emerged from exactly this substrate).
- **Unit of cognitive work** (new function): fiat never had this. A token is a *measurable quantum of intelligence-production*, which is unprecedented. This is why Huang can say engineers should consume $X of tokens — he's denominating productivity in a unit fiat can't express.

Key insight: tokens are **not yet money** but they are **already a parallel unit of account** for cognitive work, and that's the slot from which historical currencies have emerged (tallies, beaver pelts, rice, salt, cigarettes in POW camps — all started as units of account before becoming media of exchange).

#### IV. Can You Buy Bread With Tokens? Can You Buy a House?

Walk through three concrete cases from cheapest to most structural:

**Bread (~€2)**
- Price of 2€ in tokens at 2026 rates: ~200K-2M tokens of a mid-tier model.
- Feasible technically (prepaid token balance → card-like settlement).
- But: the baker has no use for tokens unless she can **convert them** to something she needs. If the baker uses AI in her business (supply chain, accounting, marketing generation), she already has a token demand. If she doesn't, tokens are useless to her and she'll either refuse or convert at a haircut.
- **Threshold**: bread-for-tokens becomes viable the moment >50% of small-business operating cost is token-denominated. Not there yet; arguably ≤5 years away in some sectors.

**A month's rent (~€1,000)**
- Landlord side: landlords already pay for property management AI, maintenance scheduling, tenant screening, legal generation. The conversion friction is smaller.
- Middle case: most likely first major consumer use.

**A house (~€300,000)**
- Totally different problem. A house is a store-of-value asset; tokens are perishable.
- Unless: a **non-consumable token instrument** (a claim on future token production — like a bond secured by an AI factory's output) is invented. This is structurally identical to **oil-linked bonds** or **electricity futures**. There's no conceptual barrier.
- Gulf sovereigns are already positioned to issue them: Saudi PIF, MGX, G42 all have the capital infrastructure. Stargate is essentially a token-production bond in disguise.

The pattern: **tokens work for flow, claims-on-tokens work for stock.** Same split as electricity vs. energy futures.

#### V. The Flow — Who Produces, Who Consumes, Who Clears

Map the actors explicitly (mirror the geopolitical section of the original):

- **Producers**: Nvidia (chips), TSMC (fabrication), hyperscalers (Microsoft, Google, Amazon, Meta, Oracle), Gulf sovereigns (financing and siting), utilities / nuclear operators (energy input), model labs (OpenAI, Anthropic, Google DeepMind, xAI, DeepSeek).
- **Issuers of denominated balances**: model labs + API aggregators (the "banks" of the token economy).
- **Consumers**: corporations (first, already happening), individuals (via subscriptions today, possibly via wallets tomorrow), **other AIs** (machine-to-machine, the fastest-growing segment).
- **Clearing layer**: today, fiat conversions happen via corporate credit cards and invoicing. Tomorrow, either (a) native token-to-token clearing between labs, or (b) a crypto-based settlement layer (the "AI-agent wallets" narrative).
- **Regulators**: nearly absent today. *To be verified at draft time: spot-check BIS / ECB / Fed for any published notes on token balances as monetary aggregates.* Mark as unverified in the draft if nothing material shows up.

Draw the diagram as ASCII (matching the terminal aesthetic):

```
[ energy ] --> [ chips ] --> [ data centers ] --> [ models ]
                                                     |
                                                     v
                                          [ token production ]
                                                     |
                             +-----------------------+-----------------------+
                             |                       |                       |
                      corporate consumers     consumer subscriptions   M2M agent economy
                             |                       |                       |
                             +-----------------------+-----------------------+
                                                     |
                                        [ clearing / settlement ]
                                              (fiat today,
                                              token-native tomorrow?)
```

#### VI. One Token or Many?

Argue there will be **monetary pluralism**, not a single coin:

- **Reasoning tokens** (thinking / hidden CoT tokens): expensive, high-power, equivalent to "premium money" — analog to gold.
- **Plain inference tokens**: everyday cash.
- **Image / audio / video tokens**: specialized currencies tied to specific use-cases, like *occupational monies* in historical economies.
- **Agent-action tokens** (tool-use, browsing, code-exec): *transaction fees*, not money — closer to gas in blockchain systems.
- **Verification tokens** (proof-carrying inference): a trust premium, priced higher because they embed attestation.

Historical parallel: medieval Europe had multiple co-circulating currencies (gold for sovereigns, silver for merchants, copper for peasants). Exchange rates between classes floated. We're heading toward something similar: **token classes stratified by model capability, with floating exchange rates between them.** This would mean whoever operates the **frontier model** effectively sets monetary policy for the top tier — and whoever controls the conversion between classes is the post-capital central bank.

This rhymes with the missing-variable article's thesis: **AI companies would wield influence comparable to today's central banks.** The article already flagged this — we're pressure-testing the mechanism.

#### VII. The Stranger Sells to Both Families

The payoff section. Use the Leone frame explicitly: the Stranger sells his gun to the Baxters and to the Rojos. Same weapon, two buyers, one profit. What does that look like in 2028?

- If UBI-style redistribution is eventually issued in **tokens**: the oligarchy doesn't need to hand out *dollars* (which still buy hard assets). It hands out *tokens*, which can only be consumed, not accumulated into ownership. **Dependents by design.** That's Scenario A — dressed down to Scenario B's terms. The Baxters think they won; they pay in the Stranger's coin.
- If tokens become a **real store of value** (via claim-instruments), whoever issues the instrument is a post-sovereign central bank. Saudi PIF, MGX, BlackRock, Nvidia itself — candidates already on the board in the original article. That's the Rojos — paid in the Stranger's coin.
- The stranger gets both fistfuls. The town burns in fiat.
- Middle-class exposure: as in 2008, they hold the old settlement asset (fiat savings, pensions) while the new settlement asset is being minted elsewhere. Phase 2 of the missing-variable article, now with a second loss layer: not just financial-asset destruction, but *denomination obsolescence.*
- Steel chest plate: the conversion of financial wealth into real assets (farmland, nuclear, compute) already documented in the original article is exactly the move that makes the oligarchy bullet-proof when the fiat Winchester empties. Ramón keeps firing. The Stranger keeps standing.

**Transition sentence (draft):**
*Currency is usually the last thing people imagine changing. That's why, when it changes, it finds most people with the wrong kind of money in their pockets.*

#### VIII. Closing — locked

Short. Matches the cadence of the original's *"who owns the mine?"* close, in Leone register.

**Closing line (approved):**

> *The town had two families. Both were paying the stranger. Neither was counting in the right currency.*

No alternatives. This is the ending the article builds toward.

### Data Sources and Methodology footer

Mirror the footer of the original article. List:
- Jensen Huang GTC 2026 keynote
- Dwarkesh Podcast episode with Jensen Huang (2026)
- Nvidia blog: "AI tokens: the language and currency powering modern AI"
- Morgan Stanley: "NVIDIA's Jensen Huang on compute as a new economic engine" (2026)
- Deloitte Insights: "AI tokens: how to navigate AI's new spend dynamics"
- AEI: "Algorithms, Compute, and the Rise of 'Tokenomics'"
- SemiAnalysis: Tokenomics Model
- Computerworld: "Nvidia CEO Huang talks up 'tokenomics'"
- RCRWireless: "Agents, inference and the new token economics"
- Tom's Hardware: Huang on engineer token consumption
- Medium pieces (Eduardo Alvarez, Gilad Barkan, zhaolongzhong, Peerism)
- The original article: `the-missing-variable.md` (internal link)

## Edge Cases and Risks

- **Risk: looking derivative.** This is an extension of someone else's idea (Huang's). If I don't name the source up-front, it reads like I'm pretending to have invented it.
  - Mitigation: preface explicitly credits Huang in one line; Section II is titled after his framing.
  - Exit clause: if the Leone voice pulls the attribution off the page, we add a single-line footnote under the title: *"The 'tokens as currency' frame is Jensen Huang's. This article is what happens when you take it seriously."*

- **Risk: the Leone frame reads as gimmick.** If every section opens with a cowboy metaphor, the article turns into cosplay and loses the analytical bite of the original.
  - Mitigation: Leone imagery anchors the *spine* (preface, sections I and VII, closing) and is sparse in the middle data-dense sections. The metaphor loads the weight where it counts; the data sections stay dry.
  - Exit clause: if a draft reader says "too much western," cut Leone references in sections II-VI entirely, keep them only in the preface/I/VII/closing.

- **Risk: too much speculation, too little data.** The original article was data-dense (Top 1% wealth share, productivity vs. wages, capex figures). Scenario C is necessarily more speculative.
  - Mitigation: anchor every speculation to a present-day fact — API pricing, Huang's $250K/engineer quote, Deloitte's corp-budget observation. No empty futurism.
  - Exit clause: if the article still reads too speculative after first draft, cut Section VI (one vs many tokens) as the most speculative and move it to a separate future article.

- **Risk: crypto contamination.** "Token" in existing discourse heavily means "crypto token." We are **not** talking about ERC-20s. The article must disambiguate in the first 500 words or half the audience will misread the whole thing.
  - Mitigation: the disambiguation block lives at the end of the Preface (single location, no duplication). One paragraph: "In this article, 'token' means an LLM input/output unit. Not a crypto coin. When crypto tokens are relevant they are named explicitly."

- **Risk: length creep.** Original is ~3,000 words. This covers more speculative ground. Risk of bloat.
  - Mitigation: hard cap at 3,500 words. Cut Section VI first if needed.

## Failure Modes and Degradation

- **If the research sources disagree or contradict** (e.g. Huang said X in GTC but Y on Dwarkesh): surface the contradiction explicitly rather than smoothing it. That's a feature of the voice.
- **If a fact can't be verified** before publish (like "central banks have not taken a position"): mark inline as *unverified* in the draft; don't state it as fact.
- **If the article can't convincingly connect back to the missing-variable scenario** in Section VII: the whole thing is just a Nvidia explainer. The connection IS the article. If Section VII doesn't land, kill the draft and rethink.

## Plan status

**APPROVED — ready to execute.**

All planning decisions are locked:
- Title: *A Fistful of Token$*
- Subtitle: *The Currency the Missing Variable Missed*
- Slug: `a-fistful-of-tokens.md`
- Voice: Leone-inflected, readable without having seen the film
- Leone metaphor load: heavy in Preface/I/VII/VIII, light in II-VI
- Closing line: *"The town had two families. Both were paying the stranger. Neither was counting in the right currency."*
- Nvidia commercial framing: dropped
- Crypto disambiguation: one paragraph at the end of the Preface
- ASCII diagrams: keep both (artifacts table in II, flow diagram in V)
- Data sources: consolidated footer at the bottom, no inline URLs
- Publish date: day of commit

## Pre-draft verifications (must clear before writing)

Three factual assumptions must be checked against primary sources before the draft is written. None block the plan's structure; all block quoting with confidence.

1. **Dwarkesh Podcast quote** — verify the exact wording of *"The input is electron, the output is tokens, that in the middle is Nvidia"* against the episode transcript. If the wording differs, use the verbatim version.
2. **Huang $500K / $250K ratio** — trace back through Tom's Hardware to the original keynote or memo. Quote the primary source, not the report.
3. **Central-bank stance on token aggregates** — spot-check BIS, ECB, Fed publications for any reference to token balances as monetary aggregates. If nothing material exists, state "as of publish date, no published position" in Section V. If something exists, integrate it.

## Execution checklist

Sequential. Each step is self-contained. Check off as you go.

**Phase 0 — Planning**
- [x] Research the source of the idea (Huang + supporting chorus).
- [x] Annotation round 1 processed (8 user notes).
- [x] Annotation round 2 processed (3 user notes), all decisions locked.

**Phase 1 — Pre-draft verification**
- [ ] Verify Dwarkesh "electron / tokens" quote against transcript.
- [ ] Verify Huang $500K / $250K ratio against primary source (not Tom's Hardware).
- [ ] Spot-check BIS / ECB / Fed for token-as-monetary-aggregate references.

**Phase 2 — Draft (in this order)**
- [ ] Create `src/content/blog/a-fistful-of-tokens.md` with locked frontmatter; set `date` to commit day.
- [ ] Write Preface + crypto-disambiguation closing paragraph. ~150 words.
- [ ] Write Section I — "What Both Families Assumed." ~250 words.
- [ ] Write Section II — "Electricity In, Tokens Out" + cited-artifacts ASCII table. ~400 words.
- [ ] Write Section III — three functions of money + fourth function. ~450 words.
- [ ] Write Section IV — bread / rent / house walkthrough. ~500 words.
- [ ] Write Section V — producers/consumers/clearing + ASCII flow diagram. ~400 words.
- [ ] Write Section VI — monetary pluralism. ~350 words.
- [ ] Write Section VII — "The Stranger Sells to Both Families" + transition sentence. ~450 words.
- [ ] Write Section VIII — locked closing line. ≤50 words.
- [ ] Write Data Sources and Methodology footer (mirror original article).

**Phase 3 — Review and ship**
- [ ] Read end-to-end. Word count must be ≤ 3,500. If over, cut Section VI first.
- [ ] Verify Leone names are each glossed once in plain terms (Baxters/Rojos/Stranger/Ramón).
- [ ] Verify every speculative claim is anchored to a present-day fact.
- [ ] Verify crypto disambiguation is present before the first use of "token" in Section II.
- [ ] `npm run build` locally — confirm content collection picks up the new file.
- [ ] `npm run dev` — spot-check rendering at `/blog/a-fistful-of-tokens`.
- [ ] Bump `VERSION` (MINOR — new content) and update `CHANGELOG.md`.
- [ ] Commit: `Add blog article: A Fistful of Token$` (include VERSION, CHANGELOG, new article file).

## Article-level acceptance criteria

The draft is ready to ship when all of the following are true:

- A reader who has never seen Leone's film can follow every argument.
- The connection back to `the-missing-variable.md` is explicit in Sections I and VII.
- No sentence treats Nvidia's commercial motive as a topic.
- The closing line is exactly the locked sentence, unchanged.
- Word count between 2,500 and 3,500.
- Every numeric claim cites its source in the footer.
- The three pre-draft verifications have been cleared (or marked *unverified* inline where appropriate).
