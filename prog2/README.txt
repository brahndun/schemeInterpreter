All "TO:DOs" were coded in and tested
Eval and Apply methods were heavily based on the hints that prof GB gave out in class.
The BuiltIn class took a while to code in, but eventually the structure was nailed down on paper
 and translated to code (separating by arguments and calling them)
Environment was built based on the hints given in class with assign and define.
Closure apply took a helper method that parsed its parameters and arguments for empty cons nodes
 and returns a closure with the rest(body) and the function environment.
These methods were tested out individually and worked.
Running Scheme4101.py results in the error below

Exception has occurred: TypeError
'module' object is not callable
  File "C:\Users\Chrow\Documents\GitHub\schemeInterpreter\prog2\Util.py", line 19, in parseList
    return Regular()
  File "C:\Users\Chrow\Documents\GitHub\schemeInterpreter\prog2\Tree\Cons.py", line 27, in parseList
    self.form = Cons.util.parseList(self)
  File "C:\Users\Chrow\Documents\GitHub\schemeInterpreter\prog2\Tree\Cons.py", line 16, in __init__
    self.parseList()
  File "C:\Users\Chrow\Documents\GitHub\schemeInterpreter\prog2\Tree\Environment.py", line 127, in define
    head = Cons(Cons(id, Cons(value, Nil.getInstance())), Nil.getInstance())
  File "C:\Users\Chrow\Documents\GitHub\schemeInterpreter\prog2\Tree\Environment.py", line 57, in populate
    env.define(sym, BuiltIn(sym))
  File "C:\Users\Chrow\Documents\GitHub\schemeInterpreter\prog2\Scheme4101.py", line 62, in <module>
    Environment.populate(env, ini_file)

We spent 2 weeks combing over the code and we are stumped as to what to do to make it run as a whole
We are certain that the individual Special and Tree components work but we still arent certain
 where the error is caused in the code; It could be a structure problem but we would miss it anyways.
