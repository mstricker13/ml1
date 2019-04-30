import matplotlib.pyplot as plt
import os
import numpy as np

def load_csv(csv_location):
    """
    Creates a tuple of two lists for females and males. The first list in the tuple contains the height and second list
    the weight. The indexes of the values correspond to each other. E.g. values at index 2 correspond to person number 2
    """
    female_data, male_data = (list(), list()), (list(), list())
    #gets the content of the file
    with open(csv_location, 'r') as file:
        text = file.read()
    #iterate through each row
    for row in text.split('\n'):
        #if we have an empty line break out of the loop
        if row == '':
            break
        #seperate values by ','
        values = row.split(',')
        #convert values from string to float and ignore the first ID value
        values = [float(value) for value in values[1:]]
        #if it is male, add values to male tuple
        if values[2] == 1:
            male_data[0].append(values[0])
            male_data[1].append(values[1])
        #else add values to female tuple (assumes correct set where 1 and -1 are the only values)
        #did you really just assume that there are only 2 genders?
        else:
            female_data[0].append(values[0])
            female_data[1].append(values[1])
    return female_data, male_data


def plot_data(female_data, male_data):
    """
    plots the data given for females and males in the format defined load_csv. Will save the plot in output folder
    :return:
    """
    #plots the male points
    plt.plot(male_data[0], male_data[1], 'bo')
    #plots the female points
    plt.plot(female_data[0], female_data[1], 'ro')
    #define some labelnames
    plt.title('Disneyland Population')
    plt.xlabel('Height')
    plt.ylabel('Weight')
    plt.legend(['Female', 'Male'], loc='upper left')
    # plt.show()
    #save plot
    save_location = os.path.join('output', 'population.png')
    if os.path.exists(save_location):
        os.remove(save_location)
    plt.savefig(save_location)
    plt.close()


def plot_data_with_line(female_data, male_data, line_data):
    """
    similar to plot_data. It just adds a line defined by line_data info
    """
    # plots the male points
    plt.plot(male_data[0], male_data[1], 'bo')
    # plots the female points
    plt.plot(female_data[0], female_data[1], 'ro')
    w = np.array(line_data[0])
    b = line_data[1][4]
    allHeight, allWeight = male_data[0] + female_data[0], male_data[1] + female_data[1]
    result_list_x, result_list_y = list(), list()
    for x1, x2 in zip(allHeight, allWeight):
        x = np.array([x1, x2])
        result = w * x + b
        result_list_x.append(result[0])
        result_list_y.append(result[1])
    plt.plot(result_list_x, result_list_y, 'k-')
    # define some labelnames
    plt.title('Disneyland Population')
    plt.xlabel('Height')
    plt.ylabel('Weight')
    plt.legend(['Male', 'Female', 'Hyperplane'], loc='upper left')
    # plt.show()
    # save plot
    save_location = os.path.join('output', 'population_lines.png')
    if os.path.exists(save_location):
        os.remove(save_location)
    plt.savefig(save_location)
    plt.close()


if __name__ == '__main__':

    #location to the csv file which contains the data
    csv_location = os.path.join('data', 'DWH_Training.csv')
    #load the female and male data in a csv file
    female_data, male_data = load_csv(csv_location)
    #plot the loaded data
    plot_data(female_data, male_data)
    w = [0.576, 0.047]
    b = [-103, -102, -101, -100, -99]
    line_data = (w, b)
    plot_data_with_line(female_data, male_data, line_data)
