class GradeBookMutants:

    def average_wrong_operator(self, grades):
        total = sum(grades)
        return total * len(grades)

    def average_off_by_one(self, grades):
        total = sum(grades)
        return total / (len(grades) - 1)

    def broken_validation(self, grade):
        if grade < 1 or grade > 10:
            raise ValueError("mutant version")