def generate_code(num_clients):
    output = []

    # Geração de Sender, Receiver e Server
    for i in range(1, num_clients,2):
        output.append(f"Sender{i} = Sender({i-1},{i});")
        output.append(f"Receiver{i} = Receiver({i}, {i-1});")
        output.append(f"Server{i} = Server({i-1},{i});")
        output.append("")
        output.append(f"Sender{i+1} = Sender({i},{i-1});")
        output.append(f"Receiver{i+1} = Receiver({i-1}, {i});")
        output.append(f"Server{i+1} = Server({i},{i-1});")
        output.append("")

    # Geração de SASLClient e SASLServer
    system_items = []
    for i in range(1, num_clients+1):
        output.append(f"SASLClient{i} = SASLClient({i-1});")
        output.append(f"SASLServer{i} = SASLServer({i-1});")
        output.append(f"TLSClient{i} = TLSClient({i-1});")
        output.append(f"TLSServer{i} = TLSServer({i-1});")
        output.append("")
        system_items.extend([f"Sender{i}", f"Receiver{i}", f"Server{i}", 
                             f"SASLClient{i}", f"SASLServer{i}", 
                             f"TLSClient{i}", f"TLSServer{i}"])

    output.append("system " + ", ".join(system_items) + ";")

    return "\n".join(output)

# Solicitar número de clientes
num_clients = 2
print(generate_code(num_clients))
