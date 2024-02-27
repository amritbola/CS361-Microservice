# CS361-Microservice
  How to Request Data from Microservice:
   - Prior to using the microservice, my partner must ensure that they have created an exercises.json file from the public domain dataset found on https://github.com/wrkout/exercises.json. After downloading the public repository, they can run the script 'npm run build:json' which will create a JSON file with all of the exercises locally.
   - The imports required for this microservice are JSON and random.
   - They will need to import the function, exercies_randomizer() from my microservice to their client side program. 
   - Depending on my partner's user interface, they can either rely on user input or a button to send a request to the my microservice.
   - If button is pushed or user input is sent: example call can be print(exercise_randomizer()).

  How to Receive Data from Microservice:
  - First, the function, exercise_randomizer() will be called from my partner's client side program.
  - The function exercise_randomizer() will generate a random number in the range (0, 872) which is the length of the exercise objects in the exercises dataset.
  - The generated random number will be used as an index for the dataset of exercises.
  - Once a random exercise is accessed using the random number, exercise_randomizer() will return the exercise JSON object.
  - My partner's client side program will receive the exercise data from exercise_randomizer() and display it out to their users.
![image](https://github.com/amritbola/CS361-Microservice/assets/97146266/9702e2d6-94aa-47d3-96e9-6b4ac1a0e55b)
