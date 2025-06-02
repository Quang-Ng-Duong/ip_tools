import socket, random, requests
import dns.resolver
from ipwhois import IPWhois
from flask import Flask, request, jsonify

def ip_lookup(ip):
    try:
        hostname = socket.gethostbyaddr(ip)
        print(f"Hostname: {hostname[0]}")
    except:
        print("IP lookup failed.")

def whois_lookup(ip):
    try:
        obj = IPWhois(ip)
        results = obj.lookup_rdap()
        print(results['network'])
    except Exception as e:
        print(f"WHOIS failed: {e}")

def dns_lookup(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        for ipval in result:
            print(f"IP: {ipval.to_text()}")
    except:
        print("DNS lookup failed.")

def reverse_dns(ip):
    try:
        host = socket.gethostbyaddr(ip)
        print(f"Hostname: {host[0]}")
    except:
        print("Reverse DNS failed.")

def check_blacklist(ip):
    print(f"Check IP {ip} at https://www.abuseipdb.com/check/{ip}")

def hostname_lookup(ip):
    try:
        host = socket.gethostbyaddr(ip)
        print(f"Hostname: {host[0]}")
    except:
        print("Hostname lookup failed.")

def generate_random_ip():
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    print(f"Random IP: {ip}")

def run_api():
    app = Flask(__name__)

    @app.route("/ip-lookup")
    def api_ip_lookup():
        ip = request.args.get("ip")
        try:
            hostname = socket.gethostbyaddr(ip)
            return jsonify({"hostname": hostname[0]})
        except:
            return jsonify({"error": "Lookup failed"}), 400

    app.run(port=5000)
