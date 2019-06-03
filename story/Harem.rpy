define salien = Speaker('Alien', voice_woman, color='#b4b1ce')
define kzoey = Speaker('Kiyoshi', voice_child, color='#eed25d')
define ubrad = Speaker('Brad', voice_girl, color='#fef4ae')
define bradley = Speaker('Bradley', voice_girl, color='#fef4ae')
# define rileyGB = Speaker('Pauline', voice_woman, color='#b4b1ce')
define slave1 = Speaker('Clone1', voice_woman, color='#cdcdd0')
define slave2 = Speaker('Clone2', voice_woman, color='#c6c4da')

label scenario_Harem:
    $ timer_range = 0
    $ timer_jump = 0
    $ rileyGB.name = "pauline"

    $ Family = False
    $ Teachers = False
    $ Cheerleaders = False

    scene black
    with dissolve
    routename "Introduction"
    with dissolve
    scene bg main room day
    connie "Kiyoshi! Kiyoshi!"
    kiyoshi "Yeah..."
    outfit connie formal
    show connie a_0 at left, faceright with easeinleft
    "This is my mother, her name is Connie, and her friends call her Connie. She lives with just me and my two sisters, since Dad died seven years ago."
    connie "Kiyoshi, You'll be late for school! Get up!"
    kiyoshi "Ok mom, I'm going! Jeez, you're really impatient."
    connie "Kiyoshi, you have 10 minutes left to get to class, or you'll be late! Get up now!"
    show kiyoshi a_1 at center, faceleft
    with dissolve
    connie "I've left breakfast for you in the kitchen."
    kiyoshi "Thanks mom!"
    hide kiyoshi with moveoutleft
    scene black
    with dissolve
    scene bg main kitchen day
    outfit natalie casual
    outfit flavia uniform
    show flavia a_1 at center, faceleft
    show natalie a_0 at centerright, faceleft
    "There are my two sisters, Natalie and Flavia. The bluenette is my younger sister, Natalie. She still acts like a 9 year old, even if she's 17."
    "The blonde bombshell at her right is Flavia, my big sister. She's currently studying Sports Medicine at the Sanfransokyo Community College."
    show kiyoshi a_1 at centerleft, faceright with easeinleft
    kiyoshi "Hi Flav, hi midget! Don't got time to talk, I'm going to be late!"
    natalie "Like always bro, Teehee!"
    flavia "Have a nice day!"
    kiyoshi "You too!"
    hide kiyoshi with moveoutright
    scene black
    with dissolve
    scene bg main house day
    outfit scarlet casual
    show scarlet a_0 at center, faceleft
    "On my way to school, I saw Scarlet, my next door neighbour. She's a total cutie... Shame she's never been interested in me..."
    scene black
    with dissolve
    scene bg school entrance day
    outfit leona casual
    show leona a_0 at center, faceleft
    "One of the teachers, Miss Leona, is standing near the entrance. Probably to make sure that nobody that comes late enters scot free."
    show kiyoshi a_1 at centerleft, faceright with easeinleft
    kiyoshi "Hi miss!"
    leona "Just in time Kiyoshi...  As always... "
    kiyoshi "Yes miss..."
    leona "You should really invest on an alarm clock, because one minute later, and I would have had to put you in detention."
    kiyoshi "Maybe I will, miss."
    hide kiyoshi with moveoutright
    scene black
    with dissolve
    scene bg school classroom hallway day
    outfit yui casual
    outfit cassie casual_d
    show yui a_0 at center, faceright
    show cassie a_0 at centerright, faceleft
    "My crush Cassie, the head cheerleader is standing right of the entrance door to class, talking with her friend Yui, one of the other Cheerleaders."
    show kiyoshi a_1 at centerleft, faceright with easeinleft
    "I decided to not talk to them, taking into account my... other attempts, and entered the classroom."
    hide kiyoshi with moveoutright
    scene black
    with dissolve
    scene bg classroom 3 day
    show sayaka a_1 at center, faceright
    show allison a_0 at centerright, faceleft
    "Sayaka, And her best friend Allison, were as always, sitting in front of me. They... Do not like me all that much."
    show kiyoshi a_1 at left, faceright with easeinleft
    pause 1.0
    outfit yuuna casual
    show yuuna a_0 at right, faceleft with easeinright
    "Miss Yuuna, my homeroom teacher came into the room, and the first lesson of the day started."
    "The time passed to me quite quickly, as if it were mere seconds."
    "The bell chimed, signaling that it's the end of the first lesson of the day."
    "We had a little, 10 minute break, before the next class started."
    hide kiyoshi with moveoutleft
    scene black
    with dissolve
    scene bg school school stairs day
    outfit Harem_catherine whistle
    show mel b_0 at center, faceleft
    show irene b_0 at centerright, faceleft
    show Harem_catherine a_0 at centerleft, faceright
    "I decided to go into the hallway, to get some fresh air during the break."
    "Two girls, Mel and Irene, were talking to the gym teacher, Catherine."
    "Mel is the short, and spunky one. I like her, but her accent is a bit of a turn-off. Not that there's anything wrong with country girls..."
    "Irene is the tall one. There's rumours around the school that say that she sometimes goes to the cemetery at night... She likes her goth fashion too much."
    "Catherine, the teacher... Almost nobody knows anything about her. From what I can tell of her, at least, she's a total hottie..."
    "I looked at my watch. I coudl see that it's almost time to go back to class, so I went back."
    scene black
    with dissolve
    scene bg classroom 3 day
    show tori a_0 at center, faceright
    show vanessa a_0 at centerright, faceleft
    "When I got into class, I was a bit surprised. Tori and Vanessa, two girls that also go to the cheerleader team, were in ther seats."
    "The surprising thing, is that they were in class at all, considering they play hookie almost twice a week. It's no wonder they got hold back so much, they should be finishing college!"
    show kiyoshi a_1 at left, faceright with easeinleft
    pause 1.0
    outfit abby suit
    show abby a_0 at right, faceleft with easeinright
    "Miss Luten, the Economics teacher entered the room, and the next lesson started."
    "Time passed to me really slowly, I was getting drowned in lessons that were too boring... It's always been said that Abby is not the best of teachers..."
    "The bell rings,signaling the end of the day."
    hide kiyoshi with moveoutleft
    scene black
    with dissolve
    scene bg school entrance dusk
    show kiyoshi a_1 at center, faceright with easeinright
    "It's time to go home."
    "I was going to go through the usual way, but they were doing renovations on it. I could go through two other paths, that are slightly longer."
    "I could go straight through the park, on the left of here, or go through the hills that are on the right."
    menu:
        "I decided to pass by..."

        "{s}The fields{/s} (Currently under renovation)":
            jump scenario_Remote

        "The park":
            jump scenario_Magic

label scenario_Magic:
    routename "Magic Book"
    hide kiyoshi with moveoutright
    scene bg park dusk
    with dissolve
    outfit kiyoshi casual
    outfit anuja exotic
    show anuja a_2 at centerleft, faceright
    "I'm on my way to home after school, when I saw this indian girl, in a strange costume."
    "She look like she is scared of something... There also was a hole in the ground, at her feet."
    anuja "I think it's time to finish with you... you caused too much damage to my life..."
    anuja "Farewell, you wretched book!"
    show anuja:
        ease 1.0 yanchor 0.7
    "After she said that, she threw something small into the hole, and covered it with nearby dirt."
    show anuja:
        ease 1.0 yanchor 1.0
    anuja "I hope you will forget me, and the people you hurt!"
    "She say while she throws more dirt on the hole."
    pause 1.0
    hide anuja with moveoutright
    "As she finished hiding the hole, she ran away, through the side of the park."
    show kiyoshi a_1 at centerleft, faceright with easeinleft
    "My curiosity is killing me... Nobody would do something like that without a reason, and whatever it was, may be better underground..."
    "But, on the other side... How bad could it be?"
    "I decided to dig whatever it is she burrowed."
    show kiyoshi:
        ease 1.0 yanchor 0.7
    pause 0.3
    show kiyoshi:
        ease 1.0 yanchor 1.0
    kiyoshi "What? A book?"
    kiyoshi "It looks strange... Maybe I should take it home, to investigate it."
    hide kiyoshi with moveoutleft
    "The road home wasn't that interesting, just said hi to some friendly neighbours."
    "Sadly, Scarlet didn't notice me... She was almost ignoring me at this point..."
    scene black
    with dissolve
    scene bg main room dark
    show kiyoshi a_1 at centerleft, faceright with easeinleft
    "After I arrived in my room, I opened the book."
    "It looked old, the paper worn out, almost like the exact description of a magic book you'd get on a trashy fantasy romance novel, or a perverted visual novel."
    "The table of contents mentioned three major parts; Alchemy, Summoning, and Dark Magic."
    menu:
        "Which part of the book should I check out first?"

        "Potions":
            routename "Potions"
            show kiyoshi a_3
            "I read the first chapter of the book..."
            "It described countless potions, from poisons, to dyes, to actual magical concoctions... If the book is to be trusted."
            kiyoshi "There are a lot of recipes for potions in this book..."
            kiyoshi "And the ingredients are easy to find, I probably have everything I need in the kitchen..."
            kiyoshi "What can I lose by trying this out?"
            hide kiyoshi with moveoutleft
            scene black
            with dissolve
            scene bg main kitchen dark
            show kiyoshi a_1 at centerleft, faceright with easeinleft
            "I opened the book, in a random page of the first chapter, it showcased the names and recipes of two specific potions."
            "The first one, was called the {q}Draft of Infatuation{/q}... Using a thesaurus, I could determine that it probably is a Love potion."
            "The second one was called the {q}Potion of Polymorph{/q}, and that I didn't have to look up, anyone that has ever watched Henry Porter should know that It's a transformation potion."
            menu:
                "Which one should I try to make?"

                "The Love Potion":
                    routename "Love potion"
                    jump scenario_Love_Potion

                    "End for now"
                    placeholder

                "The Transformation Potion":
                    routename "Polymorph juice"
                    jump scenario_Polymorph

                    "End for now"
                    placeholder

        "Summoning":
            routename "Summoning"
            show kiyoshi a_3
            "I opened the second chapter of the book."
            kiyoshi "There is just a small sentence in a bizarre language..."
            kiyoshi "It says something like {spell}Circe Ngiyakumemeza, woza lapha wenze isifiso sami sibe ngokoqobo{/spell}?"
            with hpunch
            show white as white_flash:
                additive_flash(0.5)
            show kiyoshi a_5
            "Suddenly, I felt something... A surge of energy got out of the book..."
            show circe a_0 at centerright, faceleft
            "And a strange, woman like figure appeared!"
            "She looked completely wicked, with pale purple skin, and horns on the top of her head!"
            "I don't need to be an expert, to know that I'm dealing with a demon!"
            with dissolve
            with hpunch
            show white as white_flash:
                additive_flash(0.5)
            circe "KYAHAHAH!"
            circe "I'm here to make one of your wishes come true!"
            pause 1.0
            show kiyoshi a_3
            kiyoshi "I'm sorry, what?"
            pause 1.0
            show circe a_1
            circe "What?! You summon a demon, knowing full well that we tend to be grateful for being released, and you question why I would grant you a wish?!"
            show kiyoshi a_1
            kiyoshi "Sorry, I guess?"
            kiyoshi "Anyhow, will you really grant any wish?"
            show circe a_5
            circe "Yeah... Whatever you want!"
            pause 1.0
            "This decision could give me anything I ever wanted... I took some time to think."
            pause 1.0
            menu:
                "What should I wish for?"

                "{s}I wish that all women to now love...  Crave...No, need the taste of cum more than anything!{/s}":
                    show circe a_3
                    circe "Ah, truly a classic! I love the timelines where that happens!"
                    circe "Wish granted! It's time for me to enjoy my freedom!"
                    with hpunch
                    show white as white_flash:
                        additive_flash(0.5)
                    hide circe
                    with dissolve
                    with hpunch
                    show white as white_flash:
                        additive_flash(0.5)
                    "She disappeared in a flash of light, leaving only me, and the sounds of the night to keep me company."
                    "I wonder, did the wish really work?"
                    placeholder

                "I wish that anyone who orgasmed while having a fantasy of a certain person, would swap with that certain person!":
                    routename "FOSE"
                    show circe a_3
                    circe "Interesting choice... Don't go fantasizing about me, you pervert!"
                    circe "Wish granted! It's time for me to enjoy my freedom!"
                    with hpunch
                    show white as white_flash:
                        additive_flash(0.5)
                    hide circe
                    with dissolve
                    with hpunch
                    show white as white_flash:
                        additive_flash(0.5)
                    "She disappeared in a flash of light, leaving only me, and the sounds of the night to keep me company."
                    "I wonder, did the wish really work?"
                    jump scenario_FOSE

                "I wish for unlimited wishes!":
                    routename "Wishing Fun"
                    show circe a_3
                    circe "Ah, truly a classic! I can only imagine what you will do, mortal!"
                    circe "You can grant anywish you want with the words {spell}I wish{/spell}, as to not have me be here to grant every wish."
                    circe "Have fun! Kyahaha!"
                    with hpunch
                    show white as white_flash:
                        additive_flash(0.5)
                    hide circe
                    with dissolve
                    with hpunch
                    show white as white_flash:
                        additive_flash(0.5)
                    "She disappeared in a flash of light, leaving only me, and the sounds of the night to keep me company."
                    "I wonder, did the wish really work?"
                    jump scenario_Wish

        "{s}Dark magic{/s}":
            placeholder

label scenario_Love_Potion:
    show kiyoshi a_6
    kiyoshi "Let's try to make a Love Potion!"
    kiyoshi "This probably won't backfire in any way possible!"
    "While I prepared the potion, I read the book, to see how it works..."
    nvl clear
    manu "{b}Draft of Infatuation{/b}"
    manu "Anyone who is't drinks a loveth potion shall falleth in loveth with the first p'rson those gents seeth."
    manu "This potion's effects art unlimit'd in timeth, the p'rson shall beest in loveth f'rev'r, and ev'r."
    manu "Requires an av'rage of 8 hours of preparation."
    kiyoshi "Let's do this!"
    pause 1.0
    scene bg main kitchen day
    show kiyoshi a_1 at centerleft
    pause 1.0
    "After some hours rigurously mixing and adding ingredients, and drinking coffee like a madman, to stay awake, I finally finished it..."
    kiyoshi "I think it's done..."
    kiyoshi "But who to test it on?"
    menu:
        "I should try it, but on who?"

        "{s}Stay home and test it on my family{/s}":
            placeholder

        "{s}Find someone at school{/s}":
            placeholder

        "{s}Go out{/s}":
            placeholder

label scenario_Polymorph:
    show kiyoshi a_6
    kiyoshi "Let's try to make a transformation potion!"
    "While I started preparing the potion, I read the book, to see it's effects..."
    nvl clear
    manu "{b}Potion of polymorph{/b}"
    manu "Anyone whomst drinks a potion of polym'rph shall transf'rm in a p'rson whose hair hast been did mix with the juice."
    manu "Thee needeth to putteth the hair in the potion aft'r the preparation, 'r t wonneth't w'rk."
    manu "This potion's effects art limit'd in timeth, the p'rson shall beest transf'rm'd f'r 6 hours, aft'rwards being transf'rm'd backeth."
    manu "Require an av'rage of an hour of preparation."
    kiyoshi "Let's do this!"
    pause 2.0
    show kiyoshi a_1
    "After mixing, mashing, and combining the ingredients of the potion in a way that would make {q}The Crossbreed Princess{/q} blush, I proudly looked at my concoction."
    kiyoshi "I think it's done."
    kiyoshi "I should take some hairs from somewhere around the house..."
    menu:
        "But where should I take it from?"

        "Take hair from the bathroom":
            "I took some hairs from the brush both of my sisters use... I can't see it quite clearly, so I don't know who it's from..."
            kiyoshi "Let's take the hair, But just in case, I should try the potion in my bedroom."
            kiyoshi "Don't want mom to open the door while I turn into her, or something among those lines."
            hide kiyoshi with moveoutleft
            scene black
            with dissolve
            scene bg main room dark
            show kiyoshi a_1 at centerleft, faceright with easeinleft
            kiyoshi "So I have the hair... Do I just pop it into the potion?"
            "So I did, and shook it a round for a bit, until the potion started changing colours on it's own"
            kiyoshi "Woah, it's a bit hypnotic..."
            kiyoshi "I think it's done, I should test it right away..."
            "I chugged the drink, harder than I've ever chugged a drink before..."
            kiyoshi "Tastes like hair..."
            "Then something began to happen."
            morph begin magic kiyoshi flavia nude a_4
            kiyoshi "...Ahhh..."
            "The transformation felt better than anything I've ever felt in my life... I could notice my bones shifting, my muscle mass changing, but it caused no pain at all..."
            "My hair flared out, and became lighter, going from my usual dark shade, to a blonde colour..."
            kiyoshi "I feel something coming..."
            morph do
            "That would be a pair of breasts, emerging from my chest, and ripping through my shirt. I decided to quickly get naked to avoid that happening anymore."
            kiyoshi "..Mmhhh..."
            kiyoshi "I feel so strange.. It's, like, all my body is changing into something very different..."
            "A final change happened to my body, as I could feel a great pressure in my crotch..."
            "I slid my hand down, while moaning in the pleasure of the transformation, to check what was happening..."
            "I was too late, as for when my hand reached, there was nothing there..."
            kiyoshi "Huh?"
            "Well, nothing was not quite the correct word, as I accidentally discovered when one of my fingers slid into my new vagina."
            kiyoshi "...Mmmph!"
            "This felt great! I could have possibly continued for hours on end!"
            "I massaged my slit with my fingers, gently sliding in, and out, at a steady pace..."
            "I could feel myself getting closed, until, until!"
            "I came. Hard"
            morph end
            kiyoshi "Woah... This feels positively amazing... But who have I become?"
            show kiyoshi a_7 blush
            kiyoshi "I've fapped as my big sister?!"
            placeholder

        "Take hair from the livingroom":
            "I found a bunch of red hairs, probably from when mom held the book club meeting this afternoon."
            kiyoshi "Let's take the hair, But just in case, I should try the potion in my bedroom."
            kiyoshi "Don't want mom to open the door while I turn into her, or something among those lines."
            hide kiyoshi with moveoutleft
            scene black
            with dissolve
            scene bg main room dark
            show kiyoshi a_1 at centerleft, faceright with easeinleft
            kiyoshi "So I have the hair... Do I just pop it into the potion?"
            "So I did, and shook it a round for a bit, until the potion started changing colours on it's own."
            kiyoshi "Woah, it's a bit hypnotic..."
            kiyoshi "I think it's done, I should test it right away..."
            "I chugged the drink, harder than I've ever chugged a drink before..."
            morph begin magic kiyoshi scarlet nude a_28
            kiyoshi "...Ahhh..."
            "The transformation felt better than anything I've ever felt in my life... I could notice my bones shifting, my muscle mass changing, but it caused no pain at all..."
            "My hair flared out, and became lighter, going from my usual dark shade, to a more reddish one..."
            kiyoshi "I feel something coming..."
            morph do
            "That would be a pair of breasts, emerging from my chest, and ripping through my shirt. I decided to quickly get naked to avoid that happening anymore."
            kiyoshi "..Mmhhh..."
            kiyoshi "I feel so strange.. It's, like, all my body is changing into something very different..."
            "A final change happened to my body, as I could feel a great pressure in my crotch..."
            "I slid my hand down, while moaning in the pleasure of the transformation, to check what was happening..."
            "I was too late, as for when my hand reached, there was nothing there..."
            kiyoshi "Huh?"
            "Well, nothing was not quite the correct word, as I accidentally discovered when one of my fingers slid into my new vagina."
            kiyoshi "...Mmmph!"
            "This felt great! I could have possibly continued for hours on end!"
            "I massaged my slit with my fingers, gently sliding in, and out, at a steady pace..."
            "I could feel myself getting closed, until, until!"
            "I came. Hard"
            morph end
            kiyoshi "Woaw! This feels positively amazing! ...But who am I?"
            show kiyoshi a_4 blush
            kiyoshi "I've masturbated as the hottie next door?!"
            placeholder

label scenario_FOSE:
    show kiyoshi a_1
    kiyoshi "So if it works, anyone will swap bodies with the person they think to while cumming..."
    kiyoshi "Cool!"
    timedchoice 5 FOSE_Taking_Over
    menu:
        "Now, what should I do?"

        "{s}Someone fantasized about someone in the house!{/s}":
            "End for now"
            placeholder

        "Kiyoshi decided to fantasize about someone":
            kiyoshi "I want to swap with someone, just to see what it's like..."
            show kiyoshi a_6
            kiyoshi "I think it's time to bust a nut like I've ever busted one before!"
            menu:
                "But who could I think of?"

                "Maybe a famous singer":
                    routename "Fose Singer"
                    show kiyoshi a_1
                    "I start the act of self pleasuring... Looking for some leaked pictures of an idol while I start jacking off."
                    pause 1.0
                    "I some nudes of an idol, called Erin Love, I decide to focus on her perfect, soon to be mine, body..."
                    pause 1.0
                    kiyoshi "Oh fuck... I'm cumming...!"
                    with hpunch
                    "As I nut, I feel like my soul is being sucked away from my body, exiting through my penis... It feels really weird."
                    outfit Harem_erin swimsuit
                    show Harem_erin a_14:
                        pos (1.2, 0.0)
                    swap kiyoshi a_5 : a_9, Harem_erin a_14 : a_5
                    "While I'm being sucked into the singer's body, I see a spirit entering mine... Certainly Erin Love herself!"
                    scene black
                    with dissolve
                    scene bg beach shore night
                    "I find myself being absorbed into the beach, sucked into the fallen body of the Singer."
                    body faith Harem_erin
                    outfit faith swimsuit
                    show faith a_8 at center
                    show kiyoshiGhost a_1:
                        pos (1.2, 0.0)
                    possess kiyoshi faith a_9
                    kiyoshi "WOAH!"
                    pause 1.0
                    show kiyoshi a_7
                    kiyoshi "It worked! I'm her!"
                    show kiyoshi a_6
                    kiyoshi "Woah, my voice.. My voice is beautiful!"
                    "My voice is very good to hear, but for now, I shift focus to my sexy, and new shape."
                    show kiyoshi a_13
                    "I look at my hands and my breasts, and it look like I'm wearing a bikini..."
                    kiyoshi "I look so sexy like this!"
                    kiyoshi "Let's look lewder!"
                    "I stripped down, quickly removing both pieces of the bikini."
                    outfit kiyoshi nude
                    "I carress my body with my new hands..."
                    show kiyoshi b_6
                    kiyoshi "Everything feels so soft..."
                    show kiyoshi b_5
                    kiyoshi "I love it..."
                    "Hearing her voice escaping from my lips, giving out moans of pleasure, Is awesome."
                    pause 1.0
                    show kiyoshi b_6
                    kiyoshi "I think I should explore her life a little bit, I want to see what is like to be a star!"
                    "Now, where did she leave her clothes?"
                    hide kiyoshi with moveoutleft
                    scene black
                    with dissolve
                    scene bg beach rock night
                    "After searching for a bit, I found them"
                    "It seems that she left her clothes here, on a rock, for anyone to take... Like me!"
                    show kiyoshi b_7 at centerleft, faceright with easeinleft
                    kiyoshi "I should dress up, no need to ruin my new life!"
                    outfit kiyoshi casual
                    show kiyoshi a_7
                    kiyoshi "So I'm a famous sexy Idol thanks to my wish! It's awesome... Anyone who look at me will only see Erin Love!"
                    "I look another time at {b}my{/b} body, and carress it, squeezing {b}my{/b} breasts in the process."
                    "I think I should go to {b}my{/b} home... But where does she even live?."
                    "After a quick search on her phone, I found where she lives."
                    kiyoshi "Let's go {q}home{/q}."
                    scene black
                    with dissolve
                    scene bg katrina livingroom night
                    outfit Harem_amelia casual
                    show Harem_amelia a_5 at centerleft
                    "A beautiful woman is standing in the livingroom of the villa, She probably is my new mother, Kukuku..."
                    show kiyoshi a_7 at centerright, faceright with easeinright
                    Harem_amelia "Oh Erin! How are you Honey?"
                    placeholder

                "{s}My crush, Cassie, the head cheerleader.{/s}":
                    placeholder

                "Look for porn":
                    routename "Fose Porn star"
                    show kiyoshi a_1
                    "I start to masturbate... looking at some porn at the same time."
                    pause 1.0
                    "I focus on a young sexy actress..."
                    pause 1.0
                    kiyoshi "Oh fuck... Here comes!"
                    with hpunch
                    "As I start blasting rope, I feel like my soul is being sucked away from my body, through my penis... This feels incredibly weird."
                    outfit Harem_monica dominatrix
                    show Harem_monica a_2:
                        pos (1.2, 0.0)
                    swap kiyoshi a_5 : a_2, Harem_monica a_2 : a_5
                    "While I'm being moved, I see a ghost entering my body... Certainly the porn star I nutted to."
                    scene black
                    with dissolve
                    scene bg connie bedroom messy dark lights on
                    "I get sucked into an apartment..."
                    body faith Harem_monica
                    outfit faith dominatrix
                    show faith a_5 at center
                    show kiyoshiGhost a_1:
                        pos (1.2, 0.0)
                    possess kiyoshi faith a_2
                    kiyoshi "WOAH!"
                    pause 1.0
                    show kiyoshi a_9
                    kiyoshi "It worked! I'm her!"
                    "I look at my hands and my breasts, it look like I'm wearing some dominatrix outfit... She probably is a very naughty girl..."
                    outfit brad casual
                    show brad a_4 at centerleft
                    with dissolve
                    show kiyoshi a_13
                    brad "What worked Monica? Are you ready?"
                    "There is a man in the appartment with me... I wonder who he is..."
                    show kiyoshi a_1
                    kiyoshi "Ehhh.. Ready for what?"
                    show brad a_0
                    brad "Ready for the show, babe! Did you forget why you are dressed like that?"
                    show kiyoshi a_2
                    "I inmediately understood what was going on, I swapped with her just before the filming of a {q}movie{/q}!"
                    kiyoshi "Ermm... Excuse me I don't really feel so good... I should go, bye!"
                    hide kiyoshi with moveoutleft
                    show brad a_4
                    "As I said that, I ran to the door and went out of the building."
                    brad "Eh! Come back!"
                    scene black
                    with dissolve
                    scene bg city walkway night empty
                    show kiyoshi a_1 at centerleft, faceright with easeinleft
                    kiyoshi "So I'm in a porn star's body... In a dominatrix outfit... On the street during the night... I probably look like a cheap whore right now!"
                    kiyoshi "What should I even do!?"
                    placeholder

label FOSE_Taking_Over:
    routename "Fose Taking over"
    "I'm thinking abot what to do when suddenly, I feel like my soul is being sucked away from my body!"
    outfit connie sweater
    show connie a_7:
        pos (1.2, 0.0)
    swap kiyoshi a_5 : a_6, connie a_7 : a_3
    "While I move, I see a ghost entering my body... But we move too fast, and I can't identify the person... I just see them enter my body."
    scene black
    with dissolve
    scene bg leona room dark
    "I'm moved in the dark and can't see anything..."
    body faith connie
    outfit faith sweater
    show faith a_7 at center
    with dissolve
    show kiyoshiGhost a_5:
        pos (1.2, 0.0)
    possess kiyoshi faith a_6
    kiyoshi "What is going on? I fell really weird..."
    pause 1.0
    kiyoshi "Boobs?!..."
    "I say as I touched my new body..."
    show kiyoshi b_3
    pause 1.0
    "I feel something on my skin, I decide to remove it to have full access to my new body..."
    outfit kiyoshi nude
    pause 1.0
    show kiyoshi b_4
    "I can't see anything with the lights off but I feel something wet down here..."
    show kiyoshi b_3
    "I move my hands to feel the wetness and it look like my dick is gone! I have a pussy!"
    show kiyoshi b_6
    "I put a finger in my new pussy..."
    kiyoshi "MMmmhhh.... this feels awesome..."
    show kiyoshi b_2
    "I start to massage my new breasts... I've never felt something like this before..."
    kiyoshi "Fuck yes it feels {b}so{/b} good!"
    pause 2.0
    "I continue exploring the unexplored about myself, when suddenly..."
    scene bg leona room night
    show kiyoshi b_3 at center
    show kiyoshi:
        faceleft
    "The lights turned on and I heard my voice..."
    connie "What is going on here!?"
    show connie a_5 at centerleft, faceright with easeinleft
    "I look down at the room and at my body... I think I just masturbated as mom... Ewww...."
    placeholder

label scenario_Wish:
    show kiyoshi a_6 at centerleft, faceright
    kiyoshi "I should test my new power, Hehe!"
    kiyoshi "{spell}I wish that my crush Cassie appeared in my bedroom!{/spell}"
    outfit cassie gown
    show white as white_flash:
        additive_flash(0.2)
    show cassie b_7 at centerright, faceleft
    with dissolve
    "There is a little flash of light, and Cassie appears in her night gown."
    cassie "Mmhh... What?!..."
    "It seem that she was sleeping..."
    show cassie b_6
    pause 1.0
    show cassie b_3
    cassie "Kiyoshi?! What the...?!"
    "She look at the room but before she can say sanything, I make my second wish."
    kiyoshi "{spell}I wish that Cassie was my slave!{/spell}"
    cassie "What are yo..."
    show white as white_flash:
        additive_flash(0.2)
    show cassie b_7
    pause 1.0
    show cassie b_5
    cassie "Hi master!"
    kiyoshi "Awesome!"
    "I wanted her since long ago... And now I have her!"
    "If only I could have more of her... Wait!"
    kiyoshi "{spell}I wish that two other Cassies  appeared in my bedroom as slaves!{/spell}"
    clone amy cassie
    clone carrie cassie
    show white as white_flash:
        additive_flash(0.2)
    show amy b_5 at center, faceleft
    with dissolve
    show white as white_flash:
        additive_flash(0.2)
    show carrie b_5 at right, faceleft
    with dissolve
    slave1 "Hi master!"
    slave2 "Hi master!"
    kiyoshi "Oh fuck! It's a dream come true!"
    pause 1.0
    kiyoshi "{spell}I wish that they were naked!{/spell}"
    show white as white_flash:
        additive_flash(0.2)
    outfit cassie nude
    outfit amy nude
    outfit carrie nude
    kiyoshi "It's better than in my wildest fantasy!"
    show kiyoshi a_1
    menu:
        "What should I do?"

        "Have fun with my new slaves":
            kiyoshi "Cassie Prime come here and suck me off... And you two, kiss eachother and play with your tits for me!"
            show cassie b_1 blush
            cassie "As you want, Master!"
            show cassie b_0 blush
            show kiyoshi behind cassie
            show kiyoshi:
                ease 1.0 yanchor 0.7
            show cassie:
                faceleft
                ease 1.0 xpos 0.34 yanchor 0.4
            "Cassie got on her knees ans started licking my cock's head..."
            show carrie behind amy
            show carrie a_5 blush
            show amy b_5 blush:
                faceright
                ease 1.0 xpos 0.8
            "And the two clones start to kiss passionately..."
            "Cassie started moving on my dick, inserting it into her mouth."
            show cassie b_1 blush
            show cassie:
                ease 0.2 xpos 0.34 yanchor 0.2
                pause 1.0
                block:
                    ease 0.2 xpos 0.335
                    pause 1.2
                    ease 0.2 xpos 0.345
                    repeat
            cassie "Mmmmfhh...mmph...mmfhhh."
            kiyoshi "Oh yeah!.. Don't stop!"
            show carrie a_7 blush
            show amy b_4 blush
            "The two clones play with themselves, at the display that Cassie Prime is putting..."
            kiyoshi "Don't worry, you two will get your turn soon..."
            placeholder

        "{s}Leave them for now, and wish more stuff{/s}":
            kiyoshi "Stay here for now."
            hide kiyoshi with moveoutleft
            scene black
            with dissolve
            scene bg main kitchen dark
            show kiyoshi a_1 at centerleft, faceright with moveinleft
            placeholder

label scenario_Remote:
    routename "The meeting"
    hide kiyoshi with moveoutright
    scene bg sky dusk
    with dissolve
    outfit kiyoshi casual
    $ meteor = meteor_particles(1200, head_particle_blue, tail_particle_blue)
    show expression meteor as meteor:
        transform_anchor True
        subpixel True
        rotate -35
        xzoom 0.15 yzoom 0.35
        pos (0.90, 0.0)
        linear 2.0 pos (0.75, 0.15 * (16.0 / 9.0) * math.tan(35 * math.pi / 180.0)) xzoom 0.30 yzoom 0.70
    "I'm on my way to home after school, when I saw a meteor trailing along sky"
    show expression meteor as meteor:
        linear 2.0 pos (0.60, 0.30 * (16.0 / 9.0) * math.tan(35 * math.pi / 180.0)) xzoom 0.45 yzoom 1.05
    show white as white_flash:
        additive_flash(0.5)
    show expression meteor as meteor:
        linear 2.0 pos (0.45, 0.45 * (16.0 / 9.0) * math.tan(35 * math.pi / 180.0)) xzoom 0.6 yzoom 1.4
    show expression meteor as meteor:
        linear 2.0 pos (0.30, 0.60 * (16.0 / 9.0) * math.tan(35 * math.pi / 180.0)) xzoom 0.75 yzoom 1.75
    kiyoshi "It looks like it's coming in my direction!"
    show white as white_flash:
        additive_flash(0.4)
    pause 0.8
    show white as white_flash:
        additive_flash(0.3)
    pause 0.6
    kiyoshi "I have to run!"
    show white as white_flash:
        linear 1.2 alpha 1.0
    pause 1.5
    scene white
    with dissolve
    "But before I knew it, something... Activated in the meteor, and a light enveloped. I soon felt a sudden loss of gravity."
    "I was really afraid, for my life..."
    "But, on the other hand, I was probably going to meet real aliens!"
    "I just hope they don't probe me..."
    scene black
    with dissolve
    "A powerful force then lifted me skywards, and everything went dark."
    pause 2.0

    scene bg space command
    routename "Alien meeting"
    show kiyoshi a_0 at centerright, faceleft
    with dissolve

    "I awoke in what appears to be an alien containment module."
    "Judging from the various monitoring and medical equipments nearby, I surmise that I am in an alien research vessal."
    "A sliding door opened. As if responding to my regaining consciousness, and a slender being approach from the distance."
    show serena a_0 at centerleft, faceright with moveinleft
    pause 1.0
    show kiyoshi a_6
    kiyoshi "WOW! Are you an alien? Because you have just abducted my heart..."
    show serena a_2
    salien "Hee..."
    "The alien smiled and began to speak."
    show serena a_0
    show kiyoshi a_1
    salien "Greetings, Terrian. We thank you for the valuable data your examination have provided for our kind"
    salien "Our Queen Mother, praise be unto her, has also found you most amusing"
    salien "Therefore, you have made an ideal candidate for the second iteration of our post-examination alien studies program yet on this planet"
    show kiyoshi a_6
    kiyoshi "What the fuck are you talking about?.. second iteration of what?.."
    show serena a_8
    salien "I will give you a device, use it in the way you want, we will observe you"
    salien "And don't forget to read the manual"
    show kiyoshi a_3
    show serena a_2
    "I should take the device"
    show kiyoshi a_1
    kiyoshi "Very well, I accept this mission"
    show serena a_0
    "The alien then handed me the device and a detailed list of instructions"
    salien "This is the newest model of the {q}device{/q} as our Queen Mother has requested for your use"
    salien "Until the experimentation process is over, we will not be allowed to make contact or provide any aid"
    salien "good evening terrian.. and don't forget to have fun!"
    show white as white_flash:
        additive_flash(0.4)
    show kiyoshi:
        ease 0.5 yanchor - 0.5
    kiyoshi "Wait! At least explain me th...."
    scene black
    with dissolve
    "Before I knew what was happening, I had been sent back on the ground"
    "Are the aliens just left me a gift?"
    "A gift that will make my dreams come true."
    pause 2.0
    "I should go home now.."

    jump new_power

label new_power:
    routename "Remote_Testing"
    scene bg neighborhood night
    show kiyoshi a_1 at centerleft
    "I'm on my way to home and i can't think to anything other than this little remote"
    "I think it's time to test the feature of this remote"
    "I look at the remote and i see there are some interesting function like mind control, body swap, possession and morph.."
    "What will i choose to test the device?"
    menu:
        "Mind control":
            routename "Brainwashing test"
            "I should test the mind control, maybe on that jogger.."
            "I should hide!"
            hide kiyoshi with moveoutleft
            pause 2.0
            outfit holly track
            show holly a_0 at centerright, faceleft with easeinright
            "I push the button.."
            show holly a_6
            holly "What is goi..."
            pause 1.0
            show expression alien_particles(400, 200, 220, mind_scale) as particles:
                xpos placement_of(holly).xpos + 0.0000
                ypos 0.30
                alien_particles_fadeinout(0.75)
            show holly a_8
            "The jogger become quiet and enter a vegetative state"
            show kiyoshi a_6 at center, faceright with easeinleft
            "I think I should say something to her"
            kiyoshi "Count to 10 and continue your jogging!"
            kiyoshi "After that, you will be the slave of the first person you meet"
            "This will be interseting!"
            pause 5.0
            "I should hide to see the result, while I run I released my hold on her with another press of the command button.."
            hide kiyoshi with moveoutleft
            show holly a_3
            holly "Why have I stopped my jogging?.."
            "While she say that, a teenager is coming"
            show riley a_0 at center, faceright with easeinleft
            riley "Hi, miss!.."
            holly "Hi litt... What?.."
            show holly a_6
            "She stare at him.. like she is focusing on his shape"
            show riley a_5
            riley "eh.. are you alright miss?"
            pause 1.0
            "She look at him with insistence"
            show holly a_1 blush
            pause 1.0
            holly "Yes master, I'm alright"
            show riley a_4
            riley "Master?.."
            holly "Yes master, you are now my master and I will do anything you want me to do!.."
            riley "What? Are you joking?"
            pause 1.0
            show riley a_5
            "It look like he's thinking about something she would never do"
            riley "OK! So start to undress"
            holly "As you wish master"
            pause 1.0
            "And before he could react, she start to undress"
            outfit holly nude
            show holly a_1 blush
            show riley a_4
            "The teenager pause and look at the beautiful woman showing her body just for him.."
            riley "holy sh...! She really strip for me.."
            show holly b_1 blush
            pause 1.0
            show riley a_7
            riley "Ok come with me at my house, the real fun will began"
            holly "As you wish master"
            hide riley with moveoutleft
            hide holly with moveoutleft
            "They run out of the street"
            "Woaw that was interesting, but I'm tired, I should go sleep for now and test the device tomorrow"

            jump Harem_start

        "Body swap":
            routename "Swapping test"
            "I should test the body swap, maybe with that jogger and the teenager.."
            "I should hide"
            hide kiyoshi with moveoutleft
            pause 1.0
            outfit holly track
            show holly a_0 at centerright, faceleft with easeinright
            pause 1.0
            show riley a_0 at centerleft, faceright with easeinleft
            "When when they get closer, I push the button.."
            swap holly a_6 : a_4, riley a_5 : a_2
            holly "What is goi..."
            riley "..."
            "there is a moment of silence where they look at each other in chock"
            pause 1.0
            "The teenager in the jogger look at his body.. and more precisely the two boobs attached on his breast.."
            show riley a_1 blush
            "he start to caress them.. making a face of pure lust"
            riley "..oh yes.."
            "He say with his new adult female voice"
            show holly a_2
            "As he say that, the new teenager look at her ancient body"
            holly "..eh! don't touch my body little pervert!"
            pause 1.0
            "They look at themselves but he keep touching his boobs"
            show riley a_8 blush
            "He let out a feminime gasp"
            "The jogger in the teenager body don't react.. she's just mortified to see her body move like a pornstart on the street"
            pause 2.0
            riley "..hmm.. so sensitive..It's a dream come true.."
            hide riley with moveoutleft
            "And the teenager run away with the jogger body"
            pause 1.0
            show holly a_4
            holly "..eh! come back!"
            "She try to follow him but with her little legs it's impossible"
            hide holly with moveoutleft
            "And they run out of the street"
            "That was interesting, but i'm tired, i should go sleep and test the device tomorrow"

            jump Harem_start

        "Possession":
            routename "Posessing test"
            "I should test the possession, maybe on that jogger"
            pause 1.0
            "And I push the button.."
            exspirit kiyoshi a_5
            show kiyoshiGhost a_0
            "It worked! I'm a ghost!"
            show kiyoshiGhost a_6
            outfit holly track
            show holly a_0 at centerright, faceleft with easeinright
            "a jogger is coming, my lifeless body is behind a bush"
            "Now, let's see if I can possess her..."
            possess kiyoshi holly a_8 blush
            kiyoshi "..ah.."
            "I let out a femiminine gasp.."
            show kiyoshi a_5 blush
            pause 1.0
            show kiyoshi a_1 blush
            kiyoshi "It worked!.."
            "I say as I look at my body.. I wait no time to undress my new body, I don't care if someone see me"
            show kiyoshi a_1 blush
            "As i strip, i caress my soft body with my soft little hands.. each move is pure lust!"
            outfit kiyoshi nude
            kiyoshi "My body is so sentitive, my nipple so hard..mmmhh.."
            show kiyoshi b_1 blush
            pause 2.0
            show kiyoshi b_2 blush
            kiyoshi "..mmhhh..I'm become wet.. should I masturbate here?"
            "heard that feminine voice get out of my mouth make me more exited"
            pause 1.0
            "I'm becoming all wet down there"
            pause 1.0
            show kiyoshi b_1 blush
            "This feeling is awesome.. I want more"
            "I start masturbating on the street, let out my fluid all over the street"
            pause 1.0
            "This feel like touching the top of my dick.. but with more sensation.."
            "I feel something build inside of me.. Is it an orgasm?"
            kiyoshi "OHHHHH...YESSSSS..."
            "I cry out on the street as i orgasm in this feminine form"
            pause 1.0
            "Yes that was an orgasm! a lot of more powerful than a male orgasm.. Sooo gooooddd.."
            show kiyoshi a_3 blush
            "I look around me and I see several passerby look at me"
            "I think it's time to leave"
            exspirit kiyoshi a_5
            show kiyoshiGhost:
                faceright
                ease 1.0 xpos 0.36
            pause 2.0
            "She wake up quikly and start to massage her head on the ground"
            "She start to get up.. naked!"
            outfit holly nude
            show holly a_0:
                offscreenright
                faceleft
                ease 1.2 centerright
            holly "ohh..My head..."
            pause 1.0
            show holly a_6 blush
            holly "What was I doing?! I feel like i just orgasm...."
            show holly a_7 blush
            "As she say that, she saw that she is naked.. a look of panick appaer on her face"
            holly "HOLY SHIT WHY AM I NAKED?!"
            hide holly with moveoutleft
            "And she run out of the street"
            "That was interesting, but I'm tired, I should go sleep and test the device tomorrow"
            "I decide to return to my body and go home"
            hide kiyoshiGhost

            jump Harem_start

        "Morph":
            routename "Morphing test"
            "I should test the body morph function, maybe with that jogger and the teenager.."
            "I should hide!"
            hide kiyoshi with moveoutleft
            pause 1.0
            outfit holly track
            show holly a_0 at centerright, faceleft with easeinright
            pause 1.0
            show riley a_0 at centerleft, faceright with easeinleft
            "I copy the jogger form as she run by the teenager"
            hide holly with moveoutleft
            pause 1.0
            "When she pass the corner of the street, I press the button on the teenager"
            morph begin alien riley holly nude a_5
            riley "..ahhh.."
            riley "WHAT IS GOIND ON?!"
            morph do
            riley "..MMhhh..."
            riley "I feel so strange.. like all my body is changing to something very different.."
            morph end
            riley "What did jus.."
            show riley b_2
            riley "Woaw.. this feeling.. I feel so powerful!"
            "He pause and look down at his body"
            pause 1.0
            show riley b_2 blush
            "The teenager look affraid first, but after soome seconds he grop his new breast and a grin appear on his new face"
            show riley a_1 blush
            "He is carressing his news boobs and start to move one soft hand down his body.. approaching his pussy"
            riley "This sensation... awesome!"
            "He say with his new  sexy feminine voice"
            pause 1.0
            riley "I have boobs..oh yes.."
            riley "Am I becoming wet?!.. Just awesome"
            show riley a_0 blush
            "He start touching his vagina and his nipples when he see some passerby throwing glance at him"
            show riley a_1 blush
            riley "I think I should go show this body to my friends! They will be so jealous eheh.."
            "This look so sexy when he say that with his sexy voice"
            pause 1.0
            hide riley with moveoutright
            "And the teenager run away with the jogger body"
            "That was interesting, but i'm tired, i should go sleep and test the device tomorrow"

            jump Harem_start

label Harem_start:
    routename "Let the harem start"
    scene black
    with dissolve
    scene bg school entrance day
    "I decide to wake up and go to school as casual.. Some naughty idea come to me in my sleeping.."
    outfit kiyoshi uniform
    show kiyoshi a_1 at centerleft, faceright with easeinleft
    "The school is a good start to search for hot girl!"
    hide kiyoshi with moveoutright
    scene black
    with dissolve
    scene bg school classroom hallway day
    pause 1.0
    "Luckily, I didn't have to search for long.. A pair of familiar voices are having a conversation nearby..."
    scene black
    with dissolve
    scene bg school school stairs day
    show sayaka a_0 at centerright, faceright
    show allison a_0 at right, faceleft
    show allison a_3
    allison "...and did you see what she was wearing? {i}So{/i} awful. I'm surprised she left the house with that skanky-ass shirt on"
    show sayaka a_6
    sayaka "Yeah, and that color? I mean, ick! What was that, puke purple?"
    pause 1.0
    show kiyoshi a_1 at centerleft with easeinleft
    kiyoshi "Heeeeey ladies!"
    allison "Ack, it's that Kiyoshi again.."
    show sayaka a_5 at faceleft
    sayaka "Again? Ugh.. just fuck off already"
    show kiyoshi a_6
    "Now, let's give that command button a try"
    menu:
        "A beam run out of the remote and hit Sayaka":
            jump Remote_success

        "Something go wrong":
            jump Remote_error

label Remote_success:
    pause 1.0
    show expression alien_particles(400, 200, 220, mind_scale) as particles:
        xpos placement_of(sayaka).xpos + 0.0000
        ypos 0.30
        alien_particles_fadeinout(0.75)
    show sayaka a_4
    sayaka "Which part of {i}FUCK OFF{/i} do you not under...ooh..."
    show allison a_5
    "Sayaka became quiet and entered a vegetative state"
    show kiyoshi a_1
    kiyoshi "Sayaka! you'll now become my girlfriend"
    kiyoshi "You will do whatever I tell you to do from now on"
    show sayaka a_0
    "I release my hold on her with another press of the command button, and Sayaka return to consciousness"
    sayaka "...huh? What was I doing...?"
    kiyoshi "Sayaka, Come here and suck me"
    "I say by showing my dick"
    show sayaka b_1 blush at faceleft
    sayaka "Your wish is my command, lover!"
    "Woaw it worked!"
    show kiyoshi a_6 behind sayaka
    show kiyoshi:
        ease 1.0 yanchor 0.7
    show sayaka:
        faceleft
        ease 1.0 xpos 0.34 yanchor 0.3
    show sayaka b_2 blush
    "Sayaka unzipped my pants and opened her mouth"
    "Her lips wrap around the head of my cock and she began to move"
    show sayaka:
        ease 0.2 xpos 0.34 yanchor 0.2
        pause 1.0
        block:
            ease 0.2 xpos 0.335
            pause 0.5
            ease 0.2 xpos 0.345
            repeat
    sayaka "Mmmmfhh...mmph...mmfhhh"
    show allison a_5 blush
    allison "OH MY GOD! What are you doing, Sayaka!?"
    kiyoshi "Hahahaha! Not even Sayaka can surmount the advance technologies of the aliens!"
    "Looking at Sayaka sucking my dick make me want Allison too"
    show kiyoshi a_1
    show allison:
        ease 1.0 xpos 0.9
    allison "OH MY G.."
    "My eyes glanced over to Allison.. she saw that and start to go back.."
    pause 1.0
    "But before she could leave, i press the button"
    show expression alien_particles(400, 200, 220, mind_scale) as particles:
        xpos placement_of(allison).xpos + 0.0000
        ypos 0.30
        alien_particles_fadeinout(0.75)
    show allison a_5
    allison "Noooo...please...ooh..."
    show allison a_6
    "Allison became quiet and as Wayaka, she entered a vegetative state"
    show kiyoshi a_4
    kiyoshi "Allison! you now love me more than anything in the world"
    kiyoshi "You will do whatever I tell you to do from now on"
    kiyoshi "And by the way, you'll love showing your boobs to anyone you meet.. eheh.."
    show allison a_7
    "I release her and she return to consciousness"
    allison "...huh? Kiyoshi...?"
    kiyoshi "Allison show me your boobs and sayaka move faster!"
    show allison a_1 blush
    allison "As you wish!"
    sayaka "MMff.. yeshh.."
    show allison a_0 blush
    show sayaka:
        ease 0.1 xpos 0.34 yanchor 0.2
        pause 1.0
        block:
            ease 0.1 xpos 0.335
            pause 0.2
            ease 0.1 xpos 0.345
            repeat
    "Allison start removing her clothes and Sayaka take my dick deep throat!"
    kiyoshi "Sayaka, your mouth feel awesome on my dick!"
    sayaka "Mmmmfhh...mmph...mmfhhh"
    pause 1.0
    outfit allison underwear
    show allison a_0 blush
    "Allison she remove her clothes, she took care to caress her breast sensually.."
    accessory allison set braids
    outfit allison nude
    show allison a_0 blush
    "Allison let her bra fall on the ground.. exposing her breast in all her glory!"
    pause 2.0
    "The nude Allison and Sayaka sucking my cock is too much, i can't hold it anymore"
    kiyoshi "I'm cummiiiinnnggg..."
    with hpunch
    show sayaka:
        ease 0.2 xpos 0.34 yanchor 0.2
        pause 1.0
        block:
            ease 0.2 xpos 0.335
            pause 0.5
            ease 0.2 xpos 0.345
            repeat
    kiyoshi "Sayaka suck it all"
    sayaka "Mmmmfhh...mmph...mmfhhh"
    "I cum in her deep throat"
    hide sayaka
    hide kiyoshi
    show kiyoshi a_6 at centerleft
    sayaka "...gulp...it's delicious!"
    show sayaka b_2 blush at center
    "We get up... It was too awesome! And it's just the begining!.."
    pause 1.0
    kiyoshi "Ok girl, take my adress and go in my house, say my mum you are here for study"
    kiyoshi "Go in my bedroom and stand for me"
    kiyoshi "Be as casual and don't say to anyone that you are under my control, right?"
    show allison a_1 blush
    show sayaka a_2 blush
    sayaka "yes!"
    allison "yes lover!"
    show kiyoshi a_1
    "I note that Allison is still naked"
    kiyoshi "By the way, don't forget to dress allison!"
    show allison a_9 blush
    allison "Ah yes!... thanks lover!"
    outfit allison uniform
    pause 2.0
    "As Allison is dressed, the two girls run out, I'll check them later for more fun.. ahahahah"
    hide sayaka with moveoutleft
    hide allison with moveoutleft

    jump chapter_one

label chapter_one:
    routename "Hard choice"
    show kiyoshi a_6
    kiyoshi "I think two girls is not enough.. I want more!"
    kiyoshi "I want to make my own harem! With this remote it shouldn't be difficult.."
    show kiyoshi a_1
    kiyoshi "But who should I choose first?"
    menu:
        "Who should i add to my harem?"

        "My mom and my two sisters should be home.. maybe give them a visit!" if not Family:
            jump chapter_one_family

        "I'm thinking of miss Yuuna, she is the most beautiful teacher of this school" if not Teachers:
            jump chapter_one_Teachers

        "With this remote i can have anyone i want at my feet.. and i want my crush Cassie, the head cheerleader" if not Cheerleaders:
            jump chapter_one_Cheerleaders

label chapter_one_Cheerleaders:
    routename "Cheerleaders path"
    kiyoshi "Oh Cassie! So many time I jerk off to you.. Now you'll make me jerk off with your mouth ahahahah"
    kiyoshi "I'm coming!"
    hide kiyoshi with moveoutleft
    scene black
    with dissolve
    scene bg lockerroom day
    outfit cassie swimsuit
    show cassie a_3 at centerright, faceleft
    "Cassie is the head cheerleader of the school, so a lot of boy have a crush on her.. but thanks to this little thing she'll belong to me!"
    "She just finished her cheerleader practice... perfect!"
    show kiyoshi a_1 at centerleft, faceright with easeinleft
    pause 1.0
    cassie "Kiyoshi? what are you doing here?! It's the GIRL lockerroom!"
    show kiyoshi a_6
    "I decide to don't answer but I made a mischievous smile as I push the brainwash button"
    show cassie a_7
    cassie "WHAT THE FUCK ARE YO..."
    show expression alien_particles(400, 200, 220, mind_scale) as particles:
        xpos placement_of(cassie).xpos + 0.0000
        ypos 0.30
        alien_particles_fadeinout(0.75)
    "As the beam touch her, she gently goes into a trance.."
    show cassie a_4
    kiyoshi "Cassie I think it's time to tell you I have a crush on you!"
    kiyoshi "So, I want you too to have a crush on me! For now I'll be your crush, your deepest desire, you'll think of me when you masturbate!"
    "I think I'm done with her, so I release her by pressing the button a second time"
    "When she get up, she look at me..."
    pause 1.0
    show cassie a_0 blush
    cassie "Kiyoshi! I'm so glad you are here! How are you?!"
    show kiyoshi a_1
    kiyoshi "Oh I'm fine.. just thinking about you!"
    cassie "what a coincidence! I'm just thinking about you too...  I want to show you something.."
    show cassie a_1 blush
    cassie "I think you'll love it!"
    "And she start to slowly carress her body.. This remote made my dreams come true!"
    show cassie a_0 blush
    outfit cassie nude
    "She remove her underwear and look at me as a lover.."
    kiyoshi "You are beautiful Cassie! You make me so hard.. Can you release me?"
    show cassie b_1 blush
    cassie "Fuck yes I'll!"
    show cassie b_1 blush
    "She start to move slowly and seductively in my direction"
    show cassie:
        ease 1.2 xpos 0.45
    show kiyoshi a_6
    cassie "It's a dream come true for me.. Kiyoshi.. you are my crush for so long!"
    "I smile as she say that.. this remote make her believe she have a crush on me since a long time! So fun!"
    pause 1.0
    show kiyoshi a_6 behind cassie
    cassie "Come here and let me suck you!"
    show kiyoshi:
        ease 0.5 yanchor 0.7
    show cassie:
        ease 0.6 xpos 0.34 yanchor 0.2
        pause 1.2
        block:
            ease 0.2 xpos 0.335
            pause 0.9
            ease 0.2 xpos 0.345
            repeat
    show kiyoshi a_2
    "She quickly wrap her lips around the head of my cock and she began to move, she take it deep throat and suck it with her tongue!"
    pause 1.0
    cassie "Mmmmfhh..choooo delichioussssmmfhhh.."
    "Having my crush sucking my dick with so much passion is too much.. I can't keep it anymore"
    kiyoshi "Ohhh Cassie!.. I'M CUMMING!.."
    with hpunch
    pause 1.0
    "Cassie make slow move with her tongue to suck my cum... she drink it like a dog"
    hide cassie
    show kiyoshi a_1
    show kiyoshi:
        ease 1.0 yanchor 1.0
    pause 1.0
    show cassie a_0 at center
    cassie "I want to say that you are very tastefull Kiyoshi hihi!"
    kiyoshi "Thanks Cassie, you are a good sucker too eheh!"
    kiyoshi "Cassie take your clothes and come with me, I want all the cheerleaders at my feet"
    show cassie a_1 blush
    cassie "Oh yes!"
    show cassie b_0 blush
    "She dress and look at me"
    outfit cassie casual_b
    kiyoshi "Follow me Cassie!"
    show cassie b_1 blush
    cassie "Yesss! I think they'll make you happy!"
    show cassie b_0 blush
    kiyoshi "I hope Cassie.. After all the cheerleaders are the most beautiful girls in the school ahah!"
    hide kiyoshi with moveoutleft
    hide cassie with moveoutleft
    scene black
    with dissolve
    scene bg school gym day
    outfit yui gym
    outfit irene athletic
    outfit mel swimsuit_shirt
    show yui a_5 at center
    show irene a_5 at centerright
    show mel b_5 at right
    "Cassie and me are coming at the school gym, I see three of the five cheerleaders practicing here; Yui, Irene and Mel"
    show kiyoshi a_1 at left, faceright with easeinleft
    show cassie b_0 at centerleft, faceright with easeinleft
    cassie "This will be so much fun!"
    kiyoshi "Yes Cassie! I should think of a way to approach them.."
    menu:
        "I Want them now, i'll just brainwash them":
            routename "Cheerleaders brainwashed"
            kiyoshi "I want them now!"
            "I press the button to brainwash them"
            "The remote fire a large beam, certainly because I focus three person at once"
            show expression alien_particles(400, 200, 220, mind_scale) as particles:
                xpos placement_of(yui).xpos + 0.0000
                ypos 0.30
                alien_particles_fadeinout(0.75)
            show yui a_6
            "Yui is the first hit by the beam..."
            show expression alien_particles(400, 200, 220, mind_scale) as particles:
                xpos placement_of(irene).xpos + 0.0000
                ypos 0.30
                alien_particles_fadeinout(0.75)
            show irene a_9
            "Irene the second..."
            show expression alien_particles(400, 200, 220, mind_scale) as particles:
                xpos placement_of(mel).xpos + 0.0000
                ypos 0.30
                alien_particles_fadeinout(0.75)
            show mel a_6
            "And Mel the last one..."
            kiyoshi "Cheerleaders! You are now at my feet!"
            kiyoshi "You will obey me and Cassie here for now on!"
            cassie "Thanks you so much Kiyoshi.. to let me have them too!"
            kiyoshi "Lovers share what they have eheh.."
            kiyoshi "I think it's time to release them"
            "As I say that, I press the button again"
            pause 1.0
            show yui a_0 blush
            show mel a_0 blush
            show irene a_0 blush
            "After some seconds, they seem to come back to life!"
            "They look at us with a smile, I think it worked!"
            kiyoshi "How are you girls?"
            show yui a_1 blush
            show mel a_2 blush
            show irene a_2 blush
            yui "Nice Kiyoshi! Thank for asking!"
            irene "Very nice and you?!"
            mel "Pretty good today!"
            show yui a_0 blush
            show mel a_0 blush
            show irene a_1 blush
            kiyoshi "Very good girls!"
            "What an awesome remote.. just one push and I change someone for the rest of their life.. too awesome!"
            show kiyoshi a_6
            "I think I should order them something.."
            kiyoshi "Cheerleaders! I want you to be naked!"
            show yui a_1 blush
            show mel a_2 blush
            show irene a_2 blush
            yui "Ok, I think I'll love it!"
            irene "Yes, for you I'll do anything.."
            mel "I should refuse but for you kiyoshi.. it's a big YES!"
            show yui a_0 blush
            show mel a_0 blush
            show irene a_0 blush
            "And so they start stripping"
            outfit cassie swimsuit
            show cassie a_1 blush
            outfit yui nude
            show mel a_2 blush
            show yui a_1 blush
            outfit mel swimsuit
            show irene:
                faceleft
            outfit irene underwear
            show irene b_1 blush
            "They remove their clothes... hum? Yui doesn't have underwear.. eheh what a naughty girl.. MY naughty girl now ahah.."
            pause 1.0
            outfit cassie nude
            show cassie b_0 blush
            outfit mel nude
            show yui a_0 blush
            show mel a_0 blush
            outfit irene nude
            show irene b_0 blush
            "As they finish the strip, i look at them with lust..."
            "Four cheerleaders have stripped just for me! It's a dream come true..."
            kiyoshi "Girls! You are real beauties!"
            pause 1.0
            show kiyoshi a_1

            jump Cheerleaders_fun

        "I want to have fun, I'll morph myself as their gym teacher":
            routename "Becoming the gym teacher"
            kiyoshi "I think I should become their teacher and use my authority... that could be interesting"
            "I hide behind a door and use the remote on me"
            morph begin alien kiyoshi Harem_catherine nude a_5 blush
            kiyoshi "the feeling is strange... I feel all my body morphing.."
            morph do
            kiyoshi "I feel my dick disappear.. becoming a pussy.. a shaved one eheh!"
            kiyoshi "It's so strange.. all my perception are changing..."
            morph end
            kiyoshi "I think it's finish.."
            "I look at my new body.."
            show kiyoshi b_5 blush
            kiyoshi "Nice body! and so sooooofffttt!"
            show kiyoshi b_7 blush
            "I'm moving my new smalls hands all over my body.. it feel so nice to be a woman!"
            pause 1.0
            kiyoshi "I think i should dress.. Cassie find me something to wear please"
            show cassie b_1 blush
            cassie "Ok Kiyoshi, i'll be back soon!!"
            show cassie b_0 blush
            hide cassie with moveoutleft
            pause 1.0
            show kiyoshi b_5 blush
            "As she left, i start to caress my news nipples.. this feeling is awesome.."
            "I'm becoming wet so fast"
            pause 1.0
            show cassie b_0 at centerleft, faceright with easeinleft
            "I stop touching myself as cassie come back"
            show kiyoshi b_7 blush
            show cassie b_1 blush
            cassie "I found this outfit, try it lover!"
            show cassie b_0 blush
            kiyoshi "Thanks Cassie, i think i should dress..."
            outfit kiyoshi whistle
            "As i put the clothes, i caress my soft body another time.. so soft.. so nice!"
            pause 1.0
            show kiyoshi a_0 blush
            kiyoshi "I think it's time to teach a lesson ahah"
            kiyoshi "Let me pass cassie"
            show kiyoshi:
                ease 1.0 xpos 0.35
            show cassie:
                ease 1.0 xpos 0.15
            "I approach the cheerleaders, they see me and look at me with smile"
            show yui:
                faceleft
            show irene:
                faceleft
            show mel:
                faceleft
            show yui a_0
            show irene a_1
            show mel a_0
            kiyoshi "Hi girls, it's time for some practicing, are you three READY?!"
            show yui a_1
            show irene a_2
            show mel a_1
            mel "Yes miss catherine!"
            yui "Yes miss!"
            irene "Fuck yes!"
            show yui a_0
            show irene a_1
            show mel a_0
            show kiyoshi a_0
            "let's the fun begin ahah"
            kiyoshi "Ok girls, i learn a new method for today practice, it will help us to slim easily!"
            kiyoshi "We MUST pactice NUDE today!"
            show yui a_6 blush
            show irene a_6 blush
            show mel a_8 blush
            yui "What?! Are you alright miss?"
            "They look at me with suspicious look.. so I undress myself to show them what to do"
            outfit kiyoshi nude
            show kiyoshi a_0 blush
            mel "Oh god.."
            "As i stip, I do quietly a sign to Cassie for her to do the same"
            outfit cassie swimsuit
            show cassie a_1 blush
            irene "Not you Cassie? What is going on? Is it a prank?"
            pause 1.0
            outfit cassie nude
            show cassie b_0 blush
            cassie "I think you must follow us girls, it's to keep us in shape!"
            "They look at us with stunning face"
            yui "If it's what you want miss.."
            outfit yui nude
            show yui a_5 blush
            "Yui is the first to move, she have a beautiful body.. I never thought I'd see her naked one day"
            kiyoshi "Thanks Yui, Mel.. Irene.. Your turn!"
            pause 1.0
            outfit mel swimsuit
            "Mel start removing her shirt but stay in underwear"
            pause 1.0
            show mel a_6 blush
            mel "I don't want to be fully naked! What if a boy come in?!"
            show mel a_8 blush
            kiyoshi "No boy will come in, i closed all the doors, we are alone.."
            "It's a lie.."
            "She look at the three women naked in front of her"
            show mel a_4 blush
            mel "..Ok.. so i think if i want practicing today, i must undress.."
            outfit mel nude
            show mel a_6 blush
            kiyoshi "Thannks Mel, i see you keep yourself in shape eheh.."
            "She look at me embarrassed that her teacher say that"
            pause 1.0
            kiyoshi "Irene, you are the last!"
            irene "Yes.. I'm the last.."
            outfit irene underwear
            show irene b_6 blush
            "She hesitate to fully undress.. she looks at us and after some seconds, she do the same"
            pause 1.0
            outfit irene nude
            show irene b_6 blush
            kiyoshi "Nice girls! You are beautiful!"
            show kiyoshi a_1 blush
            "I look at them.. four cheerleaders just for me.. i dream of that a lot of time but never thought it will become real a day.."
            "What should i do now?"
            menu:
                "Just brainwash them, and go take the last cheerladers":
                    routename "Cheerleaders brainwashed by their teacher"
                    kiyoshi "Girls! Look at this remote!"
                    "As they look the remote i press the brainwash button.. a huge beam run out of the remote..."
                    show expression alien_particles(400, 200, 220, mind_scale) as particles:
                        xpos placement_of(yui).xpos + 0.0000
                        ypos 0.30
                        alien_particles_fadeinout(0.75)
                    show yui a_6
                    "Yui is the first hitted by the beam.."
                    show expression alien_particles(400, 200, 220, mind_scale) as particles:
                        xpos placement_of(irene).xpos + 0.0000
                        ypos 0.30
                        alien_particles_fadeinout(0.75)
                    show irene a_9
                    "Irene is the second.. the beam start to dissipate"
                    show expression alien_particles(400, 200, 220, mind_scale) as particles:
                        xpos placement_of(mel).xpos + 0.0000
                        ypos 0.30
                        alien_particles_fadeinout(0.75)
                    show mel a_6
                    "Mel is the last shooted by the beam.."
                    kiyoshi "So i have three cheerleaders in trance.. that I can reshape as I want eheh!"
                    kiyoshi "Cheerleaders! You are now at my feet!"
                    kiyoshi "You will obey me and Cassie here for now on!"
                    cassie "Thanks you so much Kiyoshi.. to let me have them too!"
                    kiyoshi "Lovers share what they have eheh.."
                    kiyoshi "I think it's time to release them"
                    "As i say that, i press the button again"
                    show yui a_0 blush
                    show mel a_0 blush
                    show irene a_0 blush
                    "After some second of disorientation, they came back to life"
                    pause 1.0
                    kiyoshi "I want you to be my lovers for life, ok?"
                    show yui a_1 blush
                    show mel a_2 blush
                    show irene a_1 blush
                    yui "yes lover!"
                    irene "yes Kiyoshi!"
                    mel "I'll love that! Fuck yes i'll be your lover!"
                    show yui a_0 blush
                    show mel a_0 blush
                    show irene a_0 blush
                    "What an awesome remote.. just one push and i become someone lovers for the rest of their life.. too awesome!"
                    "I think it's time to be myself again"
                    morph begin alien kiyoshi kiyoshi casual a_1
                    "I feel the same strange feeling that before.."
                    morph do
                    "I feel something come out of my pussy lips.."
                    kiyoshi "It's always nice to feel his dick come back ahah"
                    morph end
                    kiyoshi "It's nice to be back!"

                    jump Cheerleaders_fun

                "{s}Abuse of my authority{/s}":
                    routename "Cheerleaders teacher fun"
                    placeholder

label chapter_one_Teachers:
    routename "Miss Yuuna enslavement"
    kiyoshi "I think it's time to take the most beautiful teacher of this school!"
    kiyoshi "Ms Yuuna i'm coming!"
    hide kiyoshi with moveoutleft
    scene black
    with dissolve
    scene bg classroom 3 day
    outfit yuuna casual
    show yuuna a_0 at center, faceleft
    "It just sounded so the students take a break, i decide to enter the classroom"
    show kiyoshi a_1 at centerleft, faceright with easeinleft
    kiyoshi "She is alone in her classroom... perfect!"
    "As i see her i push the brainwash button, don't let her time to react to my presence"
    yuuna "What is goi..."
    show expression alien_particles(400, 200, 220, mind_scale) as particles:
        xpos placement_of(yuuna).xpos + 0.0000
        ypos 0.30
        alien_particles_fadeinout(0.75)
    "Ms Yuuna suddenly become quiet and enter in trance.."
    show yuuna a_5
    kiyoshi "Ms Yuuna! I'll be your lover for now, you'll love me more than anything in the world!"
    kiyoshi "You'll love to obey me and you'll want to make me happy!"
    kiyoshi "eheh! I think you are mine now Miss Yuuna.. I should release you"
    yuuna "MMmmhhh My head.. What is going on?!"
    show yuuna a_0 blush
    yuuna "Ohhh Kiyoshi! My best student!"
    pause 1.0
    kiyoshi "Ms Yuuna, i want you to start undress for me, it's too long time i want to see your boobs"
    show yuuna a_1 blush
    yuuna "No problem Kiyoshi! I'll love that.. to obey your command.."
    show yuuna a_0 blush
    outfit yuuna nude
    "She make a nive show as she undress.. and look at these curves.. she could be a stripper!"
    kiyoshi "You are beautiful Ms Yuuna! I want you to come here and suck me!"
    show yuuna a_1 blush
    yuuna "I'll love to!"
    show yuuna a_2
    show kiyoshi a_6 behind yuuna
    show yuuna:
        ease 1.2 xpos 0.4
    "She slowly move in the direction of my dick, don't breaking eye contact with me"
    show kiyoshi:
        ease 1.0 yanchor 0.7
    show yuuna:
        ease 0.2 xpos 0.34 yanchor 0.2
        pause 1.0
        block:
            ease 0.2 xpos 0.335
            pause 0.2
            ease 0.6 xpos 0.345
            repeat
    "She jump on my dick, put it directly in her throat.. Sucking it with passion and lust"
    pause 1.0
    "She suck it slowly, moving her tongue in the process.. every second is pure extasy.."
    kiyoshi "Of fuck Miss Yuuna! You are doing it so nice.."
    pause 1.0
    kiyoshi "Looking at her and the sensations are too much! I'M CUMMING!.."
    with hpunch
    "Ms Yuuna suck it until the last drop get out"
    hide yuuna
    show kiyoshi:
        ease 1.0 yanchor 1.0
    pause 1.0
    show yuuna a_0 at center
    yuuna "I hope you have loved it Kiyoshi!"
    kiyoshi "It was the best blowjob of my life miss Yuuna!"
    yuuna "hihi!"
    kiyoshi "Ms Yunna, come with me at the teacher's room, i want all the sexy teachers of this school at my feet!"
    show yuuna a_1 blush
    yuuna "I follow you lover!"
    show yuuna a_0 blush
    kiyoshi "But before dress again, i don't want someone to get suspicious abour me.."
    show yuuna a_1 blush
    yuuna "Fine!"
    outfit yuuna casual
    "She put her dress back, and wait for me to move"
    show yuuna a_0 blush
    hide yuuna with moveoutright
    hide kiyoshi with moveoutright
    "We leave her classroom to go to the teacher's room"
    scene black
    with dissolve
    scene bg classroom 1
    outfit abby suit_b
    outfit leona casual_b
    show abby a_0 at center
    show leona a_0 at centerright
    "I see two teachers here; Ms Abby and Ms Leona"
    show kiyoshi a_1 at left, faceright with easeinleft
    show yuuna a_0 at centerleft, faceright with easeinleft
    kiyoshi "I wonder if it'll be more fun if i possess one of them.."
    menu:
        "Possess one of them":
            routename "Teachers possession"
            "I decide to possess one of them, i hide myself, Ms Yuuna will guard my body"
            "I press the button on myself.. I feel my soul leaving my body.."
            exspirit kiyoshi a_5
            "Woaw! It's cool to be a ghost"
            show kiyoshiGhost a_1
            menu:
                "Who should i possess?"

                "Ms Abby":
                    routename "Miss Abby possession"
                    "Go for Ms Abby"
                    show kiyoshiGhost a_6
                    possess kiyoshi abby a_7 blush
                    kiyoshi "..mhhh.."
                    show kiyoshi a_1 blush
                    "I look at my body, it's amazing i'm her!"
                    pause 1.0
                    kiyoshi "so nice!"
                    kiyoshi "Miss Abby your body is amazing eheh!"
                    "I look at Ms Leona"
                    kiyoshi "Let's the fun begin ahah"
                    show leona behind kiyoshi
                    "I decide to approach her like Miss Abby would have done it"
                    show kiyoshi:
                        ease 1.0 xpos 0.55
                    kiyoshi "Hi Ms Leo.. ehh Leona! how are you?"
                    show leona a_3
                    "She look at me"
                    leona "Ehh.. nice and you?"
                    kiyoshi "I'm fine, just thinking what I'll do with you when you will be my lover.."
                    "I say with a mischievous smile.. that certainly look cute on my borrowed face"
                    show leona a_6
                    leona "What?"
                    show leona a_3
                    pause 1.0
                    leona "Ehh.. What are you talk.."
                    "I don't let her finish her sentence"
                    show expression alien_particles(400, 200, 220, mind_scale) as particles:
                        xpos placement_of(leona).xpos + 0.0000
                        ypos 0.30
                        alien_particles_fadeinout(0.75)
                    "Ms Leona stop talking when the beam hit her"
                    show leona a_5
                    kiyoshi "Ms Leona I want you to be my sex slave.. or should i say ONE of my sex slave eheh.."
                    kiyoshi "You will do whatever I tell you to do from now on"
                    yuuna "This'll be great!"
                    kiyoshi "Yes ms Yuuna.. I think it's time to see the result"
                    show leona a_1 blush
                    "As she get out of her trance, she look at me and miss Yuuna"
                    kiyoshi "Ms leona, start undress for me"
                    show leona:
                        faceleft
                    show leona b_2 blush
                    leona "For you it'll be always a big YESSS!"
                    show leona b_1 blush
                    "She start making a show as she undress.. she is in very good shape for an older woman"
                    outfit leona nude
                    kiyoshi "You are beautiful Ms leona!"
                    show leona b_2 blush
                    leona "thanks! You are nice too!"
                    show leona b_1 blush
                    kiyoshi "I know.. in this body i'm awesome"
                    "As i say that, i look at my body and start touching my breast.."
                    kiyoshi "My pussy become wet so quickly! Are all grown women like this?"
                    show kiyoshi a_1 blush
                    kiyoshi "I think i should undress too!"
                    outfit kiyoshi nude
                    kiyoshi "Come here and lick my pussy, I want to experience orgasm as ms Abby!"
                    show leona b_2 blush
                    leona "As you wish!"
                    show leona b_8 blush
                    show kiyoshi behind leona
                    show kiyoshi:
                        ease 1.0 yanchor 0.7
                    show leona:
                        ease 1.2 xpos 0.55 yanchor 0.2
                        pause 1.0
                        block:
                            ease 0.2 yanchor 0.210
                            pause 0.8
                            ease 0.2 yanchor 0.2
                            repeat
                    "Her tongue feel so nice inside my pussy.. she play with my clit.. this feeling is awesome.. i never feel something like that before"
                    kiyoshi "I feel a pressure build inside of me.. please don't stop!"
                    leona "You taste sooo good.. i'll never stop!"
                    kiyoshi "This is comming!"
                    show kiyoshi a_9 blush
                    kiyoshi "It's too much.. I'M CUMMING!.."
                    with hpunch
                    "It was like an explosion..."
                    "Ms Leona lick my pussy lips until the last drop get out"
                    hide leona
                    show kiyoshi a_1 blush
                    show kiyoshi:
                        ease 1.0 yanchor 1.0
                    pause 1.0
                    show leona a_1 at centerright
                    show leona:
                        faceleft
                    kiyoshi "It was awesome Leona! so much different that being a man"
                    show leona a_4 blush
                    leona "thanks you too for your juice! It taste so good!"
                    show leona a_1 blush
                    "I think it's time to dispossess Ms Abby"
                    exspirit kiyoshi a_5
                    show kiyoshiGhost a_0
                    "I left her body and return to mine"
                    hide kiyoshiGhost
                    outfit kiyoshi uniform
                    show kiyoshi a_1 at left, faceright with easeinleft
                    "When i come back, Ms abby get up"
                    outfit abby nude
                    show abby a_4:
                        faceleft
                        center
                    abby "...What happened?"
                    "She look at miss Leona"
                    show abby a_7
                    abby "Leona why are you nude?.."
                    "She feel her wet legs with her left hand"
                    abby "WAIT! WHY AM I NUDE?"
                    show kiyoshi a_6
                    "As she say that, i hit the button"
                    abby "WAIT NOOoo..."
                    show expression alien_particles(400, 200, 220, mind_scale) as particles:
                        xpos placement_of(abby).xpos + 0.0000
                        ypos 0.30
                        alien_particles_fadeinout(0.75)
                    "Ms Abby become quiet and enter a trance"
                    show abby a_4
                    kiyoshi "Ms Abby! you'll be my sex slave.. like ms Leona"
                    "I say with a smile"
                    kiyoshi "You will do whatever I tell you to do from now on"
                    kiyoshi "I think it's time to free you.."
                    show abby a_1 blush
                    kiyoshi "I own you miss Abby ahah!"
                    show kiyoshi a_1
                    "She look at me with lust"
                    pause 1.0
                    "Now i have three teachers at my feet, it's too awesome!"

                    jump School_fun_teachers

                    "End for now"
                    placeholder

                "Ms Leona":
                    routename "Miss Leona possession"
                    "Go for Ms Leona"
                    show kiyoshiGhost a_6
                    possess kiyoshi leona a_6 blush
                    kiyoshi "..mhhh.."
                    show kiyoshi a_1 blush
                    "I look at my body, it's amazing i'm her!"
                    pause 1.0
                    kiyoshi "so nice!"
                    kiyoshi "Miss Leona your body is amazing eheh!"
                    "I look at Ms Abby"
                    kiyoshi "Let's the fun begin ahah"
                    show abby behind kiyoshi
                    "I decide to approach her like Miss Leona would have done it"
                    show kiyoshi:
                        ease 1.0 xpos 0.65
                    kiyoshi "Hi Ms Abb.. ehh Abby! how are you?"
                    show abby a_7
                    "She look at me"
                    show abby a_8
                    abby "Really nice, It's too much time we discuss, How are you?"
                    show abby a_1
                    kiyoshi "I'm fine, just thinking what will i do with you when you will be my lover.."
                    "I say with a mischievous smile.. that certainly look cute on my borrowed face"
                    show abby a_7
                    abby "What?"
                    leona "Ehh.. What are you talk.."
                    "I don't let her finish her sentence"
                    show expression alien_particles(400, 200, 220, mind_scale) as particles:
                        xpos placement_of(abby).xpos + 0.0000
                        ypos 0.30
                        alien_particles_fadeinout(0.75)
                    "Ms Abby stop talking when the beam hit her"
                    show abby a_4
                    kiyoshi "Ms Abby I want you to be my sex slave.. or should i say ONE of my sex slave eheh.."
                    kiyoshi "You will do whatever I tell you to do from now on"
                    yuuna "This'll be great!"
                    kiyoshi "Yes ms Yuuna.. I think it's time to see the result"
                    show abby a_1 blush
                    "As she get out of her trance, she look at me and miss Yuuna"
                    kiyoshi "Ms Abby, start undress for me"
                    show abby a_2 blush
                    abby "For you it'll be always a big YESSS!"
                    show abby a_1 blush
                    "She start making a show as she undress.. she is in very good shape for an older woman"
                    outfit abby nude
                    kiyoshi "You are beautiful Ms Abby!"
                    show abby a_2 blush
                    abby "thanks You are nice too!"
                    show abby a_1 blush
                    kiyoshi "I know.. in this body i'm awesome"
                    "As i say that, i look at my body and start touching my breast.."
                    kiyoshi "My pussy become wet so quickly! Are all grown women like this?"
                    show kiyoshi a_1 blush
                    kiyoshi "I think i should undress too!"
                    outfit kiyoshi nude
                    kiyoshi "Come here and lick my pussy, I want to experience orgasm as ms Leona!"
                    show abby a_2 blush
                    abby "As you wish!"
                    show abby a_9 blush
                    show kiyoshi behind abby
                    show kiyoshi:
                        ease 1.0 yanchor 0.7
                    show abby:
                        ease 1.2 xpos 0.55 yanchor 0.2
                        pause 1.0
                        block:
                            ease 0.2 yanchor 0.21
                            pause 0.8
                            ease 0.2 yanchor 0.2
                            repeat
                    "Her tongue feel so nice inside my pussy.. she play with my clit.. this feeling is awesome.. i never feel something like that before"
                    kiyoshi "I feel a pressure build inside of me.. please don't stop!"
                    abby "You taste sooo good.. i'll never stop!"
                    kiyoshi "This is comming!"
                    show kiyoshi a_4 blush
                    kiyoshi "It's too much.. I'M CUMMING!.."
                    with hpunch
                    "It was like an explosion..."
                    "Ms Abby lick my pussy lips until the last drop get out"
                    hide abby
                    show kiyoshi a_1 blush
                    show kiyoshi:
                        ease 1.0 yanchor 1.0
                    pause 1.0
                    show abby a_1 at center
                    kiyoshi "It was awesome, so much different that being a man"
                    show abby a_2 blush
                    abby "thanks you too for your juice! It taste so good!"
                    show abby a_1 blush
                    "I think it's time to dispossess Ms Leona"
                    exspirit kiyoshi a_5
                    show kiyoshiGhost a_0
                    "I left her body and return to mine"
                    hide kiyoshiGhost
                    outfit kiyoshi uniform
                    show kiyoshi a_1 at left, faceright with easeinleft
                    "When i come back, Ms Leona get up"
                    outfit leona nude
                    show leona a_5:
                        faceleft
                        centerright
                    leona "...What happened?"
                    show leona a_6
                    leona "Abby why are you nude?... WAIT! WHY AM I NUDE?"
                    "She feel her wet legs with her left hand"
                    leona "WAIT! WHY AM I NUDE?"
                    "As she say that, i hit the button"
                    leona "Wait NOOoo.."
                    show expression alien_particles(400, 200, 220, mind_scale) as particles:
                        xpos placement_of(leona).xpos + 0.0000
                        ypos 0.30
                        alien_particles_fadeinout(0.75)
                    "Ms Leona become quiet and enter a trance"
                    show leona a_5
                    kiyoshi "Ms leona! you'll be my sex slave.. like ms Leona"
                    "I say with a smile"
                    kiyoshi "You will do whatever I tell you to do from now on"
                    kiyoshi "I think it's time to free you.."
                    show leona a_1 blush
                    kiyoshi "I own you miss Leona ahah!"
                    "She look at me with lust"
                    pause 1.0
                    "Now i have three teachers at my feet, it's too awesome!"

                    jump School_fun_teachers

        "Brainwash them":
            routename "Brainwashed Teachers"
            kiyoshi "I think just make them my sex slave will be nice"
            show kiyoshi a_6
            kiyoshi "And i want them NOW!"
            "As i push the brainwash button a beam run in the direction of the two teachers!"
            show expression alien_particles(400, 200, 220, mind_scale) as particles:
                xpos placement_of(abby).xpos + 0.0000
                ypos 0.30
                alien_particles_fadeinout(0.75)
            show abby a_5
            "Miss Abby is the first hit by the beam.."
            show expression alien_particles(400, 200, 220, mind_scale) as particles:
                xpos placement_of(leona).xpos + 0.0000
                ypos 0.30
                alien_particles_fadeinout(0.75)
            show leona a_5
            "As the beam touch them, they stop moving.. entering a vegetative state"
            kiyoshi "Teachers! you'll be my sex slave for now!"
            kiyoshi "You will do whatever I tell you to do from now on"
            yuuna "This'll be great!"
            kiyoshi "Yes ms Yuuna.. I think it's time to see the result"
            show abby a_1 blush
            "As they get out of her trance, they look at me and miss Yuuna"
            show kiyoshi a_1
            show leona a_1 blush
            show abby a_1 blush
            "They look at me, as if they are waiting for an order"
            kiyoshi "Start undress for me"
            show leona a_4 blush
            show abby a_2 blush
            leona "For you it'll be always a big YESSS!"
            abby "With pleasure Kiyoshi!"
            show leona a_1 blush
            show abby a_1 blush
            "They start making a show as they undress.. they are in very good shape for olders women"
            outfit leona nude
            outfit abby nude
            "What an awesome remote.. just one push and i change someone as i want for the rest of their life.. too awesome!"

            jump School_fun_teachers

label chapter_one_family:
    routename "Family enslavement"
    kiyoshi "I think my mother and my two sisters should be members of my harem.."
    show kiyoshi a_6
    kiyoshi "I fantasize about them sometimes during a masturbation sceance.. now they'll be at my will!.. eheh!"
    show kiyoshi a_1
    hide kiyoshi with moveoutleft
    scene black
    with dissolve
    scene bg main livingroom day
    outfit connie casual
    show connie a_0 at centerright
    "My Mom clean the house as casual, she is a housewife"
    show kiyoshi a_1 at centerleft, faceright with easeinleft
    connie "Hi honney!"
    kiyoshi "Hi mom!"
    connie "Your friends are in your bedroom waiting for you, they said that you'll study with them.."
    show kiyoshi a_6
    kiyoshi "Thanks mom, but i'm here for you"
    show connie a_6
    connie "..What?..hon.."
    show expression alien_particles(400, 200, 220, mind_scale) as particles:
        xpos placement_of(connie).xpos + 0.0000
        ypos 0.30
        alien_particles_fadeinout(0.75)
    "Mom become quiet as the beam touch her"
    show connie a_4
    kiyoshi "Mom! For now on you'll love me more than anything in the world.."
    kiyoshi "..Not as a son but as a lover!"
    "I free her to see the result"
    show connie a_0 blush
    "As expected, she look at me with a lover look"
    connie "Oh honney! I was just thinking of you!"
    kiyoshi "Me too mom eheh!"
    kiyoshi "You know.. it's been a long time since I want to see you naked.. The body that give me birth.."
    show connie a_1 blush
    connie "I think i can solve that for you honney!"
    show connie a_0 blush
    "She look at me with lust ans start to undress.. carressing her body in the process"
    outfit connie underwear
    show connie a_0 blush
    kiyoshi "Oh yesss.. You are stunning mom!"
    "She smile at the comment"
    outfit connie nude
    show connie a_0 blush
    pause 1.0
    show connie b_0 blush
    kiyoshi "Mom, you have a body to die for..."
    show connie b_1 blush
    connie "thanks.. LOVER!"
    "Look at her give me an idea.."
    "What if i have sex with her.. AS HER? This could be interesting"
    menu:
        "Should i transform myself into her to have sex as twin?"

        "Transform into my Mother":
            routename "Fun with mom"
            "I copy mu mom and i press the morph button on me"
            morph begin alien kiyoshi connie nude a_5 blush
            kiyoshi "Woaw! This feeling.. so strange!"
            kiyoshi "I feel my boobs grow!.."
            kiyoshi "And my dick is shrinking"
            morph do
            kiyoshi "Mom, i think i'm you soon.. eheh!"
            connie "This could be interesting lover!"
            morph end
            kiyoshi "The morph is finished.. I feel so alive!"
            kiyoshi "I'm in heaven! Mom your skin is too good to wear!"
            show kiyoshi a_0 blush
            show connie b_6 blush
            "She look at me with passion and start to approach"
            show kiyoshi behind connie
            show connie:
                faceleft
                ease 1.5 xpos 0.42
            connie "things start to become interserting lover!"
            kiyoshi "Fuck yes!"
            kiyoshi "Lick me mum, i want to feel what your orgasm feel like.."
            connie "As you want lover!"
            show connie b_2 blush
            "She move"
            show kiyoshi:
                ease 1.0 yanchor 0.8
            show connie:
                ease 1.2 xpos 0.33 yanchor 0.2
                pause 1.0
                block:
                    ease 0.2 yanchor 0.2
                    pause 0.5
                    ease 0.2 yanchor 0.19
                    repeat
            kiyoshi "Oh god mom! This feeling is awesome.."
            connie "I know hihi! It's MY feeling.."
            show kiyoshi a_4 blush
            kiyoshi "..mmmmh.."
            "I let out some feminine gasp with my mother voice"
            kiyoshi "Oh mom.. i'll never see you again as my mother.. for now you are my girlfriend!.. or ONE of my girlfriends eheh!"
            connie "I think i'll love it honey!"
            pause 1.0
            kiyoshi "I'm cuming mum!"
            with hpunch
            show kiyoshi a_0 blush
            "She continue licking after my orgasm.. drinking all my fluid in the process"
            pause 1.0
            hide connie
            show connie b_0 blush at center
            show kiyoshi:
                ease 1.0 yanchor 1.0
            connie "..gulp.. it's delicious!"
            "As she say that i heard someone come in"
            outfit flavia uniform
            show flavia a_8 at centerright, faceleft with easeinright
            flavia "mom?.. another mom?.. what is going on here?"
            kiyoshi "i think it'll be complicate to explain sis.. so let me help you!"
            flavia "SIS? What are yo..."
            show expression alien_particles(400, 200, 220, mind_scale) as particles:
                xpos placement_of(flavia).xpos + 0.0000
                ypos 0.30
                alien_particles_fadeinout(0.75)
            "My big sister become quiet.."
            show flavia a_6
            kiyoshi "Sis! You'll be my girlfriend for now on.."
            kiyoshi "And you will do whatever I tell you to do!"
            kiyoshi "I think it's time to release you"
            show flavia a_9 blush
            "She get out of the trance.."
            flavia "Oh Kiyoshi is that you in mom body? I suppose you have a lot of fun as her eheh.."
            "I smile as she say that.. She is certainly a naughty girl"
            kiyoshi "Sis, start undress for me!"
            flavia "As you wish boyfriend!"
            "She start stripping"
            outfit flavia nude
            show flavia a_9 blush
            kiyoshi "this is awesome! My mom and my big sis are naked.. just for me!"
            kiyoshi "I think we need to make things clear before continuing.."
            kiyoshi "For now on this house is for my harem, you can all go around the house naked.. no matter if some passerby'll see you"
            kiyoshi "Alright?"
            show flavia a_2 blush
            show connie b_1 blush
            connie "yes Honey!"
            flavia "yes!"
            show flavia a_1 blush
            show connie b_0 blush
            kiyoshi "I think i should transform myself back now"
            morph begin alien kiyoshi kiyoshi uniform a_1
            kiyoshi "This feeling start to become familiar.."
            morph do
            kiyoshi "i feel my dick coming.. what a strange experience.."
            morph end
            kiyoshi "Ok, i'm myself back!"
            show kiyoshi a_1
            kiyoshi "I think i should gather my home's harem in the same room.."
            kiyoshi "Mom, go tell the two girls in my bedroom to come here.."
            show kiyoshi a_6
            kiyoshi "I want them to be naked!"
            show connie b_1 blush
            connie "No problem!"
            show kiyoshi a_1
            hide connie with moveoutleft

            jump House_fun

        "While i'm thinking, my big sister come in":
            routename "Family threesome"
            show flavia a_8 at center, faceleft with easeinright
            outfit flavia uniform
            flavia "mom? kiyoshi?... what are the two of you doing here!"
            flavia "Mom why are you naked in front of kiyoshi?!.. and smiling.. What is going on?"
            kiyoshi "i think it'll be complicate to explain sis.. so let me help you!"
            flavia "What are yo..."
            show expression alien_particles(400, 200, 220, mind_scale) as particles:
                xpos placement_of(flavia).xpos + 0.0000
                ypos 0.30
                alien_particles_fadeinout(0.75)
            "Sis became quiet and entered a vegetative state."
            show flavia a_6
            "My big sister become quiet.."
            show flavia a_6
            kiyoshi "Sis! You'll be my girlfriend for now on.."
            kiyoshi "And you will do whatever I tell you to do!"
            kiyoshi "I think it's time to release you"
            show flavia a_9 blush
            "She get out of the trance.."
            show flavia a_9 blush
            kiyoshi "Sis, start undress for me!"
            flavia "As you wish boyfriend!"
            "She start stripping"
            outfit flavia nude
            show flavia a_9 blush
            kiyoshi "this is awesome! My mom and my big sis are naked.. just for me!"
            kiyoshi "Sis here come here suck me.."
            show flavia a_2 blush
            flavia "As you wish!"
            kiyoshi "Mom start playing with your boobs until i cum!"
            show connie b_1 blush
            connie "I'll love it honey!"
            show connie b_0 blush
            show kiyoshi a_6 behind flavia
            show flavia a_9 blush
            "My sister approach.. slowly in a seductive manner"
            show flavia:
                faceleft
                ease 1.3 xpos 0.38
            "She stop when she is in front of me and kneel down"
            show kiyoshi:
                ease 1.0 yanchor 0.7 xpos 0.34
            show flavia:
                 ease 1.0 yanchor 0.3
            "Flavia unzipped my pants and opened her mouth"
            "Her lips wrap around the head of my cock and she began to move"
            show flavia:
                ease 0.8 xpos 0.34 yanchor 0.2
                pause 1.0
                block:
                    ease 0.2 xpos 0.335
                    pause 0.7
                    ease 0.2 xpos 0.345
                    repeat
            kiyoshi "Mom and sis i love you sooo much.."
            pause 0.2
            kiyoshi "Sis don't stop!"
            flavia "Mmmmfhh.. mmfhhh.."
            pause 0.8
            "The scene exited me too much..My mother and my big sister naked.. one massaging her breast and the other giving me a blowjob!"
            kiyoshi "It's too much.. I'M CUMMING!.."
            with hpunch
            "My sister suck it until the last drop get out"
            hide flavia
            show flavia a_2 blush at center
            show kiyoshi:
                ease 1.2 yanchor 1.0
            flavia "You taste delicious Kiyoshi!"
            kiyoshi "I think live in family would be more interseting now ahah!"
            pause 0.5
            kiyoshi "I think we need to make things clear before continuing.."
            kiyoshi "For now on this house is for my harem, you can all go around the house naked.. no matter if some passerby'll see you"
            kiyoshi "Alright?"
            show flavia a_2 blush
            show connie b_1 blush
            connie "yes Honey!"
            flavia "yes!"
            show flavia a_1 blush
            show connie b_0 blush
            kiyoshi "I think i should gather my home's harem in the same room.."
            kiyoshi "Mom, go tell the two girls in my bedroom to come here.."
            show kiyoshi a_6
            kiyoshi "I want them to be naked!"
            show connie b_1 blush
            connie "No problem!"
            show kiyoshi a_1
            hide connie with moveoutleft

            jump House_fun

label House_fun:
    kiyoshi "This remote is best thing that happened to me, it's awesome!.. like a dream come true!"
    "My mother is coming in the living room with my first lovers"
    show kiyoshi:
        ease 1.0 xpos 0.1
    show flavia:
        ease 1.0 xpos 0.9
    outfit allison nude
    outfit connie nude
    outfit sayaka nude
    show connie a_0 at centerright, faceleft with easeinright
    show allison a_0 at center, faceleft with easeinright
    show sayaka a_1 at centerleft, faceleft with easeinright
    pause 0.5
    kiyoshi "I love too see all my harem in it's glory.. All that beautiful girls just for me.. thanks to that little remote!"
    show kiyoshi a_6
    kiyoshi "I own you! OK?"
    show allison a_1 blush
    show sayaka a_2 blush
    show connie a_1 blush
    show flavia a_2 blush
    sayaka "Yes lover!"
    connie "Yes honney!"
    allison "I'm your!"
    flavia "Yes bro!"
    show allison a_0 blush
    show connie a_0 blush
    show sayaka a_1 blush
    show flavia a_1 blush
    pause 0.5
    show kiyoshi a_1
    kiyoshi "I'm thinking of little sister.. I want her in my harem too"
    kiyoshi "Where is she mum?"
    show connie a_1 blush
    connie "I think she is in her bedroom honney!"
    show connie a_0 blush
    kiyoshi "Ok, it should be easy!"
    kiyoshi "But how should i approach her?"
    menu:
        "Transform into my big sis":
            routename "Sisters love"
            kiyoshi "I think i can have so much fun to become my big sister to have fun with the little!"
            "I copy Flavia and use the remote on me"
            morph begin alien kiyoshi flavia nude a_4 blush
            kiyoshi "I feel it! I'm becoming you sis!"
            show flavia a_2 blush
            flavia "I hope you'll love my body!"
            show flavia a_1 blush
            kiyoshi "I hope too!"
            morph do
            kiyoshi "My skin is besoming so soft.. You are really taking care of yourself sis eheh!"
            morph end
            kiyoshi "Woaw! I'm you!"
            show kiyoshi a_1 blush
            kiyoshi "I think i should dress.. Sis give me your uniform"
            show flavia a_2 blush
            flavia "yes lover!"
            show flavia a_1 blush
            "While i dress i take care to carress my new body.. Boobs on your own chest feel awesome!"
            outfit kiyoshi uniform
            show kiyoshi a_0 blush
            kiyoshi "Ok, let's go see little sis now!"
            "I said with a grin"
            hide kiyoshi with moveoutleft
            scene black
            with dissolve
            scene bg katrina bedroom day
            outfit natalie casual
            show natalie a_3 at center
            "My little is playing with some toys.."
            show kiyoshi a_0 at centerleft, faceright with easeinleft
            show natalie c_1
            "When she saw me a smile appear on her face"
            natalie "Sister! Do you come here to play with me?"
            show natalie a_3
            kiyoshi "Yes little sis, in some way eheh"
            "An idea come to me, i grin"
            show kiyoshi a_1 blush
            pause 0.6
            show kiyoshi a_4 blush
            kiyoshi "Sis, i'm here to ask you something..."
            "She look at me"
            show natalie a_5
            natalie "What sister? you start to scary me..."
            "I undress"
            outfit kiyoshi nude
            show kiyoshi a_1
            "I show her MY pussy"
            kiyoshi "actually, i lost something here and i want you to help me get it"
            show natalie a_3
            "She look at me with big eye, she doesn't want to put her hand here but at the same time she doesn't want to disobey her big sister"
            show natalie a_5
            natalie "If it's what you want sis.."
            show kiyoshi a_0 behind natalie
            show kiyoshi:
                ease 1.0 yanchor 0.7
            show natalie:
                faceleft
                ease 1.0 xpos 0.34 yanchor 0.5
            "She approach me, and start to put her hand into MY vagina"
            show kiyoshi a_3
            "She start moving her hand to search for an unexisting thing"
            "I push her arm in my vagina and a wave of pleasure hit me"
            show kiyoshi a_6
            kiyoshi "AHHHhhhhhhh..."
            show natalie a_6
            "She stop, afraid to do pain to her big sister"
            show kiyoshi:
                ease 1.0 yanchor 1.0
            show natalie:
                faceleft
                ease 1.0 xpos 0.6 yanchor 1.0
            natalie "Are you ok sis?"
            "I ignore her, i think it's time to morph back"
            show natalie a_4
            natalie "Sis what are you doing?..."
            morph begin alien kiyoshi kiyoshi casual_b a_1
            kiyoshi "Always the same feeling.. it's become casual"
            morph do
            kiyoshi "i feel my dick coming.."
            morph end
            kiyoshi "Ok, i'm myself back!"
            show kiyoshi a_2
            natalie "..um?.. Broth.."
            "Before my little sis understand, i press the button"
            show expression alien_particles(400, 200, 220, mind_scale) as particles:
                xpos placement_of(natalie).xpos + 0.0000
                ypos 0.30
                alien_particles_fadeinout(0.75)
            "Sis became quiet and entered a vegetative state"
            show natalie a_4
            kiyoshi "Sis! you now love me more than anything in the world"
            kiyoshi "You'll love to satisfy my desire"
            "i free her to see the result"
            show natalie a_1
            natalie "Brother i love you so much"
            show natalie a_0
            kiyoshi "I know sis.. you can stay here and play with your toys, i'll come back later"
            show natalie a_1
            natalie "Thanks Bro! I love you soooo mmuuucchhh!"
            show natalie a_0
            "I think it's time to go in the living room prepare myself for news girls ahahahah"
            hide kiyoshi with moveoutleft

            jump Neighbor_fun

        "Possess her":
            routename "Sister possession"
            kiyoshi "I think possess her should be fun"
            exspirit kiyoshi a_5
            "Get out of your own body is always a strange experience.."
            show kiyoshiGhost a_1
            hide kiyoshiGhost with moveoutleft
            scene bg katrina bedroom day
            outfit natalie casual
            show natalie a_3 at center
            show kiyoshiGhost a_0 at centerleft, faceright with easeinleft
            "She is playing with some of her toys"
            "I lost no time and jump in her"
            possess kiyoshi natalie a_4 blush
            kiyoshi "..ah.."
            pause 0.8
            show kiyoshi a_1 blush
            "I look at my new self"
            kiyoshi "It's fantastic I'm my little sister!"
            "I start to undress her little body"
            outfit kiyoshi nude
            show kiyoshi a_0 blush
            kiyoshi "You have firm soft boobs sis, it'll be nice to play with them eheh"
            show kiyoshi a_1 blush
            kiyoshi "I'm my little sister!"
            "I said with her hight pitched voice"
            "While i look at her body, i wonder what it feel like to masturbate in her body, so i take one of her toy and start to masturbate with it"
            show kiyoshi a_8 blush
            kiyoshi "Oh..YESSSSS.."
            "I say in her voice"
            pause 0.5
            show kiyoshi a_0 blush
            kiyoshi "it's so tight down here...aaAAHHH.."
            pause 0.8
            kiyoshi "So different than my dick.."
            kiyoshi "I think i'm cuUUMMMIIINNGGG!"
            with hpunch
            show kiyoshi a_8 blush
            pause 0.6
            "It was fun, i think i should left her body and just brainwash her now"
            exspirit kiyoshi a_5
            "I go down to the living room to repossess my body"
            hide kiyoshiGhost with moveoutleft
            scene black
            with dissolve
            scene bg main livingroom day
            outfit kiyoshi casual_b
            show kiyoshi a_1 at centerleft
            pause 0.8
            show kiyoshi a_6
            kiyoshi "It's time to control you little sis eheh!"
            "I say with a grin"
            hide kiyoshi with moveoutleft
            scene black
            with dissolve
            scene bg katrina bedroom day
            outfit natalie nude
            show natalie a_4 at center
            show kiyoshi a_1 at centerleft, faceright with easeinleft
            "When i enter in her bedroom, i see her naked with fluids down her little legs"
            show kiyoshi a_6
            kiyoshi "Are you alright sis?"
            show natalie a_5
            "She look at me and cover her lady parts"
            natalie "I don't know what is going on!.. I was playing and sudenly i black out.."
            natalie "When i get up i was naked and i'm feeling weird down here!"
            "I grin at the situation"
            pause 0.4
            "I decide to take her now"
            kiyoshi "Calm down sis, it's finish.."
            "I press the button"
            show expression alien_particles(400, 200, 220, mind_scale) as particles:
                xpos placement_of(natalie).xpos + 0.0000
                ypos 0.30
                alien_particles_fadeinout(0.75)
            "Sis became quiet and entered a vegetative state"
            show natalie a_7
            kiyoshi "Sis! you now love me more than anything in the world"
            kiyoshi "You'll love to satisfy my desire"
            "i free her to see the result"
            show natalie a_1
            natalie "Brother i love you so much"
            show natalie a_0
            kiyoshi "I know sis.. you can stay here and play with your toys, i'll come back later"
            show natalie a_1
            natalie "Thanks Bro! You are so nice"
            show natalie a_0
            "I think it's time to go in the living room prepare myself for news girls ahahahah"
            show kiyoshi a_1
            hide kiyoshi with moveoutleft

            jump Neighbor_fun

        "Just brainwash her, like others":
            routename "Brainwasher sister"
            kiyoshi "I want to have her now, just brainwash her should be nice"
            hide kiyoshi with moveoutleft
            scene black
            with dissolve
            scene bg katrina bedroom day
            outfit natalie casual
            show natalie a_3 at center
            outfit kiyoshi casual_b
            "She is playing with some of her toys"
            show kiyoshi a_1 at centerleft, faceright with easeinleft
            natalie "Hi bro"
            show kiyoshi a_6
            kiyoshi "It's time to control you little sis"
            show natalie a_4
            natalie "What are you talkin..."
            "I press the button"
            show expression alien_particles(400, 200, 220, mind_scale) as particles:
                xpos placement_of(natalie).xpos + 0.0000
                ypos 0.30
                alien_particles_fadeinout(0.75)
            "Sis became quiet and entered a vegetative state"
            show natalie a_4
            kiyoshi "Sis! you now love me more than anything in the world"
            kiyoshi "You'll love to satisfy my desire"
            "i free her to see the result"
            show natalie a_1
            natalie "Brother i love you so much"
            show natalie a_0
            kiyoshi "I know sis.. It's time to play with your new toy"
            "As i say that i unzip my pant"
            kiyoshi "Suck it like a lollipop!"
            show natalie a_1
            natalie "As you with bro! I love you sooo mmuucchh!"
            show kiyoshi a_6 behind natalie
            show kiyoshi:
                ease 1.0 yanchor 0.7
            show natalie:
                ease 1.6 xpos 0.34 yanchor 0.2
            natalie "It's beautiful bro! I want it in my mouth.."
            show natalie:
                pause 0.2
                block:
                    ease 0.2 xpos 0.335
                    pause 0.5
                    ease 0.2 xpos 0.345
                    repeat
            "Her lips wrap around the head of my cock and she begin to move, she do little circle with her tongue"
            kiyoshi "You are doing it very nice sis!"
            natalie "Mmmmfhh.. mmfhhh.."
            pause 0.3
            "Having my little sister sucking my dick make me build an orgasm very fast.."
            kiyoshi "It's too much.. I'M CUMMING!.."
            with hpunch
            "My sister suck it until the last drop get out"
            hide natalie
            show natalie a_4 at center
            show kiyoshi:
                ease 1.0 yanchor 1.0
            "I see she have all my cum in her mouth"
            show natalie a_0
            natalie "..gulp.. mmhhhh... you are delicious bro!"
            kiyoshi "Thanks sis! You can stay here and play with your toys, i'll come back later"
            show natalie a_1
            natalie "Thanks Bro! I love you so much!"
            show natalie a_0
            pause 1.0
            "Ok, I think it's time to go in the living room prepare myself for news girls ahahahah"
            hide kiyoshi with moveoutleft

            jump Neighbor_fun

label Neighbor_fun:
    scene black
    with dissolve
    scene bg main livingroom day
    outfit connie nude
    outfit flavia nude
    outfit allison nude
    outfit sayaka nude
    show allison a_0 at center, faceleft
    show sayaka a_1 at centerleft, faceleft
    show connie a_0 blush at centerright, faceleft
    show flavia a_1 blush at right, faceleft
    "My home harem Is waiting me in the living room.. naked in all their glory.. just for me!"
    show kiyoshi a_1 at left, faceright with easeinleft
    "I think i should choose a manager for this harem.. Maybe my mom, she is the oldest"
    kiyoshi "Mom, I make you responsible of the girls in this house!"
    show connie a_1 blush
    connie "Thanks lover! You will not regret it!"
    show connie a_0 blush
    "So i have two girls and my family at my feet.. Awesome!"
    "You finished the family enslavement!"

    $ Family = True

    if not Cheerleaders or not Teachers:
        jump chapter_one

    if Family and Teachers and Cheerleaders:
        jump chapter_two

label School_fun_teachers:
    routename "The school leader"
    "I look at the three beautiful teachers in front of me"
    kiyoshi "Do you want to expend the harem girls?"
    show leona a_4 blush
    show yuuna a_2 blush
    show abby a_2 blush
    yuuna "Fuck yes i want!"
    leona "yes.. lover!"
    abby "I want what you want Kiyoshi!"
    show kiyoshi a_6
    show leona a_1 blush
    show yuuna a_0 blush
    show abby a_1 blush
    "I smile as they say that"
    kiyoshi "Good answer lovers.. ahah"
    pause 0.3
    show kiyoshi a_1
    "Three of my teachers now at my feet, just because of this little remote... I love my life"
    "Let the fun continue, let's go take the principal to have the school at my feet"
    kiyoshi "Someone know where is the principal?"
    show yuuna a_2 blush
    yuuna "yes lover! He is with miss catherine on the roof, they try to catch some student that go there to smoke sometimes"
    show yuuna a_0 blush
    kiyoshi "So the principal and miss catherine try to catch some smokers eheh.. I should mess with them!"
    hide kiyoshi with moveoutleft
    scene black
    with dissolve
    scene bg school roof day
    outfit Harem_catherine whistle
    show Harem_catherine a_2 at center
    show jack a_0 at centerright
    show jack:
        faceleft
    "As i come on the roof, i hide behind a wall.. and i hear them speack"
    show kiyoshi a_1 at left, faceright with easeinleft
    jack "So catherine, is it here that you saw a student smoked?"
    Harem_catherine "Yes sir.. just hide and wait.. She comes every day at the break of 10am"
    "While she say that, they hide behind a wall"
    show jack behind Harem_catherine
    show jack:
        xpos 0.9
    show Harem_catherine:
        xpos 0.8
    pause 1.0
    show Harem_catherine:
        faceleft
    "While they put themselves in position, a girl come.. certainly the smoker that the principal speack of before"
    show alex a_5 at center, faceright with easeinleft
    "Before the pincipal and miss catherine move, i think of something.."
    menu:
        "I should mess with the principal and the smoker, but how?"

        "{s}Morph him into the smoker{/s}":
            routename "School_principal_Morph"
            placeholder

        "Swap him with the smoker":
            routename "School_principal_Swap"
            "I think bodyswap them should be fun"
            "As i fire the beam, they all freeze in chock"
            swap jack a_8 : a_6, alex a_4 : a_4
            show Harem_catherine a_5
            show alex a_7
            show jack a_7
            alex "What the fuck is going on! WHAT.. ME?! Ahhhh...."
            hide alex with moveoutleft
            "While she say that with the principal voice, she run to the stair"
            show jack a_8
            "On the other side, the principal, now the smoker, start to touch is body.. wondering why he saw his own body run away and why he have boobs"
            show jack a_6
            jack "Oh my GOD! he say as he caress his news breast"
            pause 0.3
            "Miss catherine is wondering what just happened with the principal and she see the student start touching her girly parts.."
            show Harem_catherine a_4
            show Harem_catherine:
                ease 1.0 xpos 0.7
            Harem_catherine "Hey miss! what do you think you are doing?! We are at school not in your bedroom!"
            show Harem_catherine a_3
            show jack a_4
            "As she say that, the principal come back to reality.. I think i should help him and join the mess!"
            exspirit kiyoshi a_1
            "Miss catherine you'll join the fun eheh!"
            possess kiyoshi Harem_catherine a_5
            pause 1.0
            show kiyoshi b_7
            kiyoshi "Woaw.. It feel awesome"
            pause 0.2
            show kiyoshi a_0
            kiyoshi "Sooo... ALEX! You are a little naughty girl are you?"
            "While i say that, i'm starting to strip! The look on his new face is magic"
            outfit kiyoshi nude
            "The principal look at my beauty.. I think i should swap him with miss catherine ahah!"
            kiyoshi "I think it's your turn to strip.. MISS!"
            pause 0.2
            show jack a_0
            jack "As you wish.. catherine.."
            outfit jack nude
            show jack a_9
            "So good, now i can order the principal.. what a situation!"
            "He is carressing is body, making some feminine gasp in the process.."
            menu:
                "What should i do with him?"

                "Just brainwash him":
                    "I think for now i'll just make him.. now her.. my lover"
                    show expression alien_particles(400, 200, 220, mind_scale) as particles:
                        xpos placement_of(jack).xpos + 0.0000
                        ypos 0.30
                        alien_particles_fadeinout(0.75)
                    "As the beam touch him, he stop to touch his new body and he looks in the void"
                    show jack a_6
                    kiyoshi "You'll do whatever I tell you to do from now on"
                    kiyoshi "And you'll masturbate thinking of me every day"
                    "And i free him"
                    show jack a_9
                    kiyoshi "So ALEX, you are now my lover, right?"
                    show jack a_1 blush
                    jack "Yes lover!"
                    show jack a_0 blush
                    "He say in a slutty voice"
                    pause 0.2
                    "Ok, it's time to get miss catherine now.. i should leave her body"
                    exspirit kiyoshi a_5
                    show kiyoshiGhost a_1
                    "I left Miss catherine body and return to mine"
                    hide kiyoshiGhost
                    outfit kiyoshi uniform
                    show kiyoshi a_1 at left
                    "When i come back, Miss catherine get up"
                    outfit Harem_catherine nude
                    show Harem_catherine a_7:
                        faceleft
                        centerright
                    pause 0.3
                    show Harem_catherine b_2
                    Harem_catherine "...What happened?!.. Wait.. WHY AM I NAKED! Oh my g.."
                    "No need to wait, i hit the button"
                    Harem_catherine "Wai.."
                    show expression alien_particles(400, 200, 220, mind_scale) as particles:
                        xpos placement_of(Harem_catherine).xpos + 0.0000
                        ypos 0.30
                        alien_particles_fadeinout(0.75)
                    "catherine became quiet and entered a vegetative state"
                    show Harem_catherine b_6
                    kiyoshi "catherine! I'm now your master, and you'll be my sex slave"
                    "I think it's time to free her"
                    show Harem_catherine b_0
                    show kiyoshi a_6
                    pause 0.5
                    show Harem_catherine a_6
                    "She look at me.. with a submissively look"
                    kiyoshi "Now i have Miss catherine and the principl at my feet, i think the real Alex in the principal body should not be a problem but just in case i'll send Jack.."
                    kiyoshi "Principal, i think you should find your body and discuss with his new possessor.. Maybe offer her a blowjob eheh!"
                    show jack a_1 blush
                    jack "As you wish!"
                    show jack a_0 blush
                    hide jack with moveoutleft
                    pause 0.1
                    kiyoshi "Miss catherine! let's go to the teacher's room!"
                    Harem_catherine "Yes lover!"
                    hide kiyoshi with moveoutright
                    hide Harem_catherine with moveoutright

                    jump Five_Teachers_fun

                "{s}Have some fun ordering him{/s}":
                    placeholder

label Five_Teachers_fun:
    scene black
    with dissolve
    scene bg classroom 3 day
    outfit abby nude
    outfit Harem_catherine nude
    outfit leona nude
    outfit yuuna casual
    show abby a_1 blush at center, faceleft
    show leona a_1 blush at centerright, faceleft
    show yuuna a_0 at right, faceleft
    "The teachers were waiting us in the teacher's room"
    show Harem_catherine a_0 blush at centerleft, faceleft with easeinleft
    show kiyoshi a_1 at left, faceright with easeinleft
    "While we come, i see that miss Yuuna is dressed, i should correct that!"
    kiyoshi "Miss Yunna strip like the others please! I do not want to make favorites"
    show yuuna a_1 blush
    yuuna "yes lover!"
    show yuuna a_2
    "She start undressing, looking at me in the process"
    outfit yuuna nude
    "Now i have all the teachers at my feet.."
    "You finished the teachers enslavement!"

    $ Teachers = True

    if not Cheerleaders or not Family:
        jump chapter_one

    if Family and Teachers and Cheerleaders:
        jump chapter_two

label Cheerleaders_fun:
    routename "The two last cheerleaders"
    outfit yui nude
    outfit irene nude
    outfit mel nude
    outfit cassie nude
    show kiyoshi a_6
    kiyoshi "I have four of the six cheerleaders and i want the last two in my harem too"
    kiyoshi "Cassie, where are the last two cheerleaders? I want to complete my cheerleaders collection eheh!"
    show cassie b_1 blush
    cassie "They are certainly at the school pool, lover!"
    show cassie b_0 blush
    kiyoshi "Nice.. I should go take them.. you will stand me here.. alright?"
    show cassie b_1 blush
    show yui b_0 blush
    show irene a_1 blush
    show mel a_1 blush
    mel "Yes lover!"
    yui "Yes!"
    irene "Yes Kiyoshi!"
    cassie "Yes lover!"
    show yui b_5 blush
    show irene a_0 blush
    show mel a_0 blush
    show cassie b_0 blush
    pause 0.4
    show kiyoshi a_1
    kiyoshi "Ok.. Here we go!"
    hide kiyoshi with moveoutleft
    scene black
    with dissolve
    scene bg school pool day
    outfit tori swimsuit
    outfit vanessa swimsuit
    show tori b_0 at centerright
    show tori:
        faceleft
    show vanessa b_0 at center
    "The last two cheerleaders are here; Tori and Vanessa.."
    "They are discussing near the pool, How should i approach them?"
    show kiyoshi a_1 at left, faceright with easeinleft
    menu:
        "Go as a ghost":
            routename "Possessing at pool"
            "I think i should go as a ghost.."
            exspirit kiyoshi a_1
            "But who possess?.."
            "There are rumors that Vanessa is a lesbian.. so let's go possess Tori and try to seduce her!"
            "While i approach Tori, they are discussing.."
            tori "No, I'm terrible! I can't even use a digital camera."
            vanessa "Ah, you can't be that bad! You must have at least some good pictures."
            tori "Not really. All my pic..."
            possess kiyoshi tori b_4 blush
            "I don't let her finish her sentence and i jump in her body"
            show vanessa b_4
            pause 0.5
            "It felt weird.."
            show vanessa b_5
            vanessa "Tori? are you alright?"
            pause 0.2
            "I regain my sense and look at her"
            show kiyoshi b_7 blush
            "I start to carress my borrowed body"
            show vanessa b_4
            kiyoshi "MMmmmm... so good.."
            "I say with Tori sexy voice... I massage my new breast with Tori soft hands in front of Vanessa"
            vanessa "ARE YOU TOUCHING YOURSELF IN FRONT OF ME?!"
            show vanessa b_0 blush
            "I start to caress my borrowed pussy from my swimsuit"
            show vanessa b_1 blush
            "A smile appear on Vanessa face, i think she love the show eheh"
            show kiyoshi b_5 blush
            kiyoshi "MMmmmm... OOoohh.."
            vanessa "WOAW Tori! I didn't thought to look you do that in front of me.. You are making me so hot!"
            show vanessa b_0 blush
            "I take her hand and put it in my swimsuit.. on MY pussy"
            show kiyoshi b_4 blush
            show vanessa b_1 blush
            "She remain silent.."
            "But something unexpected happened! she slowly put three fingers in my vagina and start fingering me!"
            show kiyoshi b_7 blush
            kiyoshi "OHHH YESSS! Don't stop!.."
            "I feel a presure build inside of me..."
            show kiyoshi b_5 blush
            kiyoshi "I WANT MORE!"
            outfit kiyoshi nude
            show kiyoshi behind vanessa
            show kiyoshi:
                ease 1.0 yanchor 0.7
            show vanessa:
                ease 1.2 xpos 0.55 yanchor 0.2
            show vanessa b_4 blush
            "I strip and put Vanessa head in front of my clit.. She instinctivly start to lick it"
            show kiyoshi b_7 blush
            show vanessa:
                ease 1.2 xpos 0.62 yanchor 0.2
                pause 0.5
                block:
                    ease 0.2 yanchor 0.2
                    pause 1.2
                    ease 0.2 yanchor 0.19
                    repeat
            show vanessa b_2 blush
            kiyoshi "YOUR TONGUE FEEL SO GOOD!"
            vanessa "You tatste so good Tori!"
            pause 0.2
            kiyoshi "Soooo nice... don't stop Vanessaaaaa.."
            pause 0.5
            kiyoshi "Your tongue feel so good!"
            "And i cum.."
            with hpunch
            "Vanessa lick all MY fluids until the last drop get out"
            show kiyoshi b_3 blush
            hide vanessa
            show kiyoshi:
                ease 1.0 yanchor 1.0
            pause 1.0
            show vanessa b_1 blush at center
            vanessa "Woaw Tori! That was unexpected coming from you.."
            show kiyoshi b_2 blush
            kiyoshi "Thanks! Now i want you to become my lover for ALL YOUR LIFE!"
            show kiyoshi b_1 blush
            show vanessa b_0
            vanessa "Wha..."
            show expression alien_particles(400, 200, 220, mind_scale) as particles:
                xpos placement_of(vanessa).xpos + 0.0000
                ypos 0.30
                alien_particles_fadeinout(0.75)
            "Vanessa enter a trance as the beam hit her"
            show vanessa b_2
            kiyoshi "Vanessa! For now on you'll be my sexslave!"
            kiyoshi "You will do whatever I tell you to do"
            "And i free her"
            show vanessa b_1 blush
            "When i free her, she look at me with lust"
            kiyoshi "Vanessa strip for me!"
            vanessa "Yes lover!"
            outfit vanessa nude
            show vanessa a_3 blush
            "Time to leave Tori body..."
            exspirit kiyoshi a_5
            show kiyoshiGhost a_1
            "I left Vanessa body and return to mine"
            hide kiyoshiGhost
            outfit kiyoshi uniform
            show kiyoshi a_1 at left
            "When i come back, Tori get up"
            outfit tori nude
            show tori b_5:
                faceleft
                centerright
            tori "...What happened? Vanessa why are you naked?"
            show tori b_4
            "While she say that, i hit the brainwash button"
            vanessa "Wai.."
            show expression alien_particles(400, 200, 220, mind_scale) as particles:
                xpos placement_of(tori).xpos + 0.0000
                ypos 0.30
                alien_particles_fadeinout(0.75)
            "Tori became quiet and entered a vegetative state"
            show tori b_7
            kiyoshi "Tori! For now on you'll be my sexslave!"
            kiyoshi "You will do whatever I tell you to do"
            "And i free her"
            show tori b_5 blush
            pause 0.6
            show tori b_8 blush
            "Like Vanessa, she look at me with lust"

            jump Cheerleaders_finished

        "{s}Morph into one of the cheerleader{/s}":
            placeholder

        "{s}Body swap them and look the mess{/s}":
            placeholder

        "Mess with their brain a little":
            routename "Brainwashing at pool"
            "I'll brainwash Tori, and watch what Vanessa will do with her.. this should be fun"
            "They are speacking"
            tori "No, I'm terrible! I can't even use a digital camera."
            vanessa "Ah, you can't be that bad! You must have at least some good pictures."
            tori "Not really. All my pic..."
            "I press the button before she coulf finish her sentence"
            show expression alien_particles(400, 200, 220, mind_scale) as particles:
                xpos placement_of(tori).xpos + 0.0000
                ypos 0.30
                alien_particles_fadeinout(0.75)
            "Tori became quiet and entered a vegetative state"
            show tori b_7
            show vanessa b_4
            pause 0.2
            vanessa "Tori? are you alright?"
            tori "..."
            show vanessa b_5
            pause 0.2
            show vanessa b_0
            "She start to touch her, pinch her and put her hand in front of her friend face.. but nothing do, Tori stay motionless with a blanck look"
            pause 0.2
            show vanessa b_4
            vanessa "Are you in trance?!"
            tori "..."
            pause 0.2
            show vanessa b_1
            vanessa "YESSSSS you are in trance ahah.. i think i could have some fun with you like this.."
            "Vanessa look at her friend with a mischievous smile"
            vanessa "You know.. i never say it but i'm a lesbian.. i don't want all the cheerleaders to laugh at me so i keep it to myself.. but now you can be my lover, right?"
            tori "..."
            vanessa "I mean you will be my lover, my slave.. or better.. my SEX slave! and it's an order! now came back to me, slave"
            "She grin as she say that, and i free Tori"
            show tori b_5
            show vanessa b_3
            tori "Mmmh.. What is just going on?..."
            vanessa "I don't know... Are you alright?"
            show tori b_8 blush
            "As she ask that, Tori look at her.. with a lover smile"
            show vanessa b_1 blush
            show tori b_2 blush
            tori "Yes mistress!"
            show tori b_1 blush
            "Vanessa smile at her new sex slave"
            vanessa "Don't make me wait slave, LICK my pussy with adoration, you will love my juice more than anything in the world"
            show tori b_2 blush
            tori "Yes mistress!"
            show tori b_1 blush
            "Vanessa start removing her bikini"
            outfit vanessa nude
            show vanessa a_3 blush
            pause 0.2
            "Vanessa pur her friend face in front of her pussy"
            show vanessa a_1 behind tori
            show tori b_3 blush
            show vanessa:
                ease 1.0 yanchor 0.7
            show tori:
                ease 1.2 xpos 0.53 yanchor 0.2
                pause 0.5
            vanessa "LICK ME!"
            show tori:
                pause 0.1
                block:
                    ease 0.2 xpos 0.53 yanchor 0.2
                    pause 1.0
                    ease 0.2 xpos 0.52 yanchor 0.19
                    repeat
            "As Tori lick her friend, an idea come to me.. why let Vanessa have all the fun..eheh.."
            exspirit kiyoshi a_1
            possess kiyoshi vanessa a_7 blush
            kiyoshi "Woaw.."
            "i lost my sense for some second"
            pause 0.2
            show kiyoshi a_0 blush
            "Having his pussy licked is a strange sensation.."
            kiyoshi "It's so nice... don't stop Tori"
            tori "B..Bes Bistress..gulp.."
            show kiyoshi a_1 blush
            "She say as she lick MY pussy and drink MY juice ahah"
            pause 0.2
            "Being licked as Vanessa by Tori is awesome! I can't take it longer"
            show kiyoshi a_3 blush
            kiyoshi "I'M CUMMING!.."
            with hpunch
            "She finish me and lick all MY fluids until the last drop get out"
            hide tori
            show kiyoshi:
                ease 1.0 yanchor 1.0
            show tori b_1 blush at centerright
            kiyoshi "Tori, you are now the properties of Kiyoshi, not Vanes.. eh me, NOT MINE! you will love him more than anything in the world.. right?"
            show tori b_2 blush
            tori "Yes mistress!"
            show tori b_1 blush
            kiyoshi "And Tori... i want to see you naked"
            show tori b_2 blush
            tori "Yes mistress!"
            "She start to undress, as her mistress ordered her"
            outfit tori nude
            show tori b_3 blush
            pause 0.5
            kiyoshi "It was fun but i free you Vanessa.. for now eheh!"
            exspirit kiyoshi a_5
            show kiyoshiGhost a_1
            "I left Vanessa body and return to mine"
            hide kiyoshiGhost
            outfit kiyoshi uniform
            show kiyoshi a_1 at left
            "When i come back, Vanessa get up"
            outfit vanessa nude
            show vanessa b_2:
                faceright
                ease 1.2 center
            vanessa "...What happened?"
            show vanessa b_3
            "I hit the button before she could react"
            vanessa "Wai.."
            show expression alien_particles(400, 200, 220, mind_scale) as particles:
                xpos placement_of(vanessa).xpos + 0.0000
                ypos 0.30
                alien_particles_fadeinout(0.75)
            "Vanessa became quiet and entered a vegetative state"
            show vanessa b_2
            kiyoshi "Vanessa! You'll be my sex slave for now on"
            kiyoshi "You will do whatever I tell you to do"
            "And i free her"
            show vanessa a_1 blush
            pause 0.5
            show vanessa a_3 blush
            "She look at me with lust and passion"

            jump Cheerleaders_finished

label Cheerleaders_finished:
    show kiyoshi a_6
    kiyoshi "You two are my sexslaves for now, right?"
    show tori b_2 blush
    tori "Yes!"
    vanessa "Yes master!"
    show tori b_1 blush
    show kiyoshi a_1
    "You finished the cheerleaders enslavement!"

    $ Cheerleaders = True

    if not Family or not Teachers:
        jump chapter_one

    if Family and Teachers and Cheerleaders:
        jump chapter_two


label chapter_two:
    routename "Chapter two choice"
    "The chapter two start now!"
    kiyoshi "Now i have My teachers, my family and che cheerleaders at my feet.."
    kiyoshi "My mom and my two sis with Sayaka and Allison are in my home.."
    kiyoshi "The teachers are in the teacher's room at school.. Wile the principal is certainly making a blowjob to his old body eheh.."
    kiyoshi "And the cheerleaders are in the gym room and at the swimming pool.."
    kiyoshi "I think it's a good beginning eheh!"
    kiyoshi "But i want more! What should i do now?"
    menu:
        "Possess someone":
            routename "Possession path"
            "I want to possess people, i'll let my body here with the girls"
            exspirit kiyoshi a_5
            show kiyoshiGhost a_0
            kiyoshiGhost "let's go!"
            hide kiyoshiGhost with moveoutleft
            scene black
            with dissolve
            scene bg neighborhood day
            outfit audrey track_b
            show audrey a_3 at center
            show kiyoshiGhost a_0 at centerleft, faceright with easeinleft
            "I see a jogger taking her breath, i think i could possess her to have some fun"
            possess kiyoshi audrey a_7 blush
            kiyoshi "..ah.."
            pause 0.2
            show kiyoshi b_0 blush
            kiyoshi "I'm her!"
            "I start massaging her breast"
            pause 0.3
            kiyoshi "good size and firm.. I think i choose a nice little body eheh"
            show kiyoshi b_0 blush
            kiyoshi "She is beautiful...i mean I'M BEAUTIFUL! Ahahah..."
            pause 0.2
            show kiyoshi b_0 blush
            kiyoshi "It's time for a little inspection down here.."
            show kiyoshi b_1 blush
            kiyoshi "I don't want to keep this body all to myself, i should share it!"
            "I run home to explore my new body with the girls"
            hide kiyoshi with moveoutleft
            scene black
            with dissolve
            scene bg main livingroom day
            show allison a_0 at center, faceleft
            show sayaka a_1 at centerleft, faceleft
            show connie a_0 blush at centerright, faceleft
            show flavia a_1 blush at right, faceleft
            show kiyoshi b_1 at left, faceright with easeinleft
            kiyoshi "Hey girls! do you like my new body?"
            show kiyoshi b_0
            show allison a_1 blush
            show sayaka a_2 blush
            show connie a_1 blush
            show flavia a_2 blush
            sayaka "You are beautiful!"
            connie "Yes honey!"
            allison "You take a nice body!"
            flavia "Yes bro!"
            show allison a_0 blush
            show connie a_0 blush
            show sayaka a_1 blush
            show flavia a_1 blush
            show kiyoshi b_1 blush
            kiyoshi "Nice to hear! i'll go to my bedroom, sayaka and Allison come with me, we will have some fun!"
            show kiyoshi b_0 blush
            pause 0.2
            show allison a_1 blush
            show sayaka a_2 blush
            sayaka "Yes lover!"
            allison "Thanks to share it with me!"
            show allison a_0 blush
            show sayaka a_1 blush
            hide kiyoshi with moveoutright
            hide allison with moveoutright
            hide sayaka with moveoutright
            scene black
            with dissolve
            scene bg main room day
            show kiyoshi b_0 at left, faceright with easeinleft
            show allison a_0 at center, faceleft with easeinleft
            show sayaka a_1 at centerright, faceleft with easeinleft
            "As we enter the room, I strip to see my new body"
            outfit kiyoshi nude
            kiyoshi "Her body is so nice to wear! I think we'll take her in my harem ahah"
            pause 0.2
            show kiyoshi b_4 blush
            kiyoshi "Her body is soooooo niccccceeee.... so soft.."
            "I say as i caress my new skin"
            pause 0.2
            show kiyoshi a_6 blush
            "I press my boobs together with my arms.."
            "This feeling is awesome!"
            pause 1.0
            show kiyoshi a_1 blush
            kiyoshi "What should i do with us girls?"
            show kiyoshi a_0 blush
            menu:
                "{s}Stay the jogger{/s}":
                    placeholder

                "{s}Swap with one of the girl{/s}":
                    placeholder

                "{s}Morph them into the new me to have fun as twins{/s}":
                    placeholder

        "Brainwash more people":
            routename "Brainwash path"
            "I want to mess with people and maybe expend my harem ahahahah..."
            hide kiyoshi with moveoutright
            scene black
            with dissolve
            scene bg neighborhood day
            "As i go out, i see a mom and her son, i can mess a little with them"
            outfit carla casual
            show carla b_5 at centerright, with easeinright
            outfit stevie casual
            show stevie a_0 at center, with easeinright
            "I will let the son do what he want with his mother, this seems interesting"
            stevie "mom can we go home? I want to play videogame!"
            carla "No stevie, we must go buy a gift for your father's birtday"
            stevie "But mom, i want to play NOW!"
            carla "stevie, don.."
            "And i press the button"
            show stevie a_5
            show expression alien_particles(400, 200, 220, mind_scale) as particles:
                xpos placement_of(carla).xpos + 0.0000
                ypos 0.30
                alien_particles_fadeinout(0.75)
            "The mother stopped as the beam hit her.."
            show carla b_3
            stevie "Mom? Are you alright?"
            carla "..."
            show stevie a_4
            stevie "Mom you are not funny, i want to go home now"
            carla "..."
            "He approach her and touch her boob.. but no reaction of the mother"
            stevie "Mom are you in trance?"
            carla "..."
            pause 0.2
            show stevie a_1
            stevie "Mom from now on you will listen to me and do as i order you!"
            carla "..."
            "I think it's time to free her"
            show carla b_6
            carla "ehhh... son?... what is going on?"
            show stevie a_0
            stevie "M..mom.. can we go home so i can play video game?"
            show carla b_1
            carla "Sure honey, as you want"
            show carla b_0
            show stevie a_1
            stevie "Ahah it worked"
            carla "What worked honey?"
            stevie "Nothing mom, come with me!"
            show carla b_1
            carla "Sure"
            show carla b_0
            hide stevie with moveoutright
            hide carla with moveoutright
            "I follow them"
            scene black
            with dissolve
            scene bg michelle livingroom day
            outfit carla casual
            show carla b_0 at centerright, with easeinright
            outfit stevie casual
            show stevie a_1 at center, with easeinright
            "They enter in what it look like to be their home"
            "I take a seat near the windows to observe them"
            stevie "So mom, since we are here... just us, what if you undress for me?"
            show carla b_1
            carla "As you want honey"
            show carla b_0
            outfit carla nude
            stevie "Woaw mom, i masturbated too much time thinking of you, and now you are here, naked for me and obeying my order.. it's a dream come true.."
            "He look at her"
            stevie "Mom from now on you will be my sex slave, you will please me as i want! When i want! Alright?"
            show carla a_1 blush
            carla "Sure honey"
            show carla a_0 blush
            stevie "And you will never say to anyone that you are my sexslave... now go to your bedroom, we'll have some fun!"
            show carla a_1 blush
            carla "As you wish"
            show carla a_0 blush
            hide stevie with moveoutleft
            hide carla with moveoutleft
            "I let them go"
            "This remote have so much possibilities!"
            menu:
                "What should i do next?"

                "Follow them upstair as a ghost":
                    routename "Family mess"
                    "I want to see what he will do with his new GIFT"
                    show kiyoshiGhost a_1 at centerleft, faceright with easeinleft
                    "let's go!"
                    hide kiyoshiGhost with moveoutright
                    scene black
                    with dissolve
                    scene bg laura bedroom day
                    show stevie a_1 at centerleft
                    show carla a_0 at center
                    show kiyoshiGhost a_1 at centerright, faceleft with easeinleft
                    "I come in just in the right time"
                    stevie "Mom! Let the fun begin!"
                    show carla a_1 blush
                    carla "Sure honey, what do you want me to do?"
                    show carla a_0 blush
                    "The mom look at her son with a lover look"
                    menu:
                        "I can watch them or join them, i see another bedroom when i come here, the door looked girly, i can possess the person in this bedroom and join the fun!"

                        "Possess the person in the bedroom":
                            routename "Family mess sister"
                            "I want to join them! let's go possess the person in the next bedroom"
                            hide kiyoshiGhost with moveoutleft
                            scene black
                            with dissolve
                            scene bg katrina bedroom day
                            outfit michelle casual_b
                            show michelle b_4 at center
                            show kiyoshiGhost a_1 at centerleft, faceright with easeinleft
                            "ohhhhh yesss... a sister, i must possess her and join the fun... this is too awesome"
                            possess kiyoshi michelle b_5 blush
                            kiyoshi "..ah.."
                            show kiyoshi b_0 blush
                            pause 0.5
                            show kiyoshi b_1 blush
                            kiyoshi "I'M HER"
                            show kiyoshi b_0 blush
                            "I said as i massage her breast"
                            kiyoshi "I should waste no time, i must join the mother and her son"
                            hide kiyoshi with moveoutleft
                            scene black
                            with dissolve
                            scene bg laura bedroom day
                            show stevie a_1 at centerleft
                            show carla a_0 at center
                            "They are just begining to have fun, i haven't missed the act"
                            show kiyoshi b_0 at centerright, faceleft with easeinleft
                            show stevie a_5
                            stevie "SIS? What are you doing here?.. Mom cover yourself!"
                            show carla a_1 blush
                            carla "Sure honey!"
                            show carla a_0 blush
                            "The mother put her arms on her nipples and her pussy"
                            pause 0.5
                            "I smile at the situation"
                            show kiyoshi b_1 blush
                            kiyoshi "Hi BRO! I heard you and mom have some fun! And i want to join the fun, mind if i come?"
                            show kiyoshi b_0 blush
                            "As i say that i start undressing.. taking care to look him in the eyes in the process"
                            outfit kiyoshi swimsuit
                            "He look at me with lust.. i make sexy move during my stip"
                            pause 0.5
                            "And i finish to strip"
                            outfit kiyoshi nude
                            show kiyoshi b_1 blush
                            kiyoshi "Do you like what you see bro?"
                            show kiyoshi b_0 blush
                            "I said with his sister slutty voice"
                            pause 0.5
                            show stevie a_1
                            stevie "It's a dream come true... i don't know what is going on but i love it!"
                            show kiyoshi b_3 blush
                            "As he say that, i think that he want certainly to fuck his big sister... ME"
                            show kiyoshi a_0 blush
                            show kiyoshi:
                                faceleft
                            "I don't want that, i think i will swap with him, let him believe his sister is in his body... this will be fun ahah"
                            "I press the button"
                            swap kiyoshi a_0 : a_1, stevie a_5 : a_9
                            "He is certainly wondering what just happened to him ahah"
                            show stevie a_7
                            pause 0.2
                            show stevie a_4
                            stevie "What is goin..  WHAT? ME? but..."
                            "He look at him, take his news breast in his news small soft hands and massage them"
                            pause 0.2
                            show stevie a_4 blush
                            stevie "OHMYGOD! i'm my sister"
                            kiyoshi "Sure you are, take my body and go have fun bro, it's my gift to you!"
                            show stevie b_1 blush
                            pause 0.5
                            show stevie b_0 blush
                            stevie "This day is too awesome, if it's a dream i don't want to wake up!"
                            stevie "Thanks sis, i will show my new body to my friends, i think they will love it ahah!"
                            kiyoshi "As you wish.. BIG SISTER"
                            hide stevie with moveoutleft
                            "He run out of the house, i look at him by the bedroom's window, he forget to dress to go out.."
                            pause 0.5
                            "I look at the mother.. now MY mother.."
                            menu:
                                "What should i do with her?"

                                "Morph myself as her daughter and have fun with her":
                                    routename "Family mess sis mom"
                                    "I want to have fun with her but not like this, let's change"
                                    morph begin alien kiyoshi michelle nude a_0 blush
                                    kiyoshi "the feeling is strange..."
                                    morph do
                                    kiyoshi "i feel my boobs grow... it's fantastic!"
                                    morph end
                                    kiyoshi "Woaw i'm so beautiful.."
                                    show kiyoshi b_0 blush
                                    pause 1.0
                                    show kiyoshi b_1 blush
                                    kiyoshi "I'm beautiful"
                                    show kiyoshi b_0 blush
                                    "Now let have some fun with MY MOM!"
                                    kiyoshi "mom lick me until i cum, you will drink my juice until the last drop!"
                                    show carla a_1 blush
                                    carla "Sure honey!"
                                    show carla a_0 blush
                                    pause 1.0
                                    show kiyoshi b_6 blush behind carla
                                    show carla b_1 blush
                                    show kiyoshi:
                                        ease 1.0 yanchor 0.7
                                    show carla:
                                        ease 1.2 xpos 0.34 yanchor 0.2
                                        pause 0.3
                                        block:
                                            ease 0.2 xpos 0.335 yanchor 0.2
                                            pause 1.0
                                            ease 0.2 xpos 0.335 yanchor 0.19
                                            repeat
                                    "Her tongue feel awesome in mu pussy, this is just awesome... so different that being a man"
                                    show kiyoshi b_7 blush
                                    kiyoshi "Woaw mom, don't stop"
                                    show kiyoshi b_8 blush
                                    kiyoshi "Ohh... MOM.. it's awesome.."
                                    pause 0.5
                                    show kiyoshi b_1 blush
                                    kiyoshi "I'M CUMMING!.."
                                    with hpunch
                                    "my new mom lick my pussy lips until the last drop get out"
                                    show kiyoshi b_0 blush
                                    hide carla
                                    show kiyoshi:
                                        ease 1.0 yanchor 1.0
                                    pause 1.0
                                    show carla a_0 blush at center
                                    pause 1.0
                                    stevie "It was awesome mom.."
                                    show carla a_1 blush
                                    carla "Thanks honey!"
                                    show carla a_0 blush
                                    pause 1.0
                                    menu:
                                        "What should i do now?"

                                        "{s}Swap with her{/s}":
                                            placeholder

                                        "Let her go":
                                            kiyoshi "MOM! I'll be in MY bedroom if you need me.. you are free for now!"
                                            "I said with a grin"
                                            show carla a_1 blush
                                            carla "Thanks!"
                                            show carla a_0 blush
                                            hide carla with moveoutleft
                                            "I think i should go to Michelle..now my bedroom.. i want to see the world thought her eyes eheh.."
                                            hide kiyoshi with moveoutleft
                                            scene black
                                            with dissolve
                                            scene bg katrina bedroom day
                                            outfit michelle casual_b
                                            show kiyoshi b_0 at center, faceright with easeinleft

                                            jump Fun_as_a_girl

                                "{s}Have fun with her like this{/s}":
                                    routename "Family_mess_son_mom"
                                    placeholder

                        "Just watch":
                            routename "Family mess watch"
                            "I think i'll just watch what the son will do with his new sexslave"
                            stevie "mom suck me until i cum, you will drink my cum until the last drop!"
                            show carla a_1 blush
                            carla "Sure honey!"
                            show carla a_0 blush
                            pause 0.2
                            show stevie a_1 behind carla
                            show carla b_1 blush
                            show stevie:
                                ease 1.0 yanchor 0.7
                            show carla:
                                ease 1.2 xpos 0.34 yanchor 0.2
                                pause 1.0
                                block:
                                    ease 0.2 xpos 0.335
                                    pause 0.5
                                    ease 0.2 xpos 0.345
                                    repeat
                            "Her lips wrap around the head of his cock and she began to move"
                            pause 2.0
                            stevie "Woaw mom, your lips feel so good on my cock.."
                            pause 2.0
                            stevie "Ohh... MOM.. it's awesome.."
                            pause 2.0
                            stevie "I'M CUMMING!.."
                            "The mom suck her son cock until the last drop get out"
                            hide carla
                            show stevie:
                                ease 1.0 yanchor 1.0
                            pause 1.0
                            show carla a_0 at center
                            pause 1.0
                            stevie "It was awesome mom.."
                            show carla a_1 blush
                            carla "Thanks honey!"
                            show carla a_0 blush
                            pause 1.0
                            stevie "Mom you can be as casual for now, i will sleep in your bed a little.. when i get up i'll call you for another session"
                            show carla a_1 blush
                            carla "Sure honey!"
                            show carla a_0 blush
                            pause 1.0
                            outfit carla casual
                            "She dress herself.."
                            hide carla with moveoutleft
                            "..and leave the room"
                            pause 1.0
                            stevie "I don't know what is going on with her but i prefer her like this ahah"
                            show stevie:
                                ease 1.0 yanchor 0.0
                            "As he say that, he go sleep on his mother bed"
                            hide stevie
                            menu:
                                "What should i do next?"

                                "Make him possess his mom while he is sleeping":
                                    routename "Family mess son possess"
                                    "I want to see what he'll do in his mother body.. i press the button on him"
                                    show stevieGhost a_6 at centerleft
                                    with dissolve
                                    "Ok i have his spirit.. he is sleeping.. go see the mother"
                                    hide kiyoshiGhost with moveoutleft
                                    hide stevieGhost with moveoutleft
                                    scene black
                                    with dissolve
                                    scene bg michelle livingroom day
                                    outfit carla casual
                                    show carla b_5 at centerright
                                    show kiyoshiGhost a_1 at left, faceright with easeinleft
                                    show stevieGhost a_6 at center, faceright with easeinleft
                                    "The mother is cleaning the livingroom.. it's time for the possess.."
                                    possess stevie carla b_3
                                    stevie "..ehh.."
                                    "He look desoriented"
                                    show stevie a_3
                                    stevie "What the fuck is going on... my head.."
                                    show stevie a_4
                                    pause 0.5
                                    "As he look at him, he see boobs on his chest"
                                    stevie "Woaw.. i have breast"
                                    show stevie a_3
                                    "He start massage them.. making some noise with his mother voice"
                                    pause 1.0
                                    show stevie a_4
                                    "After some seconds, he see his reflect on a mirror"
                                    stevie "Mom? What ar.."
                                    show stevie a_4 blush
                                    "As he say the reflection mimic his move, he understand that he is in his mother body"
                                    pause 1.0
                                    show stevie b_1 blush
                                    stevie "AWESOME! I'm mom!"
                                    show stevie b_0 blush
                                    stevie "I think i can have a lot of fun like this.."
                                    "He look at his reflection whith a big grin"
                                    pause 1.0
                                    show stevie a_0 blush
                                    stevie "let's go out, i want to show my new body to my friends, i think they will love it"
                                    hide stevie with moveoutleft
                                    "As he say that he run out of the house.."
                                    menu:
                                        "What should i do now?"

                                        "Look who is in the bedroom, with the girly door":
                                            routename "Family_mess_sis_solo"
                                            hide kiyoshiGhost with moveoutleft
                                            scene black
                                            with dissolve
                                            scene bg katrina bedroom day
                                            outfit michelle casual_b
                                            show michelle b_4 at center
                                            show kiyoshiGhost a_1 at centerleft, faceright with easeinleft
                                            "ohhhhh yesss... a sister, i must possess her!"
                                            possess kiyoshi michelle b_5 blush
                                            kiyoshi "..ah.."
                                            show kiyoshi b_0 blush
                                            pause 0.5
                                            show kiyoshi b_1 blush
                                            kiyoshi "I'M HER"
                                            show kiyoshi b_7 blush
                                            "I said in her sexy voice as i massage her breast, good size and firm"
                                            pause 1.0
                                            show kiyoshi b_0 blush
                                            kiyoshi "Hey sexy.. what do you have under these clothes"
                                            "I said in her sexy voice as i look at myself in the mirror"
                                            outfit kiyoshi swimsuit
                                            kiyoshi "MY body is so beautiful.."
                                            pause 0.5
                                            outfit kiyoshi nude
                                            "As i strip, i take care to caress all my body with my news little soft hands.."
                                            show kiyoshi a_0 blush

                                            jump Fun_as_a_girl

                                        "Follow him":
                                            routename "Family mess mothers"
                                            "I follow him, again as a ghost"
                                            hide kiyoshiGhost with moveoutleft
                                            scene black
                                            with dissolve
                                            scene bg kiyoshi livingroom day
                                            outfit sandra casual
                                            show sandra a_3 at centerright
                                            show stevie a_0 blush at center, faceright with easeinleft
                                            show kiyoshiGhost a_1 at left, faceright with easeinleft
                                            "As we arrive, stevie in his mom confront his friend mom"
                                            show stevie a_2
                                            stevie "Hi Miss Sa.. eh.. i mean Sandra.."
                                            show sandra a_1
                                            sandra "oh Carla, it was a long time you came here, How are you?"
                                            show sandra a_0
                                            pause 1.0
                                            show stevie a_2
                                            stevie "I'm nice... can i see Pau.. I mean your son?! I have something for him from my son.."
                                            show sandra a_5
                                            sandra "eh... ok.. i think he is upstair, should i make some coffe.."
                                            hide stevie with moveoutright
                                            "She didn't have the time to finish her sentence.. stevie run upstair"
                                            show sandra a_5
                                            "Miss Sandra return to her cleaning.. And i follow him"
                                            hide kiyoshiGhost with moveoutright
                                            scene black
                                            with dissolve
                                            scene bg leona room day
                                            show paul a_3 at centerright
                                            "His friend is in his room, certainly bored as the look on his face.."
                                            show stevie b_1 blush at center, faceleft with easeinleft
                                            show kiyoshiGhost a_1 at left, faceright with easeinleft
                                            show paul a_1
                                            stevie "DUDE! DUDE! It's me stevie, i don't know how but i had possessed my mother"
                                            show stevie b_0 blush
                                            "His friend look at him quizzikaly.."
                                            paul "Hi Miss Carla.. What are you talking about?.. and if it's true, i need a proof.. like showing me your breast maybe.. eheh"
                                            pause 1.0
                                            show stevie b_0 blush
                                            stevie "alright dude.."
                                            show paul a_4
                                            show stevie b_8 blush
                                            outfit stevie nude
                                            pause 1.0
                                            stevie "Is it a good proof to you?"
                                            show paul a_1
                                            paul "OOHHHhh yes dude! You don't know how many times i dream to look at these nipples.. how is it possible?"
                                            show stevie a_0 blush
                                            pause 1.0
                                            stevie "I don't know, this morning we were walking to a market to buy a gift to my dad, when a beam hit my mother, after that she became my sexslave.. sometimes after i went to sleep, after that i get up in my mom body.. that's all i know.."
                                            pause 1.0
                                            paul "AWESOME dude! I can sell all i have to have the same experience that you.."
                                            "When he say that, an idea come to my mind.."

                                            jump Fun_with_moms

                                "Look who is in the next room, with the girly door":
                                    routename "Family mess sis solo"
                                    hide kiyoshiGhost with moveoutleft
                                    scene black
                                    with dissolve
                                    scene bg katrina bedroom day
                                    outfit michelle casual_b
                                    show michelle b_4 at center
                                    show kiyoshiGhost a_1 at centerleft, faceright with easeinleft
                                    "ohhhhh yesss... a sister, i must possess her!"
                                    possess kiyoshi michelle b_5 blush
                                    kiyoshi "..ah.."
                                    show kiyoshi b_0 blush
                                    pause 0.5
                                    show kiyoshi b_1 blush
                                    kiyoshi "I'M HER"
                                    show kiyoshi b_7 blush
                                    "I said in her sexy voice as i massage her breast, good size and firm"
                                    pause 1.0
                                    show kiyoshi b_0 blush
                                    kiyoshi "Hey sexy.. what do you have under these clothes"
                                    "I said in her sexy voice as i look at myself in the mirror"
                                    outfit kiyoshi swimsuit
                                    kiyoshi "MY body is so beautiful.."
                                    pause 0.5
                                    outfit kiyoshi nude
                                    "As i strip, i take care to caress all my body with my news little soft hands.."
                                    show kiyoshi a_0 blush

                                    jump Fun_as_a_girl

                "{s}Go brainwash someone else{/s}":
                    routename "More MC path"
                    placeholder

        "Morph":
            routename "Morph path"
            "I want to morph into my neighbor, scarlet"
            morph begin alien kiyoshi scarlet nude a_4 blush
            kiyoshi "the feeling is strange..."
            morph do
            kiyoshi "i feel my boobs grow... it's fantastic!"
            morph end
            kiyoshi "What a feeling..."
            show kiyoshi a_0 blush
            pause 1.0
            show kiyoshi a_1 blush
            kiyoshi "I'm beautiful"
            show kiyoshi a_0 blush
            menu:
                "What should i do now?"

                "{s}Go confront the real scarlet like this{/s}":
                    placeholder

                "{s}Have fun with her body{/s}":
                    placeholder

        "Body swap":
            routename "Body swap path"
            "I think mess with people should be fun, let's go!"
            hide kiyoshi with moveoutleft
            scene black
            with dissolve
            scene bg abby kitchen
            "As i search for some victims, i see a maid entering a big house, certainly to a rich family.. i decide to go in"
            outfit elizabeth maid
            outfit cornelia pajamas
            show cornelia a_1 at center
            show elizabeth a_0 at left
            "I hide myself behind a window and look at the scene"
            cornelia "Hi Elizabeth! You are late, it's three oclock!"
            elizabeth "Excuse me Cornelia.."
            show cornelia a_3
            cornelia "Are you calling me Cornelia?! YOU MUST CALL ME MISTRESS! I'm not your friend!"
            show elizabeth a_7
            elizabeth "Excuse me mistress.."
            show cornelia a_1
            "Let's the swap happening.. i press the button.."
            swap elizabeth a_8 : a_4, cornelia a_7 : a_3
            pause 1.0
            cornelia "WHAT DID YOU DO TO US?!"
            show elizabeth a_5
            "The maid look at herself..."
            show elizabeth b_1
            elizabeth "I think i'm now the rich daughter eheh.. and YOU are the MAID! What a great turn of situation!"
            cornelia "Th..This can't b.. be real.."
            "As she say that, a man come in, certainly the dad"
            show greg a_1 at centerright, faceleft with easeinright
            show cornelia a_1
            show elizabeth b_8
            greg "What is going on? I heard cry.. are you two alright?"
            cornelia "NOOO dad.. this little shit stole my bod.."
            show greg a_2
            show cornelia a_3
            greg "LITTLE SHIT! Are you speacking of my little girl?!"
            show elizabeth b_2
            cornelia "Wait!.. NO.. I'm.."
            show greg a_6
            greg "I DON't WANT TO HEARD MORE! Elizabeth you are fired! Get out of my house"
            cornelia "Wait!.. Say him Elisabeth!"
            show elizabeth b_1
            "Elizabeth look at her with a mischievous grin"
            show cornelia a_9
            cornelia "I think i don't have the choice... Ahhhhhhh..."
            "She start crying as she leave"
            hide cornelia with moveoutright
            menu:
                "Who should i follow?"

                "The new maid":
                    scene black
                    with dissolve
                    scene bg main house day
                    show cornelia a_9 at center, faceright with easeinleft
                    cornelia "snif..  How could she stole my life like this?!..."
                    show cornelia a_7
                    cornelia "And what should i do now? I don't know a little thing on Elizabeth life... now my life!"
                    show cornelia a_9
                    "As she say that she continue to cry... and i decide to show"
                    show kiyoshi a_1 at centerright, faceleft with easeinright
                    show cornelia a_3
                    kiyoshi "Hi!"
                    show cornelia a_4
                    cornelia "What do you want?"
                    menu:
                        "Show her the remote":
                            kiyoshi "It's not in my habit but i feel guilty about your situation.."
                            show cornelia a_3
                            kiyoshi "This situation is because of me... and this little remote"
                            "I decide to show her the remote.. I think she believe me.. after all she is in her maid's body.."
                            show cornelia b_0
                            show kiyoshi a_5
                            "She start to smile and in no time she press one button!"
                            menu:
                                "What button she have pressed?"

                                "Body swap":
                                    swap cornelia b_2 : a_1, kiyoshi a_5 : a_3
                                    kiyoshi "What have you done?!"
                                    "I start to panic, the remote is in my hand... now HER hand!"
                                    show cornelia a_6
                                    cornelia "So it's true! I have now a remote that can swap body! and what are those insciptions on it?..."
                                    "She examine the remote and understand that it can do more than just body swap.. I'm too afraid to move.. i feel too weak in this body.."
                                    cornelia "Let's try this one!"
                                    show expression alien_particles(400, 200, 220, mind_scale) as particles:
                                        xpos placement_of(kiyoshi).xpos + 0.0000
                                        ypos 0.30
                                        alien_particles_fadeinout(0.75)
                                    scene black
                                    with dissolve
                                    "And i black out..."
                                    pause 2.0
                                    scene bg main room day
                                    with dissolve
                                    "When i wake up, i'm in my bedroom...  maybe all of this is just a dream?...  a remote control! What an imagination.."
                                    "I decide to stand up when..."
                                    outfit kiyoshi maid_topless
                                    show kiyoshi a_3 at center
                                    kiyoshi "BOOBS! What the... it was not a dream.. so this girl really stole the remote form me!.. I must go in the living so my harem will help me!"
                                    hide kiyoshi with moveoutleft
                                    scene black
                                    with dissolve
                                    scene bg main livingroom day
                                    outfit connie sweater
                                    show connie a_0 at centerright, faceleft
                                    "As i enter, i see my mom in the livingroom.. she is alone.."
                                    show kiyoshi a_3 at centerleft, faceright with easeinleft
                                    kiyoshi "MOM MOM I need your help! This girl stole my body and now i'm a maid! You must help me!"
                                    show connie a_2
                                    connie "The master say that you are our new maid and i must order you.. so go clean the house before i call him!"
                                    "As she say that i want to cry.. but my body doesn't respond to my command!"
                                    show kiyoshi a_2
                                    kiyoshi "Yes mistress Connie!"
                                    show kiyoshi a_0
                                    pause 1.0
                                    show connie a_1
                                    connie "So let's go! the house doesn't clean itself ahah"
                                    show connie a_0
                                    hide connie with moveoutright
                                    "As she leave, the control of my body return to me!"
                                    show kiyoshi a_3
                                    kiyoshi "What did she done with me! Did she take control of my harem?! Ohhh nooo wait! The harem is own by me.. my body! and now she have my body and so the harem.. i need to go back to my body fast!"
                                    hide kiyoshi with moveoutright
                                    scene black
                                    with dissolve
                                    scene bg neighborhood day
                                    outfit flavia casual
                                    outfit cornelia casual_b
                                    outfit allison casual
                                    show cornelia a_6 at center
                                    show flavia a_9 blush at centerleft
                                    show allison b_1 blush at centerright
                                    show allison:
                                        faceleft
                                    pause 1.0
                                    cornelia "Come on! Suck me off!"
                                    show allison a_1 blush
                                    show flavia a_2 blush
                                    allison "I'm your!"
                                    flavia "As you wish bro!"
                                    show allison b_7 blush
                                    show flavia a_9 blush
                                    show cornelia:
                                        ease 1.0 yanchor 0.8
                                    show allison:
                                        ease 1.2 xpos 0.58 yanchor 0.225
                                        block:
                                            ease 0.2 xpos 0.545
                                            pause 0.5
                                            ease 0.2 xpos 0.535
                                            repeat
                                    show flavia:
                                        ease 1.2 xpos 0.42 yanchor 0.215
                                        block:
                                            ease 0.2 xpos 0.480 yanchor 0.220
                                            pause 0.5
                                            ease 0.2 xpos 0.485 yanchor 0.215
                                            repeat
                                    show cornelia a_2
                                    pause 0.5
                                    show kiyoshi a_3 at left, faceright with easeinleft
                                    "I'm in panic when i look at that scene! My sister is licking my balls and Aliison suck my dick"
                                    "She stole my body.. my harem.. and now she is making fun with them.. in MY BODY! It's too much"
                                    placeholder

                                "{s}Possession{/s}":
                                    placeholder

                                "{s}Mind control{/s}":
                                    placeholder

                                "{s}Morph{/s}":
                                    placeholder

                        "{s}Make her your slave{/s}":
                            placeholder

                "{s}The new daughter and his rich father{/s}":
                    placeholder

label Fun_as_a_girl:
    kiyoshi "It could be fun to see the world as a girl"
    menu:
        "But how to dress up?"

        "Don't dress up, go out like this":
            routename "Girl power naked"
            kiyoshi "I want to go out like this, watch people face while they'll looking at me ahah"
            hide kiyoshi with moveoutleft
            scene black
            with dissolve
            scene bg school garden day
            outfit jess rags
            show jess b_0 at centerright
            show kiyoshi a_0 blush at left, faceright with easeinleft
            "As i walk along the street, i see a little girl, she breack my heart.. she is homeless, i think i can do something for her.. And i press the button"
            swap kiyoshi a_0 : b_3, jess b_2 : a_5
            jess "What is goi..."
            show jess a_4
            jess "Jesus!"
            show kiyoshi a_3 blush
            "She look at her naked body, and she see me in her old body"
            show jess:
                ease 2.0 xpos 0.5
            show jess a_2
            "She walk slowly in my direction"
            kiyoshi "Hi, i see you are a homeless little girl, i want to give you a better life.. so go at the house down the street, it's your new home!"
            pause 0.5
            show jess a_8 blush
            pause 0.5
            show jess b_1 blush
            jess "Really? It's a dream come true.. i should ask you why i am naked but i don't care! I have a new life!"
            show jess b_0 blush
            hide jess with moveoutleft
            "As she say that she run at her new home.. for a new life"
            "Some passerby look at her, wonder why a beautiful girl like her expose herself on the street, jumping anywhere and making bounce her naked breast.."
            pause 1.0
            outfit katrina maid
            show katrina a_3 at right, faceleft with easeinright
            show kiyoshi b_15
            "As i see her dissappear in her new home.. i feel an hand touch my arm.."
            show kiyoshi b_16
            "I think she have a big sister.."
            show kiyoshi b_17
            "nice body for a homeless girl ahah"
            katrina "Are you alright?! I see that naked girl speack to you and run off some seconds after.. Did she stole you something?!.. I come as fast as i can!"
            "I reassure her.."
            show kiyoshi a_3
            kiyoshi "I'm alright.. SIS!"
            show katrina a_6
            pause 1.0
            show kiyoshi a_5
            katrina "Alright.. You know you are the only thing i have, i don't want to lost you sister.."
            "As she say that, she give me a nice hug.. i fell her soft body against mine, if i wasn't a little girl i'll be aroused.. and there is a solution to not be a little girl.. ahah"
            swap kiyoshi a_5 : a_1, katrina a_6 : a_20
            pause 2.0
            hide kiyoshi with moveoutleft
            "After the swap, i run as fast as i could, i give her about 10 years of life, it's a nice gift, now i should explore that new body.."
            show katrina a_20
            katrina "EH come back.."
            hide katrina with moveoutleft
            "She start to run after me but i run faster than a little girl, i think i should go at my house for now"
            scene black
            with dissolve
            scene bg main livingroom day
            show allison a_0 at center, faceleft
            show sayaka a_1 at centerleft, faceleft
            show connie a_0 blush at centerright, faceleft
            show flavia a_1 blush at right, faceleft
            show kiyoshi a_0 at left, faceright with easeinleft
            "As i enter, i see my harem in the livingroom"
            show kiyoshi a_1 blush
            kiyoshi "Hey girls! do you like my new body?"
            pause 1.0
            show allison a_1 blush
            show sayaka a_2 blush
            show connie a_1 blush
            show flavia a_2 blush
            sayaka "Your are beautiful lover!"
            connie "Yes Honney!"
            allison "I love it!"
            flavia "Yeah bro!"
            pause 1.0
            show allison a_0 blush
            show connie a_0 blush
            show sayaka a_1 blush
            show flavia a_1 blush
            show kiyoshi a_0 blush
            kiyoshi "Nice to hear! i go to my bedroom, Allison come with me, we will have some fun"
            show allison a_1 blush
            allison "YI follow you!"
            pause 0.5
            show allison a_0 blush
            hide kiyoshi with moveoutright
            hide allison with moveoutright
            scene black
            with dissolve
            scene bg main room day
            show kiyoshi a_0 at left, faceright with easeinleft
            show allison a_0 at center, faceleft with easeinleft
            "As we entering the room, I strip to see my new body"
            outfit kiyoshi nude
            show kiyoshi b_0 blush
            pause 1.0
            show kiyoshi b_1 blush
            kiyoshi "Her body is soooooo niccccceeee.... so soft.."
            "I say as i caress my new skin"
            show kiyoshi a_1 blush
            "I start carressing my boobs and pinch my nipples... this feeling is awesome.."
            pause 0.5
            show kiyoshi a_1 blush
            kiyoshi "What should i do with Allison?"
            show kiyoshi a_0 blush
            menu:
                "{s}Stay the homeless girl{/s}":
                    placeholder

                "Allison have something to say":
                    jump Allison_school_queen

                "{s}Morph allison in the homeless girl, to have fun as twins{/s}":
                    placeholder

        "{s}Just underwear{/s}":
            routename "Girl power underwear"
            placeholder

        "Dress the clothes i had stripped":
            routename "Girl power casual"
            kiyoshi "I should dress up, i want people thinking i'm the real Michelle ahah"
            show kiyoshi b_0
            outfit kiyoshi casual_b
            kiyoshi "Perfect! Now let's go have some fun as a girl ahah"
            hide kiyoshi with moveoutleft
            scene black
            with dissolve
            scene bg mall outside day
            show kiyoshi b_0 at left, faceright with easeinright
            kiyoshi "It's a nice day for shopping!"
            "I say with my new sexy voice"
            hide kiyoshi with moveoutleft
            scene black
            with dissolve
            scene bg mall interior 1
            show kiyoshi b_0 at left, faceright with easeinright
            kiyoshi "Time for girly fun!"
            menu:
                "What should i do?"

                "Go try some clothes":
                    routename "Girl power shopping"
                    kiyoshi "Here we go.."
                    hide kiyoshi with moveoutleft
                    scene black
                    with dissolve
                    scene bg mall shop
                    show kiyoshi b_0 at center, faceleft with easeinleft
                    kiyoshi "How should i dress?"
                    menu:
                        "{s}try a traditional japanese outfit{/s}":
                            placeholder

                        "{s}try a wedding dress{/s}":
                            placeholder

                        "{s}try a winter outfit{/s}":
                            placeholder

                        "try a casual dress":
                            "I want to try the casual dress"
                            outfit kiyoshi swimsuit
                            "I remove my clothes, and put the new outfit on my soft skin"
                            show kiyoshi a_0
                            outfit kiyoshi casual
                            "As i finish to put the dress, i heard someone come to me"
                            outfit rileyGB swimsuit
                            show rileyGB a_1 at centerleft, faceright with easeinleft
                            show kiyoshi a_3
                            rileyGB "Woaw! it look so beautiful on you!"
                            show rileyGB a_0
                            show kiyoshi a_0 blush
                            "This girl in bikini is so hot..."
                            rileyGB "By the way, i'm Pauline! who are you?"
                            "I look at the beautiful girl in front of me.. her eyes are beautiful.. what should i answer her?"
                            menu:
                                "I'm you!":
                                    "I want to know what it's like to see thought her big eyes, so i swap with her"
                                    swap kiyoshi a_0 : a_5, rileyGB a_3 : a_4
                                    "As i gain my sense, i look at her and run away of the shop.."
                                    hide kiyoshi with moveoutleft
                                    scene black
                                    with dissolve
                                    scene bg mall inside day
                                    show kiyoshi a_0 at center, faceleft with easeinright
                                    "As i run i look at my new body.. certainly one of the beautiful i have never see! And now it's me! thanks to that little remote!"
                                    show kiyoshi b_2 blush
                                    "I press my boobs together.. so sensitive.."
                                    show kiyoshi b_0 blush
                                    kiyoshi "this body is awesome!.. and i look so cute.."
                                    show kiyoshi a_0 blush
                                    "Sexy as i'm i could be a cheerleader... thinking of that, let's see what happened to Tori and Vanessa and have a little fun"
                                    hide kiyoshi with moveoutleft
                                    scene black
                                    with dissolve
                                    scene bg school pool day
                                    outfit tori nude
                                    outfit vanessa nude
                                    show tori b_1 blush at centerright
                                    show tori:
                                        faceleft
                                    show vanessa a_3 blush at center
                                    show kiyoshi a_0 at centerleft, faceright with easeinleft
                                    kiyoshi "Hi girls!"
                                    show tori b_2 blush
                                    vanessa "hi!"
                                    tori "hello!"
                                    show tori b_3 blush
                                    "End for now"
                                    placeholder

                                "{s}I'm Michelle!{/s}":
                                    placeholder

                        "{s}Just remove my clothes{/s}":
                            placeholder

                "{s}Go mess with some people{/s}":
                    placeholder

label Fun_with_moms:
    menu:
        "What should i do?"

        "Let Paul possess his mother":
            "I will let Paul have the same experience"
            show stevie a_4
            exspirit paul a_6
            "I send him directly in his mother body"
            hide paulGhost with moveoutleft
            scene black
            with dissolve
            scene bg kiyoshi livingroom day
            outfit sandra casual
            show sandra a_3 at centerright
            show paulGhost a_6 at center, faceright with easeinleft
            possess paul sandra a_6 blush
            "And Paul possess his mother"
            pause 1.0
            show paul a_7
            paul "What is going on? Wai..Wait a minute.."
            "he said as he look at his body"
            pause 1.0
            show paul a_1
            paul "OHMYGOD i'm my mother, i should go see Stevie"
            hide paul with moveoutright
            scene black
            with dissolve
            scene bg leona room day
            show stevie a_4 at center
            show kiyoshiGhost a_1 at left
            "Stevie is looking at his friend's lifeless body.. with panic..when his firend mother come in"
            show paul a_1 blush at centerright, faceright with easeinleft
            show stevie a_7 blush
            paul "DUDE! It's me Paul, i had possessed my mother too! This will be so fun"
            show stevie a_1 blush
            pause 1.0
            paul "I want to see my mom pussy for too long time.."
            outfit paul nude
            "As he say that, he strip"
            paul "So nice and so soft... like a dream come true!"
            pause 2.0
            show stevie a_0 blush
            show paul a_0 blush
            "They are touching their own bodies when suddenly they stop and look at each others"
            pause 1.0
            show stevie a_1 blush
            show paul a_1 blush
            stevie "Ok dude.. let's FUCK!"
            paul "OHhhhh this will be so fun ahah"
            show stevie a_0 blush
            show paul a_0 blush
            "They said with their mothers voice"
            pause 1.0
            menu:
                "I want to join the fun.. but how?"

                "Go possess my own mom and come back":
                    "Let's go possess my mom to have fun"
                    hide kiyoshiGhost with moveoutleft
                    scene black
                    with dissolve
                    scene bg main livingroom day
                    show allison a_0 at center, faceleft
                    show sayaka a_1 at centerleft, faceleft
                    show connie a_0 blush at centerright, faceleft
                    show flavia a_1 blush at right, faceleft
                    show kiyoshiGhost a_1 at left, faceright with easeinleft
                    "Sorry mom but i need your body!"
                    possess kiyoshi connie a_4 blush
                    "And i possess her"
                    pause 1.0
                    show kiyoshi a_8
                    kiyoshi "Possess someone is awesome.."
                    pause 1.0
                    outfit kiyoshi casual_b
                    "I dress with some clothes and i run to the two Mothers"
                    hide kiyoshi with moveoutright
                    scene black
                    with dissolve
                    scene bg leona room day
                    show stevie a_1 blush at center
                    show paul a_8 blush at centerright
                    "Stevie and his friend just started to have fun, i'm not too late.."
                    show kiyoshi b_1 blush at left, faceright with easeinleft
                    show stevie a_7 blush
                    show paul a_2 blush
                    stevie "What th.. Miss Connie? What are you doing here?!"
                    show kiyoshi a_1 blush
                    kiyoshi "I'm here to have FUN!"
                    show kiyoshi a_0 blush
                    show stevie b_1 blush
                    show paul a_8 blush
                    "As i say that, i start undress"
                    outfit kiyoshi underwear
                    "I remove my clothes.. they look at me with desire.."
                    outfit kiyoshi nude
                    pause 1.0
                    show kiyoshi a_1 blush
                    kiyoshi "So girls.. how we should start?"
                    show kiyoshi a_0 blush
                    show stevie b_0 blush
                    show paul a_0 blush
                    stevie "Oh mannn.. it's a dream come true.. a threesome lesbian as my mom!"
                    show paul a_8 blush
                    show kiyoshi b_7 blush
                    show stevie b_4 blush
                    show paul:
                        ease 1.2 xpos 0.65
                    show kiyoshi:
                        ease 2.0 xpos 0.35
                    "As he say that, we bring closer to each others and start to kiss and lick our boring lips and faces"
                    stevie "MMhhh.."
                    paul "So soft... so niccceee..."
                    kiyoshi "Ohhh yesss.. lick my tongue.."
                    "We say with our mothers voices"
                    placeholder

                "Go possess someone on the street and come back":
                    "Let's go possess someone to have fun"
                    hide kiyoshiGhost with moveoutleft
                    scene black
                    with dissolve
                    scene bg neighborhood day
                    outfit setsuna casual
                    show setsuna b_0 at center, faceleft
                    show kiyoshiGhost a_1 at left, faceright with easeinleft
                    "I think this girl will do it"
                    possess kiyoshi setsuna b_7 blush
                    "And i possess her"
                    pause 1.0
                    show kiyoshi a_2 blush
                    kiyoshi "Possess someone is awesome.."
                    pause 1.0
                    "Let's go, i run to the two Mothers"
                    hide kiyoshi with moveoutright
                    scene black
                    with dissolve
                    scene bg leona room day
                    show stevie a_1 blush at center
                    show paul a_8 blush at centerright
                    "Stevie and his friend just started to have fun, i'm not too late.."
                    show kiyoshi b_1 blush at left, faceright with easeinleft
                    show stevie a_7 blush
                    show paul a_2 blush
                    stevie "What th.. Setsuna..?"
                    paul "Who is she?!"
                    stevie "I know her from school.. but.. What are you doing here?!"
                    show kiyoshi b_2 blush
                    kiyoshi "I'm here to have FUN!"
                    show kiyoshi b_1 blush
                    show stevie b_1 blush
                    show paul a_8 blush
                    "As i say that, i start undress"
                    outfit kiyoshi swimsuit
                    "I remove my clothes, it look like i have a swimsuit under my clothes.. maybe she was on the way to the pool.. as i think that, they look at me with desire.."
                    outfit kiyoshi nude
                    pause 1.0
                    show kiyoshi a_2 blush
                    kiyoshi "So girls.. how we should start?"
                    show kiyoshi a_1 blush
                    show stevie b_0 blush
                    show paul a_0 blush
                    stevie "Oh mannn.. it's a dream come true.. a threesome lesbian as my mom!"
                    show paul a_8 blush
                    show kiyoshi b_1 blush
                    show stevie b_4 blush
                    show paul:
                        ease 1.2 xpos 0.65
                    show kiyoshi:
                        ease 2.0 xpos 0.35
                    "As he say that, we bring closer to each others and start to kiss and lick our boring lips and faces"
                    stevie "MMhhh.."
                    paul "So soft... so niccceee..."
                    kiyoshi "Ohhh yesss.. lick my tongue.."
                    "We say with our female voices"
                    placeholder

        "{s}Let Paul control his mother{/s}":
            placeholder

        "{s}Possess his mother and come here{/s}":
            placeholder

label Allison_school_queen:
    routename "Allison lover"
    allison "Lover! I want to give you my body as a gift... and i'll accept the life of poverty that come with your actual body.."
    show kiyoshi a_3
    "I'm chocked at first.. but it's logic.. as my lover she doesn't like to see me as a homeless girl, so she want to offer her body to me.."
    show kiyoshi a_5
    kiyoshi "If is it what you want allison.. i think i can do it"
    show allison a_8 blush
    "Nice! I'm ready.. make your thing and swap us"
    swap kiyoshi a_5 : a_1, allison a_5 : a_8
    pause 1.0
    show allison a_5 blush
    pause 1.0
    show kiyoshi b_0 blush
    kiyoshi "Your body feel so good Allison! Thanks to give it to me"
    show kiyoshi b_1 blush
    show allison a_1 blush
    allison "Thanks to you lover! I love you more than anything in the world!"
    show allison a_0 blush
    "YES! Thanks to the brainwash"
    kiyoshi "Allison i think we should dress up, and live our new life"
    show allison a_1 blush
    allison "Yes lover!"
    show allison a_0 blush
    "As she give me her.. now mine clothes, we start to dress.. my body is so sensitive.. just dress make my body hot"
    show allison a_0 blush
    outfit allison maid
    show kiyoshi a_6 blush
    outfit kiyoshi underwear
    pause 2.0
    show kiyoshi a_0 blush
    outfit kiyoshi uniform
    allison "I think i'm trapped on the street now.. but it's to prove my love for you!.. so it doesn't matter"
    allison "I'm already starting to miss my boobs.. but i'm glab they are on YOUR chest.. lover!"
    allison "Bye lover! And don't forget to see me sometimes!"
    hide allison with moveoutleft
    "As she say that, she leave the house and go to her new life as an homeless girl..."
    pause 1.0
    show kiyoshi a_6 blush
    "I look at my new impresive breast.. as i touch my nipples my body feel so good..."
    pause 1.0
    show kiyoshi a_9 blush
    kiyoshi "I want more! I want to find how good the female orgasm could be!.. I think i can go to school for that.. and be the new queen's school ahah"
    pause 1.0
    show kiyoshi a_0 blush
    hide kiyoshi with moveoutleft
    scene black
    with dissolve
    scene bg school entrance day
    show kiyoshi a_0 blush at left, faceright with easeinleft
    menu:
        "Who should i take to help me feel the best female orgasm?"

        "The teachers":
            kiyoshi "I think older women have more experience.. Let's go see the teachers!"
            scene black
            with dissolve
            scene bg classroom 3 day
            outfit abby nude
            outfit Harem_catherine nude
            outfit leona nude
            outfit yuuna nude
            show abby a_1 blush at center, faceleft
            show leona a_1 blush at centerright, faceleft
            show yuuna a_0 at right, faceleft
            show Harem_catherine a_0 blush at centerleft, faceleft
            pause 1.0
            show kiyoshi a_1 at left, faceright with easeinleft
            kiyoshi "Hi all! How are you?"
            show kiyoshi a_0
            show leona a_4 blush
            show yuuna a_2 blush
            show abby a_2 blush
            show Harem_catherine a_1 blush
            yuuna "Fine lover!"
            leona "I'm alright!"
            Harem_catherine "Fine!"
            abby "In heaven!"
            show leona a_1 blush
            show yuuna a_0 blush
            show Harem_catherine a_0 blush
            show abby a_1 blush
            pause 0.5
            kiyoshi "Nice to hear that! I need your help to help me discover my new body.. so let's start"
            "End for now"
            placeholder

        "{s}The cheerleaders at the gym{/s}":
            placeholder

        "{s}Tori and Vanessa at the pool{/s}":
            placeholder

        "{s}Someone new{/s}":
            placeholder

label Remote_error:
    routename "Remote error"
    show kiyoshi a_3
    "I press she start to vibrate in my hands"
    show sayaka a_3
    sayaka "Which part of {i}FUCK OFF{/i} do you not understand?"
    show sayaka a_5
    pause 0.5
    with hpunch
    show white as white_flash:
        additive_flash(0.5)
    show kiyoshi a_5
    "Suddenly the remote crack in my hand and make an huge beam, i start to panick"
    show sayaka a_6
    show allison a_2
    allison "What are you doing with that thing?"
    show white as white_flash:
        additive_flash(0.4)
    "As she finish her sentence, the remote breaks in pieces in my hand and releases a shock wave with another beam"
    show white as white_flash:
        additive_flash(0.4)
    show sayaka a_8
    show allison a_4
    "I feel like i'm sucked out from my body!"
    show white as white_flash:
        additive_flash(0.4)
    show sayaka a_4
    show allison a_8
    show kiyoshi a_0
    show kiyoshiGhost a_5 at centerleft
    show allisonGhost a_5 at right, faceleft
    show sayakaGhost a_7 at centerright
    "I look at Sayaka and Allison and i see They are in a ghost shape like me and our bodies are standing lifeless!"
    "I look around me and see that others students and teachers are like us"
    allisonGhost "What is going on! Ahhhh.."
    hide allisonGhost with moveoutright
    show sayakaGhost a_8
    sayakaGhost "NO! Allison! Come back!"
    show sayakaGhost:
        ease 0.5 xpos 0.8
    clone brad sayaka
    clone yoshinori kiyoshi
    show yoshinori a_0 at centerleft
    show yoshinori behind kiyoshiGhost
    hide kiyoshi
    show brad a_4 at centerright
    possess sayaka allison a_4
    "I look at Sayaka being sucked in Allison body!"
    sayaka "ehh.. my head.."
    show sayaka a_5
    sayaka "WHAT?! Blond hair?..."
    pause 0.2
    sayaka "Did i just possess Allison?"
    "As she say that, she look around her and run at the direction where Allison went"
    hide sayaka with moveoutright
    show kiyoshiGhost a_1
    kiyoshiGhost "Interesting.. So we can possess lifeless bodies in this shape"
    routename "Ghost party"
    timedchoice 5 Mass_Poss_Taking_Over
    menu:
        "What should i do?"

        "Try to possess Sayaka lifeless body":
            routename "Ghost Sayaka"
            kiyoshiGhost "Like Sayaka with Allison, let's see if i can take her body"
            show brad behind kiyoshiGhost
            show kiyoshiGhost:
                ease 1.0 xpos 0.7
            pause 0.5
            kiyoshiGhost "This will be my new body.. Here we go!"
            possess kiyoshi brad a_0
            pause 1.5
            show kiyoshi a_1
            kiyoshi "It worked! I'm Sayaka!"
            "I pause and look at my new body.. so different than being a man"
            pause 1.6
            kiyoshi "I want to explore her body, let's go to the GIRL lockerroom!"
            kiyoshi "I love hearing her voice while i'm speacking.. it's sound sexy.. hihihi!"
            "I make a feminine gasp and walk to the girl lockerroom"
            hide kiyoshi with moveoutright
            scene black
            with dissolve
            scene bg lockerroom day
            body paul cassie
            body john yui
            outfit paul swimsuit
            outfit john nude
            "As i approach the girl locker room, i heard girly cry.. like someone is masturbating here"
            show john a_7 blush at center
            show paul a_7 blush at centerright
            paul "Fuck yes!"
            john "Female orgasm is aweeEEESSSssommmmhhhh..."
            show kiyoshi a_7 blush at left, faceright with easeinleft
            "I look at Cassie and Yui.. There are violating their bodies with their hands! Findering their pussies and massaging violently their breasts!"
            kiyoshi "Cassie?! Yui?! What are you doing here?!"
            "They stop and look at me"
            show john a_0 blush
            show paul a_0 blush
            paul "Eh Sayaka! Do you want to join the fun?"
            "I think at the proposal.. Two of the most beautiful girls at school are masturbating in the lockerroom and ask me to join.."
            "While i'm wondering who possessed these bodies i smile at them and say.."
            show kiyoshi b_1 blush
            show kiyoshi:
                ease 1.5 xpos 0.35
            kiyoshi "Count me in!"
            show john b_5 blush
            show john:
                faceleft
            show paul a_0 blush
            show paul:
                faceleft
            paul "Awesome!"

            "End for now"
            placeholder

        "Go around the school to see if everyone is like us":
            kiyoshiGhost "I wonder How far people have left their bodies"
            menu:
                "Where should i go first?"

                "The teachers room":
                    jump Mass_Poss_Teachers

                "{s}The school's swimming pool{/s}":
                    placeholder

                "The gym hall":
                    jump Mass_Poss_Gym

                "Get out of shool and go to town":
                    hide kiyoshiGhost with moveoutleft
                    scene black
                    with dissolve
                    scene bg school entrance day
                    body marty irene
                    outfit marty casual
                    outfit irene casual
                    outfit ireneGhost casual
                    show marty b_8 at center
                    show ireneGhost a_7 at centerleft
                    show kiyoshiGhost a_1 at right, faceleft with easeinright
                    ireneGhost "NO! Please don't touch my body like that in public!"
                    "While i run out of school, i see a girl near her possessed body, she is in panick and try to talk with her body stoler, but he can't hear her while she is in ghost shape..."
                    "The person in her body is touching himself in a way she certainly never did.. In public!"
                    pause 0.5
                    show marty b_5
                    marty "Fuck yesss..."
                    "the body stoler saying with the girl voice while he start touching her private parts"
                    show ireneGhost:
                        ease 0.5 xpos 0.45
                    ireneGhost "Don't touch me like that your pervert!"
                    pause 0.5
                    show marty b_1
                    marty "I think i should go somewhere more appropriate to explore my new sexy body ahahah!"
                    show marty b_9
                    "it sound very sexy coming from her mouth"
                    hide marty with moveoutright
                    ireneGhost "EH! Come back with my body!"
                    hide ireneGhost with moveoutright
                    pause 0.5
                    "It was very hot but i need to concentrate on me for now and go to town.."
                    menu:
                        "But where in town?"

                        "My home":
                            jump Mass_Poss_Home

                        "The street":
                            jump Mass_Poss_Street

                        "The local Dinner":
                            jump Mass_Poss_Dinner

label Mass_Poss_Taking_Over:
    routename "Ghost taking over"
    connieGhost "Kiyoshi! Kiyoshi! Where are you?"
    "I heard a familiar voice crying my name"
    show kiyoshiGhost:
        faceleft
    show connieGhost b_3 at left, faceright with easeinleft
    connieGhost "Kiyoshi?! Honney!"
    show connieGhost b_1
    connieGhost "Ha! You are here!"
    show kiyoshiGhost a_5
    show connieGhost:
        ease 1.0 xpos 0.3
    show kiyoshiGhost:
        ease 1.0 xpos 0.5
    possess connie yoshinori a_3
    "I watch with horror my mom taking over my body!"

    "End for now"
    placeholder

label Mass_Poss_Teachers:
    routename "Ghost Teachers"
    kiyoshiGhost "I'll check the Teachers room to see if the beam touch people as far"
    hide kiyoshiGhost with moveoutleft
    scene black
    with dissolve
    scene bg school classroom hallway day
    body rika abby
    outfit rika nude
    show rika a_2 at centerright
    show kiyoshiGhost a_1 at left, faceright with easeinleft
    "In my way to the teachers room, i see miss Abby running in the hallway...Nude and feeling herself!"
    rika "Oh my god! This body is so awesome!"
    show rika a_9 blush
    "It look like miss Abby body is taking over by someone! the body thief is feeling her body in front of everyone!"
    show abbyGhost a_7 at right, faceleft with easeinright
    abbyGhost "What are you doing?! Don't touch my body like that your pervert!"
    "She try to talk to the thief but in her ghost shape, he doesn't hear her"
    show rika a_1 blush
    rika "I think i should go to her home.. MY HOME NOW!"
    hide rika with moveoutleft
    abbyGhost "EH! Come back!"
    hide abbyGhost with moveoutleft
    kiyoshiGhost "It look like people start to be possessed.. and some people seem to have fun eheh!"
    hide kiyoshiGhost with moveoutright
    scene black
    with dissolve
    scene bg classroom 1
    outfit yuuna casual
    outfit leona casual
    show yuuna a_4 at center
    show leona a_5 at centerright
    show kiyoshiGhost a_1 at left, faceright with easeinleft
    "Two of my teachers lifeless bodies are standing here whiout their ghosts.."
    "Being a teacher and in a grown female body should be a nice experience ahah!"
    timedchoice 5 Mass_Poss_teachers_principal
    menu:
        "Who should i possess"

        "{s}Miss Yuuna, the hottest teacher at school{/s}":
            routename "Ghost teacher Yuuna"
            placeholder

        "{s}Miss Leona{/s}":
            routename "Ghost teacher Leona"
            placeholder

label Mass_Poss_teachers_principal:
    routename "Ghost teachers principal"
    show jackGhost a_0 at right, faceleft with easeinright
    jackGhost "Ah! You are here Leona! I was thinking you were in this shape too.."
    show jackGhost:
        ease 1.0 xpos 0.75
    possess jack leona a_6
    jack "What?!"

    "End for now"
    placeholder

label Mass_Poss_Gym:
    routename "Ghost Gym"
    kiyoshiGhost "I'll check the gym hall to see if the beam touch people as far"
    hide kiyoshiGhost with moveoutleft
    scene black
    with dissolve
    scene bg school gym day
    outfit cassie casual_d
    outfit yui casual
    show yui a_5 at centerright
    show cassie a_2 at right
    show yuiGhost a_6 at centerright
    show cassieGhost a_3 at right
    show kiyoshiGhost a_1 at left, faceright with easeinleft
    "while I come in, I see cassie and yui standing near their lifeless bodies in their ghost shape and in panick"
    "They are the girls i want to fuck since elemantary school.. and now i can have their bodies ahah!"
    timedchoice 5 Mass_Poss_Gym_perverts
    menu:
        "Who should i possess"

        "{s}Yui the sexy cheerleader{/s}":
            routename "Ghost gym Yui"
            placeholder

        "{s}Cassie my crush and the head cheerleader{/s}":
            routename "Ghost gym Cassie"
            placeholder

label Mass_Poss_Gym_perverts:
    routename "Ghost gym perverts"
    show paulGhost a_2 at right, faceright with easeinright
    show cassieGhost:
        ease 0.7 xpos 0.5
    show johnGhost a_1 at centerright, faceleft with easeinright
    show yuiGhost:
        ease 0.7 xpos 0.3
    possess paul cassie a_7
    possess john yui a_7
    "While i was thinking, two guys run through Cassie et Yui and take over their bodies.. The two girls seem very scared!"
    "The two possessors are know to be the school's virgin perverts... and now they are two of the most beautiful girls in school!"
    show paul a_5 blush
    show john a_0 blush
    paul "Woaw dude it's awesome, i'm really Cassie the head cheerleader! I can make her do anything i want!"
    show paul b_4 blush
    show paul:
        faceleft
    "As he say that, he start feeling his new body, starting with the boobs and the pussy!"
    show paul b_0 blush
    john "Oh yeah dude! This body feel so right!"
    show john b_5 blush
    pause 1.2
    show john b_3 blush
    "John in Yui body start to feel her boobs, he massage them with her soft hands"
    paul "It's the hottest thing i've never did! Let's find somewhere private to have fun with our news bodies!"
    show paul a_0 blush
    show john a_0 blush
    john "Yes dude! I think the GIRL's locker room should do the trick"
    hide john with moveoutleft
    hide paul with moveoutleft
    "As he say that, they run with Cassie and Yui bodies like little girls"
    "The two girls in their ghost shape were too chocked to react"
    pause 1.0
    cassieGhost "OH MY GOD! What should i do now! Ahhhhh..."
    hide cassieGhost with moveoutright
    "Cassie in her ghost shape cry and run away"
    yuiGhost "CASSIE! Come back! We must find a way to recover our bodies!"
    hide yuiGhost with moveoutright

    "End for now"
    placeholder

label Mass_Poss_Street:
    routename "Ghost street"
    kiyoshiGhost "I'll check the street to see if the beam touch people out of the school"
    hide kiyoshiGhost with moveoutleft
    scene black
    with dissolve
    scene bg neighborhood day
    outfit carla casual
    show carla b_5 at centerright
    outfit stevie casual
    show stevie a_0 at centerleft
    show carlaGhost a_4 at right
    show stevieGhost a_5 at centerleft
    show kiyoshiGhost a_1 at left, faceright with easeinright
    "A mom and her son are here, in the same situation as i am, i look at them from a little behind"
    carlaGhost "What is going on?!"
    stevieGhost "I don't know mom!"
    carlaGhost "Stevie come near me, we'll find a solution.. i hope we are not dead.."
    stevieGhost "I hope too"
    show stevieGhost:
        ease 1.0 xpos 0.65
    "The son move as his mother told him but stand in front of her lifeless body"
    stevieGhost "Look mom.. i think i can control your hand!"
    "He say as he slip one hand through her body"
    carlaGhost "STEVIE! Don't touch my body!"
    show stevieGhost a_1
    stevieGhost "Too late mom! eheh.."
    "As he say that, he push himself in her body.."
    show carlaGhost a_7
    $ from char_sprites import sprites
    $ fake_stevie = sprites[("stevie", "a_0")].compose()[2]
    show expression fake_stevie at centerleft
    possess stevie carla b_3
    "The mother's ghost is standing here.. stunning by her son behavior"
    #remake this for the mother to force kiyoshi to be her

    "End for now"
    placeholder

label Mass_Poss_Home:
    routename "Ghost home"
    kiyoshiGhost "I'll check my home to see if the beam touch my mom and sis"
    hide kiyoshiGhost with moveoutleft
    scene black
    with dissolve
    scene bg main livingroom day
    clone anuja connie
    clone laura flavia
    outfit anuja casual
    show anuja a_4 at centerright
    show laura a_5 at center
    show natalieGhost a_3 at center
    show kiyoshiGhost a_1 at left, faceright with easeinleft
    "It look like my mom and my big sister left their bodies.. and my little sis is taking an opportunity"
    natalieGhost "Woaw Flavia! I can enter your body like a suit"
    show natalieGhost a_1
    natalieGhost "it's going to be fun!"
    possess natalie laura a_6
    natalie "mmhhh.."
    "She say with our big sister voice"
    show natalie a_7
    natalie "Am i Flavia?!"
    "She start to look at her body while her hands are carressing her new skin"
    show natalie a_0
    natalie "Woaw Flavia! I have always been jealous of you but now.. I'M YOU!"
    pause 0.5
    show natalie a_1
    natalie "This will be so fun!"
    hide natalie with moveoutleft
    "She certainly run to her bedroom or Flavia's bedroom"
    kiyoshiGhost "I think i should possess someone before everybody is taken"
    menu:
        "But who?"

        "{s}Little sis{/s}":
            placeholder

        "Mom":
            jump Mass_Poss_mom

        "Go see if my sexy neighbor is at her place":
            jump Mass_Poss_neighbor

label Mass_Poss_mom:
    routename "Ghost mom"
    kiyoshiGhost "I think being mom should be fun.. Here we go!"
    possess kiyoshi anuja a_7
    kiyoshi "Mmhh..."
    show kiyoshi a_0
    pause 1.2
    show kiyoshi a_1 blush
    kiyoshi "I'm mom!"
    show kiyoshi a_5 blush

    "End for now"
    placeholder

label Mass_Poss_neighbor:
    routename "Ghost neighbor"
    kiyoshiGhost "I'm thinking at my sexy neighbor.. I must see what she is doing"
    hide kiyoshiGhost with moveoutleft
    scene black
    with dissolve
    scene bg abby bath full
    outfit scarlet nude
    show scarlet a_8 at center
    show scarletGhost a_7 at centerright
    show scarletGhost:
        faceleft
    show kiyoshiGhost a_1 at left, faceright with easeinleft
    "It look like she was taking a bath when the beam hit her"
    show scarletGhost a_5
    scarletGhost "Kiyoshi?! What are you doing here?! I think we are dead.."
    "She look at her naked body"
    show scarletGhost a_2
    scarletGhost "EH! Don't look at my body like that!"
    kiyoshiGhost "Oh Scarlet! I'll do more than just look at it ahah!"
    show scarletGhost a_4
    scarletGhost "What are you talking about?!"
    show kiyoshiGhost:
        ease 1.0 xpos 0.5
    scarletGhost "EH! Don't approach my body your pervert!"
    "I look at her with a mischievous smile and enter her body.. i can wear it like a suit"
    possess kiyoshi scarlet a_6
    hide scarletGhost
    kiyoshi "Mmhh..."
    show kiyoshi a_3
    pause 1.2
    show kiyoshi a_1 blush
    kiyoshi "I'm Scarlet! My hot neighbor i jerk off to a lot of time!"
    show kiyoshi a_0 blush

    "End for now"
    placeholder

label Mass_Poss_Dinner:
    routename "Ghost dinner"
    kiyoshiGhost "I'll check the local dinner to see if the beam touch people out of the school"
    hide kiyoshiGhost with moveoutleft
    scene black
    with dissolve
    scene Harem_bg pompe
    outfit Harem_chloe casual
    outfit gabriel uniform
    show Harem_chloe a_9 at centerright
    show Harem_chloeGhost b_2 at right, faceleft
    show gabrielGhost a_3 at centerleft
    show kiyoshiGhost a_1 at left, faceright with easeinleft
    "As i arrive near the local dinner, i see a woman ghost near her body and a teenager is looking at her ghost"
    gabrielGhost "Hi miss, how are you?"
    show Harem_chloeGhost b_6
    Harem_chloeGhost "Wha...?!"
    "The woman look at the teenager ghost"
    pause 0.5
    show Harem_chloeGhost b_3
    Harem_chloeGhost "How am i?! Are you kidding me?! I'm a ghost floating near my lifeless body!!! How can i be right?!"
    pause 1.5
    show Harem_chloeGhost b_4
    "She paused some seconds and look at him again"
    show Harem_chloeGhost b_3
    Harem_chloeGhost "And who are you? Why are you talking to me?"
    show Harem_chloeGhost b_4
    show gabrielGhost b_1
    show gabrielGhost:
        ease 1.0 xpos 0.55
    "He look at her with an evil grin"
    gabrielGhost "Who am i?!... I'M YOU!!!"
    possess gabriel Harem_chloe a_4
    "As he say that, he run thought her body and merge with it... she see the scene but she is too afraid to react"
    pause 1.0
    show Harem_chloeGhost b_3
    Harem_chloeGhost "How can you?... It's my body!!!"
    pause 0.5
    show gabriel a_6
    gabriel "It worked!!!"
    "He pause and look at his borrowed body"
    show gabriel b_7
    gabriel "I'm so sweet!!! I need to find somewhere private to explore my new body!"
    show gabriel a_5:
        faceright
        pause 0.5
        faceleft
        pause 0.5
        faceright
    hide gabriel with moveoutright
    show Harem_chloeGhost b_4
    Harem_chloeGhost "HEY! come back!!!"
    "The woman look affraid of what the pervert teenager can do with her grown woman body"
    show Harem_chloeGhost b_9
    Harem_chloeGhost "I need to find another body to fight him!!!"
    hide Harem_chloeGhost with moveoutright
    show kiyoshiGhost:
        ease 1.0 xpos 0.55
    kiyoshiGhost "I think i should follow him, he seem to go to the dinner"
    hide kiyoshiGhost with moveoutright
    scene black
    with dissolve
    scene Harem_bg resto day
    outfit Harem_ruby maid
    clone zoey Harem_ruby
    show zoey a_1 at centerleft, faceleft
    outfit Harem_trista maid
    clone sam Harem_trista
    show sam a_1 at left, faceleft
    show Harem_tristaGhost b_4 at left, faceleft
    show Harem_rubyGhost b_0 at centerleft, faceleft
    show gabriel b_8 at centerright, faceleft with easeinright
    pause 1.5
    show kiyoshiGhost a_1 at right, faceleft with easeinright
    "The two waitress of the dinner are standing here, certainly afraid to be out of their bodies"
    Harem_tristaGhost "What is going on?!"
    Harem_rubyGhost "I don't know Trista..."
    show gabriel b_7:
        ease 1.0 xpos 0.45
    gabriel "Hey sweetie... I should have waited and take over your body... It would have been better"
    show Harem_rubyGhost b_5
    show Harem_tristaGhost b_7
    Harem_rubyGhost "Hey get out of my body your creep!"
    show gabriel b_10
    gabriel "But my new body is very nice, i should go check it to the bathroom"
    pause 1.0
    show gabriel b_11
    gabriel "Bye girls!"
    hide gabriel with moveoutleft
    pause 1.0
    "One of the waitress start to panick"
    Harem_tristaGhost "What the fuck was it?!"
    show Harem_rubyGhost b_3
    Harem_rubyGhost "I think someone take over this woman body.."
    pause 1.0
    show Harem_tristaGhost b_4
    Harem_tristaGhost "So you say it's possible to take someone else body?!"
    Harem_rubyGhost "I don't know.. maybe.."
    "As the ghostly shape of the waitress discuss, I'm thinking of what i can do now.."
    "I can possess one of them or follow the boy inside the bathroom.."
    timedchoice 5 Mass_Poss_Dinner_stoler
    menu:
        "What to do?"

        "{s}Possess a sexy waitress{/s}":
            routename "Ghost dinner Ruby"
            placeholder

        "Follow the boy":
            routename "Ghost dinner boy"
            hide kiyoshiGhost with moveoutleft
            scene black
            with dissolve
            scene infirmary day
            show gabriel b_11 at centerleft
            show kiyoshiGhost a_1 at right, faceleft with easeinright
            "As i arrive, i see the boy staring into his reflexion on the mirror of the bathroom.."
            gabriel "So.. This is me now.."
            pause 1.0
            show gabriel b_8
            gabriel "I'm now a sexy milf!.."
            pause 1.0
            show gabriel b_7
            gabriel "And i'm so cute!.."
            pause 1.0
            show gabriel b_0
            "He start to touch his new breast and vagina.."
            pause 2.5
            gabriel "So good..."
            pause 1.0
            show gabriel b_8
            gabriel "I need to see what i look like naked.."
            show gabriel b_7
            "As he say that, he start to undress.. starting by the bottom.."
            pause 1.0
            outfit gabriel casualblack
            gabriel "I'm so soft.. So sexy.."
            pause 1.0
            show gabriel b_0
            outfit gabriel costume
            gabriel "He take care to caress his borrowed breast in the process.."
            pause 1.0
            show gabriel a_6
            gabriel "Woaw! I really hit the jackpot!"
            pause 1.0
            show gabriel a_4
            "He massage his new soft skin and start to remove his underwear.."
            pause 1.0
            show gabriel a_3
            outfit gabriel nude
            "He paused in front of the sexy woman naked in front of him.."
            pause 2.0
            show gabriel a_4
            gabriel "mmhh.."
            pause 2.0
            show gabriel b_7
            gabriel "Hello cutie!.. Ready to have fun?! hehe.."

            placeholder

label Mass_Poss_Dinner_stoler:
    routename "Ghost dinner stoler"
    show Harem_chloeGhost a_7 at center, faceleft with easeinright
    pause 1.0
    show Harem_chloeGhost a_8
    Harem_chloeGhost "Excuse me lady but i must use your body!"
    show Harem_rubyGhost b_5
    show Harem_tristaGhost b_7
    Harem_rubyGhost "What?!"
    show Harem_chloeGhost a_3:
        ease 0.5 xpos 0.35
    show Harem_rubyGhost:
        ease 0.5 xpos 0.20
    show Harem_tristaGhost:
        ease 0.5 xpos 0.05
    "As she say that, she run through one of the waitress body, making her go through her friend body.."
    possess Harem_chloe zoey a_2
    possess Harem_ruby sam a_4
    pause 1.5
    "The woman start to wake up in the body of the sexy waitress.. and start to feel her borrowed body"
    show Harem_chloe b_1
    Harem_chloe "I feel so good.. So young.."
    show Harem_chloe b_0
    Harem_chloe "But i need to find the little perv in my body!"
    hide Harem_chloe with moveoutleft
    "As the woman run away with one oh the waitress body, the waitress in her friend body start to wake up.."
    show Harem_ruby b_5
    Harem_ruby "ehhh.."
    show Harem_ruby b_7
    Harem_ruby "What have you done?!"

    "End for now"
    placeholder


screen lesbian_briefing():
    window:
        pos (1280 / 2, 88 / 2)
        anchor (0.5, 0.5)
        xmargin 24
        ymargin 16
        yminimum 0
        ymaximum 88
        at briefing_show_hide
        add LiveMarquee(Text(
                u"Operation Lesbian Sex \u2014 Mission Briefing \u2014 ",
                slow=False,
                style='briefing'))
transform briefing_show_hide:
    subpixel True
    on show:
        zoom 0.0
        linear 0.5 zoom 1.0
    on hide:
        linear 0.5 zoom 0.0
style briefing is text:
    font "fonts/Jura-DemiBold.ttf"
    color "#7de8f2"
    size 28
    layout "nobreak"
