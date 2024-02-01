HR = [("Mark Zukerberg, HR, 30000"), ("Bruno Mars, HR, 40000")]
class Employee:
    def __init__(self,department):
        self.department = department

        # if self.department == 'HR':
        #     HRdept()

    def HRdept(self):
        hrperson = []
        hrname = input("Enter your full name: ")
        hrperson.append(hrname)
        hrperson.append('HR')
        hrpay = input("Enter your salary: ")
        hrperson.append(hrpay)

        for i in range(len(hrperson)):
            print(i + 1, hrperson[i])
department = input("Enter your department: ")
emp1 = Employee(department)
if department == 'HR':
         emp1.HRdept()
