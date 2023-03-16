

class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, prefix_dict:dict):
        """
        Insert price and prefix to the node
        
        """
        #loop through the dict and value in the prefix and price
        for prefix, price in prefix_dict.items():
            node = self.root
            #for each digit in prefix
            for digit in prefix: 
                # print("digit",digit)
                #if the digit doesn't exist continue or skip
                if digit not in node:
                    # print("yes")
                    node[digit] = {}
                    #{"1":{}} 
                    # print("node digit is", node[digit])
                node = node[digit]
            node['price'] = price

    def lookup(self, number):
        """
        lookup prefix and price in the node
        
        """
        #initialize thie current node
        node = self.root
        price = None
        #loop through the digit 
        for digit in number:
            print("digit",digit)
            #if the digit doesnt exist break
            if digit not in node:
                break
            # else move to the next node and check the price label and update the price variable
            node = node[digit]
            print("next node",node)
            
            if 'price' in node:
                price = node['price']
        print("price",price)
        return price

def cheapest_operator(number, operators):
    """
    run look up function on each operator and return the minimum price in the tree
    """
    cheapest_price = float('inf')
    cheapest_operator = None
    
    for name, operator in operators.items():
        price = operator.lookup(number)
        if price is not None and price < cheapest_price:
            cheapest_price = price
            cheapest_operator = name
    print([cheapest_operator, cheapest_price])
    return [cheapest_operator, cheapest_price]
