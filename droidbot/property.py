def compare_properties(self, state1, state2):
    
        dict1 = state1.to_dict()
        dict2 = state2.to_dict()

        return dict1 == dict2