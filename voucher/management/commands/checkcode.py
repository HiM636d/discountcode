from django.core.management.base import BaseCommand
from voucher.models import Code,Groups
from django.utils.crypto import get_random_string
import json

################ creating custom cli command to check if code exists in json file
class Command(BaseCommand):
    help='makes discount voucher-codes for groups ** takes amount of vouchers as first argument** name of group as second argument'

    ##defining arguments expected by the command, the command expects one argument which will be the code to check for existence in json file
    def add_arguments(self,parser):
        parser.add_argument('codeToCheck',type=str, help='Indicates the code to be checked')
    ##function that handles the logic of the command
    def handle(self,*args, **kwargs):
        ##assiggning argument
        codeToCheck=kwargs['codeToCheck']
        
        
        ###checking if the code exists as a value for any of the groups
        file=open("./voucher/codes.json")
        data=json.load(file)
        if any(codeToCheck in val for val in data.values()):
            group=[key for key, value in data.items() if codeToCheck in value]
            ##outputting result if it does
            self.stdout.write("the code " +codeToCheck+" is valid for group :"+str(group)+".")

    ###outputing result if it doesnt
        else:
            self.stdout.write( "code is not valid for any group")