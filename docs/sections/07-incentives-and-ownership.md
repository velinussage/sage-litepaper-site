# Incentives and Ownership

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
