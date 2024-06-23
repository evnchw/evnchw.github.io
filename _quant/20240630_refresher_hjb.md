---
title: "Quick refresher on Hamilton-Jacobi-Bellman"
collection: quant
type: "Post"
permalink: /quant/20240630_refresher_hjb
date: 2024-06-30 # TODO: update
---

This is a quick refresher on the basic formulation and ideas of Hamilton-Jacobi-Bellman in optimal control, including value functions and dynamic programming for both deterministic and stochastic formulations.

The notes and notation here are adapted from [1], with additional notes from [2] and [3]. (We keep mean field game theory in mind for down the road.) I go into much more detail to understand each aspect.

- I prioritize intuition/readability linking to references where appropriate.
- We will focus on the key equations, not go too deeply into proofs and may skip some parts for brevity.
- All feedback and corrections are welcome.

Lastly, this focuses solely understanding HJB through the dynamic programming perspective. Later topics around the calculus of variations, Euler-Lagrange, viscosity solutions, etc. will be covered in future posts.

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
    f &: \mathbb{R}^d \times \mathbb{R}^m \to \mathbb{R}^d & \text{$f$ is deterministic} 
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
- Alternatively upon completion, this yields the terminal cost $$G(x_T)$$.

Although this sequence of events occur forward in time, each step depends strictly on the previous step. So from the agent's perspective, it is best to consider the whole sequence and *optimize this sequence of events (costs, states, controls) backward*. This is encapsulated in the principle of dynamic programming.

### The value function

Define $$u(x_t,t)$$ as the *value function*, aka, the optimal (best-achievable) cost starting from a particular time $$t$$ and a particular state $$x_t$$ [+].

$$
\begin{align}
u(x_t,t) &= \underset{a \in \mathcal{A}}{\inf} \mathcal{J} := \underset{a \in \mathcal{A}}{\inf} \left[\int_t^T L(x_s, a_s) ds + G(x_T) \right] & \text{value function}
\end{align}
$$

It is notable that $$u(.)$$, as the loose minimum (infinimum), no longer depends on the controls. Moreover, it is defined from a particular time $$t$$. Hence, from any particular starting time $$t$$ and starting state $$x$$, we can compute the optimal cost (bound).

[+] A small abuse of notation: $$x_t$$ is the state at time $$t$$ but is not *defined* by $$t$$. That is, we could write $$u(x,t)$$ as in the original reference [4] and it would mean the same thing: (states X time).

### Dynamic programming

Consider a value function $$u(x_t,t)$$ at $$(x,t)$$. The principle of dynamic programming says, for any incremental time $$\tau: t < \tau \leq T$$, the value function only needs to be computed incrementally from $$t \to \tau$$, and thereafter will simply be $$u(x_\tau,\tau)$$.

$$
\begin{align}
    u(x_t,t) &= \underset{a \in \mathcal{A}}{\inf} \left[\int_t^\tau L(x_s, a_s) ds + u(x_\tau, \tau) \right] & \text{dynamic programming principle}
\end{align}
$$

Intuitively, suppose we are at $$(x,t)$$. If we know the optimal running cost $$\int_t^\tau L(x_s, a_s) ds$$ of moving from $$(x,t) \to (x_\tau, \tau)$$, and the subsequent optimal cost (value function) thereafter $$u(x_\tau, \tau)$$, the *sum* of these give us our optimal cost $$u(x_t,t)$$ that can be achieved at $$(x,t)$$. Hence, the value function can be efficiently computed backward-in-time: given $$u(x_\tau, \tau)$$, we proceed backward to $$(x_\tau, \tau)$$ to compute the running cost from $$(x,t) \to (x_\tau, \tau)$$, and this yields $$u(x, t)$$.

So, if we choose the optimal path at any $$(x,t)$$, we will stay on the optimal path.

### The HJB equation

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

Since we have assumed $$a_t$$ is continuous in time, let $$h \to 0$$. Note first the running cost term converges as follows ([Limit of average integral - StackExchange](https://math.stackexchange.com/questions/3790721/limit-of-average-value-on-interval-as-it-shrinks)):

$$
\begin{align}
    \lim_{h \to 0} \frac{1}{h} \int_t^{t+h} L(x_s, a_s) ds = L(x_t, a_t)
\end{align}
$$

noting for the StackExchange answer this follows the same format $$\lim_{b \to a} \frac{1}{b-a} \int_a^b q(x) dx$$, with $$b=t+h$$ and $$a=t$$.

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

Now the agent faces the following stochastic optimal control problem, defined over some time period $$[t, T]$$, and where $$s \in [t,T]$$.

$$
\begin{align}
    \underset{a \in \mathcal{A}}{\min} \hspace{0.5cm}& \mathcal{J} := \mathbb{E}\left[\int_t^T L(x_s, a_s, t)ds + G(x_T) \right] & \text{cost functional} \\
    \textbf{s.t. } \hspace{0.5cm}& d x_s = \underbrace{f(x_s, a_s, s) ds}_{\text{drift}} + \underbrace{\sigma(x_s, a_s, s) dB_s}_{\text{diffusion}} & \text{state dynamics} \\
    &\hspace{1cm} f(.): [t,T] \times \mathbb{R}^d \times \mathbb{R}^m \to \mathbb{R}^{d} \\
    &\hspace{1cm} \sigma(.): [t,T] \times \mathbb{R}^d \times \mathbb{R}^m \to \mathbb{R}^{d \times n} \\
    &\hspace{1cm} B_s: \text{Brownian on } \left(\Omega, \mathcal{F}, \{\mathcal{F}_s\}_{s \geq t}, P\right) \\
    \hspace{0.5cm}& x_t = x & \text{initial state condition} \\
    \hspace{0.5cm}& a_s (\omega):  [t, T] \times \Omega \to \mathbb{R}^m \hspace{0.5cm} \text{ adapted to } \{\mathcal{F_s}\}_{s\geq t} & \text{controls} \\
    \hspace{0.5cm}& x_s (\omega):  [t, T] \times \Omega \to \mathbb{R}^d & \text{states}
\end{align}
$$

Immediately, we see the cost functional is now stochastic (and expressed *in expectation*). We also observe that the agent now controls the state dynamics via a non-stochastic "drift" $$f(.)ds$$, and a stochastic "diffusion" $$\sigma(.)dB_s$$.

*As a stochastic process.* In the deterministic case, if we chose the optimal control we would know (mechanically) how everything would unfold thereafter. However, in this case there is randomness following each time step, and so in considering a control $$a_s$$ at time $$s$$ we do not know exactly how the future will unfold. Therefore, it is important that our control process only use information available at the time ("point-in-time"). More formally, define the *filtration* of the control process as the (montonically expanding) set of information we acquire over time: $$\{\mathcal{F_s}\}_{s \geq t} = \{ \mathcal{F}_t \subseteq \mathcal{F}_{t+1} \subseteq \dots \}$$. Hence, we say that our control process $$a_s$$ is *adapted* to this filtration in that it only uses $$\mathcal{F}_s$$, the set of information known up to time $$s$$ (no peeking into the future!).

*A note on randomness.* Now, the randomness comes from $$B_s$$, a Brownian on the probability space $$\left(\Omega, \mathcal{F}, \{\mathcal{F}_s\}_{s \geq t}, P\right)$$. At each time step $$s$$ it takes on the realization of a random outcome $$\omega \in \Omega$$ ("possible outcomes," specifically a sigma-algebra), according to the probability measure $$P$$ and respecting the current filtration $$\mathcal{F}_s$$. This (realized) random draw $$\omega \in \Omega$$ impacts the states and controls thereafter, hence we write $$x_s(\omega)$$ and $$a_x(\omega)$$ to indicate they depend on this randomness.

*Sequence of events at each time.* Therefore, the sequence of events of time $$s$$ proceeds as follows:

- The agent begins with a vector of states $$x_s(\omega) \in \mathcal{R}^d$$ as well as that realized Brownian draw $$\omega \in \Omega$$.
- On observing those the agent decides which actions to take, aka the vector of controls $$a_s(\omega) \in \mathcal{R}^m$$.
    - This only uses the set of information known up to $s$, aka $$\{\mathcal{F_s}\}_{s \geq t}$$.
- Then, given the states $$x_t$$ and the controls decided upon $$a_t$$, this generates:
    - The running cost $$\mathcal{L}(x_s, a_t, s)$$.
    - A new realization $$\omega \in \Omega$$ of the Brownian $$B_s$$.
    - Subsequently, the incremental change to the state vector $$\dot{x}_s=f(.) ds + \sigma(.)dB_s$$.
    - This yields the state vector $$x_{s+\varepsilon}$$ for the next period $$s+\varepsilon$$, as well as $$\omega$$.
- Alternatively upon completion, this yields the terminal cost $$G(x_T)$$.

### The value function

As in the deterministic case, we can define the *value function*, noting that we must express it in expectation:

$$
\begin{align}
u(x_t,t) &= \underset{a \in \mathcal{A}}{\inf} \mathcal{J} := \underset{a \in \mathcal{A}}{\inf} \mathbb{E} \left[\int_t^T L(x_s, a_s, s) ds + G(x_T) \right] & \text{value function}
\end{align}
$$

### Dynamic programming

Following this logic, the dynamic programming relation is given by:

$$
\begin{align}
    u(x_t,t) &= \underset{a \in \mathcal{A}}{\inf} \mathbb{E} \left[\int_t^\tau L(x_s, a_s, s) ds + u(x_\tau, \tau) \right] & \text{dynamic programming principle}
\end{align}
$$

for $$t < \tau$$ of c

### The HJB equation
 
Here we proceed in a similar way as in the deterministic case, except that instead of the chain rule, we need to use Ito's Lemma, and specifically for our state dynamics which is a multivariate drift-diffusion process. Adapted for our notation from [Wikipedia](https://en.wikipedia.org/wiki/It%C3%B4%27s_lemma):

<p style="text-align: center; font-weight: bold; font-family: Serif">Itô's lemma for a multivariate drift-diffusion process</p>

For any time $$s \in [t, \tau]$$, let $$X_s=(X_s^1, \dots, X_s^n)^T$$ be a real-valued vector of Itô processes, following:

$$
\begin{align}
dX_s &= \mu_s ds + G_s dB_s
\end{align}
$$

for a vector $$\mu_s$$, matrix $$G_s$$ and Brownian $$B_s$$. Moreover, let $$f(s, X_s)$$ be a twice differentiable function in both arguments. Then the lemma states:

$$
\begin{align}
d f(s, X_s) &= \frac{\partial f}{\partial s} ds + (\nabla_X f)^T dX_s + \frac{1}{2} (dX_s)^T (H_X f) dX_s \\
&= \left( \frac{\partial f}{\partial s} + (\nabla_x f)^T \mu_s + \frac{1}{2} \text{Tr}\left[G_s^T (H_x f) G_s\right] \right) ds + (\nabla_x f)^T G_s dB_s
\end{align}
$$

where $$\nabla_x f$$ is the gradient of $$f$$ wrt. X, $$H_x f$$ is the Hessian of $$f$$ wrt. $$X$$, and $$\text{Tr}$$ is the trace operator. In essence, this lemma says: given the dynamics of random vector $$X_s$$ that changes over time ($$s$$), we can find the dynamics of a transformation $$f(X_s, s)$$. Note here in the case of drift-diffusion, the dynamics of the transformation also take on a drift-diffusion form. $$\square$$

*Applying this to find a stochastic HJB equation.* As before, our strategy is to obtain the dynamics of the value function $$u(.)$$, which is a function of states $$X_s$$ and time $$s$$. These resulting dynamics (the stochastic HJB equation) will indirectly define the optimal controls and trajectory of states. Note we require $$u(.)$$ to be twice differentiable in its arguments.

Let's recall our state dynamics and dynamic programming relation, and label each component so it corresponds to the above format of Itô's lemma. (Recall $$x_s, a_s, G_s, \dots$$ are all vector and matrix quantities).

$$
\begin{align}
d x_s &= \overbrace{f(x_s, a_s, s)}^{\mu_s} ds + \overbrace{\sigma(x_s, a_s, s)}^{G_s} dB_s & \text{state dynamics} \\
x_t &= x & \text{initial state condition} \\
\underbrace{u(x_t,t)}_{f} &= \underset{a \in \mathcal{A}}{\inf} \mathbb{E} \left[\int_t^\tau L(x_s, a_s, s) ds + \underbrace{u(x_\tau, \tau)}_{f} \right] & \text{dynamic programming principle}
\end{align}
$$

As before, our strategy is to obtain the dynamics of the value function $$u(.)$$, which indirectly defines the optimal controls and trajectory of states. Consistent for the lemma, we require the $$u(.)$$ to be twice differentiable in its arguments. With $$\tau$$ analogous to $$t+h$$ above, write out the expansion of $$u(x_\tau, \tau)$$ via the lemma:

$$
\begin{align}
    \underbrace{u(x_\tau, \tau) - u(x,t)}_{d f(s, X_s)} = &
            \underbrace{\int_t^\tau \left(\frac{\partial u(x_s, s)}{\partial t} + \frac{\partial u(x_s, s)}{\partial x} f(x_t, a_t, t) +
            \frac{1}{2} \text{Tr}(D^2 u(x_s, s) \sigma(x_s, a_s, s)\sigma^T(x_s, a_s, s)) \right) ds
            }_{
                \left(
                    \frac{\partial f}{\partial s} + (\nabla_X f)^T \mu_s + \frac{1}{2} \text{Tr}\left[ G_s^T (H_x f) G_s \right]
                \right) ds
            } \\
            &+
            \underbrace{
                \int_t^\tau \frac{\partial u(x_s, s)}{\partial x}^T \sigma(x_s, a_x, s) dB_s
            }_{
                (\nabla_X f)^T G_s dB_s
            } & \text{via Itô} \\
            =&
            \int_t^\tau \left(\frac{\partial u(x_s, s)}{\partial t} + \mathcal{L}^\alpha u \right) ds +
                \int_t^\tau \frac{\partial u(x_s, s)}{\partial x}^T \sigma(x_s, a_x, s) dB_s & \text{rewriting} \\
            &\text{where } \mathcal{L}^\alpha (u) = \frac{\partial u(x_s, s)}{\partial x} f(x_t, a_t, t) +
            \frac{1}{2} \text{Tr}( H_x u(x_s, s)\sigma(x_s, a_s, s)\sigma^T(x_s, a_s, s))
\end{align}
$$

where $$H_x u(x_s, s)$$ is the Hessian of $$u$$ wrt. $$x$$. Note also that the increment $$t \to \tau$$ functions as the "differential change in time" here: we could mirror the chain rule formulation directly and write $$u(x_\tau, \tau) = u(x, t) + \dots$$

Now plug this into the dynamic programming formulation above:

$$
\begin{align}
    u(x_t,t) &= \underset{a \in \mathcal{A}}{\inf} \mathbb{E} \left[\int_t^\tau L(x_s, a_s, s) ds + u(x_\tau, \tau)\right] & \text{dynamic programming} \\
    0 &= \underset{a \in \mathcal{A}}{\inf} \mathbb{E} \left[
        \int_t^\tau L(x_s, a_s, s) ds + u(x_\tau, \tau) - u(x_t, t)
    \right] & \text{subtract } u(x_t, t) \\
    0 &= \underset{a \in \mathcal{A}}{\inf} \mathbb{E} \left[
        \int_t^\tau L(x_s, a_s, s) ds +
            \int_t^\tau \left(\frac{\partial u(x_s, s)}{\partial t} + \mathcal{L}^\alpha u \right) ds +
            \int_t^\tau \frac{\partial u(x_s, s)}{\partial x}^T \sigma(x_s, a_x, s) dB_s
    \right] & \text{substitute lemma result} \\
    &\text{note } 
        \underset{a \in \mathcal{A}}{\inf} \mathbb{E} \left[ \int_t^\tau \frac{\partial u(x_s, s)}{\partial x}^T \sigma(x_s, a_x, s) dB_s \right] = 0 & \text{martingale has zero mean} \\
    0 &= \underset{a \in \mathcal{A}}{\inf} \mathbb{E} \left[
        \int_t^\tau L(x_s, a_s, s) ds +
            \int_t^\tau \left(\frac{\partial u(x_s, s)}{\partial t} + \mathcal{L}^\alpha u \right) ds
    \right] & \text{substitute lemma result}
\end{align}
$$

Note the subtraction goes into the expectation because $$u(x_t, t)$$ is an infimum. Now, let $$\tau := t+h$$, divide by $$h$$ and let $$h \to 0$$:

$$
\begin{align}
    0 &= \underset{a \in \mathcal{A}}{\inf} \mathbb{E} \left[
            \frac{1}{h} \int_t^{t+h} L(x_s, a_s, s) ds +
            \frac{1}{h} \int_t^{t+h} \left(\frac{\partial u(x_s, s)}{\partial t} + \mathcal{L}^\alpha u \right) ds
        \right] \\
    &= \underset{a \in \mathcal{A}}{\inf} \mathbb{E} \left[
        \frac{1}{h} \int_t^{t+h} \frac{\partial u(x_s, s)}{\partial t} ds + 
        \frac{1}{h} \int_t^{t+h} L(x_s, a_s, s) ds +
        \frac{1}{h} \int_t^{t+h} \mathcal{L}^\alpha (u) ds
    \right]
\end{align}
$$

This yields our desired HJB equation:

$$
\begin{align}
    0 &= \frac{\partial u(x,t)}{\partial t} + \underset{a \in \mathcal{A}}{\inf} \mathbb{E} \left[
        L(x_t, a_t, t) + \mathcal{L}^a(u)
        \right] \\
    0 &= \frac{\partial u(x,t)}{\partial t} +
        \underbrace{
            \underset{a \in \mathcal{A}}{\inf} \mathbb{E} \left[
            L(x_t, a_t, t) +
            \frac{\partial u(x_s, s)}{\partial x} f(x_t, a_t, t) +
            \frac{1}{2} \text{Tr}(H_xu(x_s, s) \sigma(x_s, a_s, s)\sigma^T(x_s, a_s, s))
        \right]
        }_{\text{The Hamiltonian } \mathcal{H}(H_x(u), \nabla_x(u), x_t, t)} \\
    & \text{note this is of form } \hspace{0.25cm} 0 = \frac{\partial u}{\partial t} + \mathcal{H}(H_x(u), \nabla_x(u), x_t, t) \hspace{0.25cm} \text{with Hessian } H_x(u) \text{, vector of derivatives } \nabla_x(u)
\end{align}
$$

The interpretation is that at optimum, the instantaneous change in today's cost can be decomposed into the incremental (running) cost to tomorrow plus tomorrow's cost. The Hamiltonian $$\mathcal{H}$$ captures the tradeoff between "current" and "future" costs, which must be determined by the controls.

Lastly, to tie this back to the optimal controls and trajectory of states, we summarize our system dynamics as before to define the optimal controls and states indirectly:

$$
\begin{align}
    0 &= \frac{\partial u(x,t)}{\partial t} + \underset{a \in \mathcal{A}}{\inf} \mathbb{E} \left[
            L(x_t, a_t, t) +
            \frac{\partial u(x_s, s)}{\partial x} f(x_t, a_t, t) +
            \frac{1}{2} \text{Tr}(D^2 u(x_s, s) \sigma(x_s, a_s, s)\sigma^T(x_s, a_s, s))
        \right] & \text{HJB equation} \\
        &= \frac{\partial u}{\partial t} + \mathcal{H}(H_x(u), \nabla_x(u), x_t, t) & \text{(HJB equation, simplified)} \\
    d x_s &= f(x_s, a_s, s) ds + \sigma(x_s, a_s, s) dB_s & \text{state dynamics} \\
    x_t &= x & \text{initial state condition}
\end{align}
$$

where optimal controls and trajectory of states $$(x_t^{*}, a_t^{*})$$ satisfy the above system to yield the optimal cost $$u_t$$. $$\square$$.

Note that the HJB equation is a second-order differential equation via the Hamiltonian $$\mathcal{H}$$, and so can be infeasible if not impossible to solve analytically. This motivates the idea of the *Legendre transform* to find a feasible solution via an extremal-preserving conjugate transformation, which we may cover in a future post.
 
# References

[1] https://math.stanford.edu/~ryzhik/STANFORD/MEAN-FIELD-GAMES/notes-mean-field.pdf

[2] QING, YUTONG. "INTRODUCTION TO THE OPTIMAL CONTROL THEORY AND SOME APPLICATIONS." (2019).

[3] https://math.nyu.edu/~goodman/teaching/StochCalc2011/SDE.pdf