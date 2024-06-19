# A brief refresher on mean field games

While brushing up on mean field game theory ("MFG") I wanted to write a brief refresher to solidify the key ideas, even if only for myself. Hence in this blog post I aim to present the key formulation and ideas of MFG in a concise, informal and practical way.

In favor of accessibility there will be some imprecisions in this exposition: all feedback and corrections are welcome.

The fundamental idea of MFG is to model (differential) game-theoretic equilibria where there are a very large number of agents. The key characteristic is that each agent optimizes decisions against the *distribution* of everyone else's decisions (the "mean field"), and where agents are identical to some degree. This allows one to obtain asymptotic equilibria by surmounting the usual combinatorial (agent-to-agent) complexity of differential game theory. Applications of include modeling traffic congestion, pedestrian foot traffic, financial markets, and more.

The idea was originally presented in [1]. Introductory notes to this were compiled in [2] and [3], and upon those even more introductory notes were compiled at Stanford [4]. I base this brief refresher upon several excellent resources.

- The core of this material and notation is primarily drawn and restated from [4].
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

<p align="center"><strong>FORMULATION</strong></p>

An agent faces the following optimal control problem:

$$
\begin{align}
    \underset{a \in \mathcal{A}}{\min} \hspace{0.5cm}& \mathcal{J} := \mathbb{E} \left[\int_0^T L(x_s, a_s)ds + G(x_T) \right] & \text{cost functional} \\
    \textbf{s.t. } \hspace{0.5cm}& \dot{x}_t = f(x_t, a_t) & \text{state dynamics} \\
    \hspace{0.5cm}& x_0 = x & \text{initial state condition} \\
    \hspace{0.5cm}& \forall t \in [0, T]: x_t \in \mathbb{R}^d, a_t \in \mathcal{A} \subset \mathbb{R}^m & \text{states and controls}
\end{align}
$$

where $f: \mathcal{R}^d \times \mathcal{R}^m \to \mathcal{R}^d$ is deterministic.

The explanation is as follows. Over the finite time horizon $t=0, \dots, T$, the agent wants to minimize the cost functional $\mathcal{J}$, which consists of a "running" cost $L(.)$ at each time $t$, and then a "terminal" cost $G(.)$ at the last time period $T$.

At each time step $t=0,\dots,T$, the mechanics are as follows:

- The agent begins with a vector of states $x_t \in \mathcal{R}^d$.
- Subsequently the agent decides which actions to take, aka the vector of controls $a_t \in \mathcal{R}^m$.
    - This vector $a_t$ takes a measurable value within of a compact space $\mathcal{A}$, called the set of admissible controls.
- Then, given the states $x_t$ and the controls decided upon $a_t$, this generates:
    - The running cost $\mathcal{L}(x_t, a_t)$.
    - The incremental change to the state vector $\dot{x}_t=f(x_t, a_t)$, and therefore the state vector $x_{t+\varepsilon}$ for the next period $t+\varepsilon$.

Although this sequence of events occur forward in time, each step depends strictly on the previous step. So from the agent's perspective, it is best to consider the whole sequence and *optimize this sequence of events (costs, states, controls) backward*. This is encapsulated in the principle of dynamic programming.

<p align="center"><strong>THE VALUE FUNCTION</strong></p>

Define $u(x,t)$ as the *value function*, aka, the optimal (best-achievable) cost starting from a particular time $t$.

$$
\begin{align}
u(x,t) &= \underset{a \in \mathcal{A}}{\inf} \mathcal{J} := \underset{a \in \mathcal{A}}{\inf} \mathbb{E} \left[\int_t^T L(x_s, a_s) ds + G(x_T) \right] & \text{value function}
\end{align}
$$

It is notable that $u(.)$, as the loose minimum (infinimum), no longer depends on the controls but only the sequence of state vectors $x_t$ (incl. the initial). Moreover, it is defined from a particular time $t$. Hence, from any particular starting time $t$ and starting states $x$, we can compute the optimal cost (bound).

<p align="center"><strong>DYNAMIC PROGRAMMING</strong></p>

Consider a value function $u(x,t)$ at $(x,t)$. The principle of dynamic programming says, for any incremental time $\tau: t < \tau \leq T$, the value function only needs to be computed incrementally from $t \to \tau$, and thereafter will simply be $u(x_\tau,\tau)$.

$$
\begin{align*}
    u(x,t) &= \underset{a \in \mathcal{A}}{\inf} \mathbb{E} \left[\int_t^\tau L(x_s, a_s) ds + u(x_\tau, \tau) \right]
\end{align*}
$$

Intuitively, suppose we are at $(x,t)$. If we know the optimal running cost $\int_t^\tau L(x_s, a_s) ds$ of moving from $(x,t) \to (x_\tau, \tau)$, and the subsequent optimal cost (value function) thereafter $u(x_\tau, \tau)$, the *sum* of these give us our optimal cost $u(x,t)$ that can be achieved at $(x,t)$. Hence, the value function can be efficiently computed backward-in-time: given $u(x_\tau, \tau)$, we proceed backward to $(x_\tau, \tau)$ to compute the running cost from $(x,t) \to (x_\tau, \tau)$, and this yields $u(x, t)$.

<p align="center"><strong>HAMILTON-JACOBI-BELLMAN</strong></p>

Assume the value function $u(x,t)$ is continuous and differentiable in both $x,t$, and that the optimal control $a^*_t$ is continuous in time. As above, let's explicitly write $\tau := t + h$ for some $h > 0$. 






### From HJB to Euler-Lagrange









## References

[1] Lasry, Jean-Michel, and Pierre-Louis Lions. "Mean field games." Japanese journal of mathematics 2.1 (2007): 229-260.

[2] Cardaliaguet, Pierre. Notes on mean field games. Technical report, 2010.

[3] Achdou, Yves, et al. "An introduction to mean field game theory." Mean Field Games: Cetraro, Italy 2019 (2020): 1-158.

[4] https://math.stanford.edu/~ryzhik/STANFORD/MEAN-FIELD-GAMES/notes-mean-field.pdf

[5] QING, YUTONG. "INTRODUCTION TO THE OPTIMAL CONTROL THEORY AND SOME APPLICATIONS." (2019).

[6] https://math.nyu.edu/~goodman/teaching/StochCalc2011/SDE.pdf