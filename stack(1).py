class Node:
    def __init__(self, data):
        self.data = data    
        self.next = None    

class SinglyLinkedList:
    
    def __init__(self):
        self.top = None     
        self.last = None    
        self.size = 0       

    def insert_at_end(self, data):
        """
        Insere um novo nó no final da lista (last).
        Se for o primeiro elemento, ele será tanto o top quanto o last.
        """
        new_node = Node(data)
        new_node.next = None  

        if self.size == 0:
            self.top = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.size += 1


    def delete_from_top(self):
        """
        Remove o nó do início da lista e retorna seu valor.
        Se a lista estiver vazia, levanta um erro.
        """
        if self.top is None:
            raise IndexError("Estrutura Vazia - Impossível remover elemento")
    
        removed_data = self.top.data    
        self.top = self.top.next        
        self.size -= 1

        if self.top is None:
            self.last = None  
    
        return removed_data

    def is_empty(self):
        """
        Verifica se a lista está vazia.
        """
        return self.top is None

    def peek(self):
        """
        Retorna o valor do topo, sem removê-lo.
        """
        if self.top is None:
            raise IndexError("Estrutura Vazia - Impossível espiar")
        return self.top.data

class Queue:
    def __init__(self):
        self.singly_linked_list = SinglyLinkedList()

    def enqueue(self, data):
        self.singly_linked_list.insert_at_end(data)
        print(f"{data} adicionado à fila com sucesso.")

    def dequeue(self):
        """
        Remove o elemento do início da fila e retorna seu valor.
        """
        data = self.singly_linked_list.delete_from_top()
        print(f"{data} removido da fila com sucesso.")
        return data

    def peek(self):
        """
        Espia (peek) o elemento na frente da fila sem removê-lo.
        """
        data = self.singly_linked_list.peek()
        print(f"O elemento na frente da fila é: {data}")
        return data

    def is_empty(self):
        """
        Verifica se a fila está vazia.
        """
        return self.singly_linked_list.is_empty()
    
    def size(self):
        """
        Retorna o tamanho da fila.
        """
        print (f"O tamanho da fila é: {self.singly_linked_list.size}")
        return self.singly_linked_list.size
    
    def __str__(self):
        """
        Representa a fila no formato:

        1 (Frente)
        ↓
        5
        ↓
        3 (Fim)

        Mostra a ligação interna entre os nós da fila.
        """
        if self.singly_linked_list.top is None:
            return "Fila vazia"

        linhas = []
        atual = self.singly_linked_list.top  
        index = 0  

        while atual is not None:
            if index == 0:
                linhas.append(f"{atual.data} (Frente)")
            else:
                linhas.append(f"{atual.data}")

            atual = atual.next
            if atual is not None:
                linhas.append("↓")
            index += 1

        if "↓" in linhas[-1]:
            linhas.pop()

        if index > 1:
            for i in range(len(linhas) - 1, -1, -1):
                if linhas[i] != "↓":
                    linhas[i] += " (Fim)"
                    break

        return "\n".join(linhas)

fila = Queue()

fila.enqueue(1)
fila.enqueue(5)
fila.enqueue(3)

print(fila)    

fila.peek()        

fila.dequeue()     
fila.size()        

print(fila)        
