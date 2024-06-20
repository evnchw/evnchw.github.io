---
title: "Quick refresher on Hamilton-Jacobi-Bellman"
collection: quant
type: "Post"
permalink: /quant/refresher_hjb
date: 2024-06-21
---

This is a quick refresher on the basic formulation and ideas of Hamilton-Jacobi-Belmman in optimal control, including value functions and dynamic programming.

- I prioritize intuition/readability linking to references where appropriate.
- We will not go deeply into proofs here.
- We may skip over some parts for brevity
- All feedback and corrections are welcome.

Much of these notes and notation is adapted from [1], with additional notes from [2] and [3]. (We keep mean field game theory in mind for down the road.)

## Hamilton-Jacobi-Bellman, deterministic

Here we formulate the simplest, deterministic version of an agent's optimal control problem.

### The agent's control problem

An agent faces the following deterministic optimal control problem:

$$
\begin{align}
    \underset{a \in \mathcal{A}}{\min} \hspace{0.5cm}& \mathcal{J} := \left[\int_0^T L(x_s, a_s)ds + G(x_T) \right] & \text{cost functional} \\
    \textbf{s.t. } \hspace{0.5cm}& \frac{\partial x_t}{\partial t} = f(x_t, a_t) & \text{state dynamics} \\
    \hspace{0.5cm}& x_0 = x & \text{initial state condition} \\
    \hspace{0.5cm}& \forall t \in [0, T]: x_t \in \mathbb{R}^d, a_t \in \mathcal{A} \subset \mathbb{R}^m & \text{states and controls} \\
    f &: \mathcal{R}^d \times \mathcal{R}^m \to \mathcal{R}^d & \text{$f$ is deterministic}
\end{align}
$$

The explanation is as follows. Over the finite time horizon $$t=0, \dots, T$$, the agent wants to minimize the cost functional $$\mathcal{J}$$, which consists of a "running" cost $$L(.)$$ at each time $$t$$, and then a "terminal" cost $$G(.)$$ at the last time period $$T$$.

At each time step $$t=0,\dots,T$$, the mechanics are as follows:

- The agent begins with a vector of states $$x_t \in \mathcal{R}^d$$.
- Subsequently the agent decides which actions to take, aka the vector of controls $$a_t \in \mathcal{R}^m$$.
    - This vector $$a_t$$ takes a measurable value within of a compact space $$\mathcal{A}$$, called the set of admissible controls.
- Then, given the states $$x_t$$ and the controls decided upon $$a_t$$, this generates:
    - The running cost $$\mathcal{L}(x_t, a_t)$$.
    - The incremental change to the state vector $$\dot{x}_t=f(x_t, a_t)$$, and therefore the state vector $$x_{t+\varepsilon}$$ for the next period $$t+\varepsilon$$.

Although this sequence of events occur forward in time, each step depends strictly on the previous step. So from the agent's perspective, it is best to consider the whole sequence and *optimize this sequence of events (costs, states, controls) backward*. This is encapsulated in the principle of dynamic programming.

### The value function

Define $$u(x_t,t)$$ as the *value function*, aka, the optimal (best-achievable) cost starting from a particular time $$t$$ and a particular state $$x_t$ [+].

$$
\begin{align}
u(x_t,t) &= \underset{a \in \mathcal{A}}{\inf} \mathcal{J} := \underset{a \in \mathcal{A}}{\inf} \left[\int_t^T L(x_s, a_s) ds + G(x_T) \right] & \text{value function}
\end{align}
$$

It is notable that $$u(.)$$, as the loose minimum (infinimum), no longer depends on the controls. Moreover, it is defined from a particular time $$t$$. Hence, from any particular starting time $$t$$ and starting state $$x$$, we can compute the optimal cost (bound).

[+] A small abuse of notation: $$x_t$$ is the state at time $$t$$ but is not *defined* by $$t$$. That is, we could write $u(x,t)$ as in the original reference [4] and it would mean the same thing: (states X time).

### Dynamic programming

Consider a value function $$u(x_t,t)$$ at $$(x,t)$$. The principle of dynamic programming says, for any incremental time $$\tau: t < \tau \leq T$$, the value function only needs to be computed incrementally from $$t \to \tau$$, and thereafter will simply be $$u(x_\tau,\tau)$$.

$$
\begin{align}
    u(x_t,t) &= \underset{a \in \mathcal{A}}{\inf} \left[\int_t^\tau L(x_s, a_s) ds + u(x_\tau, \tau) \right]
\end{align}
$$

Intuitively, suppose we are at $$(x,t)$$. If we know the optimal running cost $$\int_t^\tau L(x_s, a_s) ds$$ of moving from $$(x,t) \to (x_\tau, \tau)$$, and the subsequent optimal cost (value function) thereafter $$u(x_\tau, \tau)$$, the *sum* of these give us our optimal cost $$u(x_t,t)$$ that can be achieved at $$(x,t)$$. Hence, the value function can be efficiently computed backward-in-time: given $$u(x_\tau, \tau)$$, we proceed backward to $$(x_\tau, \tau)$$ to compute the running cost from $$(x,t) \to (x_\tau, \tau)$$, and this yields $$u(x, t)$$.

So, if we choose the optimal path at any $$(x,t)$$, we will stay on the optimal path.

### The Hamilton-Jacobi-Bellman equation

So far we have formulated the optimal control problem in terms of (costs, states, controls), and we have introduced the idea of a optimal cost path (value function) that can be computed recursively backward-in-time. The next step will be to examine the dynamics of the value function. Then, we can optimize the controls and compute the resulting states trajectory, giving us the optimal (costs, states, controls) and therefore solving the control problem.

Assume the value function $$u(x_t,t)$$ is continuous and differentiable in both $$x,t$$, and now also, that an *optimal control* $$a^*_t$$ exists for all $$t$$ and is continuous in time. As above, let's explicitly write $$\tau := t + h$$ for some $$h > 0$$. The value function is hence:

$$
\begin{align}
    u(x_t,t) &= \underset{a \in \mathcal{A}}{\inf} \left[\int_t^{t + h} L(x_s, a_s) ds + u(x_{t+h}, t+h) \right]
\end{align}
$$

By continuity of $$u(x_t,t)$$, we can expand $$u(x_{t+h},t+h)$$ via its Taylor series w/the chain rule for $$x_{t+h}$$, noting $$h \equiv \Delta t$$:

$$
\begin{align}
    u(x_{t+h}, t+h) &= u(x, t) + \frac{\partial u(x_t, t)}{\partial x_t} \frac{\partial x_t}{\partial t} h + \frac{\partial u(x_t, t)}{\partial t} h + o(h) & \text{Taylor series w/chain rule} \\
        &= u(x_t,t) + \frac{\partial u(x_t, t)}{\partial x} f(x_t, a_t) h + h \frac{\partial u(x_t, t)}{\partial t} + o(h) &\text{state dynamics } \dot{x}_t = \frac{\partial x_t}{\partial t} = f(x_t, a_t) \\
        &= u(x_t,t) + h f(x_t, a_t) \frac{\partial u(x_t, t)}{\partial x} + h \frac{\partial u(x_t, t)}{\partial t} + o(h) &\text{rearrange}
\end{align}
$$

Applying this expansion, the value function is:

$$
\begin{align}
    u(x_t,t) &= \underset{a \in \mathcal{A}}{\inf} \left[\int_t^{t + h} L(x_s, a_s) ds + \overbrace{u(x_t,t) + h f(x_t, a_t) \frac{\partial u(x_t, t)}{\partial x} + h \frac{\partial u(x_t, t)}{\partial t} + o(h)}^{u(x_{t+h}, t+h)}\right] & \\
    0 &= \underset{a \in \mathcal{A}}{\inf} \left[\int_t^{t + h} L(x_s, a_s) ds + h f(x_t, a_t) \frac{\partial u(x_t, t)}{\partial x} + h \frac{\partial u(x_t, t)}{\partial t} + o(h) \right] & \text{terms } u(x_t,t) \text{ cancel} \\
    0 &=  h \frac{\partial u(x_t, t)}{\partial t} + o(h) + \underset{a \in \mathcal{A}}{\inf} \left[\int_t^{t + h} L(x_s, a_s) ds + h f(x_t, a_t) \frac{\partial u(x_t, t)}{\partial x} \right] & \text{take out } o(h) \text{ and } hu_t(x_t,t) \\
    0 &=  \frac{\partial u(x_t, t)}{\partial t} + \frac{o(h)}{h} + \underset{a \in \mathcal{A}}{\inf} \left[\frac{1}{h} \int_t^{t + h} L(x_s, a_s) ds + h f(x_t, a_t) \frac{\partial u(x_t, t)}{\partial x} \right] & \text{divide by } h \\
\end{align}
$$

Since we have assumed $a_t$ is continuous in time, let $h \to 0$. Note first the running cost term converges as follows ([Limit of average integral - StackExchange](https://math.stackexchange.com/questions/3790721/limit-of-average-value-on-interval-as-it-shrinks)):

$$
\begin{align}
    \lim_{h \to 0} \frac{1}{h} \int_t^{t+h} L(x_s, a_s) ds = L(x_t, a_t)
\end{align}
$$

The $$o(h)/h$$ term goes to zero, hence plugging this and rearranging we obtain the famous **Hamilton-Jacobi-Bellman** equation which gives the dynamics of the value function.

$$
\begin{align}
\frac{\partial u(x_t,t)}{\partial t} + \overbrace{\underset{a \in \mathcal{A}}{\inf} \left[L(x_t, a_t) + f(x_t, a_t) \frac{\partial u(x_t, t)}{\partial x}\right]}^{\text{"Hamiltonian" } H(\nabla u, x_t)} &= 0 & \text{Hamilton-Jacobi-Bellman (HJB) equation} \\
\frac{\partial u(x_t,t)}{\partial t} + H(\nabla u, x_t) &= 0 & \text{concise notation} \\
u(x_T, T) &= G(x_T) &\text{recall: terminal condition}
\end{align}
$$

Intuitively, the Hamiltonian can be interpreted as the instantaneous version of the Lagrangian from static optimization ([Wiki](https://en.wikipedia.org/wiki/Hamiltonian_(control_theory))), combining your running cost from being in a state with the sensitivity to the changes in your state. This can be thought of as a tradeoff between your current cost vs. your (near-)future cost, which by the equation must match the change in the optimal cost (value function) at equilibrium.

The optimal controls ($$a^*_t$$) and optimal trajectory of states ($$x^*_t$$) are given indirectly as the solution to the following set of partial differential equations:

$$
\begin{align*}
    a^*_t &= \underset{a \in \mathcal{A}}{\text{argmin}} \left[L(x_t^*, a_t) + f(x_t^*, a_t) \frac{\partial u(x_t^*, t)}{\partial x}\right] & \text{optimal controls} \\
    \textbf{s.t. } \hspace{0.5cm}& \frac{\partial x_t^*}{\partial t} = f(x_t^*, a_t) & \text{optimal state dynamics} \\
    \hspace{0.5cm}& x_0^* = x & \text{initial state condition} \\
\end{align*}
$$

Simple analytical results are often not feasible, and moreover, this has assumed smoothness for the value function and controls.

## Hamilton-Jacobi-Bellman, stochastic

Now, we reformulate the problem in a textbook way with stochastic drift and diffusion.

### The agent's control problem

TODO

# References

[1] https://math.stanford.edu/~ryzhik/STANFORD/MEAN-FIELD-GAMES/notes-mean-field.pdf

[2] QING, YUTONG. "INTRODUCTION TO THE OPTIMAL CONTROL THEORY AND SOME APPLICATIONS." (2019).

[3] https://math.nyu.edu/~goodman/teaching/StochCalc2011/SDE.pdf