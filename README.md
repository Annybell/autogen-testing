# Autogen Test

# Overview

Tested the new Microsoft Multiagent functionality Autogen, in which multiple LLMs can talk and solve a problem autonomously with or without human intervention. This could be useful to create a virtual "company" like ChatDev giving different agents different roles like CEO, CTO, programmer, tester, designer. The initial tests suggests that right now using GPT4 to run this experiment autonomusly is expensive, costing about 3$ to run a few basic stock prompts, given that sometimes it couldn't find the right tickers. Also the program sometimes crashed. 

https://microsoft.github.io/autogen/

# Thoughts

- It is better to run it with human intervention to save money and guide the AI better, but then it is not that much different than using chatgpt on the general UX
- For some reason using GPT3 didnt work from within the configuration file, it always seemed to use GPT4 which is quite expensive from the API level
- This could be use to have a little virtual company in the future, bearing in mind that the answers that the LLMs generate to solve the same problem might be different sometimes, human oversight is needed

# Tools
- Gitpod seems easier to use from a git push perspective than github codespaces
  
# Demo Video
https://github.com/Annybell/autogen-testing/assets/22093818/37278741-c22b-4ae1-a038-7e829f202614


