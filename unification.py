def is_variable(x):                        # variables look like "?x"
    return isinstance(x, str) and x.startswith('?')

def unify(x, y, subs):
    if subs is None:                       # an earlier step already failed
        return None
    elif x == y:                           # identical, so nothing to substitute
        return subs
    elif is_variable(x):                   # x is a variable, so bind it
        return unify_var(x, y, subs)
    elif is_variable(y):                   # y is a variable, so bind it
        return unify_var(y, x, subs)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        if not x:                          # both lists empty, so success
            return subs
        # unify the first elements, then the rest using that result
        return unify(x[1:], y[1:], unify(x[0], y[0], subs))
    else:                                  # different constants or shapes
        return None

def unify_var(var, x, subs):
    if var in subs:                        # var already bound, so unify its value
        return unify(subs[var], x, subs)
    elif isinstance(x, str) and x in subs: # x is a bound variable, so use its value
        return unify(var, subs[x], subs)
    elif occurs_check(var, x, subs):       # would create an infinite term
        return None
    else:
        subs[var] = x                      # record the binding
        return subs

def occurs_check(var, x, subs):            # does var appear inside x?
    if var == x:
        return True
    elif isinstance(x, list):
        return any(occurs_check(var, xi, subs) for xi in x)
    elif isinstance(x, str) and x in subs:
        return occurs_check(var, subs[x], subs)
    return False

expr1 = ["f", "?x", "a"]                   # f(x, a)
expr2 = ["f", "b", "?y"]                   # f(b, y)
result = unify(expr1, expr2, {})           # start with empty substitutions
print("Expression 1:", expr1)
print("Expression 2:", expr2)
print("Unification Result:")
if result is not None:
    for k, v in result.items():
        print(f"  {k} -> {v}")
else:
    print("  Unification failed.")