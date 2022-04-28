def display_main_menu():
    print("Enter some numbers separated by commas(e.g. 5,76,32)")

def get_user_input():
    x = input("Enter your numbers: ")
    print("\n")
    list = x.split(",")
    print('list: ', list)
    newList = []
    #convert each item to int type
    for i in list:
        newList.append(int(i))
    print("Sum = ", sum(newList))
    return newList

def calc_average_temperature(num_list):
    avg = sum(num_list)/len(num_list)
    print("The average is: ", avg)

def calc_min_max_temperature(num_list):
    print("The minimum temperature is: ", min(num_list))
    print("The maximum temperature is: ", max(num_list))

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average_temperature(num_list)
    calc_min_max_temperature(num_list)

if __name__ == "__main__":
    main()