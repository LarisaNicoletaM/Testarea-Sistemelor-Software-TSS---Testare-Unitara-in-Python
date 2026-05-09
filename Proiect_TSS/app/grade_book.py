class GradeBook:
    def __init__(self):
        self.students = {}

    # ADD GRADE (3 intrări + validări)
    def add_grade(self, student_id, grade):
        if grade < 0 or grade > 10:  # IF fără else
            raise ValueError("Grade must be between 0 and 10")

        if student_id in self.students:  # IF + ELSE
            self.students[student_id].append(grade)
        else:
            self.students[student_id] = [grade]

    # CALCUL MEDIE (loop + condiții)
    def get_average(self, student_id):
        if student_id not in self.students:
            return 0

        grades = self.students[student_id]
        total = 0

        for g in grades:  # CIRCUIT / ITERAȚIE
            if g >= 5:  # condiție simplă
                total += g
            elif g < 5 and g >= 0:  # condiție compusă
                total += g

        if len(grades) > 0:
            return total / len(grades)
        else:
            return 0

    # STATUS STUDENT (decizie)
    def get_status(self, student_id):
        if student_id not in self.students:
            return "NO DATA"

        avg = self.get_average(student_id)

        if avg >= 5 and avg <= 10:
            return "PASS"
        else:
            return "FAIL"

        # =========================
        # Mutanti
        # =========================

        class GradeBookMutants:

            def average_wrong_operator(self, grades):
                # Mutant 1: wrong operator
                total = sum(grades)
                return total * len(grades)

            def average_off_by_one(self, grades):
                # Mutant 2: off-by-one error
                total = sum(grades)
                return total / (len(grades) - 1)

