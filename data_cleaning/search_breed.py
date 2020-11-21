from request_clean_intakes import clean_intake_data
 
dog_df = clean_intake_data()

search_breed = input("Breed name: ")

print("""
========================================
DOG SEARCH RESULTS
========================================
""")

find_dogs = []

for i in range(0, len(dogs_df)):
    if search_breed in dogs_df.iloc[i]['primary_breed'] or search_breed in dogs_df.iloc[i]['secondary_breed']:
        find_dogs.append(dogs_df.iloc[i])

found_dogs_df = pd.DataFrame(find_dogs)

print(found_dogs_df)