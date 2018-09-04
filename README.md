# battle_sim_project
The task is to implement a simple battle simulator that pits one army against another.

At the start of the game, each commander is given a starting total of $10. Units are purchased and stored in their army. The commanders may spend as much or as little of their money as they desire. After the armies are assembled, the units are then made to fight each other in the order they were purchased in. Each unit in the standard game costs $1.

There are three types of units available:
• Archer
• Soldier
• Knight

Each unit has a weakness and a strength. 
Archers are good against Soldiers but are terrible against Knights. 
Soldiers are good against Knights but can’t win against Archers. 
Knights beat Archers, but fall short against Soldiers.
If a unit comes up against a unit of the same type, both lose. 

After each fight, the winner is left on the battlefield to fight the next combatant. If both units lose, then two new units are taken from the army and begin their fight.

Each army is stored as a Python list in the order that they were purchased. This order must be maintained so that the units fight at the correct time. A menu is made for unit selection which allows user interaction through the console (i.e. command-line interface).

Combat is resolved automatically. The outcome of each fight is listed in the console until one army is defeated. Once this occurs, the winner is listed and the game ends.


# advanced_game_proj

Advanced Game

Combat is very simple in the original game, as such an improved version of the combat was implemented using the following rules:
  1. In the cases where a unit would win, it instead deals its damage before the other unit is able to deal theirs. 
    Soldiers hit Knights first, 
    Archers hit Soldiers first, and
    Knights hit Archers first.

  2. Knights are able to trample other units. If the Knight is fighting an Archer and the unit behind the Archer is another Archer, then        the Knight deals its damage to
     both Archers.

  3. If an Archer is at the front of its army but not in battle, they deal their damage to the opposing unit if they are still alive at        the end of combat.
  
  An additional feature that was also implemented was the role of medics:
  Money remaining after the purchasing of armies will be used to hire and outfit medics. When a unit dies, it will be returned to the pool   at the back of the army. Each time this happens, supplies for the medics decreases. Once the medics have no supplies left,
  they will be unable to save any more units.
  Medics are hired and supplied at $1 per unit. All money at the end of army creation is spent on Medics.
