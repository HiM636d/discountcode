from django.core.management.base import BaseCommand
from voucher.models import Code,Groups
from django.utils.crypto import get_random_string
import json
################## creating custom cli command to generate a certain amount of vouchers for a specific group##########

class Command(BaseCommand):
    help='makes discount voucher-codes for groups ** takes amount of vouchers as first argument** name of group as second argument'

### defining the arguments expected by the command first argument is an intiger and is the amount of codes to be generated,
# ##second argument is a string and is the name of the group
    def add_arguments(self,parser):
        parser.add_argument('amount',type=int,help='Indicates the amount of codes to be created')
        parser.add_argument('group',type=str, help='Indicates the name of the group to create the codes for')
    
    
##main function that handles the logic of the command
    def handle(self,*args, **kwargs):
        #function that generates random code and checks if it already exists ,
        # if it does it loops untill a unique code is generated
        def uniqueCode():
            unique_code=get_random_string(6)
            while not Code.objects.filter(code=unique_code):
                unique_code=get_random_string(6)
                return unique_code
        
        
        
        ##assigning arguments
        amount=kwargs['amount']
        group=kwargs['group']
        ###looping in range of number of codes to be generated,
        # generating codes and appending them to temporary dictionary
        resid,res=Groups.objects.get_or_create(groupName=group)
        codeDict={group:[]}
        for i in range(amount):
             Code.objects.create(code=uniqueCode(),Group_id=resid.id)
             codeDict[group].append(uniqueCode())
            
        
       ####checking if json file has data,if it does the temporary dictionary created will be appended,
       ##if it doesnt it will be populated with the dictionary
        with open("./voucher/codes.json","r") as file:
            try:
                data=json.load(file)
                with open("./voucher/codes.json","w") as file:
                    data.update(codeDict)
                
                    json.dump(data,file,indent=4)

            except:
                with open("./voucher/codes.json","w") as file:
                    json.dump(codeDict,file,indent=4)

        ##looping over all data in json file and returning the number of groups and the number of codes
        file=open("./voucher/codes.json")
        data=json.load(file)
        for group in data :
            lentotal=0
            numberofgroups=0
            lentotal+=len(data[group])
            numberofgroups+=1
        
        ##outputing number of groups and number of codes
        self.stdout.write('the file must have '+str(lentotal)+' codes and '+str(numberofgroups)+' groups.')          