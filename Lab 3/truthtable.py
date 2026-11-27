from itertools import product
def implies(a, b):
    return (not a) or b
def knowledge_base(P, Q, R):
    rule1 = implies(P, Q)
    rule2 = implies(Q, R)
    fact1 = P
    return rule1 and rule2 and fact1
def query(P, Q, R):
    return R
symbols = ['P', 'Q', 'R']
entailment = True
models = 0
print("TRUTH TABLE")
print("P\tQ\tR\tKB\tQuery")
for values in product([True, False], repeat=3):
    P, Q, R = values
    kb = knowledge_base(P, Q, R)
    q = query(P, Q, R)
    print(P, Q, R, kb, q, sep="\t")
    if kb:
        models += 1
        if not q:
            entailment = False
print("\nRESULT:")
if entailment and models > 0:
    print("KB entails the Query (KB |= Query)")
else:
    print("KB does NOT entail the Query")
