# Project2-PetSelect

Key objectives/desired end results:
The user inputs information about themselves and the app recommends a pet that would fit their lifestyle, and then connects the user to a pet that is available for adoption. 

Two types of data: Existing data (static) from the Shelter API and user inputted data that we collect in our own database. 

Possible: Refresh the data daily from the Shelter API (they update their data hourly)?

### Data we want to utilize:

Animal Shelter Intakes: https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Intakes/wter-evkm

Animal Shelter Outtakes:
https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Outcomes/9t4d-g238

Dog Breeds API:
https://dog.ceo/dog-api/

Other Animal Shelter Info: 
https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Dog-Intakes-Chart/r5dg-6cvf

Austin Pets Alive Resource:
https://www.austinpetsalive.org/adopt/dogs


### Routes:
* Landing page
* Input a new user
* User questionnaire/Search for dog that’s best for me 
* Shelter inventory grouped by pet type/energy level/etc.
* Fun kid page with pics of cute dogs
* Breed info page
* Visuals/Analytics/Interesting Findings
* Documentation on code, cool technical things we did when building the app


### Visuals/Analytics:
* Interactive Plotly
* Which breeds are searched
* Which breeds are most available
* How long are dogs in the shelter (by breed or age)



### Notes from Ed:
* If possible, query the shelter API each day to make sure there’s always current data in the system. Add anything that’s been added since the last time we pulled the query, and also remove anything on the outtakes list. Or we may need to just duplicate their database and translate/clean it up, depending on the quality of the API.  
* He’d normally recommend SQL, but if for some reason the incoming data is inconsistent then maybe use NoSQL (i.e. web scraping).
* Maybe the user could submit a picture of a dog and find a dog that looks similar to it. 
* Possibly project 3 idea: Train the ML to train it to do the classification work, then use it in the web app so the ML model identifies the type of dog it is. 
* Do an authentication layer. 
* Give an option so the user gets an alert if a specific type of breed is added. 
* Dogs get re-surrendered to the shelter - find that and do something with it. 
* Have the users query the database ad hoc rather than creating and saving users in a database.
* Keep the algorithm simple. Do branching if/then logic. Possibly use “cosine similarity and compare to vectors”. Using numerical measures would be easiest if possible - match the dog breed to a number. Start with the dumbest algorithm and then build it up and refine it over time to make it better. 
* Deploy when we can as soon as possible. Deploy many times throughout the project. We can deploy this one on heroku probably. 
* Everything will need to work in parallel as much as possible. A lot is going to hinge on the initial database creation. Work on the routes that won’t depend on the main database while others are working on the database, or structuring the app, or etc. Get the database up as fast as possible - create the schema, create the database. He’d recommend sqlalchemy, but noSQL is also possible. Make a decision ASAP. Don’t worry about the updating yet - just get some data in the database so we can work on the other parts (CRUD functions, query functions, visuals, analytics, etc.). Try to plan this so as much gets done simultaneously as possible.



### Algorithm:

* Dog “personality type” algorithm (sample/conceptual)


