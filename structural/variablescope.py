# L -> E -> G-> B
"""L- LOCAL VARIABLE
E- ENCLOSING VARIABLE 
G- GLOBAL VARAIBLE 
B - BUILT IN VARIABLE""" 

global_partner="you can access from anywhere"

def local():
    name="Deepak"
    
    def Enclosing():
        area="tamilnadu"
        print(f"{name} from {area} {global_partner}")
    Enclosing()

local()