import time
import zmq


def main():

    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://192.168.100.5:2020")

    while True:
        #Exercicio 1 :
        publisher.send_multipart([b"umidade", b'{ "regarOuNao":"sim"}'])
        time.sleep(1)

    publisher.close()
    context.term()

if __name__ == "__main__":
    main()
