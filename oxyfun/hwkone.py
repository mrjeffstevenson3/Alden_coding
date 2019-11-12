# import needed modules to do work. numpy is coolest.
import numpy as np
from itertools import count, islice


# method for question 1
# make 3D solution with defaults for zcoords set to 0 for 2D case
def getdistance(x1, y1, x2, y2, z1=0, z2=0):
    # set up vectors
    p1 = np.array([x1, y1, z1], dtype=np.float64)
    p2 = np.array([x2, y2, z2], dtype=np.float64)
    # calculate cartesian distance
    dist = np.sqrt(np.sum((p2 - p1) ** 2, axis=0))
    return dist


# method for question 2
def isprime(n):
    if n < 2:
        return False
    # divide the work in half.
    # see https://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python/27946768
    nsqrt = np.floor(np.sqrt(n))
    # use islice and count to set up array of numbers to test
    for number in islice(count(2), int(nsqrt) - 1):
        # if it can be divided without remainder by any intervening number it is not prime
        if n % number == 0:
            return False
    return True


# method for question 3
def usernamechecker(uname):
    # make sure its string data type
    uname = str(uname)
    if len(uname) < 5:
        return False
    # set up counters for testing upper, lower, and digit
    upcount, lowcount, numcount = 0, 0, 0
    # loop over and test every letter.
    for l in uname:
        if l in ['@', '#', ' ']:
            # stop here if you find special chars
            return False
        # test/count for uppercase, lowercase, and digit
        if str.isupper(l):
            upcount += 1
        if str.islower(l):
            lowcount += 1
        if str.isdigit(l):
            numcount += 1
    # test if any of the counters are lower than 1
    if any([upcount < 1, lowcount < 1, numcount < 1]):
        return False
    # passed all tests and over whole loop. must be a good uname
    return True


# method for question 4
def counttriple(blurb):
    blurb = str(blurb)
    # set up counters
    i, end, numtriples = 0, len(blurb) - 2, 0
    while i <= end:
        # grab 1st char using slicing
        lead = blurb[0]
        # test if it repeats twice after itself
        if lead * 2 in blurb[1:3]:
            numtriples += 1
        # shorten string by one and increment counter
        blurb = blurb[1:]
        i += 1
    return numtriples


# method for question 5
def swappairs(listofpairs):
    # make sure its a valid list or array
    if not isinstance(listofpairs, (list, np.ndarray)):
        raise TypeError('input not a list or array.')
    # set up counter and empty new list
    i, newlist = 0, []
    # do even swapping
    if len(listofpairs) % 2 == 0:
        while i < len(listofpairs):
            # reverse order of pairs using indexing
            newlist.append(listofpairs[i + 1])
            newlist.append(listofpairs[i])
            i += 2
    else:
        # do odd swapping
        while i < (len(listofpairs) - 1):
            newlist.append(listofpairs[i + 1])
            newlist.append(listofpairs[i])
            i += 2
        # add the odd man out at the end
        newlist.append(listofpairs[-1])
    return newlist


# extra credit question
def arraysums(arr1, arr2):
    # make sure they are a valid list or arrays
    if not any([isinstance(arr1, (list, np.ndarray)), isinstance(arr2, (list, np.ndarray))]):
        raise TypeError('one or both inputs not a list or array.')
    # convert to numpy arrays for easy manipulation
    arr1, arr2 = np.array(arr1), np.array(arr2)
    # if array sizes are the same add them
    if arr1.shape == arr2.shape:
        arr_sum = np.add(arr1, arr2)
    # if size/shape of arr1 is larger then make that template size the smaller arr2 will fit into
    if arr1.shape > arr2.shape and len(arr1.shape) == len(arr2.shape):
        # make dummy arr2, same size as arr1 but with zeros
        _arr2 = np.zeros(arr1.shape)
        # put elements of arr2 in order into dummy _arr2
        _arr2[:arr2.shape[0]] = arr2
        # now that arrays are the same size. element wise add them
        arr_sum = np.add(arr1, _arr2)
    # if size/shape of arr2 is larger then make that template size the smaller arr1 will fit into
    if arr1.shape < arr2.shape and len(arr1.shape) == len(arr2.shape):
        # make dummy arr1, same size as arr2 but with zeros
        _arr1 = np.zeros(arr2.shape)
        # put elements of arr1 in order into dummy _arr1
        _arr1[:arr1.shape[0]] = arr1
        # now that arrays are the same size. element wise add them
        arr_sum = np.add(_arr1, arr2)
    return arr_sum

# show test results of each method
print('results for question 1')
for points in [[1, 1, 4, 4], [2, 2, 3, 5]]:
    print('  cartesian distance between the points is {p}'.format(p=getdistance(*points)))
print('results for question 2')
for p in [13, 20]:
    print('  is the number {p} prime? '.format(p=p), isprime(p))
print('results for question 3')
for u in ['snowflake', 'snow', 'snowFlake123', 'snow flake', '@snowflake']:
    print('  is the user name "{u}" valid? '.format(u=u), usernamechecker(u))
print('results for question 4')
for t in ['abcXXXabc', 'xxxabyyyycd', '', 'a', '123111123444444']:
    print('  the number of triples in "{t}" is {numt}.'.format(t=t, numt=counttriple(t)))
print('results for question 5')
print('  ', swappairs(["four", "score", "and", "seven", "years", "ago"]))
print('  ', swappairs(["to", "be", "or", "not", "to", "be", "hamlet"]))
print('results for extra credit question 6')
print('  ', arraysums([1.19, 3.3, -1.22, 9.421], [4.4, 1.234]))

# part 2
# question 1
class Course(object):
    # default variables for Course class
    department = ''
    courseid = ''
    coursename = ''

    # no special setup required
    def __init__(self):
        pass

    def tostring(self, department, courseid, coursename):
        # overwrite defaults with given variables
        self.department = department
        self.courseid = courseid
        self.coursename = coursename
        # generate course description text string
        course = '{dept}{cid}: {cname}'.format(dept=self.department,
                                               cid=self.courseid, cname=self.coursename)
        print(course)
        return course


# question 2
# Major as subclass of Course class
class Major(Course):
    # default variables for Major class
    numreqcourses = 1
    reqcourses = []

    def __init__(self, major):
        # creates containers for parent class variables
        super(Course, self).__init__()
        self.major = major

    def newmajor(self, major, numreqcourses):
        # overwrite defaults with given variables
        self.numreqcourses = numreqcourses

    def addcourse(self, course):
        if len(self.reqcourses) <= int(self.numreqcourses):
            self.reqcourses.append(course)
        else:
            print('required course list full. either increase number of \
                  required courses or use replacecourse.')

    def replacecourse(self, oldcourse, newcourse):
        newreqcourses = [rc.replace(oldcourse, newcourse) for rc in self.reqcourses]
        self.reqcourses = newreqcourses

    def tostring(self):
        print('List of required courses for {maj}:'.format(maj=self.major.capitalize()))
        for rc in self.reqcourses:
            print('\t{course}'.format(course=rc))


# question 3
# Student as subclass of Major
class Student(Major):
    # default variables for Student class
    firstname = ''
    lastname = ''
    gpa = 0.0
    stu_major = ''
    taken_courses = []

    # 1st constructor
    def __init__(self, firstname, lastname, taken_courses):
        # creates containers for parent class variables
        super(Major, self).__init__()
        # overwrite defaults with given variables
        self.firstname = firstname
        self.lastname = lastname
        self.taken_courses = taken_courses
        # parent variable reqcourses doesn't update
        self.reqcourses = Major.reqcourses

    # second constructor
    def declaremajor(self, stu_major):
        self.stu_major = stu_major

    # 3rd constructor
    def updategpa(self, gpa):
        self.gpa = gpa

    # 4th constructor
    def getInitials(self):
        initials = self.firstname[0].capitalize() + self.lastname[0].capitalize()
        return initials

    # 5th constructor
    def satisfymajor(self, course):
        if course in self.reqcourses:
            return True
        return False

    # 6th constructor
    def canyougraduate(self):
        """
        test condition to graduate
        used python set function (more efficient) instead of looping over each
        course taken and testing if returns True with satisfymajor which is
        purpose of satisfymajor.
        FYI: does not account for electives but that was not in scope of work.
        """
        if self.gpa >= 2.0 and set(self.taken_courses).issubset(set(self.reqcourses)):
            return True
        else:
            return False

course1 = Course().tostring('ECON', '101', 'Principles of Economics I')
course2 = Course().tostring('ECON', '301', 'Environmental Economics and Policy')
course3 = Course().tostring('ECON', '350', 'Managerial Economics')
course4 = Course().tostring('ECON', '305', 'Game Theory')
course5 = Course().tostring('ECON', '210', 'replacement course for 350')
maj = Major('economics')
maj.newmajor('economics', 5)
maj.addcourse(course1)
maj.addcourse(course2)
maj.addcourse(course3)
maj.addcourse(course4)
print()
maj.tostring()

maj.replacecourse(course3, course5)
maj.tostring()

student1 = Student('bo', 'didley', [course1, course2, course3, course4])
student1.updategpa(3.5)
student1.declaremajor('economics')
student1.reqcourses


student1.taken_courses

# this is weird. should have most current state, not default state.
maj.reqcourses == student1.reqcourses

# confirms student1 does not see changes from maj.replacecourse(course3, course5)
student1.taken_courses == student1.reqcourses

student1.replacecourse(course3, course5)
student1.reqcourses


print(student1.getInitials(),
      student1.satisfymajor(course1),
      student1.satisfymajor(course2),
      student1.satisfymajor(course3),
      student1.satisfymajor(course4))
