#!/usr/bin/python3  
import sys  

def main():  
    arguments = sys.argv[1:]  
    num_arguments = len(arguments)  

    if num_arguments == 0:  
        print("0 arguments.")  
    else:  
        argument_label = "argument" if num_arguments == 1 else "arguments"  
        print(f"{num_arguments} {argument_label}:")  
        
        for i in range(num_arguments):  
            print(f"{i + 1}: {arguments[i]}")  

if __name__ == '__main__':  
    main() 
