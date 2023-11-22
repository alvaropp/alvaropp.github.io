---
layout: page
date: 2018-05-10
title: Decentralised Voting System
description: on blockchain
brief: An experiment about using blockchain for decentralised voting using the Ethereum. In more detail, white-listed users can vote for one of the candidates using a web app, and a smart contract keeps track of the votes. This was built as part of a one-day <a href="https://www.aic.ecs.soton.ac.uk/" target="_blank">AIC</a> hackathon with several colleagues. 
img: https://user-images.githubusercontent.com/4785303/40201649-91fca2aa-5a17-11e8-84aa-253056b4b917.png
skills: Python, blockchain, Ethereum, Solidity, HTML, js.
how-to: code available on <a href="https://github.com/dorotafilipczuk/blockchain-voting-system" target="_blank">GitHub</a>.
big_img: https://user-images.githubusercontent.com/4785303/40201815-192cff04-5a18-11e8-8fa8-53e81c4631ca.png
---

Blockchain has introduced a new ecosystem of decentralised and transparent applications, running without a central authority and providing high guarantees against tampering. During a one-day hackathon at the University of Southampton, we decided to implement a stereotypical example in order to learn more about blockchain: a voting application implemented in [Ethereum](https://www.ethereum.org/){:target="_ blank"}.

The proposed framework consists of three components:
- A private Ethereum test blockchain running on [Ganache](https://github.com/trufflesuite/ganache){:target="_ blank"}.
- A smart contract taking care of voter identity and vote counts, implemented using [Solidity](https://solidity.readthedocs.io/en/v0.4.24/){:target="_ blank"}. It *heavily* borrows from an example in the Solidity docs, but it has a couple more features: a white-list of of voters and max one vote per voter.
- A web app where voters can type their public address, cast their vote and see real-time vote counts.

For the demo, the idea was to give people print outs with a public address of the blockchain, which they could then use to login in the web app and cast their vote. Of course, this project was quick, exploratory work. The resulting web app and smart contract are not safe for real use, but work fine for illustrative purposes.

<div class="img_single">
    <img class="col three" src="https://user-images.githubusercontent.com/4785303/40201943-76e3ca9c-5a18-11e8-9f1c-177af60c4726.png"/>
</div>

<hr>

![](https://img.shields.io/badge/License-MIT-yellow.svg)
