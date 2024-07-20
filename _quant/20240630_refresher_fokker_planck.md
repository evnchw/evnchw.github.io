---
title: "[under construction] Quick refresher on Fokker-Planck (drift-diffusion)"
collection: quant
type: "Post"
permalink: /quant/20240714_refresher_fokker_planck
date: 2024-07-14
---

These are my quick refresher notes on Fokker-Planck equation(s) for the evolution of a probability density over time. Like my notes on [Hamilton-Jacobi-Bellman](https://evnchw.github.io/quant/20240623_refresher_hjb), I focus on the main analytical aspects and intuitive understanding rather than the detailed proofs. I follow a similar format as well.

- I prioritize intuition/readability linking to references where appropriate.
- We will focus on the key equations, not go too deeply into proofs and may skip some parts for brevity.
- All feedback and corrections are welcome.

There are various ways to look at Fokker-Planck (see [1] for a relatively recent introduction, and [2] for a control-oriented treatment), but we are going to work through the view of Fokker-Planck sketched in [3] in the context of mean field games (MFG). Specifically:

1. We wish to understand a particular forward Fokker-Planck equation that appears in MFG
2. We want to understand a particular associated drift-diffusion solution

In other words, we go backward: we have the the FP equation for how a probability density evolves, and then we want to understand which probability densities can satisfy this. This is important because it tells us what our theoretical (distributional) boundaries are for modeling many-agent behavior in MFG and what is required to take advantage of MFG results.

## In a nutshell: the FP equation provides a way to model the evolution of a probability density over time

From [Wikipedia](https://en.wikipedia.org/wiki/Fokker%E2%80%93Planck_equation):

> In statistical mechanics and information theory, the Fokker–Planck equation is a partial differential equation that describes the time evolution of the probability density function of the velocity of a particle under the influence of drag forces and random forces, as in Brownian motion. The equation can be generalized to other observables as well. The Fokker-Planck equation has multiple applications in information theory, graph theory, data science, finance, economics etc.

## The main result we want to show

This is a result in [3] but we present it in a more linear order, from the particular state dynamics to the final Fokker-Planck equation.

### Setup.

We have a $$d$$-dimensional vector of states $$X \in \mathbb{R}^d$$, and a continuous but finite timeline $$t \in [0, T]$$. Define a "drift" function $$b: \mathbb{R}^D \times [0, T] \to \mathbb{R}$$ which is Hölder-continuous in space and continuous in time.

### State dynamics.

We consider this drift-diffusion stochastic differential equation (SDE) for the time evolution of $$X$$:

$$
\begin{align}
    d X_t &= \overbrace{-b (X_t, t) dt}^{\text{drift}} + \overbrace{\sqrt{2} dB_t}^{\text{diffusion}} & t \in [0, T] \hspace{0.5cm} \text{state evolution} \\
    X_0 &= Z_0 & \text{initial state}
\end{align}
$$

### Our goal: dynamics of the probability density (transformation) over the states.

In the MFG world, we are interested in how the *distribution* of $$X$$ evolves over time. The idea is that we have many identical agents and so their distribution of states will evolve in the same way. Of course, this means we just want to use a density function of $$X$$, and so Fokker-Planck will tell us what the dynamics of this $$X$$-transformation will be.

Our goal is to see how the above drift-diffusion system satisfies the Fokker-Planck equation:

$$
\begin{align}
    \frac{\partial m}{\partial t} - \Delta m - \text{div} (mb) &= 0 & \text{in } \mathbb{T}^d \times (0,T) & \hspace{0.5cm} \text{density evolution} \\
    m(0,x) &= m_0 (x) & \text{initial density}
\end{align}
$$

<!--
TODO:
- define probability measure on complex unit circle (mathbb T)
- define the \Delta operator for m
- https://www.thphys.uni-heidelberg.de/~wolschin/statsem23_6.pdf
-->

where we have defined the density of $$X$$ as $$m \in L^1(\mathbb{T}^d \times [0,T])$$. That is, $$m(x, t)$$ will be the density of $$x$$ at time $$t$$.

- Note that since this is a probability density over states, (at each time) it must sum up to 1 and so its domain is **not** based on $$\mathbb{R}^d$$ but rather restricted to the $$d$$-dimensional probability simplex $$\mathbb{T}^d$$. (For example, if $$d=2$$, then we can select $$\{x, y \in [0,1]: x + y = 1\}$$.)
- The component $$L^1$$ means that $$m$$ is a member of the Lebesgue space $$L^1$$ ([StackExchange](https://math.stackexchange.com/questions/745894/what-does-it-mean-to-be-an-l1-function)): informally, the absolute value of $$m$$ is bounded everywhere.

<!--
https://math.stackexchange.com/questions/2790010/what-does-the-delta-notation-in-this-formula-mean
-->

Note that $$\Delta m$$ is the [Laplace operator](https://en.wikipedia.org/wiki/Laplace_operator): $$\Delta m = \frac{\partial^2 m}{\partial x^2}$$.

<!--
This says the density $$m(x,t)$$ starts from some initial distribution $$m_0(x)$$. Then, it follows dynamics such that the instantaneous change in $$m$$ ($$\frac{\partial m}{\partial t}$$) is equal to the change wrt. to a state:
--> 

## Informal derivation: from the state dynamics to Fokker-Planck

*Follows the derivation in [4].*

Our strategy to obtain the probability density will be indirect. First, we will use Ito's formula ([see my post on HJB](https://evnchw.github.io/quant/20240623_refresher_hjb)) for some arbitrary but well-defined function $$\phi(x)$$. Then, we will take the expectation at a given time to explicitly reveal the density $$m(x,t)$$. Finally, we will draw on the calculus of variations to eliminate the arbitrary test function from our equation, leaving only the dynamics of $$m(x,t)$$.

Our state dynamics are (from above):

$$
\begin{align}
    d X_t &= -b (X_t, t) dt + \sqrt{2} dB_t & t \in [0, T] \hspace{0.5cm} \text{state evolution} \\
    X_0 &= Z_0 & \text{initial state}
\end{align}
$$

Now, introduce an arbitrary test function $$\phi(X): \mathbb{R}^d \to \mathbb{R}$$ such that BOUNDEDNESS ETC. (This represents a non-dynamic transformation on $$X$$ only). <!-- We obtain two representations of the time derivative of $$\mathbb{E}_x[\phi]$$, show they are equal, and then equality of the integrands will reveal Fokker Planck. -->

<!--
First, directly represent take the expectation of $$\phi$$ wrt. $$X$$ and then its time derivative:

$$
\begin{align}
    \frac{d \mathbb{E}[\phi(X_t)]}{d t} &= \frac{d}{d t} \int_{\mathbb{T}^d} \phi(X_t) m(X_t, t) dX_t & \text{def. of expectation wrt.} X \\
    &= \int_{\mathbb{T}^d} \phi(X_t) \frac{\partial m(X_t, t)}{\partial t} dX_t & \text{Lebesgue integral rule: bounds don't depend on } t
\end{align}
$$

(Not quite sure about the E[d phi(x)] = d E[phi(x)] part.)

To obtain a second representation of this quantity, apply Ito's lemma to $\phi$:

$$
\begin{align}
    d \phi(X_t) &= \left[
        \frac{\partial \phi(X_t)}{\partial t}
        - b(X_t, t) \frac{\partial \phi(X_t)}{\partial X_t}
        + \frac{\partial^2 \phi(X_t)}{\partial X_t^2}
    \right] dt +
    \sqrt{2} \frac{\partial \phi(X_t)}{\partial X_t} dB_t & \text{diffusion coefficient $\sqrt{2}$ cancels out} \\
    \mathbb{E}[d \phi (X_t)] &= \mathbb{E}\left( \left[
        \frac{\partial \phi(X_t)}{\partial t}
        - b(X_t, t) \frac{\partial \phi(X_t)}{\partial X_t}
        + \frac{\partial^2 \phi(X_t)}{\partial X_t^2}
     \right] dt \right) +
    \mathbb{E} \left(\sqrt{2} \frac{\partial \phi(X_t)}{\partial X_t} dB_t \right) & \\
    &= \mathbb{E}\left( \left[
        \frac{\partial \phi(X_t)}{\partial t}
        - b(X_t, t) \frac{\partial \phi(X_t)}{\partial X_t}
        + \frac{\partial^2 \phi(X_t)}{\partial X_t^2}
     \right] dt \right) & \text{expectation of Brownian term is zero} \\
    &= \mathbb{E}\left( \left[
        \frac{\partial \phi(X_t)}{\partial t}
        - b(X_t, t) \frac{\partial \phi(X_t)}{\partial X_t}
        + \frac{\partial^2 \phi(X_t)}{\partial X_t^2}
     \right] \right) dt & \text{term $dt$ constant wrt. expectation}
\end{align}
$$

Dividing by $$dt$$ we therefore have:
$$
\begin{align}
    \mathbb{E} &= \mathbb{E}\left( \left[
        \frac{\partial \phi(X_t)}{\partial t}
        - b(X_t, t) \frac{\partial \phi(X_t)}{\partial X_t}
        + \frac{\partial^2 \phi(X_t)}{\partial X_t^2}
     \right] \right) dt & \text{term $dt$ constant wrt. expectation}
\end{align}
$$

-->

<!-- 
## Derivation of Fokker-Planck

You can see here for an accessible derivation of Fokker-Planck: [Appendix: Derivation of the Fokker-Planck Equation (UC Berkeley)](https://sites.me.ucsb.edu/~moehlis/moehlis_papers/appendix.pdf) -->

## Interpretation as mass conservation

<!--
https://math.stackexchange.com/questions/2292544/understanding-the-fokker-planck-equation-for-non-stationary-processes
https://en.wikipedia.org/wiki/Fokker%E2%80%93Planck_equation
-->

## Links to the Kolmogorov Forward/Backward Equations

# References

[1] Bogachev, Vladimir I., et al. Fokker–Planck–Kolmogorov Equations. Vol. 207. American Mathematical Society, 2022.

[2] Sharma, Shambhu N., and Hiren G. Patel. "The Fokker-Planck equation." Stochastic Control. Rijeka: IntechOpen, 2010. 1-20.

[3] [Ryzhik (2018)](https://math.stanford.edu/~ryzhik/STANFORD/MEAN-FIELD-GAMES/notes-mean-field.pdf)

[4] https://www.thphys.uni-heidelberg.de/~wolschin/statsem23_6.pdf

[5] https://xl0418.github.io/2018/10/24/2018-10-24-derivingFPequ/

[6] https://www.whoi.edu/cms/files/lecture07_21269.pdf