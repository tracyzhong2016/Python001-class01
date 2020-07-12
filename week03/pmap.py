import argparse
import socket
import subprocess
from concurrent.futures.thread import ThreadPoolExecutor

success_list = []

def get_open_tcp_port(ip_port_tuple):
    #获取开放的端口

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        result = s.connect_ex(ip_port_tuple)
    except Exception as e:
        print(e)
    s.close()
    if result==0:
        success_list.append(ip_port_tuple[1])
    else:
        return success_list

    save_to_file(success_list, './result.json')


def is_ping_connected(ip_address):
    # 是否ping通，如果是，打印ping的地址
    try:
        re = subprocess.run(["ping", ip_address, "-t", "2"],
                            capture_output=True)
        if re.returncode == 0:
            print(ip_address)
    except Exception as e:
        print('something wrong',e)


def task_generation(task_type,ip,n):

    if task_type=='tcp':
        seed = [(ip, port) for port in range(0, 2)]
        with ThreadPoolExecutor(n) as executor:
            executor.map(get_open_tcp_port, seed)
        print(f'IP地址{ip}的所有开放端口是：{success_list}\n')
    elif task_type == 'ping':
        if '-' in ip:
            start_ip, stop_ip = ip.split('-')
            start_last_num = start_ip.split('.')[-1]
            stop_last_num = stop_ip.split('.')[-1]
            start_head = start_ip.rstrip(start_last_num).rstrip('.')
            seed = [start_head + '.' + str(num) for num in range(int(start_last_num), int(stop_last_num) + 1)]
            with ThreadPoolExecutor(n) as executor:
                executor.map(is_ping_connected, seed)
        else:
            is_ping_connected(ip)

def save_to_file(result,file_path):
    with open(file_path, 'a+') as f:
        f.write(" | ".join(str(line) for line in result))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',type=int, default=4, help='number of concurrent')
    parser.add_argument('-f',type=str,choices=['ping', 'tcp'], default='tcp', help='protocol, ping or tcp')
    parser.add_argument('-ip', type=str, required=True, help='ip range, e.g. 192.168.1.1-192.168.1.128')
    parser.add_argument('-w', help='write to file')

    args = parser.parse_args()
    task_generation(args.f,args.ip,args.n)


if __name__ == '__main__':
    main()

