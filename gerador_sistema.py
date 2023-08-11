def generate_code(num_clients):
    output = []

    # Geração de Sender, Receiver e Server
    for i in range(1, num_clients*2,2):
        output.append(f"Sender{(i+1)//2} = Sender({i-1},{i});")
        output.append(f"Receiver{(i+1)//2} = Receiver({i}, {i-1});")
        output.append(f"Server{(i+1)//2} = Server({i-1},{i});")
        output.append("")

    # Geração de SASLClient e SASLServer
    for i in range(1, num_clients+1):
        output.append(f"SASLClient{i} = SASLClient({i-1});")
        output.append(f"SASLServer{i} = SASLServer({i-1});")
        output.append("")

    # Geração de TLSClient e TLSServer
    for i in range(1, num_clients+1):
        output.append(f"TLSClient{i} = TLSClient({i-1});")
        output.append(f"TLSServer{i} = TLSServer({i-1});")
        output.append("")

    # Gerar a linha final de sistema
    system_items = []
    for i in range(1, num_clients+1):
        system_items.extend([f"Sender{i}", f"Receiver{i}", f"Server{i}", 
                             f"SASLClient{i}", f"SASLServer{i}", 
                             f"TLSClient{i}", f"TLSServer{i}"])

    output.append("system " + ", ".join(system_items) + ";")

    return "\n".join(output)

# Solicitar número de clientes
num_clients = 3
print(generate_code(num_clients))
