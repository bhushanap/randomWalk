<img src='https://github.com/bhushanap/randomWalk/assets/83635464/3a432ddd-3250-497c-83cf-4c24fd08d33d' height='400'>

# Random Walk Simulation

This is an attempt to gain more insights into what strategy can be effective at generating more profits in the stock market.
Financial markets can be simulated by a normally distributed [random walk](https://en.wikipedia.org/wiki/Random_walk).
Intuitively one expects a random walk to be a zero sum game. A simple random walk can be thought of as flipping a coin at every step and either moving up or down by 1 based on if it lands on heads or tails.

Let's denote the probability of reaching 101 by a given time step k be P_k(101) and 99 be P_k(99)

### Take a simplistic scenario: We start from 100.

Would P_k(101) be the same as P_99(k)? 
In a simple random walk, yes.

But if it were a Gaussian random walk with standard deviation proportional to the current position, then one would expect that the probability of making your wealth 101/100 times should be the same as making it 100/101 times. Only then can we say it is a zero sum game.
So the probability of reaching 99 would be slightly less than reaching 101/100.

Infact as it turns out P_k(101) is roughly the same as the probability of reaching P_k(99.0099...) so for practical purposes we can say P_k(101) ~ P_k(99)

### How about 110?
The probability of reaching 110 would be the same as the probability of reaching 100/110 = 90.9090... and not 90. P_k(110) = P_k(99.0909...) But still roughly the same as P_k(99)
It should be noted here that we have kept steps same as k in both the cases.

### Can we state P_10k(110) = P_k(100.957...) ^ 10 ~ P_k(101) ~ P_k(99)?
Since 110 = 100 * 1.00957... ^ 10, one would think that mulyiplying the probabilities for each time step should give the net value after 10 time steps.
So the net probability P_10k(110) ~ P_k(99) ^ 10.

In simple words, if we set a target profit of 110 and a stop loss of 99, or in other words a Reward Risk Ratio of 10:1, then the odds of winning would be 1:10. Intuitively, this feels right if we think of this as a zero sum game.
But in reality, one cannot multiply probabilities like that. What we are multiplying are normal distributions. In this particular step we need to multiply/integrate 10 normal distributions in order to arrive at the distribution at the 10th step.

Although this feels counterintuitive, it can be shown via simulation that the odds of reaching 110 although lesser than the odds of reaching 99 are much higher than 1:10. Infact, if we multiply these odds with the gains and losses, we can obtain a net profit value.

<img src='https://github.com/bhushanap/randomWalk/assets/83635464/fb82d7fe-ded0-4b57-9b14-1618ef2ffaf3' height='400'>

This is how the returns look like for various Reward Risk Ratios.

![image](https://github.com/bhushanap/randomWalk/assets/83635464/3eaaf070-9e5a-4229-b68a-c24424f373cb)

As can be clearly seen if we start increasing both reward targets and risk stoploss, the results are less likely to conclude within a simulation of 20 time steps. So in such cases we just take whatever the position is at the end of all time steps.
Even then we can clearly see a pattern that having a higher Reward:Risk ratio makes the most profits in the long term. We can reduce the inconclusive results by increasing the standard deviation of our simulation or by increasing the time steps.

![image](https://github.com/bhushanap/randomWalk/assets/83635464/4407b186-901c-4ef0-b1fc-3f950c998c1d)

This time it's even more clearer. Even though our win rate is lower, the net returns are much higher when we use a higher RRR. ;)
