# Codage mots de passe en RSA
Ce projet est un programme **Python** permemttant de saisir, coder, stocker de manière sécuriser  et gérer les identifiants et mots de passe d'un utilisateurs.
**Fonctionnalités principales:

**Saisi sécurisée des données de connexion** : L'utilisateur, en executant le programme, fait face à un menu où il a le choix entre différentes actions. Il peut choixir de saisir de nouvelles informations de connexion : il lui est donc demandé de fournir le site ou service auquel donnent accès ces informations de connexion, ainsi que son identifiant ou mot de passe; à chaque saisi la possibilité est laissée à l'utilisateur de revenir sur son choix ou saisir une information différente.

**Codage à l'aide de la méthode RSA** : La méthode RSA est extrêmement utilisée en cryptographie, nous en proposons ici une utilisation pour coder les identifiants et mots de passe. Le programme selectionne des nombres premiers et réalise l'ensemble des calculs d'arithmétique nécessaires pour la sécurisation des mots de passe. Les informations codées sont stockées dans une base de données ("base_de_données_mdp.csv") tandis que la clef privée de décodage est enregistrée dans une autre base de données séparée ("decryptage_mdp.csv").

**Gestion personnelle par l'utilisateur** : On propose à l'utilisateur de gérer ses informations en rajoutant de nouvelles, en les mettant à jour ou en les supprimant. L'utilisateur peut également choisir d'afficher ses informations de connexion, pour se les remémorer par exemple. Tout est fait de manière sécurisée pour éviter que l'utilisateur saisisse un doublon ou demande d'afficher des informations inexistantes.


**Strucure du projet :
Ce programme est structuré en 2 programmes complémentaires, la division s'est faite en vue de faciliter la relécture et de ne pas saturer le code.
**AuxiliairesRSA.py** : Ce programme contient l'ensemble des fonctions de saisi, de vérification ainsi que de calculs.

**Programme_principal.py** : Ce programme fait à maintes reprises appel au code précédent. On y propose un menu de fonctionnalités à l'utilisateur, qui est guidé vers telle ou telle fonction selon ses réponses. Il existe une fonction de saisie de nouvelles informations, une fonction de mise à jour, une fonction de suppression ainsi qu'une fonction d'affichage.

**Langage :** Python 

**Librairies Data :** Pandas

**Librairie cryptologie :** Secrets


   par Mohammed T, étudiant en L1 MIASHS à la faculté d'Economie et Gestion d'Aix-en-Provence
                                                                        le 26/06/2026



