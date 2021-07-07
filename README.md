# discountcode{
environment:
python 3.8.10
django 3.0


description:

A django project with the main feature is the availability of two custom cli commands

first command:
-mkvouchers:
    description: 
     this command creates a certain "amount" of random discount codes for a specified "group" of clients and outputs the result in a codes.json file
    
    specifications:
      this command expects two parameters the first one is an interger and is the "amount" of codes to be generate and the second parameter is the "group" name for whom the codes are generated
      the command generates unique code across all groups,the command outputs as stdout a string that indicates number of all codes created and number of all groups
      the generated codes and group name are placed in a dictionary where the name of the group is the key and the the codes are elements of a value list
      the dictionary is serialize appended to the codes.json and does not replace previous object
      
    usage :
      e.g:  python manage.py 10 vivoclients
      
      the above example will create 10 unique codes for a group with the name vivoclients and append it to jcode.son file as an object.
      
      
      
 second command:
 
 -checkcode:
      description:
          this command checks wether a code exists in the code.json file as a valid generated code.
          
       specifications:
       
          this command expects one parameter ,a string that is the code to be checked for validity.
          the command iterates over the values and returns the group name if found
          and if code not found in code.json file an stdout will display a message that code does not exist
          
        usage:
        e.g: python manage.py KHSYKt
        
        the above example will check in the code.json file ,if the code has been generated before and exists in the code.json file an stdout will indicate that code exist for the specific group name
        if the code does not exist in the code.json file and stdout will display that code does not exist.
    
