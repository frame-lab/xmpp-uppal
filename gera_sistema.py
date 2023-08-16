def generate_code():
    classes_with_two_indices = ['XMPPStreamSetupServer', 'Sender', 'Receiver', 'Server', 'XMPPStreamFinalizationServer']
    classes_with_one_index = [
        'XMPPStreamSetupSender', 'XMPPStreamSetupReceiver', 'TLSClient', 
        'TLSServer', 'SASLClient', 'SASLServer', 'XMPPStreamFinalizationSender', 
        'XMPPStreamFinalizationReceiver'
    ]

    # Generate code lines for classes with one index
    lines = []
    for cls in classes_with_one_index:
        for i in range(1, 3): # 1 and 2
            if cls in ['TLSClient', 'TLSServer', 'SASLClient', 'SASLServer'] or (cls in ['XMPPStreamSetupSender', 'XMPPStreamFinalizationSender', 'XMPPStreamFinalizationReceiver'] and i == 1):
                lines.append(f"{cls}{i} = {cls}({i-1});")
            else:
                lines.append(f"{cls}{i} = {cls}({2-i});")
    
    # Generate code lines for classes with two indices
    for cls in classes_with_two_indices:
        for i in range(1, 3): # 1 and 2
            lines.append(f"{cls}{i} = {cls}({i-1},{2-i});")
    
    # Add system line
    instances = [f"{cls}{i}" for cls in classes_with_one_index + classes_with_two_indices for i in range(1, 3)]
    system_line = "system " + ','.join(instances) + ";"

    # Combine all lines
    code = '\n'.join(lines) + '\n' + system_line
    return code

print(generate_code())
