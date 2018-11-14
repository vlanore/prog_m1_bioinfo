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