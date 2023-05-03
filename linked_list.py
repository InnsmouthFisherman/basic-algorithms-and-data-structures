# связанный список:
# преимущества: быстрая вставка данных и удаление, динамическое изменение
# недостатки: требовательность к памяти, долгий поиск элементов


class Box:
    def __init__(self, element=None):
        self.element = element
        self.nextelement = None


class LinkedList:
    def __init__(self):
        self.head = None

    def contains(self, element):
        lastbox = self.head
        while lastbox:
            if element == lastbox.element:
                return True
            else:
                lastbox = lastbox.nextelement
        return False
        
    def add(self, newelement):
        newbox = Box(newelement)
        if self.head is None:
            self.head = newbox
        else:
            lastbox = self.head
            while lastbox.nextelement:
                lastbox = lastbox.nextelement
            lastbox.nextelement = newbox

    def get(self, elementIndex):
        lastbox = self.head
        boxIndex = 0
        while boxIndex <= elementIndex:
            if boxIndex == elementIndex:
                return lastbox.element
            boxIndex += 1
        lastbox = lastbox.nextelement  
        
    def remove(self, rmelement=None, index=None):
        if rmelement:
            headbox = self.head
            if headbox is not None:
                if headbox.element == rmelement:
                    self.head = headbox.nextelement
                    headbox = None
                    return
            while headbox is not None:
                if headbox.element == rmelement:
                    break
            lastelement = headbox
            headbox = headbox.nextelement
            if headbox == None:
                return
            lastelement.nextelement = headbox.nextelement
            headbox = None
        elif index:
            lastbox = self.head
            boxIndex = 0
            while boxIndex <= elementIndex:
                if boxIndex == elementIndex:
                    lastbox.element = None
                boxIndex += 1
            lastbox = lastbox.nextelement  
