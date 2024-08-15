---
title: "[in progress] Quick paper notes: Cardaliguet and Lehalle (2017)"
collection: quant
type: "Post"
permalink: /quant/20240817_cardaliguet_and_lehalle_2017
date: 2024-08-17
---

This is a quick post to summarize the motivation, model, and findings of Cardaliguet and Lehalle (2017): *Mean field game of controls and an application to trade crowding*.

Categorically, this goes under optimal trading models that make use of [mean field game theory](https://en.wikipedia.org/wiki/Mean-field_game_theory).

The format I follow is:

- Motivation
- Model specification
- Model findings
  - Solutions (analytical, numerical)
  - Other findings

## Motivation

The goal of this paper is to formulate the classic problem of optimal trading (optimal liquidation) within a mean field framework. Classically, the problem is for a large trader to liquidate a large order over time, in a way that minimizes impact to the market price (Almgren & Chriss 2000). In other frameworks there is a distribution of "noise traders" that represents atomic randomness by other market participants, that must also be accounted for (Kyle 1985). Hence to model the agent's optimal trading problem against the large population's distribution of trading behavior, it is natural to formulate this via a *mean-field game.*

This is an *extended mean field game* since the mean field aspect enters through the controls, and not through the states. We will see how this works.

### Model specification

There is a distribution of atomic identical traders, each of whom is indexed by a parameter $a$, and a finite time horizon $\mathcal{T}=1 \dots T$. The market price moves according a drift-diffusion where the drift is the net trade flow $\mu_t$ of all traders.

$$
\begin{align}
    d S_t &= \alpha \mu dt + \sigma dW_t & \alpha, \sigma \in \mathbb{R}_{+}
\end{align}
$$

At time $t$, each trader $a$ has two states inventory $Q_t^a$ and wealth $X_t^a$, and has to decide how much to trade $\nu_t^a$ (the control). Hence the inventory and wealth dynamics are:

$$
\begin{align}
    dQ_t^a &= \nu_t^a dt & \text{trader's inventory process} \\
    dX_t^a &= -\nu_t^a (S_t + \kappa \nu_t^a) dt & \text{trader's wealth process, } \kappa \in \mathbb{R}
\end{align}
$$

where $\kappa \nu_t^a$ is the *temporary price impact* and represents the adverse change in price induced by more trading $\nu_t^a$. Initial conditions are given by $X_0^a=0$ for all traders, and $Q_0^a>0$ for all sellers (aiming for $\nu_t^a>0$) and $Q_0^a<0$ for all buyers similarly, hence within this single distribution of $Q_0^a$ we have two kinds of traders.

Finally, the trader wants to maximize a payoff that is the sum of the terminal cash, the terminal value of inventory minus terminal market impact, minus the running cost of trading at each time. This running cost is quadratic in the inventory and parameterized by $\phi^a$, and is interpretable as *risk aversion*. Written as a value function at time $t$ to terminum $T$, for some $A^a \in \mathbb{R}$:

$$
\begin{align}
V_t^a &= \sup_{\nu} \mathbb{E}\left[
    X_t^a + Q_T^a(S_t - A^a Q_T^a) - \phi^a \int_t^T (Q_s^a)^2 ds
\right]
\end{align}
$$

Solving this yields the Hamilton-Jacobi-Bellman and associated optimal feedback (the optimal control) below. It is helpful to recall that HJB is a partial differential equation and specifies the dynamics a value function must satisfy over time.

$$
\begin{align}
    0 &= \partial_t V^a - \phi^a q^2 + \frac{1}{2} \sigma^2 \partial_S^2 V^a \\
        &\hspace{0.5cm} + \alpha \mu \partial_S V^a + \sup_{\nu}[\nu \partial_q V^a - \nu (s + \kappa \nu) \partial_X V^a] &\text{HJB} \\
    V^a(T, x, s, q; \mu) &= x + q(s - A^a q) &\text{terminal condition (see above)} \\ 
    V^a &= x + qs + v^a (t, q; \mu) &\text{useful ersatz} \\
    \nu^a (t, q) &= \frac{\partial_q v^a(t,q)}{2\kappa} &\text{optimal feedback}
\end{align}
$$

Note that $s$ is now part of $\partial_q v^a$. Moreover, note that we have via the ersatz $\nu^a(t, q; \mu)$, so that the control now depends on the net trading flow $\mu$. (Note that this impacts the market price $S_t$ via the *permanent market impact* term $\alpha$.) Using the ersatz and the optimal feedback we obtain, by substituting out the supremum wrt. $\nu$:

$$
\begin{align}
    -\alpha \mu q &= \partial_t v^a - \phi^a q^2 + \sup_\nu [\nu \partial_q v^a - \kappa \nu^2] &\text{HJB with ersatz} \\
    \therefore -\alpha \mu q &= \partial_t v^a - \phi^a q^2 + \frac{(\partial_q v^a)^2}{4\kappa} &\text{HJB, use optimal feedback to eliminate $\nu$} \\
\end{align}
$$

Hence this gives us the HJB (the MFG backward equation) as well as the optimal feedback. Now, using the latter we define the net trading flow as the sum of optimal trading (the optimal feedback) across all participants:

$$
\begin{align}
    \mu_t &= \int_{(q,a)} \nu_t^a(q) m(t, dq, da) = \int_{(q,a)} \frac{\partial_q v^a(t,q)}{2\kappa} m(t, dq, da)
\end{align}
$$

As usual, there is a mean field $m(.)$ that is the distribution of $(q, a)$ over traders. (Since $a$ is predetermined, this really means the $q$.) However, there is *also a mean field in the controls*, since we have $\nu_t^a \mapsto v^a(t, q; \mu) \mapsto \mu \mapsto \nu_t^a$. So, we have mean fields in both the states $(q_t, a) \leftrightarrow m(t, q, a)$ as well as in the controls $\nu_t^a \leftrightarrow \mu_t$.

Lastly, the states $Q_t^a$ follow a drift-only equation with a positive drift term $\nu_t^a$. Hence, apply Fokker-Planck (only drift, so only Laplacian term) to obtain the dynamics of the state distribution $m(.)$:

$$
\begin{align}
    \partial_t m + \partial_q \left(m \nu_t^a\right) &= 0 &\text{Fokker-Planck, positive drift only} \\
    \partial_t m + \partial_q \left( m \frac{\partial_q v^a}{2 \kappa} \right) &= 0 &\text{paper form}
\end{align}
$$

Hence, we obtain an extended mean field game system with *three equations* plus boundaries: the backward HJB equation, the forward Fokker-Planck equation, and the mean field relation between the controls.

$$
\begin{align}
    -a q \mu_t &= \partial_t v^a - \phi^a q^2 + \frac{(\partial_q v^a)^2}{4 \kappa} &\text{backward HJB} \\
    0 &= \partial_t m + \partial_q \left( m \frac{\partial_q v^a}{2\kappa} \right) &\text{forward transport equation (FP)} \\
    \mu_t &= \int_{(q,a)} \frac{\partial_q v^a (t, q)}{2 \kappa} m(t, dq, da) &\text{mean field in the controls} \\
    m(0, dq, da) &= m_0(dq, da) &\text{initial forward condition, $t=0$} \\
    v^a(T, q; \mu) &= -A^a q^2 &\text{initial backward condition, $t=T$}
\end{align}
$$

### Model results