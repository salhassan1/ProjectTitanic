# ouverture de fichier titanic.csv

import pandas as pd
from matplotlib import pyplot as plt

# pandas est une librairie python qui permet de manipuler des données

# Charger les données
data_titanic = pd.read_csv('titanic.csv')

print(data_titanic.head())

#   affichage des colonnes
print(data_titanic.columns)

# verifie si les données sont manquantes

print(data_titanic.isnull().sum())

# longueur des données
print(len(data_titanic))

# ******* age *********************
# age maxi et mini des passagers
print("Age maxi et mini des passagers")
print(data_titanic['Age'].min())
print(data_titanic['Age'].max())
# age moyen des passagers
print("Age moyen des passagers")
print(data_titanic['Age'].mean())

# Selection_col = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
Selection_col = [ 'Pclass ' 'Age']
target_col = ['Survived']

# decision tree classifier
from sklearn.tree import DecisionTreeClassifier

max_depth = 4  # Profondeur maximale de l'arbre
clf = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
print(clf)

# jeu de données grace a selection_col


# Préparer les données pour l'arbre de décision
X= data_titanic[['Pclass',  'Age']].copy()# features ou caractéristiques

y= data_titanic['Survived'] # label ou prédiction

clf.fit(X, y)

# Utiliser .loc pour assigner les valeurs
X.loc[:, 'Sex'] = data_titanic['Sex'].map({'male': 0, 'female': 1})
from sklearn.tree import plot_tree

# display decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=X.columns, class_names=['Not Survived', 'Survived'], filled=True)
plt.show()