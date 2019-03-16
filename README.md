# Genetic Algo

This is a project aiming to manually code a genetic algorithm, to present its principle to my data colleagues 👍🏼

# Veille data - Algorithmes génétiques
12/03/2019
****

## Plan :
1) Introduction du **principe** de l’algorithme, solution à quels types de problèmes (comparaison avec l’évolution de Darwin)
	
	1.1) Problèmes non-supervisés
	1.2) Sélection naturelle (générations)

2) **Définitions** et **explications** des grandes étapes (métaphore filée avec la génétique) 

	2.1) Population initiale 
	2.2) Fonction fitness 
	2.3) Sélection
	2.4) Crossover 
	2.5) Mutation 
	2.6) Terminaison

3) Application sur un **exemple** :

	-> Sourcing agences

4) Applications chez Evaneos : 

	-> Recommendation de desti 
	-> Optimisation de paramètres en Machine Learning 

****

## Développement :

### 1) Introduction

	Les algorithmes génétiques font partie de la famille des algorithmes évolutionnistes. Pour info : algorithmes évolutionnistes = algorithmes qui s’inspirent de la ::théorie de l’évolution de Darwin:: pour résoudre des problèmes. C’est-à-dire donc, que lors de la résolution d’un problème l’algorithme va fonctionner sous forme d’itérations, et à chaque itération (penser génération), seules les meilleures solutions seront retenues et participeront à la création des solutions de la génération suivante (d’où l’idée de ::génétique::). 

	Ces algorithmes sont utilisés lors de la recherche de solution à des ::problèmes d’optimisation:: pour lesquels ils n’existent pas de méthode exacte ou que la solution est inconnue. 

	Métaphore  filée avec la génétique pour permettre une meilleure compréhension.

### 2) Les grandes étapes

#### 2.1) La population initiale 

		Après défini le problème auquel on souhaite répondre, on va 	définir ce qu’on appelle notre population initiale. Celle-ci consiste en un nombre défini arbitrairement de solutions potentielles au problème.  Chaque solution sera nommée ::« individu »::.

		Pour faire la comparaison avec la génétique on va définir les termes utilisés lors de la présentation :

[image:AF5023FB-A4E2-429A-B26B-83B9D9EC6B2E-3336-0000047DC9974C04/Capture d’écran 2019-03-15 à 11.44.54.png]

		
	Chez l’Homme, les ::chromosomes:: présent dans le noyau de nos cellules vont coder l’entièreté des informations nécessaires à la formation de notre être. Les chromosomes sont tout simplement des ::chaînes d’ADN::. L’ADN est quant à lui, une chaîne de ::multiples gènes::. Ce sont donc les gènes qui codent toute l’information de notre système. 

	Dans notre algorithme, nous aurons constamment un pool de solutions que l’on va faire évoluer jusqu’à trouver la meilleure solution à notre problème. Les ::solutions::, les individus, sont semblables aux chromosomes chez l’Homme, et les ::caractéristiques:: d’une solution (que l’on définira en fonction de notre problème) sont donc semblables aux gènes au sein d’un chromosome. 

	La première étape, de notre algorithme est donc de générer aléatoirement une première population, un nombre d’individus, de solutions au problème. 

#### 2.2) La fonction fitness

	 Comme mentionné précédemment l’algo va fonctionner sous forme d’itérations. A chaque itération ou génération on va tester l’ensemble de nos solutions, et pour cela il faut un outil pour évaluer les solutions. C’est ce que l’on va appeler la ::fonction fitness:: ( à ne pas confondre avec le fait de faire 22 tractions à la salle). 

	Il va alors falloir définir une fonction qui est en mesure de prendre en input les caractéristiques de nos individus et de ressortir un score. Généralement, la probabilité que l’individu soit choisi pour la génération suivante (*ie* survivre à la sélection naturelle) est liée à ce score. Plus le score est haut, plus l’individu aura de chances d’être sélectionné.

#### 2.3) La sélection (create the mating pool)

		La sélection est l’étape durant laquelle les individus de notre population vont  être choisis pour transmettre leurs informations aux générations précédentes.  

		Lors de la sélection on va généralement former une paire de deux individus avec des bons fitness scores qui vont former les parents des individus de la génération suivante.

		Il existe 2 principales approches à la formation de ces paires. D’une part la sélection basée sur la fitness score : la probabilité d’être sélectionné est proportionnelle au fitness score (::Fitness Proportionate Selection::) . D’autre part, la sélection (::Tournament Selection::) durant laquelle, on sélectionne des groupes d’individus, et parmi ces groupes l’individu avec le plus haut score sera considéré comme premier parent, et idem pour la sélection du deuxième parent. 

		**NB:** On peut parfois ajouter un système ::« d’élitisme »:: via lequel on sélectionne d’office nos x% meilleurs individus.

#### 2.4) Le cross-over
	
			Il est temps pour les parents de générer leurs descendants à la fin de notre itération. On commence par déterminer un ::crossover point::.  

[image:74EEEE4F-9070-4067-AF06-D9A84D15C6E1-3336-000009A2D57DF250/Capture d’écran 2019-03-15 à 13.18.59.png]

[image:1A377695-A9D6-4B7F-A14F-9EA62E27C6CA-3336-000009A46F9D10AD/Capture d’écran 2019-03-15 à 13.19.05.png]
 
Formation des descendants :

[image:D10BC9B6-A97B-4D4F-9816-650CA28BA15F-3336-000009A682C03FDF/Capture d’écran 2019-03-15 à 13.19.11.png]
		
#### 2.5) La mutation

			Si l’on réalise seulement l’étape de cross-over on prend le risque d’aboutir à une ::convergence locale::, c’est-à-dire qu’on prend le risque de combiner souvent les mêmes parents et avec un peu de malchance on choisit toujours les mêmes crossover point. 

			C’est pourquoi on peut introduire le concept de mutation, que l’on retrouve encore une fois en génétique, avec le concept du même nom qui est en mesure de modifier l’information portée par les gènes. 

			Ainsi, on pourra aléatoirement modifier certaines caractéristiques d’individus dans notre population. 

[image:B3B6A58B-87D6-4345-827B-9423285EC0E6-3336-00000C9C5251CDC4/Capture d’écran 2019-03-15 à 15.13.11.png]

####  2.6) La terminaison
			
			L’algorithme atteint son terme lorsque notre population d’étude, nos solutions convergent, càd que d’une génération à une autre la population ne change plus vraiment. 

			Cette convergence peut-être déterminée de plusieurs manières différentes : soit l’on définit *à priori* le nombre de générations que l’on souhaite générer, soit l’on définit un *seuil* au dessous duquel on souhaite trouver un **score de fitness**.


### 3) Application sur un exemple - Sourcing d’agences

Présentation du problème : 

	Imaginons qu’un/une employé(e) d’Evaneos parte à la conquête d’un nouveau pays pour y sourcer des agences. Cette personne a 5 jours pour visiter 6 agences situées dans des villes différentes et éloignées. A priori cela relève de l’impossible, il faudrait imaginer LE parcours optimal qui permettrait de visiter ces agences dans les temps données.

		
[image:F107CE2C-9D4F-45C6-9C63-B78085B034EE-3336-000012DC50D9BFD6/Capture d’écran 2019-03-15 à 17.07.59.png]


	Dans ce cas l’algorithme génétique est une solution à ce problème. En effet, on a *à priori* pas la réponse à cette question (ici on n’a pas bcp de villes à visiter mais ça peut être beaucoup plus long).
	
	On a un total de ::6! = 720:: possibilités de routes différentes pour visiter les 6 villes dans un ordre précis. Laquelle de ces combinaisons est le plus rapide ? 





