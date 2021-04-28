define R = Character("Sam", color="#eb3474")
define r = Character("Weird Girl", color="#eb3474")
define dad = Character("Dad", color="#7732a8")
define mom = Character("Mom", color="#ebdb2d")
define mc = Character("You", color="#3bd9b4")
define t = Character("Trevor", color="#36b300")
define i = Character("Instructor", color="#CE8147")
define t2 = Character("Tray", color="#CDE7BE")
define gui.text_font = "NewTegomin-Regular.ttf"
define gui.interface_text_font = "NewTegomin-Regular.ttf"
define gui.glyph_font = "NewTegomin-Regular.ttf"

# The game starts here.
label start:
    
    $ choices = [] #Contains the keyword strings of all choices made by the player.
    $ trueChoices = dict()
    $ relantionship = 0 #Relantionship rating based on choices made [int]
    #A bool dict to help with final showing of results
    $ choicesMade = {"2a":False,"2b":False,"3a":False,"3c":False,"4a":False,"4b":False,"4c":False,"5a":False,"5b":False,"6a":False,"6b":False,"7b":False,"8":False,"9a":False,"9b":False,"9c":False,"10a":False,"10b":False,"10c":False}
    #Stats of ghost girl, each choice changes her emotions, too low in certain values causes the end of the game.
    $ ghostStats = {'trust':50, 'anger':50, 'anxiety':50, 'helped':50, 'strength':50, 'hurt':50, 'happiness':50}
    $ resultOutput = {  "2a":"Self blame is usually a sign of symptoms of depression. Repeated self-doubt and lack of belief in one self is connected with low self-esteem. The lower the confidence the higher the chance of having been affected by depression.",
                        "2b":"Repeated blaming of everyone around you instead of yourself, can be a sign of a mental health issues however is not usually tied with depression.",
                        "3a":"Self blame is usually a sign of symptoms of depression. Repeated self-doubt and lack of belief in one self is connected with low self-esteem. The lower the confidence the higher the chance of having been affected by depression.",
                        "3c":"Showed a lack of trust towards Sam, when you first met her. While not as hurtful when it is your first time meeting her, if continued would cause more pain. Trust can only be earned through trust.",
                        "4a":"Dismissing Sam opening up to you made her trust you less and made her feel unwanted. It’s best to listen to depressed people when they open up to you because it can be a really difficult thing for them to do. Shutting them down will make them feel like their battle to tell you has been for nothing and that they should have listened to their doubts about telling you.",
                        "4b":"Appreciating Sam opening up to you and telling you about losing her passion for things is one of the best choices that can be made. It is best to encourage when depressed people open up to you as it can be a quite difficult thing to do and shows a lot of trust.",
                        "4c":"Losing your passion for many things in life is one of the main symptoms of depression. It can be absolutely heartbreaking. Not having things that used to bring you happiness any more can be destructive.",
                        "5a":"Trusted Sam during the dog attack, while it can be hard to trust people, this was a needed factor for Sam.",
                        "5b":"Didn’t trust Sam during the dog attack. The Repeated lack of trust towards her was very hurtful and caused her to not want to open up to you much. Unless you managed to prove otherwise.",
                        "6a":"You provided Sam your name. It is important to remember that it’s best to sometimes reach out to someone multiple times, even if they seem fine. Looking available for help can be really reassuring.",
                        "6b":"It’s best to show that you’re there and available for people to vent to you and trust you, but it’s also a good idea not to push anyone into revealing information that they don’t want to give you.",
                        "7b":"You responded with anger when asked if you had hope for being found. This represents your hidden anger for the world. Feeling like you don’t don’t owe anything to the world. A lack of care for your actions on the world. Can be a sign of a form of depression. Best would be to not lose hope in this situation.",
                        "8":"The feeling of numbness is what depression can most be associated with. It’s that feeling of being so overwhelmed with emotions that no emotions are active at all. It is not prevalent in all forms of depression. Feeling numb from time to time can be okay and just a sign of being overwhelmed with emotions but frequent occurrences is a sign of depression.",
                        "9a":"When Sam passed through you, you put pressure on her to tell you what is up. This is not the best way to go about this as you are putting stress onto her to tell you something that is very difficult to talk about. In real life when interacting with a depressed person it is best to not pressure them into telling you everything straight away. The best strategy is to be available to them and let them know that you’re there for them and that they can open up to you.",
                        "9b":"When Sam passed through you, you were careful with her. This is the best approach to this situation, putting too much pressure on her to open up may cause her to close up and not want to open up. In real life when interacting with a depressed person it is best to not pressure them into telling you everything straight away. The best strategy is to be available to them and let them know that you’re there for them and that they can open up to you.",
                        "9c":"When Sam passed through you, you put a lot pressure on her to tell you what is up. This is not the best way to go about this as you are putting stress onto her to tell you something that is very difficult to talk about. In real life when interacting with a depressed person it is best to not pressure them into telling you everything straight away. The best strategy is to be available to them and let them know that you’re there for them and that they can open up to you.",
                        "10a":"During Sam’s mental breakdown you were understanding to her and supportive. Mental breakdowns are not fun to go through and generally feel horrible to go through. An outburst of emotions suddenly happens and it is very difficult to control that's why it is best to be understanding, careful and supportive with anyone going through one.",
                        "10b":"During Sam’s mental breakdown you were apologetic to her but supportive. Mental breakdowns are not fun to go through and generally feel horrible to go through. An outburst of emotions suddenly happens and it is very difficult to control that's why it is best to be understanding, careful and supportive with anyone going through one.",
                        "10c":"During Sam’s mental breakdown you pushed her to move on and get over it. This is the worst approach that can be taken and can be very hurtful when a person is at their worst. Mental breakdowns are not fun to go through and generally feel horrible to go through. An outburst of emotions suddenly happens and it is very difficult to control that's why it is best to be understanding, careful and supportive with anyone going through one."
                        }
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    init python:
        import pymongo
        import algorithm
        from pymongo import MongoClient
        #client = MongoClient('****')
        #db = client.mongodb4075


    #python:
        #algorithm.algorithm_function()
        
    screen start_screen():
        frame:
            xalign 0.5 yalign 0.5 xpadding 20 ypadding 20
            vbox:
                text "Hello, this is the creator of the game.\n\nI would like to warn you that this game is centred around topics of depression, anxiety and bullying.\n\nIf you are sensitive to these topics and wish to avoid them then please exit the game now.\n\nThe game and dialogue has been created with one form of depression in mind, learned about from various research papers, and through the experiences of those around me.\n\nYou will be playing as an unnamed boy that has just been sent to a summer camp by his parents. This game seeks to find out if there can be a correlation between signs of potential depression through the actions that the player takes when developing a bond with a character that this game is centred around.\n\nPlease, try to answer each choice based on how you would act rather than how you think the character would act. Some choices are more important than others. Thank you for playing!\n\n"
                hbox xalign 0.5 spacing 500:
                    textbutton "I consent.":
                        action Return(True)
                    textbutton "I do not consent.":
                        action Quit(confirm=None)

        
    call screen start_screen
    play music "audio/Awaiting-the-Devil.ogg" volume 1.0 fadein 1 fadeout 1 loop
    scene act1 with Dissolve(1.0)
    pause .5
    scene bg room with Dissolve(1.0)
    pause .5
    mom "Are you sure that this is absolutely the best idea? Do you genuinely think that one less mouth to…"
    dad "Quiet, he’ll hear you. You wouldn’t want to cause that boy any more harm, would you?"
    mom "It’s fine, he’s listening to his music, he can’t hear us. He’s probably all lost in his virtual world again."

    "I was in truth not listening to any music nor was I in any virtual fantasy world where everything was OK."
    "I was sitting in a car going miles away from civilization to some summer camp, that according to my dad would make all the worries go away."
    "Whose worries? That was something that he did not expand upon. The world that I am in is reality. A harsh tough reality that does not always care about what you want."
    mom "I just think that maybe there could be a better way to go about this."
    dad "I wish that there was, but this summer camp might just be our saving grace."
    "Just as those words left the mouth of my stern father, a flimsy wooden cracked sign with the words “John Kai’s Summer Camp” passed by the car."
    "The dirt track road spiralled down a forest so dense it felt as if the car would have to squeeze through to pass."
    "Even though it was July, the deeper we went, the more and more the trees lost their colours. With each passing minute, colours got drained out of the environment to leave just pale broken down tree barks."
    "Hollow emotionless trees replaced those bright summer colours and with them, they took the already sparse joyous emotions"
    play sound "audio/Car.ogg" volume 0.5 fadein 1 fadeout 1
    mc "So this, is it? The place where I will spend the rest of the summer all away from you guys?"
    dad "Look Sport, we already discussed this with your mom, this will benefit you the most, so get out there and let the person in charge know that you’re here."

    menu choice_1:
        "Reconsider":
            python:
                choices.append("Reconsider")
                trueChoices[0] = "Reconsider"
            jump choice_1_home

        "*silence*":
            python:
                choices.append("Silence")
                trueChoices[0] = "Silence"

            jump choice_1_done

        "Understanding":
            python:
                choices.append("Understanding")
                trueChoices[0] = "Understanding"

            jump choice_1_understanding
    
    label choice_1_home:
        mc "Can’t you please reconsider? I don’t think that I should be here. I’ll do whatever it takes to stay home."
        dad "Listen, it will only be for a short time, soon you’ll be back home with us. We just can’t handle things right now."
        jump choice_1_done

    label choice_1_understanding:
        mc "Yeah, I understand, I will give this a shot, and hopefully, it won’t be too bad. If anything happens I will let you guys know."
        dad "Thanks for understanding sport."
        jump choice_1_done

    label choice_1_done:
        "Without even saying goodbye they were gone. The car getting swallowed by the spiral of trees, possibly never to be seen again."
    
    play music "audio/Punch-Deck-Longing.ogg" volume 1.0 fadein 1 fadeout 1 loop
    "By looking at the camp, you could tell that in the past it must have been filled with the joyous souls of children laughing about, enjoying their summers, stress-free and happy."
    "All the buildings shining, feeling alive and fresh. The new reality was a mere husk of the past. The lake where children would cool off after a long day of activities looked more like one step inside would contaminate your body with toxic waste."
    "The cabins and buildings all looked soulless, the colour drained from this place. It looked like it was all going to collapse soon from all the mould and lack of care."
    "From everyone’s expressions, you could tell that joy and happiness were two emotions gone from this world. Everyone had the same facial expression, an expression that screamed help me, let me leave, I’ve had enough."
    "Even those that were in charge all looked like they were slaves, slaving away for a minimal wage, hoping to get by until their next paycheque."
    
    play sound "audio/Thud.ogg" volume 1.0
    with hpunch
    t "Hey watch it! What do you think that you’re doing?"
    "Before I even got a chance to respond, he grabbed me by my shirt and held me against the wall."
    t "Listen here, I see that you’re new here, so I’m only going to give you a warning this time. People around here are in fear when they hear my name. The boys and I here are T."
    t "We run this little camp, so don’t you dare ever bump into me or the boys ever again. If you do you’ll get this but much worse."
    play sound "audio/Punch.ogg" 
    with vpunch
    "With that, he punched me in the gut and left me heaving on the ground. As his friends walked by they spat on me and called me a loser."
    "What a great way to start this camp. Hopefully, he won’t be too much of a problem."

    play music "audio/Dystopian.ogg" volume 1.0 fadein 1 fadeout 1 loop
    "After going to the head’s office to sign up and be assigned to a bed in a run-down cabin. I was informed that I’ve come on time to be able to partake in the final activity of the day before bedtime."
    "One of the run-down buildings had a nice set of windows to one of the sides of the walls overlooking the forest. The cabin wasn’t as bad as it looked from the outside, the walls constructed out of logs with certifications hung up and framed from years before I was even born."
    "How I wish I could have dealt with this camp twenty years ago during its glory years. While I am the last person to enjoy group activities and the outside, it would have made it much more bearable."
    "Opposing the wall of windows was a large fireplace, it was the only signal of hope in this building. Burning brightly, being strong and tough, all quantities that I would need to survive this summer."
    i "Welcome all to the afternoon slash evening class for today. We will box to tire ourselves out so that we can have that goodnights sleep."
    "There were only about twenty kids here, most of which looked like they would rather be dead than to partake in this activity."
    i "Since most of you are new to this camp, the teams have been picked randomly. Now don’t worry you won’t be punching each other. One of you will be holding the punching bag while the other will be punching it. I will read the pairs out now."
    "I almost lost my heart to shock when I heard my name announced after the name Tray. For I realized in that split second upon seeing his face that the guy that had punched a hole through my gut was Trevor."
    t "I hope that you remember the warning that you got earlier today."
    "Hearing those words echo in my brain along with the devious smile plastered on his face brought back the feeling of pain that still wasn’t fully away. I was first to hold the punching bag. Trevors face grew with pleasure every time that he punched."
    play sound "audio/Punch.ogg"
    with vpunch
    pause 0.25
    queue sound "audio/Punch.ogg" volume 0.75
    with hpunch
    pause 0.25
    queue sound "audio/Punch.ogg" volume 0.60
    with vpunch
    pause 0.25
    queue sound "audio/Punch.ogg" volume 0.25
    with hpunch
    pause 0.25
    queue sound "audio/Punch.ogg" volume 0.5
    with vpunch
    "Each punch sent shockwaves throughout my body and pushed me further. Keeping my balance was getting more difficult with each punch. The harder the punch the wider the grin on his face would be."
    "Somehow I managed to survive the first twenty minutes, it was now my turn to punch. It didn’t seem like my punches had any impact on Tray whatsoever. It was as if I was just gently tapping the punching bag."
    "For the first time, I was a little at peace, I could study the surrounding environment. Everyone seemed to be doing much better, some even had a smile on their face. It looked like they were making friends."
    "If some details had been taken out of the equation, it would almost be a wholesome scene to witness. Before I could fully immerse myself, it was time to swap once again. I held onto dear life, hoping to not let go of the punching bag, for if I did I would be in a world of pain."
    "Trevor was not holding back at all. Thankfully, I managed to survive the full twenty minutes, only one last set from me before I was free."
    "As I punched I started to immerse myself, none of this would have happened if I wasn’t here, this pain wouldn’t be in my stomach. I wouldn’t be wasting my time on a summer camp if it wasn’t for:"

    menu choice_2:
        "Myself":
            python:
                choices.append("Myself")
                choicesMade["2a"] = True
                trueChoices[1] = "Myself"
                
            jump choice_2_me

        "My family":
            python:
                choices.append("Family")
                choicesMade["2b"] = True
                trueChoices[1] = "Family"

            jump choice_2_family

        "No one's fault":
            python:
                choices.append("No ones fault")
                trueChoices[1] = "Noonesfault"

            jump choice_2_no_one
    
    label choice_2_me:
        "This is all my fault, if I had just done things differently, helped out more, if I was different. If I was better, to myself and them. I wish I was good enough."
        jump choice_2_done
    
    label choice_2_family:
        "It’s all of their fault, if only they would just care, maybe offer some help. Focus on me for once. Why can’t I get the focus for a bit sometimes? I just wish that they were better."
        jump choice_2_done

    label choice_2_no_one:
        "It’s no one’s fault that I am in this situation. Things just sometimes happen that we have no control over. Things happen because of luck and misfortune, and I was just unlucky to get to this point."
        jump choice_2_done
    
    label choice_2_done:
        play sound "audio/Punch.ogg" volume 0.75
        t "Oh I am going to absolutely kill you."
    
    "I was so lost in thought that I did not realize that time was over. I boxed Trevor into the throat."
    i "Hey now calm down it was an accident, leave him alone."
    "Thank god that the supervisor was there to save me otherwise I probably would have died just there and then."
    t "You’re dead."
    "That’s all Trevor said as he left the building."
    play music "audio/EmptyStreets.ogg" volume 1.0 fadein 1 fadeout 1 loop
    "With that, the activities had come to an end and so did the day. After making my way to the cabin and being checked off the present list I was ready to end the day in a hard and cold bed. I wanted to finally rest, the day had been so exhausting."
    "Even though I was so dead my body did not listen to me and instead kept me awake reliving all the events that had transpired. I just sat there at my bed wishing that this was all a dream and that I would just wake up in my bed at home."
    "Sadly, this isn’t a primary school short story where all conflicts got resolved and disappeared when the character suddenly wakes up and realizes it had all been just a dream. This is instead a reality where Trevor had gathered his friends and had come after me."
    "Finding the cabin where I would be sleeping was not a difficult task. Even going blindly would give you a twenty percent chance to guess on the first try. There were five cabins for each gender which housed five kids each."
    "It didn’t take long before I heard the door open before a hand had been put over my mouth, with other hands used to drag me outside. It all happened so fast that I didn’t even get a chance to yell or focus attention on myself."
    "The last thing that I saw was a bright star shining in the night sky before everything went dark."
    play music "audio/sad_piano_track_4.ogg" volume 0.5 fadein 1 fadeout 1 loop
    play sound "audio/Punch.ogg" volume 0.75
    "I woke up to a punch to the gut, the same punch that I had received earlier."
    t "Well, well, well, I told you that I’d kill you. You know, no one has messed up on the same day as their warning. You must be incredibly stupid or incredibly unlucky."
    t "Either way, let me explain what's going to happen to you. I want to see the fear in your eyes as I go over everything that will happen to you."
    t "Firstly, calm down, you’re not actually going to die, you’re just going to suffer a lot. My boys and I are going to roughen you up a little. When you are found tomorrow morning you’ll have to be brought to the hospital and possibly be put on life support."
    t "But hey it will get rid of you from this camp and out of my face. I don’t want any of my problems here, and you have become a problem."
    "With that came punches and kicks all over my body."
    play sound "audio/Punch.ogg"
    with vpunch
    pause 0.25
    queue sound "audio/Punch.ogg" volume 0.75
    with hpunch
    pause 0.25
    queue sound "audio/Punch.ogg" volume 0.60
    with vpunch
    pause 0.25
    queue sound "audio/Punch.ogg" volume 0.25
    with hpunch
    pause 0.25
    queue sound "audio/Punch.ogg" volume 0.5
    with vpunch
    "I had no idea where I was. I was in the forest for sure but from what I could see, but it wasn't anywhere near the camp. The trees were here to cover up any sounds that might help me."
    "The branches as if being held against my mouth muffling anything that would escape my mouth, in hopes of getting help. It was almost pitch black now if I was to survive this beat down would I even be able to get back? I didn’t deserve this."
    t2 "Hey Trevor isn’t this forest haunted?"
    t "Tray are you completely stupid?"
    play sound "audio/Howl2.ogg" volume 1 
    "Suddenly a loud howl echoed throughout the forest distracting everyone. My hands remained tied by some rope, my legs although beaten were free."
    "With the adrenaline in my body, I made a run for it through the forest with only a slight head start before being followed."
    "There wasn’t much light left from the sun and most of it was unable to pass through the forest sky. I had no clue where I was going before slipping and tumbling down."
    play music "audio/Punch-Deck-Brahe.ogg" volume 1.0 fadein 1 fadeout 1 loop
    #Chapter 2
    scene act2 with Dissolve(1.0)
    pause .5
    scene bg room with Dissolve(1.0)
    pause .5
    r "Oh looks like you’re waking up. That fall looked like it hurt a lot."
    "I awoke to the sounds of someone gently talking as if assuming that no one would hear them. I couldn’t understand what they were saying, everything muffled and blurring. It took a couple of seconds before my eyes adjusted, and I could decipher what was said to me."
    "I was still in the forest, however, it felt different, that dead atmosphere disappeared and got replaced by a brighter living forest. Although it was dark, the bright stars illuminated the surroundings."
    "The trees no longer looked like they were trying to grab at you but instead looked like they were offering you a hug to console you. In front of me sat a girl about my age on a log."
    "She wore a typical summer outfit of a t-shirt and pants, but for some reason had a red scarf tied around her neck."
    r "Well blue shirt? Did the fall remove your ability to communicate? Are you okay?"
    mc "Oh yeah Uhm sorry I was just trying to recollect myself. Where are we?"
    "I tried getting up to get closer to her for a better look but as I tried to stand on my right foot, I collapsed to the ground from the pain."
    r "Yikes blue shirt, looks like that fall might have twisted your ankle. You’re lucky that I am here to save you. You did almost fall on me though when you decided to tumble down all of those hills."
    r "I did notice that your hands had been tied with some rope, poor craftsmanship for sure though. So bad that your hands got untied by the fall. What did happen to you?"
    "As she talked the moon lit up her face, she looked like an ordinary weird girl, weird because she had a huge smile plastered on her face the entire time that she talked."
    "Snickering here and there at her jokes. It kinda felt like she was happy that I almost fell on her. What do I tell her about what had happened?"

    menu choice_3:
        "My own fault":
            python:
                choices.append("Blame self")
                relantionship += 5
                choicesMade["3a"] = True
                ghostStats['happiness'] -= 5
                ghostStats['strength'] -= 2
                ghostStats['trust'] += 2
                trueChoices[2] = "Blameself"
                

            jump choice_3_depressive

        "Trevor":
            python:
                choices.append("Blame Bully")
                relantionship += 2
                ghostStats['happiness'] -= 2
                ghostStats['strength'] += 2
                ghostStats['trust'] += 2
                trueChoices[2] = "BlameBully"

            jump choice_3_hurtful

        "Dismiss Question":
            python:
                choices.append("Distrust")
                relantionship -= 5
                choicesMade["3c"] = True
                ghostStats['happiness'] -= 5
                ghostStats['strength'] -= 5
                ghostStats['trust'] -= 10
                ghostStats['anger'] += 5
                trueChoices[2] = "Distrust"

            jump choice_3_distrustrusful

    label choice_3_depressive:
        mc "I messed up a lot, where bumping into someone lead up to getting beaten up to messing up again. I ran away from them, but I couldn’t see in the dark and slipped, so now I am here. It is all my fault."
        r "Yeah that makes a little sense, most of our pain starts from little things that transpire out of control and eventually lead us here. But everything will be okay, we just need to get you to someplace to rest for a while. This part of the forest sometimes has wild rabid dogs."
        r "I wouldn’t want you getting hurt more than you already are, Blue Shirt." 
        jump choice_3_done

    label choice_3_hurtful:
        mc "I got bullied by this guy called Trevor and his friends. I don’t know why I deserved such treatment, but I did accidentally punch Trevor in the throat."
        r "Well thanks for being honest with me. The treatment that we get from others isn’t always the one that we deserve."
        r "Though I understand why someone would be upset if they got hit in the throat. We should walk to a cabin nearby, this part of the forest sometimes has wild rabid dogs sniffing about. I worry about getting caught up in that, Blue Shirt."
        jump choice_3_done

    label choice_3_distrustrusful:
        mc "I don’t want to talk about it. Things happened, and now I am here with bruises all over my body and a potentially twisted ankle."
        r "Things could be worse. At least you’re still alive. Let’s go get you some help, this part of the forest tends to have wild dogs roaming about."
        r "Wouldn’t want to add damage top that body. Would we now? Blue Shirt."       
        jump choice_3_done

    label choice_3_done:
        r "Be careful with that ankle, let’s walk slowly a bit this way. Eventually, we will reach a cabin that has some medical supplies."
        r "Or at least it did have them the last time that I was there, which hadn’t been for a while."

    "With that, she jumped from the log that she was sitting at and waited for me to get up. Exerting pressure on the ankle caused a lot of pain shooting throughout my body but limping made walking somewhat possible."
    "My entire body was already in pain from the still fresh beat down, so slightly more pain wouldn’t be too noticeable. The girl was very weird, walking a few feet in front of me."
    "To me, it seemed like her constant smile tried to tell people that she was happy. However, when she would reply to me, her eyes and speech made it feel like her smile was a cover-up for how she genuinely felt."
    "Her smile wasn’t a product of her heart but a product of her mind to hide away her true feelings. Yet there was something about her that gave me hope."
    mc "What were you doing here anyway? Are you also from the camp?"
    r "Oh no I was just strolling about trying not to be in the way of things. I don’t know anything about any camp, you might have fallen for a while and hit your head quite hard. I hope that ankle doesn’t hurt too much."        
    "How she knew where to go was a mystery to me, darkness was surrounding us trying to engulf us inside it. It was as if she was my torch, a torch that if it went out would leave me to be a hopeless mess struggling to ever getting back to safety."
    "I had to get back to the camp and make my way somehow. I hate this place, this red scarf girl is the first good thing about this entire day."
    mc "Do you live around here?"
    r "In the past, I used to almost live around these woods with my Mom and Dad. I used to enjoy strolling around these hills, looking at nature, drawing everything into my journal. These woods helped me out a lot, they let me escape the stress of home."
    r "But after a while, I stopped enjoying strolling about and drawing. I found it pointless, it no longer helped me, it just drained so much of my energy, so I stopped."
    r "After something happened I even started to hate the woods for a while, they made me feel locked inside them, made me feel like I couldn’t escape and made me feel like I have changed, that I wasn’t the same me any more."
    r "But today I just felt drawn to these woods, I don’t know why, but I just had an urge to explore again. Oh, sorry for talking for so long, I doubt that you wanted to hear all of that."
    
    menu choice_4:
        "Dismissal":
            python:
                choices.append("Dismissal")
                relantionship -= 5
                choicesMade["4a"] = True
                ghostStats['happiness'] -= 5
                ghostStats['strength'] -= 5
                ghostStats['trust'] -= 5
                ghostStats['anger'] += 5
                ghostStats['anxiety'] += 2
                ghostStats['helped'] -= 5
                ghostStats['hurt'] -= 5
                trueChoices[3] = "Dismissal"

            jump choice_4_dismissal

        "Appreciative":
            python:
                choices.append("Appreciative")
                relantionship += 2
                choicesMade["4b"] = True
                ghostStats['happiness'] += 5
                ghostStats['strength'] += 2
                ghostStats['trust'] += 5
                ghostStats['anger'] -= 5
                ghostStats['anxiety'] -= 2
                ghostStats['helped'] += 2
                ghostStats['hurt'] -= 2
                trueChoices[3] = "Appreciative"

            jump choice_4_appreciative

        "Relate":
            python:
                choices.append("Relate to losing passion")
                relantionship += 5
                choicesMade["4c"] = True
                ghostStats['happiness'] += 2
                ghostStats['trust'] += 5
                ghostStats['anger'] -= 5
                ghostStats['anxiety'] -= 2
                ghostStats['hurt'] -= 2
                trueChoices[3] = "Relatetolosingpassion"

            jump choice_4_relate

    label choice_4_dismissal:
        "Yeah I didn’t ask for any of that. I just want to get to the cabin as soon as possible to fix this ankle."
        r "Yeah I’m sorry. I just got carried away a little, don’t worry we are almost there."
        jump choice_4_done

    label choice_4_appreciative:
        "No, I appreciate hearing that. I feel like I understand you a little more. I understand losing passion for something that you used to love. While it has not happened to me, I know that it must be very painful."
        "Losing our passion for something is kind of like losing a part of ourselves."
        r "Thanks, I’m sorry for going off, but I am glad that you can understand a part of this weird reality that I live in. We are almost at the cabin now."
        jump choice_4_done

    label choice_4_relate:
        "Yeah I can relate to that. While mine isn’t about nature and drawing necessarily, I’ve had a similar experience with something similar. Also lost my love for doing something that I used to love a lot. It felt like a part of me was torn away, like a part of the old me is missing."
        "Something that I continue to want to get back. But no matter how hard I try I just can’t."
        r "I’m glad that you can understand,  but I am sad that you can relate. It would be nice if everyone never lost their passions. To me losing my passion felt like I had lost a part of myself."
        r "It made me feel like a damaged person, and I kept questioning myself why I was being different. We are almost at the cabin but thank you, I appreciate it."
        jump choice_4_done
    
    label choice_4_done:
        play music "audio/sad_piano_track_6.ogg" volume 0.5 fadein 1 fadeout 1 loop
        "After a few seconds of us silently walking through the forest, twigs breaking under our feet, our shoes getting dirtier by the damp soil. A howl similar to that which I’ve used to escape from Tray echoed throughout the woods again."
        play sound "audio/Howl4.ogg" volume 1
        "This time the sound wrapped through my skull, it felt much more intense and much closer. My legs started to twitch from the fear, my eyes gazing all around hoping to not see the source of the noises."
        "The red scarf girl had noticed my twitching and looking around, she pointed behind me and when I averted my gaze to what laid there, I saw two bright yellow eyes. Eyes of death hungry not just for the meat on my bones but eager to ravage my soul."
        r "Listen to me Blue shirt, we will be in trouble if we are caught, I want you to go run as fast as possible with that hurt ankle, in the direction that we have been heading in. You will see the cabin, go inside, and you should see a ladder heading up into the attic."
        r "Go there now, I will distract these dogs. Trust me, go!"

    menu choice_5:
        "Trust":
            python:
                choices.append("Trust")
                relantionship += 10
                choicesMade["5a"] = True
                ghostStats['happiness'] += 5
                ghostStats['strength'] += 5
                ghostStats['trust'] += 5
                ghostStats['anger'] -= 2
                ghostStats['anxiety'] -= 5
                trueChoices[4] = "Trust"

            jump choice_5_trust

        "Distrust":
            python:
                choices.append("Distrust")
                relantionship -= 10
                choicesMade["5b"] = True
                ghostStats['happiness'] -= 2
                ghostStats['strength'] -= 2
                ghostStats['trust'] -= 5
                ghostStats['anger'] += 5
                ghostStats['anxiety'] += 2
                ghostStats['helped'] -= 2
                trueChoices[4] = "Distrust"
            
            jump choice_5_distrust
    
    label choice_5_trust:
        mc "Okay I trust you"
        $ trust = True
        jump choice_5_done

    label choice_5_distrust:
        mc "No, I don’t trust you, what if something happens?"
        "As soon as those words left my mouth a growling vicious-looking dog emerged from behind me. Its eyes full of lust for meat, awaiting its turn to attack."
        play sound "audio/Howl1.ogg" volume 1
        r "If you don’t leave right now you’ll be a dogs chew toy, so go!"
        "No more words of encouragement were needed, I had to trust her and with that, I limped out of her way as fast as my legs would carry me."
        $ trust = False
        jump choice_5_done

    label choice_5_done:
        "With those words, I limped as quickly as possible ahead. As I departed I looked back to notice a big wide smile on the girl’s face, the further I got, the less I saw until the only thing that I could see was her red scarf in the distance."
    
    "Movement occurred, but I could not recognize what was happening. Loud howls echoed through the woods as I limped further and further until I finally reached a cabin that looked more like a shack where a single step inside it would bring it crashing down."
    "Nevertheless, I had to trust her and looked for the attic ladder she had mentioned and climbed my way up. I was very thankful that the ladder didn’t break under me and that my ankle was able to take all of that pressure."
    "Pain was the last thing that I needed more of. I was all out of breath, wondering if the girl was going to be okay. Each second felt like an hour. What was I going to do without her? How would I get back?"
    "Would I be able to live with the fact that a girl could have given up her life for me?"
    r "You’re whimpering like a scared little puppy, don’t worry everything is okay."
    play music "audio/Beautiful-Splatter-Invadable-Harmony.ogg" volume 1.0 fadein 1 fadeout 1 loop

    if trust:
        r "Thanks for trusting me by the way"
    else:
        r "Would have certainly been easier if you had just trusted me."
        if ghostStats['trust'] <= 50:
            jump end_distrust
    
    
    r "Hmm, let’s see, I could swear that there was a first aid box somewhere around here, oh yeah there it is."
    "After finally being able to calm down and realize that the girl was okay, I finally had the chance to notice where I was. A low wooden ceiling that did not offer much protection. If the girl stayed here during the night, the scarf would start to make more sense, it was starting to get chilly."
    "The attic space showed no signs of being used, no place for a bed, absolutely nothing lying around. Just an empty hollow room that would have been swallowed in darkness if it was not for a tiny circle window that allowed some moonlight to enter through its mouth."
    mc "How did you manage to escape?"
    r "Ah Blue shirt does not want nay plot holes, well I just made those dogs feel scared, I asserted my dominance and threw some rocks. Just needed you to leave because it is embarrassing to do and there is no way that you could ever pull of dominance."
    r "Now no more questions, get yourself patched up, there are some bandages in that aid box over there."

    #Chapter 3
    scene act3 with Dissolve(1.0)
    pause .5
    scene bg room with Dissolve(1.0)
    pause .5
    "She must have enjoyed calling me ‘Blue Shirt’, although it is true that neither one of us had introduced ourselves to one another. I guess that if I had worn any other t-shirt that day then I would have been called by that colour instead."
    "The sense of urgency of it all just left us without much time or care towards names. We just went along with everything, both of our social skills must have needed a little help. To me, she’s just a weird girl that found me in the forest at a time of need,"
    " a girl with a red scarf, a girl that gives me hope and helps me survive right now."
    "Finding the bandage in the first aid box was an easy task. Most of the other items were missing, but luckily I was able to use the bandages. Had I injured something else and required other items I would have been out of luck."
    "Thankfully upon closer inspection of my ankle, I noticed that although I had put plenty of pressure on it while running over here, it was not bruised nor had grown in size. Although a small victory still a victory that gave me hope that I very much needed."
    mc "You know it is kinda funny that I haven’t even asked for your name yet even after you have helped me so much."
    r "Oh Uhm yeah, you are right, it is a little funny, I guess I just enjoyed calling you Blue Shirt. I haven’t talked with anyone for a long time, most people don’t even notice me."
    "Yeah, she definitely needed some work with her social skills, she hadn’t even given me her name even after I asked. But oh well I guess I will take the lead."

    menu choice_6:
        "Nice":
            python:
                choices.append("Nice")
                relantionship += 5
                choicesMade["6a"] = True
                ghostStats['happiness'] += 5
                ghostStats['strength'] += 2
                ghostStats['trust'] += 2
                ghostStats['anger'] -= 5
                ghostStats['anxiety'] -= 5
                ghostStats['helped'] += 2
                ghostStats['hurt'] -= 5
                trueChoices[5] = "Nice"
                
            
            jump choice_6_nice

        "Dismiss":
            python:
                choices.append("Dismiss")
                relantionship -= 5
                choicesMade["6b"] = True
                ghostStats['happiness'] -= 2
                ghostStats['strength'] -= 2
                ghostStats['trust'] -= 2
                ghostStats['anxiety'] += 5
                ghostStats['helped'] -= 2
                ghostStats['hurt'] += 2
                trueChoices[5] = "Dismiss"
            
            jump choice_6_dismiss

    label choice_6_nice:
        python:
            name = renpy.input("What's your name?")
            name = name.strip() or "MC"
        
        mc "My name is [name], it is very nice to meet you. I’m very thankful for all of your help so far. What’s your name?"
        r "Oh yeah sorry for not introducing myself, people used to call me Sam. It’s nice to meet you Blue Shirt."
        mc "You’re not going to drop the Blue Shirt name huh?"
        R "Nope I like it."
        mc "I guess I have no choice in this matter."
        "Well I didn’t get rid of the Blue Shirt nickname, but at least I got to find out her real name. Weirdly though when she said her name, it looked like it was causing her some pain."
        mc "My ankle is a bit better, any idea where we can go to find out where the camp is?"
        jump choice_6_done
    
    label choice_6_dismiss:
        mc "Never mind forget it, names aren’t important, it doesn’t matter."
        r "I think that you’re right, most people never used my name anyway, and those who did went onto forget it. Still, though my name is Sam. I haven’t been called y it in ages, so I don’t associate myself with it any more, but you’re free to use it if you want Blue Shirt."
        "I guess I’ll be keeping the Blue Shirt nickname. Not only that, but I need to figure out how to get back to camp."
        mc "I think that my ankle is a little better, any idea where we can go to find out where the camp is?"
        jump choice_6_done
    
    label choice_6_done:
        R "I don’t know Blue Shirt, I don’t think that there is any hope in getting back to where you came from. Do you even want to return to a place that hurt you? Don’t you think that the pain will just happen again, over and over?"
        R "I think that it is pretty hopeless, will people even look for you? Does anyone care?"
    
    menu choice_7:
        "Hopeful":
            python:
                choices.append("Hopeful")
                relantionship += 5
                choicesMade["7a"] = True
                ghostStats['happiness'] += 2
                ghostStats['strength'] += 5
                ghostStats['trust'] += 2
                ghostStats['anxiety'] -= 2
                ghostStats['hurt'] -= 5
                trueChoices[6] = "Hopeful"

            jump choice_7_hopeful

        "Anger":
            python:
                choices.append("Anger")
                relantionship -= 5
                choicesMade["7b"] = True
                ghostStats['happiness'] -= 5
                ghostStats['trust'] -= 2
                ghostStats['anger'] += 5
                ghostStats['anxiety'] += 5
                trueChoices[6] = "Anger"

            jump choice_7_anger

        "Optimistic":
            python:
                choices.append("Optimistic")
                relantionship += 3
                ghostStats['happiness'] += 2
                ghostStats['strength'] += 5
                ghostStats['trust'] += 5
                ghostStats['anger'] -= 2
                ghostStats['anxiety'] -= 5
                ghostStats['helped'] += 2
                ghostStats['hurt'] -= 5
                trueChoices[6] = "Optimistic"

            jump choice_7_optimistic
    
    label choice_7_hopeful:
        mc "I can’t just lose hope now. Things are bad, I know that, but I can’t just give up. Even if no one would come looking for me. Even if there isn’t anyone that cares, I have to keep fighting. Life can always get better even if it may not seem that way,"
        mc "even if I don’t know what’s to come, I want my future to be better even if I have to fight for it."
        R "Why fight for a future with more pain in it?  Even if there are good things to come, the bad overshadows it. Isn’t it easier to give up now to give up on the pain?"
        "Although still maintaining that smile of hers, her voice trembled."
        R "What if you can’t save yourself?"
        mc "I don’t think that most of us can do this alone, I can’t beat my problems alone. I need help from others, but I won’t ever get that help if I don’t try if I don’t ask for it. I have to take the first step. I can’t do this alone. So Sam please help me. Please help me return home."
        "That was the first time that I saw her face without s smile, without a mask on. Her sad glistening eyes now matched the rest of her face. A single tear rolled down her cheek. This was the true Sam in front of me."
        "It only lasted a few seconds that I would see her like that. Looking into her eyes full of despair felt like hours had been lost,"
        "it felt like a lot was still unexplained a lot more tears were built up, still yet to drop. But that single droplet was all I was going to get out of her today. She quickly composed herself, the mask wasn’t shattered yet, it was still capable of hiding her emotions."
        R "Okay Blue Shirt, I’ll give you my all to help you."
        jump choice_7_done
    
    label choice_7_anger:
        mc "I don’t care if anyone cares about me or not. I am not living my life for others, I am not going to let anyone ruin my life. If I have to go through some pain to live then I will. Yeah, it hurts to live like this. Hurts to have to face life alone."
        mc "But life isn't fair, it was never fair and never will be fair. Just get over it. Being just sad about things won’t help. It doesn’t help you, doesn’t help me. Doesn’t help anyone. Let’s just focus on getting me home."
        "Once again she had that smile on her face, the smile that she uses to hide behind. Caring about every little thing won’t help anyone. I don't need her help to get home, I can't be too far."
        R "Fine, I'll help you"
        jump choice_7_done
    
    label choice_7_optimistic:
        mc "Some people care about me. People will come to look for me. I know that I was hurt and may be hurt again, but there are people out there that love me and need me. A few bullies won't stop me from living my life."
        mc "I got hurt physically, but mentally I am still strong. Those bullies just have their problems and used me to deal with them."
        mc "I don’t think that bad people mean to be bad. They are just people with issues trying to solve them in evil ways, but they aren’t evil. Our society just can’t deal with them properly yet."
        "As I was saying those words, Sam’s smile changed, she didn’t lose her smile, it just changed. This changed wasn’t permanent, it only lasted a little while, but for that while, it just felt genuine that it was hard not to smile myself."
        R "You are way too optimistic about the world, you’re a big dumbass but the world needs more people like you. I may not completely agree with you but hey I will help you get back home if you want my help."
        jump choice_7_done

    label choice_7_done:
        "Hmm, how would I get back to the camp without knowing in which direction it is or anything. The dog chase got both of us very disoriented. I didn’t have the faintest of clues, but if I got to some high point then maybe I would be able to see it,"
        "I just need to find the lake, and then I would be set and should be able to get back."
    
    mc "I think that our best bet is to get to some high ground to find out where the lake is. Finding the lake will make it much easier to find the camp. Do you know what place where we would have a view of the surrounding area?"
    R "Yeah good idea, I don’t think that it should be too hard to climb up a hill and get a view of the surroundings, alternatively though, you could just climb one of the trees, if you know how to climb them that is, along with a bad ankle of course."
    mc "Well hill it is then since I don’t know how to climb trees and a bad ankle would make things way too hard to learn now."

    #Chapter 4
    scene act4 with Dissolve(1.0)
    pause .5
    scene bg room with Dissolve(1.0)
    pause .5
    "It was finally time to leave the attic, time to set off home. A sense of hope washed over me, it was always noise to have a plan, hopefully, there will be no more encounters with any wildlife. As we departed from the shack, we were both illuminated under the night sky."
    "It wasn’t a typical skyline where all the stars were covered by clouds, only peeking from time to time like we had been used to. No, tonight was different, there wasn’t a single cloud in the sky, no light pollution, just tonnes of sparkling stars in the sky surrounding a large hypnotizing full moon."
    "Tonight was special. The only tall hill that would allow us to see the surrounding area that Sam knew of was about a few minutes walk from where we were. With my ankle, it would take a bit longer but shouldn’t have too much of an impact."
    "Thankfully my ankle was recovering. Sam started skipping along ahead of me. How did she have so much energy to skip. I have no idea. It made me realize that I didn’t even know what time it could possibly be."
    "How long was I out for initially, how long had I spent with Sam, time was all a blur. Only the moon directly above us gave some sort of sense of time."
    R "It really is a beautiful night, you picked the best night to be bullied on. Nights like these used to be the best for getting rid of all the stress. For a while it used to help so much, yet ended up causing all the problems in the end."
    "Her voice trembled with the delivery of that last line. Sam was still a large mystery to me, sometimes she would talk about the forest with so much passion and love, but that passion would turn to sadness and despair very easily. The forest helped her a lot but also caused her the most problems."
    R "I used to feel so motivated, so hopeful, so full of life. I used to want to become an environmentalist to help protect this forest and many forests like it, forests that helped other people like me. Those times were much better."
    mc "What happened that made you change your mind? At times, you’re in love with this forest and at other times, the forest seems to almost bring you to tears."
    R "I don’t want to talk about it too much, because the reason is weird. I wish that I had a particular reason and could just blame it all on that. But I don’t have that. I have nothing to blame, it all just happened, no cause and effect, just bam there you go all of your feelings."
    R "Suddenly you no longer care, suddenly there is nothing that makes you feel any more if you try really hard then you’ll manage to make yourself feel pain. For some reason after not feeling anything but guilt for a while that pain seduces you, makes you want more."
    R "For a few seconds, you feel alive and happy, but after you’re left with guilt and more self-hate. You try to get that passion for things back, even trying to get that passion back in itself is difficult, and after pushing yourself so hard, only to not be able to get it back hurts a lot."
    R "It brings intense numbness. Have you ever felt so numb, where you would try anything to feel again?"

    menu choice_8:
        "Yes":
            python:
                choices.append("Yes")
                relantionship += 5
                choicesMade["8"] = True
                ghostStats['happiness'] += 2
                ghostStats['strength'] += 5
                ghostStats['anxiety'] -= 5
                trueChoices[7] = "Yes"

            jump choice_8_yes

        "Somewhat":
            python:
                choices.append("Somewhat")
                relantionship += 2
                choicesMade["8"] = True
                ghostStats['happiness'] += 2
                ghostStats['strength'] += 2
                trueChoices[7] = "Somewhat"

            jump choice_8_somwhat

        "No":
            python:
                choices.append("No")
                relantionship += 2
                choicesMade["8"] = True
                ghostStats['happiness'] += 2
                ghostStats['anxiety'] += 2
                trueChoices[7] = "No"

            jump choice_8_no
    
    label choice_8_yes:
        mc "Yeah, I’ve been feeling numb a lot lately. It sucks when you know how you should be feeling in certain situations, but you just don’t feel that way. Sometimes you just fake it to seem normal, but it hurts on the inside that you can’t feel what you should be feeling."
        jump choice_8_done

    label choice_8_somwhat:
        mc "I’ve only felt numb a few times. Thankfully it goes away after a while but there are moments when I know that I should be feeling a certain way, but I just can't process any emotions. It does suck."
        jump choice_8_done
    
    label choice_8_no:
        mc "Thankfully, I’ve never felt like that, sometimes sure when you’re shocked and try to process things, but eventually it all catches up with me. But I can't imagine how bad it must be to feel like that all the time."
        jump choice_8_done
    
    label choice_8_done:
        R "Yeah it certainly isn’t nice. It all just makes you want to blame yourself, there is nothing else to blame, so it must be me. That blame against yourself, it hurts your body a lot, it stops you from sleeping at night while also making you tired and wanting to stay in bed all the time."
    
    R "You end up not having any energy to do anything, you either eat nothing or eat too much which just brings you more self-hate. But while all of this is happening you don’t want to worry those around you, you don’t want them to worry about you."
    R "You don’t feel like your life is important enough to bring those that care worries and stress. You lose all control of your life. So, the main reason for my love-hate with the forest is that I don’t know."
    "There was no more skipping from Sam after that, no more smile to brighten up that face. Just a neutral walk with a neutral expression. Like her body had been reminded of the past which brought enough horror to her that her body was no longer able to put up her mask to the world."
    "She had to recover before she could function again."
    mc "I guess that’s why we put on a brave face, why we act like nothing is wrong, we don’t want anyone to feel the same kind of pain that we are feeling. We don’t want them to know how much pain we are in."
    R "Hiding it, and appearing fine is so hard sometimes, makes you want people to forget about you, makes you wish that you weren’t around so that none of your pain can be brought onto others."
    "The only image left were two people walking slowly, one in front of the other. Tough words have been said. A moment of peace was needed, a moment to take our minds off everything."
    mc "The stars are so pretty tonight, I wish we could just lay here and enjoy them for a while. To forget about everything, to get a little life back."
    "Keeping my eyes open got harder and harder each second. The difference between having my eyes opened and closed was becoming less and less noticeable. Every time that I blinked my eyes remained closed for longer. What would it be like at home if I never returned?"
    "Would they be sad without me around?  They did send me away. Mom would be heartbroken. She always tried to be tough to protect us. She didn’t often cry but when she did it felt as if the world was drowning in sorrows."
    "Mom didn’t want us to worry about her, so she always hid her tears, didn't want to make us sad. Overworking herself each night so that everything was okay. Never taking a day off. Mom would feel like she had failed her duty to protect me."
    "What about Dad? He always had his moments of anger, an anger that existed out of care for us. He always wanted all of us to be happy and carried us on his back."
    "His face was always the same, drained eyes and an expressionless look. He needed to appear tough so that we could all lean against him. I don’t think that I had ever seen him cry. He made us believe that he wasn’t even capable of it."
    "Would he be sad if I never came back? Maybe things would be easier without me, maybe without the burden of my existence, everyone would get along better. Would I be sad if I didn’t get back? Do I still have a place to come back to? What if they don’t want me to come back?"
    R "You sure were very weird. I guess you’re not used to amazing night-time adventures with someone as great as me."
    "I had not realized it until now but the entire time, my eyes were closed. I left the world for the land of the stars."
    mc "What happened?"
    R "Well Blue Shirt, I was just minding my own business. When I heard a loud thud sound and the next thing I know is that you’re just lying there on the ground enjoying your sleep time. You didn’t even invite me to join."
    "It wasn’t easy getting off the grass back onto my feet. The grass pulling me back to dreamland, soothing me, and although I was dreaming about negative thoughts I still wanted to return. Pulling off from the ground felt like a connection was being severed."
    "Goodbye dreamland, goodbye land full of glistening stars, it’s time to get back to the travels."
    R "Hey I just want you to know that I am sorry about all these things that you have to go through, it must be hard and tiring. But hey look, we are almost there just a few more minutes."
    "Sam was correct, right in front of us was the base of a tall hill, just a few more steps before the hill would open our view from the shackles of the surrounding trees. The inclination increased with each step, each step was more difficult to make than the one before."
    "For the first time, I wasn’t sure if a tree wasn’t easier to climb."
    mc "Geez you certainly picked a steep hill."
    R "Only for you. Although I don’t remember it being this steep, this is the only spot that escapes these trees, there is no other nearby point high enough that I know of."
    "Soon I would discover Sam’s biggest secret. The hill that we were almost climbing at this point was known to the locals as the Truth Seeker. A place that would one way or another be the cause to reveal all major secrets, and Sam’s secret was a big one."

    #Chapter 5
    scene act5 with Dissolve(1.0)
    pause .5
    scene bg room with Dissolve(1.0)
    pause .5
    R "We are almost…"
    "As soon as those words escaped her mouth, her foot failed to maintain balance and with one slip she came tumbling down towards me. At first, I thought that it would only be a slight problem, that I would be able to catch her."
    "But when I laid out my hands and arms to prepare myself to catch her, I discovered the real problem. Her body did not make an impact against me, it did not stop, I felt a cold shiver right as her body passed through mine."
    mc "What the?"
    "That was all my mouth could say as my brain realized that this girl had just passed through me. What kind of magic was this? How tired was I? Her body did not fall too far, stopping slightly behind me."
    R "Oops, that wasn’t supposed to happen, anyway, let’s keep going shall we?"
    mc "No no, wait for a second, what just happened? You need to explain yourself, Sam."
    R "But Blue Shirt, it isn’t important, plus we have to get to the top of this hill and get you back as fast as possible."

    menu choice_9:
        "Please Sam, I would really like to know what is up with you. I don’t understand what just happened.":
            python:
                choices.append("Pressure")
                relantionship += 2
                choicesMade["9a"] = True
                ghostStats['happiness'] += 5
                ghostStats['trust'] -= 5
                ghostStats['anger'] += 5
                ghostStats['anxiety'] += 5
                ghostStats['helped'] -= 5
                ghostStats['hurt'] += 5
                trueChoices[8] = "Pressure"

            jump choice_9_1

        "I’m sorry I’m just confused about what just happened. If you are comfortable, could you tell me about it?":
            python:
                choices.append("Careful")
                relantionship += 5
                choicesMade["9b"] = True
                ghostStats['happiness'] += 5
                ghostStats['strength'] += 5
                ghostStats['trust'] += 5
                ghostStats['anger'] -= 5
                ghostStats['anxiety'] -= 5
                ghostStats['helped'] += 5
                ghostStats['hurt'] -= 5
                trueChoices[8] = "Careful"
                

            jump choice_9_2

        "Sam tell me what just happened. I deserve to know what you just did to me.":
            python:
                choices.append("Pushing")
                relantionship -= 5
                choicesMade["9c"] = True
                ghostStats['happiness'] -= 5
                ghostStats['anger'] += 2
                ghostStats['anxiety'] += 10
                ghostStats['helped'] -= 5
                ghostStats['hurt'] -= 2
                trueChoices[8] = "Pushing"

            jump choice_9_3
    
    label choice_9_1:
        jump choice_9_done

    label choice_9_2:
        jump choice_9_done
    
    label choice_9_3:
        if ghostStats['anger'] > 30 and ghostStats['trust'] < 40:
            jump end_hill
        else:
            jump choice_9_done
    
    label choice_9_done:
        R "Fine, okay I will tell you everything, le’s just get to the top of this hill first, it’s not much longer, and I think that it will be much easier to do it there. I also need time to think through it."
    
    play music "audio/ForeverLost.ogg" volume 0.5 fadein 1 fadeout 1 loop
    "The next five minutes were filled with dead silence. The only audible noises were our shoes stomping on the ground below as we tried to maintain balance. I tried to think about all the other times that Sam had touched, when I first fell while running from the bullies,"
    "I almost fell onto her, but I wasn’t conscience back then, when we first met she sat away from me and didn’t touch me at all, neither did she touch me during the dog ambush. She also told me to bandage myself. She had always skipped ahead of me, only ever slowing down and turning around to talk to me."
    "Was there something wrong with her or me? As we near the top, I noticed Sam’s face, she wasn’t hiding her emotions, there was no smile, just sadness and worry. The top of the hill was way brighter than any other location that we had been to thus far."
    "It was free from all the sheltering trees. The dark sky, the bright stars, the shining moon were all perfectly fully visible and glancing at us for the tree’s protection as now gone. I looked across the horizon, for a second I was scared because all I could see was a large dense forest."
    "But then as I looked towards the direction of the moon, I finally saw it. A glistening body of water, if it wasn’t for the lake I would have never noticed those dark cabins to the side of it. There wasn’t a single light on, so I would have to follow the moon to be able to get back."
    "I turned around to tell Sam that I had just found the camp only to see her saddening face, a tear rolling down her cheek."
    R "I guess it’s time for me to tell you everything now. I don’t remember too much about my life. I was an ordinary kid that loved being out in nature, especially this forest, painting and drawing the landscape or just running around. It was my biggest passion."
    R "I had other passions besides that of course, but this forest was the main one. Every summer my family and I would travel here, stay out camping and just enjoy life. Just a family tradition that was passed down through generations. It was my favourite time of life, the family being together all happy,"
    R "they would all focus on me, and we would have painting sessions together. We would take loads of photos and just smile a lot. As I grew older my passions changed but this forest remained. It was more of a home for me than my own house."
    R "Then all of a sudden I just slowly started losing interest in all of my passions. I had trouble with sleep, with eating, with being happy."
    R "Sure there were stressful things going on in my life. The family wasn’t the best, I wasn’t doing too well in school any more. I was just left with one single piece of hope for me and my family and that was going camping in this forest over the summer. However, we had to skip that year."
    R "Mother wasn’t feeling too well and dad was just too busy at work to make any time for us. I clawed onto this one hope for the next year to come. I hated that year, I felt like a husk, I couldn’t feel anything and hated myself for that, but I couldn’t let anyone worry about me, they all had plenty of problems themselves,"
    R "I didn’t want to add to them, so I just put on a happy face and pretended that everything was okay while crying all night. I think that my parents must have noticed that something was up because they announced that we would be going camping that summer,"
    R "that dad would take time off work and that mother was feeling well enough for it."
    R "At the time it was two months away, but it gave me so much hope, and honestly, it was the only thing keeping me alive. I thought that one visit to the forest would help me with all of my problems that it would suddenly just fill me with joy. Mother was even feeling a little better during that time too."
    R "When we finally got to the forest though I realized that I had no passion for it. I looked forward to being together once again, but that feeling was left unfulfilled. I felt hollow."
    R "It wasn’t all that bad until Dad got a work call, and told us that we would have to go back because it was important, and he could just not miss out on it. Dad was once again leaving us and mother wouldn’t say anything."
    R "I couldn’t control myself at that point any more, all the emotions that were being held back erupted and came flying out, and I let it all out on them, yelling at them both."
    R "At dad for only caring about money and not taking care of mom when she needed comfort the most, and for mom not doing anything about my dad, for being a pushover and doing nothing for herself or the family."
    R "I couldn’t take it any more and just ran out crying. I hated everything that had just happened. I regretted it the second that it happened, but I couldn’t get myself to come back."
    R "Life was so unfair. But I wanted to calm down and return. A part of me felt fantastic for letting things go. I finally felt alive after almost two years. As I walked back I noticed the heart rising around me."
    
    play sound "audio/ForestFire.ogg" volume 0.2
    
    R "There was a forest fire going off strongly right where mom and dad were. I had only been gone for about an hour, I didn’t know if they were okay or not, but I had to run away, getting caught up in the flames and smoke would have been the end of me."
    R "I ran as fast as I could. I had to get away and find my parents. The fire was spreading at a high rate, it was almost impossible to see anything, shades of red and orange just engulfed the atmosphere."
    R "While I was running disoriented, the ground below me collapsed and send me crashing down to some deep unused well. The fall had knocked me out and when I came to, it was already dark."
    R "I wanted to get up and potentially climb out, but my leg was broken by the fall, and it was hard to breathe. I couldn’t move out of there, I was trapped. Not only that, but I spent hours crying and shouting for help until I lost all of my voice. No one ever came for me."
    R "I remember passing out and feeling full of regret. I awoke in the burnt down forest, I thought that someone had found me and rescued me, but there was no one to be found."
    R "I was feeling completely okay. I thought that maybe I just passed out, and it had all been a bad nightmare, so I went looking for people. Everyone that I met would just ignore me, after a few hours I got tired and thought that I was going to force someone to listen to me,"
    R "but I couldn’t touch anyone I just went through them. People just passed through me and no one could hear me. I realized that I must have died that night, that it wasn’t a dream, that life was over, and I was just a wandering spirit or ghost now."
    R "It was like that for a long time, just walking about in the forest, observing random things. Once you get used to passing time it gets easier. Days end up passing as fast as seconds, weeks passed like hours and years passed like days."
    R "It was becoming hell, then one day I saw you tumble down that hill, things didn’t look okay for you,"
    R "so I decided to stick around to see what you would do. I was very surprised when you started talking back to me, that fact that you could see me and hear me cheered me up. It had been such a long time since I’ve talked to another person and not just myself."
    mc "Wow that is a lot to process."
    R "I know Blue Shirt, I am sorry that I didn’t tell you sooner, I just felt like there was never a good time to blurt it out."
    "Tears were running down her face, dripping onto the grass below. She had become the most beautiful waterfall."
    R "It’s too much to think about. I had held it down for so long. I can’t take it."
    "Each sentence took longer to leave her mind. Each in between sobs."
    R "I just feel everything and nothing at the same time. I just can’t."
    "She collapsed onto her knees, crying and sobbing. It was hard not to do anything. I wanted to hug her so hard. I wanted to hold her and tell her that everything was going to be okay."
    "A part of me related to her heavily. I’ve held in emotions a lot too. When they suddenly come crashing out it overwhelms you and leaves you crushed."
    R "It’s so difficult. I know that I am crying here in front of you, and I’m really sorry about that but at the same time, I don't feel anything. I’m so numb and overwhelmed."
    menu choice_9_5:
        "Relate, Understanding":
            mc "It’s okay don’t worry I understand you, I’ve felt like that before. Just overwhelmed and so emotional but just not feeling anything. People have tried to console me in that state, but it’s just like I understand that you’re worried about me, but I just can’t emotionally feel it."
            python:
                choices.append("Understanding")
                relantionship += 5
                choicesMade["10a"] = True
                ghostStats['happiness'] += 2
                ghostStats['strength'] += 5
                ghostStats['trust'] += 5
                ghostStats['anger'] -= 5
                ghostStats['anxiety'] -= 5
                ghostStats['helped'] += 2
                ghostStats['hurt'] -= 2
                trueChoices[9] = "Understanding"

            jump choice_9_5_1

        "Sorry, Can't imagine how you're feeling.":
            mc "I can’t imagine how you’re feeling. I am sorry for making you let all of that pain out."
            python:
                choices.append("Apologetic")
                relantionship += 5
                choicesMade["10b"] = True
                ghostStats['happiness'] += 2
                ghostStats['strength'] += 5
                ghostStats['trust'] += 5
                ghostStats['anger'] -= 5
                ghostStats['anxiety'] -= 5
                ghostStats['helped'] += 2
                ghostStats['hurt'] -= 2
                trueChoices[9] = "Apologetic"
            
            jump choice_9_5_2
        
        "Get over it":
            mc "Listen can you get over it. We need to head on, we don’t have the entire night."
            python:
                choices.append("Get over it")
                relantionship -= 5
                choicesMade["10c"] = True
                ghostStats['happiness'] -= 5
                ghostStats['strength'] -= 5
                ghostStats['trust'] -= 5
                ghostStats['anger'] += 2
                ghostStats['anxiety'] += 2
                ghostStats['helped'] -= 2
                ghostStats['hurt'] += 5
                trueChoices[9] = "Getoverit"
            
            jump choice_9_5_3

    label choice_9_5_1:
        R "Just give me some time, I’ll be fine don’t worry. I have gone through worse before."
        "At the end of that sentence she tried really hard to let out a smile, but her body had failed her. It was too tired to fake any sort of positive emotion."
        jump choice_9_5_done
    
    label choice_9_5_2:
        R "Just give me some time, I’ll be fine don’t worry. I have gone through worse before. It isn’t your fault."
        "At the end of that sentence she tried really hard to let out a smile, but her body had failed her. It was too tired to fake any sort of positive emotion."
        jump choice_9_5_done

    label choice_9_5_3:
        R "Yeah sure, just give me some time to recover."
        jump choice_9_5_done

    label choice_9_5_done:
        "We sat around at the top of the hill taking in the environment. We felt like we were on top of the world being able to see the entire landscape out in front of us. The sun was going to be rising soon. Filling the world with red, orange, and yellow colours of warmth."
    
    R "You know, this would be very romantic if it wasn’t for the fact that I am dead and stuff."
    mc "Oh absolutely so romantic. Sitting on the top of a hill in our tears watching the sunrise together while being sleep-deprived."
    "Sam was back to normal for now. We could set out now onto our journey, but where should we go?"
                
    menu choice_10:
        "I just want to get home, I don't wish to help her":
            python:
                choices.append("Focus getting Home")
                relantionship -= 5
                ghostStats['happiness'] -= 2
                ghostStats['strength'] -= 2
                ghostStats['trust'] -= 2
                ghostStats['anger'] += 2
                ghostStats['helped'] -= 2
                ghostStats['hurt'] += 5
                trueChoices[10] = "FocusgettingHome"
            
            jump choice_10_home

        "Focus on helping Sam, with the chance that I may not be able to get home":
            python:
                choices.append("Focus on Sam")
                relantionship += 10
                ghostStats['happiness'] += 10
                ghostStats['strength'] += 5
                ghostStats['trust'] += 10
                ghostStats['anger'] -= 5
                ghostStats['anxiety'] -= 2
                ghostStats['helped'] += 10
                ghostStats['hurt'] -= 10
                trueChoices[10] = "FocusonSam"

            jump choice_10_sam

    label choice_10_home:
        mc "Well what has happened to you sucks but now that we know where the camp is I think that we should focus on getting me back home."
        R "Oh I see, well since you know the way back I think that this is where we should separate. I feel like I have been fair to you and understanding enough, but you have not treated me with respect. So, good luck getting back home, I hope that we will never meet again."
        "There was nothing that I could say or do to get Sam to stay with me. I guess that I will have to finish this journey by myself."
        jump choice_10_end
    
    label choice_10_sam:
        mc "You mentioned that the last thing that you remembered was falling into some kind of hole after the ground broke beneath you near the lake right? Since we’re heading in that direction anyway, would you like to come with me to see if we can find it?"
        R "I think that I would like that, I’ve never searched for it myself, I have been too afraid of what I might find. I’m scared, I don’t want to see my body but feel like it might be the key to passing onto the next life."
        jump choice_10_done
    
    label choice_10_done:
        #Chapter 6
    
    scene act6 with Dissolve(1.0)
    pause .5
    scene bg room with Dissolve(1.0)
    pause .5
    "We set off onto the final stretch of our journey, a lot of things had been said. They were all stuck in my head, and it would be awhile before I could process everything properly. It did make me question my sanity among other things,"
    "but it had been a long night, accepting supernatural events was easier than you’d think when you’re very heavily sleep-deprived."
    "I kind of let logic go away and embraced Sam’s words for the truth. It was now downhill towards the truth and back home. The horizon had begun to tear away, allowing for some of the rising sun’s light to emanate into the world."
    R "I miss my Mom and Dad. I tried looking for them after I awoke. But I never found them. I never even heard a thing about them. The thought that they had lost their daughter either to a fire or potentially hoping that she had run off and started a new life, was just heartbreaking to me."
    mc "Did you find anything at the place you guys were camping at?"
    R "Just ashes. The whole part of being born again as a spirit must have taken a while. Somehow I never managed to leave this forest. I did try but whenever I would head in a direction that I knew would lead me out, the forest would just keep going without ending."
    R "Maybe I am cursed to this place? Maybe I am tied to my body?  I don’t know, we are dealing with the weird paranormal here. I don’t live in reality but in fiction. Not only that, but I really miss them and wish that the last memory of me wouldn’t be me running away from them. It’s been too long now."
    R "The chances that they are alive are very slim. I used to read every single newspaper that I would find in hopes of maybe hearing something about them, but newspapers rarely have any good news, it was becoming depressing to read. Plus it's not common to bring newspaper to a random forest in the middle of nowhere."
    R "Do you miss your parents?"
    menu choice_11:
        "Yeah, I do.":
            python:
                choices.append("Miss Parents")
                relantionship += 2
                ghostStats['happiness'] += 5
                ghostStats['strength'] += 2
                ghostStats['trust'] += 5
                trueChoices[11] = "MissParents"

            jump choice_11_1

        "Not really.":
            python:
                choices.append("Doesn't miss parents")
                relantionship -= 2
                ghostStats['happiness'] -= 2
                ghostStats['strength'] += 2
                ghostStats['trust'] += 5
                trueChoices[11] = "Doesntmissparents"

            jump choice_11_2
    
    label choice_11_1:
        mc "Yeah, I do. I know that it’s only been a day since I last got to see them but life at home has been weird for a while. They haven’t been their old selves because of the stress they are under."
        mc "I wish that there was something that I could do to help them, I really worry that I am just taking up space and not helping in any way."
        jump choice_11_done

    label choice_11_2:
        mc "Not really. They have been going through a lot and don’t pay attention to me or what I need at all. The reason I am here is because of them, because they could no longer take proper care of me and needed time without me. It hurts."
        jump choice_11_done

    label choice_11_done:
        R "I think that it is important to remember that they won’t be with us forever. One day we will lose them and most of us won’t know that day in advanced."
        R "Had I known things would have turned that way I would have told them about my emotions and my state while I was still in control. Not in some random outburst."

    mc "I know, it’s just sometimes you get tired of being the bigger person. You want them to take you seriously. You want them to listen. They are great parents they just have a lot on their plate. I just don’t want to be robbed of my future because of them. If they mess up their life, they mess up mine too."     
    R "I robbed myself of my future. I don’t know how that fire started. I don’t really blame it either, I blame myself for everything. I don’t even know if I wanted a future back then. I wish for a future now, but I know that is no longer possible."
    R "I think that now I just want to be able to pass on. Living like this is not what I want."
    "The walk downhill was much easier physically, but emotionally it had been much tougher. Sam was having a hard time keeping everything together. A mask of fake emotions was no longer possible for now. All the raw emotions were out there to deal with now."    
    R "What if the hole doesn’t even exist any more, don’t you think that someone would have found me by now, and we are just wasting our time searching? What if finding my body doesn’t change anything, and I’ll still be stuck in this world?"
    mc "Well, I think that maybe the hole got covered over, there would have been a lot of ash after a fire. Mabe some logs fell over and covered it? I don’t know, but I don’t think that we are wasting time attempting. You have done a lot for me, so at least let me do this small task for you."
    mc "Let’s not lose hope before we have even begun."
    "The sense of anticipation in the atmosphere grew as we neared the lake, the lights from the camp grew from across the lake. I was no longer lost and could easily get back now, but this was no longer about me, this was now about repaying the one that had saved my life."
    "I was still limping around, but my body had got used to the pain from stepping on my sore ankle."
    R "I have a hard time remembering where exactly, well, where exactly I died. But I do remember that there was a large tree stump and the remains of a small castle tower I think. I also wanted to say that I appreciate everything that you have done for me Blue Shirt."
    R "I think that we have gone through a lot tonight but spending it with you was worthwhile and your company was really enjoyable, much better than just walking around talking to myself."
    R "You have given me hope for the future, maybe there are other people out there like you that can see me and hear me. Plus you’ll be in camp so like maybe we could hang out sometimes if you’d like. I know that accepting a person lie me might not be the easiest, but I really do cherish this night with you"
    "Just as I was about to answer Sam, I heard faint shouting coming from the direction of the camp. I turned around trying to solve what the words shouted at us meant, thinking that maybe some camp instructor had seen us and was worried about me."
    play music "audio/Forgotten-Memories.ogg" volume 1.0 fadein 1 fadeout 1 loop
    "But as my luck would have it, my eyes focused and realized that it was none other than the people responsible for my adventure in the forest, the bullies."
    "Immediately my legs froze and panic had devoured my body. My brain translated the shouts, they were after me, and anger was a calm word to express their expressions. Sam had no clue what was going on at first until she saw my terrified expression. I think that she could guess who these people were."
    "Just as I thought that life was going to be over, Sam grabbed my hand and pulled me to start running with her. At the time the fact that she had grabbed my hand was lost in my worries, and it wouldn’t be until much later that it would connect in my mind."
    "How was she holding me when a few hours ago she couldn’t make contact with me? They say that spirits stay around if they have a lot of willpower."
    "Was it all possible because of the amount of willpower she put into helping me? It would be something that I would only be able to speculate about. The ground was muddy and damp, each step drained the slimmer of energy that I had left."
    "Lifting my leg was a struggle, each step felt like the earth was grabbing my shoes, not wanting me to leave."
    "We did not run long before we spotted what might have been exactly what Sam had described, a small run-down stone tower. It did not feel like we were getting any distance on the bullies they were getting closer, Sam pulled my hand towards the castle tower."
    "It wouldn’t be long before I would collapse, my lungs were working overtime and after walking around all night, my legs were starting to give up."
    "Yet with all of this happening, my eyes were starting to close more than ever, everything felt as if it was in slow motion. Sam was trying her best to get us to safety, there wasn’t a smile on her face"
    "nor any sense of positive emotions, it was completely different from the dog incident. Back then she forced herself to wear a smile to hide her true feelings from the world, but right now the mask was destroyed."
    "The scenery here was completely different, huge trees with branches that crept out to block out the sun were replaced with sparse burnt tree stumps that embraced the rising sun and used the dampness in the air to create orange filled burning sights."
    "Those were the last images I saw as we entered the tower, where the ground below me gave away and crumbled underneath me. As everything was going black I heard the loudest, darkest screech that I have ever heard in my life."
    play sound "audio/Ghost.ogg" volume 1.0
    "I don’t think that it was dark for long before my eyes adjusted and could see around me. Sunlight was entering through the circular hole in the sky through which I had fallen. I was surrounded by narrow stone slimy walls."
    "Laying in a pool of water explained my drenched state and low body heat. I was freezing and sore all over. Where was I? That was when my eyes adjusted and noticed that I was not the only one stuck in this hole, right beside me were skeleton remains."
    "I wanted to panic and freak out, but my body had no energy left for anything besides mere thoughts. I noticed the red fabric wrapped around the neck of the remains. A scarf which looked exactly like the one Sam wore. We must have done it, we must have found her body."
    stop sound
    "Well now hopefully I won’t meet the same end as her. I used the last tiny amount of energy that I had managed to recollect to shout at the top of my lungs for help. No one answered back."
    "What had happened to Sam and the bullies? Did they get her? No, there was no way they would be able to see her. I didn’t stay conscience in that hole for long before I passed out from the damage the night has taken out on my body. I was told that a camp instructor showed up soon"
    "because he had heard a loud screech and my call for help. Firefights and the police were called, firefights to save me and police to investigate the body. I awoke in a hospital bed where the police questioned me about the night."
    play music "audio/Punch-Deck-Ethereal.ogg" volume 1.0 fadein 1 fadeout 1 loop
    "I changed the story around to not include any mentions of Sam but told them to please look into whom the body was. This was the most that I would be able to do to hopefully make Sam pass onto the next life. Both of my parents were very worried about me. I didn’t get a night of sleep and had broken many bones."
    "That was more than enough for my parents to pull me out of the camp and keep me at home. A few days later an article had been published about Sam and that she had been missing for over sixty years, only to be found dead in that hole that I had fallen into."
    "The article didn’t mention me by name but mentioned how I almost suffered the same faith. The article ended with missing pictures of the bullies, they had gone missing from the camp at the same time as I was found."
    "There were search parties sent out but no one could find them. I wanted to revisit that forest and see Sam again, but a broken leg was keeping me at home and finding an excuse to revisit the forest was basically impossible."
    "It sadly took a few years before I would be able to visit again. A few years that would have been much more difficult if I hadn’t had met Sam that night. It was strange, but she felt like a part of me, there to remind me of hope at the worst of times."
    "I spent the day strolling through the forest, revisiting the cabin that we used for shelter, the hilltop, the place where I awoke to see her for the first time. In all those years it had not changed at all."
    "A part of me hoped to be able to see her again, while the other hoped that she was laid to rest after her body had been found."
    "She was free from the forest. Life went on, and I decided to use her memory of visiting the forest with her family every year for my family too. Every year as I grew older I wished that maybe she would be there or at least know how grateful I was for her existence."
    jump end

    label end_hill:
        play music "audio/joshua-mclean_dreams-left-behind.ogg" volume 1.0 fadein 1 fadeout 1 loop
        R "Blue Shirt that’s too much. I... I don’t think that I can do this any more. I know that you must be very confused about the current situation, but you’ve been kinda rude to me and I just can’t trust you this much."
        R "I understand that it is partly unfair to you, but I’m sorry this is my fault. I have to leave, good luck with getting home, you should be able to do it on your own now."
        "Tears ran down her face, her eyes screamed from the pain that she was in. It was too much for her to handle. She ran away from me, I was now all alone to solve what just happened and to get home. The next five minutes were filled with dead silence."
        "The only audible noises were my shoes stomping on the ground below as I tried to maintain balance. I tried to think about all the other times that Sam had touched, when I first fell while running from the bullies,"
        "I almost fell onto her, but I wasn’t conscience back then, when we first met she sat away from me and didn’t touch me at all, neither did she touch me during the dog ambush. She also told me to bandage myself."
        "She had always skipped ahead of me, only ever slowing down and turning around to talk to me. The top of the hill was way brighter than any other location that we had been to thus far. It was free from all the sheltering trees."
        "The dark sky, the bright stars, the shining moon were all perfectly fully visible and glancing at us for the tree’s protection as now gone. I looked across the horizon, for a second I was scared because all I could see was a large dense forest. But then as I looked towards the direction of the moon, I finally saw it."
        "A glistening body of water, if it wasn’t for the lake I would have never noticed those dark cabins to the side of it. There wasn’t a single light on, so I would have to follow the moon to be able to get back."
        "It was time to get home."
        jump choice_10_end

    label choice_10_end:
        play music "audio/joshua-mclean_dreams-left-behind.ogg" volume 1.0 fadein 1 fadeout 1 loop
        "I had been walking for a while. My ankle was sorer than ever. I would say that it was worse than when I first hurt it. All the walking must have taken its toll. For some reason, the forest seemed scarier alone."
        "The sounds seemed to intensify when you were alone with just your thoughts. Only a little while to go before I would get back to the camp. The horizon had begun to tear away, allowing for some of the rising sun’s light to emanate into the world."
        "The sense of anticipation in the atmosphere grew as we neared the lake, the lights from the camp grew from across the lake. I was no longer lost and could easily get back now. Just as I was about to rest before walking further, I heard faint shouting coming from the direction of the camp."
        "I turned around trying to solve what the words shouted at me meant, thinking that maybe some camp instructor had seen me and was worried that I wasn’t in bed, but as my luck would have it, my eyes focused and realized that it was none other than the people responsible for my adventure "
        " in the forest, the bullies. Immediately my legs froze and panic had devoured my body. My brain translated the shouts, they were after me, and anger was a calm word to express their expressions."
        if ghostStats['trust'] >= 50 and ghostStats['hurt'] <= 50 and ghostStats['anger'] <= 45:
            jump reunite
        else:
            "It wasn’t long before they caught up to me. The impact they had on my body made it give up. It was too much to handle, it was over. I'm sorry."
            jump end
    
    label end_distrust:
        play music "audio/joshua-mclean_dreams-left-behind.ogg" volume 1.0 fadein 1 fadeout 1 loop
        r "Sorry Blue Shirt but I don’t think that we should do this journey together. You’ve shown me that you don’t trust me, and it does seem like you don’t want me here. I can take a lot, but I have to be fair to myself, this isn’t good for me."
        r "I’ve enjoyed your company a bit since I haven’t been in one for a long time. But enough is enough. I wish you the best of luck with getting home. I'm sorry."
        "My words had hurt her too much, showing a lack of trust and being dismissal towards her didn’t work. I guess that I will have to do this alone now."
        "The attic space showed no signs of being used, no place for a bed, absolutely nothing lying around. Just an empty hollow room that would have been swallowed in darkness if it was not for a tiny circle window that allowed some moonlight to enter through its mouth."
        "Finding the bandage in the first aid box was an easy task. Most of the other items were missing, but luckily I was able to use the bandages. Had I injured something else and required other items I would have been out of luck."
        "While I was bandaging my ankle I realized how bad it truly was. Inflamed and bruised, it will be difficult to walk the rest of the journey with this ankle. The next thing that I remember is waking up in massive pain, not just my ankle, but I was starving."
        "Sun shined through the circle window, it was daytime now, I must have fallen asleep from the pain and weakness. I had to leave this place and get back to camp or else I would starve soon, well I was more likely to die from thirst first."
        "Each step was extremely painful, my ankle wouldn’t be able to take much. However, that pain could not be compared to the pain that I would feel next. The pack of dogs had surrounded the entrance of the cabin."
        " I didn’t realize this until it was too late. Way too late to do anything at all. I’m sorry."
        jump end 

    label reunite:
        play music "audio/Forgotten-Memories.ogg" volume 1.0 fadein 1 fadeout 1 loop
        "Just as I thought that life was going to be over, Sam grabbed my hand and pulled me to start running with her. At the time the fact that she had grabbed my hand was lost in my worries, and it wouldn’t be until much later that it would connect in my mind."
        R "You’re not going to get rid of me so easily blue shirt, now shush I’ll save you."
        "How was she holding me when a few hours ago she couldn’t make contact with me? They say that spirits stay around if they have a lot of willpower."
        "Was it all possible because of the amount of willpower she put into helping me? It would be something that I would only be able to speculate about. The ground was muddy and damp, each step drained the slimmer of energy that I had left."
        "Lifting my leg was a struggle, each step felt like the earth was grabbing my shoes, not wanting me to leave."
        "We did not run long before we spotted what might have been exactly what Sam had described, a small run-down stone tower. It did not feel like we were getting any distance on the bullies they were getting closer, Sam pulled my hand towards the castle tower."
        "It wouldn’t be long before I would collapse, my lungs were working overtime and after walking around all night, my legs were starting to give up."
        "Yet with all of this happening, my eyes were starting to close more than ever, everything felt as if it was in slow motion. Sam was trying her best to get us to safety, there wasn’t a smile on her face"
        "nor any sense of positive emotions, it was completely different from the dog incident. Back then she forced herself to wear a smile to hide her true feelings from the world, but right now the mask was destroyed."
        "The scenery here was completely different, huge trees with branches that crept out to block out the sun were replaced with sparse burnt tree stumps that embraced the rising sun and used the dampness in the air to create orange filled burning sights."
        "Those were the last images I saw as we entered the tower, where the ground below me gave away and crumbled underneath me. As everything was going black I heard the loudest, darkest screech that I have ever heard in my life."
        play sound "audio/Ghost.ogg" volume 1.0
        "I don’t think that it was dark for long before my eyes adjusted and could see around me. Sunlight was entering through the circular hole in the sky through which I had fallen. I was surrounded by narrow stone slimy walls."
        "Laying in a pool of water explained my drenched state and low body heat. I was freezing and sore all over. Where was I? That was when my eyes adjusted and noticed that I was not the only one stuck in this hole, right beside me were skeleton remains."
        stop sound
        "I wanted to panic and freak out, but my body had no energy left for anything besides mere thoughts. I noticed the red fabric wrapped around the neck of the remains. A scarf which looked exactly like the one Sam wore. We must have done it, we must have found her body."
        "Well now hopefully I won’t meet the same end as her. I used the last tiny amount of energy that I had managed to recollect to shout at the top of my lungs for help. No one answered back."
        "What had happened to Sam and the bullies? Did they get her? No, there was no way they would be able to see her. I didn’t stay conscience in that hole for long before I passed out from the damage the night has taken out on my body. I was told that a camp instructor showed up soon"
        "because he had heard a loud screech and my call for help. Firefights and the police were called, firefights to save me and police to investigate the body. I awoke in a hospital bed where the police questioned me about the night."
        play music "audio/Punch-Deck-Ethereal.ogg" volume 1.0 fadein 1 fadeout 1 loop
        "I changed the story around to not include any mentions of Sam but told them to please look into whom the body was. This was the most that I would be able to do to hopefully make Sam pass onto the next life. Both of my parents were very worried about me. I didn’t get a night of sleep and had broken many bones."
        "That was more than enough for my parents to pull me out of the camp and keep me at home. A few days later an article had been published about Sam and that she had been missing for over sixty years, only to be found dead in that hole that I had fallen into."
        "The article didn’t mention me by name but mentioned how I almost suffered the same faith. The article ended with missing pictures of the bullies, they had gone missing from the camp at the same time as I was found."
        "There were search parties sent out but no one could find them. I wanted to revisit that forest and see Sam again, but a broken leg was keeping me at home and finding an excuse to revisit the forest was basically impossible."
        "It sadly took a few years before I would be able to visit again. A few years that would have been much more difficult if I hadn’t had met Sam that night. It was strange, but she felt like a part of me, there to remind me of hope at the worst of times."
        "I spent the day strolling through the forest, revisiting the cabin that we used for shelter, the hilltop, the place where I awoke to see her for the first time. In all those years it had not changed at all."
        "A part of me hoped to be able to see her again, while the other hoped that she was laid to rest after her body had been found."
        "She was free from the forest. Life went on, and I decided to use her memory of visiting the forest with her family every year for my family too. Every year as I grew older I wished that maybe she would be there or at least know how grateful I was for her existence."
        jump end

    label end:
        python:
            print(choices)
            print(choices[0])
            choicesUpload = choices
            print(choicesUpload)
        
        "[choices]"
        # This ends the game.


    
    
    #python:
        #lengthC = len(choicesUpload)
        #if lengthC < 12:
        #    if lengthC == 11:
        #        choicesUpload.append("")
        #    else:
        #        choicesUpload.append("")
        #        choicesUpload.append("")
        #        choicesUpload.append("")
        # 
        #posts = db.projectTest
        #post_data = {
        #    'Choice 1': choicesUpload[0],
        #    'Choice 2': choicesUpload[1],
        #    'Choice 3': choicesUpload[2],
        #    'Choice 4': choicesUpload[3],
        #    'Choice 5': choicesUpload[4],
        #    'Choice 6': choicesUpload[5],
        #    'Choice 7': choicesUpload[6],
        #    'Choice 8': choicesUpload[7],
        #    'Choice 9': choicesUpload[8],
        #    'Choice 10': choicesUpload[9],
        #    'Choice 11': choicesUpload[10],
        #    'Choice 12': choicesUpload[11],
        #}
        #result = posts.insert_one(post_data) 
    init python:
        def calculateHighestEmotion(emotions):
            emotionToReturn = ""
            hE = 0
            for emotion in emotions:
                if emotions[emotion] > hE:
                    hE = emotions[emotion]
                    emotionToReturn = emotion

            if emotionToReturn == "trust":
                emotionToReturn = "Trusting"
            elif emotionToReturn == "anger":
                emotionToReturn = "Angry"
            elif emotionToReturn == "anxiety":
                emotionToReturn = "Anxious"
            elif emotionToReturn == "helped":
                emotionToReturn = "Helped"
            elif emotionToReturn == "strength":
                emotionToReturn = "Strong"
            elif emotionToReturn == "anger":
                emotionToReturn = "Angry"
            elif emotionToReturn == "hurt":
                emotionToReturn = "Hurt"
            elif emotionToReturn == "happiness":
                emotionToReturn = "Happy"
            
            return emotionToReturn
        
        def dictContainsTrue(dict):
            for key in dict:
                if dict[key] == True:
                    return True
        
        def removeElements(choices, listToRemove):
            for elements in listToRemove:
                choices[elements] = False
            return choices
            

    $ highestEmotion = calculateHighestEmotion(ghostStats)
    $ displayAmount = 4

screen end_screen3():
    frame:
        xalign 0.5 yalign 0.5 xpadding 20 ypadding 20
        vbox:
            $ displayAmount = 4
            if choicesMade["2a"] and displayAmount > 0:
                $ displayAmount -= 1
                #$ choicesMade["2a"] = False
                text resultOutput["2a"]+"\n"
            if choicesMade["2b"] and displayAmount > 0:
                $ displayAmount -= 1
                #$ choicesMade["2b"] = False
                text resultOutput["2b"]+"\n"
            if choicesMade["3a"] and displayAmount > 0:
                $ displayAmount -= 1
                #$ choicesMade["3a"] = False
                text resultOutput["3a"]+"\n"
            if choicesMade["3c"] and displayAmount > 0:
                $ displayAmount -= 1
                #$ choicesMade["3c"] = False
                text resultOutput["3c"]+"\n"
            if choicesMade["4a"] and displayAmount > 0:
                $ displayAmount -= 1
                #$ choicesMade["4a"] = False
                text resultOutput["4a"]+"\n"
            if choicesMade["4b"] and displayAmount > 0:
                $ displayAmount -= 1
                #$ choicesMade["4b"] = False
                text resultOutput["4b"]+"\n"
            if choicesMade["4c"] and displayAmount > 0:
                $ displayAmount -= 1
                #$ choicesMade["4c"] = False
                text resultOutput["4c"]+"\n"
            if choicesMade["5a"] and displayAmount > 0:
                $ displayAmount -= 1
                #$ choicesMade["5a"] = False
                text resultOutput["5a"]+"\n"
            if choicesMade["5b"] and displayAmount > 0:
                $ displayAmount -= 1
                #$ choicesMade["5b"] = False
                text resultOutput["5b"]+"\n"
            if choicesMade["6a"] and displayAmount > 0:
                $ displayAmount -= 1
                #$ choicesMade["6a"] = False
                text resultOutput["6a"]+"\n"
            if choicesMade["6b"] and displayAmount > 0:
                $ displayAmount -= 1
                #$ choicesMade["6b"] = False
                text resultOutput["6b"]+"\n"
            if choicesMade["7b"] and displayAmount > 0:
                $ displayAmount -= 1
                #$ choicesMade["7b"] = False
                text resultOutput["7b"]+"\n"
            if choicesMade["8"] and displayAmount > 0:
                $ displayAmount -= 1
                #$ choicesMade["8"] = False
                text resultOutput["8"]+"\n"
            if choicesMade["9a"] and displayAmount > 0:
                $ displayAmount -= 1
                #$ choicesMade["9a"] = False
                text resultOutput["9a"]+"\n"
            if choicesMade["9b"] and displayAmount > 0:
                $ displayAmount -= 1
                #$ choicesMade["9b"] = False
                text resultOutput["9b"]+"\n"
            if choicesMade["9c"] and displayAmount > 0:
                $ displayAmount -= 1
                #$ choicesMade["9c"] = False
                text resultOutput["9c"]+"\n"
            if choicesMade["10a"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["10a"]+"\n"
                #$ choicesMade["10a"] = False
            if choicesMade["10b"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["10b"]+"\n"
                #$ choicesMade["10b"] = False
            if choicesMade["10c"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["10c"]+"\n"
               # $ choicesMade["10c"] = False
            hbox xalign 0.5 spacing 500:
                textbutton ""
                textbutton "Continue":
                    action Return(True)

screen end_screen2():
    frame:
        xalign 0.5 yalign 0.5 xpadding 20 ypadding 20
        vbox:
            $ displayAmount = 4
            if choicesMade["2a"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["2a"]+"\n"
                $ removeChoices.append("2a")
                #$ choicesMade["2a"] = False
            if choicesMade["2b"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["2b"]+"\n"
                $ removeChoices.append("2b")
                #$ choicesMade["2b"] = False
            if choicesMade["3a"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["3a"]+"\n"
                $ removeChoices.append("3a")
                #$ choicesMade["3a"] = False
            if choicesMade["3c"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["3c"]+"\n"
                $ removeChoices.append("3c")
                #$ choicesMade["3c"] = False
            if choicesMade["4a"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["4a"]+"\n"
                $ removeChoices.append("4a")
                #$ choicesMade["4a"] = False
            if choicesMade["4b"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["4b"]+"\n"
                $ removeChoices.append("4b")
                #$ choicesMade["4b"] = False
            if choicesMade["4c"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["4c"]+"\n"
                $ removeChoices.append("4c")
                #$ choicesMade["4c"] = False
            if choicesMade["5a"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["5a"]+"\n"
                $ removeChoices.append("5a")
                #$ choicesMade["5a"] = False
            if choicesMade["5b"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["5b"]+"\n"
                $ removeChoices.append("5b")
                #$ choicesMade["5b"] = False
            if choicesMade["6a"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["6a"]+"\n"
                $ removeChoices.append("6a")
                #$ choicesMade["6a"] = False
            if choicesMade["6b"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["6b"]+"\n"
                $ removeChoices.append("6b")
                #$ choicesMade["6b"] = False
            if choicesMade["7b"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["7b"]+"\n"
                $ removeChoices.append("7b")
                #$ choicesMade["7b"] = False
            if choicesMade["8"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["8"]+"\n"
                $ removeChoices.append("8")
                #$ choicesMade["8"] = False
            if choicesMade["9a"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["9a"]+"\n"
                $ removeChoices.append("9a")
                #$ choicesMade["9a"] = False
            if choicesMade["9b"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["9b"]+"\n"
                $ removeChoices.append("9b")
                #$ choicesMade["9b"] = False
            if choicesMade["9c"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["9c"]+"\n"
                $ removeChoices.append("9c")
                #$ choicesMade["9c"] = False
            if choicesMade["10a"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["10a"]+"\n"
                $ removeChoices.append("10a")
                #$ choicesMade["10a"] = False
            if choicesMade["10b"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["10b"]+"\n"
                $ removeChoices.append("10b")
                #$ choicesMade["10b"] = False
            if choicesMade["10c"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["10c"]+"\n"
                $ removeChoices.append("10c")
                #$ choicesMade["10c"] = False
            hbox xalign 0.5 spacing 500:
                textbutton ""
                textbutton ">>":
                    action Return(True)


$ removeChoices = []
screen end_screen1():
    frame:
        xalign 0.5 yalign 0.5 xpadding 20 ypadding 20
        vbox:
            text "You left Sam feeling "+highestEmotion+"\n"+"your result: "+algorithm.startAlgorithm(trueChoices)
            $ displayAmount = 4
            
            if choicesMade["2a"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["2a"]+"\n"
                $ removeChoices.append("2a")
                #$ choicesMade["2a"] = False
            if choicesMade["2b"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["2b"]+"\n"
                $ removeChoices.append("2b")
                #$ choicesMade["2b"] = False
            if choicesMade["3a"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["3a"]+"\n"
                $ removeChoices.append("3a")
                #$ choicesMade["3a"] = False
            if choicesMade["3c"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["3c"]+"\n"
                $ removeChoices.append("3c")
                #$ choicesMade["3c"] = False
            if choicesMade["4a"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["4a"]+"\n"
                $ removeChoices.append("4a")
                #$ choicesMade["4a"] = False
            if choicesMade["4b"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["4b"]+"\n"
                $ removeChoices.append("4b")
                #$ choicesMade["4b"] = False
            if choicesMade["4c"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["4c"]+"\n"
                $ removeChoices.append("4c")
                #$ choicesMade["4c"] = False
            if choicesMade["5a"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["5a"]+"\n"
                $ removeChoices.append("5a")
                #$ choicesMade["5a"] = False
            if choicesMade["5b"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["5b"]+"\n"
                $ removeChoices.append("5b")
                #$ choicesMade["5b"] = False
            if choicesMade["6a"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["6a"]+"\n"
                $ removeChoices.append("6a")
                #$ choicesMade["6a"] = False
            if choicesMade["6b"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["6b"]+"\n"
                $ removeChoices.append("6b")
                #$ choicesMade["6b"] = False
            if choicesMade["7b"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["7b"]+"\n"
                $ removeChoices.append("7b")
                #$ choicesMade["7b"] = False
            if choicesMade["8"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["8"]+"\n"
                $ removeChoices.append("8")
                #$ choicesMade["8"] = False
            if choicesMade["9a"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["9a"]+"\n"
                $ removeChoices.append("9a")
                #$ choicesMade["9a"] = False
            if choicesMade["9b"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["9b"]+"\n"
                $ removeChoices.append("9b")
                #$ choicesMade["9b"] = False
            if choicesMade["9c"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["9c"]+"\n"
                $ removeChoices.append("9c")
                #$ choicesMade["9c"] = False
            if choicesMade["10a"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["10a"]+"\n"
                $ removeChoices.append("10a")
                #$ choicesMade["10a"] = False
            if choicesMade["10b"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["10b"]+"\n"
                $ removeChoices.append("10b")
                #$ choicesMade["10b"] = False
            if choicesMade["10c"] and displayAmount > 0:
                $ displayAmount -= 1
                text resultOutput["10c"]+"\n"
                $ removeChoices.append("10c")
                #$ choicesMade["10c"] = False
            hbox xalign 0.5 spacing 500:
                textbutton ""
                textbutton ">>":
                    action Return(True)




menu optional_name:
    "Say Statement"
    "Choice 1":
        "Yes"
        #block of code to run
    "Choice 2":
        "Yes"
        #block of code to run


call screen end_screen1
$ choicesMade = removeElements(choicesMade, removeChoices)
$ removeChoices = []
if dictContainsTrue(choicesMade):
    call screen end_screen2
$ choicesMade = removeElements(choicesMade, removeChoices)
if dictContainsTrue(choicesMade):
    call screen end_screen3  
return
