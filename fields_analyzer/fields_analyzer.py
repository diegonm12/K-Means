
##this is where all the data is preprocessed
import numpy as np

def select_fields_to_analyze(json_data):
    json_data_length = len(json_data)
    json_keys_array = list(json_data[0].keys())

    array_to_analyze = []     # all elements from a key in one array
    approved_fields_dict = {} # this is a dictionary with the fields and the values approved after the analyze.
    for key in json_keys_array:
        for index_json_data in range(len(json_data)):
            if key == 'pid':
                array_to_analyze.append(str(json_data[index_json_data][key]))
            else:
                array_to_analyze.append(json_data[index_json_data][key])
        # after put all elements from a key in an array we analyze the len
        set_to_be_compared = set(array_to_analyze) # this tuple is going to be compared with the len of the json_data
        number_of_distinct_values = len(set_to_be_compared)
        diff = json_data_length - number_of_distinct_values
        diff_percentage = (diff/json_data_length) * 100
        if(type(array_to_analyze[0]) is int): #**********YOU SHOULD JUSTIFY THIS*****************
            approved_fields_dict[key] = array_to_analyze # if the diff_percentage is greater than 20% it is a categorical field.
        elif (diff_percentage > 20):
            approved_fields_dict[key] = array_to_analyze
        array_to_analyze = []
    # In these lines we change the characters approved to be analyzed into number, using the ASCII representation, using ord() function
    for key in approved_fields_dict:
        if(type(approved_fields_dict[key][0]) is str):
            for element in range(len(approved_fields_dict[key])):
                approved_fields_dict[key][element] = ord(approved_fields_dict[key][element])
    values_from_dict = np.array(list(approved_fields_dict.values()))

    #Here we create all the elements or samples to be analyzed, one array from the matrix represents an entity
    array_to_return = [[] for _ in range(len(values_from_dict[0]))]
    for row in range(len(values_from_dict)):
        for column in range(len(values_from_dict[row])):
            array_to_return[column].append(values_from_dict[row][column])
    return np.array(array_to_return) # here we have all the attributes from the entities in every array of the matrix


