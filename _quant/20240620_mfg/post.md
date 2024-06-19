# A brief refresher on mean field games

While brushing up on mean field game theory ("MFG") I wanted to write a brief refresher to solidify the key ideas, even if only for myself. Hence in this blog post I aim to present the key formulation and ideas of MFG in a concise, informal and practical way. All feedback and corrections are welcome!

The fundamental idea of MFG is to model (differential) game-theoretic equilibria where there are a very large number of agents. The key characteristic is that each agent optimizes decisions against the *distribution* of everyone else's decisions (the "mean field"), and where agents are identical to some degree. This allows one to obtain asymptotic equilibria by surmounting the usual combinatorial (agent-to-agent) complexity of differential game theory. Applications of include modeling traffic congestion, pedestrian foot traffic, financial markets, and more.

The idea was originally presented in [1]. Introductory notes to this were compiled in [2] and [3], and upon those even more introductory notes were compiled at Stanford [4]. I base this brief refresher upon several excellent resources.

- The core of this material, and the notation, is primarily drawn and restated from [4].
- For optimal control I refer to [5].
- For Fokker-Planck and drift-diffusion stochastic differential equations I refer to [6].

## Specification of a mean field game

As described in [4], a mean field game consists of two coupled equations plus boundary conditions.

$$
\begin{align}
    -\partial_t u - \nu \Delta u + H(x, Du) &= f(x, m(x,t)) & \in \mathbb{R}^d \times (0, T) & \hspace{0.5cm} \text{backward Hamilton-Jacobi (agent's optimization)} \\
    \partial_t m - \nu \Delta m - \text{div}(D_pH(x,Du)m) &= 0 & \in \mathbb{R}^d \times (0, T) & \hspace{0.5cm} \text{forward Fokker-Planck (evolution of state distribution)} \\
    u(x,T) &= G(x) & & \hspace{0.5cm} \text{backward boundary: terminal payoff} \\
    m(0,x) &= m_0(x) & & \hspace{0.5cm} \text{forward boundary: initial distribution of states}
\end{align}
$$

**This looks daunting, but essentially this says: each agent optimizes its payoff against everyone else who optimize in the same way, and we reach an equilibrium in finite time.**

Why is it useful to think this way? In "normal" game theory each agent has to make decisions in light of everyone else, which becomes computationally infeasible (and unrealistic) for very large populations. As an example, if you're searching to find an exit out of Shibuya Station in Tokyo, which has millions of commuters each day [(Wiki)](https://en.wikipedia.org/wiki/Shibuya_Station), you have to navigate your way against the general mass of commuters as a whole and not really against any specific individuals. Moreover, everyone uses the same entrances and exits (more or less), so to some extent each person faces the same problem.

The first equation represents the expression for each agent's optimal control problem. Each agent optimizes the stream of future payoffs backward-in-time, and agents identically face this same problem. The second equation represents the expression for how the distribution of agents (their states) evolves forward-in-time. Lastly, the boundary conditions must be satisfied: we must have a terminal payoff (as usual per control problems), and we must have an initial distribution of agents.

The unusual features are that we have coupled two equations that are solved opposite directions in time, and also that each agent optimizes against a distribution of which they are a part of (the "mean field"). Let's dive in to understand these equations.

## The forward equation

In this part, we will concisely build up the agent's optimal control problem, starting from a purely deterministic version, to a stochastic version, to finally the stochastic version with the mean field.

### Hamilton-Jacobi-Bellman, deterministic

Here we formulate the simplest, deterministic version of the agent's optimal control problem.



### From HJB to Euler-Lagrange









## References

[1] Lasry, Jean-Michel, and Pierre-Louis Lions. "Mean field games." Japanese journal of mathematics 2.1 (2007): 229-260.

[2] Cardaliaguet, Pierre. Notes on mean field games. Technical report, 2010.

[3] Achdou, Yves, et al. "An introduction to mean field game theory." Mean Field Games: Cetraro, Italy 2019 (2020): 1-158.

[4] https://math.stanford.edu/~ryzhik/STANFORD/MEAN-FIELD-GAMES/notes-mean-field.pdf

[5] QING, YUTONG. "INTRODUCTION TO THE OPTIMAL CONTROL THEORY AND SOME APPLICATIONS." (2019).

[6] https://math.nyu.edu/~goodman/teaching/StochCalc2011/SDE.pdf