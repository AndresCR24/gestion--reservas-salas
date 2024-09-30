class Node:
  __slots__ = 'value', 'next'

  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    return str(self.value)

class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __iter__(self):
    curr_node = self.head
    while curr_node is not None:
      yield curr_node
      curr_node = curr_node.next

  def __str__(self):
    result = [str(x.value) for x in self]
    return '--'.join(result)

  def append(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = None
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1

  def prepend(self, value):
    new_node = Node(value)
    if self.head == None:
       self.head = new_node
       self.tail = new_node
    else:
       new_node.next = self.head
       self.head = new_node
    self.length += 1

  def get(self, index):
    if index == -1 or index == self.length-1:
       return self.tail
    elif index < -1 or index >= self.length :
       return None

    indextemp = 0
    for cur_nodo in self:
      if indextemp==index:
        return cur_nodo
      indextemp +=1


  def insert(self, value, index):
    if index== 0:
      self.prepend(value)
      return True
    elif index ==-1 or index == self.length-1:
      self.append(value)
      return True
    elif index < -1 or index > self.length-1:
      return False
    else:
      new_node = Node(value)
      prev_node = self.get(index-1)
      new_node.next = prev_node.next
      prev_node.next = new_node
      self.length += 1
      return True
    return False

  def traverse(self):
    for x in self:
      print(x.value)

  def search(self, target):
    if self.head == None:
      return "No hay elementos para realizar la busqueda"
    else:
      for cur_nodo in self:
        if cur_nodo.value == target:
          return True

      return False

  def set(self, target, newtarget):
    if self.head == None:
      return "No hay elementos para realizar la busqueda"
    else:
      for cur_nodo in self:
        if cur_nodo.value == target:
           cur_nodo.value = newtarget
           return True
      return False

  def pop_first(self):
    if self.head == None:
      return "No hay elementos para realizar la busqueda"

    elif self.length == 1:
      popped_node = self.head
      self.head = None
      self.tail = None
      self.length = 0
      return popped_node
    else:
      popped_node = self.head
      self.head = self.head.next
      self.length -= 1
      popped_node.next = None
      return popped_node


  def pop(self):
    if self.head == None:
      return "No hay elementos para realizar la busqueda"

    elif self.length == 1:
      popped_node = self.head
      self.head = None
      self.tail = None
      self.length = 0
      return popped_node
    else:
      popped_node = self.tail
      print("previo cola",self.get(self.length-2))
      self.tail = self.get(self.length-2)
      self.tail.next = None
      self.length -= 1
      return popped_node

  def remove(self, index):
    if index== 0:
      return self.pop_first()
    elif index ==-1 or index == self.length-1:
      return self.pop()
    elif index < -1 or index > self.length-1:
      return False
    else:
      popped_node = self.get(index)
      prev_node = self.get(index-1)
      prev_node.next = popped_node.next
      popped_node.next = None
      self.length -= 1
      return popped_node
    return False

  def delete(self):
      self.head = None
      self.tail = None
      self.length = 0