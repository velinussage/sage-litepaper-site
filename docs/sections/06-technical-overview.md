# Technical Overview

At a high level, Sage glues together three things your community already uses:

-   On‑chain governance (Governor + Timelock) for trusted upgrades
-   IPFS for content and manifests with immutable CIDs
-   An index layer (subgraph + MCP) for search and agent access

Updates are “manifest‑first”: one proposal approves a new manifest CID and atomically updates the entire library. Agents read the subgraph first and fall back to RPC, so they always see the latest approved version.

---
