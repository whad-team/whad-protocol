===============================================
Protocole ouvert pour tools de hacking wireless
===============================================

Ce document est un draft sujet à modification et commentaires.


Objectifs du protocole
======================

Ce protocole a pour objectif de permettre l'interopérabilité des équipements et des outils de hack wireless,
idéalement indépendamment du ou des technologies supportées. Il vise notamment à:

* faciliter l'interopérabilité des outils (firmware/cli)
* être compatible avec un maximum de langages de développement (portabilité)
* optimiser la taille des échanges tout en permettant l'évolutivité


Draft de solution
=================


Layer physique
--------------

L'utilisation de Protocol Buffers pour la sérialisation/désérialisation semble être adaptée:

* supporté par la grande majorité des langages
* langage de formalisation des messages
* sérialisation/désérialisation optimisée (varint, etc.)

Néanmoins, il pourrait être judicieux d'avoir une surcouche permettant d'envoyer et recevoir des chunks de données
gérant la fragmentation. 


Domaines, capacités et messages
-------------------------------

### Domaines

Vu que le protocole a vocation à être utilisé pour divers protocoles wireless, il serait intéressant d'y inclure
la notion de *domaine*. Un *domaine* correspondrait ainsi à un protocole, et serait associé à un ensemble de
messages.

De cette manière, il sera possible dans le futur d'ajouter de nouveaux protocoles et les messages associés.


### Capacités

Chaque device implémentant ce protocole implémente un jeu de messages de base, peu importe les domaines qu'il supporte.
Ce jeu de messages permet:

* d'identifier formellement le device en question: sa version de firmware, la version du protocole supportée
* de récupérer le ou les domaines supportés
* de récupérer les capacités par domaine
* de récupérer les commandes supportées par domaine

Ce protocole de découverte permet ainsi à un outil exécuté sur un hôte de déterminer si un device connecté peut être utilisé pour réaliser une ou plusieurs actions, sans avoir à se soucier du device ou de son firmware.

### Messages

Pour chaque domaine, un ensemble de messages normalisés est défini en fonction du domaine et des opérations qui peuvent
être réalisées sur ce dernier. 

Bon, va falloir formaliser tout ça ! => C'est franchement le gros du boulot ...




