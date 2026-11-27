def is_variable(x):
    return isinstance(x, str) and x[0].islower() and x not in constants
constants = ['john', 'mary', 'ram', 'alice']
def occurs_check(var, term, subst):
    term = substitute(term, subst)
    if var == term:
        return True
    if isinstance(term, tuple):
        return any(occurs_check(var, t, subst) for t in term[1:])
    return False
def substitute(term, subst):
    if isinstance(term, str):
        while term in subst:
            term = subst[term]
        return term
    if isinstance(term, tuple):
        return (term[0],) + tuple(substitute(t, subst) for t in term[1:])
    return term
  def unify(x, y, subst):
    if subst is None:
        return None
    x = substitute(x, subst)
    y = substitute(y, subst)
    if x == y:
        return subst
    if is_variable(x):
        if occurs_check(x, y, subst):
            return None
        subst[x] = y
        return subst
    if is_variable(y):
        if occurs_check(y, x, subst):
            return None
        subst[y] = x
        return subst
    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y) or x[0] != y[0]:
            return None
        for a, b in zip(x[1:], y[1:]):
            subst = unify(a, b, subst)
            if subst is None:
                return None
        return subst
    return None
    
x = ("Parent", "x", "john")
y = ("Parent", "mary", "y")
result = unify(x, y, {})
print("First Order Logic Unification")
print("--------------------------------")
print("Expression 1:", x)
print("Expression 2:", y)
if result is not None:
    print("Unification Successful!")
    print("Substitution:", result)
    print("Expression 1 after substitution:",
          substitute(x, result))
    print("Expression 2 after substitution:",
          substitute(y, result))
else:
    print("Unification Failed!")
    print("No possible substitution exists.")
