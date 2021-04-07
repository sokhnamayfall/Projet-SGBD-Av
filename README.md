# Projet-SGBD-Av
Covid-19 progression modeler est un projet de classe basé sur les SGBDs . 
Ce projet a pour objectif de faciliter l'analyse de l'évolution du covid-19 au sénégal.
Description
L’année 2020 et 2021 sont marquées par la progression du COVID 19. Afin d’informer la population sénégalaise, chaque jour un communiqué de presse est diffusé en ligne par le Ministère de la Santé et de l’Action Sociale du Sénégal.
Un groupe de scientifique désireux de regrouper et analyser ces données pour la compréhension de sa diffusion dans le territoire sénégalais engage un groupe de développeurs pour concevoir et développer une solution permettant de modéliser son évolution spatiale et temporelle.
La solution envisagée est un système intégré devant répondre au cahier des charges fonctionnelles qui suit.
Il est présenté ici sous la forme de l’architecture du système ainsi que des fonctionnalités attendues par l’utilisateur. On trouvera ainsi dans la description des modules attendues et la présentation des fonctionnalités / différents usages possibles.
Architecture logique
Le système à développer devra être composé de 4 modules utilisables séquentiellement, à savoir :
- Le module DataAcquisition
- Le module DataLoader
- Le module DataExplorer
- Le module EvolutionAnalyzer.
o DataAcquisition:
Utilisant les sources de données officielles, ce module permettra de :
• télécharger des fichiers pdfs et/ou des images des communiqués officiels du ministère de la santé dans un répertoire local
• parcourir , extraire et agréger au fur et à mesure des téléchargements des fichiers, les données qu’elles contiennent pour les stocker dans des fichiers mensuels (Json ou fichiers XML en fonction du besoin de l’utilisateur ) respectant la hiérarchie suivante :
o Année-Mois//NomDuFichier
▪ Date1 : NbTest, Nb nouveaux Cas , Nb Cas contacts, Nb Cas Communautaires, Nb
Guéris, Nb Décès, NomFichierSource, DateHeureExtraction
• Localité : NomLocalité , NbCas
Rqe : il vous est possible de proposer des champs supplémentaires en cohérence avec l’objectif du projet Sources de données officielles à considérer :
- Sur twitter en image : https://twitter.com/MinisteredelaS1
- Sur son site internet en document pdf : http://www.sante.gouv.sn/actualites
o DataLoader
Ce module permet le chargement des données téléchargées vers un serveur de base de données relationnelles en ligne. Ainsi dans ce module, l’utilisateur peut voir la liste des fichiers obtenus dans le module précédent et parcourir leur arborescence et prévisualiser les données . Grâce à des cases à cocher sur les différents jours, il lui est loisible de sélectionner les dates à importer vers le SGBD. Il peut décider si les données seront chargées par lot et en mode transactionnel ou pas. Dans ce dernier cas il doit avoir la possibilité de valider à la fin du processus les données importées, ou bien annuler tout le processus bien que les données soient déjà sur le serveur et ainsi les effacer.
En cas de duplication de données, il lui est proposé d’écraser les nouvelles données ou ignorer les nouvelles données.
Le chargement des données devant être intelligent, chaque localité doit être associée dans la base de données au niveau administratif lui correspondant (commune, département, région, ville , etc.), afin de supporter le fait que les communiqués dans le temps aient changé de format et ne comportent pas toujours les mêmes localités.
o DataExplorer
En considérant les données issues du module précédent, le présent devra permettre de :
- Consulter sur une carte géographique l’évolution journalière du nombre de cas des régions du sénégal grâce à une barre temporelle.
  
- Sur le clique dans une région, de fournir une fenêtre flottante avec la répartition des types de cas de la région et un bouton détail. Le bouton détails donnera une vue comprenant :
o La courbe temporelle d’évolution des cas de la région,
o la carte de ses départements avec le dénombrement des cas leurs correspondants
- Télécharger en format image PNG la carte affichée ( nationale ou régionale) , pour une date choisie
- Télécharger en format SQL /CSV les données affichées par la carte en cours
o EvolutionAnalyzer
Grace aux données du système ce module permet d’interpréter partiellement l’évolution du Covid 19 sur le territoire en générant un graphe de flux spatio/temporel. Ce graphe est une représentation du chemin pris potentiellement par le covid pour se propager entre les régions.
Afin d’obtenir une image cohérente, ce module devra évaluer en base de données pour chaque département et pour chaque mois :
- la concentration du cumul de nombre de cas sur la population du département : Conc
- le taux de progression de ce cumul mensuel par rapport au mois précédent (Prog)
A l’apparition de nouveaux cas dans un département(i) , on considérera comme son origine le département (j) voisin avec le plus fort niveau taux de transmissibilité possible sur la base de la formule suivante :
𝑁𝑖𝑣𝑒𝑎𝑢 𝑑𝑒 𝑇𝑟𝑎𝑛𝑠𝑚𝑖𝑠𝑠𝑖𝑏𝑖𝑙𝑖𝑡é( 𝐷𝑒𝑝𝑡﷩𝑖﷩, 𝐷𝑒𝑝𝑡﷩𝑗﷩) 𝑃𝑟𝑜𝑔﷩𝑗﷩﷩𝐷𝑖𝑠𝑡𝑎𝑛𝑐𝑒( 𝐷𝑒𝑝𝑡﷩𝑖﷩, 𝐷𝑒𝑝𝑡﷩𝑗﷩)﷩
Le Département (j) ainsi obtenu sera considéré comme la source de contamination du département(i) et une flèche sera représentée sur la carte depuis le département (j) vers le département (i) avec comme annotations sur la flèche la date du premier cas de (i).
Le scenario de propagation du covid sera alors téléchargeable sous deux formats :
- graphique grace à un Fichier PNG representant la carte des départements du sénégal et les flêches obtenues par l’évaluation
- grace à un rapport sous forme texte décrivant la propagation du virus sous la forme suivante :
o Date : Departement i -> Departement j : NbCas
o...
o Datek:Departementorig->DepartementDest:NbCas
Afin de garantir une sécurisation du système chaque module disposera d’une authentification et de privilèges spécifiques qui devront aussi être décrits dans la documentation.
