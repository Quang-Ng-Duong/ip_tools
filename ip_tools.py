from utils import *

def main():
    print("=== IP Tools ===")
    print("1. IP Address Lookup")
    print("2. IP WHOIS Lookup")
    print("3. DNS Lookup")
    print("4. Reverse DNS Lookup")
    print("5. IP Blacklist Check")
    print("6. Hostname Lookup")
    print("7. Random IP Generator")
    print("8. Run API Server")

    choice = input("Choose a function (1-8): ")

    if choice == '1':
        ip = input("Enter IP: ")
        ip_lookup(ip)
    elif choice == '2':
        ip = input("Enter IP: ")
        whois_lookup(ip)
    elif choice == '3':
        domain = input("Enter domain: ")
        dns_lookup(domain)
    elif choice == '4':
        ip = input("Enter IP: ")
        reverse_dns(ip)
    elif choice == '5':
        ip = input("Enter IP: ")
        check_blacklist(ip)
    elif choice == '6':
        ip = input("Enter IP: ")
        hostname_lookup(ip)
    elif choice == '7':
        generate_random_ip()
    elif choice == '8':
        run_api()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
