## TP Docker & Flask 


**Quickstart Docker** 

* comprendre la différence entre images et containers et à quoi sert un `Dockerfile` 
* installer docker sur votre machine (Ubuntu de préférence, si pas de machine ubuntu vous pouvez faire un double boot ou bien installer une VM en profitant de l'accès gratuit d'un éditeur cloud GCP, Azur, AWS...) 
* lancer votre premier container ubuntu, l'équivalent du *hello-world* de docker  
* regarder si votre container est bien lancer 
* faire un résumé type `cheat sheet` des principales commandes dockers relatives aux images et containers
	* expliquer les commandes docker `build`, `run` et `exec`
	* expliquer ce qu'est un port dans un container
* vérifier en vous connectant à votre container qu'il est bien `up` et qu'il s'aggit bien 
* **(bonus)** lancer un petit container applicatif en python avec docker 

**Docker et Python**

* écrire un Dockerfile contenant : 
	* Une image ubuntu ou python 
	* installer python3, pip3 et vim 
	* une installation automatique du fichier `requirements.txt` que vous écrirez à la racine de votre application. Renseignez vous sur ce fichier `requirements.txt`, que fait il, pourquoi est il utile? 
	* un repertoire app (dans lequel se trouvera votre application flask) 
	* une exposition du port de votre choix
	* pour finir le container devra lancer votre application flask sur le port de votre choix précédemment exposé.  
	* **(bonus)** déployer votre application sur le cloud gratuit [heroku](https://www.heroku.com)

	
**Projet Bonus facultastif à rendre pour le 02/12**
Coder un site type vitrine/portfolio en flask et le déployer avec github pages 