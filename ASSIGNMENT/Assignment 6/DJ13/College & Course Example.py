class CMR:
    cname = "CMR College"

    def show_college(self):
        print("College Name:", self.cname)


class Course(CMR):

    def show_courses(self):
        print("BBA")
        print("MBA")
        print("BE")
        print("MTech")


obj = Course()
obj.show_college()   # inherited
obj.show_courses()