from starfinder_classes.starfinder_mystic import Mystic
from starfinder_classes.starfinder_operative import Operative
from starfinder_classes.starfinder_technomancer import Technomancer
from starfinder_races.starfinder_kasatha import Kasatha

from starfinder_feats.feat_requirement import Requirements
from starfinder_feats.starfinder_feat import Feat
from starfinder_feats.starfinder_feat_type import FeatType

any_feat = Feat("Any", False, None, None)
any_combat_feat = Feat("Any", True, None, None)

adaptive_fighting = Feat("Adaptive Fighting", True,
                        Requirements(feat=[any_combat_feat, any_combat_feat, any_combat_feat]),
                        FeatType.WORDS)
basic_melee_prof = Feat("Basic Melee Weapon Proficiency", True, None, FeatType.WORDS)
advanced_melee_prof = Feat("Advanced Melee Weapon Proficiency", True,
                            Requirements(feat=[basic_melee_prof]), FeatType.WORDS)
amplified_glitch = Feat("Amplified Glitch", True,
                        Requirements(skills=[["computers", 3], ["intimidate", 3]]), FeatType.WORDS)
antagonize = Feat("Antagonize", False, Requirements(skills=[["diplomacy", 5], ["intimidate", 5]]),
                    FeatType.WORDS)
barricade = Feat("Barricade", True, Requirements(skills=[["engineering", 1]]), FeatType.WORDS)
blind_fight = Feat("Blind-Fight", True, None, FeatType.WORDS)
bodyguard = Feat("Bodyguard", True, None, FeatType.WORDS)
harms_way = Feat("In Harm's Way", True, Requirements(feat=[bodyguard]), FeatType.WORDS)
cleave = Feat("Cleave", True, Requirements(ability=[["str", 13]], bab=1), FeatType.WORDS)
great_cleave = Feat("Great Cleave", True, Requirements(ability=[["str", 13]], feat=[cleave], bab=4),
                    FeatType.WORDS)
climbing_master = Feat("Climbing Master", False, Requirements(skills=[["athletics", 5]]),
                        FeatType.WORDS) # speed effected
combat_casting = Feat("Combat Casting", True, Requirements(spell_level=2), FeatType.WORDS)
connection_inkling = Feat("Connection Inkling", False, Requirements(ability=[["wis", 15]], level=5),
                            FeatType.WORDS) # TODO need to check that the character is NOT mystic
coordinated_shot = Feat("Coordinated Shot", True, Requirements(bab=1), FeatType.WORDS)
deadly_aim = Feat("Deadly Aim", True, Requirements(bab=1), FeatType.WORDS)
deflect_projectile = Feat("Deflect Projectiles", True, Requirements(bab=8), FeatType.WORDS)
reflect_projectile = Feat("Reflect Projectiles", True,
                            Requirements(bab=16, feat=[deflect_projectile]), FeatType.WORDS)
diehard = Feat("Diehard", False, None, FeatType.WORDS)
dive_for_cover = Feat("Dive for Cover", True, Requirements(reflex=2), FeatType.WORDS) # reflex +2
diversion = Feat("Diversion", False, None, FeatType.WORDS)
drag_down = Feat("Drag Down", True, None, FeatType.WORDS)
enhanced_resistance = Feat("Enhanced Resistance", False, Requirements(bab=4), FeatType.WORDS)
extra_resolve = Feat("Extra Resolve", False, Requirements(level=5), FeatType.WORDS) # resolve + 2
far_shot = Feat("Far Shot", True, Requirements(bab=1), FeatType.WORDS)
fast_talk = Feat("Fast Talk", False, Requirements(skills=[["bluff", 5]]), FeatType.WORDS)
fleet = Feat("Fleet", True, None, FeatType.WORDS) # speed effected
fusillade = Feat("Fusillade", True, Requirements(bab=1, race=Kasatha), FeatType.WORDS)
great_fortitude = Feat("Great Fortitude", False, None, FeatType.WORDS) # fortitude + 2
improved_great_fortitude = Feat("Improved Great Fortitude", False,
                                Requirements(feat=[great_fortitude], level=5), FeatType.WORDS)
grenade_proficiency = Feat("Grenade Proficiency", True, None, FeatType.WORDS)
tmp_class_name = Mystic()
tmp_class_name.select_selection("Healer")
harm_undead = Feat("Harm Undead", False, Requirements(class_name=tmp_class_name), FeatType.WORDS)
light_armor = Feat("Light Armor Proficiency", True, None, FeatType.WORDS)
heavy_armor = Feat("Heavy Armor Proficiency", True,
                    Requirements(ability=[["str", 13]], feat=[light_armor]), FeatType.WORDS)
small_arm_proficiency = Feat("Small Arm Proficiency", True, None, FeatType.WORDS)
longarm_proficiency = Feat("Longarm Proficiency", True, Requirements(feat=[small_arm_proficiency]),
                            FeatType.WORDS)
heavy_weapon = Feat("Heavy Weapon Proficiency", True,
                    Requirements(ability=[["str", 13]],
                                feat=[longarm_proficiency, small_arm_proficiency]),
                    FeatType.WORDS)
improved_combat = Feat("Improved Combat Maneuver", True, Requirements(bab=1),
                        FeatType.WORDS) # +4 bonus to perform one combat maneuver
pull_the_pin = Feat("Pull the Pin", True, Requirements(feat=[improved_combat]), FeatType.WORDS)
improved_crit = Feat("Improved Critical", True, Requirements(bab=8), FeatType.WORDS)
improved_feint = Feat("Improved Feint", True, None, FeatType.WORDS)
greater_feint = Feat("Greater Feint", True, Requirements(feat=[improved_feint], bab=6),
                        FeatType.WORDS)
improved_init = Feat("Improved Initiative", True, None, FeatType.WORDS) # "initiative", 4
improved_unarmed = Feat("Improved Unarmed Strike", True, None, FeatType.WORDS)
iron_will = Feat("Iron Will", False, None, FeatType.WORDS) # "Will", 2
improved_iron_will = Feat("Improved Iron Will", False, Requirements(feat=[iron_will], level=5),
                            FeatType.WORDS)
jet_dash = Feat("Jet Dash", False, None, FeatType.WORDS)
kip_up = Feat("Kip Up", True, Requirements(skills=[["acrobatics", 1]]), FeatType.WORDS)
lightning_reflexes = Feat("Lightning Reflexes", False, None, FeatType.WORDS) # "Reflex", 2
improved_lightning_reflexes = Feat("Improved Lightning Reflexes", False,
                                    Requirements(feat=[lightning_reflexes], level=5),
                                    FeatType.WORDS)
lunge = Feat("Lunge", True, Requirements(bab=6), FeatType.WORDS)
master_crafter = Feat("Master Crafter", False,
                        Requirements(skills=[["computers", "engineering", "life science",
                                              "mysticism", "physical science", "profession"], 5]),
                        FeatType.WORDS)
medical_expert = Feat("Medical Expert", False,
                        Requirements(skills=[["life science", 1], ["medicine", 1],
                                                ["physical science", 1]]),
                        FeatType.WORDS)
minor_psychic_power = Feat("Minor Psychic Power", False, Requirements(ability=[["cha", 11]]),
                            FeatType.WORDS) # Cast a 0-level spell as a spell-like ability 3/day
psychic_power = Feat("Psychic Power", False,
                    Requirements(ability=[["cha", 13]], feat=[minor_psychic_power], level=4),
                    FeatType.WORDS) # Cast a 1st-level spell as a spell-like ability 1/day
major_psychic_power = Feat("Major Psychic Power", False,
                            Requirements(ability=[["cha", 15]],
                                        feat=[minor_psychic_power, psychic_power], level=4),
                            FeatType.WORDS) # Cast a 2nd-level spell as a spell-like ability 1/day
mobility = Feat("Mobility", True, Requirements(ability=[["dex", 13]]), FeatType.WORDS)
agile_casting = Feat("Agile Casting", False,
                    Requirements(ability=[["key", 15], ["dex", 15]], feat=[mobility],
                                class_name=[Mystic, Technomancer], level=4),
                    FeatType.WORDS)
shot_on_run = Feat("Shot on the Run", True,
                    Requirements(ability=[["dex", 15]], feat=[mobility], bab=4), FeatType.WORDS)
parting_shot = Feat("Parting Shot", True,
                    Requirements(ability=[["dex", 15]], feat=[mobility, shot_on_run], bab=6),
                    FeatType.WORDS)
sidestep = Feat("Sidestep", True,
                Requirements(ability=[["dex", 15]], from_list=[["feat", [mobility]],
                                        ["class", Operative]]),
                FeatType.WORDS)
improved_sidestep = Feat("Improved Sidestep", True,
                        Requirements(ability=[["dex", 15]], feat=[sidestep],
                                    from_list=[["feat", [mobility]], ["class",  Operative]]),
                        FeatType.WORDS)
spring_attack = Feat("Spring Attack", True,
                    Requirements(ability=[["dex", 15]], feat=[mobility], bab=4), FeatType.WORDS)
multi_weapon_attack = Feat("Multi-Weapon Fighting", True, None, FeatType.WORDS)
mystic_strike = Feat("Mystic Strike", True, Requirements(spell_level=1), FeatType.WORDS)
nimble_moves = Feat("Nimble Moves", True, Requirements(ability=[["dex", 15]]), FeatType.WORDS)
opening_volley = Feat("Opening Volley", True, None, FeatType.WORDS)
penetrating_attack = Feat("Penetrating Attack", True, Requirements(bab=12), FeatType.WORDS)
penetrating_spell = Feat("Penetrating Spell", False, Requirements(spell_level=4), FeatType.WORDS)
power_armor_proficiency = Feat("Powered Armor Proficiency", True,
                                Requirements(ability=[["str", 13]], feat=[light_armor], bab=5),
                                FeatType.WORDS)
quick_draw = Feat("Quick Draw", True, Requirements(bab=1), FeatType.WORDS)
skill_focus = Feat("Skill Focus", False, None, FeatType.WORDS) # "choose", ["skill", ["any", 3]]
skill_synergy = Feat("Skill Synergy", False, None,
                    FeatType.WORDS) # "classSkill", [["any"], ["any"]]], # or a +2 bonus to it
sky_jockey = Feat("Sky Jockey", False, Requirements(skills=[["piloting", 5]]), FeatType.WORDS)
slippery_shooter = Feat("Slippery Shooter", True, Requirements(ability=[["dex", 15]], bab=6),
                        FeatType.WORDS)
sniper_weapon = Feat("Sniper Weapon Proficiency", True, None, FeatType.WORDS)
special_weapon = Feat("Special Weapon Proficiency", True,
                        Requirements(from_list=[["feat", [small_arm_proficiency,
                                                            basic_melee_prof]]]),
                        FeatType.WORDS)
spell_focus = Feat("Spell Focus", False, Requirements(spell_level=1, level=3), FeatType.WORDS)
spell_penetration = Feat("Spell Penetration", False, None,
                            FeatType.WORDS) # +2 bonus to caster level checks to overcome SR
greater_spell_penetration = Feat("Greater Spell Penetration", False,
                                    Requirements(feat=spell_penetration), FeatType.WORDS)
# ^ Additional +2 bonus to caster level checks to overcome SR
spellbane = Feat("Spellbane", False, Requirements(spell_level=-1), FeatType.WORDS)
spry_cover = Feat("Spry Cover", True, Requirements(bab=1), FeatType.WORDS)
stand_still = Feat("Stand Still", True, None, FeatType.WORDS)
improved_stand_still = Feat("Improved Stand Still", True, Requirements(feat=[stand_still]),
                            FeatType.WORDS)
step_up = Feat("Step Up", True, Requirements(bab=1), FeatType.WORDS)
step_up_and_strike = Feat("Step Up and Strike", True,
                            Requirements(ability=[["dex", 13]], feat=[step_up], bab=6),
                            FeatType.WORDS)
strike_back = Feat("Strike Back", True, Requirements(bab=1), FeatType.WORDS)
suppressive_fire = Feat("Suppressive Fire", True, Requirements(feat=[heavy_weapon], bab=1),
                        FeatType.WORDS)
swimming_master = Feat("Swimming Master", False, Requirements(skills=[["athletics", 5]]),
                        FeatType.WORDS) # effects speed
techno_dabbler = Feat("Technomantic Dabbler", False, Requirements(ability=[["int", 15]], level=5),
                        FeatType.WORDS) # TODO need to check that the character is NOT technomancer
toughness = Feat("Toughness", False, None,
                FeatType.WORDS) # +1 Stamina Point per character level and other bonuses
unfriendly_fire = Feat("Unfriendly Fire", True, Requirements(skills=[["bluff", 5]]), FeatType.WORDS)
veiled_threat = Feat("Veiled Threat", False,
                     Requirements(skills=[["intimidate", 1]], ability=[["cha", 15]]), FeatType.WORDS)
weapon_focus = Feat("Weapon Focus", True, None, FeatType.WORDS) # something gets chosen
versatile_focus = Feat("Versatile Focus", True, Requirements(feat=[weapon_focus]), FeatType.WORDS)
weapon_specialization = Feat("Weapon Specialization", True, Requirements(level=3), FeatType.WORDS)
versatile_specialization = Feat("Versatile Specialization", True,
                                Requirements(feat=[weapon_specialization], level=3),
                                FeatType.WORDS)


feats = [
    adaptive_fighting,
    advanced_melee_prof,
    amplified_glitch,
    antagonize,
    barricade,
    basic_melee_prof,
    blind_fight,
    bodyguard,
    harms_way,
    cleave,
    great_cleave,
    climbing_master,
    combat_casting,
    connection_inkling,
    coordinated_shot,
    deadly_aim,
    deflect_projectile,
    reflect_projectile,
    diehard,
    dive_for_cover,
    diversion,
    drag_down,
    enhanced_resistance,
    extra_resolve,
    far_shot,
    fast_talk,
    fleet,
    fusillade,
    great_fortitude,
    improved_great_fortitude,
    grenade_proficiency,
    harm_undead,
    heavy_armor,
    heavy_weapon,
    improved_combat,
    pull_the_pin,
    improved_crit,
    improved_feint,
    greater_feint,
    improved_init,
    improved_unarmed,
    iron_will,
    improved_iron_will,
    jet_dash,
    kip_up,
    light_armor,
    lightning_reflexes,
    improved_lightning_reflexes,
    longarm_proficiency,
    lunge,
    master_crafter,
    medical_expert,
    minor_psychic_power,
    psychic_power,
    major_psychic_power,
    mobility,
    agile_casting,
    shot_on_run,
    parting_shot,
    sidestep,
    improved_sidestep,
    spring_attack,
    multi_weapon_attack,
    mystic_strike,
    nimble_moves,
    opening_volley,
    penetrating_attack,
    penetrating_spell,
    power_armor_proficiency,
    quick_draw,
    skill_focus,
    skill_synergy,
    sky_jockey,
    slippery_shooter,
    small_arm_proficiency,
    sniper_weapon,
    special_weapon,
    spell_focus,
    spell_penetration,
    greater_spell_penetration,
    spellbane,
    spry_cover,
    stand_still,
    improved_stand_still,
    step_up,
    step_up_and_strike,
    strike_back,
    suppressive_fire,
    swimming_master,
    techno_dabbler,
    toughness,
    unfriendly_fire,
    veiled_threat,
    weapon_focus,
    versatile_focus,
    weapon_specialization,
    versatile_specialization,
]
