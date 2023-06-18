import whois
import concurrent.futures

domains_path = "./domains.txt"
available_domains = "./available_domains.txt"
threads = 10


def write_to_available(url: str):
    with open(available_domains, "a") as df:
        df.write(url + "\n")


def perform_whois_lookup(domain):
    try:
        whois.whois(domain)
    except:
        write_to_available(domain)


with open(domains_path) as f:
    domains = [line.strip() for line in f]

with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
    futures = [executor.submit(perform_whois_lookup, domain) for domain in domains]
    concurrent.futures.wait(futures)
