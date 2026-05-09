import pytest
from app.grade_book import GradeBook


# -------------------------
# 1. EQUIVALENCE PARTITIONING
# -------------------------

def test_valid_grades():
    gb = GradeBook()
    gb.add_grade("S1", 8)
    gb.add_grade("S1", 6)
    assert gb.get_average("S1") == 7


def test_invalid_student():
    gb = GradeBook()
    assert gb.get_average("UNKNOWN") == 0


# -------------------------
# 2. BOUNDARY VALUE ANALYSIS
# -------------------------

def test_boundary_low():
    gb = GradeBook()
    gb.add_grade("S1", 0)
    assert gb.get_average("S1") == 0


def test_boundary_high():
    gb = GradeBook()
    gb.add_grade("S1", 10)
    assert gb.get_average("S1") == 10


# -------------------------
# 3. DECISION + CONDITION COVERAGE
# -------------------------

def test_pass_status():
    gb = GradeBook()
    gb.add_grade("S1", 6)
    gb.add_grade("S1", 7)
    assert gb.get_status("S1") == "PASS"


def test_fail_status():
    gb = GradeBook()
    gb.add_grade("S1", 3)
    gb.add_grade("S1", 4)
    assert gb.get_status("S1") == "FAIL"


def test_no_data_status():
    gb = GradeBook()
    assert gb.get_status("X") == "NO DATA"


# -------------------------
# 4. STATEMENT COVERAGE
# -------------------------

def test_multiple_students():
    gb = GradeBook()
    gb.add_grade("A", 5)
    gb.add_grade("B", 10)
    assert gb.get_average("A") == 5
    assert gb.get_average("B") == 10


# -------------------------
# 5. CIRCUIT / LOOP COVERAGE
# -------------------------

def test_loop_execution():
    gb = GradeBook()
    for i in range(1, 6):
        gb.add_grade("S1", i)
    assert gb.get_average("S1") == 3


