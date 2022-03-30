# theater-seating

<a name="project-setup"></a>
# Project Setup

1. Clone this repo 
```sh
git clone https://github.com/nguyentommycs/theater-seating.git
``` 
2. create a virtual environment
```sh
python -m venv env
``` 
3. (a) For Windows, activate the virtual environment<br />
```sh
env\Scripts\activate.bat
```
3. (b) For Linux, activate the virtual environment<br />
```sh
source env/bin/activate
```
4. Run the program by passing in the input file path. Use this command to run the sample input, or replace ```.\sampleinput ``` with the full path to your input.
```sh
python app.py .\sampleinput
```
# Assumptions
1. Middle rows are preferred to outer rows (i.e. rows E>F>D>G>C>H...). Earlier requests will receieve seats as close to middle row as possible.
2. While middle column seats (i.e. seats 10,11) may be slightly preferred to edge seats, the algorithm will assign seats left to right to better accomodate big groups.
3. Reservation groups will not be split up unless there are no remaining ways to fit them. If they are split, they will be split into as few groups as possible. For simplicity, we will value fewer split groups over more evenly split groups (i.e. a group of 9 would be split 8-1 rather than 3-3-3).
4. If a reservation group is larger than the total amount of remaining seats, they will not be seated. (i.e. 18 people out of a group of 20 will not be seated if there are only 18 seats left)