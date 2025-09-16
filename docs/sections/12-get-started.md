# Get Started

**Install and connect**
```bash
npm i -g @sage-protocol/cli
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
