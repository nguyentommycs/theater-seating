# theater-seating

# Setup
Ensure you have Python installed. Ths was created in version 3.10.2 but other versions will probably work.
1. Clone this repo 
```sh
git clone https://github.com/nguyentommycs/theater-seating.git
``` 
2. cd into the folder containing app.py
```sh
cd C:\fakepath\theater-seating
``` 
3. Run the program by passing in the input file path. Use this command to run the sample input, or replace ```.\sampleinput``` with the full path to your input.
```sh
python app.py .\sampleinput.txt
```
# Assumptions
1. Middle rows are preferred to outer rows (i.e. rows E>F>D>G>C>H...). Earlier requests will receieve seats as close to middle row as possible.
2. While middle column seats (i.e. seats 10,11) may be slightly preferred to edge seats, the algorithm will assign seats left to right to better accomodate big groups.
3. Reservation groups will not be split up unless there are no remaining ways to fit them. If they are split, they will be split into as few groups as possible. For simplicity, we will simply break up the group into any available seats, going from the middle rows outwards. (This is probably not the best way, but is being done for the sake of time.)
4. If a reservation group is larger than the total amount of remaining seats, they will not be seated. (i.e. 18 people out of a group of 20 will not be seated if there are only 18 seats left)