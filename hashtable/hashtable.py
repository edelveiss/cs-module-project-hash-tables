class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

#-----------------class HashLinkedList-------------------
class HashLinkedList:
    def __init__(self): 
        self.head = None
    
    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr != None:
            currStr += f'{str(curr.value)} ->'
            curr = curr.next
        return currStr

#-----------------find-------------------
# return node w/ value
 # runtime: O(n) where n = number nodes
    def find(self, key):
        cur = self.head

        while cur is not None:
            if cur.key == key:
                return cur

            cur = cur.next

        return None

#-----------------insert_at_head-------------------
# insert node at head of list
    # runtime: O(1)
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

#---------insert_or_overwrite_value------------
# overwrite node or insert node at head
    # runtime: O(n)
    def insert_or_overwrite_value(self,key, value):
        node = self.find(key) # O(n)

        if node is None:
            # Make a new node
            self.insert_at_head(HashTableEntry(key, value))  # O(1)
            return False
        else:
            # Overwrite old value
            node.value = value
            return True

#-----------------delNode-------------------
# deletes node w/ given value then return that node
    # runtime: O(n) where n = number of nodes
    def delNode(self, key):
        cur = self.head

        # Special case of deleting head
        if cur.key == key:
            self.head = cur.next
            cur.next = None
            return cur

        # General case of deleting internal node
        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.key == key:  
                prev.next = cur.next 
                cur.next = None  
                return cur  
            else:
                prev = cur
                cur = cur.next

        return None  

 #-----------------class HashTable-------------------
class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):  
        self.capacity = capacity
        self.hash_table = [None] * capacity
        self.counter = 0

        #Creating linked lists in each slot of a hash table
        for i in range(self.capacity):
            self.hash_table[i] = HashLinkedList()

        
   
#-----------------get_num_slots-------------------
    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
       
        return self.capacity

#-----------------get_load_factor-------------------
    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        if self.capacity == 0:
            return None
        return self.counter/self.get_num_slots()

#-----------------fnv1-------------------
    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        #Constants
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        hash = offset_basis 
        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)
        return hash

#-----------------djb2-------------------
    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for char in key:
            hash = (( hash << 5) + hash) + ord(char)
        return hash & 0xFFFFFFFF

#-----------------hash_index-------------------
    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity
       
#-----------------put-------------------
    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        i = self.hash_index(key)
        overwritten = False
        overwritten = self.hash_table[i].insert_or_overwrite_value(key, value)
        if overwritten is False:
            self.counter +=1
        # check the load_factor, if load_factor > 0.7 -> resize
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)
        

#-----------------delete-------------------
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # i = self.hash_index(key)
        # if self.hash_table[i] is None:
        #     print(f"Key {key} does not exist!")
        # self.hash_table[i] = None
        #--------------------------------
        i = self.hash_index(key)
        deleted = self.hash_table[i].delNode(key).value
        if deleted is not None:
            self.counter -=1

        # check the load_factor, if load_factor < 0.2 -> resize
        if self.get_load_factor() < 0.2:
            if self.capacity/2 < 8:
                self.resize(8)
            else:
                self.resize(self.capacity / 2)
        return deleted

#-----------------get-------------------
    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # i = self.hash_index(key)
        # if self.hash_table[i] is None:
        #     return None
        # return self.hash_table[i]
        #--------------------------------
        i = self.hash_index(key)
        if self.hash_table[i].find(key) is None:
            return None
        else:
            return self.hash_table[i].find(key).value

        
#-----------------resize-------------------
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        current_table = self.hash_table
        self.capacity = new_capacity
        resized_hash_table = [None] * self.capacity

        #Creating linked lists in each slot of a resized_hash_table
        for i in range(self.capacity):
            resized_hash_table[i] = HashLinkedList() 

        self.hash_table = resized_hash_table
       
        for el in current_table:
            head_value = el.head
            while head_value:
                self.put(head_value.key, head_value.value)
                head_value = head_value.next
                

            
   


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
