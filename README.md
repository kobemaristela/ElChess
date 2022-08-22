# ElChess

___A world filled with magic and creatures beyond your wildest imagination___

You must embark on a journey to cross all six realms. Each realm has a relic chess piece that governs the land. You must defeat monsters and the realm boss to gain the relic piece. Each chess piece acquired gives you power to control the corresponding chess piece on the world board. All pieces must be gathered to challenge the God of Elchess and become the Grandmaster of the World. 

---------

[_Progress Overview_](https://docs.google.com/presentation/d/1_W84oneH_hCo1ZpfxYTXvR2kcTZxyzj29MZaU5xUayI/edit?usp=sharing) | [_Technical Design Document_](https://docs.google.com/document/d/1WySE5AJgGUELTtmZoP7sx3xJvzS245AY7lwgcv_Rrt0/edit?usp=sharin)

[_Final Presentation_](https://docs.google.com/presentation/d/1lsZgmz72L6cZa9fiWMthpchZmsisM7wh4t5uLwRueKQ/edit?usp=sharing)
--------
## Features
* Chess Puzzle Simulator  - Solve chess puzzles to battle against randomly encountered enemies and bosses. Utilize the Stockfish chess engine to set AI difficulty and chess settings.
    * Solve 1 chess puzzle equates to dealing 1 damage against an enemy.
    * Take 1 damage when failing a chess puzzle.
* GUI-based RPG - Explore the world of Elchess in our 2D world created in pygame. Fight monsters in our custom turn-based battle mechanic. Defeat the realm boss in an interactive brain-teaser chess puzzle. Ultimately, fight the God of Elchess in a full on 1v1 game of chess and earn the title of _Grandmaster_!
* Accept inputs via an external chat interface (like Zoom or Twitch) to enable crowdplay.

### _Bonus (if we have time):_

* Variations or additional features to the game of Chess itself
* Expansions to the RPG aspects
* Maximize replayability through better randomizers or additional content
* Other minigames

### _Challenges:_
* None of us know Chess well. We would all need to do heavy research on the subject before diving in.
* Worldbuilding and script writing would be a large undertaking on top of the coding requirement of building a text-based RPG
* The sheer volume of Chess puzzles needed to keep the randomizer for "battles" fresh, on top of needed classification into various stages of difficulty for each of the "realms"
* Making the game fun, challenging, and replayable


## Installation

ElChess requires [Python](https://www.python.org/downloads/) to run.

___Clone the repository___
```sh
git clone https://gitlab.com/techwise-group-15/ElChess.git
```

___Initiate the virtual environment___
```sh
pip install pipenv
pipenv install --dev
```
> Note: `pipenv` is required for initiating the virtual environment.

___Activate the virtual environment___
```sh
pipenv shell
```

## Initialize Game
___Start Game___
```sh
python ElChess.py
```

___Update Settings - Game Modes, HP, Database,etc...___
```sh
nano settings.conf
```
### Pipenv Commands
Install additional dependencies to environment
```sh
pipenv install name_of_dependency
```

Deactivate the environment
```sh
deactivate
```

Remove the virtual environment
```sh
pipenv --rm
```
