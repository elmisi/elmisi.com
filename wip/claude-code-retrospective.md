# Claude Code Retrospective

*Cosa ho scoperto facendo analizzare il mio modo di lavorare a Claude Code stesso.*

---

Uso Claude Code da oltre un anno. 77 progetti, un plugin di automazione che ho costruito io, account Max, effort level high, permessi aperti, voice abilitata. Non sono un utente che sta imparando — sono uno che costruisce sopra lo strumento.

Eppure c'è un problema che mi accompagna da mesi: **l'80% dei piani che Claude produce non mi soddisfa**. Si concentra su dettagli irrilevanti e trascura le cose che per me contano. Ho sempre pensato fosse un limite del modello. Poi ho fatto una cosa che non avevo mai fatto: ho chiesto a Claude di fare una retrospettiva su come lavoro.

## Il setup

Ho preso la [Claude Code Ultimate Guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) — 23.000 righe di documentazione, 219 template, guide su architettura, sicurezza, workflow — e ho chiesto: "basandoti su quello che sai di me e su questo riferimento, cosa potrebbe migliorare il mio modo di lavorare?"

L'idea era semplice: usare la guida come benchmark per capire se mi mancava qualcosa.

Il risultato non è stato quello che mi aspettavo.

## La scoperta: Claude conosce la mappa ma non la bussola

Ho fatto leggere a Claude tutti i miei file di memoria — 22 MEMORY.md distribuiti sui vari progetti. Sono dettagliati: architetture, comandi di deploy, path SSH, bug risolti con root cause, dipendenze cross-repo. Li uso come runbook operativi e funzionano bene per quello scopo.

Ma Claude ha notato un pattern che io non vedevo: **i miei file di memoria dicono COSA sono le cose, mai PERCHÉ mi importano**.

Esempio concreto. Ho un ecosistema di microservizi interconnessi. La memoria documenta ogni servizio: stack, porta, database, comando di deploy. Quando chiedo a Claude di pianificare una modifica all'infrastruttura, lui sa *come* si fa il deploy — ha tutte le informazioni tecniche. Ma non sa che la mia priorità è **verificare l'impatto sui servizi collegati prima di scrivere una riga di codice**. Quindi il piano si concentra sulla configurazione (che sa fare bene) invece che sulla verifica d'impatto (che è quello che mi interessa).

Il piano è tecnicamente corretto. Ma non è il piano che farei io.

## Feedback che muore con la sessione

C'è un progetto — un sistema IoT complesso con hardware, firmware, backend e app mobile — dove la memoria funziona particolarmente bene. Il motivo è che ci ho salvato dei **feedback specifici**: "non proporre soluzioni senza test preliminari verificati", "leggi sempre la documentazione dell'ecosistema prima di rispondere".

Quei feedback sono il tipo di contesto che rende i piani migliori. Dicono a Claude non solo cosa fare, ma come ragionare.

Il problema? Gli altri 20 progetti non hanno feedback. Le correzioni che do a Claude — "no, non così", "prima verifica", "questo è irrilevante" — muoiono con la sessione. E il pattern che mi frustra è lo stesso ovunque: Claude propone prima di verificare, si concentra sul "come fare" invece che sul "cosa conta".

Ho sempre dato la colpa al modello. In realtà il modello non ha il contesto per fare diversamente.

## Il mio CLAUDE.md globale: 2 righe

Quando ho guardato il mio file di configurazione globale — quello che Claude carica in ogni sessione, su ogni progetto — c'erano due regole:

1. Gestisci il versioning semantico
2. Non metterti come co-autore nei commit

Tutto qui. Nessuna indicazione su come ragiono, cosa prioritizzo, quali errori mi fanno perdere tempo. Claude parte ogni sessione sapendo che uso semver e che non voglio il suo nome nei commit. Nient'altro su di me.

## Cosa ho trovato di utile nella guida

Su 23.000 righe, le cose concretamente rilevanti per il mio caso sono circa 200, distribuite in 3 file. Il resto è per chi sta imparando lo strumento.

**Il pattern "Annotation Cycle"** (`guide/workflows/plan-driven.md`). Invece di chiedere un piano e poi spiegare verbalmente cosa non va, il piano viene scritto in un file markdown condiviso. Io annoto direttamente nel file — commento, cancello, aggiungo domande. Claude rilegge le mie annotazioni e riscrive. Il loop continua finché non ci sono più domande aperte. Il file diventa uno stato condiviso tra me e l'agente, non una conversazione che si perde.

**Il framework FIRE per incident response** (`guide/ops/devops-sre.md`). Quattro step pensati per chi è solo con 15 servizi in produzione alle 3 di notte. Sintomo in 30 secondi, diagnostica guidata, gate di approvazione prima di qualsiasi azione, postmortem automatico. Non è un workflow astratto — è una checklist operativa che posso mettere nel CLAUDE.md e avere disponibile quando serve.

**Context engineering modulare** (`guide/core/context-engineering.md`). Invece di un CLAUDE.md monolitico per progetto, regole che si caricano solo quando lavori in una specifica directory. Il backend ha le sue regole, l'infrastruttura le sue, il frontend le sue. Claude carica solo il contesto rilevante per quello che stai facendo in quel momento.

## La mia filosofia, confermata

La mia posizione è sempre stata: **non devo imparare io ad usare lo strumento. Lo strumento si deve adattare a me.**

Questa retrospettiva non l'ha cambiata — l'ha raffinata. Lo strumento si adatta a me nella misura in cui io gli dico chi sono. Non sto parlando di leggere guide o imparare comandi. Sto parlando di scrivere 10 righe nel file giusto:

- Quando pianifichi, parti sempre da: cosa può rompersi?
- Mai proporre un piano senza verificare l'impatto sui servizi collegati
- Le mie priorità: funzionante > elegante > ottimizzato
- Se non sei sicuro, chiedimi. Non inventare.
- I piani devono essere brevi: 3-5 step. Se servono più step, il task è troppo grande.

Queste non sono istruzioni tecniche. Sono il mio modo di ragionare, esternalizzato in un file che Claude legge prima di ogni sessione. È la differenza tra avere un collaboratore che sa fare il deploy e avere uno che sa cosa mi importa.

## Il takeaway

Dopo un anno di uso intenso, il mio vero collo di bottiglia non era una feature mancante o un pattern che non conoscevo. Era che **ogni sessione partiva senza sapere come penso**.

I file di memoria documentavano il mondo. Ma non documentavano la mia bussola.

---

*Guida usata come riferimento: [Claude Code Ultimate Guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) (v3.37.5)*

---

# Claude Code Retrospective (English)

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
