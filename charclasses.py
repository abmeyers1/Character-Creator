# For creating character classes with basic starting equipment and abilities
# Each needs to contain class abilities, equipment, proficiency, saving throws
classes = {
    'Artificer': {
        'skill number': 2,
        'skill proficiencies': ['Arcana', 'History', 'Investigation', 'Medicine', 'Perception', 'Sleight of Hand'],
        'tool proficiencies': ["Thieves' Tools", "Tinker's Tools", "One type of artisan's tools of your choice"],
        'weapon proficiencies': ['Simple Weapons'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields'],
    },
    'Barbarian': {
        'skill number': 2,
        'skill proficiencies': ['Animal Handling', 'Athletics', 'Intimidation', 'Nature', 'Perception', 'Survival'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons', 'Martial Weapons'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields']
    },
    'Bard': {
        'skill number': 3,
        'skill proficiencies': ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception', 'History',
                                'Insight',
                                'Intimidation', 'Investigation', 'Medicine', 'Nature', 'Perception', 'Performance',
                                'Persuasion', 'Religion', 'Sleight of Hand', 'Stealth', 'Survival'],
        'tool proficiencies': ['Musical Instrument', 'Musical Instrument', 'Musical Instrument'],
        'weapon proficiencies': ['Simple Weapons', 'Hand Crossbows', 'Longsword', 'Rapier', 'Shortsword'],
        'armor proficiencies': ['Light Armor']
    },
    'Blood Hunter': {
        'skill number': 3,
        'skill proficiencies': ['Athletics', 'Acrobatics', 'Arcana', 'History', 'Insight', 'Investigation', 'Religion',
                                'Survival'],
        'tool proficiencies': ["Alchemist's supplies"],
        'weapon proficiencies': ['Simple Weapons', 'Martial Weapons'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields']
    },
    'Cleric': {
        'skill number': 2,
        'skill proficiencies': ['History', 'Insight', 'Medicine', 'Persuasion', 'Religion'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields']
    },
    'Druid': {
        'skill number': 2,
        'skill proficiencies': ['Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion',
                                'Survival'],
        'tool proficiencies': ['Herbalism kit'],
        'weapon proficiencies': ['Club', 'Dagger', 'Darts', 'Javelins', 'Maces', 'Quarterstaff', 'Scimitars', 'Sickles',
                                 'Slings', 'Spears'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields', 'No armor or shields made of metal']
    },
    'Fighter': {
        'skill number': 2,
        'skill proficiencies': ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation',
                                'Perception', 'Survival'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons', 'Martial Weapons'],
        'armor proficiencies': ['All Armor', 'Shields']
    },
    'Monk': {
        'skill number': 2,
        'skill proficiencies': ['Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth'],
        'tool proficiencies': ["One type of Artisan's tools or one musical instrument"],
        'weapon proficiencies': ['Simple Weapons', 'Shortsword'],
        'armor proficiencies': []
    },
    'Paladin': {
        'skill number': 2,
        'skill proficiencies': ['Athletics', 'Insight', 'Intimidation', 'Medicine', 'Persuasion', 'Religion'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons', 'Martial Weapons'],
        'armor proficiencies': ['All armor', 'Shields']
    },
    'Ranger': {
        'skill number': 3,
        'skill proficiencies': ['Animal Handling', 'Athletics', 'Insight', 'Investigation', 'Nature', 'Perception',
                                'Stealth', 'Survival'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons', 'Martial Weapons'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields']
    },
    'Rogue': {
        'skill number': 4,
        'skill proficiencies': ['Acrobatics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception',
                                'Performance', 'Persuasion', 'Sleight of Hand', 'Stealth'],
        'tool proficiencies': ["Thieves' Tools"],
        'weapon proficiencies': ['Simple Weapons', 'Hand Crossbows', 'Longswords', 'Rapiers', 'Shortswords'],
        'armor proficiencies': ['Light Armor']
    },
    'Sorcerer': {
        'skill number': 2,
        'skill proficiencies': ['Arcana', 'Deceptions', 'Insight', 'Intimidation', 'Persuasion', 'Religion'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light Crossbows'],
        'armor proficiencies': []
    },
    'Warlock': {
        'skill number': 2,
        'skill proficiencies': ['Arcana', 'Deception', 'History', 'Intimidation', 'Investigation', 'Nature',
                                'Religion'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons'],
        'armor proficiencies': ['Light Armor']
    },
    'Wizard': {
        'skill number': 2,
        'skill proficiencies': ['Arcana', 'History', 'Insight', 'Investigation', 'Medicine', 'Religion'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light Crossbows'],
        'armor proficiencies': []
    }
}
