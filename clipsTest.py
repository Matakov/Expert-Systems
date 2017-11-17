import clips
clips.Reset()

user = True

def py_getvar(k):
    return (clips.Symbol('TRUE') if globals().get(k) else clips.Symbol('FALSE'))

clips.RegisterPythonFunction(py_getvar)

# if globals().get('user') is not None: assert something
clips.BuildRule("user-rule", "(test (eq (python-call py_getvar user) TRUE))", '(assert (user-present))', "the user rule")
clips.BuildRule("do-stuff-rule", "(we-should-do-stuff)", '(python-call py_dostuff)', "the do stuff rule")
clips.BuildRule("do-stuff-rule2", "(we-should-do-stuff2)", '(python-call py_dostuff2)', "the do stuff rule2")
clips.BuildRule("user-rule2", "(test (eq (python-call py_getvar user2) TRUE))", '(assert (user-present2))', "the user rule2")

clips.Run()
clips.PrintFacts()
