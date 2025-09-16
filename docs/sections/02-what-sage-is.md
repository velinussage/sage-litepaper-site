# What Sage Is

Sage is a protocol that lets communities publish prompt libraries on **IPFS**, register them on-chain, and govern upgrades through their own **SubDAO**. A manifest file defines an entire library, and one proposal updates the whole set. Discoverability runs through a subgraph and an **MCP** server so agents can search and pull context directly. Interfaces include a **CLI**, a web app, and Model Context Protocol (**MCP**) endpoints for agent tooling like Claude Desktop.

-   **Publish**: Push a manifest and prompt files to **IPFS**. Get immutable CIDs.
-   **Propose**: Each manifest is one governance proposal in your **SubDAO**. Vote, queue, and execute through a Timelock.
-   **Discover**: Agents, the **CLI**, and the web app read via subgraph first and fall back to RPC.
-   **Use**: **MCP** tools return content by CID so agents can load context on demand.

This approach gives AI artists, prompt engineers, and research groups an easy path to share and store their working prompts with permanence, version history, and clear community ownership.

---
