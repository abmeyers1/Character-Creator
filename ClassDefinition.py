import random
import backgrounddicts
import charclasses
import heritage


class Character:
    def __init__(self, char_name, player_name, char_class, char_back, char_heritage, stats):
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
        self.stats = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        self.roll_stats(stats)
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
        stats_str = ', '.join(self.stats)

        # Return description of character
        
        return f'Your name is {self.player_name} \nYour character is {self.char_name}, ' \
               f'the {self.heritage} {self.charclass} ' \
               f'\nYour background is {self.background}\n' \
               f'Skills:\t {prof_str}\n' \
               f'Tools:\t{tool_str}\nArmor:\t{armor_str}\nWeapons:\t{weapon_str}\n' \
               f'Stats: {stats_str}\n' \
               f'Strength: {self.stats["STR"]} Dexterity: {self.stats["DEX"]} \nConstitution: {self.stats["CON"]} Intelligence: {self.stats["INT"]} \nWisdom: {self.stats["WIS"]} Charisma: {self.stats["CHA"]}'

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




    def roll_stats(self, stats):
        # uses random to roll for stats
        if stats == 'Random':
            # Roll for stats randomly
            print("RANDOM ROLLS!")
            saved_rolls = []
            for i in range(6):
                roll = []
                while len(roll)<4:
                    roll.append(random.randint(1,6))
                roll.remove(min(roll))
                saved_rolls.append(sum(roll))
            print("Rolls: " + str(saved_rolls))
            
            # assign rolls to stats
            for key, value in self.stats.items():
                # print(f"Key: {key}")
                temp = random.choice(saved_rolls)
                self.stats[key] = temp 
                saved_rolls.remove(temp)



        #  Need to account for Racial bonuses here before final printout:


        # Print out final stats:
            # print('Your character\'s stats are: \nSTR: ' + str(self.stats['STR']) + '\nDEX: ' + str(self.stats['DEX']) +
            #   '\nCON: ' + str(self.stats['CON']) + '\nINT: ' + str(self.stats['INT']) + '\nWIS: '
            #   + str(self.stats['WIS']) + '\nCHA: ' +str(self.stats['CHA']) )
        else:
            print("RECOMMENDED ROLLS!")
            
            print(backgrounddicts.bgds[self.background])
            self.stats['STR'] = charclasses.classes[self.charclass]['stat_rec'][0]
            self.stats['DEX'] = charclasses.classes[self.charclass]['stat_rec'][1]
            self.stats['CON'] = charclasses.classes[self.charclass]['stat_rec'][2]
            self.stats['INT'] = charclasses.classes[self.charclass]['stat_rec'][3]
            self.stats['WIS'] = charclasses.classes[self.charclass]['stat_rec'][4]
            self.stats['CHA'] = charclasses.classes[self.charclass]['stat_rec'][5]


            print('Your character\'s stats are: \nSTR: ' + str(self.stats['STR']) + '\nDEX: ' + str(self.stats['DEX']) +
              '\nCON: ' + str(self.stats['CON']) + '\nINT: ' + str(self.stats['INT']) + '\nWIS: '
              + str(self.stats['WIS']) + '\nCHA: ' +str(self.stats['CHA']) )
        
        # Add heritage bonuses to stats
        print(type(heritage.heritages[self.heritage]['stat_bonus']))
        for key, value in heritage.heritages[self.heritage]['stat_bonus'].items():
            self.stats[key] += value





if __name__ == '__main__':
    jeff=Character('Rognar the Blue','Jefft Stork', 'Bard','Acolyte', 'Human',"Recommended")
    print(jeff)