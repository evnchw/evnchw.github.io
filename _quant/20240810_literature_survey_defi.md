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

### #1. 

### #3. Zetzsche, Dirk A., Douglas W. Arner, and Ross P. Buckley. "Decentralized finance." Journal of Financial Regulation 6.2 (2020): 172-203.

> DeFi (‘decentralized finance’) has joined FinTech (‘financial technology’), RegTech (‘regulatory technology’), cryptocurrencies, and digital assets as one of the most discussed emerging technological evolutions in global finance. Yet little is really understood about its meaning, legal implications, and policy consequences. In this article I introduce DeFi, put DeFi in the context of the traditional financial economy, connect DeFi to open banking, and end with some policy considerations. I suggest that decentralization has the potential to undermine traditional forms of accountability and erode the effectiveness of traditional financial regulation and enforcement. At the same time, I find that where parts of the financial services value chain are decentralized, there will be a reconcentration in a different (but possibly less regulated, less visible, and less transparent) part of the value chain. DeFi regulation could, and should, focus on this reconcentrated portion of the value chain to ensure effective oversight and risk control. Rather than eliminating the need for regulation, in fact DeFi requires regulation in order to achieve its core objective of decentralization. Furthermore, DeFi potentially offers an opportunity for the development of an entirely new way to design regulation: the idea of ‘embedded regulation’. Regulatory approaches could be built into the design of DeFi, thus potentially decentralizing both finance and its regulation, in the ultimate expression of RegTech.

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

### #2. 

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
