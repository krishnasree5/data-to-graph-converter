from matplotlib.pyplot import *


def convert_bargraph():   #converts to bar graph
    
    labels = input('\t\t\t\tEnter labels separated by commas').split(',')
    frequency = list(map(int,input('\t\t\t\tEnter frequency separated by commas').split(',')))
    
    chart_length = int(input('\t\t\t\tSelect the length of the chart'))
    chart_width = int(input('\t\t\t\tSelect the width of the chart'))
    
    x_label = input('\t\t\t\tEnter heading for x axis')
    y_label = input('\t\t\t\tEnter heading for y axis')
    chart_title = input('\t\t\t\tEnter title for the chart')
    
    figure(figsize=(chart_width,chart_length))
    # to set the dimensions of bargraph
    
    plot = bar(labels,frequency,width=0.5)
    
    for frequency in plot:
        print(frequency)
        h = frequency.get_height()
        W = frequency.get_width()
        X = frequency.get_x()
        Y = frequency.get_y()
        text(X+W/2, 1.002*h, int(h))
    
    xlabel(x_label)  #heading for x axis
    ylabel(y_label)  #heading for y axis
    title(chart_title)  #title of bargarph
    
    show()
    
    exit_function()
    
    
def convert_histogram():  #converts to histogram
    
    limits = list(map(int,input("\t\t\t\tEnter lower limits and include the last upper limit").split(',')))
    frequency = list(map(int,input('\t\t\t\tEnter frequency separated by commas').split(',')))
    
    chart_length = int(input('\t\t\t\tSelect the length of the chart'))
    chart_width = int(input('\t\t\t\tSelect the width of the chart'))
    
    x_label = input('\t\t\t\tEnter heading for x axis')
    y_label = input('\t\t\t\tEnter heading for y axis')
    chart_title = input('\t\t\t\tEnter title for the chart')
    
    figure(figsize = (chart_width,chart_length))
    # to set the dimensions of histogram
    hist(limits[:-1], bins=limits, weights=frequency, edgecolor='black')
    
    xlabel(x_label)          #heading for x axis
    ylabel(y_label)          #heading for y axis
    title(chart_title)        #heading for histogram
    
    show()
    
    exit_function()
    
    
def convert_piechart():   #to convert to piechart
    
    labels = input('\t\t\t\tEnter labels separated by commas').split(',')
    #labels are for headings of each slice in piechart
    values = list(map(int,input('\t\t\t\tEnter values separated by commas').split(',')))
    #the value for each slice

    pie(values, labels = labels)
    chart_title = input('\t\t\t\tEnter title for the chart')
    title(chart_title)
    
    show()
    
    exit_function()
    

def converter(choice):    #takes the userchoice and acts accordingly
    
    if choice == 1:
        convert_bargraph()
    elif choice == 2:
        convert_histogram()
    else:
        convert_piechart()
        

def user_choice():   #takes the user choice 
    
    display_string = '''\t\t\t\tChoose one of the below Options!!!
    \t\t\t\t1)Convert to Bargraph
    \t\t\t\t2)Convert to Histogram
    \t\t\t\t3)Convert to Piechart'''

    print(display_string)
    
    choice = int(input('\t\t\t\tChoice: '))
    while choice not in [1,2,3]:
        print('\t\t\t\tEnter valid choice')
        choice = int(input('\t\t\t\tChoice: '))
    
    converter(choice)
    

def exit_function():    #asks the user if he wants to exit or not
    
    option = input('\t\t\t\tDo you want to continue? y/n')
    
    while option not in ['y','n','Y','N']:
        print('\t\t\t\tEnter valid choice')
        option = input('\t\t\t\tChoice: y/n')
    
    if option in ['n','N']:
        print('\t\t\t\tThank You!')
    else:
        user_choice()
    
#main program
print('Data to Graph Converter'.center(88,'*'))
print()
print()
print()

user_choice()
