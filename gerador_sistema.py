
import random

message_options = ['IQ_GET','IQ_SET','MESSAGE']

SENDER_ID = 0


def gerateRandomMessages(number_of_messages, num_clients):
    messages = []
    for _ in range(number_of_messages):
        chosen_message = message_options[random.randint(0,2)]
        chosen_message_destiny = random.randint(1,num_clients-1)
        messages.append("{" + f"{SENDER_ID}, {chosen_message_destiny}, {chosen_message}" + "}")
    return messages

def generate_code(num_clients):
    output = []

    # Geração de Sender, Receiver e Server
    output.append(f"Sender{0} = Sender({0});")
    output.append(f"Server{0} = Server();")
    output.append("")
    for i in range(1, num_clients):
        output.append(f"Receiver{i} = Receiver(0,{i},{errorProbability});")
        output.append(f"SenderStreamSetup{i} = SenderStreamSetup({0},{i});")
        output.append(f"ReceiverStreamSetup{i} = ReceiverStreamSetup({0},{i});")
        output.append("")
    
    system_items = []
    for output_item in output:
        output_item_split = output_item.split("=")
        if len(output_item_split) > 1:
            system_items.append(output_item_split[0].strip())

    output.append("system " + ", ".join(system_items) + ";")

    return "\n".join(output)

# Solicitar número de clientes
num_clients = 4
errorProbability = 0
print(generate_code(num_clients))

print('')
print('{'+', '.join(gerateRandomMessages(10, num_clients))+ '}')