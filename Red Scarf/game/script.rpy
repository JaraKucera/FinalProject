define R = Character("Sam", color="#eb3474")
define r = Character("Weird Girl", color="#eb3474")
define dad = Character("Dad", color="#7732a8")
define mom = Character("Mom", color="#ebdb2d")
define mc = Character("You", color="#3bd9b4")
define t = Character("Trevor", color="#36b300")
define i = Character("Instructor", color="#CE8147")
define t2 = Character("Tray", color="#CDE7BE")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # These display lines of dialogue.

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
    mc "So this, is it? The place where I will spend the rest of the summer all away from you guys?"
    dad "Look Sport, we already discussed this with your mom, this will benefit you the most, so get out there and let the person in charge know that you’re here."

    menu choice_1:
        "Can’t you please reconsider? I don’t think that I should be here. I’ll do whatever it takes to stay home.":
            jump choice_1_home

        "*silence*":
            jump choice_1_done

        "Yeah, I understand, I will give this a shot, and hopefully, it won’t be too bad.  If anything happens I will let you guys know.":
            jump choice_1_understanding
    
    label choice_1_home:
        dad "Listen, it will only be for a short time, soon you’ll be back home with us. We just can’t handle things right now."
        jump choice_1_done

    label choice_1_understanding:
        dad "Thanks for understanding sport."
        jump choice_1_done

    label choice_1_done:
        "Without even saying goodbye they were gone. The car getting swallowed by the spiral of trees, possibly never to be seen again."
    
    "By looking at the camp, you could tell that in the past it must have been filled with joyous souls of children laughing about, enjoying their summers, stress-free and happy."
    "All the buildings shining, feeling alive and fresh. The new reality was a mere husk of the past. The lake where children would cool off after a long day of activities looked more like one step would fill your body with toxic waste."
    "The cabins and buildings all looked soulless, the colour drained from this place. It looked like it was all going to collapse soon from all the mould and lack of care."
    "From everyone’s expressions, you could tell that joy and happiness were two emotions gone from this world. Everyone had the same facial expression, an expression that screamed help me, let me leave, I’ve had enough."
    "Even those that were in charge all looked like they were slaves, salving away for a minimal wage, hoping to get by until their next paycheque."
    t "Hey watch it, what do you think that you’re doing?"
    "Before I even get a chance to respond, he grabs me by my shirt and holds me against the wall."
    t "Listen here, I see that you’re new here, so I’m only going to give you a warning this time. People around here are in fear when they hear my name. The boys and I here are T."
    t "We run this little camp, so don’t you dare ever bump into me or the boys ever again. If you do you’ll get this but much worse."
    "With that, he punched me in the gut and left me heaving on the ground. As his friends walked by they spat on me and called me various names."
    "What a great way to start this camp. Hopefully, he won’t be too much of a problem."
    
    "After going to the head’s office to sign up and be assigned to a bed in a run-down cabin. I was informed that I’ve come on time to be able to partake in the final activity of the day before bedtime."
    "One of the run-down buildings had a nice set of windows to one of the sides of the walls overlooking the forest. The cabin wasn’t as bad as it looked from the outside, the walls constructed out of logs with certifications hung up and framed from years before I was even born."
    "How I wish I could have dealt with this camp twenty years ago during its glory years.  While I am the last person to enjoy group activities and the outside, it would have made it much more bearable."
    "Opposing the wall of windows was a large fireplace, burning brightly, it was the only signal of hope in this building. Burning brightly, being strong and tough, all quantities that I would need to survive this summer."
    i "Welcome all to the afternoon slash evening class for today. We will box to tire ourselves out so that we can have that goodnight sleep."
    "There were only about twenty kids here, most of which looked like they would rather be dead than to partake in this activity."
    i "Since most of you are new to this camp, the teams have been picked randomly. Now don’t worry you won’t be punching each other. One of you will be holding the punching bag while the other will be punching it. I will read the pairs out now."
    "I almost lost my heart to shock when I heard my name announced after the name Tray. For I realized in that split second upon seeing his face that the guy that had punched a hole through my gut was Tray."
    t "I hope that you remember the warning that you got earlier today."
    "Hearing those words echo in my brain along with the devious smile plastered on his face brought back the feeling of pain that still wasn’t fully away. I was first to hold the punching bad. Trays face grew with pleasure every time that he punched."
    "Each punch sent shockwaves through my body and pushed me further. Keeping my balance was getting more difficult with each punch. The harder the punch the wider the grin on his face would be."
    "Somehow I managed to survive the first twenty minutes, it was now my turn to punch. It didn’t seem like my punches had any impact on Tray whatsoever. It was as if I was just gently tapping the punching bag."
    "For the first time, I was a little at peace, I could study the surrounding environment. Everyone seemed to be doing much better, some even had a smile on their face. It looked like they were making friends."
    "If some details had been taken out of the equation, it would almost be a wholesome scene to witness. Before I could fully immerse myself, it was time to swap once again. I held onto dear life, hoping to not let go of the punching bag, for if I did I would be in a world of pain."
    "Tray was not holding back at all. Thankfully, I managed to survive the full twenty minutes, only one last set from me before I was free."
    "As I punched I started to immerse myself, none of this would have happened if I wasn’t here, this pain wouldn’t be in my stomach. I wouldn’t be wasting my time on a summer camp if it wasn’t for:"

    menu choice_2:
        "This is all my fault, if I had just done things differently, helped out more if I was different. If I was better, to myself and them. I wish I was good enough.":
            jump choice_2_me

        "It’s all of their fault, if only they would just care, maybe offer some help. Focus on me for once. Why can’t I get the focus for a bit sometimes? I just wish that they were better.":
            jump choice_2_family

        "It’s no one’s fault that I am in this situation. Things just sometimes happen that we have no control over. Things happen because of luck and misfortune, and I was just unlucky to get to this point.":
            jump choice_2_no_one
    
    label choice_2_me:
        jump choice_2_done
    
    label choice_2_family:
        jump choice_2_done

    label choice_2_no_one:
        jump choice_2_done
    
    label choice_2_done:
        t "Oh I am going to absolutely kill you."
    
    "I was so lost in thought that I did not realize that time was over. I boxed Trevor into the throat."
    i "Hey now calm down it was an accident, leave him alone."
    "Thank god that the supervisor was there to save me otherwise I probably would have died just there and then."
    t "You’re dead"
    "That’s all Tray said as he left the building."

    "With that, the activities had come to an end and so did the day. After making my way to the cabin and being checked off the present list I was ready to end the day in a hard and cold bed. I wanted to finally rest, the day had been so exhausting."
    "Even though I was so dead my body did not listen to me and instead kept me awake reliving all the events that had transpired. I just sat there at my bed wishing that this was all a dream and that I would just wake up in my bed at home."
    "Sadly, this isn’t a primary school short story where all conflicts had been resolved and disappear when the character suddenly wakes up and realizes it had all been just a dream. This is instead a reality where Trevor had gathered his friends and had come after me."
    "Finding the cabin where I would be sleeping was not a difficult task. Even going blindly would give you a twenty percent chance to guess on the first try. There were five cabins for each gender which housed five kids each."
    "It didn’t take long before I heard the door open before a hand had been put over my mouth, with other hands used to drag me outside. It all happened so fast that I didn’t even get a chance to yell or focus attention on myself."
    "The last thing that I saw was a bright star shining in the night sky before everything went dark."

    "I woke up to a punch to the gut, the same punch that I had received earlier."
    t "Well, well, well, I told you that I’d kill you. You know, no one has messed up on the same day as their warning. You must be incredibly stupid or incredibly unlucky."
    t "Either way, let me explain what's going to happen to you. I want to see the fear in your eyes as I go over everything that will happen to you."
    t "Firstly, calm down, you’re not actually going to die, you’re just going to suffer a lot. My boys and I are going to roughen you up a little. When you are found tomorrow morning you’ll have to be brought to the hospital and possibly be put on life support."
    t "But hey it will get rid of you from this camp and out of my face. I don’t want any of my problems here, and you have become a problem."
    "With that came punches and kicks all over my body. I had no idea where I was. I was in the forest for sure but from what I could see it wasn't anywhere near the camp. The trees were here to cover up for any sounds that might help me."
    "The branches as if being held against my mouth muffling anything that would escape my mouth in hopes of getting help. It was almost pitch black now if I was top survive this beat down would I even be able to get back? I didn’t deserve this."
    t2 "Hey Trevor isn’t this forest haunted?"
    t "Tray are you completely stupid?"
    "Suddenly a loud howl echoed throughout the forest distracting everyone. Although my hands remained tied by some rope, my legs although beaten were free."
    "With the adrenaline in my body, I made a run for it through the forest with only a slight head start before being followed."
    "There wasn’t much light left from the sun and most of it was unable to pass through the forest sky. I had no clue where I was going before slipping and tumbling down."

    #Chapter 2
    r "Oh looks like you’re waking up. That fall looked like it hurt a lot."
    "I awoke to the sounds of someone gently talking as if assuming that no one would hear them. I couldn’t understand what they were saying, everything muffled and blurring. It took a couple of seconds before my eyes adjusted, and I could decipher what was said to me."
    "I was still in the forest, however, it felt different, that dead atmosphere disappeared and got replaced by a brighter living forest. Although it was dark, the bright stars illuminated the surroundings."
    "The trees no longer looked like they were trying to grab at you but instead looked like they were offering you a hug to console you. In front of me sat a girl about my age on a log. She wore a typical summer outfit of a t-shirt and pants, but for some reason had a red scarf tied around her neck."
    r "Well blue shirt? Did the fall remove your ability to communicate? Are you okay?"
    mc "Oh yeah Uhm sorry I was just trying to recollect myself. Where are we?"
    "I tried getting up to get closer to her for a better look but as I tried to stand on my right foot, I collapsed to the ground from the pain."
    r "Yikes blue shirt, looks like that fall might have twisted your ankle. You’re lucky that I am here to save you. You did almost fall on me though when you decided to tumble down all of those hills. I did notice that your hands had been tied with some rope, poor craftsmanship for sure though."
    r "So bad that your hands got untied by the fall. What did happen to you?"
    "As she talked the moon lit up her face, she looked like an ordinary weird girl, weird because she had a huge smile plastered on her face the entire time that she talked."
    "Snickering here and there at her jokes. It kinda felt like she was happy that I almost fell on her. What do I tell her about what had happened?"

    menu choice_3:
        "I messed up a lot, where bumping into someone lead up to getting beaten up to messing up again. I ran away from them, but I couldn’t see in the dark and slipped, so now I am here. It is all my fault.":
            jump choice_3_depressive

        "I got bullied by this guy called Trevor and his friends. I don’t know why I deserved such treatment, but I did accidentally punch Trevor in the throat.":
            jump choice_3_hurtful

        "I don’t want to talk about it. Things happened, and now I am here with bruises all over my body and a potentially twisted ankle.":
            jump choice_3_distrustrusful

    label choice_3_depressive:
        r "Yeah that makes a little sense, most of our pain starts from little things that transpire out of control and eventually lead us here. But everything will be okay, we just need to get you to someplace to rest for a while. This part of the forest sometimes has wild rabid dogs."
        r "I wouldn’t want you getting hurt more than you already are, Blue Shirt." 
        jump choice_3_done

    label choice_3_hurtful:
        r "Well thanks for being honest with me. The treatment that we get from others isn’t always the one that we deserve."
        r "Though I understand why someone would be upset if they got hit in the throat. We should walk to a cabin nearby, this part of the forest sometimes has wild rabid dogs sniffing about. I worry about getting caught up in that, Blue Shirt."
        jump choice_3_done

    label choice_3_distrustrusful:
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
            jump choice_4_dismissal

        "Appreciative":
            jump choice_4_appreciative
        "Relate":
            jump choice_4_relate

    label choice_4_dismissal:
        "Yeah I didn’t ask for any of that. I just want to get to the cabin as soon as possible to fix this ankle."
        r "Yeah I’m sorry. I just got carried away a little, don’t worry we are almost there."
        jump choice_4_done

    label choice_4_appreciative:
        "No, I appreciate hearing that. I feel like I understand you a little more. I understand losing passion for something that you used to love. While it has not happened to me, I know that it must be very painful. Losing our passion for something is kind of like losing a part of ourselves."
        r "Thanks, I’m sorry for going off, but I am glad that you can understand a part of this weird reality that I live in. We are almost at the cabin now."
        jump choice_4_done

    label choice_4_relate:
        "Yeah I can relate to that. While mine isn’t about nature and drawing necessarily, I’ve had a similar experience with something similar. Also lost my love for doing something that I used to love a lot. It felt like a part of me was torn away, like a part of the old me is missing."
        "Something that I continue to want to get back. But no matter how hard I try I just can’t."
        r "I’m glad that you can understand,  but I am sad that you can relate. It would be nice if everyone never lost their passions. To me losing my passion felt like I had lost a part of myself."
        r "It made me feel like a damaged person, and I kept questioning myself why I was being different. We are almost at the cabin but thank you, I appreciate it."
        jump choice_4_done
    
    label choice_4_done:
        "After a few seconds of us silently walking through the forest, twigs breaking under our feet, our shoes getting dirtier by the damp soil. A howl similar to that which I’ve used to escape from Tray echoed throughout the woods again."
        "This time the sound wrapped through my skull, it felt much more intense and much closer. My legs started to twitch from the fear, my eyes gazing all around hoping to not see the source of the noises."
        "he red scarf girl had noticed my twitching and looking around, she pointed behind me and when I averted my gaze to what laid there, I saw two bright yellow eyes. Eyes of death hungry not just for the meat on my bones but eager to ravage my soul."
        r "Listen to me Blue shirt, we will be in trouble if we are caught, I want you to go run as fast as possible with that hurt ankle, in the direction that we have been heading in. You will see the cabin, go inside, and you should see a ladder heading up into the attic. Go there now, I will distract these dogs. Trust me, go!"

    menu choice_5:
        "Trust":
            jump choice_5_trust

        "Distrust":
            jump choice_5_distrust
    
    label choice_5_trust:
        mc "Okay I trust you"
        $ trust = True
        jump choice_5_done

    label choice_5_distrust:
        mc "No, I don’t trust you, what if something happens?"
        "As soon as those words left my mouth a growling vicious-looking dog emerged from behind me. Its eyes full of lust for meat, awaiting its turn to attack."
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

    if trust:
        r "Thanks for trusting me by the way"
    else:
        r "Would have certainly been easier if you had just trusted me."
    
    r "Hmm, let’s see, I could swear that there was a first aid box somewhere around here, oh yeah there it is."
    "After finally being able to calm down and realize that the girl was okay, I finally had the chance to notice where I was. A low wooden ceiling that did not offer much protection. If the girl stayed here during the night, the scarf would start to make more sense, it was starting to get chilly."
    "The attic space showed no signs of being used, no place for a bed, absolutely nothing lying around. Just an empty hollow room that would have been swallowed in darkness if it was not for a tiny circle window that allowed some moonlight to enter through its mouth."
    mc "How did you manage to escape?"
    r "Ah Blue shirt does not want nay plot holes, well I just made those dogs feel scared, I asserted my dominance and threw some rocks. Just needed you to leave because it is embarrassing to do and there is no way that you could ever pull of dominance."
    r "Now no more questions, get yourself patched up, there are some bandages in that aid box over there."

    #Chapter 3
    "She must have enjoyed calling me ‘Blue Shirt’, although it is true that neither one of us had introduced ourselves to one another. I guess that if I had worn any other t-shirt that day then I would have been called by that colour instead."
    "The sense of urgency of it all just left us without much time or care towards names. We just went along with everything, both of our social skills must have needed a little help. To me, she’s just a weird girl that found me in the forest at a time of need, a girl with a red scarf, a girl that gives me hope and helps me survive right now."
    "Finding the bandage in the first aid box was an easy task. Most of the other items were missing, but luckily I was able to use the bandages. Had I injured something else and required other items I would have been out of luck."
    "Thankfully upon closer inspection of my ankle, I noticed that although I had put plenty of pressure on it while running over here, it was not bruised nor had grown in size. Although a small victory still a victory that gave me hope that I very much needed."
    mc "You know it is kinda funny that I haven’t even asked for your name yet even after you have helped me so much."
    r "Oh Uhm yeah, you are right, it is a little funny, I guess I just enjoyed calling you Blue Shirt. I haven’t talked with anyone for a long time, most people don’t even notice me."
    "Yeah, she definitely needed some work with her social skills, she hadn’t even given me her name even after I asked. But oh well I guess I will take the lead."

    menu choice_6:
        "Nice":
            jump choice_6_nice

        "Dismiss":
            jump choice_6_dismiss

    label choice_6_nice:
        python:
            name = renpy.input("What's your name?")
            name = name.strip() or "MC"
        
        "My name is [name], it is very nice to meet you. I’m very thankful for all of your help so far. What’s your name?"
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
        R "I don’t know Blue Shirt, I don’t think that there is any hope in getting back to where you came from. Do you even want to return to a place that hurt you? Don’t you think that the pain will just happen again, over and over? I think that it is pretty hopeless, will people even look for you? Does anyone care?"
    
    menu choice_7:
        "Hopeful":
            jump choice_7_hopeful

        "Anger":
            jump choice_7_anger

        "Optimistic":
            jump choice_7_optimistic
    
    label choice_7_hopeful:
        mc "I can’t just lose hope now. Things are bad, I know that, but I can’t just give up. Even if no one would come looking for me. Even if there isn’t anyone that cares, I have to keep fighting. Life can always get better even if it may not seem that way, even if I don’t know what’s to come, I want my future to be better even if I have to fight for it."
        R "Why fight for a future with more pain in it?  Even if there are good things to come, the bad overshadows it. Isn’t it easier to give up now to give up on the pain?"
        "Although still maintaining that smile of hers, her voice trembled."
        R "What if you can’t save yourself?"
        mc "I don’t think that most of us can do this alone, I can’t beat my problems alone. I need help from others, but I won’t ever get that help if I don’t try if I don’t ask for it. I have to take the first step. I can’t do this alone. So Klara please help me. Please help me return home."
        "That was the first time that I saw her face without s smile, without a mask on. Her sad glistening eyes now matched the rest of her face. A single tear rolled down her cheek. This was the true Klara in front of me. It only lasted a few seconds that I would see her like that. Looking into her eyes full of despair felt like hours had been lost,"
        "it felt like a lot was still unexplained a lot more tears were built up, still yet to drop. But that single droplet was all I was going to get out of her today. She quickly composed herself, the mask wasn’t shattered yet, it was still capable of hiding her emotions."
        R "Okay Blue Shirt, I’ll give you my all to help you."
        jump choice_7_done
    
    label choice_7_anger:
        mc "I don’t care if anyone cares about me or not. I am not living my life for others, I am not going to let anyone ruin my life. If I have to go through some pain to live then I will. Yeah, it hurts to live like this. Hurts to have to face life alone. But life isn’t fair, it was never fair and never will be fair. Just get over it."
        mc "Being just sad about things won’t help. It doesn’t help you, doesn’t help me. Doesn’t help anyone. Let’s just focus on getting me home."
        "Once again she had that smile on her face, the smile that she uses to hide behind. Caring about every little thing won’t help anyone. I don't need her help to get home, I can't be too far."
        R "Fine, I'll help you"
        jump choice_7_done
    
    label choice_7_optimistic:
        mc "Some people care about me. People will come to look for me. I know that I was hurt and may be hurt again, but there are people out there that love me and need me. A few bullies won't stop me from living my life. I got hurt physically, but mentally I am still strong. Those bullies just have their problems and used me to deal with them."
        mc "I don’t think that bad people mean to be bad. They are just people with issues trying to solve them in evil ways, but they aren’t evil. Our society just can’t deal with them properly yet."
        "As I was saying those words, Klara’s smile changed, she didn’t lose her smile, it just changed. This changed wasn’t permanent, it only lasted a little while, but for that while, it just felt genuine that it was hard not to smile myself."
        R "You are way too optimistic about the world, you’re a big dumbass but the world needs more people like you. I may not completely agree with you but hey I will help you get back home if you want my help."
        jump choice_7_done

    label choice_7_done:
        "Hmm, how would I get back to the camp without knowing in which direction it is or anything. The dog chase got both of us very disoriented. I didn’t have the faintest of clues, but if I got to some high point then maybe I would be able to see it, I just need to find the lake, and then I would be set and should be able to get back."
    
    mc "I think that our best bet is to get to some high ground to find out where the lake is. Finding the lake will make it much easier to find the camp. Do you know what place where we would have a view of the surrounding area?"
    R "Yeah good idea, I don’t think that it should be too hard to climb up a hill and get a view of the surroundings, alternatively though, you could just climb one of the trees, if you know how to climb them that is, along with a bad ankle of course."
    mc "Well hill it is then since I don’t know how to climb trees and a bad ankle would make things way too hard to learn now."

    #Chapter 4
    "It was finally time to leave the attic, time to set off home. A sense of hope washed over me, it was always noise to have a plan, hopefully, there will be no more encounters with any wildlife. As we departed from the shack, we were both illuminated under the night sky."
    "It wasn’t a typical skyline where all the stars were covered by clouds, only peeking from time to time like we had been used to. No, tonight was different, there wasn’t a single cloud in the sky, no light pollution, just tonnes of sparkling stars in the sky surrounding a large hypnotizing full moon."
    "Tonight was special. The only tall hill that would allow us to see the surrounding area that Klara knew of was about a few minutes walk from where we were. With my ankle, it would take a bit longer but shouldn’t have too much of an impact."
    "Thankfully my ankle was recovering. Klara started skipping along ahead of me. How did she have so much energy to skip. I have no idea. It made me realize that I didn’t even know what time it could possibly be."
    "How long was I out for initially, how long had I spent with Klara, time was all a blur. Only the moon directly above us gave some sort of sense of time."
    R "It really is a beautiful night, you picked the best night to be bullied on. Nights like these used to be the best for getting rid of all the stress. For a while it used to help so much, yet ended up causing all the problems in the end."
    "Her voice trembled with the delivery of that last line. Klara was still a large mystery to me, sometimes she would talk about the forest with so much passion and love, but that passion would turn to sadness and despair very easily. The forest helped her a lot but also caused her the most problems."
    R "I used to feel so motivated, so hopeful, so full of life. I used to want to become an environmentalist to help protect this forest and many forests like it, forests that helped other people like me. Those times were much better."
    mc "What happened that made you change your mind? At times, you’re in love with this forest and at other times, the forest seems to almost bring you to tears."
    R "I don’t want to talk about it too much, because the reason is weird. I wish that I had a particular reason and could just blame it all on that. But I don’t have that. I have nothing to blame, it all just happened, no cause and effect, just bam there you go all of your feelings."
    R "Suddenly you no longer care, suddenly there is nothing that makes you feel any more if you try really hard then you’ll manage to make yourself feel pain. For some reason after not feeling anything but guilt for a while that pain seduces you, makes you want more."
    R "For a few seconds, you feel alive and happy, but after you’re left with guilt and more self-hate. You try to get that passion for things back, even trying to get that passion back in itself is difficult, and after pushing yourself so hard, only to not be able to get it back hurts a lot."
    R "It brings intense numbness. Have you ever felt so numb, where you would try anything to feel again?"

    # This ends the game.

    return
