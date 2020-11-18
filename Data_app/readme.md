# TP : réalisation d'une data app 

votre mission est de construire une petite application de visualisation interactive de données avec l’outil Streamlit vu au chapitre précédent, qui contiendra les fonctionnalités suivantes :   

* Charger des jeux de données (au moins 2) présents dans votre répertoire local
	* il faudra donc que votre application pointe un chemin et sorte les fichier (dataset) du repertoire pointé. Vous utiliserez pour cela le module `os` de python.
* Afficher le dataset chargé suivant un nombre de ligne entrées par l’utilisateur
* Afficher le nom des colonnes du dataset 
* Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées 
* La shape du dataset, par lignes et par colonnes
* Afficher les statistiques descriptives du dataset
* Afficher plusieurs type de graphique dans une partie visualisation avec notamment : 
	* Une heatmap des corrélations avec Matplotlib et Seaborn (avec les valeurs annotés)
	* Un graphique en barres afin de visualiser la taille du dataset par caractéristiques (on pourra notamment grouper les données afin d’avoir des graphiques plus précis)

Et enfin une dernière partie dite « visualisation personnalisable » qui permettra de : 

* Sélectionner le type de graphique à tracer
Sélectionner des colonnes dans le jeux de données afin de générer le graphique
* **(bonus)**À noter que suivant certain jeux de données il y aura des graphiques qui n’auront pas de sens capturez les dans des exceptions 🧐