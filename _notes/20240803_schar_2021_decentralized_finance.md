---
title: "Schar, Fabian. \"Decentralized Finance: On Blockchain and Smart Contract-Based Financial Markets.\" Federal Reserve Bank of St. Louis Review, Second Quarter 2021, 103(2), pp. 153-74."
collection: notes
type: "Post"
permalink: /notes/20240803_schar_2021_decentralized_finance
date: 2024-08-03
---

**Abstract**

```
Decentralized finance (DeFi) is a blockchain-based financial infrastructure that has recently gained a lot of traction. The term generally refers to an open, permissionless, and highly interoperable protocol stack built on public smart contract platforms, such as the Ethereum blockchain (see Buterin, 2013). It replicates existing financial services in a more open and transparent way. In particular, DeFi does not rely on intermediaries and centralized institutions. Instead, it is based on open protocols and decentralized applications (DApps). Agreements are enforced by code, transactions are executed in a secure and verifiable way, and legitimate state changes persist on a public blockchain. Thus, this architecture can create an immutable and highly interoperable financial system with unprecedented transparency, equal access rights, and little need for custodians, central clearing houses, or escrow services, as most of these roles can be assumed by “smart contracts.” The term decentralized finance (DeFi) refers to an alternative financial infrastructure built on top of the Ethereum blockchain. DeFi uses smart contracts to create protocols that replicate existing financial services in a more open, interoperable, and transparent way. This article highlights opportunities and potential risks of the DeFi ecosystem. I propose a multi-layered framework to analyze the implicit architecture and the various DeFi building blocks, including token standards, decentralized exchanges, decentralized debt markets, blockchain derivatives, and on-chain asset management protocols. I con- clude that DeFi still is a niche market with certain risks but that it also has interesting properties in terms of efficiency, transparency, accessibility, and composability. As such, DeFi may potentially contribute to a more robust and transparent financial infrastructure. (JEL G15, G23, E59)
```

  - **Citations**: 692
  - **Research objective**: This is a Fed paper that proposes a framework for evaluating and assessing risks across the DeFi ecosystem (protocols, markets, financial functionality, technology, etc.).
  - **Key notes**:
    - At the time of writing, stablecoins (USD) were already in circulation, and about $10B in DeFi.
    - The backbone of DeFi are smart contracts, on the public ledger for verification by every participant.
      - My thought is that this is verification at the level of the technology logic, not verification at the sense of financial standards and regulation (of course).
    - Original idea of a smart contract comes from Szabo (1994): the idea that transactions could be embedded in technology in such a way to make breach of contract expensive. (I suppose this idea later made its way to Bitcoin.)
    - What are the building blocks of DeFi? **Framework: SAPAA**
      - Architecture: hierarchical layer format (each layer depends on layer below.)
      - Five general layers, from deepest to the surface.
        - Settlements (layer 1): Underlying blockchain with smart contract functionality + its native token.
          - Authoritative transaction history, handles settlements & dispute resolution etc.
          - (Example: Ethereum, with native ETH token.)
          - Mechanics:
            - underlying blockchain. adding additional tokens = "tokenization" and gets recorded on the ledger
            - ex: Ethereum issues tokens via the "ERC-20" token standard (as a primary one).
        - Assets (layer 2): Assets on top of this underlying blockchain.
          - Includes native token + other tokens (fungible/non-fungible) that are also on top of the blockchain.
          - For instance this includes the fungible token DAI which is implemented via underlying smart contract logic on the Ethereum blockchain.
          - My understanding is this also includes non-fungible tokens (NFTs) as well.
        - Protocols (layer 3): Specific use cases built on top of the Settlement and Assets layer.
          - Example: debt, lending, derivatives, on-chain asset management, etc.
          - Implemented as set of smart contracts, all interoperable.
        - Applications (layer 4): user-specific applications, say web interfaces, user-oriented software etc.
        - Aggregations (layer 5): aggregation across user-specific applications
          - compare protocols, summarize information in a clear manner, etc.
      - Summarizing all this with a new user use case at the protocol layer (layers 1-3)
        - Say you want to send DAI (a kind of token)
        - I set up a crypto wallet via some wallet platform like MetaMask.
        - On a crypto exchange (say Coinbase) I use USD to buy ETH.
        - Then on a decentralized exchange (say Uniswap) I use that ETH to buy DAI, paying a little ETH in gas fees.
          - DAI is implemented via smart contract functionality on the Ethereum blockchain, and the most common & standard smart contract logic is the ERC-20 standard.
            - ERC-20: a set of functions and events (transfer, transferFrom, etc.) that all tokens must implement in their smart contract functionality. Interoperable with everything that usees ERC-20.
          - Note I need ETH to participate (pay gas fees) on this blockchain.
        - So now I have used USD to buy DAI, and can send it to my friend's wallet.
      - For assets backed in tokens (such as DAI), which are themselves implemented in Defi protocols, how are those backed in real value? (collateralized)
      - Three ways of collateralization.
        - 1. Off-chain collateral: proffer as collateral tokens that are backed by real assets, most common being USDT and USDC for the dollar and DGX for gold. However, these require off-chain audits, may require being collateralized in commercial banks and other traditional financial solutions, and so may lose some transparency and decentralization that the blockchain offers.
        - 2. On-chain collateral: proffer as collateral tokens the native token of the underlying settlement layer (for Ethereum, ETH). Fast and transparent.
          - However, may experience price fluctuations. ETH is not pegged to the dollar, and so the ETH/USD is a floating rate.
          - To deal with this: require you to overcollateralize (say 150% of what you want to deal with in DAI) and if the collateral (ETH) drops below some threshold due to the floating rate (ETH/USD), it will start to auction off the collateral returning the principal to the owners and cancelling the debt. Because it is overcollateralized, the loan holder has a disincentive to default.
      - Decentralized exchange protocols
        - early ones: less transparent, no shared liquidity between exchanges (walled garden), very illiquid ecosystem in general
        - open exchange protocols: transparent market making process
        - decentralized order book exchanges
          - on-chain order book
            - completely decentralized, but expensive because placing a limit order (intent to trade) / cancellation must also be recorded as a transaction, so slow and costly
          - off-chain order book (e.g. 0x)
            - can treat the blockchain just for settlement ("executed trades")
            - centralized 3rd-parties (relayers) store and release info on the order book but do not execute/match anything themselves, just provide ordered list with quotes
          - constant function automated market maker
            - e.g. Uniswap
            - between two tokens x and y, and a constant k, maintain y*x=k
            - trade corresponds to movement on convex curve. ("when the token supply of either one of the two tokens approaches zero, its relative price rises infinitely as a result.")
            - liquidity provider provides tokens to the pool, earns pool share tokens --> increases k
            - market price stabilized via public arbitrage
          - smart-contract reserve aggregation
            - various liquidity providers offer quotes for tokens (X, Y)
            - smart contracts automatically find the user the best quote across those and execute
          - peer-to-peer protocols
            - look for party to negotiate trade bilaterally with
            - executed via smart contract. advantage is avoiding front-running
        - Decentralized lending platforms
          - advantage: completely anonymous and permissionless, anyone can participate
          - how is default risk managed?
            - 1. flash loans / atomic transactions: within the same transaction, you borrow, execute and repay back. If the funds are not paid by the transaction execution cycle (e.g. somehow slip in before the repayment), the transaction will be cancelled and reverted.
            - 2. collateral (for loans)
              - A. collateralized debt: you lock up an (overcollateralized) amout of another cryptoasset to issue yourself a collateralized loan token that lets you withdraw an amount up to the equivalent amount of your (over-)collateral. To close the loan, you need to repay the amount plus interest rate set by protocol governance token holders.
              - B. collateralized debt markets: instead of locking up your collateral in that way, you find a counterparty directly to borrow (lend) from. This can be done in two ways:
                - direct peer-to-peer lending, with fixed interest rate, if there is a match
                - pooled lending: borrower funds all combined into a pool of liquidity, with dynamic interest rates set by supply and demand for those funds
        - Decentralized derivatives
          - usually require *oracles* (external data sources) to track underlying assets.
          - Asset-based decentralized derivatives
            - these track the price of an underlying asset, with collateralization
            - e.g. you put down 150% collateral in ETH, to get a DGX token that tracks gold
            - but to make sure everyone's tokens are fungible with each other, let the total collateralization debt pool (amount of collateralization) decreased based on the underlying assets, in aggregate
            - so, you are exposed to everyone else's risk too.
          - Event-based decentralized derivatives
            - idea: tokens for prediction markets (with some nb. of potential outcomes)
            - each participant locks in 1 ETH (collateral) via the smart contract and gets a full set (1/n each) of subtokens, each of which tracks a single potential outcome
            - participants can buy and sell tokens
            - when the event transpires, the total pool of crypto collateral is distributed among those who hold the winning outcome
            - requires oracle data source for the event; risks of manipulation
        - On-chain asset management
          - idea: you lock up some crypto via a smart contract and get "fund tokens" which correspond to the smart contract's investment strategies (trend following, moving average crossovers, sometimes actively managed etc.).
          - These represent partial ownership in the fund and can be redistributed / traded.
          - Closing this out: fund tokens get burned, underlying assets sold on decentralized exchange and compensated with ETH-equivalent share of the basket.
          - Various implementations: fully automated, semi-automated, fund of funds, highest yield, etc.
          - However many of these require external oracles.
        - Opportunities and risks for Defi
          - efficiency, transparency, accessibility, and composability (flexibility to create new protocols and services)
          - risks
            - smart contract execution bugs
            - operational security (e.g. admin keys held by developers to shut down systems for maintenance)
            - centralized governance (governance tokens held by minority; yield farming to obtain governance control)
            - dependencies, esp. for derivatives and oracles
            - illicit activity and laundered centralization: whether protocols really are decentralized or rather controlled by a single group (e.g. who could pump-and-dump)
            - scalability: Ethereum has a bottleneck for transactions confirmations (-> wait times) and also increased gas fees
  - **Overall impression**:
    - Extremely useful paper and overview of the Defi ecosystem (as of 2021).
