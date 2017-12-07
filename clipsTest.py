import clips
import subprocess
import sys
from capturer import CaptureOutput
from cStringIO import StringIO
clips.Reset()

"""
user = True

def py_getvar(k):
    return (clips.Symbol('TRUE') if globals().get(k) else clips.Symbol('FALSE'))

clips.RegisterPythonFunction(py_getvar)

# if globals().get('user') is not None: assert something
clips.BuildRule("user-rule", "(test (eq (python-call py_getvar user) TRUE))", '(assert (user-present))', "the user rule")
clips.BuildRule("do-stuff-rule", "(we-should-do-stuff)", '(python-call py_dostuff)', "the do stuff rule")
clips.BuildRule("do-stuff-rule2", "(we-should-do-stuff2)", '(python-call py_dostuff2)', "the do stuff rule2")
clips.BuildRule("user-rule2", "(test (eq (python-call py_getvar user2) TRUE))", '(assert (user-present2))', "the user rule2")

def addf(a, b):
    return a + b

clips.RegisterPythonFunction(addf)
"""
#clips.Build("""(defrule duck  (animal-is duck)  =>  (assert (sound-is quack))  (printout t \"it's a duck\" crlf)  (bind ?tot (python-call addf 40 2 ))  (printout t ?tot crlf))""")

#clips.Assert("(animal-is duck)")

#clips.Run()
#clips.PrintFacts()
#t = clips.StdoutStream.Read()
#print t
#ri=clips.BuildRule("user-rule", "(test (eq (python-call py_getvar user) TRUE))", '(assert (user-present))', "the user rule")

r0=clips.Build("""
(defrule Enginefailure1 "Engine fails to start, Spark is good"
  (Engine fails to start)(Spark is good)
  =>
  (assert (Obstructed fuel line))
  (assert (Obstructed fuel filter))
  (assert (Leaking head gasket))
  (assert (Low compression)))
""")

r1=clips.Build("""
(defrule Enginefailure2 "Engine fails to start, Spark is not good"
  (Engine fails to start)(Spark is not good)
  =>
  (assert (Loose electrical connections))
  (assert (Dirty electrical connections))
  (assert (Loose or broken ignition coil ground wire))
  (assert (Broken  or  shorted   high  tension  lead  to  the spark plug))
  (assert (Discharged battery))
  (assert (Disconnected or damaged battery connection))
  (assert (Neutral,starter  lockout  or  side  stand  switch trouble)))
""")

#clips.Assert("(Engine fails to start)")
#clips.Assert("(Spark is good)")

r2=clips.Build("""
(defrule EngineStart
  (Engine is difficult to start)
  =>
  (assert (Fouled spark plugs))
  (assert (Improperly adjusted choke))
  (assert (Intake manifold air leak))
  (assert (Contaminated fuel system))
  (assert (Improperly adjusted carburetor))
  (assert (Weak ignition  unit))
  (assert (Weak ignition  coils))
  (assert (Poor compression))
  (assert (Engine and transmission oil too beavy)))
""")

r3=clips.Build("""
(defrule EngineKrank
  (Engine Will Not Crank)
  =>
  (assert (Blown fuse))
  (assert (Discharged battery))
  (assert (Defective starter motor))
  (assert (Seized piston-s))
  (assert (Seized crankshaft bearings))
  (assert (Broken connecting rod)))
""")

r4=clips.Build("""
(defrule EngineIdle
  (Engine Will Not Idle)
  =>
  (assert (Carburetor incorrectly adjusted))
  (assert (Fouled or improperly gapped spark pIug-s))
  (assert (Leaking bead gasket))
  (assert (Obstructed fuel line or fuel shutoff valve))
  (assert (Obstructed fuel filter))
  (assert (Ignition  timing  incorrect  due to defective  ignition component))
  (assert (Valve clearance incorrect)))
""")

r5=clips.Build("""
(defrule EngineMisses
  (Engine Misses at High Speed)
  =>
  (assert (Fouled or improperly gapped spark plugs))
  (assert (Improper  carburetor main jet selection))
  (assert (Ignition  timing  incorrect  due  to defective  ignition  component-s))
  (assert (Weak ignition  coil-s))
  (assert (Obstructed fuel line or fuel shutoff valve))
  (assert (Obstructed fuel filler))
  (assert (Clogged carburetor jets)))
""")

r6=clips.Build("""
(defrule EngineOverheating
  (Engine Overheating)
  =>
  (assert (Incorrect   carburetor   adjustment or jet  selection))
  (assert (Ignition  timing  incorrect  due to improper  adjustment  or defective  ignition  components))
  (assert (Improper spark plug beat range))
  (assert (Damaged or blocked cooling fins))
  (assert (Oil level low))
  (assert (Valves leaking))
  (assert (Oil not circulating properly))
  (assert (Heavy engine carbon deposits)))
""")

r7=clips.Build("""
(defrule EngineOverheatingCooling
  (Engine Overheating Water-cooling problems)
  =>
  (assert (Clogged radiator))
  (assert (Damaged thermostat))
  (assert (Worn or damaged radiator cap))
  (assert (Water pump worn or damaged))
  (assert (Fan relay damaged))
  (assert (Thermostatic fan switch damaged))
  (assert (Damaged fan blade-s)))
""")

r8=clips.Build("""
(defrule EngineExhaustSmoke
  (Excessive  Exhaust   Smoke  and  Engine  Runs Roughly)
  =>
  (assert (Clogged air filter element))
  (assert (Carburetor   adjustment   incorrect-mixture too rich))
  (assert (Choke not operating properly))
  (assert (Water or other contaminants in fuel))
  (assert (Clogged fuel line))
  (assert (Ignition coil defective))
  (assert (Spark plugs fouled))
  (assert (IC igniter or pickup coil defective))
  (assert (Loose or defective ignition circuit wire))
  (assert (Short circuit from damaged wire insulation))
  (assert (Loose battery cable connection))
  (assert (Valve liming incorrect))
  (assert (Intake manifold or air cleaner  air leak)))
""")

r9=clips.Build("""
(defrule EnginePowerLoss
  (Engine Loses Power at Normal Riding Speed)
  =>
  (assert (Carburetor incorrectly adjusted))
  (assert (Engine overheating))
  (assert (Ignition  timing  incorrect  due to defective  ignition component-s))
  (assert (Incorrectly gapped spark plugs))
  (assert (Obstructed muffler))
  (assert (Dragging brakes-s)))
""")

r10=clips.Build("""
(defrule EngineLacksAcceleration
  (Engine Lacks Acceleration)
  =>
  (assert (Carburetor mixture too lean))
  (assert (Clogged fuel line))
  (assert (Ignition  timing  incorrect  due to defecrive  ignition component))
  (assert (Dragging brakes-s)))
""")

r11=clips.Build("""
(defrule EngineOilConsumption
  (Engine Oil  Consumption High)
  =>
  (assert (Worn valve guides))
  (assert (Worn or damaged piston rings)))
""")

r12=clips.Build("""
(defrule EngineSmokes
  (Engine Smokes Excessively)
  =>
  (assert (Worn valve guides))
  (assert (Worn or damaged piston rings)))
""")

r13=clips.Build("""
(defrule EngineOilLeaks
  (Excessive Engine Oil Leaks)
  =>
  (assert (Clogged air cleaner breather hose))
  (assert (Loose engine parts))
  (assert (Damaged gasket sealing surfaces)))
""")

r14=clips.Build("""
(defrule EngineOilLeaks
  (Excessive Engine Oil Leaks)
  =>
  (assert (Clogged air cleaner breather hose))
  (assert (Loose engine parts))
  (assert (Damaged gasket sealing surfaces)))
""")

r15=clips.Build("""
(defrule ClutchSlipping
  (Clutch slipping)
  =>
  (assert (Weak clutch springs))
  (assert (Worn clutch plates))
  (assert (Damaged pressure plate))
  (assert (Clutch release mechanism damage)))
""")

r16=clips.Build("""
(defrule ClutchDragging
  (Clutch dragging)
  =>
  (assert (Incorrect clutch adjustment))
  (assert (Clutch spring tension uneven))
  (assert (Warped clutch plates))
  (assert (Excessive clutch lever play))
  (assert (Clutch housing damage)))
""")

r17=clips.Build("""
(defrule ClutchNoise
  (excessive clutch noise)
  =>
  (assert (Damaged clutch gear teeth))
  (assert (Worn or warped clutch plates)))
""")

#clips.Assert("(Engine fails to start)")
#clips.Assert("(Spark is good)")
#clips.Run()

#clips.FactList()
#print clips.FactList()
#with CaptureOutput() as capturer:
#	clips.PrintFacts()
#	print  capturer.get_lines()
#print h
#clips.PrintRules()
#clips.Matches()
clips.Save("rulez.clp")

#clips.Ppdefrule()
#subprocess.call(["ls", "-l"])
#print subprocess.check_output(['ls','-l'])

#clips.FindRule("""ClutchNoise""")
#clips.SendCommand("""(rules)""")
#clips.StdinStream.Write("""(rules)""")
#clips.Build("""rules""")
#t = clips.RuleList()
#clips.Run()
#clips.StdoutStream.Read()
#clips.Call("""ppdefrule""","""EngineStart""")
#print t

#clips.SendCommand("(assert (Engine fails to start))")
#clips.SendCommand("(assert (Spark is good))")
#clips.SendCommand("(ppdefrule "+"EngineStart"+")")
#clips.Run()
#clips.PrintFacts()
