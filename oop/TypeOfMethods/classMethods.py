
class student:

    school= "ABC Higher secondery School"
    @classmethod
    def get_school(cls):
        return cls.school

print(student.get_school())    