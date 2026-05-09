# Raport de utilizare AI

## Instrument AI utilizat

Pentru acest proiect am folosit ChatGPT pentru a mă ajuta cu:
- generarea de idei de teste unitare
- înțelegerea testării mutațiilor
- îmbunătățirea documentației proiectului

---

## Exemple de solicitări

### Solicit 1
"Generează teste unitare pytest pentru o clasă GradeBook în Python"

### Solicit 2
"Dă-mi exemple de teste de mutații în Python"

---

## Teste generate de AI

### Exemplu de test 1

```python
def test_average_correct_values():
gb = GradeBook()
assert gb.add_grade("Ana", 10) is True
assert gb.add_grade("Ana", 8) is True
```

### Exemplu de test 2

```python
def test_average_boundary_values():
gb = GradeBook()
gb.add_grade("Ion", 0)
gb.add_grade("Ion", 10)
assert 0 <= gb.get_average("Ion") <= 10
```

---

## Testarea mutațiilor

Doi mutanți manuali au fost introduși în proiect.

### Mutantul 1

```python
return total * len(grades)
```

### Mutantul 2

```python
return total / (len(grades) - 1)
```

Testarea mutațiilor a fost efectuată automat folosind mutmut.

Comandă utilizată:

```bash
mutmut run
```

---

## Concluzie

Instrumentele AI au ajutat la accelerarea procesului de testare și au oferit idei utile pentru testele unitare și testarea mutațiilor.
Implementarea finală și ajustările au fost verificate manual.