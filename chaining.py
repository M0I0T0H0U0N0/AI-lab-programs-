class Rule :
    def __init__(self,antecedents,consequent):
        self.antecedents=antecedents
        self.consequent=consequent

class KnowledgeBase :
    def __init__(self) :
        self.facts=set()
        self.rules=[]
    def add_fact(self,fact):
        self.facts.add(fact)
    def add_rules(self,rule):
        self.rules.append(rule)
    def apply_forward_chaining(self):
        new_facts_derived=True
        while new_facts_derived :
            new_facts_derived=False
            for rule in self.rules :
                if all(antecedent in self.facts for antecedent in rule.antecedents )and rule.consequent not in self.facts :
                    self.facts.add(rule.consequent)
                    new_facts_derived=True
if __name__=="__main__":
    kb=KnowledgeBase()
    rule1=Rule(["A","C"],"E")    
    rule2=Rule(["A","E"],"G")
    rule3=Rule(["B"],"E")
    rule4=Rule(["G"],"D")
    kb.add_rules(rule1)
    kb.add_rules(rule2)
    kb.add_rules(rule3)
    kb.add_rules(rule4)
    kb.add_fact("A")
    kb.add_fact("C")
    kb.apply_forward_chaining()
    print("derived facts",kb.facts)
