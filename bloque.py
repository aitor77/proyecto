# coding=utf-8
import time
import hashlib
import json
import requests

PEER_NODES  = []
MINER_NODE_URL = "http://localhost:5000"
MINER_ADDRESS =

class Block:
    def __init__(self, index, timestamp, root_arbol, hash_anterior):
        """
        Args:
            index (int): Numero del bloque.
            timestamp (int): La hora de generación del bloque.
            root_arbol (str): Root del árbol de Merkle.
            hash_anterior(str): Hash del bloque anterior.
        Attrib:
            index (int): Numero del bloque.
            timestamp (int): La hora de generación del bloque.
            root_arbol (str): Root del árbol de Merkle.
            hash_anterior(str): Hash del bloque anterior
            hash(str): Bloque actual hash único.
        """
        self.index = index
        self.timestamp = timestamp
        self.root_arbol = root_arbol
        self.hash_anterior = hash_anterior
        self.hash = self.hash_block()

    def hash_block(self):
        """crear el hash unico en  sha256."""
        sha = hashlib.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.root_arbol) + str(self.hash_anterior)).encode('utf-8'))
        return sha.hexdigest()


def create_genesis_block():
    """Si no hay hash anterior hay que crear el primero con indice 0"""
    return Block(0, time.time(), {
        "proof-of-work": 9,
        "transactions": None},
        "0")


# Node's blockchain copy
BLOCKCHAIN = [create_genesis_block()]

NODE_PENDIENTE_TRANSACTIONS = []

def proof_of_work(ultima_prueba, blockchain):

    incremento = ultima_prueba + 1
    start_time = time.time()
    while not (incremento % 7919 == 0 and incremento % ultima_prueba == 0):
        incremento += 1

        if int((time.time() - start_time) % 60) == 0:

            nuevo_blockchain = compruebo(blockchain)

            if nuevo_blockchain:
                return False, nuevo_blockchain

    return incremento, blockchain

def compruebo(blockchain):

    cadena_aux = buscar_nueva_cadena()

    BLOCKCHAIN = blockchain
    larga = BLOCKCHAIN
    for cadena in cadena_aux:
        if len(larga) < len(cadena):
            larga = cadena

    if larga == BLOCKCHAIN:
        return False
    else:
        BLOCKCHAIN = larga
        return BLOCKCHAIN

def buscar_nueva_cadena():
    cadena_aux = []
    for nodo_url in PEER_NODES:

        block = requests.get(nodo_url + "/blocks").content

        block = json.loads(block)

        valido = validador_blockchain(block)
        if valido:
            cadena_aux.append(block)
    return cadena_aux

def validador_blockchain(block):
    """Validar la cadena enviada. Si los hashes no son correctos, devuelve falso
    block(str): json
    """
    return True

def  mine(a, blockchain, node_pending_transactions):
    BLOCKCHAIN = blockchain
    NODE_PENDIENTE_TRANSACTIONS = node_pending_transactions
    while True:

        # Obtenga la última prueba de trabajo
        last_block =  BLOCKCHAIN [ len ( BLOCKCHAIN ) -  1 ]
        last_proof = last_block.data [ ' proof-of-work ' ]
        # Encontrar la prueba de trabajo para el bloque actual que se está extrayendo
        # Nota: El programa se bloqueará aquí hasta que se encuentre una nueva prueba de trabajo
        proof = proof_of_work (last_proof, BLOCKCHAIN )
        # Si no adivinamos la prueba, comience a extraer de nuevo
        if not proof[0]:
            # Actualizar blockchain y guardarlo en el archivo
            BLOCKCHAIN  = proof[1]
            a.send ( BLOCKCHAIN )
            continue
        else :
            # Una vez que encontramos una prueba válida de trabajo, sabemos que podemos extraer un bloque
            # Primero cargamos todas las transacciones pendientes enviadas al servidor de nodo
            NODE_PENDING_TRANSACTIONS  = requests.get ( MINER_NODE_URL  +  " / txion? Update = "  +  MINER_ADDRESS ) .content
            NODE_PENDING_TRANSACTIONS  = json.loads ( NODE_PENDING_TRANSACTIONS )


            # Ahora podemos reunir los datos necesarios para crear el nuevo bloque
            new_block_data = {
                " prueba de trabajo " : proof[0],
                " transacciones " : list ( NODE_PENDING_TRANSACTIONS )
            }
            new_block_index = last_block.index + 1
            new_block_timestamp = time.time()
            last_block_hash = last_block.hash
            # Lista de transacciones vacía
            NODE_PENDING_TRANSACTIONS = []
            # Ahora crea el nuevo bloque
            mined_block = Block (new_block_index, new_block_timestamp, new_block_data, last_block_hash)
            BLOCKCHAIN .append (mined_block)
            # Deje que el cliente sepa que este nodo extrajo un bloque
            print (json.dumps ({
              " índice " : new_block_index,
              " marca de tiempo " : str (new_block_timestamp),
              " datos " : new_block_data,
              " hash " : last_block_hash
            }) +  " \ N " )
            a.send ( BLOCKCHAIN )
