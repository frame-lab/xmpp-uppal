import random
import argparse

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
        output.append(f"Receiver{i} = Receiver(0,{i},{error_probability});")
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

def main():
    parser = argparse.ArgumentParser(description='Gerador de sistema XMPP')
    parser.add_argument('--num_clients', type=int, required=True, help='Número de clientes')
    parser.add_argument('--error_probability', type=int, required=True, help='Probabilidade de erro')
    parser.add_argument('--num_messages', type=int, required=True, help='Número de mensagens')
    args = parser.parse_args()

    global error_probability
    error_probability = args.error_probability
    num_clients = args.num_clients
    num_messages = args.num_messages

    print(generate_code(num_clients))
    print('')
    print('{' + ', '.join(gerateRandomMessages(num_messages, num_clients)) + '}')

if __name__ == '__main__':
    main()