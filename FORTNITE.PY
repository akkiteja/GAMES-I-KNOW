import time
#game startup
print('----------------------------------------')
print('|Welcome to the Fortnite Adventure Game|')
print('----------------------------------------')
print('')
CharacterName = input('What is your username?')
time.sleep(1)
print('')
print(CharacterName +', welcome to this Fortnite python adventure game!')
time.sleep(5)
print('')
print('In this game you will be going through a simulation of Fortnite. It is up to you how you play the game and go for the victory royale!')
time.sleep(7)
print('')
print('Beep Beep')
print('')
print('The battle bus is about ready to takeoff')
time.sleep(4)
print('')
print('And we have liftoff. Where should we drop today?')
print('')
print('1. Tilted Towers')
print('2. Salty Springs')
DropAt = int(input())
if(DropAt == 1):
  time.sleep(1)
  print('You jump off the bus and head for tilted towers. You quickly decide to go to your favorite building, Trump Tower.')
  time.sleep(6)
  print('')
  print('Landing at the top you dash for a wepon. You struggle to find a common supressed SMG with all the defulty boys pickaxing you. Luckily you got the only wepon so you easily destroyed everyone at the top.')
  time.sleep(8)
  print('')
  print('Breaking the floor from under you, you look for a better wepon. You find a trap and a minigun')
  time.sleep(6)
  print('')
  print('You hear someone comming up the stairs. Do you:')
  time.sleep(2)
  print('')
  print('1. Place down the trap')
  print('2. Charge up your minigun and go crazy')
  TiltChoice1 = int(input())
  if(TiltChoice1 == 1):
    time.sleep(1)
    print('You place the trap on the staircase. The enemy hears you place the trap. They slow down and decide what to do')
    time.sleep(6)
    print('The enemy throws some stink bombs at you, forcing you to run down the stairs. You run down to find the enemy waiting for you, Where they one pump you.')
    time.sleep(7)
    print('')
    print('And with that the game is over. Try again to go for the victory royale')
    print('Better luck next time. Thanks for playing '+ CharacterName + '. This game was created by CodePython2')
  else:
    time.sleep(1)
    print('You start charging up the minigun. You go crazy blasting the bullets everywhere and even hitting the enemy a couple times. But the fun is short lived because you run out of amo. The enemy quickly one pumps you')
    time.sleep(10)
    print('')
    print('And with that the game is over. Try again to go for the victory royale')
    print('Better luck next time. Thanks for playing ' +CharacterName + '. This game was created by CodePython2')
if(DropAt == 2):
  time.sleep(1)
  print('')
  print('You drop towords salty springs and remember the secret bunker that Ali-A told you about')
  time.sleep(4)
  print('')
  print('Bump, bana, bump, bana, bump, bana, dump, dump. Bump, bana, bump, bana, bump, bana, dump, dump.')
  time.sleep(9)
  print('')
  print('Jokes aside, you drop at the bunker. You head down and loot both chests')
  time.sleep(6)
  print('')
  print('You get a RPG and inpulse nades. You hear someone above you. Do you:')
  time.sleep(3)
  print("")
  print('1. Box in and camp')
  print('2. Inpulse away from them')
  print('3. Run at them with your RPG')
  Salt1 = int(input())
  if(Salt1 == 1):
    time.sleep(1)
    print('You box up and camp like a chicken. They come down and start shooting out your walls. When they break the wall you fire a RPG at them, but they already placed down a wall. The RPG colides with the wall and blows you into smitheriens.')
    time.sleep(5)
    print('')
    print('And with that the game is over. Try again to go for the victory royal')
    print('Better luck next time. Thanks for playing ' +CharacterName + '. This game was created by CodePython2')
  if(Salt1 == 2):
    time.sleep(1)
    print('')
    print('You quickly inpulse away, fleeing to dusty divot. You go up to the depot finding a shopping cart just waiting for you to ride in. You see someone running at you from the mountain. Do you:')
    time.sleep(7)
    print('')
    print('1. Boost towords them in the shopping cart')
    print('2. Quickly build up a 1 by 1')
    Salt2 = int(input())
    if (Salt2 == 1):
      time.sleep(1)
      print('')
      print('You blast a RPG behind you giving you a massive speed boost. Switching to the passenger seat you fire and the RPG colides with the enemys head, sending them back to the lobby. Nice one')
      time.sleep(10)
      print('')
      print('You loot his drops and find that he was carring a bush on him. You put it on and camp near the shopping cart untill there are 3 people left. They are both high up in 1 by 1 towers. They dont even notice you are there')
      time.sleep(11)
      print('')
      print('They start bombarding each other with gernades, destroying most of the bases of their towers. You shoot a RPG at both of the bases')
      time.sleep(7)
      print('')
      print('The buildings both come crashing down, killing one and severly hurting the other. It is now a 1v1 between the Omega and you. This is IT. Do you:')
      time.sleep(10)
      print('')
      print('1. Stay in the bush untill the storm closes in')
      print('2. Try to nock them into the storm with the shopping cart')
      print('3. Rush them and fire a RPG')
      Salt3 = int(input())
      if(Salt3 == 1):
        time.sleep(1)
        print('')
        print('You decide to put trust in your bush. You see the Omega healing and then build a new tower. The storm starts closing it. Slowly but surly you move in')
        time.sleep(9)
        print('')
        print('You see the Omega above you but you dont do anything. The storm is almost all the way closed in')
        time.sleep(7)
        print('')
        print(' Wait, what!')
        time.sleep(1)
        print('The Omega is dropping down from the tower. They spin in the air and fire a snipe at you.')
        time.sleep(9)
        print('')
        print('You stay very still. The bullet barly misses you. The Omega hits the ground and dies of fall damage.')
        time.sleep(6)
        print('')
        print('Yay!!!! You won!!!!!!')
        print('')
        print('---------------------')
        print('| VICTORY ROYAL! #1 |')
        print('---------------------')
        print('')
        time.sleep(3)
        print('Thanks for playing ' + CharacterName +'. This game was made by CodePython2')
      if(Salt3 == 2):
        time.sleep(1)
        print('')
        print('You fling your loyal shopping cart at the Omega. But the shopping cart is useless because the Omega builds a giant wall seperating both halves of the circle')
        time.sleep(6)
        print('')
        print('You think about your options. A Donald Trump is on the other side of the wall and will not let you cross the boarder. You are just a bush with a RPG. How can you outplay this monster?')
        time.sleep(8)
        print('')
        print('You have come up with a plan. You can beat him')
        time.sleep(4)
        print('')
        print('(Donald Trump): That is FAKE NEWS. You are WRONG. You cant stop me and all my MONEY!')
        time.sleep(9)
        print('')
        print("Gernades start raining from the sky, aniliating you and your wonderful bush.")
        time.sleep(5)
        print('')
        print('Hello darkness my old friend')
        time.sleep(4)
        print('')
        print('And with that the game is over. Try again to go for the victory royal')
        print('Better luck next time. Thanks for playing ' +CharacterName + '. This game was created by CodePython2')
      if(Salt3 == 3):
        time.sleep(1)
        print('')
        print("You start ramping them with you amazing building skills that you learned from ninja. Once you get high up you throw down the Myth in a can you found lying around. You now have the high ground")
        time.sleep(9)
        print('')
        print('(Memes): Its over Anikin! I have the HIGH GROUND!')
        time.sleep(6)
        print('')
        print('You send down you final RPG waiting for the explosion')
        time.sleep(6)
        print('')
        print('      _____[_  ---')
        print('     /       | ----')
        print('     \       | ------')
        print('      -----[-  -------')
        time.sleep(1)
        print('')
        print('     _____[_  ---')
        print('    /       | ----')
        print('    \       | ------')
        print('     -----[-  -------')
        time.sleep(1)
        print("")
        print('    _____[_  ---')
        print('   /       | ----')
        print('   \       | ------')
        print('    -----[-  -------')
        time.sleep(1)
        print("")
        print('  \ | /  ')
        print('  -   -  ')
        print('  / | \  ')
        time.sleep(1)
        print("")
        print(' \  |  /')
        print('  \ | / ')
        print(' --   --')
        print('  / | \ ')
        print(' /  |  \ ')
        time.sleep(1)
        print('')
        print("\   |   /")
        print(' \  |  /')
        print('  \ | /')
        print('---   ---')
        print('  / | \ ')
        print(' /  |  \ ')
        print('/   |   \ ')
        time.sleep(2)
        print("")
        print('Yay!!!! You won!!!!!!')
        print('')
        print('---------------------')
        print('| VICTORY ROYALE! #1 |')
        print('---------------------')
        print('')
        time.sleep(3)
        print('Thanks for playing ' + CharacterName +'. This game was made by CodePython2')



    else:
      time.sleep(1)
      print('')
      print('You build up your 1 by 1, leaving the shopping cart. You lookout to see the enemy comming towords you with also a RPG. They quickly inpulse at you and blast the RPG mid air. The RPG hits and blows you up, sending you back to the lobby')
      time.sleep(10)
      print('')
      print('And with that the game is over. Try again to go for the victory royal')
      print('Better luck next time. Thanks for playing ' +CharacterName + '. This game was created by CodePython2')
  if(Salt1 == 3):
      time.sleep(1)
      print('')
      print('You dangerously run at him with your RPG. They look like a noob so you calm down. You drop them some sheild and a wepon, seeing what they will do')
      time.sleep(6)
      print('')
      print('They pick up the gun and out of no where headshot you with the tac. It seams they were a pro pretending to be a noob. They then do take the l, the little troll that they are')
      time.sleep(7)
      print('')
      print('And with that the game is over. Try again to go for the victory royal')
      print('Better luck next time. Thanks for playing ' +CharacterName + '. This game was created by CodePython2')