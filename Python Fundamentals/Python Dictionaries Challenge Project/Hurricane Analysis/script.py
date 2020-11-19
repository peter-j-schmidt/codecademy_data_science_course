# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def damages_to_float(list):
  new_list = []
  for item in list:
    if item == 'Damages not recorded':
      new_list.append(item)
    else:
      if 'M' in item:
        item = item.replace('M', '')
        new_item = float(item) * 1000000
        new_list.append(new_item)
      elif 'B' in item:
        item = item.replace('B', '')
        new_item = float(item) * 1000000000
        new_list.append(new_item)
  return new_list


new_damages = damages_to_float(damages)
print(new_damages)

# write your construct hurricane dictionary function here:

def list_to_dictionary(names, months, years, max_stutained_winds, areas_affected, damages, deaths):
  hurricane_dict = {}
  for i in range(34): 
    hurricane_dict[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damages[i], "Deaths": deaths[i]}
  return hurricane_dict

new_hurricane_dict = list_to_dictionary(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths)

print(new_hurricane_dict)



# write your construct hurricane by year dictionary function here:

def list_to_dictionary_by_year(names, months, years, max_stutained_winds, areas_affected, damages, deaths):
  hurricane_dict = {}
  for i in range(34): 
    hurricane_dict[years[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damages[i], "Deaths": deaths[i]}
  return hurricane_dict

new_hurricane_dict_by_year = list_to_dictionary_by_year(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths)

print(new_hurricane_dict_by_year)



# write your count affected areas function here:

def aff_areas_by_count(big_list):
  new_list = []
  new_dict = {}
  for list in big_list:
    for item in list:
      new_list.append(item)
  for item in new_list:
    count = new_list.count(item)
    new_dict[item] = count
  return new_dict

aff_area_dict = aff_areas_by_count(areas_affected)

print(aff_area_dict)




# write your find most affected area function here:

def most_affected_area(dictionary):
  max_area = ''
  max_area_count = 0
  for key, value in dictionary.items():
    if value > max_area_count:
      max_area_count = value
      max_area = key
  max_tuple = (max_area, max_area_count)
  return max_tuple

max_area_info = most_affected_area(aff_area_dict)

print(max_area_info)




# write your greatest number of deaths function here:

def max_death(dictionary):
  max_deaths_name = ''
  max_deaths = 0
  for key, value in dictionary.items():
    deaths = value.get("Deaths")
    if deaths > max_deaths:
      max_deaths = deaths
      max_deaths_name = key
  return (max_deaths_name, max_deaths)

max_death_hurricane = max_death(new_hurricane_dict)
print(max_death_hurricane)



# write your catgeorize by mortality function here:

def find_mortality(dictionary):
  mortality = {}
  for key, value in dictionary.items():
    deaths = value.get('Deaths')
    if deaths == 0:
      mortality[key] = 0
    elif deaths > 0 and deaths <= 100:
      mortality[key] = 1
    elif deaths > 100 and deaths <= 500:
      mortality[key] = 2
    elif deaths > 500 and deaths <= 1000:
      mortality[key] = 3
    elif deaths > 1000 and deaths <= 10000:
      mortality[key] = 4
  return mortality

mortality_ratings = find_mortality(new_hurricane_dict)
print(mortality_ratings) 





# write your greatest damage function here:

def max_damage(dictionary):
  max_damage_name = ''
  max_damage = 0
  for key, value in dictionary.items():
    damage = value.get("Damage")
    if damage == 'Damages not recorded':
      continue
    else:
      if damage > max_damage:
        max_damage = damage
        max_damage_name = key
  return (max_damage_name, max_damage)

max_damage_hurricane = max_damage(new_hurricane_dict)
print(max_damage_hurricane)





# write your catgeorize by damage function here:

def find_damage_level(dictionary):
  damage_rating = {}
  for key, value in dictionary.items():
    damage = value.get('Damage')
    if damage == 'Damages not recorded':
      continue
    elif damage == 0:
      damage_rating[key] = 0
    elif damage > 0 and damage <= 100000000:
      damage_rating[key] = 1
    elif damage > 100000000 and damage <= 1000000000:
      damage_rating[key] = 2
    elif damage > 1000000000 and damage <= 10000000000:
      damage_rating[key] = 3
    elif damage > 10000000000 and damage <= 50000000000:
      damage_rating[key] = 4
  return damage_rating

damage_scale = find_damage_level(new_hurricane_dict)
print(damage_scale) 






