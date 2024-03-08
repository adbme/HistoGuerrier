# HistoGuerrier

Projet machine learning python : 
- avoir un dataset de plusieurs types de guerriers historiques, avec des caractéristiques qui les différencient.
- A partir d'une image d'un guerrier antique ***[d'une date]*** à ***[une date]*** l'algo nous retourne des infos du guerrier, son type etc

![image](https://github.com/adbme/HistoGuerrier/assets/98839796/11109e44-335c-4fbb-8a7c-4a2cd1ad0fda)

![image](https://github.com/adbme/HistoGuerrier/assets/98839796/2d277142-ae59-4246-92f2-b8c88b62e34d)


## Entrainement 1 - réseau de neurones - CLASSIFICATION D'IMAGES DE CHIFFRES    
1. installation des librairies : 

Je vais utiliser les librairies
***- tensorflow :*** permet d'entrainer notre modèle

```python
pip install tensorflow
```

Pour Vérif la version on l'importe puis on le print de cette manière :

```python
import tensorflow as tf
print(tf.__version__)
```

Je suis sur la ***2.15.0***

2. Dataset

Au lieu d'en créer un, je vais prendre une ***base de donnée MNIST** existantes. De ce que j'ai compris, une MNIST reggroupe un tas d'image de chiffres 

Cela va nous renvoyer des tuples, c'est comme un format de liste(json), mais un tuple est défini avec des parenthèzes
```python
mytuple = ("apple", "banana", "cherry")
```
ou
```python
mytuple = (1, 2, 3)
```

