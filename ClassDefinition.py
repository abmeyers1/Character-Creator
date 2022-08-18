import random
import backgrounddicts
import charclasses
import heritage


class Character:
    def __init__(self, char_name, player_name, char_class, char_back, char_heritage):
        self.char_name = char_name
        self.player_name = player_name
        self.heritage = char_heritage
        self.charclass = char_class
        self.background = char_back
        self.class_skill_number = charclasses.classes[char_class]['skill number']
        self.heritage_skill_number = 0
        self.skill_proficiencies = []
        self.tool_proficiencies = []
        self.weapon_proficiencies = []
        self.armor_proficiencies = []
        self.set_proficiencies()
        # self.stats = {}
        # self.roll_stats()
        # self.abilities = []
        # self.abilities.append(self.background['feature'])
        # self.gear = {}
        # self.gear = (self.background['equipment'])

    def __repr__(self):

        # Create strings for proficiencies
        prof_str = ', '.join(self.skill_proficiencies)
        tool_str = ', '.join(self.tool_proficiencies)
        armor_str = ', '.join(self.armor_proficiencies)
        weapon_str = ', '.join(self.weapon_proficiencies)

        # Return description of character
        return f'Your name is {self.player_name} \nYour character is {self.char_name}, ' \
               f'the {self.heritage} {self.charclass} ' \
               f'\nYour background is {self.background}\n' \
               f'Skills:\t {prof_str}\n' \
               f'Tools:\t{tool_str}\nArmor:\t{armor_str}\nWeapons:\t{weapon_str}'

    def set_proficiencies(self):

        # Look at background, class, heritage for tool/armor/weapon profs
        count = 0   # Used to skip adding class skills twice
        for source in [charclasses.classes[self.charclass], backgrounddicts.bgds[self.background],
                       heritage.heritages[self.heritage]]:
            if len(source['skill proficiencies']) != 0:
                # count = 0 when we're looking at class skills, need to skip
                if count != 0:
                    for item in source['skill proficiencies']:
                        self.skill_proficiencies.append(item)
            if len(source['tool proficiencies']) != 0:
                for item in source['tool proficiencies']:
                    self.tool_proficiencies.append(item)

            if len(source['armor proficiencies']) != 0:
                for item in source['armor proficiencies']:
                    self.armor_proficiencies.append(item)

            if len(source['weapon proficiencies']) != 0:
                for item in source['weapon proficiencies']:
                    self.weapon_proficiencies.append(item)
            count += 1

        # Sort each prof list
        self.skill_proficiencies.sort()
        self.tool_proficiencies.sort()
        self.armor_proficiencies.sort()
        self.weapon_proficiencies.sort()

        # Update skill number
        try:
            self.class_skill_number += heritage.heritages[self.heritage]['skill number']
        except KeyError:
            pass
        # print('Class skill number:\t' + str(self.class_skill_number))
        # print('Heritage skill number:\t' + str(self.heritage_skill_number))




    def roll_stats(self):
        # uses random to roll for stats
        saved_rolls = []
        for i in range(6):
            roll = []
            while len(roll)<4:
                roll.append(random.randint(1,6))
            # print(roll)
            roll.remove(min(roll))
            # print(roll)
            saved_rolls.append(sum(roll))
        print(f' You rolled:\t{saved_rolls}')

        # Ask player to create order of stats
        statlist=['STR','DEX','CON','INT','WIS','CHA']
        print('What is your character\'s highest stat?\n')

        # List all stats, assign one at a time in decreasing order
        while len(statlist) != 1:
            for index in range(len(statlist)):
                print(f'{index+1}:\t{statlist[index]}')

            # User selects stat to assign highest number to
            choice = (input('Enter a number:\t'))

            # Confirm that entry is number in range
            while choice not in [x for x in range(1,len(statlist)+1)]:
                # If they entered abbreviation, let it pass
                if choice in statlist:
                    choice = int(statlist.index(choice) + 1)
                try:
                    choice = int(choice)
                except ValueError:
                    choice = input('Enter a number to choose your stat:\t')
                    continue
                if choice < 1 or choice > len(statlist):
                    choice = input('Enter a number to choose your stat:\t')
                    continue


            # Assign highest roll to chosen stat, and remove roll & stat from lists
            self.stats[statlist[choice - 1]] = max(saved_rolls)
            del statlist[choice - 1]
            saved_rolls.remove(max(saved_rolls))

            # Loop for rest of stats until 1 left
            print(f"Stats remaining: {statlist}")
            print(f"Rolls remaining: {saved_rolls}")

        # Assign remaining stat
        self.stats[statlist[0]] = saved_rolls[0]


        #  Need to account for Racial bonuses here before final printout:


        # Print out final stats:
        print('Your character\'s stats are: \nSTR: ' + str(self.stats['STR']) + '\nDEX: ' + str(self.stats['DEX']) +
              '\nCON: ' + str(self.stats['CON']) + '\nINT: ' + str(self.stats['INT']) + '\nWIS: '
              + str(self.stats['WIS']) + '\nCHA: ' +str(self.stats['CHA']) )

        # print(self.stats)





if __name__ == '__main__':
    jeff=Character('Rognar the Blue','Jefft Stork', 'Paladin','Acolyte', 'Human')
    print(jeff)
