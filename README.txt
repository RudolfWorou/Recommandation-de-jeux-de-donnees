
SYSTEME DE RECOMMANDATION DE JEUX DE DONNÉES


Version Python :  3.7.10

Prérequis : 
		Anaconda qui est aussi utilisé pour exécuter les notebooks
		Les bibliothèques python suivantes à installer en utilisant la commande pip install:  
					numpy           
					pandas 		
					scikit-learn    
					nltk 		
					pickle5 
					regex
	
Le Jupyter notebook se nomme requete_user.ipynb. Il permet d'éxécuter le back-end du site mis en place.
Le site apporte juste l'aspect graphique et user friendly.

Lancement du site web sur une machine locale. 
	

	
	Étape 1 : Installer Django avec la commande : 
		conda install -c anaconda django
	
	Étape 1:  Se mettre dans le répectoire mysite et y ouvrir un invite de commande

	Étape 2 : Exécuter les lignes de code suivantes pour lancer le server
		conda activate
		python ./manage.py runserver
	
	Étape 4 : Cliquez sur le lien obtenu et vous avez accès au site


En cas d'erreurs vérifié les librairies manquantes ainsi que la version de python utilisée.