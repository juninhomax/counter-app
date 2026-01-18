Guide : Configurer un serveur HTTP dans OpenHands accessible depuis Windows
Architecture
Windows Host
    └── WSL
        └── Docker Desktop
            ├── LM Studio (mistralai/devstral-small-2505) sur port 1234
            └── OpenHands Containers
                ├── openhands-app (interface web)
                └── oh-agent-server-* (environnement d'exécution)
Problème à comprendre
Quand vous lancez OpenHands avec Docker, deux types de conteneurs sont créés :

openhands-app : Le conteneur principal qui héberge l'interface web (port 3000)
oh-agent-server-* : Le conteneur d'exécution où votre code s'exécute réellement
Le piège des ports mappés
Quand vous ajoutez -p 5000:5000 à la commande Docker, ce port est mappé sur le conteneur openhands-app, PAS sur l'agent-server où votre code Python s'exécute !

C'est pourquoi un serveur HTTP lancé dans le terminal OpenHands ne sera pas accessible via un port que vous mappez manuellement.

Solution : Utiliser les ports pré-mappés de l'agent-server
L'agent-server mappe automatiquement ces ports :

Port dans le conteneur	Port sur Windows/WSL	Usage typique
8000	Port dynamique (ex: 58747)	Port principal
8001	Port dynamique (ex: 49157)	Port secondaire
8011	Port dynamique (ex: 46069)	Recommandé pour HTTP server
8012	Port dynamique (ex: 37215)	Port alternatif
Procédure complète
1. Lancer OpenHands
bash
docker run -it --rm --pull=always \
  -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.openhands.dev/openhands/runtime:1.2-nikolaik \
  -e SANDBOX_TYPE=exec \
  -e LOG_ALL_EVENTS=true \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v ~/.openhands:/.openhands \
  -p 3000:3000 \
  --add-host host.docker.internal:host-gateway \
  --name openhands-app \
  docker.openhands.dev/openhands/openhands:1.2
2. Identifier les ports mappés
Une fois OpenHands démarré, dans votre terminal WSL :

bash
docker ps
Cherchez le conteneur oh-agent-server-* et notez les ports mappés :

CONTAINER ID   IMAGE                                           PORTS
2b6fd8341b53   ghcr.io/openhands/agent-server:10fff69-python   0.0.0.0:58747->8000/tcp, 
                                                                0.0.0.0:49157->8001/tcp, 
                                                                0.0.0.0:46069->8011/tcp, ← Ce port !
                                                                0.0.0.0:37215->8012/tcp
Dans cet exemple, le port 8011 du conteneur est mappé sur le port 46069 de votre Windows.

3. Lancer votre serveur HTTP dans OpenHands
Dans le terminal OpenHands (accessible via l'interface web) :

bash
# Naviguez vers votre projet
cd /workspace/project/counter-app

# Lancez le serveur sur le port 8011 (ou 8012)
python3 -m http.server 8011
Vous devriez voir :

Serving HTTP on 0.0.0.0 port 8011 (http://0.0.0.0:8011/) ...
4. Accéder depuis votre navigateur Windows
Ouvrez votre navigateur et allez sur :

http://localhost:46069
(Remplacez 46069 par le port correspondant à 8011 dans votre docker ps)

Ports recommandés
✅ Ports à utiliser
8011 (recommandé) - Généralement libre
8012 (alternatif) - Généralement libre
❌ Ports à éviter
8000 - Utilisé par l'agent-server lui-même
8001 - Souvent occupé par des services internes
5000, 3001, 8080, etc. - Non mappés par défaut sur l'agent-server
Dépannage
Le port est déjà utilisé
bash
OSError: [Errno 98] Address already in use
Solution : Essayez un autre port (8011 ou 8012)

Rien ne s'affiche dans le navigateur
Vérifiez que le serveur tourne dans le terminal OpenHands
Vérifiez le mapping des ports avec docker ps
Utilisez le bon port mappé (celui qui correspond à 8011 ou 8012)
Essayez http://localhost:PORT (pas https://)
Le conteneur agent-server n'apparaît pas
Solution : Créez une nouvelle conversation/session dans OpenHands. L'agent-server est créé dynamiquement quand vous démarrez une session de travail.

Alternative : Utiliser l'onglet Browser d'OpenHands
Si vous voulez que l'agent IA visualise et interagisse avec votre application :

Lancez votre serveur sur n'importe quel port (ex: 5000)
Dans le chat OpenHands, demandez :
   Use the browser tool to navigate to http://localhost:5000
L'onglet Browser affichera votre application
Note : L'onglet Browser est contrôlé par l'agent IA, pas par vous directement. Il est utile pour les tests automatisés.

Configuration avec LM Studio
Si vous utilisez un modèle local via LM Studio :

Dans les Settings d'OpenHands :
Base URL : http://host.docker.internal:1234/v1
Model : mistralai/devstral-small-2505
API Key : lm-studio (ou n'importe quelle valeur)
Le flag --add-host host.docker.internal:host-gateway permet au conteneur d'accéder à LM Studio sur votre machine hôte.

Résumé rapide
bash
# 1. Lancer OpenHands
docker run -it --rm --pull=always \
  -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.openhands.dev/openhands/runtime:1.2-nikolaik \
  -e SANDBOX_TYPE=exec \
  -e LOG_ALL_EVENTS=true \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v ~/.openhands:/.openhands \
  -p 3000:3000 \
  --add-host host.docker.internal:host-gateway \
  --name openhands-app \
  docker.openhands.dev/openhands/openhands:1.2

# 2. Identifier le port mappé
docker ps | grep oh-agent-server

# 3. Dans le terminal OpenHands
cd /workspace/project/votre-projet
python3 -m http.server 8011

# 4. Ouvrir dans Windows
# http://localhost:PORT_MAPPE
Références
Documentation OpenHands
OpenHands GitHub
Date de création : 18 janvier 2026
Architecture testée : Windows + WSL + Docker Desktop + LM Studio + OpenHands 1.2

