---
theme: white
title: Cours M1 bioinfo
---

<link href='custom.css' rel='stylesheet' type='text/css'>

<!--=================================================================================================== -->
## <h2 style="color:white;">Conception logicielle orientée objet</h2>
<!--=================================================================================================== -->
<!-- .slide: style="color:white" -->
<!-- .slide: data-background="img/code.png" -->

UE programmation orientée objet

Master bioinfo

Automne 2018

---

<!--=================================================================================================== -->
## <h2 style="color:white;">Rappels concepts objet</h2>
<!--=================================================================================================== -->
<!-- .slide: style="color:white" -->
<!-- .slide: data-background="img/code.png" -->

---

### Objets

> __Objet:__ entité qui combine code et données

```python
>>> a = 1.2
>>> a.real
1.2
>>> a.is_integer()
False
```

---

### Attributs

> __Attribut:__ donnée associée à un objet

```python
>>> a.real
1.2
```

Ici, `a.real` est l'attribut `real` de l'objet `a`

---

### Méthode

> __Méthode:__ fonction associée à un objet

```python
>>> a.is_integer()
False
>>> a.is_integer
<built-in method is_integer of float object at 0x7fb92fcd4138>
```

Ici, `a.is_integer` est la méthode `is_integer` de l'objet `a`

Une méthode peut accéder aux attributs de l'objet.


---

### Classes

> __Classe:__ modèle à partir duquel<br/>des objets peuvent être créés

```python
class MyFloat:
    def __init__(self, value):
        self.real = value
    
    def is_integer(self):
        return (self.real - float(int(self.real))) == 0
```

----

#### Déclaration de méthode

```python
class MyFloat:    
    def is_integer(self):
        return (self.real - float(int(self.real))) == 0
```

Une méthode prend self en paramètre pour pouvoir accéder à l'état de l'objet via `self.<nom de l'attribut>`

----

#### Constructeur

> __Constructeur:__ méthode chargée<br/>d'initialiser l'état d'un objet créé

```python
class MyFloat:
    def __init__(self, value):
        self.real = value
```

En python, le constructeur s'appelle `__init__`

---

### Instances

> __Instance:__ objet créé à partir d'une classe

```python
a = MyFloat(1.2)
```

On dit que `a` est une instance de la classe `MyFloat`

---

### Héritage

Une classe peut __hériter__ d'une autre classe dont<br/>elle récupère toutes les méthodes et les attributs

```python
class ImprovedFloat(MyFloat):
    def is_positive(self):
        return self.real >= 0
```

```python
>>> a = ImprovedFloat(1.2)
>>> a.real
1.2
>>> a.is_positive()
True
```

Ici, `MyFloat` est la __classe mère__ et `ImprovedFloat` la __classe fille__.

----

#### Redéfinition de méthodes<br/> dans les classes filles

```python
class MyInt(ImprovedFloat):
    def is_integer(self):
        return True
```

```python
>>> a = ImprovedFloat(1.2)
>>> b = MyInt(1.2)
>>> a.is_integer()
False
>>> b.is_integer()
True
```

---

### Méthodes statiques

> __Méthode statique:__ fonction associée à<br/>une classe (plutôt qu'à une instance)

```python
class MyClass:
    @staticmethod
    def class_name():
        return "MyClass"
```

```python
>>> x = MyClass()
>>> x.class_name()
'MyClass'
>>> MyClass.class_name()
'MyClass'
```

---

### Résumé des rappels

* les __objets__ regroupent:
    * des données (les __attributs__)
    * du code (les __méthodes__)
* les __classes__ sont des modèles d'objets
    * le __constructeur__ initialise l'état d'un objet
* une __instance__ est un objet créé à partir d'une classe
* une classe peut __hériter__ d'une autre pour récuperer attributs et méthodes
    * une classe fille peut __redéfinir une méthode__ d'une classe mère

---

<!--=================================================================================================== -->
## <h2 style="color:white;">Le polymorphisme</h2>
<!--=================================================================================================== -->
<!-- .slide: style="color:white" -->
<!-- .slide: data-background="img/code.png" -->

---

### Le polymorphisme

> __Polymorphisme:__ possibilité d'interagir avec des objets de différents types de façon unifiée

```python
>>> add(1, 2)
3
>>> add(1, 2.3)
3.3
>>> add("a", "b")
'ab'
```

---

### Opérations polymorphes en python

```python
>>> 1 + 2
3
>>> "a" + "b"
'ab'
```

```python
>>> 2 * 3
6
>>> "a" * 3
'aaa'
```

```python
>>> len([1, 2, 3])
3
>>> len((1,2))
2
>>> len({1:3, 2:4})
2
```

etc...

----

#### Ma fonction polymorphe

```python
def add(a, b):
    return a + b
```

```python
>>> add(1, 2)
3
>>> add(1, 2.3)
3.3
>>> add("a", "b")
'ab'
```

---

### Polymorphisme en<br/>manipulant les types

```python
def sum(l):
    assert type(l) == list
    result = 0
    for element in l:
        result += element
    return result
```

```python
>>> sum([1, 2, 3])
6
>>> sum(["a", "b", "c"])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in sum
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
```
<!-- .element: class="fragment" data-fragment-index="1" -->

----

Disjonction sur le type de `l`

```python
def sum(l):
    assert type(l) == list
    assert len(l) > 0
    if type(l[0]) == str:
        zero = ""
    elif type(l[0]) == int:
        zero = 0
    for element in l:
        zero += element
    return zero
```

```python
>>> sum([1, 2, 3])
6
>>> sum(["a", "b", "c"])
'abc'
```
<!-- .element: class="fragment" data-fragment-index="1" -->

----

Refactoring avec un dictionnaire de zéros

```python
zeros = {str:"", int:0, float:0, list:[]}

def sum(l):
    assert type(l) == list
    assert len(l) > 0
    result = zeros[type(l[0])]
    for element in l:
        result += element
    return result
```

```python
>>> sum([1.2, 2, 3])
6.2
>>> sum(["a", "b", "c"])
'abc'
>>> sum([[1, 2], [3, "a"], [4]])
[1, 2, 3, 'a', 4]
```
<!-- .element: class="fragment" data-fragment-index="1" -->

---

### Polymorphisme avec des classes

Deux classes implémentant une même méthode peuvent être traitées de façon polymorphe

```python
class List3:
    "List with 3 elements"
    def __init__(self, a, b, c):
        self.value = [a, b, c]
    
    def count(self, value):
        result = 0
        for element in self.value:
            if value == element:
                result += 1
        return result
```

Par exemple `List3` implémente la méthode `count`,<br/>comme `list`

----

La méthode `count_list` ci-dessous fait la somme des `counts`<br/>de tous les éléments d'une liste

```python
def count_list(l, value):
    result = 0
    for element in l:
        result += element.count(value)
    return result
```

```python
>>> l1 = [1, 2, 1]
>>> l2 = List3(2, 1, 3)
>>> l3 = (1, 3)
>>> count_list([l1, l2, l3], 1)
4
```

---

### Problème: garantir/tester les objets

```python
def sum(l):
    assert type(l) == list
    assert len(l) > 0
    element_class = type(l[0])
    result = element_class.zero()
    for element in l:
        result.add(element)
    return result
```

Comment tester (par ex. avec un `assert`) qu'un objet a bien:
* une méthode statique `zero`
* une méthode `add`

---

### Interfaces

Une interface est un ensemble de fonctionnalités

Par example, on peut décider d'appeler `Addable` l'interface constituée de
* une méthode statique `zero`
* une méthode `add`
* une méthode `greather_or_equal`

----

#### Implémentation en python

```python
from abc import ABC, abstractmethod, abstractproperty

class Addable(ABC):
    @abstractmethod
    def add(self, other):
        pass
    
    @staticmethod
    @abstractmethod
    def zero():
        pass

    @abstractmethod
    def greater_or_equal(self, other):
        pass
```


---

* rappels orienté object
    * interfaces
    * polymorphisme
* enjeux:
    * code flexible ?
    * factorisation ?
    * réutilisation ?
* composition / héritage
    * liskov principle
* invariants, pré/ost conditions
* MVC
* sérialisation
* code générique (type / collection hétérogènes)