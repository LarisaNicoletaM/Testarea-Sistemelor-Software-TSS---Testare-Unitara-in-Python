# Raport de utilizare AI

## Prezentare generală a asistenței AI

Instrumentele de inteligență artificială au fost utilizate în timpul dezvoltării acestui proiect pentru îndrumare, asistență pentru depanare și generarea unui număr mic de exemple de testare.

Logica proiectului, structura proiectului, capturile de ecran, execuția și integrarea au fost completate manual.

---

# Elemente generate de AI

Următoarele componente au fost generate sau parțial asistate de AI:

## 1. Exemple de testare a mutațiilor

AI a fost utilizat pentru a genera exemple de mutanți pentru aplicația GradeBook.

Exemplu:

```python
class GradeBookMutants:

def average_wrong_operator(self, notes):
total = sum(grades)
return total * len(grades)

def average_off_by_one(self, notes):
total = sum(grades)
return total / (len(grades) - 1)
```

Acești mutanți simulează implementări logice incorecte care ar trebui detectate de teste.

---

## 2. Exemple de teste asistate de AI

Asistența AI a fost utilizată pentru generarea unui număr mic de idei de teste.

Exemplu:

```python
def test_mutant_grade_validation():
gb = GradeBook()
with pytest.raises(ValueError):
gb.add_grade("S1", -1)
```

Exemplu:

```python
def test_mutant_average_logic():
gb = GradeBook()
gb.add_grade("S1", 10)
gb.add_grade("S1", 0)
assert gb.get_average("S1") == 5
```

---

# Contribuția mea

Următoarele activități au fost finalizate manual:

* implementarea proiectului
* organizarea structurii proiectului
* depanare
* rularea testelor
* crearea capturilor de ecran
* integrare GitHub
* validarea execuției
* demonstrație de testare a mutațiilor


---

# Concluzie

Instrumentele de inteligență artificială au fost utilizate ca asistență pentru dezvoltare și suport pentru învățare.

Integrarea finală, execuția, validarea și finalizarea proiectului au fost efectuate manual.