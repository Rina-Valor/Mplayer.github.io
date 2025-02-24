init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="fixeded",
            category=["life"],
            prompt="How to fix the issue!",
            pool=True,
            unlocked=True
        )
    )

image origami1 = "/submods/issue/start.png"
image origami2= "/submods/issue/enter project.png"
image origami3 = "/submods/issue/select all of them!.png"
image origami4 = "/submods/issue/should be located in github!.png"
image origami5 = "/submods/issue/enter real project.png"
image origami6 = "/submods/issue/paste them all in!.png"
image origami7 = "/submods/issue/go back to the arduino.png"
image origami8 = "/submods/issue/copy the ino!.png"
image origami9 = "/submods/issue/drop in the src area!.png"
image origami10 = "/submods/issue/select new folder!.png"
image origami11 = "/submods/issue/open and boom done!.png"

transform craneframe:
    xanchor 0
    yanchor 0
    xpos 80
    ypos 150
    alpha 1.0

label fixeded:
show monika at t22
m 3rta "Odd choice [player], But to fix this issue!"
show origami1 at craneframe zorder 13
m 3rta "We should find our Documents Folder!"
hide origami1
show origami2 at craneframe zorder 13
m 3rub "Then enter the Platform.io folder!"
hide origami2
show origami3 at craneframe zorder 13
m 3hua "Then select and copy all the files n folders!"
hide origami3
show origami4 at craneframe zorder 13
m 3hub "Go to your github folder in \\C: Drive!"
hide origami4
show origami5 at craneframe zorder 13
m 3rua "Go into your real project folder (The folder you want for github)"
hide origami5
show origami6 at craneframe zorder 13
m 3cub "And paste them!"
hide origami6
show origami7 at craneframe zorder 13
m 3rua "Now go back to the documents folder with your arduino!"
hide origami7
show origami8 at craneframe zorder 13
m 3rub "And Copy the ino you want!"
hide origami8
show origami9 at craneframe zorder 13
m 3rua "Place it in the src folder of the github project!"
hide origami9
show origami10 at craneframe zorder 13
m 3rub "Now in visual studio code, go to files and select open folder!"
hide origami10
show origami11 at craneframe zorder 13
m 3rua "Open the folder and done!"
hide origami11
show monika at t11
m 3rub "Then you just wait for the platfrom.io core to load and it'll all work!"
m 2nua "That's all player wanted for this!"
m 2tua "Now this should be an easy tutorial"
return
