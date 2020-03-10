# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # if there's nothing at the address, 
        #     insert the key and value as the value to the address
        # if there's something at the address
        #     make a new LP with next pointing to what was prev at the address
        address = self._hash_mod(key)
        item = self.storage[address]
        if not item:
            item = LinkedPair(key, value)
            self.storage[address] = item
        else:
            newLP = LinkedPair(key, value)
            newLP.next = item
            self.storage[address] = newLP


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        address = self._hash_mod(key)
        item = self.storage[address]
        if not item:
            print("WARNING")
        else:
            if key == item.key:
                self.storage[address] = item.next
            while item.next is not None:
                item = item.next 
                if key == item.key:
                    self.storage[address] = item.next




    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        address = self._hash_mod(key)
        item = self.storage[address]
        if not item:
            return None
        else:
            # move through LL and check for item - return item
            while item is not None:
                if key == item.key:
                    return item.value
                else:
                    item = item.next
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity * 2
        tempStore = self.storage[:]
        self.storage = [None] * self.capacity
        for i in tempStore:
            if i is None:
                pass
            else: 
                item = i
                while item is not None:
                    self.insert(item.key, item.value)
                    item = item.next

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
