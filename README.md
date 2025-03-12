# Game Moderator Guide for Fire Drills
This Repository contains all you need to train a team on a production-like scale with real scenarios. The Fire Drills are played as a game and hence consist of three roles, the **Game Moderator**, **Game Council** and the **Players**.

The **Game Moderator(s)** orchestrate, execute and evaluate the Fire drills.

The **Game council** independent group of individuals representing the organizations Security and Engineering standards. They guard the scope of the game and support the **Game Moderator** in defining expected outcomes.

The **Players** are the individuals of one or more Teams that build and own a digital service (SaaS, PaaS or IaaS). 

## What are the Fire Drills?
The Fire drills are a set of reviewed Scenarios that are executed in the players Production-like environment. The Game Moderator observes the Scenarios and evaluates the players approach on how they solved them. The goal of Fire Drills is to measure and improve Player’s maturity in delivering digital services.

The GM aims to simulate real-world incidents and test the response and communication abilities of the Players, using a single chat tool such as Slack or MS Teams as the primary communication channel. 

A safe game environment is key – the drills are executed in an isolated blame-safe environment in which the GMs interact with the Players on behalf of the clients/users, Security Office and other Engineering teams and departments relevant to the Scenarios.

The GM(s) assess the Players in four phases for each Scenario: 
- Detect 
- Identify 
- Communicate
- Resolve  

## The Game
The Game is divided in 6 stages.
- Defining Service Level Ambitions
- Creating & Reviewing of the Fire Drill Plan
- Preparation
- Game Days
- Assessment
- Evaluate


### Defining Service Level Ambitions
*Roles involved: Game Moderator(s) and Players' Product Owner*

In the Game Moderator Excel Template there is a sheet called the "Service Level Ambition". This form has questions to the Product Owner that will be playing the Fire Drill Game. This form should help you to populate the "Scenarios" sheet to meet the expectations that the Players are expected to achieve.

### Creating & Reviewing of the Fire Drill Plan
*Roles involved: Game Moderator(s) and Game Council*

The Fire Drill Plan sheet should at this stage be filled out, it is time to review and determine the importance of each scenario. This should be done in consultation with the Game council. The Game Council is expected to comment and rate each Scenario. 

### Preparation
*Roles involved: Game Moderator(s)*

The games will be high paced for the Game Moderator, to prevent it from becoming overwhelming, the GMs must prepare the scenarios and the fire Drill Evaluation sheet. A few things are expected by the players:
- Their steps are recorded on day-to-day basis
- An End of day report is delivered with notes of each Scenario that was executed
- The GM is expected to answer appropriately to escalations to external parties, such as Security, Platform and as other Engineers
- The GM is expected to fire realistic load to mimic user activity on the Product's Environment.

To prepare for this, we must
- Configure a load testing tool (e.g., JMeter) to automatically simulate user load
- Acquire the required permissions to execute the scenarios
- Configure the Scripts to target the Fire Drill environment
- Prepare and test the execution of the scenarios
- Prepare your Evaluation form to quickly document day to day and scenario to scenario activity
- Learn the patterns of your external parties to meet the players expectations when they escalate
- Setup a private communication channel (e.g., Slack or Teams) for the gameplay and invite the Players.


### Game days
*Roles involved: Game Moderator(s) and the Players*

The GM will kick of the Fire drills by the distribution of an infographic. The Players are invited to the Slack channels and a Q&A is planned few days after the first day. During this Q&A the players can comment on the process and the GM and Players can adjust appropriately.

The GM must run load on the service continuously during the Fire Drill time. As you execute Scenarios make sure to monitor the players and the Environment to record their actions. During this GM should actively evaluate the actions to assemble the end report in a timely manner. Use the Fire Drill Evaluation Sheet to record this. This sheet should not be shared with anyone. 

At the end of the day the GM shares the End of day report in the Communication channel.

### Assessment
*Roles involved: Game Moderator(s)*

It is the end of the Fire drill and its finally time to fill wrap up with the Fire Drill Report! Use the word template and fill in the Questions that are in Red. 

You can Start with Chapter 3 where you copy and paste the End of Day reports. 

In Chapter 4 the GM explains the scoring of each Scenario and calculates the final grade for each phase. 

Chapter 5 gives the players and PO a nice summary of the observations of the Fire Drill. Let yourself be inspired by the daily reports and the score explanation of each Scenario.

Chapter 6 documents the follow ups and 7 has all the appendices of the Postmortems that were created during the Fire Drills.

Make sure to finally REDACT all names from the Report, the name of the GM can remain. Furthermore, distribution of the report should be limited to the stakeholders only. In order to re-use material over multiple teams’ confidentiality of the report is key.

### Evaluate
*Roles involved: Game Moderator(s), Council and the Players' Product Owner*

Although the report contains scores. these are on an arbitrary scale. The goal of the scores is to highlight the areas of improvement. They are not meant for Fail/Pass judgements. During the evaluation the GMs, Game Council and the product owners have prepared their point of attention and share them accordingly. Collectivly, follow-ups are agreed upon.

