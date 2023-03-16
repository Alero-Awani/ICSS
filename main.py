from app import Trie, cheapest_operator


opa = {"234":0.9, "236":5.1, "44":0.17, "446":0.0, "468":0.15, "4631":0.15, "4673":0.9, "46732":1.1}
opb = {"1":0.92, "44":0.5, "46":0.2, "467":1.0, "48":1.2}

operator_a = Trie()
operator_a.insert(opa)

operator_b = Trie()
operator_b.insert(opb)

operators = {
    'Operator A': operator_a,
    'Operator B': operator_b,
}




if __name__ == "__main__":
    cheapest_operator(number="446038954127", operators=operators)