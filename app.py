from flask import Flask, render_template

app = Flask(__name__)

mainTitle = "Path of Exile Item Design"
highlight_text = "Click on an image to highlight it."
intention_title = "Gameplay Intention"
flavor_title = "Flavor Comment"

@app.route('/')
def home():
    return render_template('index.html', mainTitle=mainTitle)

@app.route('/POE1')
def poe1():
    cards = [
        {
            'image': 'images/POE_Item_01_MotherGift.png',
            'GameplayText': 'A great option to generate <a href="https://www.poewiki.net/wiki/Vaal_skill" target=blank>souls</a> '
                            'at any time with the condition of summoning and killing minions.',
            'FlavorText': 'I wanted to name this item "Divine\'s Gift," but sacrificing your children for '
                        '<a href="https://www.poewiki.net/wiki/Vaal_skill" target=_blank>Vaal Skills</a> '
                        'or <a href="https://www.poewiki.net/wiki/Soul_Eater" target=_blank>Soul Eater</a> really fits the dark fantasy of POE.',
        },
        {
            'image': 'images/POE_Item_02_Derealization.png',
            'GameplayText': 'This item would allow the player to avoid building defenses for themselves but only for their minions,'
                            'as the player wouldn\'t exist for the enemies.',
            'FlavorText': '<a href="https://en.wikipedia.org/wiki/Derealization" target=blank>What is Derealization?</a>',
        },
        {
            'image': 'images/POE_Item_04_TillDeathDoUsPart.png',
            'GameplayText': '<a href="https://www.poewiki.net/wiki/Trauma" target=blank>Trauma</a> is a mechanic that basically '
                            'increases your damage but makes you hit yourself with physical damage the more trauma you have. <br> <br> '
                            'This item requires building a maximum amount of physical damage reduction. <br> <br> Once you start a boss fight with this '
                            'ring equipped, one of the two will die from trauma at some point.',
            'FlavorText': '',
        },
        {
            'image': 'images/POE_Item_07_MalachaisLoop.png',
            'GameplayText': 'A way of getting the <a href="https://www.poewiki.net/wiki/Berserk" target=blank>Berserk buff</a> '
                            'other than <a href="https://www.poewiki.net/wiki/Berserk" target=_blank>the gem</a> (currently the only way) with the condition of generating and removing '
                            '<a href="https://www.poewiki.net/wiki/Frenzy_charge" target=blank>frenzy charges</a>.',
            'FlavorText': 'The flavor text refers to the item but also to Path of Exile.',
        },
        {
            'image': 'images/POE_Item_08_Paranoia.png',
            'GameplayText': 'This item would provide agency over the number of enemies near you, which affects some mechanics like '
                            '<a href="https://www.poewiki.net/wiki/Overwhelm" target=blank>Overwhelm</a>.',
            'FlavorText': '',
        },
        {
            'image': 'images/POE_Item_09_QuillOfPersonality.png',
            'GameplayText': 'A way for players to create their own "unique" item.',
            'FlavorText': '',
        },
        {
            'image': 'images/POE_Item_10_QuanticEncounters.png',
            'GameplayText': 'A way to get some agency over the placement of encounters, as some of them depend heavily on their '
                            'position, like <a href="https://www.poewiki.net/wiki/Breach" target=blank>breaches</a>.',
            'FlavorText': 'Partly inspired by Outer Wilds.',
        },
        {
            'image': 'images/POE_Item_11_MuscleTissue.png',
            'GameplayText': 'I wanted to make Strength/Dexterity stacking work on two stats instead of one to add a new dimension to attribute stacking.',
            'FlavorText': 'I like the idea of '
                        '<a href="https://www.poewiki.net/wiki/Passive_skill#Jewel_sockets" target="blank">socketing</a> '
                        'something organic instead of mineral.',
        },
        {
            'image': 'images/POE_Item_12_FailedExperiment.png',
            'GameplayText': 'I think that experience orbs feel really good and give movement a new dimension. <br> <br>'
                            'I also wanted to create an experience strategy where generating more experience would result in getting more items.',
            'FlavorText': '',
        },
        {
            'image': 'images/POE_Item_13_TheThird.png',
            'GameplayText': 'This is a giga end-game item where you have to build two characters instead of one. <br> <br>'
                            'The other character would be a bot considered as another player and apply the <a href="https://www.poewiki.net/wiki/Partying" target=blank>same rules</a>. <br> <br> '
                            'The second character would probably only be built as an aura bot, so I considered preventing auras from applying between the two.',
            'FlavorText': 'This item was strongly inspired by the '
                        '<a href="https://en.wikipedia.org/wiki/Third_man_factor" target=blank>Third man factor</a>.',
        },
        {
            'image': 'images/POE_Item_14_SpatialDistortion.png',
            'GameplayText': 'Splitting hits in two can interact with other mechanics, notably '
                            '<a href="https://www.poewiki.net/wiki/Defiance_of_Destiny" target=blank>Defiance of Destiny</a>. <br> <br> '
                            'Adding a small delay before the second hit would be interesting but too strong.',
            'FlavorText': 'The flavor text was inspired by '
                        '<a href="https://www.youtube.com/watch?v=4ofJpOEXrZs" target=blank>The Amazing Digital Circus Ep2</a>.',
        },
        {
            'image': 'images/POE_Item_16_ANS.png',
            'GameplayText': 'This would allow you to be "half stunned," as you wouldn\'t be able to change the action your character '
                            'is performing, but your character would repeat this action.',
            'FlavorText': '<a href="https://en.wikipedia.org/wiki/Autonomic_nervous_system" target=blank>Autonomic Nervous System</a> '
                        'basically allows you to breathe even when unconscious.',
        },
        {
            'image': 'images/POE_Item_17_TheFinalPiece.png',
            'GameplayText': 'Changing your character while in a map (moving gems) is annoying. This item would reward you for not doing it. <br> <br>'
                            'Right now, the reward is more damage and damage reduction, but it should be more interesting.',
            'FlavorText': '',
        },
        {
            'image': 'images/POE_Item_18_ShortCircuit.png',
            'GameplayText': 'A "short circuit" would happen within a loop in the skill tree, which is something you want to avoid '
                            'right now, but this item would make it worthwhile.',
            'FlavorText': 'The flavor text mainly refers to making builds as strong as possible, which is the main goal of POE.',
        },
        {
            'image': 'images/POE_Item_19_OmniGem.png',
            'GameplayText': 'Designed to create gameplay variations by using many different skills with the same gem. <br> <br> '
                            'Martial weapons don\'t exist right now, but they would be: Axe, Sword, Mace, Claw, Bow, Warstaff. <br> <br> '
                            '"That you can use" means that, for example, if this gem were supported by '
                            '<a href="https://www.poewiki.net/wiki/Shockwave_Support" target=blank>Shockwave</a>, it would add a requirement of '
                            'only staffs and maces, so only skills that can be used with a staff or mace could be used by this gem. <br> <br> '
                            'Great synergy with mechanics that ask you to use different spells or attacks, like '
                            '<a href="https://www.poewiki.net/wiki/Mastery_Effect:Caster3" target=blank>This Caster Mastery</a>.',
            'FlavorText': '',
        }
    ]
    return render_template('poe1.html', mainTitle=mainTitle, highlight_text=highlight_text, intention_title=intention_title,
                        flavor_title=flavor_title, cards=cards)

@app.route('/POE2')
def poe2():
    cards = []
    return render_template('poe2.html', mainTitle=mainTitle, highlight_text=highlight_text, intention_title=intention_title,
                        flavor_title=flavor_title, cards=cards)

if __name__ == '__main__':
    app.run(debug=True)