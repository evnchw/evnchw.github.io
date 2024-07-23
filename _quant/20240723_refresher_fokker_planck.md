---
title: "[under construction] Quick refresher on Fokker-Planck (drift-diffusion)"
collection: quant
type: "Post"
permalink: /quant/20240723_refresher_fokker_planck
date: 2024-07-23
---

These are my quick refresher notes on Fokker-Planck (forward Kolmogorov) for the evolution of a probability density over time. Like my notes on [Hamilton-Jacobi-Bellman](https://evnchw.github.io/quant/20240623_refresher_hjb), I focus on the main analytical aspects and intuitive understanding rather than the detailed proofs. I follow a similar format as well.

**Disclaimers**:

- I prioritize intuition/readability linking to references where appropriate.
- We will focus on the key equations, not go too deeply into proofs and may skip some parts for brevity.
- There may be imprecisions: all feedback and corrections are welcome.
- Long equations may not show up on mobile.

There are various ways to look at Fokker-Planck (Bogachev 2022; Sharma 2010), but we are going to work through the view sketched briefly in the Achdou/Cardialiguet intro notes on mean field games ("MFG") (Achdou et al. 2020, "1.3.1 Heuristic derivation of the MFG system"), and reviewed also in (Ryzhik 2018). This is a core ingredient of a standard MFG formulation, namely specifying how the distribution of many agents evolves over time, and so it is important to understand this result with some depth.

Specifically:

1. We take a look at the (standard) drift-diffusion dynamics of the underlying states.
2. We derive its forward Fokker-Planck equation that specifies how its probability distribution evolves over tiem.
3. We tie this back to the MFG formulation in the Achdou/Cardialiguet notes.

For (1-2), the Fokker-Planck derivation primarily summarizes general notes on Fokker-Planck (Orlandini 2024; Wolschin 2024; Liang 2024; Brown 2024; Frouah 2024). The main contribution here is to formulate the derivation for the MFG formulation, and also gather/fill in treatments of boundary conditions & time/space integrals in a single place.

## In a nutshell: the FP equation provides a way to model the evolution of a probability density over time

From [Wikipedia](https://en.wikipedia.org/wiki/Fokker%E2%80%93Planck_equation):

> In statistical mechanics and information theory, the Fokker–Planck equation is a partial differential equation that describes the time evolution of the probability density function of the velocity of a particle under the influence of drag forces and random forces, as in Brownian motion. The equation can be generalized to other observables as well. The Fokker-Planck equation has multiple applications in information theory, graph theory, data science, finance, economics etc.

This is also called the forward Kolmogorov equation.

## The main result we want to show

### Setup and state dynamics

We have a $$d$$-dimensional vector of states $$X \in \mathbb{R}^d$$, and a continuous but finite timeline $$t \in [0, T]$$. Define a "drift" function $$b: \mathbb{R}^D \times [0, T] \to \mathbb{R}$$ which is Hölder-continuous in space and continuous in time. The states $$X$$ evolve over time according to the stochastic differential equation (SDE):

$$
\begin{align}
    d X_t &= \mu(X_t, t) dt + \sigma(X_t, t) dB_t & t \in [0, T] \hspace{0.5cm} \text{state evolution} \\
    X_0 &= Z_0 & \text{initial state}
\end{align}
$$

### Our goal: dynamics of the probability density over the states.

In the MFG world, we are interested in how the *distribution* of $$X$$ evolves over time, as to model the crowd behavior of many (identical) agents. Since $$X$$ evolves stochastically (via the Brownian), we need to focus on the probability density of $$X$$. This is just a transformation of $$X$$, which motivates using Ito's Lemma to model its dynamics, and with more analysis, ultimately the Fokker-Planck forward equation.

Specifically we want to see how the above drift-diffusion system satisfies the Fokker-Planck forward equation:

$$
\begin{align}
    \frac{\partial m}{\partial t} - \Delta m - \text{div} (mb) &= 0 & \text{in } \mathbb{R}^d \times (0,T) & \hspace{0.5cm} \text{density evolution} \\
    m(x,0) &= m_0 (x) & \text{initial density}
\end{align}
$$

for some vector field $$b: \mathbb{R}^d \times [0, T] \to \mathbb{R}$$.

We introduce here the probability density of $$d-$$dimensional $$X$$ at time $$t$$ as $$m: \mathbb{R}^d \times [0,T] \to \mathbb{R}$$.

- $$m$$ (and all its derivatives) is a **scalar field**: this means at any point $$(X,t)$$ this assigns a scalar value.
- This density is a member of the Lebesgue space $$L^1$$ ([StackExchange](https://math.stackexchange.com/questions/745894/what-does-it-mean-to-be-an-l1-function)). Informally, the absolute value of $$m$$ is bounded everywhere.
- We assume that the probability density vanishes at the boundaries so that $$m^c(\pm\infty)=0$$ for all orders of differentiation $c$. This additional regularity condition corresponds to the "natural boundary" condition referenced in (Orlandin 2024).

<!-- Note that $$\Delta m$$ is the [Laplace operator](https://en.wikipedia.org/wiki/Laplace_operator): $$\Delta m = \frac{\partial^2 m}{\partial x^2}$$. -->
<!--
(Moreover, $$D\phi$$ indicates the vector of first $$X$$-derivatives, and similarly $$\Delta \phi$$ is the [Laplace operator](https://en.wikipedia.org/wiki/Laplace_operator) and indicates the second derivatives.)
-->

## From the state dynamics to Fokker-Planck

Introduce a [smooth](https://en.wikipedia.org/wiki/Smoothness) arbitrary test function $$\phi: \mathbb{R}^d \times (0, T) \to \mathbb{R}$$, with boundary conditions $$\phi(X,T)=\phi(X,0)=0$$. (We assume scalar-valued for simplicity.) We obtain the dynamics of $$\phi(x,t)$$ via Ito's lemma:

$$
\begin{align}
    d \phi(X_t, t) &= \left[
        \frac{\partial \phi(X_t, t)}{\partial t} + \mu \frac{\partial \phi(X_t, t)}{\partial X_t} +
        \frac{1}{2} \sigma^2 \frac{\partial^2 \phi(X_t, t)}{\partial X_t^2}
    \right] dt + \left[
        \sigma \frac{\partial \phi(X_t, t)}{\partial X_t}
    \right] dB_t
\end{align}
$$

This yields the Ito integral:

$$
\begin{align}
    \phi(X_T, T) &= \phi(Z_0, 0) +
        \int_0^t \left[
            \frac{\partial \phi(X_s, s)}{\partial s} + \mu \frac{\partial \phi(X_s, )}{\partial X_s} +
            \frac{1}{2} \sigma^2 \frac{\partial^2 \phi(X_s, s)}{\partial X_s^2}
        \right] ds +
        \int_0^t \left[
        \sigma \frac{\partial \phi(X_t, t)}{\partial X_t}
        \right] dB_s
\end{align}
$$

Now, take the expectation wrt. $$X$$ on both sides, and removing the Brownian integral which has [expectation zero](https://math.stackexchange.com/a/2392039):

$$
\begin{align}
    \mathbb{E}[\phi(X_T, T)] &= \mathbb{E}[\phi(Z_0, 0)] +
        \mathbb{E}\left(
            \int_0^T \left[
                \frac{\partial \phi(X_s, s)}{\partial s} + \mu \frac{\partial \phi(X_s, s)}{\partial X_s} +
                \frac{1}{2} \sigma^2 \frac{\partial^2 \phi(X_s, s)}{\partial X_s^2}
            \right] ds
        \right)
\end{align}
$$

Expand the expectation terms to reveal the probability density of $$X$$:

$$
\begin{align}
    \underbrace{\int_{\mathbb{R}^d} \phi(X, T) m(X, T) dX}_{\text{terminal integral}} &=
        \underbrace{\int_{\mathbb{R}^d} \phi(Z_0, 0) m(X, 0) dX}_{\text{initial integral}}
        +
        \underbrace{
            \int_{\mathbb{R}^d} 
                \int_0^T \left[
                    \frac{\partial \phi(X_s, s)}{\partial s} + \mu \frac{\partial \phi(X_s, s)}{\partial X_s} +
                    \frac{1}{2} \sigma^2 \frac{\partial^2 \phi(X_s, s)}{\partial X_s^2}
                \right]
            m(X_s, s) dX ds
        }_{\text{running integral}}
\end{align}
$$

Of course, at the boundaries $$\phi(X,T)=\phi(X,0)=0$$, so both the terminal and initial integral are zero:

$$
\begin{align}
    0 &= \underbrace{
            \int_{\mathbb{R}^d} 
                \int_0^T \left[
                    \frac{\partial \phi(X_s, s)}{\partial s} + \mu \frac{\partial \phi(X_s, s)}{\partial X_s} +
                    \frac{1}{2} \sigma^2 \frac{\partial^2 \phi(X_s, s)}{\partial X_s^2}
                \right]
            m(X_s, s) dX ds
        }_{\text{running integral}}
\end{align}
$$

Hence we have an expression for the dynamics of the probability density $$m(X_t, t)$$ for any time $$t \in (0,T)$$. To evaluate the running integral, split up the sum into three smaller integrals, which we will handle separately. Our goal is to move the derivatives of $$\phi$$ onto $$m$$ so we can obtain its dynamics and therefore the Fokker-Planck equation. (For brevity we omit the parameters for $$m, \phi$$, and also write $$X$$ instead of $$X_s$$ since $$s$$ is given below.)

$$
\begin{align}
    \int_{\mathbb{R}^d} 
                    \int_0^T &\left[
                        \frac{\partial \phi(X_s, s)}{\partial s} + \mu \frac{\partial \phi(X_s, s)}{\partial X_s} +
                        \frac{1}{2} \sigma^2 \frac{\partial^2 \phi(X_s, s)}{\partial X_s^2}
                    \right] m(X_s, s) dX ds
        = \\
        & \underbrace{
            \int_{\mathbb{R}^d} \int_0^T m \frac{\partial \phi}{\partial s} ds dX
        }_{\text{Integral }1} +
          \underbrace{
            \int_{\mathbb{R}^d} \int_0^T m \mu \frac{\partial \phi}{\partial X} ds dX
        }_{\text{Integral }2} +
          \underbrace{
            \frac{1}{2}
            \int_{\mathbb{R}^d} \int_0^T m \sigma^2 \frac{\partial^2 \phi}{\partial X^2} ds dX
        }_{\text{Integral }3}
\end{align}
$$

where $$m, \phi, \mu, \sigma$$ are all functions of $$(X_s, s)$$. To take the integrals, we will use integration by parts and also our boundary conditions for $$\phi, m$$.

$$
\begin{align}
    \int_a^b u(x) v'(x) dx &= u(b) v(b) - u(a) v(a) - \int_a^b u'(x) v(x) dx &\text{integration by parts}
\end{align}
$$

Integral 1, with $$u=m, v'=\frac{\partial \phi}{\partial s}$$:

$$
\begin{align}
    \int_{\mathbb{R}^d} \int_0^T m \frac{\partial \phi}{\partial s} ds dX &= \int_{\mathbb{R}^d} \left[
        m\phi |^T_0 - \int_0^T \frac{\partial m}{\partial s} \phi ds
    \right] dX = - \int_{\mathbb{R}^d} \int_0^T \frac{\partial m}{\partial s} \phi ds dX
\end{align}
$$

Integral 2, with $$u=m\mu, v'=\frac{\partial \phi}{\partial X}$$ and recalling $$m(\pm \infty)=0$$.

$$
\begin{align}
    \int_{\mathbb{R}^d} \int_0^T m \mu \frac{\partial \phi}{\partial X} ds dX &=
    \int_0^T \int_{\mathbb{R}^d} m \mu \frac{\partial \phi}{\partial X} dX ds & \text{switch integration limits} \\
    &= \int_0^T \left[
        (m \mu) \phi |_{\mathbb{R}^d} - \int_{\mathbb{R}^d} \frac{\partial (m \mu)}{\partial X} \phi dX
    \right] ds & \text{integration by parts} \\
    &= - \int_0^T \int_{\mathbb{R}^d} \frac{\partial (m \mu)}{\partial X} \phi dX ds & \text{apply boundaries } m^c(\pm\infty)=0 \\
    &= - \int_{\mathbb{R}^d} \int_0^T \frac{\partial (m \mu)}{\partial X} \phi ds dX & \text{switch integration limits}
\end{align}
$$

Integral 3, where we will have to apply integration by parts twice so we get $$\frac{\partial^2 \phi}{\partial X^2} \to \frac{\partial \phi}{\partial X} \to \phi$$ to yield its dynamics.

$$
\begin{align}
    \frac{1}{2} \int_{\mathbb{R}^d} \int_0^T m \sigma^2 \frac{\partial^2 \phi}{\partial X^2} ds dX &=
        \frac{1}{2} \int_0^T \int_{\mathbb{R}^d} m \sigma^2 \frac{\partial^2 \phi}{\partial X^2} dX ds & \text{switch integration limits} \\
        &= \frac{1}{2} \int_0^T \left[
                m \sigma^2 \frac{\partial \phi}{\partial X} |_{\mathbb{R}^d}
                -
                \int_{\mathbb{R}^d} \frac{\partial (m \sigma^2)}{\partial X} \frac{\partial \phi}{\partial X} dX
            \right] ds & \text{by parts, } u=m\sigma^2 \text{ and } v'=\frac{\partial^2 \phi}{\partial X^2} \\
        &= \frac{1}{2} \int_0^T \left[
                - \int_{\mathbb{R}^d} \frac{\partial (m \sigma^2)}{\partial X} \frac{\partial \phi}{\partial X} dX
            \right] ds & \text{apply boundaries } m^c(\pm\infty)=0 \\
        &= \frac{1}{2} \int_0^T \left[
                -\frac{\partial (m\sigma^2)}{\partial X} \phi |_{\mathbb{R}^d}
                +
                \int_{\mathbb{R}^d} \frac{\partial^2 (m\sigma^2)}{\partial X^2} \phi dX
            \right] ds & \text{by parts, } u=\frac{\partial (m\sigma^2)}{\partial X} \text{ and } v'=\frac{\partial \phi}{\partial X} \\
        &= \frac{1}{2} \int_0^T \left[
                -\left(
                    \frac{\partial m}{\partial X} \sigma^2 + m \frac{\partial \sigma^2}{\partial X}
                \right)\phi|_{\mathbb{R}^d}
                +
                \int_{\mathbb{R}^d} \frac{\partial^2 (m\sigma^2)}{\partial X^2} \phi dX
            \right] ds & \text{product rule} \\
        &= \frac{1}{2} \int_0^T
                \int_{\mathbb{R}^d} \frac{\partial^2 (m\sigma^2)}{\partial X^2} \phi dX
            ds & \text{apply boundaries } m^c(\pm\infty)=0
\end{align}
$$

Putting it all together, we obtain the expression:

$$
\begin{align}
    0 = \underbrace{- \int_{\mathbb{R}^d} \int_0^T \frac{\partial m}{\partial s} \phi ds dX}_{\text{Integral 1}} +
        \underbrace{- \int_{\mathbb{R}^d} \int_0^T \frac{\partial (m \mu)}{\partial X} \phi ds dX}_{\text{Integral 2}} +
        \underbrace{\frac{1}{2} \int_0^T
                \int_{\mathbb{R}^d} \frac{\partial^2 (m\sigma^2)}{\partial X^2} \phi dX
            ds}_{\text{Integral 3}} \\
    0 = \int_{\mathbb{R}^d} \int_0^T \phi \left[
        - \frac{\partial m}{\partial s}
        - \frac{\partial (m \mu)}{\partial X} +
        \frac{1}{2} \frac{\partial^2 (m\sigma^2)}{\partial X^2}
    \right] dX ds
\end{align}
$$

Since we have specifed any arbitrary $$\phi$$, this implies the rest of the integrand must be zero. Rearranging and adding back notation we obtain for any time $$t$$:

$$
\begin{align}
    \frac{\partial m}{\partial t} &= - \frac{\partial (m \mu)}{\partial X} + \frac{1}{2} \frac{\partial^2 (m\sigma^2)}{\partial X^2} & \text{Fokker-Planck} \\
    \frac{\partial m(X_t, t)}{\partial t} &= - \frac{\partial (m(X_t, t) \mu(X_t, t))}{\partial X_t} +
        \frac{1}{2} \frac{\partial^2 (m(X_t, t)\sigma(X_t, t)^2)}{\partial X_t^2} & \text{parametrized}
\end{align}
$$

This is the Fokker-Planck (forward Kolmogorov) equation, specifying the dynamics of $$X$$'s probability density $$m(X, t)$$ over $$t \in (0, T)$$. Briefly, this says that the probability density of $$X$$ evolves stochastically, negatively wrt. $$X$$'s drift and positively wrt. $$X$$'s diffusion. It is important to take a moment to examine each term and importantly its dimensions.

- $$\frac{\partial m(X_t, t)}{\partial t}$$ is a **scalar field**. This means 

Lastly, we need to tie this back to the mean field game notation in the Achdou/Cardaliguet notes (Achdou et al. 2020).

<!--
https://math.stackexchange.com/questions/2292544/understanding-the-fokker-planck-equation-for-non-stationary-processes
https://en.wikipedia.org/wiki/Fokker%E2%80%93Planck_equation
-->

# References

[1] Bogachev, Vladimir I., et al. Fokker–Planck–Kolmogorov Equations. Vol. 207. American Mathematical Society, 2022.

[2] Sharma, Shambhu N., and Hiren G. Patel. "The Fokker-Planck equation." Stochastic Control. Rijeka: IntechOpen, 2010. 1-20.

[3] Achdou, Yves, et al. "An introduction to mean field game theory." Mean Field Games: Cetraro, Italy 2019 (2020): 1-158.

[4] Ryzhik, Lenya. Notes on Mean Field Games. Stanford University, https://math.stanford.edu/~ryzhik/STANFORD/MEAN-FIELD-GAMES/notes-mean-field.pdf. Accessed 23 July 2024.

[5] Orlandini, Gianni. "Notes of the course in Statistical Mechanics." University of Padova, https://userswww.pd.infn.it/~orlandin/fisica_sis_comp/fokker_planck.pdf. Accessed 23 July 2024.

[6] Wolschin, Georg. Statistical Mechanics and Stochastic Processes. University of Heidelberg, https://www.thphys.uni-heidelberg.de/~wolschin/statsem23_6.pdf. Accessed 23 July 2024.

[7] Liang, Xiaolong. "Deriving the Fokker-Planck Equation." Xiaolong Liang's Blog, 24 Oct. 2018, https://xl0418.github.io/2018/10/24/2018-10-24-derivingFPequ/. Accessed 23 July 2024.

[8] Brown, Kevin. Lecture Notes on the Fokker-Planck Equation. Woods Hole Oceanographic Institution, https://www.whoi.edu/cms/files/lecture07_21269.pdf. Accessed 23 July 2024.

[9] Frouah, Rachid. "Derivation of the Fokker-Planck Equation." Finance Notes, https://www.frouah.com/finance%20notes/Derivation%20of%20the%20Fokker-Planck%20equation.pdf. Accessed 23 July 2024.
