# Dejan Djokic
# Project 3
# 1 December 2013
# Project 3 Option A: complete employ.py and also this module (empDB.py).
# For empDB.py
# Document each method with a description of what it accomplishes and returns, and how each parameter is used.

# For each method, also state what its big-Oh runtime is and justify your claim
# You may use the following in your runtime justifications:
# The run-time of adding an element to the end of a list is constant time
# The run-time of most string operations are linear, except indexing and len, which are constant time.
# The run-time of a slice operation is proportional to the length of the output, but independent of the size of the input.

# Restrictions on use of built-in functions ar listed above some of the methods you will code

import copy
from employ import *

class empDB:
    def __init__(self, lst= []):   
        self.lst = lst

    # Returns string for database output in csv (comma separated values) format: one employee per line, attibutes separated by commas
    # Big O Notation : O(n)
    # It goes through the list N times, while concatenating employee to a new, created string
    def __str__(self):
        ns = ''
        for emp in self.lst:
            ns += str(emp) + '\n'
        return ns

    # Returns the lenght of a list
    # Big O Notation: O(n)
    # It goes through the list one time checking each element
    def __len__(self):
        lenght = 0
        for employee in self.lst:
            lenght += 1
        return lenght

    # Inserts an employee to the end of the list
    # Big O Notation: O(1)
    def appendEmp(self, emp=Employee()):
        self.lst += [emp]

    # Do not use slices: code this yourself
    # Inserts an employee into the list at position index
    # Big O Notation = O(n)
    # insertEmp takes on the index of each worker in self.lst and compares it with the index provided
    # Inserts an employee into the position index and, therefore, moves all elements up one index
    def insertEmp(self, index, emp=Employee()):
        ni = 0
        nl = []
        for employee in self.lst:
            if ni == index:
                nl += [emp]
            nl += [employee]
            ni += 1
        self.lst = nl
                
    # Three standard methods to overload
    # Allows for bracket operator to be used to return indexth element of the empDB 
    # Returns element at position index of self.list
    # Big O Notation: O(1)
    # The runtime of most string operations are usually linear, except indexing and len, which have constant time
    def __getitem__(self, index):    
        return self.lst[index]

    # Allows for bracket operator to be used to modify indexth element of the empDB, setting it to val
    # Assigns the employee, emp to the position index
    # Big O Notation: O(1)
    # The runtime of most string operations are usually linear, except indexing and len, which have constant time
    def __setitem__(self, index, emp=Employee()):  # this is complete
        self.lst[index] = emp

    # Do not use del operator, but you may slice or bracket operator
    # Deletes item at indexth element
    # Big O Notation: O(1)
    # The runtime of a slice operation is proportional to the lenght of the output, however, independent of the size of the input
    def __delitem__(self, index):
        self.lst = self.lst[:index] + self.lst[index+1:]


    # Search on the attribute "lastName". For extra credit search on any attribute using: getattr(object, attrib[, defaultAttrib]) 
    # Big O Notation = O(n)
    # This is because the algorithm traverses through the list once comparing each element in the list N times comparing each element in the list to the value passed into the search
    # When the element being search for is found, the index of the matching element is returned. If no match found, -1 is returned
    def sequentialSearch(self, val, attrib='lastName'):
        for i in range(len(self.lst)):
            if val == getattr(self.lst[i], attrib):
                return i
        return -1

    # Sorts on any attribute using: getattr(object, attrib[, defaultAttrib])
    # Big O Notation : O(n**2)
    # This is because it containts nested loop which goes through the list for each loop, N times
    def selectionSort(self, attrib="lastName"):         # this method is complete
        minIndex = 0
        for i in range (len(self.lst)):
            minIndex = i
            for j in range(i+1, len(self.lst)):
                # This is how to sort by lastName if there was no parameter attrrib
                # if self.lst[minIndex].lastName > self.lst[j].lastName:  
                # This is how to sort by parameter attribute with "lastName" as the default
                if getattr(self.lst[minIndex], attrib, "lastName") > getattr(self.lst[j],attrib, "lastName"):
                    minIndex = j
            temp = self.lst[minIndex]
            self.lst[minIndex] = self.lst[i]
            self.lst[i] = temp
            
    # Sort on the attribute "lastName" (ie: sort by last name)
    # For extra credit sort on any attribute using: getattr(object, attrib[, defaultAttrib])
    # Big O Notation: O(n log n)
    # Merge sort splits the unsorted list into n sublist, each containing 1 element. It repeatedly merges afterwards
    # Sublisting to produce new sublists until there is only 1 sublist remaining becoming the sorted list
    # Helper function that starts divider function and passes in self.list
    def mergeSort(self, attrib="lastName"):
        self.lst = self.splits(self.lst,attrib)
    # Divides the list into sublist until each element in the original list containts 1 element
    def splits(self,lst, attrib):
        if len(lst) == 1:
            return lst[0]
        mid = len(lst) / 2
        left = lst[:mid]
        right = lst[mid:]
        if len(left)>1:
            left = self.splits(left, attrib)
        if len(right)>1:
            right = self.splits(right, attrib)
        return self.joint(left, right, attrib)

    # Creates a new list from two sublists and moves from smallest sublist all the way to the top
    def joint(self, left, right, attrib):
        result = []
        while left and right:
            if getattr(left[0], attrib) < getattr(right[0], attrib):
                result += [left[0]]
                left = left[1:]
            else:
                result += [right[0]]
                right = right[1:]
        if left:
            result += left
        else:
            result += right
        return result 
   
    # Sort on the attribute 'lastName'
    # For extra credit sort on any attribute using: getattr(object, attrib[, defaultAttrib])
    # Big O Notation: O(n**2)
    # Sorts through the list iterating N times up the list and N times down the list
    def insertionSort(self, attrib = 'lastName'): 
        for i in range (1, len(self.lst)):
                temp = self.lst[i]
                j = i-1
                while j >= 0:
                    if getattr(self.lst[j], attrib) > getattr(temp, attrib):
                        self.lst[j+1] = self.lst[j]
                        j -= 1                      
                    else:
                        break
                self.lst[j+1] = temp
            
    # Search on the    attribute 'lastName' (ie: return index of employee with last name == val)
    # For extra credit search on any attribute using: gettatr(object, attrib[, defaultAttrib])
    # Hint: if you code this recursively, then write and call a helper function with parameters lo, hi
    # Carries out a recursive binary search on a sorted list. Takes a list and val and returns the index
    # Big O Notation: O(log  n)
    # binarySearch processes half of the data every time it makes a decision
    def binSearch(self, val, attrib = 'lastName', lo = 0, hi = 0):
        mid = (lo + hi) / 2
        if getattr(self.lst[mid], attrib) == val:
            return mid
        if lo >= hi:
            return -1 
        elif getattr(self.lst[mid], attrib) > val:
            return self.binSearch(val, attrib, lo, mid - 1)
        elif getattr(self.lst[mid], attrib) < val:
            return self.binSearch(val, attrib, mid+1, hi)

    def binarySearch(self, val, attrib='lastName'):
        lo = 0
        hi = len(self.lst) - 1
        return self.binSearch(val, attrib, lo, hi)
    
    # Given listEmpHrsWorked is a list of tuples with (SSID, hrsWorkedThisPeriod) for each employee in the list
    # Returns a new list of tuples for each tuple in listEmpHrsWorked
    # Your new list will contain the following tuple for each SSID in listEmpHrsWorked:
    # (firstname, lastName, ssID,  hrsWorkedThisPeriod, payThisPeriod)
    # Big O Notation: O(n) * O(n)
    # Traverses through the list N times while calling on sequental search also traversing through the list N times
    def calcPayroll(self, listEmpHrsWorked):
            payroll = []
            for elem in listEmpHrsWorked:
                cell = empList.sequentialSearch(elem[0], 'ssID')
                emp = empList[cell]
                payThisPeriod = emp.calc_Salary(elem[1])
                empTup = (emp.firstName, emp.lastName, emp.ssID, emp.hrsWorkedThisPeriod, payThisPeriod)
                payroll += [empTup]
            return payroll

### A start on testing :
##empList = empDB()
##NUM_EMPS = 10
##for i in range(NUM_EMPS):
##    SSstring =  "111-22-120" + str(i)
##    empList.appendEmp(Employee("Employee", str(NUM_EMPS-i-1), SSstring, datetime.fromordinal(1), datetime.today(), 800.00*i ))
##    #print empList[i].lastName
##print

empList = empDB()
employDB_backup = copy.deepcopy(empList)

empList.appendEmp(Manager("Anniston", "Avor", "456-72-3843", datetime.fromordinal(1), datetime.today(), 2412, ['Brickson', 'Click']))
empList.appendEmp(AdminAssistant("Bob", "Brickson", "123-29-4328", datetime.fromordinal(1), datetime.today(), 9994, 'Djokic', "Human Resources" ))
empList.appendEmp(AdminAssistant("Calvin", "Click", "167-22-3428", datetime.fromordinal(1), datetime.today(), 83, 'Djokic', "Art & Design" ))
empList.appendEmp(Manager("Dejan", "Djokic", "154-56-2123", datetime.fromordinal(1), datetime.today(), 300, ['Finatra', 'Govano']))
empList.appendEmp(FactoryWorker("Emmanuel", "Ebro", "934-43-0009", datetime.fromordinal(1), datetime.today(), 21, 'Djokic', 'Fries'))
empList.appendEmp(FactoryWorker("Frank", "Finatra", "315-34-6434", datetime.fromordinal(1), datetime.today(), 10, 'Djokic', 'Burgers'))
empList.appendEmp(Manager("Gerrard", "Govano", "625-65-2312", datetime.fromordinal(1), datetime.today(), 18, ['Harry', 'Ifko']))
empList.appendEmp(MaintenanceWorker("Harold", "Harry", "356-05-7000", datetime.fromordinal(1), datetime.today(), 12, 'Djokic',['LoSchiavo']))
empList.appendEmp(MaintenanceWorker("Ian", "Ifko", "111-55-7093", datetime.fromordinal(1), datetime.today(), 12, 'Djokic',['Phelan', 'Gillson']))

# Tests
print 'Emplist cell 1 and 6'
print '********************'
print empList[1]
print empList[6]
print "%s" %("Unsorted employee list:")
print '********************'
print
print "%s" %("Employee list lenght:"), empList.__len__(),"\n"

empList[1].salary=40.0
empList[6].lastName='Dre'
empList[7]=FactoryWorker("Michael", "Mordan", "305-03-9999", datetime.fromordinal(1), datetime.today(), 20, 'Djokic', 'Fries')
print empList

print '%s' %("Delete employee at index 7 and 8")
print '********************'
empList.__delitem__(7)
empList.__delitem__(8)
print '%s' %("New employee list")
print
print "%s" %("Employee list lenght:"), empList.__len__(),"\n"
print

print "%s"%("Insert Manager 'Nicolas Cage' at index 0 using InsertEmp:")
print '********************'
empList.insertEmp(0, Manager("Nicolas", "Cage", "111-00-3984", datetime.fromordinal(1), datetime.today(), 40, ['Brickson', 'Ifko']))
print
print "%s" %("Employee list lenght:"), empList.__len__(),"\n"

print "%s" %("Insert Maintainence Worker 'Dole Morena' at index 5 using InsertEmp:")
print '********************'
empList.insertEmp(5, MaintenanceWorker("Dole", "Morena", "923-12-9000", datetime.fromordinal(1), datetime.today(), 42, 'Djokic', ["LoSchiavo"]))
print "%s" %("Employee list lenght:"), empList.__len__(),"\n"

print "%s" %("Insert Factory Worker 'Jessica Parker' at index 2 using InsertEmp:")
print '********************'
empList.insertEmp(2, MaintenanceWorker("Jessica", "Parker", "323-00-9821", datetime.fromordinal(1), datetime.today(), 84, 'Djokic',["Gillson"]))
print "%s" %("Employee list lenght:"), empList.__len__(),"\n"

print "%s" %("Append Manager 'Habib Jamal' to List using appendEmp:")
print '********************'
empList.appendEmp(Manager("Habib", "Jamal", "399-00-1111", datetime.fromordinal(1), datetime.today(), 1203,['Ifko', 'Harry']))
print
print "%s" %("Employee list lenght:"), empList.__len__(),"\n"

print "%s" %("Append Admin Assistant 'Nick Frost' to List using appendEmp:")
print '********************'
empList.appendEmp(AdminAssistant("Nick", "Frost", "043-11-1000", datetime.fromordinal(1), datetime.today(), 67, 'Djokic', ["Gillson"]))
print
print "%s" %("Employee list lenght:"), empList.__len__(),"\n"

print "%s" %('Sequential search')
print '********************'
print "%s" %('Search for ssID "154-56-2123"'), empList.sequentialSearch('154-56-2123', 'ssID')
print "%s" %('Search for lastName "Avor"'), empList.sequentialSearch('Avor')
print "%s" %('Search for lastName "Brickson"'), empList.sequentialSearch('Brickson')
print "%s" %('Search for lastName "Click"'), empList.sequentialSearch('Clickson')
print "%s" %('Search for lastName "Djokic"'), empList.sequentialSearch('Djokic')
print "%s" %('Search for lastName "Ebro"'), empList.sequentialSearch('Ebro')
print "%s" %('Search for lastName "Finatra"'), empList.sequentialSearch('Finatra')
print "%s" %('Search for lastName "Govano"'), empList.sequentialSearch('Govano')
print "%s" %('Search for firstName "Dejan"'), empList.sequentialSearch('Dejan', 'firstName')
print "%s" %('Search for salary "$9994"'), empList.sequentialSearch(9994, 'salary')

print "%s" %('MergeSort list of employees by lastName: ')
print '********************'
empList.mergeSort()
print empList

print "%s" %('MergeSort list of employees by firstName: ')
print '********************'
empList.mergeSort('firstName')
print empList

print "%s" %('MergeSort list of employees by salary: ')
print '********************'
empList.mergeSort('salary')
print empList

print "%s" %('MergeSort list of employees by ssID: ')
print '********************'
empList.mergeSort('ssID')
print empList

print "%s" %('InsertionSort list of employees by lastName: ')
print '********************'
empList.insertionSort()
print empList

print "%s" %('InsertionSort list of employees by firstName: ')
print '********************'
empList.insertionSort('firstName')
print empList

print "%s" %('InsertionSort list of employees by salary: ')
print '********************'
empList.insertionSort('salary')
print empList

print "%s" %('Binary Search')
print '********************'
print "%s" %('Search for ssID "154-56-2123"'), empList.binarySearch('154-56-2123', 'ssID')
print "%s" %('Search for lastName "Avor"'), empList.binarySearch('Avor')
print "%s" %('Search for lastName "Brickson"'), empList.binarySearch('Brickson')
print "%s" %('Search for lastName "Click"'), empList.binarySearch('Clickson')
print "%s" %('Search for lastName "Djokic"'), empList.binarySearch('Djokic')
print "%s" %('Search for lastName "Ebro"'), empList.binarySearch('Ebro')
print "%s" %('Search for lastName "Finatra"'), empList.binarySearch('Finatra')
print "%s" %('Search for lastName "Govano"'), empList.binarySearch('Govano')
print "%s" %('Search for firstName "Dejan"'), empList.binarySearch('Dejan', 'firstName')
print "%s" %('Search for salary "$9994"'), empList.binarySearch(9994, 'salary')

print

print "%s" %('Calculate Payroll of workers by ssID')
print '********************'
hoursList = [('456-72-3843', 22), ('123-29-4328', 10), ('167-22-3428', 100), ('154-56-2123', 94), ('356-05-7000', 17)]
print empList.calcPayroll(hoursList)
print

print "%s" %('Additional testing')
## More testing after you fill in some methods:
print empList[5]
empList[5].salary = 2500.0
print empList[5]
print

empList.selectionSort()
print empList

empList.selectionSort("startDate")
print empList

empList[9] = AdminAssistant("Sarah", "James", "111-22-1234", datetime.fromordinal(1), datetime.today(), 25, 'Hwang', "CS" )
print empList[9]
print

empList.appendEmp(EmpHourly())
empList[10].lastName="Djokic"
print empList[10]
print
empList.appendEmp(Manager("Sophie", "Hwang", "111-22-1267", datetime.fromordinal(1), datetime.today(), 4900,["Sarah James", "Juan Ortiz"] ) )
print empList[11]
print
empList.appendEmp(AdminAssistant("Juan", "Ortiz", "111-22-1239", datetime.fromordinal(1), datetime.today(), 25, 'Hwang', "CS" ))
print empList[12]
print

print employDB_backup

