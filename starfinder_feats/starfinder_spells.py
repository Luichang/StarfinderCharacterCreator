from starfinder_feats.starfinder_spell import Spell

daze = Spell('Daze', 0, True, True)
pyschokinetic_hand = Spell('Psychokinetic Hand', 0, True, True)
detect_thoughts = Spell('Detect Thoughts', 1, True, False)
identify = Spell('Identify', 1, True, True)
augury = Spell('Augury', 2, True, False)
tongues = Spell('Tongues', 3, True, True)
divination = Spell('Divination', 4, True, False)
contact_plane = Spell('Contact Other Plane', 5, True, True)
vision = Spell('Vision', 6, True, False)
zone_truth = Spell('Zone of Truth', 2, True, False)
clairaudience = Spell('Clairaudience/Clairvoyance', 3, True, True)
mind_probe = Spell('Mind Probe', 4, True, False)
telepathy = Spell('Telepathy', 5, True, False)
true_seeing = Spell('True Seeing', 6, True, True)
command = Spell('Command', 1, True, False)
hold_person = Spell('Hold Person', 2, True, False)
suggestion = Spell('Suggestion', 3, True, False)
confusion = Spell('Confusion', 4, True, False)
dominate_person = Spell('Dominate Person', 5, True, False)
mass_suggestion = Spell('Suggestion, Mass', 6, True, False)
magic_missile = Spell('Magic Missile', 1, False, True)
darkvision = Spell('Darkvision', 2, True, True)
irridate = Spell('Irradiate', 3, True, True)
remove_radioactivity = Spell('Remove Radioactivity', 4, True, True)
telekinesis = Spell('Telekinesis', 5, False, True)
control_gravity = Spell('Control Gravity', 6, True, True)
life_bubble = Spell('Life Bubble', 1, True, True)
fog_cloud = Spell('Fog Cloud', 2, True, True)
entropic_grasp = Spell('Entropic Grasp', 3, False, True)
reincarnate = Spell('Reincarnate', 4, True, False)
commune_nature = Spell('Commune With Nature', 5, True, False)
terraform = Spell('Terraform', 6, False, True)
mystic_cure_1 = Spell('Mystic Cure', 1, True, False)
mystic_cure_2 = Spell('Mystic Cure', 2, True, False)
mystic_cure_3 = Spell('Mystic Cure', 3, True, False)
mystic_cure_4 = Spell('Mystic Cure', 4, True, False)
mystic_cure_5 = Spell('Mystic Cure', 5, True, False)
mystic_cure_6 = Spell('Mystic Cure', 6, True, False)
lesser_remove_condition = Spell('Remove Condition, Lesser', 1, True, False)
remove_condition = Spell('Remove Condition', 2, True, False)
remove_affliction = Spell('Remove Affliction', 3, True, False)
restoration = Spell('Restoration', 4, True, False)
greater_remove_condition = Spell('Remove Condition, Greater', 5, True, False)
mind_thrust_1 = Spell('Mind Thrust', 1, True, False)
mind_thrust_2 = Spell('Mind Thrust', 2, True, False)
mind_thrust_3 = Spell('Mind Thrust', 3, True, False)
mind_thrust_4 = Spell('Mind Thrust', 4, True, False)
mind_thrust_5 = Spell('Mind Thrust', 5, True, False)
mind_thrust_6 = Spell('Mind Thrust', 6, True, False)
lesser_confusion = Spell('Confusion, Lesser', 1, True, False)
inflict_pain = Spell('Inflict Pain', 2, True, False)
synaptic_pulse = Spell('Synaptic Pulse', 3, True, False)
feeblemind = Spell('Feeblemind', 5, True, False)

spells = [
    Spell('Dancing Lights', 0, False, True),
    daze,
    Spell('Detect Affliction', 0, True, True),
    Spell('Detect Magic', 0, True, True),
    Spell('Energy Ray', 0, False, True),
    Spell('Fatigue', 0, True, False),
    Spell('Ghost Sound', 0, True, True),
    Spell('Grave Words', 0, True, False),
    Spell('Mending', 0, False, True),
    pyschokinetic_hand,
    Spell('Stabilize', 0, True, False),
    Spell('Telekinetic Projectile', 0, True, False),
    Spell('Telepathic Message', 0, True, True),
    Spell('Token Spell', 0, True, True),
    Spell('Transfer Charge', 0, False, True),
    Spell('Charm Person', 1, True, False),
    command,
    Spell('Comprehend Languages', 1, False, True),
    lesser_confusion,
    Spell('Detect Radiation', 1, True, True),
    Spell('Detect Tech', 1, False, True),
    detect_thoughts,
    Spell('Disguise Self', 1, True, True),
    Spell('Erase', 1, False, True),
    Spell('Fear', 1, True, False),
    Spell('Flight', 1, False, True),
    Spell('Grease', 1, False, True),
    Spell('Hold Portal', 1, False, True),
    Spell('Holographic Image', 1, False, True),
    identify,
    Spell('Jolting Surge', 1, False, True),
    Spell('Keen Senses', 1, True, True),
    life_bubble,
    magic_missile,
    mind_thrust_1,
    Spell('Mindlink', 1, True, False),
    mystic_cure_1,
    Spell('Overheat', 1, False, True),
    Spell('Reflecting Armor', 1, True, False),
    lesser_remove_condition,
    Spell('Share Language', 1, True, False),
    Spell('Supercharge Weapon', 1, False, True),
    Spell('Unseen Servant', 1, False, True),
    Spell('Wisp Ally', 1, True, False),
    augury,
    Spell('Caustic Conversion', 2, False, True),
    Spell('Command Undead', 2, True, True),
    darkvision,
    Spell('Daze Monster', 2, True, True),
    Spell('Fear', 2, True, False),
    Spell('Flight', 2, False, True),
    fog_cloud,
    Spell('Force Blast', 2, True, False),
    hold_person,
    Spell('Holographic Image', 2, False, True),
    Spell('Hurl Forcedisk', 2, True, False),
    Spell('Implant Data', 2, False, True),
    inflict_pain,
    Spell('Inject Nanobots', 2, False, True),
    Spell('Invisibility', 2, False, True),
    Spell('Knock', 2, False, True),
    Spell('Logic Bomb', 2, False, True),
    Spell('Make Whole', 2, False, True),
    Spell('Microbot Assault', 2, False, True),
    mind_thrust_2,
    Spell('Mirror Image', 2, False, True),
    mystic_cure_2,
    Spell('Recharge', 2, False, True),
    remove_condition,
    Spell('Restoration, Lesser', 2, True, False),
    Spell('Security Seal', 2, False, True),
    Spell('See Invisibility', 2, True, True),
    Spell('Shield Other', 2, True, False),
    Spell('Spider Climb', 2, True, True),
    Spell('Status', 2, True, False),
    zone_truth,
    Spell('Arcane Sight', 3, False, True),
    Spell('Arcing Surge', 3, False, True),
    Spell('Bestow Curse', 3, True, False),
    Spell('Charm Monster', 3, True, False),
    clairaudience,
    Spell('Deep Slumber', 3, True, False),
    Spell('Discharge', 3, False, True),
    Spell('Dispel Magic', 3, True, True),
    Spell('Displacement', 3, False, True),
    entropic_grasp,
    Spell('Explosive Blast', 3, False, True),
    Spell('Fear', 3, True, False),
    Spell('Flight', 3, False, True),
    Spell('Handy Junkbot', 3, False, True),
    Spell('Haste', 3, True, True),
    Spell('Healing Junkbot', 3, False, True),
    Spell('Hologram Memory', 3, True, False),
    Spell('Holographic Image', 3, False, True),
    Spell('Instant Virus', 3, False, True),
    irridate,
    mind_thrust_3,
    mystic_cure_3,
    Spell('Nondetection', 3, False, True),
    Spell('Probability Prediction', 3, False, True),
    Spell('Psychokinetic Strangulation', 3, True, False),
    Spell('Ray of Exhaustion', 3, True, False),
    remove_affliction,
    Spell('Resistant Armor, Lesser', 3, True, True),
    Spell('Slow', 3, True, True),
    Spell('Speak with Dead', 3, True, False),
    suggestion,
    synaptic_pulse,
    tongues,
    Spell('Animate Dead', 4, True, True),
    Spell('Arcane Eye', 4, False, True),
    confusion,
    Spell('Corrosive Haze', 4, False, True),
    Spell('Cosmic Eddy', 4, True, False),
    Spell('Creation', 4, False, True),
    Spell('Death Ward', 4, True, False),
    Spell('Destruction Protocol', 4, False, True),
    Spell('Dimension Door', 4, False, True),
    Spell('Discern Lies', 4, True, False),
    Spell('Dismissal', 4, True, True),
    divination,
    Spell('Enervation', 4, True, False),
    Spell('Fear', 4, True, False),
    Spell('Flight', 4, False, True),
    Spell('Hold Monster', 4, True, False),
    Spell('Holographic Image', 4, False, True),
    Spell('Invisibility, Greater', 4, False, True),
    mind_probe,
    mind_thrust_4,
    mystic_cure_4,
    Spell('Overload Systems', 4, False, True),
    Spell('Planar Binding', 4, True, True),
    reincarnate,
    remove_radioactivity,
    Spell('Resilient Sphere', 4, False, True),
    Spell('Resistant Armor', 4, True, True),
    restoration,
    Spell('Rewire Flesh', 4, False, True),
    Spell('Soothing Protocol', 4, False, True),
    Spell('Telepathic Bond', 4, True, False),
    Spell('Wall of Fire', 4, False, True),
    Spell('Break Enchantment', 5, True, True),
    Spell('Call Cosmos', 5, True, False),
    Spell('Command, Greater', 5, True, False),
    commune_nature,
    contact_plane,
    Spell('Control Machines', 5, False, True),
    Spell('Creation', 5, False, True),
    Spell('Crush Skull', 5, True, False),
    Spell('Dismissal', 5, True, True),
    Spell('Dispel Magic, Greater', 5, True, True),
    dominate_person,
    feeblemind,
    Spell('Flight', 5, False, True),
    Spell('Heat Leech', 5, False, True),
    Spell('Holographic Image', 5, False, True),
    Spell('Holographic Terrain', 5, False, True),
    mind_thrust_5,
    Spell('Mislead', 5, False, True),
    Spell('Modify Memory', 5, True, False),
    mystic_cure_5,
    Spell('Mystic Cure, Mass', 5, True, False),
    Spell('Passwall', 5, False, True),
    Spell('Planar Binding', 5, True, True),
    Spell('Private Sanctum', 5, False, True),
    Spell('Prying Eyes', 5, False, True),
    Spell('Raise Dead', 5, True, False),
    Spell('Rapid Repair', 5, False, True),
    greater_remove_condition,
    Spell('Resistant Aegis', 5, True, True),
    Spell('Retrocognition', 5, True, False),
    Spell('Synapse Overload', 5, False, True),
    Spell('Synaptic Pulse, Greater', 5, True, False),
    telekinesis,
    telepathy,
    Spell('Teleport', 5, False, True),
    Spell('Unwilling Guardian', 5, False, True),
    Spell('Wall of Force', 5, False, True),
    Spell('Waves of Fatigue', 5, True, False),
    Spell('Battle Junkbot', 6, False, True),
    Spell('Chain Surge', 6, False, True),
    control_gravity,
    Spell('Control Undead', 6, True, True),
    Spell('Discharge, Greater', 6, False, True),
    Spell('Disintegrate', 6, False, True),
    Spell('Enshrining Refuge', 6, True, False),
    Spell('Ethereal Jaunt', 6, True, True),
    Spell('Flesh to Stone', 6, True, False),
    Spell('Flight', 6, False, True),
    Spell('Gravitational Singularity', 6, True, False),
    Spell('Holographic Image', 6, False, True),
    Spell('Inflict Pain, Mass', 6, True, False),
    Spell('Interplanetary Teleport', 6, False, True),
    Spell('Invisibility, Mass', 6, False, True),
    mind_thrust_6,
    mystic_cure_6,
    Spell('Mystic Cure, Mass', 6, True, False),
    Spell('Planar Barrier', 6, True, True),
    Spell('Planar Binding', 6, True, True),
    Spell('Plane Shift', 6, True, True),
    Spell('Psychic Surgery', 6, True, False),
    Spell('Regenerate', 6, True, False),
    Spell('Resistant Armor, Greater', 6, True, True),
    Spell('Rewire Flesh, Mass', 6, False, True),
    Spell('Shadow Walk', 6, True, True),
    Spell('Shadowy Fleet', 6, False, True),
    Spell('Snuff Life', 6, True, False),
    Spell('Subjective Reality', 6, True, False),
    mass_suggestion,
    Spell('Sympathetic Vibration', 6, False, True),
    Spell('Telepathic Jaunt', 6, True, False),
    terraform,
    true_seeing,
    Spell('Veil', 6, False, True),
    vision,
    Spell('Wall of Steel', 6, False, True)
]

def spells_by_level(spells_list : list[Spell], level : int) -> list[Spell]:
    """function that returns a list of spells based on the entered level

    Args:
        spells_list (list[Spell]): list of spells, preferably already reduced to single class
        level (int): spell level

    Returns:
        list[Spell]: list of spells of the desired level
    """
    level_spells = []
    for spell in spells_list:
        if spell.level == level:
            level_spells.append(spell)
    return level_spells

def spells_by_class(spells_list : list[Spell], class_name) -> list[Spell]:
    """function that returns a list of spells based on the entered class name

    Args:
        spells_list (list[Spell]): list of spells
        class_name (str): class name

    Returns:
        list[Spell]: list of spells of the desired class
    """
    class_spells = []
    for spell in spells_list:
        if (class_name == "Mystic" and spell.mystic) or \
            (class_name == "Technomancer" and spell.technomancer):
            class_spells.append(spell)
    return class_spells
