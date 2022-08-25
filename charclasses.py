# For creating character classes with basic starting equipment and abilities
# Each needs to contain class abilities, equipment, proficiency, saving throws
classes = {
    'Artificer': {
        'skill number': 2,
        'hit_die': 8,
        'skill proficiencies': ['Arcana', 'History', 'Investigation', 'Medicine', 'Perception', 'Sleight of Hand'],
        'tool proficiencies': ["Thieves' Tools", "Tinker's Tools", "One type of artisan's tools of your choice"],
        'weapon proficiencies': ['Simple Weapons'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields'],
        'stat_rec':[ 8,12,14,15,13,10]
    },
    'Barbarian': {
        'skill number': 2,
        'hit_die': 12,
        'skill proficiencies': ['Animal Handling', 'Athletics', 'Intimidation', 'Nature', 'Perception', 'Survival'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons', 'Martial Weapons'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields'],
        'stat_rec': [15,13,14,8,10,12] 
    },
    'Bard': {
        'hit_die':8,
        'skill number': 3,
        'skill proficiencies': ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception', 'History',
                                'Insight',
                                'Intimidation', 'Investigation', 'Medicine', 'Nature', 'Perception', 'Performance',
                                'Persuasion', 'Religion', 'Sleight of Hand', 'Stealth', 'Survival'],
        'tool proficiencies': ['Musical Instrument', 'Musical Instrument', 'Musical Instrument'],
        'weapon proficiencies': ['Simple Weapons', 'Hand Crossbows', 'Longsword', 'Rapier', 'Shortsword'],
        'armor proficiencies': ['Light Armor'],
        'stat_rec': [8,14,13,12,10,15] 

    },
    'Blood Hunter': {
        'hit_die': 10,
        'skill number': 3,
        'skill proficiencies': ['Athletics', 'Acrobatics', 'Arcana', 'History', 'Insight', 'Investigation', 'Religion',
                                'Survival'],
        'tool proficiencies': ["Alchemist's supplies"],
        'weapon proficiencies': ['Simple Weapons', 'Martial Weapons'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields'],
        'stat_rec' : [14,12,13,15,10,8] 
    },
    'Cleric': {
        'skill number': 2,
        'hit_die': 8,
        'skill proficiencies': ['History', 'Insight', 'Medicine', 'Persuasion', 'Religion'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields'],
        'stat_rec': [13,8,14,10,15,12] 
    },
    'Druid': {
        'skill number': 2,
        'hit_die': 8,
        'skill proficiencies': ['Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion',
                                'Survival'],
        'tool proficiencies': ['Herbalism kit'],
        'weapon proficiencies': ['Club', 'Dagger', 'Darts', 'Javelins', 'Maces', 'Quarterstaff', 'Scimitars', 'Sickles',
                                 'Slings', 'Spears'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields', 'No armor or shields made of metal'],
        'stat_rec': [8,13,14,10,15,12] 
    },
    'Fighter': {
        'skill number': 2,
        'hit_die': 10,
        'skill proficiencies': ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation',
                                'Perception', 'Survival'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons', 'Martial Weapons'],
        'armor proficiencies': ['All Armor', 'Shields'],
        'stat_rec': [15,13,14,12,10,8] 
    },
    'Monk': {
        'skill number': 2,
        'hit_die': 8,
        'skill proficiencies': ['Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth'],
        'tool proficiencies': ["One type of Artisan's tools or one musical instrument"],
        'weapon proficiencies': ['Simple Weapons', 'Shortsword'],
        'armor proficiencies': [],
        'stat_rec': [8,15,13,10,14,12] 
    },
    'Paladin': {
        'skill number': 2,
        'hit_die': 10,
        'skill proficiencies': ['Athletics', 'Insight', 'Intimidation', 'Medicine', 'Persuasion', 'Religion'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons', 'Martial Weapons'],
        'armor proficiencies': ['All armor', 'Shields'],
        'stat_rec': [15,8,13,10,12,14] 
    },
    'Ranger': {
        'skill number': 3,
        'hit_die': 10,
        'skill proficiencies': ['Animal Handling', 'Athletics', 'Insight', 'Investigation', 'Nature', 'Perception',
                                'Stealth', 'Survival'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons', 'Martial Weapons'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields'],
        'stat_rec': [10,15,13,8,14,12] 
    },
    'Rogue': {
        'skill number': 4,
        'skill proficiencies': ['Acrobatics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception',
                                'Performance', 'Persuasion', 'Sleight of Hand', 'Stealth'],
        'tool proficiencies': ["Thieves' Tools"],
        'weapon proficiencies': ['Simple Weapons', 'Hand Crossbows', 'Longswords', 'Rapiers', 'Shortswords'],
        'armor proficiencies': ['Light Armor'],
        'hit_die': 8,
        'stat_rec': [8,15,12,14,10,13] 
    },
    'Sorcerer': {
        'skill number': 2,
        'skill proficiencies': ['Arcana', 'Deceptions', 'Insight', 'Intimidation', 'Persuasion', 'Religion'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light Crossbows'],
        'armor proficiencies': [],
        'hit_die': 6,
        'stat_rec': [8,13,14,10,12,15] 
    },
    'Warlock': {
        'skill number': 2,
        'skill proficiencies': ['Arcana', 'Deception', 'History', 'Intimidation', 'Investigation', 'Nature',
                                'Religion'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons'],
        'armor proficiencies': ['Light Armor'],
        'hit_die': 8,
        'stat_rec': [10, 12,14,13,8,15] 
    },
    'Wizard': {
        'skill number': 2,
        'skill proficiencies': ['Arcana', 'History', 'Insight', 'Investigation', 'Medicine', 'Religion'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light Crossbows'],
        'armor proficiencies': [],
        'hit_die': 6,
        'stat_rec': [8,14,13,15,10,12] 
    }
}
