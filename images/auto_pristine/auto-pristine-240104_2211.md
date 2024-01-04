# Auto Pristine

**Start Message**

**Player picks car**

**Zenith Nomad (Off Roader)**

- Speed 4
- Durability 8
- Handling 8

**Nebula Mirage (Speedster)**

- Speed 9
- Durability 3
- Handling 8

**Intro Message -** Welcome to AUTO PRISTINE, a cyberpunk racing dystopia for the elite. Customize your ride, choose surreal tracks, and let bizarre driving styles unfold. Victory is pursued from the detached luxury of the uber-rich, who neither get in the car nor bother to watch it race.

**Player picks one of 3 cars**

1. **Speedster:**Speed: 9

Durability: 3

Handling: 8



2. **Muscle Car:**Speed: 6

Durability: 7

Handling: 6



3. **Off-Roader:**Speed: 4

Durability: 8

Handling: 8

**Player Picks a track** 

_Neon Boulevard Circuit: Street Race_

- **Surface Type:** Smooth
- **Durability Challenge:** Low
- **Track Complexity:** Challenging Circuit
- **Speed Challenge:** High
- **Environmental Conditions:** Rain
- **Handling Challenge:** Moderate

_Cyberpunk Junkyard Rally: Urban Off-Road_

- **Surface Type:** Uneven Terrain
- **Durability Challenge:** High
- **Track Complexity:** Dynamic Layout
- **Speed Challenge:** Moderate
- **Environmental Conditions:** Dusty
- **Handling Challenge:** Moderate

### _Virtual Reality Skyline Challenge: Futuristic Hologram Race_

- **Surface Type:** Floating Holographic Platforms
- **Durability Challenge:** Moderate
- **Track Complexity:** Intricate Maze
- **Speed Challenge:** Very High
- **Environmental Conditions:** Digital Rain
- **Handling Challenge:** Very High

### _Megacity Expressway: High-Speed Commute_

- **Surface Type:** Highways with Straight Stretches
- **Durability Challenge:** Low
- **Track Complexity:** Straightforward
- **Speed Challenge:** Very High
- **Environmental Conditions:** Normal
- **Handling Challenge:** Low

### _Underground Tech Tunnels: Tech Haven_

- **Surface Type:** High-tech Tunnels
- **Durability Challenge:** Moderate
- **Track Complexity:** Tactical Path
- **Speed Challenge:** High
- **Environmental Conditions:** Artificial Light Grid
- **Handling Challenge:** High

Ideally this is built around an LLM or the random module to create new tracks everytime or at least a random choice of 3 from a catalogue of 10+ maps

**Player Chooses Racing Styles**

4. **Aggressive Racing:Effect on Speed:** High + 1 to 3

**Effect on Durability:** Low - 1 to 3

**Effect on Handling:** High + 1 to 3

**Description:** The Aggressive Racing style is all about pushing the car to its limits. Drivers opting for this style prioritize speed and maneuverability, willing to take risks even if it means sacrificing some durability.



5. **Defensive Cruising:Effect on Speed:** Low

**Effect on Durability:** High

**Effect on Handling:** Moderate

**Description:** Defensive Cruising focuses on cautious and defensive driving. Drivers adopting this style prioritize durability over speed, aiming to navigate through challenges with a focus on maintaining the integrity of their vehicle.



6. **Precision Tech Driving:Effect on Speed:** Moderate

**Effect on Durability:** Moderate

**Effect on Handling:** Very High

**Description:** Precision Tech Driving emphasizes exact and calculated movements. Drivers following this style aim for optimal handling and control, making precise maneuvers to navigate complex tracks without compromising too much on speed or durability.



5 - 9 other cars are generated that are 1 of the 3 car choices from the start they are also allocated random racing styles

- If too many aggressive racers are chosen then perhaps a mass collision happens
- Too many tech drivers - cross synapses, and everyones driving styles are randomised
- Too many defensive drivers - the race is seriously uncool you might still win but at what cost? (no change apart from the win and lose message is different)

Race Begins!

Lose State

Looks like you shmucked out, kid. In this unforgiving city, defeat is just another curve in the track. But remember, only the resilient thrive in AUTO PRISTINE. Dust off, recalibrate, and dare to reclaim your position among the best. The city awaits your comeback.

Win State

Your victory echoes through the city, but in AUTO PRISTINE, staying at the top doesn't last long and requires relentless determination. Will you continue to dominate and leave a lasting mark among the elite?

**Obsidian Regalia (Muscle Car)**

- Speed 6
- Durability 7
- Handling 6

**Player chooses AI**

**Aggressive Racing:**

- **Effect on Speed:** High
- **Effect on Durability:** Low
- **Effect on Handling:** High
- **Description:** The Aggressive Racing style is all about pushing the car to its limits. Autopilots opting for this style prioritise speed and maneuverability, willing to take risks even if it means sacrificing some durability.

**Defensive Cruising:**

- **Effect on Speed:** Low
- **Effect on Durability:** High
- **Effect on Handling:** Moderate
- **Description:** Defensive Cruising focuses on cautious and defensive driving. Autopilots adopting this style prioritise durability over speed, aiming to navigate through challenges with a focus on maintaining the integrity of their vehicle.

**Precision Tech Driving:**

- **Effect on Speed:** Moderate
- **Effect on Durability:** Moderate
- **Effect on Handling:** Very High

- **Description:** Precision Tech Driving emphasizes exact and calculated movements. Autopilots following this style aim for optimal handling and control, making precise maneuvers to navigate complex tracks without compromising too much on speed or durability.

**Player picks a track to race on**

### Neon Boulevard Circuit: Street Race

- **Surface Type:** Smooth
- **Durability Demand:** Low
- **Track Complexity:** Challenging Circuit
- **Speed Demand:** High
- **Environmental Conditions:** Rain
- **Handling Demand:** Moderate

### Cyberpunk Junkyard Rally: Urban Off-Road

- **Surface Type:** Uneven Terrain
- **Durability Demand:** High
- **Track Complexity:** Dynamic Layout
- **Speed Demand:** Moderate
- **Environmental Conditions:** Dusty
- **Handling Demand:** Moderate

### Virtual Reality Skyline Challenge: Futuristic Hologram Race

- **Surface Type:** Floating Holographic Platforms
- **Durability Demand:** Moderate
- **Track Complexity:** Intricate Maze
- **Speed Demand:** Very High
- **Environmental Conditions:** Digital Rain
- **Handling Demand:** Very High

### Megacity Expressway: High-Speed Commute

- **Surface Type:** Highways with Straight Stretches
- **Durability Demand:** Low
- **Track Complexity:** Straightforward
- **Speed Demand:** Very High
- **Environmental Conditions:** Normal
- **Handling Demand:** Low

### Underground Tech Tunnels: Tech Haven

- **Surface Type:** High-tech Tunnels
- **Durability Demand:** Moderate
- **Track Complexity:** Tactical Path
- **Speed Demand:** High
- **Environmental Conditions:** Artificial Light Grid
- **Handling Demand:** High

for the sake of codability these choices change the base stats of the car chosen with some randomisation.

- maybe an average of scores against eachother to determine the winner?

Tracks should be randomly generated if possible using llm to come up with name/list of possible naming conventions and random module to choose track variables 

- will assign value ranges to each of the surfaces/complexities/environments and their effect on corresponding car stats
- maybe stats come first then llm creates name on likely possible environments IE rough terrain is likely in the badlands rather than the city
- _currently working with a list of like 12 tracks and random.choice'ing' them_

Randomly generate 5-9 other vehicles and driving styles that will try to out perform you 

- These other cars must be similarly capped in someway, ie speed high/durability low or average all rounder etc
- numpy or tf for proababilities _(currently using random module lol)_

I want there to always be some risk involved, 

- If too many aggressive racers are chosen then perhaps a mass collision happens
- Too many tech drivers - cross synapses, and everyones driving styles change 
- Too many defensive drivers - the race is seriously uncool you might still win but at what cost? (no effect on stats) just disappointing win or lose state)
- **this can be determined by numpy hopefullyyyy**

Game will be primarily built on python ergo no visuals whatsoever

- perhaps some images or gifs of luxury surrounding
- sounds of cars in the background?

## _**Welcome to AUTO PRISTINE, a cyberpunk racing dystopia for the elite. Customize your ride, choose surreal tracks, and let bizarre driving styles unfold. Victory is pursued from the detached luxury of the uber-rich, who neither get in the car nor bother to watch it race.**_

**Race Starts!**

Based on the base stats, and driving style the cars will perform differently

Lose State

Looks like you shmucked out, kid. In this unforgiving city, defeat is just another curve in the track. But remember, only the resilient thrive in AUTO PRISTINE. Dust off, recalibrate, and dare to reclaim your position among the best. The city awaits your comeback.

Win State

Congratulations on emerging victorious! In this city, cred only lasts so long. Dare to go again and assert your dominance among the elite? The pursuit of victory is relentless, and only the resilient thrive in the ever-shifting landscape of AUTO PRISTINE.



these things can change the win or lose state? 

- so we have 8 outcomes 
- win/lose
- mass collision win/lose
- tech win/lose
- boring win/lose