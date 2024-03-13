import dns.resolver

def dns_query(cible, record_type):
    try:
        answers = dns.resolver.query(cible, record_type)
        for rdata in answers:
            print(f"{record_type} enregistrements pour {cible}: {rdata}")
    except dns.resolver.NoAnswer:
        print(f"Pas d'enregistrements {record_type} pour {cible}")
    except dns.resolver.NXDOMAIN:
        print(f"Le domaine {cible} n'existe pas")

cible = "iut-acy.local"
record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]

for record_type in record_types:
    dns_query(cible, record_type)



    