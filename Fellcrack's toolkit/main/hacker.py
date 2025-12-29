import os
import requests
from colorama import Fore, Style, init


# Inicializar colorama
init(autoreset=True)

def hacker_news():
    os.system('''curl -s https://hacker-news.firebaseio.com/v0/newstories.json \
| jq -r '.[0:10][]' \
| while read id; do
    curl -s https://hacker-news.firebaseio.com/v0/item/$id.json
  done \
| jq -r '
  "\u001b[1;36m▶ " + .title + "\u001b[0m\n" +
  "\u001b[2;37m  " + (.url // ("https://news.ycombinator.com/item?id=" + (.id|tostring))) + "\u001b[0m\n"
'
''')

# Diccionario de servicios disponibles
AVAILABLE_SERVICES = {
    "github": {"url": "https://www.githubstatus.com", "type": "statuspage"},
    "cloudflare": {"url": "https://www.cloudflarestatus.com", "type": "statuspage"},
    "discord": {"url": "https://discordstatus.com", "type": "statuspage"},
    "zoom": {"url": "https://status.zoom.us", "type": "statuspage"},
    "atlassian": {"url": "https://status.atlassian.com", "type": "statuspage"},
    "dropbox": {"url": "https://status.dropbox.com", "type": "statuspage"},
    "slack": {"url": "https://status.slack.com", "type": "statuspage"},
    "reddit": {"url": "https://www.redditstatus.com", "type": "statuspage"},
    "twitch": {"url": "https://status.twitch.tv", "type": "statuspage"},
    "notion": {"url": "https://status.notion.so", "type": "statuspage"},
    "figma": {"url": "https://status.figma.com", "type": "statuspage"},
    "vercel": {"url": "https://www.vercel-status.com", "type": "statuspage"},
    "stripe": {"url": "https://status.stripe.com", "type": "statuspage"},
    "heroku": {"url": "https://status.heroku.com", "type": "statuspage"},
    "datadog": {"url": "https://status.datadoghq.com", "type": "statuspage"},
    "mongodb": {"url": "https://status.mongodb.com", "type": "statuspage"},
    "gitlab": {"url": "https://status.gitlab.com", "type": "statuspage"},
    "npm": {"url": "https://status.npmjs.org", "type": "statuspage"},
    "docker": {"url": "https://status.docker.com", "type": "statuspage"}
}

def _check_statuspage_service(service_name, base_url):
    """Verifica servicios que usan el formato StatusPage.io (función interna)"""
    try:
        # Estado actual
        print(f"{Fore.YELLOW}Connecting to {service_name}...")
        status_response = requests.get(f"{base_url}/api/v2/status.json", timeout=15)
        
        if status_response.status_code != 200:
            print(f"{Fore.RED}Error: Service returned status code {status_response.status_code}")
            return
            
        status_data = status_response.json()
        
        print(f"\n{Fore.CYAN}{'='*50}")
        print(f"{Fore.YELLOW}Service: {Fore.WHITE}{Style.BRIGHT}{status_data['page']['name']}")
        
        # Color según el estado
        status_desc = status_data['status']['description']
        if "Operational" in status_desc:
            status_color = Fore.GREEN
        else:
            status_color = Fore.RED
            
        print(f"{Fore.YELLOW}Current Status: {status_color}{Style.BRIGHT}{status_desc}")
        print(f"{Fore.YELLOW}Indicator: {Fore.WHITE}{status_data['status']['indicator']}")
        print(f"{Fore.YELLOW}Last Update: {Fore.WHITE}{status_data['page']['updated_at']}")
        
        # Última caída
        incidents_response = requests.get(f"{base_url}/api/v2/incidents.json", timeout=15)
        incidents_data = incidents_response.json()
        
        if incidents_data['incidents']:
            incident = incidents_data['incidents'][0]
            print(f"\n{Fore.MAGENTA}{Style.BRIGHT}--- Last Outage ---")
            print(f"{Fore.YELLOW}Incident: {Fore.WHITE}{incident['name']}")
            print(f"{Fore.YELLOW}Date: {Fore.WHITE}{incident['created_at']}")
            
            # Color según estado del incidente
            if incident['status'] == 'resolved':
                incident_color = Fore.GREEN
            else:
                incident_color = Fore.RED
                
            print(f"{Fore.YELLOW}Status: {incident_color}{Style.BRIGHT}{incident['status']}")
            
            # Color según impacto
            impact_colors = {
                'none': Fore.GREEN,
                'minor': Fore.YELLOW,
                'major': Fore.RED,
                'critical': Fore.RED + Style.BRIGHT
            }
            impact_color = impact_colors.get(incident['impact'], Fore.WHITE)
            
            print(f"{Fore.YELLOW}Impact: {impact_color}{Style.BRIGHT}{incident['impact']}")
        else:
            print(f"\n{Fore.GREEN}No recent incidents found")
            
        print(f"{Fore.CYAN}{'='*50}\n")
        
    except requests.exceptions.Timeout:
        print(f"\n{Fore.RED}Error: Request timeout. The service is not responding.")
        print(f"{Fore.YELLOW}The service might be down or the API is not available.\n")
    except requests.exceptions.ConnectionError:
        print(f"\n{Fore.RED}Error: Could not connect to the service.")
        print(f"{Fore.YELLOW}The service might not have a public status API.\n")
    except requests.exceptions.RequestException as e:
        print(f"\n{Fore.RED}Error: Network error - {str(e)}\n")
    except KeyError as e:
        print(f"\n{Fore.RED}Error: Invalid response format from the service.")
        print(f"{Fore.YELLOW}This service might use a different API format.\n")
    except Exception as e:
        print(f"\n{Fore.RED}Error: {str(e)}\n")

def _check_service_status(service_name, service_info):
    """Router para verificar diferentes tipos de servicios (función interna)"""
    service_type = service_info.get("type", "statuspage")
    base_url = service_info.get("url")
    
    if service_type == "statuspage":
        _check_statuspage_service(service_name, base_url)
    else:
        print(f"{Fore.YELLOW}Service type '{service_type}' not yet implemented.")

def _show_available_services():
    """Muestra la lista de servicios disponibles (función interna)"""
    print(f"\n{Fore.CYAN}{'='*50}")
    print(f"{Fore.GREEN}{Style.BRIGHT}Available Services ({len(AVAILABLE_SERVICES)}):")
    print(f"{Fore.CYAN}{'='*50}")
    
    # Mostrar en columnas
    services = sorted(AVAILABLE_SERVICES.keys())
    col1, col2 = services[:len(services)//2], services[len(services)//2:]
    
    for s1, s2 in zip(col1, col2):
        print(f"{Fore.YELLOW}  • {Fore.WHITE}{s1.capitalize():<20} {Fore.YELLOW}• {Fore.WHITE}{s2.capitalize()}")
    
    # Si hay un número impar, mostrar el último
    if len(services) % 2 != 0:
        print(f"{Fore.YELLOW}  • {Fore.WHITE}{services[-1].capitalize()}")
    
    print(f"{Fore.CYAN}{'='*50}\n")

def check_services():
    """
    Sistema completo de verificación de servicios caídos.
    Esta es la única función que necesitas llamar para ejecutar todo el sistema.
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}")
    print("╔════════════════════════════════════════════════╗")
    print("║       SERVICE STATUS CHECKER v1.1              ║")
    print("╚════════════════════════════════════════════════╝")
    print(Style.RESET_ALL)
    
    while True:
        print(f"{Fore.WHITE}Type {Fore.CYAN}'list'{Fore.WHITE} to see available services")
        print(f"Type {Fore.CYAN}'exit'{Fore.WHITE} to quit")
        
        user_input = input(f"\n{Fore.GREEN}Enter service name: {Fore.WHITE}").strip().lower()
        
        if user_input == 'exit':
            print(f"\n{Fore.CYAN}Thanks for using Service Status Checker! Goodbye! 👋\n")
            break
        elif user_input == 'list':
            _show_available_services()
            continue
        elif user_input == '':
            print(f"{Fore.YELLOW}Please enter a service name.\n")
            continue
        
        if user_input in AVAILABLE_SERVICES:
            service_info = AVAILABLE_SERVICES[user_input]
            _check_service_status(user_input, service_info)
        else:
            print(f"\n{Fore.RED}{Style.BRIGHT}╔════════════════════════════════════════════════╗")
            print(f"{Fore.RED}{Style.BRIGHT}║            404 Not Found Service               ║")
            print(f"{Fore.RED}{Style.BRIGHT}╚════════════════════════════════════════════════╝")
            print(f"{Fore.YELLOW}The service '{user_input}' is not in our database.")
            print(f"{Fore.YELLOW}Type 'list' to see available services.\n")

# Punto de entrada principal

def hacker_news():

    choice = input("What do you wanna do?")
    print('''
    .__________________________________.     
    |                                  |
    | [1] Check down services          |
    |__________________________________|
    |                                  |
    | [2] Look up last hacker news     |
    |__________________________________|

    ''')
    if choice == "1":
        check_services()
    elif choice == "2":
        hacker_news()
    else:
        print("That's not an option...")
