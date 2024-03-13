import socket

def get_ips_par_recherche_dns(cible, port=443):
    try:
        # Fait une recherche DNS pour la cible sur le port spécifié
        infos = socket.getaddrinfo(cible, port)
        # Extrait les adresses IP des informations
        ips = [info[4][0] for info in infos]
        return ips
    except socket.gaierror:
        print(f"Pas d'informations DNS pour la cible {cible}")
        return []

# Teste la fonction avec la cible "iut-acy.local"
print(get_ips_par_recherche_dns("iut-acy.local"))