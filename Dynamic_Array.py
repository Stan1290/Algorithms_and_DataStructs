
# coding: utf-8

# # Dynamic Array
#

# In[ ]:


import ctypes


class DynamicArray(object):


    def __init__(self):
        self.size = 0 # Stores the current size of the array
        self.capacity = 1 # Stores max current capacity of the array
        self.Arr = self.make_array(self.capacity)


    def __len__(self): #Return the current size of the array
        return self.n

    def __getitem__(self, index):
        if not (0 <= index < self.size):
                return IndexError('Requested index is out of bounds.')
        return self.Arr[index]


    def append(self, element):
        if self.size == self.capacity:
            self._resize(2 * self.capacity) # Doubles the current capacity

        self.Arr[self.size] = element # Adds new element to the end of the array
        self.size += 1

    def _resize(self, new_capacity):
        temp_arr = self.make_array(new_capacity)

        for i in range(self.size):
            temp_arr[i] = self.Arr[i]
            self.capacity = new_capacity

    def make_array(self, new_capacity):
        return (new_capacity 8 ctypes.py_objects)()
