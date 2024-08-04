---
title: "DeFi, top 100 papers (August 2024)"
collection: quant
type: "Post"
permalink: /quant/20240810_literature_survey_defi
date: 2024-08-10
---

This is a whirlwind survey of the top 100 recent papers in decentralized finance, based on Google Scholar citation data.

In this post I attempt to get up to speed quickly on DeFi. Why academic papers and not blog posts, tutorials, etc. which are also useful?

1. These papers do often include introductory & motivating content, while showcasing what is new in the field.
2. I have some idea of their influence via citations and other publication metrics.
3. I can ensure that I are sampling a good chunk of topics in DeFi.

To obtain this list, I used the tool [Publish or Perish](https://harzing.com/resources/publish-or-perish) to search for the most cited papers in DeFi.

- First, I obtain the first 500 papers for DeFi that show up on Google Scholar.
  - **This list was fetched on August 3, 2024.**
  - **This is roughly Google's "top 500 papers," which I will filter down further.
  - Search query: "defi AND decentralized finance"
  - Only 2013 onward (when Ethereum was released); this will push down the citation counts in the tool a little.
  - Omits citation records and patents. I also skip full books for obvious reasons.
  - I could find more than 500 papers but Google Scholar already returns more influential papers first, and I only survey the top 100 anyway.
- Then I simply sort by decreasing citation count, since my goal is simply to read the most cited papers in the field, from most influential to least influential.
  - [Yes, pure citation count is not perfect by any means](https://academia.stackexchange.com/questions/37021/why-is-it-bad-to-judge-a-paper-by-citation-count)
- I give some summary statistics on this universe of 500 papers.
- Out of those, I pick **top 100** to read and summarize for this blog post.

**Here are my very rough notes.** Let's go!

## What is decentralized finance?

From [Wikipedia](https://en.wikipedia.org/wiki/Decentralized_finance):

>  Decentralized finance (often stylized as DeFi) offers financial instruments without relying on intermediaries such as brokerages, exchanges, or banks by using smart contracts on a blockchain, mainly Ethereum. DeFi platforms allow people to lend or borrow funds from others, speculate on price movements on assets using derivatives, trade cryptocurrencies, insure against risks, and earn interest in savings-like accounts. DeFi uses a layered architecture and highly composable building blocks. Some applications promote high-interest rates but are subject to high risk. Coding errors and hacks have been common in DeFi.

## Summary of Google's top 500 papers on DeFi

HoIver, note this includes some noise: papers that are returned by the search query but not related to DeFi.

## The top 100 papers

For each paper, I present the title/abstract/citation count, followed by three bullet points.

- Research objective - this covers the main research question(s), the goal of the work, etc.
- Key findings - this covers important findings and how they are achieved (methodology, etc.).
- Implications & evaluation - this covers the implications of the research and our opinion on the research overall.

### #1. Chen, Yan, and Cristiano Bellavitis. "Blockchain disruption and decentralized finance: The rise of decentralized business models." Journal of Business Venturing Insights 13 (2020): e00151.

```
Blockchain technology can reduce transaction costs, generate distributed trust, and empower
decentralized platforms, potentially becoming a new foundation for decentralized business
models. In the financial industry, blockchain technology allows for the rise of decentralized
financial services, which tend to be more decentralized, innovative, interoperable, borderless,
and transparent. Empowered by blockchain technology, decentralized financial services have the
potential to broaden financial inclusion, facilitate open access, encourage permissionless
innovation, and create new opportunities for entrepreneurs and innovators. In this article, we
assess the benefits of decentralized finance, identify existing business models, and evaluate
potential challenges and limits. As a new area of financial technology, decentralized finance may
reshape the structure of modern finance and create a new landscape for entrepreneurship and
innovation, showcasing the promises and challenges of decentralized business models.
```

  - **Citations**: 711
  - **Research objective**: Survey the benefits, challenges, and limits of blockchain-based decentralized finance.
  - **Key notes**:
    - This is a business school study.
    - decentralized finance (as of 2020) is not fully interoperable, i.e. integration across protocols (blockchains): 87% of publicly funded DeFi projects were on Ethereum
    - what are the major business models in DeFi?
      - decentralized currencies (Bitcoin, etc.)
      - decentralized payment networks (Libra, Bitcoin, Ripple, etc.)
      - decentralized fundraising
        - initial coin offering: project offers investors stake in token
        - initial exchange offering: project lists on an existing crypto exchange
      - decentralized contracting
        - smart contracts: auto-execute contract when conditions reached
    - risks
      - susceptible to fraud / bugs / risk
      - underlying often has volatility
      - technology push > pull: trap of building tech first, then hoping people will join
    - what are the fundamental limits of defi?
      - cost of distributed trust: inherently costly by distributing info to everyone?
      - user privacy: some protocols (Monero, Zcash) do this but not sure
      - decentralized consensus: may slow major upgrades and innovations
      - accountability: who should be accountable for major issues that come up?
      - not holistic: financial aspects that cannot be recorded objective transactions on the ledger (my thought: credit ratings may be tough)
      - lack of human judgment: may inhibit progress broadly
  - **Overall impression**:
    - Just a quick, readable survey paper of decentralized finance, its business use cases, risks, and limits. Breadth over depth for this one. (Probably things have changed a lot since 2020.)

### #2. Schar, Fabian. "Decentralized Finance: On Blockchain and Smart Contract-Based Financial Markets." Federal Reserve Bank of St. Louis Review, Second Quarter 2021, 103(2), pp. 153-74.

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

### #3. Zetzsche, Dirk A., Douglas W. Arner, and Ross P. Buckley. "Decentralized finance." Journal of Financial Regulation 6.2 (2020): 172-203.

```
DeFi (‘decentralized finance’) has joined FinTech (‘financial technology’), RegTech (‘regulatory technology’), cryptocurrencies, and digital assets as one of the most discussed emerging technological evolutions in global finance. Yet little is really understood about its meaning, legal implications, and policy consequences. In this article I introduce DeFi, put DeFi in the context of the traditional financial economy, connect DeFi to open banking, and end with some policy considerations. I suggest that decentralization has the potential to undermine traditional forms of accountability and erode the effectiveness of traditional financial regulation and enforcement. At the same time, I find that where parts of the financial services value chain are decentralized, there will be a reconcentration in a different (but possibly less regulated, less visible, and less transparent) part of the value chain. DeFi regulation could, and should, focus on this reconcentrated portion of the value chain to ensure effective oversight and risk control. Rather than eliminating the need for regulation, in fact DeFi requires regulation in order to achieve its core objective of decentralization. Furthermore, DeFi potentially offers an opportunity for the development of an entirely new way to design regulation: the idea of ‘embedded regulation’. Regulatory approaches could be built into the design of DeFi, thus potentially decentralizing both finance and its regulation, in the ultimate expression of RegTech.
```

  - **Citations**: 494
  - **Research objective**: To discuss the role of financial regulation in DeFi, the relationship to traditional financial regulation, and recommendations for regulating DeFi.
  - **Key notes**:
    - defi: a key advantage of providing multiple "hubs" for financial services and (de)regulation
    - **primarily this is a discussion paper between DeFi vs. (1) the traditional financial system (2) the state**
    - on the technology:
      - key technological groundings of defi:
        - 1. Moore's law: data processing grows exponentially
        - 2. Kryder's law: same for data storage
        - 3. Decreased marginal cost of connection bandwidth
    - on the relationship to the state:
      - where does jurisdiction fall? entities, also tech developers now?
        - example: BlackRock Aladdin risk mgmt (>GDP) --> at least you have Blackrock who is the main legal entity
        - "not subject to law anywhere" -> but is it subject to law EVERYWHERE?
        - Liability ties down economic benefit --> challenge to develop true DeFi framework
      - enforcement: how do you enforce regulation, liability standards, etc?
        - key concept: the *risk of defection*. If I have technology party X (integrator) and user Y (contributor), both can defect if the cost of compliance gets too high.
          - X: wants to enforce compliance on Y but either too lax (fines, bankruptcy) or too strict (loses users)
          - Y: can only comply as long as the economic benefit is greater than the cost of compliance (X's geo, Y's geo.)
        - how do you apply standards across geographies, protocols, etc.?
        - cooperation on a cross-border basis: doesn't this defeat the purpose of DeFi?
      - data protection and privacy
        - where do we store data: backups, emergency funds for insolvency, etc?
      - tech risk:
        - tech itself: bugs, hacks, lag behind legal frameworks and audit capability, correlation between networks (technology protocols)
        - connectivity: number of entry points is now multiplied as well. if one person gets hacked, is the whole network at risk?
        - support: hard to distribute support (emergency liquidity, lender of last resort, deposit guarantee schemes)
    - challenging aspects of DeFi regulation
      - how do we regulate a decentralized system that is centralized wrt. the developers? and for many protocols? ("safe harbor" guidelines?)
      - how do we coordinate regulation cross-border? especially for things like stablecoins
        - one approach: "subsituted compliance": approved in EU --> can use this approval elsewhere
      - how do we stabilize risk exposures exposures (data backups and financial risk) in each domain?
        - traditionally we have data backups in regions + financial reserves
    - Open finance (e.g. open details on transactions via public ledgers) could help with antitrust
    - Embedded regulation: regulatory tech that is written into DeFi ledgers and applies compliance real-time
    - summary notes:
      - unclear how decentralized finance will exist in a regulated financial world, especially around accountability, enforcement, determination of jurisdiction, and risk of defection
      - tragedy of the commons: where do incentives to develop the core come from, with increasing decentralization?
      - DeFi will have to recentralize *somewhere* in the value chain (whether it is the core technology development, the regulation, etc.) - big opportunity for embedded regulation
  - **Overall impression**: A useful discussion that opens various questions about DeFi's real ability to decentralize, where the burdens and incentives fall, how risk and reserves are managed, and how it can exist in a regulated financial ecosystem. Embedded regulation is a very interesting idea.

### #4. 

```
Decentralized Finance (DeFi), a blockchain powered peer-to-peer financial system, is mushrooming. Two years ago the total value locked in DeFi systems was approximately 700m USD, now, as of April 2022, it stands at around 150bn USD. The frenetic evolution of the ecosystem has created challenges in understanding the basic principles of these systems and their security risks. In this Systematization of Knowledge (SoK) we delineate the DeFi ecosystem along the following axes: its primitives, its operational protocol types and its security. We provide a distinction between technical security, which has a healthy literature, and economic security, which is largely unexplored, connecting the latter with new models and thereby synthesizing insights from computer science, economics and finance. Finally, we outline the open research challenges in the ecosystem across these security types.
```

  - **Citations**: 347
  - **Research objective**: Propose a classification for the DEFI ecosystem by protocol types and their security.
  - **Key notes**:
    - both audited and unaudited smart contracts pose technical risks
    - *atomicity* property of smart contracts: immediately succeed or fail
    - review, execution of a transaction:
      - create or reuse smart contract
      - broadcast transaction to peers (mempool) who validate the transaction
      - transaction and its associated transaction fee (gas fee) goes into a queue for mining
      - miners choose to add these transactions to the public ledger via a "mining" process
        - solve mathematical cryptographic puzzle --> that new block gets added to the ledger (blockchain)
      - however this has now moved to "proof of stake"
    - entities and roles
      - keepers: programs that automatically keep the blockchain up to date (e.g. trigger and write transactions such as liquidating collateral)
      - oracles: components to ingest external data into the blockchain (e.g. for synthetic tokens)
      - governance:
        - usually starts with the protocol creators (small council "multisig") who promise to eventually decentralize the governance
        - governance decentralized via governance tokens 
        - majority voting on protocol updates, etc.
    - DEFI protocols
      - On-chain asset exchange
      - Loanable fund markets for on-chain assets
        - overcollateralized loans
        - flash loans - prone to attacks
      - Stablecoins
        - don't include *custodial* stablecoins (USDT) which are managed by centralized third-party
        - how do you achieve price stability for on-chain stablecoins?
      - Portfolio management
    - a side note on yield: rewards you earn from providing liquidity or stability to these decentralized protocols
      - lending protocols: yield = interest rates from lending out your assets to provide liquidity
      - stakers: if you lock up your tokens in proof-of-stake you can earn rewards
      - liquidity providers: if you provide liquidity for decentralized exchanges
      - incentive programs for new protocols: if you sign up
      - yield farming and why it is controversial: providing liquidity to protocols is risky for many reasons. for one, both the asset you lock up (specifically its exchange rate with the protocol's native token) and the reward tokens you receive can be highly volatile. ponzi-like criticism, in that rewards for users are based on new user entry and growth. also, rug pulls: original developers may withdraw all the liquidity shortly after release, leaving the user with worthless tokens. lastly: risks for money laundering and illicit activities.
    - Derivatives
      - Synthetic assets: tokenized version of off-chain instruments
      - Perpetual swaps: like futures but never expire.
        - you can hold as long as you want, as long as you hold required margin.
          - this let you do leverage: put down 10% of a (X BTC) position.
          - at a later time you can buy (sell) that much.
        - periodic funding rate mechanisms implemented at the level of exchanges: compare the perpetual swap contract price & spot, and if there is imbalance then swap buyers (long positions) pay a rebalancing amount, the "funding rate," to the swap sellers (short positions).
      - Privacy-preserving mixers
        - mix coins together to preserve privacy (could shield illicit activity)
    - Definition of an exploit:
      - consider the difference at time T between the smart contract's off-chain estimates and the true off-chain economic ground truth, given the filtration of information up to that point
        - 1. exploiting intended vs. actual implementation of smart contract (e.g. bugs)
        - 2. exploiting that informational gap at time T
        - 3. creating that information gap at time T
      - intention matters however. In the AMM mechanism, it is okay if the price deviates as to let arbitrageurs close the gap.
    - Technical security exploit
      - Definition: attacker can atomically exploit a protocol
      - "risk free" - either works or not (paying gas fees).
      - often occur in a single transaction or single block of transactions
    - Smart contract vulnerabilities
      - Reentrancy: functions can be called repeatedly before as the system state is only partially modified (especially if prioritized via higher gas fees). This caused the big DAO hack: repeated withdraw.
      - Integer manipulation: protocols can only check integer precision (overflow or underflow) to a certain extent
      - Logic bugs in smart contracts
    - Single transaction attacks
      - Governance tokens are a point of risk.
        - Attackers can atomically (instantaneously, within the same transaction) gain enough governance tokens via flash loans, make changes, then commit
      - Single transaction sandwich attacks
        - Create imbalance in AMM --> exploit (composable) contracts that rely on the price --> reverse the imbalance, all within the same (atomic) transaction
        - Example: Harvest. (1) $50m USDT flash loan from Harvest --> (2) use funds to create liquidity imbalance via manipulating on Curve (an AMM) and increase price of USDT --> (3) Curve was an on-chain oracle for Harvest, so Harvest sees a USDT price increase --> (4) attacker deposits USDT to "help" this in exchange for Harvest liquidity-provider tokens --> (5) lastly, reverse the imbalance on Curve and withdraw USDT.
    - Transaction ordering attacks
      - Front-running / back-running: transactions prioritized by gas fees, so can exploit by setting gas fees to time your transactions (risk-free if you are a miner)
      - Displacement attacks
        - front-run another later transaction (not depending on its execution)
        - example: bug-bounty, or front-running transaction that is trying to rescue funds
      - Multi-transaction sandwich attacks
        - Manipulating price via changing imbalance on AMMs
        - Example: "sandwich" another user's transaction
          - front-run with a high gas fee
          - back-run with a low gas fee
        - Note: ultimately depends on transaction's miner to set order, so not guaranteed
        - Can also be done from the liquidity provider's side, withdrawing (front-running) then resupplying liquidity
    - Economic security exploits
      - Non-atomic exploits, so not risk-free and only probabilistic.
      - Example: say AMM depends on an oracle. Could manipulate it instantly (atomic attack) or over time, esp. if oracle say depends on some time window.
      - Economic security only makes sense if technical security is first achieved.
      - Rational agents: profit optimizing (will never play a strictly worse strategy).
      - Incentive compatibility: agents are incentivized to execute the game as originally intended by the mechanism designer.
    - Overcollateralization as security
      - Recall: automatic deleveraging (if collateral falls below % threshold against the principal, then begins being auctioned off)
      - Deleveraging risks
        - One way: negative shocks to collateral asset --> can reduce its value and so undercollateralization / deleveraging can happen organically
        - This is a big question to me: how do you ensure stability for (over-)collateral? Especially given there are not that many proven crypto derivatives yet (just perpetual swaps, some basic options, etc.)
        - Another way: endogenous risk. How do you make sure that collateralization actions of agents don't impact each others' collateral value?
          - Example: every agent puts up some ETH collateral to borrow DAI --> this will drive down the value of ETH (at least directly with respect to DAI and possibly indirectly with respect to other currencies)
          - Risk of deleveraging feedback effects. Example: DAI black thursday in early 2020 when crypto asset values fell dramatically. (uncertainty --> no room for speculative assets: "risk-off")
          - There is a potential application of MFG here, at the level of one or multiple protocols: everyone puts up collateral to maintain the value of what they can borrow, yet doing so drives the price of everyone's collateral. How do you optimize against that overall trajectory?
      - Miner extractable value (MEV) threats
        - miners not always incentivized to act in public interest
        - especially because can choose the order of mining transactions
        - undercutting
          - say you have blocks 1-6 that require validation on the ledger by miners
          - one adversarial miner sees block 5 has high expected value, "forks" from there and starts mining that and gets other miners to join in
          - eventually block 5 becomes the continuation of the new blockchain
        - time-bandit attacks
          - like undercutting (forking from previous block), but based on expected MEV and pursue a 51% layer attack until the fork becomes the main chain
        - Other forms of miner collusion
      - Governance risks
        - Governance tokens = like shares in the protocol
        - Incentives should ideally come from improvements and appreciation of the protocol assets over time (so you have incentive to govern well), say future discounted cashflows
        - Governance extractable value (GEV): value from behaviors that are helpful to the governors but not to the protocol and (non-governor) users
        - Risk: you can buy governance tokens on the open market sometimes, so if you take out a flash loan to buy those and immediately change the protocol and repay the loan, that can be a governance attack
      - Market and oracle manipulation
        - AMMs are highly manipulable and should not be used as oracles.
        - In the case of lending, collateral (say locked-up ETH) may use oracles (say for ETH exchange rates) to track the collateralization value. If there is bug or manipulation on those oracles that induces a negative price movement in the collateral value, this may trigger a sell-off and negative feedback cycles thereafter.
          - Prior to the liquidation, attackers could benefit from a short position (a priori) or a discount purchase of the liquidated collateral (ex post).
      - Incentives tied to consensus are risky if the consensus is modified.
      - Other open questions:
        - How can stablecoins achieve true stability?
        - How can protocols achieve incentive compatibility for governance?
        - How do miners optimize their miner-extracted value?
        - How do GEV and MEV endogenously affect the behavior of these systems?
        - How do we analyze programs and protocols for technical correctness, formally?
  - **Overall impression**:
    - A useful survey of technical and economic risks in DeFi protocols.


<!-- placeholder -->
### #X. TEMPLATE

*Abstract*

  - **Citations**: ...
  - **Research objective**: ...
  - **Key notes**: ...
  - **Overall impression**:












<!--
Could cluster these papers by their metadata also.
-->
