#Object of the Class employee consulting costs
name = "Ajax Enterprises"
chargeRate = {'UG':500, 'OG': 450, 'NG': 375}

class Employee:
    def __init__(self, name, chargeRate):
        self.name = name
        self.chargeRate = chargeRate
        print "Welcome to Consultant Costing"
        
    def companyName(self):
        print "The name of the company is"
        return self.name
    
    def costOf(self, resource):
        if resource not in self.chargeRate:
            print resource, "doesn\'t work here"
            return None
        else:
            print resource,"would cost you"
            return self.chargeRate[resource]
    def resourceHoursFrom(self,resource, hours):
        cost = 0
        if resource in self.chargeRate:
            if resource == 'OG':
                print "Don\'t bother let him work on spark"
                return None
            else:
                cost = cost + (self.costOf(resource) * hours)
                return cost          
        else:
            print resource, "doesn\'t work here"   
            
        
if __name__ == "__main__":
   
    x = Employee(name,chargeRate)
    print(x.costOf('UG'))
    print(x.companyName())
    print(x.resourceHoursFrom('NG',25))
    print(x.resourceHoursFrom('OG',25))