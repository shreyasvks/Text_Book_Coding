class Sets:
    def __init__(self):
        print("Creation of Object type Set\n")
        self.set_obj=set()

    def description(self):
        print("Sets : Collection of well defined object is called set")
        print("     eg: Set of Natural numbers is a set\n         Set of all good persons in a group is not a set\n")
        print("     \n")
        print("     Representation of set : \n          Set builder form or Rule form : Description of elements is given eg : {x:x=n where n>1 and n<5}\n          Roster form : Here all the elements in the set r repsented directily in set eg : {2,3,4,5}")
        print("\n\n")
        print("     Type of sets : \n          1. Empty set \n          2. Singleton set\n          3. Finite and infinite set \n          4. Subsets\n          5. Proper subset : If A is subset of B and A not equal to B \n          6. Power Set : Set of all subsets of a set\n          7. Universal set")
        print("\n\n")
        print("     Venn Diagrams Operations : \n          1. Union\n          2. Intersection\n          3. Difference\n          4. Compliment of set : Difference of set with universal set \n          5. Demorgans law : (A ^ B)' = A' v B'     and (A v B)'= A' ^ B'")

    def set_union(self,new_set):
        print("Union of Current set with New_set is : ",self.set_obj.union(new_set))
        return self.set_obj.union(new_set)
    def set_intersection(self,new_set):
        print("Intersection of Current set with New_set is : ", self.set_obj.intersection(new_set))
        return self.set_obj.intersection(new_set)
    def set_difference(self,new_set):
        print("Difference of Current set with New_set ( i.e Current_set - new_set is : ", self.set_obj.difference(new_set))
        return self.set_obj.difference(new_set)
    def set_compliment(self,union_set):
        print("Compliment of Current set with New_set ( i.e Union_set - Current_set is : ",union_set.difference(self.set_obj))
        return union_set.difference(self.set_obj)
    def add_element_to_set(self,new_element):
        self.set_obj.add(new_element)

    def clear_current_set(self):
        self.set_obj.clear()
    def delete_element_in_set(self,element_value):
        if(element_value in self.set_obj):
            self.set_obj.discard()
    def remove_random_element(self):
        self.set_obj.pop()

    def get_copy_of_set(self):
        #Return Shallow copy of set
        return self.set_obj.copy()

    def is_disjoint(self,new_set):
        return self.set_obj.isdisjoint(new_set)
    def is_subset(self,new_set):
        return self.set_obj.issubset(new_set)
    def is_superset(self,new_set):
        return self.set_obj.issuperset(new_set)
    def is_disjoint(self,new_set):
        return self.set_obj.isdisjoint(new_set)
    def symmetric_difference(self,new_set):
        return self.set_obj.symmetric_difference(new_set)



obj=Sets()
obj.description()
