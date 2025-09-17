# 📜 Sage Litepaper

> ### The first permissionless protocol for incentivized agent context sharing.

Sage is a governance-powered protocol for community-owned agent instructions. Publish once to **IPFS**, let your **SubDAO** steward upgrades, and let agents automatically discover the trusted version. As the network's distributed intelligence improves, rewards route back to the people training it. Follow the founder [@VelinusSage](https://x.com/VelinusSage) for updates.

---

## Why Now?

AI models evolve weekly; agent instructions rarely keep pace. Agent instructions and prompt libraries are still scattered across chats, docs, and private repos. As models shift, even well-tested agent instructions drift out of sync, and communities lose the ability to coordinate their agent fleets. Sage focuses on four persistent gaps:

1.  **No Shared Memory for Agents**  
    Everyone forks ad hoc copies of their agent instructions; there’s no governed, tamper-evident version that humans and agents can trust together.

2.  **Static Instructions Fall Behind**  
    Markets, models, and tooling evolve weekly. Yesterday’s prompts quietly break, and orchestration stalls without a governed path to ship updates.

3.  **Contributors Lose Attribution**  
    Reuse happens without provenance or revenue share, so the people training the network rarely see upside.

4.  **No Compounding Incentive Loop**  
    Communities lack a transparent way to pool funds, reward experiments, and reinvest the learnings so the collective intelligence plateaus.

> Sage exists to turn community knowledge into governed, composable intelligence that compounds.

---

## What Sage Is

Sage is a governance layer for distributed intelligence, turning community prompt libraries into coordinated agent instructions. Publish once to **IPFS**, register the library on-chain, and let your **SubDAO** steer how agents pull, trust, and evolve that context. A manifest defines the full collection of prompts, and a single proposal upgrades the whole set. Discovery runs through a subgraph and an **MCP** server so agents can search and synchronize without manual glue code. Interfaces include a **CLI**, a web app, and Model Context Protocol (**MCP**) endpoints for agent tooling like Claude Desktop.

-   **Publish**: Push manifests and prompt files to **IPFS**. Immutable CIDs establish the authorized set of agent instructions.
-   **Propose**: Each manifest is one governance proposal in your **SubDAO**. Vote, queue, and execute through a Timelock.
-   **Discover**: Agents, the **CLI**, and the web app read via subgraph first and fall back to RPC for a consistent view.
-   **Use**: **MCP** tools return content by CID so agents can orchestrate tasks with the community-approved version.

This approach turns simple prompt libraries into governed, self-improving agent instructions for communities of AI artists, prompt engineers, and research collectives so they can coordinate agent behavior with clear ownership.

---

## What Makes It Different

-   **Community-Governed Intelligence**  
    Each community spins up a **SubDAO** with its own library, treasury, and upgrade cadence. Forks, remixes, and attribution happen in the open, so distributed intelligence stays transparent and aligned.

-   **Manifest-First Upgrades**  
    Ship atomic updates to the entire library in one proposal. Governance encodes the bounds, agents inherit the updated instructions, and everyone moves together.

-   **Incentives for Learning**  
    **Boosts**, **Bounties**, and **Premiums** route value to the contributors training the network. Treasuries become self-improving capital that compounds as the distributed intelligence gets better.

-   **Metaprompting Co-Pilot**  
    The CLI guides contributors through system-driven metaprompting, tapping distributed intelligence to surface reusable instructions. Use `sage prompt generate` to turn a simple idea into a structured asset ready for review.

-   **Agent-Native Discovery**  
    The **MCP** server exposes search, fetch, and manifest validation. Agents query Sage like an API, retrieve the approved context, and execute without brittle middleware.

-   **Production-Ready on Base**  
    Contracts, subgraph, and flows run on Base Sepolia today, with a gated path to Base mainnet so communities can scale in a credibly neutral environment.

---

## The Self-Improving Metaprompting Loop

1.  **Publish**  
    Authors codify collective knowledge into human-readable manifests. **IPFS** CIDs anchor the canonical version for humans and agents alike.

2.  **Curate**  
    The community proposes variants, votes, and executes upgrades on-chain. Approver Councils can be badge-gated to fast-track scoped changes while governance stays in charge.

3.  **Reward**  
    **Boosts** pay voters or contributors for high-signal interventions. **Bounties** fund targeted experiments. **Premiums** monetize specialized instructions. Treasury routes and guardrails stay programmable through governance.

4.  **Use and Measure**  
    Agents fetch context via **MCP**, execute within approved bounds, and feed results back through on-chain signals like forks, bounty completions, and proposal outcomes that close the learning loop.

---

## Core Components

-   **On-chain Governance**  
    **SubDAO** Factory, Governor + Timelock, LibraryRegistry, PromptRegistry, and Treasury modules provide the guardrails for how agent instructions evolve, plus optional **LBP** and **Bonding** integrations for liquidity.

-   **Persistent Shared Memory**  
    **IPFS** stores payloads, while subgraph-first reads keep the **CLI**, web app, and **MCP** endpoints aligned on the latest approved manifest.

-   **Tooling for Distributed Intelligence**  
    A full **CLI**, a discovery app, and an **MCP** stdio server (with HTTP mode) connect human editors and automated agents to the same governed knowledge base, orchestrating metaprompting sessions along the way.

---

## Technical Overview

At a high level, Sage combines three familiar building blocks:

-   On‑chain governance (Governor + Timelock) for trusted upgrades
-   IPFS for content and manifests with immutable CIDs
-   An index layer (subgraph + MCP) for search and agent access

Updates are “manifest‑first”: one proposal approves a new manifest CID and atomically updates the entire library. Agents read the subgraph first and fall back to RPC, so they always see the latest approved version.

---

## Incentives and Ownership

Sage powers three on‑chain incentive rails that communities can combine.

### 1. Boosts

Parameterizable rewards for governance participation or contributor actions. Two manager contracts exist:

-   Direct manager for per‑voter payouts tied to a proposal.
-   Merkle manager for pooled funding and claim‑by‑proof.

Both paths are governed through the **SubDAO** Timelock. The **CLI** supports `create`, `fund`, `set-root`, `status`, `claim`, and `finalize`.

### 2. Bounties

Announce tasks, award winners, and pay out from the Timelock. This system is event-only by design. Fund the Timelock with ETH or an ERC‑20 before executing payout proposals.

### 3. Premium Prompts

Encrypt content client-side, pin to **IPFS**, and gate decryption with Lit v7 and ERC‑1155 receipts. Buyers pay in USDC, get a receipt NFT, and decrypt locally with session signatures. Pricing and treasury routing are on‑chain. No reveal server is needed.

### Paid Pinning Revenue

When libraries are pushed with paid pinning, the service receives USDC and calls on-chain attribution. The default split routes 80% to the **SubDAO** treasury and 20% to the protocol treasury.

In production, an HTTP‑native payment flow (x402) can collect USDC at request time and attribute proceeds automatically. For communities, this means: pay once to persist content; revenue lands transparently in your treasury.

### SBTs and Badge‑Gated Fast Tracks

Non‑transferable **SBTs** recognize contributors and can gate Approver Council permissions to move quickly on scoped updates, with function selectors allow‑listed by governance.

---

## Governance Modes (Simple)

Communities can start simple and evolve their governance shape over time:

-   Bootstrap: member list with proposal cooldowns and refundable deposits to prevent spam.
-   Token: standard ERC20Votes quorum using SAGE or a SubDAO stake token.
-   Operator: trusted multisig or owner executes via Timelock for fast iteration.

The CLI can plan/apply role changes safely through proposals or Safe transactions.

---

## For Communities

-   **AI Artists and Prompt Engineers**  
    Store instructions permanently with **IPFS** CIDs, track versions, and get discovery out of the box. Add premium entries when you want to offer high-effort sets.

-   **Research Groups and Guilds**  
    Use **Bounties** for new methods, **Boosts** for review cycles, and **SBTs** for reputation. Fork libraries when styles or standards diverge.

-   **Agent Builders**  
    Query the subgraph or **MCP** to pull the latest approved context and keep agents in sync as libraries evolve.

---

## Why Base



In plain terms: Base keeps fees low, and has the most active community for AI‑adjacent projects today. That means cheaper governance, faster experiments, and better discovery for new libraries.

---

## Security and Launch Status

-   **Security Model**  
    All writes flow through a Governor to a Timelock. Emergency pause, least-privilege roles, and upgrade paths are governance-controlled.

-   **Testnet Readiness**  
    Fully working end-to-end on Base Sepolia, including library updates, governance, treasury demos, **MCP**, and the app.

-   **Audits & Reviews**: Contracts follow standard OZ Governor/Timelock patterns; external audits and public review precede mainnet.
-   **Role Boundaries**: Sensitive actions route through the Timelock; council modules can allowlist function selectors for scoped, badge‑gated fast tracks.
-   **Operational Hygiene**: Default timelock delays, proposal cooldowns, and per‑address caps reduce spam and operational risk during bootstrap.

---

## Token and Treasury, in Plain Terms

The Sage economy is designed around a few core principles to create a self-sustaining ecosystem:

-   **Treasury Growth:** The protocol's main treasury is funded by a one-time **LBP** launch and ongoing **bond** sales. This ensures the long-term financial health and stability of the `SAGE` token.
-   **Creator Rewards:** **SubDAOs** receive grants from the main treasury and use those funds to post **bounties**. This creates a direct, work-to-earn loop for prompt engineers and other contributors.
-   **Community Governance:** `SAGE` token holders stake their tokens in **SubDAOs** to vote on content curation and community decisions, ensuring that the most valuable context is promoted and rewarded.
-   **Fixed Supply**: SAGE targets a fixed 1B supply at genesis with deflationary burns tied to creation/forking where appropriate. No inflation.
-   **Treasury Bootstrapping**: A public **LBP** plus optional bond sales seed protocol‑owned liquidity and long‑term reserves; SubDAOs may receive grants.
-   **Coordination over Fees**: Tokens primarily coordinate long‑horizon work (governance, reputation, commitment burns) rather than charging per‑prompt usage.

---

## Metaprompting CLI

The Sage **CLI** guides contributors through system-driven metaprompting sessions, pulling from distributed intelligence to suggest reusable agent instructions and formatting them for everyday tools.

-   **Discover**: `sage context pull` syncs the latest approved libraries into Cursor, Windsurf, or plain Markdown so people and agents share the same context.
-   **Iterate**: `sage prompt generate` and companion commands propose updated instructions that the network can reuse and iterate on.
-   **Ship**: Validate manifests locally, pin to **IPFS**, and open governance proposals without leaving the terminal.

This keeps the governance loop fast while letting the network learn from each metaprompting cycle.

---

## Get Started

**Connect**
```bash
sage wallet connect --type cast
sage doctor
```

**Publish a library**

```bash
sage library scaffold-manifest
sage library lint manifest.json
sage library push manifest.json --pin
sage library propose manifest.json --subdao 0xYourSubDAO
```

**Run the MCP server for agents**

```bash
node cli/mcp-server-stdio.js
# or start HTTP and set NEXT_PUBLIC_MCP_HTTP_URL
```

Tools include: `search_onchain_prompts`, `get_prompt_content`, `list_subdaos`, `get_library_manifests`.

**Offer a premium prompt**

```bash
sage premium-pre authsig --out ./authSig.json
sage premium-pre publish --in ./prompt.md --name "Title" --description "Desc" \
  --subdao 0xYourSubDAO --price 2.50 --auth-sig ./authSig.json
```

**Incentivize participation**

```bash
# Direct manager, per-voter
sage boost create --governor 0xGov --proposal-id 1 --per-voter 250000 --max-voters 100 --min-votes 1

# Merkle pool
sage boost fund --proposal-id 1 --amount 25000000
sage boost set-root --manager 0xMerkle --proposal-id 1 --root 0xRoot
```

**Set up SBTs and an Approver Council**

```bash
sage sbt propose-mint --to 0xContributor --badge 1 --uri ipfs://CID
sage council set-config --badge $SBT --badge-id 1 --target $PROMPT_REGISTRY
sage council allow --selector addForkedPrompt(string,string,string,string,address)
```

---

## Roadmap

*   Completed
    SubDAO factory, Library and Prompt registries, governance flows, **Boosts**, **Premiums**, **SBTs**, **MCP**, **CLI**, and web app are live on Base Sepolia.

*   **In Progress**
    Full testnet launch with airdrop incentives and Discord; **CLI** V2 with meta prompting agent, Fjord partnership, and web app.

*   **Mainnet**
    Execute the launch sequence, wire canonical liquidity, and transition ownership entirely to DAO contracts.

*   **Growth**
    First community libraries in creative AI, research, and agent ops. Grants and **bounties** focused on subjective domains where human curation matters most.

---

## License

MIT. See the repository for full docs, guides, and examples.
