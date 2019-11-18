Written by Chris Calvo and Brandon Norman.
It was fun trying to debug this whole thing /s
All "TO:DOs" were coded in and tested
Eval and Apply methods were heavily based on the hints that prof GB gave out in class.
The BuiltIn class took a while to code in, but eventually the structure was nailed down on paper
 and translated to code (separating the apply method by # of arguments and calling them)
Environment was built based on the hints given in class with assign and define.
Closure.apply took a helper method that parsed its parameters and arguments for pairs and nulls
 and returns a closure with the rest(body) and the function environment.
There are test prints spread throughout the special and tree folders (used to see where it died)
There were a few errors in the binaries that prevented us from testing intially so the config.json might mess things up but it worked in
 the classes server prior to submission so we dont think that will affect anything.
 We had to recode the entire thing in the classes server and for some reason it works now? we wont ask why or how.







