
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

*Propositions de Domaines*

* Bluetooth
* Bluetooth Low Energy
* 802.15.4
    - Zigbee
    - Sixlowpan
* Enhanced ShockBurst
    - Logitech Unifying
* Mosart
* ANT
    - ANT+
    - ANT-FS
* Generic

### Capacités

Chaque device implémentant ce protocole implémente un jeu de messages de base, peu importe les domaines qu'il supporte.
Ce jeu de messages permet:

* d'identifier formellement le device en question: sa version de firmware, la version du protocole supportée
* de récupérer le ou les domaines supportés
* de récupérer les capacités par domaine
* de récupérer les commandes supportées par domaine

Ce protocole de découverte permet ainsi à un outil exécuté sur un hôte de déterminer si un device connecté peut être utilisé pour réaliser une ou plusieurs actions, sans avoir à se soucier du device ou de son firmware.

#### Capacités Bluetooth Low Energy
* Bas niveau
	* sniffing des advertisements
	* sniffing de connection (observation de l'initiation)
	* sniffing de connection (inférence des paramètres)
	* injection de paquet directe
	* injection de paquet au sein d'une connection (vers slave)
	* injection de paquet au sein d'une connection (vers master)
	* hijacking d'un rôle au sein d'une connection  (slave)
	* hijacking d'un rôle au sein d'une connection (master)
	* établissement d'un Man-in-the-Middle (avant initiation)
	* établissement d'un Man-in-the-Middle (connection établie)
	* jamming d'une connection
	* jamming des advertisements
	* reactive jamming  (?)
* Haut niveau
	* simulation d'un Scanner
	* simulation d'un Advertiser
	* simulation d'un Central
	* simulation d'un Peripheral

#### Capacités 802.15.4 (Zigbee)

* Bas niveau
	* Jamming d'un canal
	* Reactive jamming
	* Injection de paquet (avec contrôle du FCS)
	* Injection de paquet (sans contrôle du FCS)
	* Sniffing de paquet
	* établissement d'un Man-in-the-Middle
* Haut niveau
	* simulation d'un End Device
	* simulation d'un Coordinator
	* simulation d'un Router

#### Capacités Enhanced ShockBurst

* Bas niveau
	* jamming d'un canal
	* Reactive jamming
	* Injection de paquet
	* Sniffing de paquet (sans connaissance préalable de l'adresse)
	* Sniffing de paquet (avec connaissance préalable de l'adresse)
* Haut niveau
	* simulation d'un PRX
	* simulation d'un PTX

##### Capacités Logitech Unifying
* sniffing de l'appairage
* simulation d'un clavier (PTX, traffic chiffré)
* simulation d'une souris (PTX, traffic non chiffré)
* simulation d'un dongle (PRX, traffic chiffré)
* établissement d'un Man-in-the-Middle

#### Capacités Mosart
* Bas niveau
	* jamming d'un canal
	* Reactive jamming
	* Injection de paquet
	* Sniffing de paquet
* Haut niveau
	* simulation d'un dongle
	* simulation d'un clavier
	* simulation d'une souris

#### Capacités ANT
* Bas niveau
	* jamming d'un canal
	* Reactive jamming
	* Injection de paquet
	* Sniffing de paquet
	* Hijacking d'un master
	* Hijacking d'un slave
	* Établissement d'un Man-in-the-Middle

* Haut niveau
	* simulation d'un Master
	* simulation d'un Slave
	
#### Capacités Generic
* Bas niveau
	* sélection d'une fréquence (bande ? )
	* sélection d'une modulation (type: GFSK, 2-FSK, 4-FSK, QPSK, OQPSK, etc) et ses paramètres (déviation ?)
	* sélection d'un datarate (250kbps, 500kbps, 1Mbps, 2Mbps)
	* sélection d'un préambule
	* sélection d'une taille de paquets
	* Sniffing de paquet
	* Injection de paquet
	* Monitoring de l'activité d'un canal

### Messages
Pour chaque domaine, un ensemble de messages normalisés est défini en fonction du domaine et des opérations qui peuvent
être réalisées sur ce dernier. 

Bon, va falloir formaliser tout ça ! 
	=> C'est franchement le gros du boulot ...




