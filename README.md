# B-9 Indifference
For [NaNoGenMo 2017](https://github.com/NaNoGenMo/2017/).

_Star Trek: Nemesis_ brings to an end **SPOILER** not only the story of the U.S.S. Enterprise-E and her crew,
but that of lieutenant commander Data as well. [The film ends](https://www.youtube.com/watch?v=qkwuTewUrcU) 
on a hopeful note, however, with the technologically inferior B-9 (B-4 in the movie itself) android, into which Data had
 previously copied all of his own memories, displaying some of Data’s mannerisms.

_B-9 Indifference_ generates a _Star Trek: The Next Generation_ script of arbitrary length using Markov chains trained on 
the show’s episode and movie scripts. It is intended to simulate B-9 reconstructing Data’s memories as best as its poor 
programming can manage.

To generate the output yourself you can type `python b9_app.py` in the command line and you will be prompted for the 
desired wordcount. _B-9 Indifference_ then:

1. Trains all the relevant models.
2. Picks a random cast member to begin.
3. Generates a random number of sentences for that cast member.
4. Selects the next cast member most likely to follow the first.
5. Rinses and repeats, incrementing the stardate and adding more text until the word limit is hit.
6. Outputs the final script to an HTML file.

You can see the latest output [here](https://github.com/eoinnoble/b9-indifference/blob/master/output/output.html), but I
 don’t recommend you read through it in its entirety. Instead, I’ve picked out some key pieces below:

![42532.1 RIKER: Captain Picard, this is the USS Enterprise. I’m sorry, Worf… but I can’t help you – I don’t know who 
any of you are. Give us everything you can to get them out of there, Mister O’Brien… We’re fine tuned enough to see your
 parents, that’s your business… but we don’t get in that thing, I guarantee you won’t either. Picard, Riker and Troi 
 move toward the turbolift… Riker passes Geordi and Picard… GEORDI: Under normal circumstances, we could divert that 
 field energy and use it to simulate the pulse sent by the 
 shuttle.](https://github.com/eoinnoble/b9-indifference/blob/master/output/images/b91.jpg)

![PICARD: Nevertheless, you will obey every order you’re given and you will not profit by them. If I can boost the 
output field, I might be able to knock it off-line with a single shot… Firing… TROI: He’s concealing something and it’s 
more than just a role to you. Captain, I just want to voice my concerns about the way the change in command is affecting
 the crew. Commander Riker and I are two separate individuals. You have no idea how frightening it is for me to accept 
 that there’s a reality out there where you never loved 
 me…](https://github.com/eoinnoble/b9-indifference/blob/master/output/images/b92.jpg)

![Beverly suddenly reacts to something he sees, stands… Kurn pauses, glances threateningly back at Riker – he gets the 
hint. BEVERLY: … And I’m going to skip it today. Up to that moment, you were the reason he and Deanna never got 
together. It may be true that headaches were once quite common… but this was in the middle of writing a cook book when 
she died. TROI: But believe me, she doesn’t want to stay in my quarters. But you will need me if you have any idea why 
Hedril would make my mother your step-mother. I think it is trying to bring it all into focus. Troi and Worf are at 
their stations; Data relieves the supernumerary at Ops, examines readouts. RIKER: The preparation for the mission… the 
play… they were all sucked out into space.. He walks warily out of the engine core. A beat as the crew watches 
him.](https://github.com/eoinnoble/b9-indifference/blob/master/output/images/b93.jpg)

![TROI: I want you to start a new piece… I’d like you to talk about things they want to reveal. Tasha, duty always, 
steps forward and grabs the fallen singer’s BAT’LETH. In the background, the bed is violently shaken underneath her. 
Picard gives them a reassuring smile and moves away… Timicin sighs, gets out of bed. PICARD: I do, Mister Data… and our 
job is to find out what it is or where it comes from? Mister Riker, set a course for the site of the first tests of this
 new technology. Do you know how to operate this vessel. We can see on his face is thoughtful, reflective, not in pain. 
 WESLEY: For a second there, I thought I wanted to be by myself, but I guess you could say I’m a little… troubled. No 
 one is going to be fine… I don’t have to find my own path. She is sitting down at his left arm and grabs it, as if he’s
  talking to himself – he’s practicing a speech. Worf reacts, surprised, but before he can answer, Alexandra BURSTS INTO
   the room, Troi CLOSE BEHIND him. Wesley makes an adjustment to his 
   circuitry.](https://github.com/eoinnoble/b9-indifference/blob/master/output/images/b94.jpg)

## Credits
- The original _TNG_ series and film scripts were sourced from 
[Star Trek Minutiae](http://www.st-minutiae.com/resources/scripts/), which has a disclaimer that I should include here 
as well: this project is not endorsed, sponsored or affiliated with CBS Studios Inc. or the _Star Trek_ franchise. This 
project is intended for personal use only, under “fair use” principles of United States copyright law.
- The Markov chains were trained using the excellent [Markovify](https://github.com/jsvine/markovify).
- The typeface used in the output file is 
[Swiss 911 Std Ultra Compressed](https://www.myfonts.com/fonts/bitstream/swiss-911/ultra-compressed/), by 
[Bitstream](https://www.myfonts.com/foundry/Bitstream/), licensed from [MyFonts](https://www.myfonts.com/).


> PICARD: I don’t know if all this has made sense to you, but I wanted you to know what kind of man he was. In his quest to be more like us, he helped show us what it means to be human.