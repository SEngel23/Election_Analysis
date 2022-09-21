counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])
if counties[3] !='Jefferson':
    print(counties[2])

counties = ["Arapahoe", "Denver", "Jefferson"]

if "El Paso" in counties:
    print("El Paso in the list of counties.")

else:
    print("El Paso is not in the list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")

else: 
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")

else:
    print("Arapahoe is in the list of counties.")

for county in counties:
    print(county)

numbers = [0,1,2,3,4]

for num in numbers:
    print (num)

for num in range(5):
    print (num)
# this will produce the same results as numbers

for i in range(len(counties)):

    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)
    #this also yields the same results, but pulls the keys or keyword and applying county as the variable

for voters in counties_dict.values():
        print(voters)
    # remember, conties_dict = {"keys1":values1, "keys2": values2}
    #Here we are searching for values and applying voters as the variable name

# another format to get the key value is using dictionary_name[key]

for county in counties_dict:
    print(counties_dict[county])

#another way to get the values of a key is using the get() function
for county in counties_dict:
    print(counties_dict.get(county))

#to get the key-value pair infromation, use the items() function
#for key, value in dictionary_name.items()
    #print(key, value)
for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters")



voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['registered_voters'])
#alternative formula to print the county name from each dictionary
for county_dict in voting_data:
    print(county_dict['county'])

# F-strings

for county, voters in counties_dict.items():
    print(county+ "County has" + str(voters) + " registered voters.")

# Print F-string version of this
    print(f"{county} county has {voters} registered voters.")

# multi f-string example

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county, voters in voting_data():
    print(f"{county} county has {voters} registered voters.")
    #This code is not finished - not sure how to get this to operate correctly. goal is to have the f-string print from the voting data