import time
import zmq

base_url = "192.168.100.22"
port = "2020"
url = "tcp://" + base_url + ":" + port

def main():
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind(url)

    while True:
        publisher.send_multipart([b"umidade", b'{ "precisaRegar":true,"umidade":20}'])
        time.sleep(1)

    publisher.close()
    context.term()


if __name__ == "__main__":
    main()
