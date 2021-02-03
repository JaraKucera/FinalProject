define R = Character("Sam", color="#eb3474")
define r = Character("Unknown", color="#eb3474")
define dad = Character("Dad", color="#7732a8")
define mom = Character("Mom", color="#ebdb2d")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    mom "Are you sure that this is absolutely the best idea? Do you genuinely think that one less mouth to…"

    dad "Quiet, he’ll hear you. You wouldn’t want to cause that boy any more harm, would you?"

    mom "It’s fine, he’s listening to his music, he can’t hear us. He’s probably all lost in his virtual world again."

    "I was in truth not listening to any music nor was I in any virtual fantasy world where everything was OK."
    "I was sitting in a car going miles away from civilization to some summer camp, that according to my dad would make all the worries go away."
    "Whose worries? That was something that he did not expand upon. The world that I am in is reality. A harsh tough reality that does not always care about what you want."
    # This ends the game.

    return
