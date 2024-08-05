---
title: "Karim, S, Lucey, BM, Naeem, MA and Uddin, GS. \"Examining the interrelatedness of NFTs, DeFi tokens and cryptocurrencies.\" Finance Research Letters, 2022, Elsevier."
collection: notes
type: "Post"
permalink: /notes/20240805_karim_2022_examining
date: 2024-08-05
---

**Abstract**

  - **Citations**: ...
  - **Research objective**: Examine spillovers between NFTs, DeFi tokens, and cryptocurrencies via a quantile connectedness approach.
  - **Key notes**:
    - Methodology
      - take time series of returns of about 15 of these (NFTs, DeFi tokens, crypto)
      - estimate GARCH(1,1) model to get estimated volatilities
      - estimate effect of y (volatility of instrument) from past x (quantiles of past volatility of another instrument), for instance ETH ~ lags of SOL at their 75th quantile
      - examine breakdowns of forecast error for y across all x (via generalized forecast error decomposition)
      - from there get "total connectedness index" measuring contribution of risk spillovers at each quantile, e.g. relative contribution of 75th vol spillover from other instruments (wrt. total forecast error) for ETH.
      - "net connectedness" (to get a direction) is the difference between inward and outward spillovers, in terms of magnitude
      - question: why not just look at (rolling) correlation matrix between instruments vol?
        - have to understand methods more
      - empirical results:
        - extreme high quantiles of vol --> much more connected.
          - supports idea "assets highly correlated in high-vol times"
        - events captured via vol connectedness:
          - covid --> high volatility connectedness
          - tesla not taking BTC in May '21 --> high vol connectedness
      - takeaways:
        - high level of volatility spillovers at median, extreme low and extreme high
        - NFTs: higher diversification potential against DeFi/Cryptos
  - **Overall impression**: ...
    - helpful empirical paper, quite short and simple and focuses on a single task.
    - useful ideas:
      - could polarize into volatility spillovers regimes --> measure of systemic risk





