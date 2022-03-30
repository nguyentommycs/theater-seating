import sys
import pathlib
from datetime import datetime
def file_to_arr(file_path):
    """
    Returns: array containing each seating request 
    
    This function converts seating requests from a text request
    to an array containing ints representing each request
    
    Parameter file_path: file path containing seating requests
    Precondition: valid file path

    """
    file = open(file_path,"r")
    requests = []
    line = file.readline()
    while line!="":
        requests.append(int(line[5:]))
        line = file.readline()
    file.close()
    return requests
        

def result_to_file(result):
    """
    Returns: file path
    
    This function writes the result string to a new text file 
    and returns the path to the file. The file will include the 
    date and time the results were generated
    
    Parameter result: string containing seating assignments
    Precondition: valid string


    """
    #label file with date and time
    now = datetime.now()
    dt_str = now.strftime("%m-%d-%Y %H-%M-%S")
    file = open("results "+dt_str+".txt","w")
    file.write(result)
    return str(pathlib.Path().resolve()) + "\\results " +dt_str+".txt"
    
    




# grab file path from arguments
file_path = str(sys.argv[1])

#convert to ints representing requests
requests = file_to_arr(file_path)

NUM_TO_ROW = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J"}
ROW_CAPACITY = 20
NUM_ROWS = 10
BUFFER = 3
row_caps = [ROW_CAPACITY]*NUM_ROWS #capacity of each row, index 0 corresponds to row A
total_cap = ROW_CAPACITY*NUM_ROWS #total amount of seats left
seating_str=""
row_pref = []
#generate correct preferential order of rows; middle rows first, then outer rows
for i in range((NUM_ROWS-1)//2,-1,-1):
    row_pref.append(i)
    row_pref.append(NUM_ROWS-i-1)


for i in range(len(requests)):
    #keep going until no seats left (or no more requests)
    if total_cap<=0:
        break
    request = requests[i]

    if total_cap>=request:
        completed_request = False

        #generate the string for the result
        temp_str = "\nR"
        if i<99:
            temp_str = temp_str+"0"
        if i<9:
            temp_str = temp_str+"0"
        temp_str = temp_str + str(i+1) + " "

        for row in row_pref:
            row_cap = row_caps[row]

            if row_cap>=request:
                #we can fit the entire request in one row
                #append seats to the result string
                for j in range(request):
                    if j == 0:
                        temp_str = temp_str + str(NUM_TO_ROW[row]) + str(j+ROW_CAPACITY-row_cap+1)
                    else:
                        temp_str = temp_str +","+ str(NUM_TO_ROW[row]) + str(j+ROW_CAPACITY-row_cap+1)
                

                #update our total and row by row capacity
                total_cap = total_cap - min(request+BUFFER,row_cap)
                row_caps[row]=row_cap-(request+BUFFER)
                completed_request=True
                break
        
        #if we get here, the group can't fit as one whole unit, but they
        #can fit if they get broken up
        if not completed_request:
            for row in row_pref:
                row_cap = row_caps[row]
                if row_cap>0:

                    for j in range(min(request,row_cap)):
                        temp_str = temp_str +","+ str(num_to_row[row]) + str(j+ROW_CAPACITY-row_cap+1)
                    #update our total and row by row capacity
                    total_cap = total_cap - min(request+BUFFER,row_cap)
                    row_caps[row]=row_cap-(request+BUFFER)
                    request = request - row_cap
                if request <=0:
                    break
            #remove an extra comma
            temp_str = temp_str[0:6]+temp_str[7:]
        seating_str=seating_str+temp_str
            


#remove extra newline at beginning of str
if seating_str!="":
    seating_str =seating_str[1:]
print(seating_str)
print(result_to_file(seating_str))