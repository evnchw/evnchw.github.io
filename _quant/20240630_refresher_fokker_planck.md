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

## In a nutshell: the FP equation is a way to model the evolution of a probability density over time

From [Wikipedia](https://en.wikipedia.org/wiki/Fokker%E2%80%93Planck_equation):

> In statistical mechanics and information theory, the Fokker–Planck equation is a partial differential equation that describes the time evolution of the probability density function of the velocity of a particle under the influence of drag forces and random forces, as in Brownian motion. The equation can be generalized to other observables as well. The Fokker-Planck equation has multiple applications in information theory, graph theory, data science, finance, economics etc.

## The main result we want to show

From [3] but we present it in a more linear order, from the particular state dynamics to the final Fokker-Planck equation.

### Setup.

We have a $$d$$-dimensional vector of states $$X \in \mathbb{R}^d$$, and a continuous but finite timeline $$t \in [0, T]$$. Define a "drift" function $$b: \mathbb{R}^D \times [0, T] \to \mathbb{R}$$.

### State dynamics.

Now consider a particular stochastic differential equation (SDE) for the time evolution of $$X$$:

$$
\begin{align}
    d X_t &= \overbrace{-b (X_t, t) dt}^{\text{drift}} + \overbrace{\sqrt{2} dB_t}^{\text{diffusion}} & t \in [0, T] \hspace{0.5cm} \text{state evolution} \\
    X_0 &= \mathbb{Z}_0 & \text{initial state}
\end{align}
$$

### Probability density (transformation) over the states.

In the MFG world, we are interested in how the *distribution* of $$X$$ evolves over time. The idea is that we have many identical agents and so their distribution of states will evolve in the same way. Of course, this means we just want to use a density function of $$X$$, and so Fokker-Planck will tell us what the dynamics of this $$X$$-transformation will be.

<!--
TODO:
- define probability measure on complex unit circle (mathbb T)
- define the \Delta operator for m
-->
Define the density of $$X$$ as $$m \in L^1(\mathbb{T}^d \times [0,T])$$.

- Note that since this is a probability density over states, (at each time) it must sum up to 1 and so its domain is **not** based on $$\mathbb{R}^d$$ but rather restricted to the $$d$$-dimensional unit circle $$\mathbb{T}^d$$, consistent with functional analysis. (For example, if $$d=2$$, then we can select $$\{x, y \in [0,1]: x^2 + y^2 = 1\}$$.)
- The component $$L^1$$ means that $$m$$ is a member of the Lebesgue space $$L^1$$ ([StackExchange](https://math.stackexchange.com/questions/745894/what-does-it-mean-to-be-an-l1-function)): informally, the absolute value of $$m$$ is bounded everywhere.

### Evolution of the transformation.

We want to see how the above drift-diffusion system yields the Fokker-Planck equation:

$$
\begin{align}
    \frac{\partial m}{\partial t} - \Delta m - \text{div} (mb) &= 0 & \text{in } \mathbb{T}^d \times (0,T) & \hspace{0.5cm} \text{density evolution} \\
    m(0,x) &= m_0 (x) & \text{initial density}
\end{align}
$$

Our strategy will be to apply Ito's formula ([see my post on HJB](https://evnchw.github.io/quant/20240623_refresher_hjb)) to obtain the dynamics of this transformation.

## Derivation of Fokker-Planck

Here we restate Ito's lemma for our particular context [(Wikipedia)](https://en.wikipedia.org/wiki/It%C3%B4%27s_lemma).

<p style="text-align: center; font-weight: bold; font-family: Serif">Itô's lemma</p>

Let $$X_t$$ evolve over time according to the state dynamics:

$$
\begin{align}
    d X_t &= a(t) dt + b(t) dB_t & \text{state evolution} \\
    X_0 &= X \\
\end{align}
$$

## Links to the Kolmogorov Forward/Backward Equations

# References

[1] Bogachev, Vladimir I., et al. Fokker–Planck–Kolmogorov Equations. Vol. 207. American Mathematical Society, 2022.

[2] Sharma, Shambhu N., and Hiren G. Patel. "The Fokker-Planck equation." Stochastic Control. Rijeka: IntechOpen, 2010. 1-20.

[3] [Ryzhik (2018)](https://math.stanford.edu/~ryzhik/STANFORD/MEAN-FIELD-GAMES/notes-mean-field.pdf)

