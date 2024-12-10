print("Welcome to the Data Analyzer and Transformer Program!")

is_on=True
arr=[]

# operation 1
def input_data():
    """
        This function will take the element value of array and store it in the array
    """
    print(input_data.__doc__)
    global arr
    numbers=input("\nEnter data for a 1D array (seprated by spaces):")
    for i in numbers.split(' '):
        arr.append(int(i))
    print("\nData has been stored successfully!")

# operation 2
def display_data_summary():
    """
        This function will give you data summary of the array like, total elements, maximum and minimum value in the array, sum of all values of the array and average value of the array
    """
    print(display_data_summary.__doc__)
    if arr!=[]:
        print(f"Data summary:\n- Total elements: {len(arr)}\n- Minimum value: {min(arr)}\n- Maximum value: {max(arr)}\n- Sum of all values: {sum(arr)}\n- Average value: {sum(arr)/len(arr)}")
    else:
        print("\nYour array is empty!")

# operation 3
def factorial(num):
    """
        this is recursive function, it will find the factorial of given number in recursive way
    """
    print(factorial.__doc__)
    if num<=1:
        return 1
    else:
        return num*factorial(num-1)

# operation 4
"""
this is lambda function, which filter out the above value of threshold value, which is input by user 
"""
filter_values=lambda num,lst:lst>num
print(filter_values.__doc__)

# operation 5
def sort_data():
    """
        this function will sort the array in ascending or descending order using built-in global function sorted() 
    """
    print(sort_data.__doc__)
    if arr!=[]:
        order=int(input("\nChoose sorting option:\n1. Ascending\n2. Descending\nEnter the your choice:"))
        if order==1:
            arr1=sorted(arr)
            print("\nSorted Data in Ascending Order:")
            for i in arr1:
                print(f"{i} ",end=" ")
        elif order==2:
            arr2=sorted(arr,reverse=True)
            print("\nSorted Data in Descending Order:")
            for i in arr2:
                print(f"{i} ",end=" ")
        else:
            print("\nYou entered the wrong order option!")
    else:
        print("\nYour array is empty!")

# operation 6
def show_statistics():
    """
        this function will return the summary of the array including maximum and minimum value, sum of all values, average value of the array
    """
    print(show_statistics.__doc__)
    if arr!=[]:
        return ["\nDataset statistics:\n",f"-Minimum value:{min(arr)}",f"-Maximum value:{max(arr)}\n-Sum of all values: {sum(arr)}\n-Average value:{sum(arr)/len(arr)}"]
    else:
        print("\nYour array is empty!")


while is_on:
    choice=int(input("\n\nMain Menu:\n1. Input Data\n2. Display Data Summary (Built-in functions)\n3. Calculate Factorial (Recursion)\n4. Filter Data by Threshold (Lambda Function)\n5. Sort Data\n6. Display Dataset Statistics (Return Multiple Values)\n7. Exit Program\nPlease enter your choice:"))
    
    if choice==1:
        input_data()
    
    elif choice==2:
        display_data_summary()
    
    elif choice==3:
        number=int(input("\nEnter a number to calculate its factorial:"))
        a=factorial(number)
        print(f"\nFactorial of {number} is: {a}")
    
    elif choice==4:
        if arr!=[]:
            num=int(input("\nEnter a threshold value to filter out data above this value:"))
            filter_data=[]
            for i in arr:
                if filter_values(num,i):
                    filter_data.append(i)
            print(f"\nFiltered Data (values >= {num})")
            for i in filter_data:
                print(f"{i} ",end=" ")
        else:
            print("\nYour array is empty!")
    
    elif choice==5:
        sort_data() 
    
    elif choice==6:
        dataset=show_statistics()
        if arr!=[]:
            for i in dataset:
                print(i)  
    
    elif choice==7:
        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
        is_on=False
    
    else:
        print("\nYou are exit from the program!")