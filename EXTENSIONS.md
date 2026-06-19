# Extension Catalog


**Total: 23 extensions · 184 commands**

_23 extensions available in this catalog. Generated from `catalog.json`._

Install any extension into a Spec-Kit project:

```bash
export SPECKIT_CATALOG_URL="https://raw.githubusercontent.com/nareshsiriveri/sketchkit/main/catalog.json"
specify extension add <id>
```

| Extension | id | Ver | Commands | Description |
|-----------|----|-----|---------:|-------------|
| ACME Hello | `acme-hello` | 0.1.0 | 1 | Sample org extension that adds a greeting slash command. Replace with your real extension… |
| ADR Logger | `adr-logger` | 0.1.0 | 2 | Create and maintain Architecture Decision Records from the Spec-Kit workflow. |
| claude-for-msft-365-install | `claude-for-msft-365-install` | 0.1.5 | 6 | Provision direct cloud access (Vertex AI, Bedrock, or LLM gateway) for the Claude Office … |
| Coverage Gate | `coverage-gate` | 0.1.0 | 1 | Enforce a minimum test-coverage threshold via a command and a lifecycle hook. |
| earnings-reviewer | `earnings-reviewer` | 0.1.1 | 7 | Earnings call and filings to model update to note draft |
| equity-research | `equity-research` | 0.1.2 | 18 | Equity research tools: earnings analysis, initiating coverage reports, and research workf… |
| financial-analysis | `financial-analysis` | 0.1.1 | 20 | Core financial modeling and analysis tools: DCF, comps, LBO, 3-statement models, competit… |
| fund-admin | `fund-admin` | 0.1.0 | 6 | Fund administration and finance ops skills: GL reconciliation, break tracing, accruals, r… |
| gl-reconciler | `gl-reconciler` | 0.1.0 | 5 | Finds breaks, traces root cause, routes for sign-off |
| investment-banking | `investment-banking` | 0.2.1 | 16 | Investment banking productivity tools: client and market insights, deck creation, financi… |
| kyc-screener | `kyc-screener` | 0.1.0 | 4 | Parses onboarding docs, runs the rules engine, flags gaps |
| lseg | `lseg` | 1.0.0 | 16 | Price bonds, analyze yield curves, evaluate FX carry trades, value options, and build mac… |
| market-researcher | `market-researcher` | 0.1.1 | 6 | Sector or theme to industry overview, competitive landscape, peer comps, and ideas shortl… |
| meeting-prep-agent | `meeting-prep-agent` | 0.1.1 | 5 | Briefing pack before every client meeting |
| model-builder | `model-builder` | 0.1.0 | 7 | DCF, LBO, 3-statement, comps - live in Excel |
| month-end-closer | `month-end-closer` | 0.1.0 | 6 | Accruals, roll-forwards, variance commentary |
| operations | `operations` | 0.1.0 | 2 | Operational workflows: KYC document parsing and rules-grid evaluation |
| pitch-agent | `pitch-agent` | 0.1.1 | 12 | Comps, precedents, LBO to a branded pitch deck, end to end |
| private-equity | `private-equity` | 0.1.2 | 20 | Private equity deal sourcing and workflow tools: company discovery, CRM integration, and … |
| sp-global | `sp-global` | 1.0.1 | 3 | S&P Global - Financial data and analytics skills including company tearsheets, earnings p… |
| statement-auditor | `statement-auditor` | 0.1.0 | 4 | Audits pre-generated LP statements before distribution |
| valuation-reviewer | `valuation-reviewer` | 0.1.1 | 5 | Ingests GP packages, runs valuation template, stages LP reporting |
| wealth-management | `wealth-management` | 0.1.2 | 12 | Wealth management and financial advisory tools: client reviews, financial planning, portf… |

---

## Details


### ACME Hello (`acme-hello`)

Sample org extension that adds a greeting slash command. Replace with your real extensions.

- **Install:** `specify extension add acme-hello`
- **Version:** 0.1.0 · **Tags:** sample, hello
- **Commands (1):**
  - `/speckit.acme-hello.greet` — Greet the user and confirm the ACME Hello extension is active.

### ADR Logger (`adr-logger`)

Create and maintain Architecture Decision Records from the Spec-Kit workflow.

- **Install:** `specify extension add adr-logger`
- **Version:** 0.1.0 · **Tags:** documentation, adr, governance
- **Commands (2):**
  - `/speckit.adr-logger.new` — Create a new Architecture Decision Record in docs/adr/.
  - `/speckit.adr-logger.list` — List all Architecture Decision Records and their status.

### claude-for-msft-365-install (`claude-for-msft-365-install`)

Provision direct cloud access (Vertex AI, Bedrock, or LLM gateway) for the Claude Office add-in. Generates the customized add-in manifest, walks through Azure admin consent, and writes per-user config via Microsoft Graph extension attributes.

- **Install:** `specify extension add claude-for-msft-365-install`
- **Version:** 0.1.5 · **Tags:** financial-services
- **Commands (6):**
  - `/speckit.claude-for-msft-365-install.bootstrap` — Build the bootstrap endpoint — per-user MCP servers, skills, dynamic config
  - `/speckit.claude-for-msft-365-install.consent` — Azure admin consent URLs — one-time tenant approval for Entra SSO and Outlook Gr
  - `/speckit.claude-for-msft-365-install.debug` — Diagnose deployment issues (stale config, connect failures, missing add-in)
  - `/speckit.claude-for-msft-365-install.manifest` — Generate the add-in manifest XML with your cloud config baked in
  - `/speckit.claude-for-msft-365-install.setup` — Setup wizard — provision Vertex/Bedrock/Foundry/gateway, admin consent, generate
  - `/speckit.claude-for-msft-365-install.update-user-attrs` — Set per-user config (tokens, region overrides) via Azure AD extension attributes

### Coverage Gate (`coverage-gate`)

Enforce a minimum test-coverage threshold via a command and a lifecycle hook.

- **Install:** `specify extension add coverage-gate`
- **Version:** 0.1.0 · **Tags:** quality, testing, coverage
- **Commands (1):**
  - `/speckit.coverage-gate.check` — Report current test coverage and whether it meets the threshold.

### earnings-reviewer (`earnings-reviewer`)

Earnings call and filings to model update to note draft

- **Install:** `specify extension add earnings-reviewer`
- **Version:** 0.1.1 · **Tags:** financial-services
- **Commands (7):**
  - `/speckit.earnings-reviewer.audit-xls` — Audit a spreadsheet for formula accuracy, errors, and common mistakes. Scopes to
  - `/speckit.earnings-reviewer.earnings-analysis` — Create professional equity research earnings update reports (8-12 pages, 3,000-5
  - `/speckit.earnings-reviewer.earnings-preview` — Build pre-earnings analysis with estimate models, scenario frameworks, and key m
  - `/speckit.earnings-reviewer.model-update` — Update financial models with new data — quarterly earnings, management guidance,
  - `/speckit.earnings-reviewer.morning-note` — Draft concise morning meeting notes summarizing overnight developments, trade id
  - `/speckit.earnings-reviewer.xlsx-author` — Produce a .xlsx file on disk (headless) instead of driving a live Excel workbook
  - `/speckit.earnings-reviewer.agent-earnings-reviewer` — Processes an earnings event end to end — reads the call transcript and filings, 

### equity-research (`equity-research`)

Equity research tools: earnings analysis, initiating coverage reports, and research workflows

- **Install:** `specify extension add equity-research`
- **Version:** 0.1.2 · **Tags:** financial-services
- **Commands (18):**
  - `/speckit.equity-research.catalysts` — View or update the catalyst calendar
  - `/speckit.equity-research.earnings-preview` — Build a pre-earnings preview with scenarios
  - `/speckit.equity-research.earnings` — Analyze quarterly earnings and create an earnings update report
  - `/speckit.equity-research.initiate` — Create an initiating coverage report
  - `/speckit.equity-research.model-update` — Update a financial model with new data
  - `/speckit.equity-research.morning-note` — Draft a morning meeting note
  - `/speckit.equity-research.screen` — Run a stock screen or generate investment ideas
  - `/speckit.equity-research.sector` — Create a sector overview report
  - `/speckit.equity-research.thesis` — Create or update an investment thesis
  - `/speckit.equity-research.catalyst-calendar` — Build and maintain a calendar of upcoming catalysts across a coverage universe —
  - `/speckit.equity-research.earnings-analysis` — Create professional equity research earnings update reports (8-12 pages, 3,000-5
  - `/speckit.equity-research.earnings-preview-skill` — Build pre-earnings analysis with estimate models, scenario frameworks, and key m
  - `/speckit.equity-research.idea-generation` — Systematic stock screening and investment idea sourcing. Combines quantitative s
  - `/speckit.equity-research.initiating-coverage` — Create institutional-quality equity research initiation reports through a 5-task
  - `/speckit.equity-research.model-update-skill` — Update financial models with new data — quarterly earnings, management guidance,
  - `/speckit.equity-research.morning-note-skill` — Draft concise morning meeting notes summarizing overnight developments, trade id
  - `/speckit.equity-research.sector-overview` — Create comprehensive industry and sector landscape reports covering market dynam
  - `/speckit.equity-research.thesis-tracker` — Maintain and update investment theses for portfolio positions and watchlist name

### financial-analysis (`financial-analysis`)

Core financial modeling and analysis tools: DCF, comps, LBO, 3-statement models, competitive analysis, and deck QC

- **Install:** `specify extension add financial-analysis`
- **Version:** 0.1.1 · **Tags:** financial-services
- **Commands (20):**
  - `/speckit.financial-analysis.3-statement-model` — Fill out a 3-statement financial model template
  - `/speckit.financial-analysis.competitive-analysis` — Create a competitive landscape analysis
  - `/speckit.financial-analysis.comps` — Build a comparable company analysis with trading multiples
  - `/speckit.financial-analysis.dcf` — Build a DCF valuation model with comps-informed terminal multiples
  - `/speckit.financial-analysis.debug-model` — Debug and audit a financial model for errors
  - `/speckit.financial-analysis.lbo` — Build an LBO model for a PE acquisition
  - `/speckit.financial-analysis.ppt-template` — Create a reusable PPT template skill from a PowerPoint template file
  - `/speckit.financial-analysis.3-statement-model-skill` — Complete, populate and fill out 3-statement financial model templates (Income St
  - `/speckit.financial-analysis.audit-xls` — Audit a spreadsheet for formula accuracy, errors, and common mistakes. Scopes to
  - `/speckit.financial-analysis.clean-data-xls` — Clean up messy spreadsheet data — trim whitespace, fix inconsistent casing, conv
  - `/speckit.financial-analysis.competitive-analysis-skill` — Framework for building competitive landscape decks — market positioning, competi
  - `/speckit.financial-analysis.comps-analysis` — Build institutional-grade comparable company analyses with operating metrics, va
  - `/speckit.financial-analysis.dcf-model` — Real DCF (Discounted Cash Flow) model creation for equity valuation. Retrieves f
  - `/speckit.financial-analysis.deck-refresh` — Updates a presentation with new numbers — quarterly refreshes, earnings updates,
  - `/speckit.financial-analysis.ib-check-deck` — Investment banking presentation quality checker. Reviews a pitch deck or client-
  - `/speckit.financial-analysis.lbo-model` — This skill should be used when completing LBO (Leveraged Buyout) model templates
  - `/speckit.financial-analysis.ppt-template-creator` — Creates self-contained PPT template SKILLS (not presentations) from user-provide
  - `/speckit.financial-analysis.pptx-author` — Produce a .pptx file on disk (headless) instead of driving a live PowerPoint doc
  - `/speckit.financial-analysis.skill-creator` — Guide for creating effective skills. This skill should be used when users want t
  - `/speckit.financial-analysis.xlsx-author` — Produce a .xlsx file on disk (headless) instead of driving a live Excel workbook

### fund-admin (`fund-admin`)

Fund administration and finance ops skills: GL reconciliation, break tracing, accruals, roll-forwards, variance commentary, NAV tie-out

- **Install:** `specify extension add fund-admin`
- **Version:** 0.1.0 · **Tags:** financial-services
- **Commands (6):**
  - `/speckit.fund-admin.accrual-schedule` — Build the period-end accrual schedule — for each accrual, compute the entry, cit
  - `/speckit.fund-admin.break-trace` — Root-cause a reconciliation break to its source transaction or posting — follow 
  - `/speckit.fund-admin.gl-recon` — Reconcile general ledger to subledger for a trade date or period — match at the 
  - `/speckit.fund-admin.nav-tieout` — Tie an LP statement to the fund's NAV pack — recompute the LP's capital account 
  - `/speckit.fund-admin.roll-forward` — Build a roll-forward schedule for a balance-sheet account — beginning balance pl
  - `/speckit.fund-admin.variance-commentary` — Write flux commentary for every P&L and balance-sheet line over threshold — curr

### gl-reconciler (`gl-reconciler`)

Finds breaks, traces root cause, routes for sign-off

- **Install:** `specify extension add gl-reconciler`
- **Version:** 0.1.0 · **Tags:** financial-services
- **Commands (5):**
  - `/speckit.gl-reconciler.audit-xls` — Audit a spreadsheet for formula accuracy, errors, and common mistakes. Scopes to
  - `/speckit.gl-reconciler.break-trace` — Root-cause a reconciliation break to its source transaction or posting — follow 
  - `/speckit.gl-reconciler.gl-recon` — Reconcile general ledger to subledger for a trade date or period — match at the 
  - `/speckit.gl-reconciler.xlsx-author` — Produce a .xlsx file on disk (headless) instead of driving a live Excel workbook
  - `/speckit.gl-reconciler.agent-gl-reconciler` — Reconciles general ledger to subledger across asset classes for a trade date — f

### investment-banking (`investment-banking`)

Investment banking productivity tools: client and market insights, deck creation, financial analysis, and transaction management

- **Install:** `specify extension add investment-banking`
- **Version:** 0.2.1 · **Tags:** financial-services
- **Commands (16):**
  - `/speckit.investment-banking.buyer-list` — Build a buyer universe for a sell-side process
  - `/speckit.investment-banking.cim` — Draft a Confidential Information Memorandum
  - `/speckit.investment-banking.deal-tracker` — Track and review live deal pipeline
  - `/speckit.investment-banking.merger-model` — Build an accretion/dilution merger model
  - `/speckit.investment-banking.one-pager` — Create a one-page company strip profile using branded PPT template
  - `/speckit.investment-banking.process-letter` — Draft a process letter or bid instructions
  - `/speckit.investment-banking.teaser` — Draft an anonymous one-page teaser
  - `/speckit.investment-banking.buyer-list-skill` — Build and organize a universe of potential acquirers for sell-side M&A processes
  - `/speckit.investment-banking.cim-builder` — Structure and draft a Confidential Information Memorandum for sell-side M&A proc
  - `/speckit.investment-banking.datapack-builder` — Build professional financial services data packs from various sources including 
  - `/speckit.investment-banking.deal-tracker-skill` — Track multiple live deals with milestones, deadlines, action items, and status u
  - `/speckit.investment-banking.merger-model-skill` — Build accretion/dilution analysis for M&A transactions. Models pro forma EPS imp
  - `/speckit.investment-banking.pitch-deck` — Populates investment banking pitch deck templates with data from source files. U
  - `/speckit.investment-banking.process-letter-skill` — Draft process letters and bid instructions for sell-side M&A processes. Covers i
  - `/speckit.investment-banking.strip-profile` — Creates professional investment banking strip profiles (company profiles) for pi
  - `/speckit.investment-banking.teaser-skill` — Draft anonymous one-page company teasers for sell-side M&A processes. Creates a 

### kyc-screener (`kyc-screener`)

Parses onboarding docs, runs the rules engine, flags gaps

- **Install:** `specify extension add kyc-screener`
- **Version:** 0.1.0 · **Tags:** financial-services
- **Commands (4):**
  - `/speckit.kyc-screener.kyc-doc-parse` — Parse an investor or client onboarding packet into structured KYC fields — ident
  - `/speckit.kyc-screener.kyc-rules` — Apply the firm's KYC/AML rules grid to a parsed onboarding record — assign a ris
  - `/speckit.kyc-screener.xlsx-author` — Produce a .xlsx file on disk (headless) instead of driving a live Excel workbook
  - `/speckit.kyc-screener.agent-kyc-screener` — Parses an onboarding document packet, runs the firm's KYC/AML rules engine, scre

### lseg (`lseg`)

Price bonds, analyze yield curves, evaluate FX carry trades, value options, and build macro dashboards using LSEG financial data and analytics.

- **Install:** `specify extension add lseg`
- **Version:** 1.0.0 · **Tags:** financial-services
- **Commands (16):**
  - `/speckit.lseg.analyze-bond-basis` — Analyze the bond futures basis with CTD identification, implied repo rate, and b
  - `/speckit.lseg.analyze-bond-rv` — Analyze a bond's relative value vs yield curves and credit spreads with scenario
  - `/speckit.lseg.analyze-fx-carry` — Evaluate FX carry trade opportunities with spot, forwards, vol surface, and hist
  - `/speckit.lseg.analyze-option-vol` — Analyze option volatility with vol surface, Greeks, and implied vs realized vol 
  - `/speckit.lseg.analyze-swap-curve` — Analyze the swap curve with government and inflation overlays to identify curve 
  - `/speckit.lseg.macro-rates` — Build a macro and rates dashboard with economic indicators, yield curves, inflat
  - `/speckit.lseg.research-equity` — Generate a comprehensive equity research snapshot with consensus estimates, fund
  - `/speckit.lseg.review-fi-portfolio` — Review a fixed income portfolio with pricing, reference data, cashflows, and sce
  - `/speckit.lseg.bond-futures-basis` — Analyze the bond futures basis by pricing futures, identifying the cheapest-to-d
  - `/speckit.lseg.bond-relative-value` — Perform relative value analysis on bonds by combining pricing, yield curve conte
  - `/speckit.lseg.equity-research` — Generate comprehensive equity research snapshots combining analyst consensus est
  - `/speckit.lseg.fixed-income-portfolio` — Review fixed income portfolios by pricing multiple bonds, retrieving reference d
  - `/speckit.lseg.fx-carry-trade` — Evaluate FX carry trade opportunities by combining spot rates, forward points, i
  - `/speckit.lseg.macro-rates-monitor` — Build macroeconomic and rates dashboards combining macro indicators, yield curve
  - `/speckit.lseg.option-vol-analysis` — Analyze option volatility by combining vol surface data, option pricing with Gre
  - `/speckit.lseg.swap-curve-strategy` — Analyze the interest rate swap curve by pricing swaps at multiple tenors, overla

### market-researcher (`market-researcher`)

Sector or theme to industry overview, competitive landscape, peer comps, and ideas shortlist

- **Install:** `specify extension add market-researcher`
- **Version:** 0.1.1 · **Tags:** financial-services
- **Commands (6):**
  - `/speckit.market-researcher.competitive-analysis` — Framework for building competitive landscape decks — market positioning, competi
  - `/speckit.market-researcher.comps-analysis` — Build institutional-grade comparable company analyses with operating metrics, va
  - `/speckit.market-researcher.idea-generation` — Systematic stock screening and investment idea sourcing. Combines quantitative s
  - `/speckit.market-researcher.pptx-author` — Produce a .pptx file on disk (headless) instead of driving a live PowerPoint doc
  - `/speckit.market-researcher.sector-overview` — Create comprehensive industry and sector landscape reports covering market dynam
  - `/speckit.market-researcher.agent-market-researcher` — Produces sector or thematic market research — industry overview, competitive lan

### meeting-prep-agent (`meeting-prep-agent`)

Briefing pack before every client meeting

- **Install:** `specify extension add meeting-prep-agent`
- **Version:** 0.1.1 · **Tags:** financial-services
- **Commands (5):**
  - `/speckit.meeting-prep-agent.client-report` — Generate professional client-facing performance reports with portfolio returns, 
  - `/speckit.meeting-prep-agent.client-review` — Prepare for client review meetings with portfolio performance summary, allocatio
  - `/speckit.meeting-prep-agent.investment-proposal` — Create professional investment proposals for prospective clients. Covers the fir
  - `/speckit.meeting-prep-agent.pptx-author` — Produce a .pptx file on disk (headless) instead of driving a live PowerPoint doc
  - `/speckit.meeting-prep-agent.agent-meeting-prep-agent` — Builds a briefing pack before a client or prospect meeting — relationship histor

### model-builder (`model-builder`)

DCF, LBO, 3-statement, comps - live in Excel

- **Install:** `specify extension add model-builder`
- **Version:** 0.1.0 · **Tags:** financial-services
- **Commands (7):**
  - `/speckit.model-builder.3-statement-model` — Complete, populate and fill out 3-statement financial model templates (Income St
  - `/speckit.model-builder.audit-xls` — Audit a spreadsheet for formula accuracy, errors, and common mistakes. Scopes to
  - `/speckit.model-builder.comps-analysis` — Build institutional-grade comparable company analyses with operating metrics, va
  - `/speckit.model-builder.dcf-model` — Real DCF (Discounted Cash Flow) model creation for equity valuation. Retrieves f
  - `/speckit.model-builder.lbo-model` — This skill should be used when completing LBO (Leveraged Buyout) model templates
  - `/speckit.model-builder.xlsx-author` — Produce a .xlsx file on disk (headless) instead of driving a live Excel workbook
  - `/speckit.model-builder.agent-model-builder` — Builds DCF, LBO, three-statement, and trading-comps models live in Excel from a 

### month-end-closer (`month-end-closer`)

Accruals, roll-forwards, variance commentary

- **Install:** `specify extension add month-end-closer`
- **Version:** 0.1.0 · **Tags:** financial-services
- **Commands (6):**
  - `/speckit.month-end-closer.accrual-schedule` — Build the period-end accrual schedule — for each accrual, compute the entry, cit
  - `/speckit.month-end-closer.audit-xls` — Audit a spreadsheet for formula accuracy, errors, and common mistakes. Scopes to
  - `/speckit.month-end-closer.roll-forward` — Build a roll-forward schedule for a balance-sheet account — beginning balance pl
  - `/speckit.month-end-closer.variance-commentary` — Write flux commentary for every P&L and balance-sheet line over threshold — curr
  - `/speckit.month-end-closer.xlsx-author` — Produce a .xlsx file on disk (headless) instead of driving a live Excel workbook
  - `/speckit.month-end-closer.agent-month-end-closer` — Runs the month-end close for an entity — accruals, roll-forwards, and variance c

### operations (`operations`)

Operational workflows: KYC document parsing and rules-grid evaluation

- **Install:** `specify extension add operations`
- **Version:** 0.1.0 · **Tags:** financial-services
- **Commands (2):**
  - `/speckit.operations.kyc-doc-parse` — Parse an investor or client onboarding packet into structured KYC fields — ident
  - `/speckit.operations.kyc-rules` — Apply the firm's KYC/AML rules grid to a parsed onboarding record — assign a ris

### pitch-agent (`pitch-agent`)

Comps, precedents, LBO to a branded pitch deck, end to end

- **Install:** `specify extension add pitch-agent`
- **Version:** 0.1.1 · **Tags:** financial-services
- **Commands (12):**
  - `/speckit.pitch-agent.3-statement-model` — Complete, populate and fill out 3-statement financial model templates (Income St
  - `/speckit.pitch-agent.audit-xls` — Audit a spreadsheet for formula accuracy, errors, and common mistakes. Scopes to
  - `/speckit.pitch-agent.comps-analysis` — Build institutional-grade comparable company analyses with operating metrics, va
  - `/speckit.pitch-agent.dcf-model` — Real DCF (Discounted Cash Flow) model creation for equity valuation. Retrieves f
  - `/speckit.pitch-agent.deck-refresh` — Updates a presentation with new numbers — quarterly refreshes, earnings updates,
  - `/speckit.pitch-agent.ib-check-deck` — Investment banking presentation quality checker. Reviews a pitch deck or client-
  - `/speckit.pitch-agent.lbo-model` — This skill should be used when completing LBO (Leveraged Buyout) model templates
  - `/speckit.pitch-agent.pitch-deck` — Populates investment banking pitch deck templates with data from source files. U
  - `/speckit.pitch-agent.pptx-author` — Produce a .pptx file on disk (headless) instead of driving a live PowerPoint doc
  - `/speckit.pitch-agent.sector-overview` — Create comprehensive industry and sector landscape reports covering market dynam
  - `/speckit.pitch-agent.xlsx-author` — Produce a .xlsx file on disk (headless) instead of driving a live Excel workbook
  - `/speckit.pitch-agent.agent-pitch-agent` — End-to-end investment banking pitch agent. Given a target company and a strategi

### private-equity (`private-equity`)

Private equity deal sourcing and workflow tools: company discovery, CRM integration, and founder outreach

- **Install:** `specify extension add private-equity`
- **Version:** 0.1.2 · **Tags:** financial-services
- **Commands (20):**
  - `/speckit.private-equity.ai-readiness` — Scan the portfolio for the highest-leverage AI opportunities
  - `/speckit.private-equity.dd-checklist` — Generate a due diligence checklist
  - `/speckit.private-equity.dd-prep` — Prep for a diligence meeting or expert call
  - `/speckit.private-equity.ic-memo` — Draft an investment committee memo
  - `/speckit.private-equity.portfolio` — Review portfolio company performance
  - `/speckit.private-equity.returns` — Build IRR/MOIC sensitivity tables
  - `/speckit.private-equity.screen-deal` — Screen an inbound deal (CIM or teaser)
  - `/speckit.private-equity.source` — Source deals — discover companies and draft founder outreach
  - `/speckit.private-equity.unit-economics` — Analyze unit economics (ARR cohorts, LTV/CAC, retention)
  - `/speckit.private-equity.value-creation` — Build a post-acquisition value creation plan
  - `/speckit.private-equity.ai-readiness-skill` — Scan the portfolio for the highest-leverage AI opportunities and rank where to d
  - `/speckit.private-equity.dd-checklist-skill` — Generate and track comprehensive due diligence checklists tailored to the target
  - `/speckit.private-equity.dd-meeting-prep` — Prepare for due diligence meetings — management presentations, expert network ca
  - `/speckit.private-equity.deal-screening` — Quickly screen inbound deal flow — CIMs, teasers, and broker materials — against
  - `/speckit.private-equity.deal-sourcing` — PE deal sourcing workflow — discover target companies, check CRM for existing re
  - `/speckit.private-equity.ic-memo-skill` — Draft a structured investment committee memo for PE deal approval. Synthesizes d
  - `/speckit.private-equity.portfolio-monitoring` — Track and analyze portfolio company performance against plan. Ingests monthly/qu
  - `/speckit.private-equity.returns-analysis` — Build quick IRR/MOIC sensitivity tables for PE deal evaluation. Models returns a
  - `/speckit.private-equity.unit-economics-skill` — Analyze unit economics for PE targets — ARR cohorts, LTV/CAC, net retention, pay
  - `/speckit.private-equity.value-creation-plan` — Structure post-acquisition value creation plans with revenue, cost, and operatio

### sp-global (`sp-global`)

S&P Global - Financial data and analytics skills including company tearsheets, earnings previews, and transaction summaries

- **Install:** `specify extension add sp-global`
- **Version:** 1.0.1 · **Tags:** sp-global, finance, capital-iq, tearsheets, earnings, transactions, excel
- **Commands (3):**
  - `/speckit.sp-global.earnings-preview-beta` — Generate a concise 4-5 page equity research earnings preview for a single compan
  - `/speckit.sp-global.funding-digest` — Generate a polished one-page PowerPoint slide summarizing key takeaways from rec
  - `/speckit.sp-global.tear-sheet` — Generate professional company tear sheets using S&P Capital IQ data via the Kens

### statement-auditor (`statement-auditor`)

Audits pre-generated LP statements before distribution

- **Install:** `specify extension add statement-auditor`
- **Version:** 0.1.0 · **Tags:** financial-services
- **Commands (4):**
  - `/speckit.statement-auditor.audit-xls` — Audit a spreadsheet for formula accuracy, errors, and common mistakes. Scopes to
  - `/speckit.statement-auditor.nav-tieout` — Tie an LP statement to the fund's NAV pack — recompute the LP's capital account 
  - `/speckit.statement-auditor.xlsx-author` — Produce a .xlsx file on disk (headless) instead of driving a live Excel workbook
  - `/speckit.statement-auditor.agent-statement-auditor` — Audits a batch of pre-generated LP capital-account statements against the fund N

### valuation-reviewer (`valuation-reviewer`)

Ingests GP packages, runs valuation template, stages LP reporting

- **Install:** `specify extension add valuation-reviewer`
- **Version:** 0.1.1 · **Tags:** financial-services
- **Commands (5):**
  - `/speckit.valuation-reviewer.ic-memo` — Draft a structured investment committee memo for PE deal approval. Synthesizes d
  - `/speckit.valuation-reviewer.portfolio-monitoring` — Track and analyze portfolio company performance against plan. Ingests monthly/qu
  - `/speckit.valuation-reviewer.returns-analysis` — Build quick IRR/MOIC sensitivity tables for PE deal evaluation. Models returns a
  - `/speckit.valuation-reviewer.xlsx-author` — Produce a .xlsx file on disk (headless) instead of driving a live Excel workbook
  - `/speckit.valuation-reviewer.agent-valuation-reviewer` — Ingests GP valuation packages for a fund, runs them through the valuation templa

### wealth-management (`wealth-management`)

Wealth management and financial advisory tools: client reviews, financial planning, portfolio analysis, and client reporting

- **Install:** `specify extension add wealth-management`
- **Version:** 0.1.2 · **Tags:** financial-services
- **Commands (12):**
  - `/speckit.wealth-management.client-report` — Generate a client performance report
  - `/speckit.wealth-management.client-review` — Prep for a client review meeting
  - `/speckit.wealth-management.financial-plan` — Build or update a financial plan
  - `/speckit.wealth-management.proposal` — Create an investment proposal for a prospect
  - `/speckit.wealth-management.rebalance` — Analyze drift and generate rebalancing trades
  - `/speckit.wealth-management.tlh` — Identify tax-loss harvesting opportunities
  - `/speckit.wealth-management.client-report-skill` — Generate professional client-facing performance reports with portfolio returns, 
  - `/speckit.wealth-management.client-review-skill` — Prepare for client review meetings with portfolio performance summary, allocatio
  - `/speckit.wealth-management.financial-plan-skill` — Build or update a comprehensive financial plan covering retirement projections, 
  - `/speckit.wealth-management.investment-proposal` — Create professional investment proposals for prospective clients. Covers the fir
  - `/speckit.wealth-management.portfolio-rebalance` — Analyze portfolio allocation drift and generate rebalancing trade recommendation
  - `/speckit.wealth-management.tax-loss-harvesting` — Identify tax-loss harvesting opportunities across taxable accounts. Finds positi
