class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LL:
    def __init__(self):
        self.head = None


    def ll_get(self, value):
        current =self.head 
        #check for head
        #if val is head, ret
        #check next node if not head
        #if not found none

        while current is not None:
            if current.value ==value:
                return current
            current.next
            return None

    def ll_delete(self, value):
        current = self.head
#search for value
#if value on next is value delete
#reset next node
        while current.next is not None:
            if current.next.value == value:
                delete = current.next
                current.next.next
                return delete
                current=current.next


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


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = [None] * capacity
        #initialize spaces
        self.storage = 0
        


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code 
        return len(self.capacity)
        

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        load_factor = self.storage / self.get_num_slots()
        return load_factor
        


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # Your code here
    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
             
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % len(self.capacity)
        return self.djb2(key) % len(self.capacity)
        

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #find index
        #insert val at index

        #slot = self.hash_index(key)
        #self.capacity[slot]= HashTableEntry(key, value)
        #need to increment?

        #####LL VERSION ###
        #increment storage by 1
        #get index, insert value again
        #check if space is empty
        #if empty, insert/
        ##CHECK LOAD
        ##*When load factor increases above 0.7, automatically rehash the table to double its previous size* ##
        #if not empty:
        #check for val in list
        #use ll to insert 
        #insert at next node

        self.storage += 1
        
        slot = self.hash_index(key)
        adding = HashTableEntry(key, value)

        if self.capacity[slot] is None:
            self.capacity[slot] = adding
            if self.get_load_factor() > .7:
                print(self.get_load_factor())
                self.resize(len(self.capacity) * 2)
        else:
            current = self.capacity[slot]
            if current:
                if current.key == key:
                    self.capacity[slot] = adding
                    if self.get_load_factor() > .7:
                        print(self.get_load_factor())
                        self.resize(len(self.capacity) * 2)
                else:
                    while current is not None:
                        if current.key == key:
                            self.capacity[slot] = adding
                            if self.get_load_factor() > .7:
                                self.resize(len(self.capacity) * 2)
                                current = current.next
                    return None
            
            # head
            adding.next = self.capacity[slot]
            self.capacity[slot] = adding
            if self.get_load_factor() > .7:
                print(self.get_load_factor())
                self.resize(len(self.capacity) * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        #self.put(key, None)
        #need to decrement?

    ####LL VERSION#####
    #check if empty
    #if head?
    #use del from ll
    #delete slot
    #reset next
    #decrement in storage
        slot = self.hash_index(key)
        current = self.capacity[slot]

        if current:
            if current.key == key:
                delete = current
                self.capacity[slot] = current.next
                self.storage-= 1
                return delete
            else:
                while current.next is not None:
                    if current.next.key == key:
                        delete = current.next
                        current.next = current.next.next
                        self.storage -= 1
                        return delete
                    current = current.next
                return None
        return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        #slot = self.hash_index(key)
        #hash_entry = self.capacity[slot]
        #if hash_entry is not None:
            #return hash_entry.value

        #return None

####LL VERSION ####
        slot = self.hash_index(key)
        hash_entry = self.capacity[slot]

        if hash_entry:
            if hash_entry.key is key:
                return self.capacity[slot].value
            else:
                while hash_entry is not None:
                    if hash_entry.key is key:
                        return hash_entry.value
                    hash_entry= hash_entry.next
                return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_capacity = self.capacity
        self.capacity = [None] * new_capacity

        for i in old_capacity:
            current = i
            while current is not None:
                self.put(current.key, current.value)
                current =current.next
        



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
