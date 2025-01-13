# ProjectTitanic
Création d'un arbre de décision en Python

Préparation des données :
Tout d'abord, j'ai collecté les données nécessaires pour entraîner l'arbre de décision. Ces données étaient soit stockées dans un fichier CSV, soit créées manuellement sous forme de tableau.
Les données contenaient des caractéristiques (features) et une colonne cible (target), représentant la classe ou le résultat attendu.

Création de l'arbre de décision :
Ensuite, j'ai utilisé le module DecisionTreeClassifier de scikit-learn pour construire l'arbre de décision. J'ai également configuré certains hyperparamètres comme la profondeur maximale (max_depth) ou le critère de division (criterion).

Entraînement du modèle :
Une fois l'arbre créé, je l'ai entraîné sur l'ensemble d'entraînement en utilisant la méthode .fit()

Visualisation de l'arbre :
Pour mieux comprendre la structure de l'arbre, j'ai utilisé plot_tree ou export_text pour visualiser ou afficher l'arbre de décision.

Cette démarche méthodique a permis de construire un arbre de décision performant et adapté à mon problème.

