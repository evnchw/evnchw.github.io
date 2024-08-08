# Notes on uniswap incentive design (8/7/2024)

From https://www.gauntlet.xyz/resources/uniswap-incentive-design-analysis

## ChatGPT summary

The Gauntlet analysis on Uniswap incentive design provides several key insights into the effectiveness of liquidity mining in boosting Total Value Locked (TVL) and trading volumes across selected pools. The study set up a controlled experiment by comparing pools with incentives (treatment group) against similar pools without incentives (control group), allowing for a clearer assessment of the incentive impact.

Key Findings:

- Statistically Significant Impact: Out of five pools analyzed, two demonstrated a sustained and significant increase in both TVL and trading volume compared to their control counterparts. This indicates that liquidity mining can effectively attract and retain liquidity under certain conditions.
- Mixed Results: Three of the pools did not show a sustained increase in performance metrics. Factors such as mismatched control pools, external incentive programs affecting results, or inherently low trading volumes might have confounded these results.
- Optimization of Incentive Allocation: The analysis underscored the importance of carefully selecting which pools to incentivize and determining the appropriate amount and duration of incentives. The goal is to maximize the net benefit to the protocol, considering factors like potential shifts in trading volume from competing platforms and the overall cost of incentives.
- Advanced Modeling: Gauntlet used sophisticated simulation models to project the outcomes of incentive spends, optimizing for parameters such as TVL increase and trading volume enhancement. These models consider various market dynamics and competitive scenarios to fine-tune the incentive strategies.
- Strategic Recommendations: For effective liquidity mining, protocols should focus on pools with high market-wide trading volumes but low market shares on their platform. This strategy aims to capture volume from competing decentralized exchanges (DEXes) and centralized exchanges (CEXes).

Conclusion:

- The success of liquidity mining in DeFi, as shown in the Uniswap case study by Gauntlet, is nuanced and highly dependent on precise execution and continuous monitoring. Protocols considering similar incentive designs must employ robust analytical tools to simulate outcomes and adjust strategies dynamically based on real-time market conditions.

## Quick cheat sheet of incentives and entities

Overall:

- LPs
  - Incentives: liquidity mining, staking rewards, tiered incentives, fee share, loss compensation
  - Metrics: TVL, revenue, volume-to-liquidity, churn rate, impermanent loss metrics
- Traders
  - Incentives: reduced trading fees, loyalty programs, trading competitions, flash rebates ("surge" subsidies), referral programs
  - Metrics: PNL, trading volume, active users, microstructural aspects (market depth, order flow toxicity, adverse selection of traders etc.)
- miners
- Protocol itself
  - Incentives:
  - Metrics: value of token on the secondary markets (esp. against other protocols tokens), governance aspects (diversity, etc.), technical aspects (bugs like reentrancy, etc.)

### LPs

Type of incentive programs one could run:

- Liquidity Mining: Reward LPs with protocol tokens based on the amount of liquidity they provide relative to the total pool. This can be in proportion to the time and size of liquidity provided.
- Staking Rewards: Offer additional rewards for LPs who lock their liquidity tokens for a certain period. This can help stabilize liquidity in the pool.
- Tiered Incentives: Implement a tiered reward system where long-term or larger liquidity providers earn higher rates or special bonuses.
- Fee Share: Allow LPs to earn a portion of the trading fees proportional to their share in the pool. This can be a direct motivation to keep funds in the pool.
- Loss Compensation: Implement mechanisms to partially compensate LPs for impermanent loss, especially in volatile pools.

Metrics to monitor:

- Total Value Locked (TVL): Monitor the growth in liquidity to assess the attractiveness of the pool.
- Volume-to-Liquidity Ratio: Helps in understanding how efficiently the provided liquidity is being utilized.
- Churn Rate of LPs: High churn rates might indicate dissatisfaction or better opportunities elsewhere.
- Impermanent Loss Metrics: Track how much LPs are losing due to price divergence to tweak incentives accordingly.

### Traders

Incentive Strategies:

- Reduced Trading Fees: Offer discounted fees for traders who reach certain volume thresholds. This can encourage higher trading frequency and volumes.
- Loyalty Programs: Create a loyalty program where traders earn points that can be redeemed for various benefits like lower fees, access to exclusive events, or direct token rewards.
- Trading Competitions: Host regular competitions with prizes for top traders by volume or profitability. This can temporarily boost trading activity and attract new users.
- Flash Rebates: Provide immediate rebates for trades over a certain size or during specific times to incentivize larger trades or trading during low activity periods.
- Referral Programs: Reward traders who bring new users to the platform with a share of the trading fees generated by the referred users.

Metrics to Monitor:

- Trading Volume: Track overall and per-pair trading volumes to gauge the activity level and the protocol’s market capture.
- Active Users: Monitor both daily and monthly active users to assess user engagement and growth.
- Fee Revenue: Evaluate the total fees generated, which directly correlates with the protocol’s profitability.
- Cost per Acquisition (CPA): Keep an eye on the cost of acquiring new traders through incentives versus the revenue they generate.
- Retention Rates: Measure how well the platform retains traders over time, indicating the long-term effectiveness of incentives.

### Miners

- primarily validate transactions at the infrastructural level (settlement level, in the SAPAA framework: settlement, assets, protocol, application, aggregation)
- Do not usually interact directly with LPS and traders
- but they get the fees


### Protocol itself

Metrics to Monitor:

- (metrics for LPs and traders)
- Performance of governance token 

