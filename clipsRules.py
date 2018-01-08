import clips
import subprocess
import sys
from capturer import CaptureOutput
from cStringIO import StringIO
clips.Reset()
#sys.stdout = open("logfile", "w")
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

r18=clips.Build("""
(defrule GearNoise
  (excessive gear noise)
  =>
  (assert (Worn bearings))
  (assert (Worn or damaged gears))
  (assert (Excessive gear backlash)))
""")

r19=clips.Build("""
(defrule DifficultShifting
  (Difficult shifting)
  =>
  (assert (Damaged gears))
  (assert (Damaged shift forks))
  (assert (Damaged shift drum))
  (assert (Damaged shift lever assembly))
  (assert (Incorrect clutch disengagement))
  (assert (Incorrect main shaft and countershaft engagement)))
""")

r20=clips.Build("""
(defrule GearsPopOut
  (Gears pop out of mesh)
  =>
  (assert (Worn gear or transmission shaft splines))
  (assert (Shift forks worn or bent))
  (assert (Worn dog holes In gears))
  (assert (Insufficient shift lever sprIng tensIon))
  (assert (Damaged shift lever linkage)))
""")

r21=clips.Build("""
(defrule IncorrectShiftOperation
  (Incorrect shift lever operation)
  =>
  (assert (Bent shift lever))
  (assert (Bent or damaged shift lever shaft))
  (assert (Damaged shift lever linkage or gears)))
""")

r22=clips.Build("""
(defrule StarterNotWork
  (Starter does not work)
  =>
  (assert (Low battery))
  (assert (Worn brushes))
  (assert (Defective relay))
  (assert (Defective awltch))
  (assert (Defective wiring or connection))
  (assert (Intemal short circuit)))
""")

r23=clips.Build("""
(defrule StarterWeak
  (Starter action is weak)
  =>
  (assert (Low battery))
  (assert (Pitted relay contacts Worn))
  (assert (brushes Defective))
  (assert (connection short circuit in commutator)))
""")

r24=clips.Build("""
(defrule StarterRunsContinuously
  (Starter runs continuously)
  =>
  (assert (Stuck relay)))
""")

r25=clips.Build("""
(defrule StarterNoEngine
  (Starter turnes but not engine)
  =>
  (assert (Defective starter clutch)))
""")

r26=clips.Build("""
(defrule ExcessiveVibration
  (Excessive Vibration)
  =>
  (assert (Broken frame))
  (assert (Severely worn primary chain))
  (assert (Worn drive chain))
  (assert (Primary chain  links  tight  due to improper lubrication))
  (assert (Improperly balanced wheels))
  (assert (Defective or damaged wheels))
  (assert (Defective or damaged tires))
  (assert (Internal engine wear or damage)))
""")

r27=clips.Build("""
(defrule IrregularWobblySteering
  (Irregular or Wobbly Steering)
  =>
  (assert (Loose wheel axle nuts))
  (assert (Loose or worn steering head bearings))
  (assert (Excessive wheel hub bearing play))
  (assert (Damaged cast wheel))
  (assert (Unbalanced wheel assembly))
  (assert (Worn hub bearings))
  (assert (Incorrect wheel alignment))
  (assert (Bent or damaged  steering  stem or frame at steering neck))
  (assert (Tire incorrectly seated on rim))
  (assert (Excessive front end loading  from non-standard equipment)))
""")

r27=clips.Build("""
(defrule ExcessiveVibration
  (Excessive Vibration)
  =>
  (assert (Broken frame))
  (assert (Severely worn primary chain))
  (assert (Worn drive chain))
  (assert (Primary chain  links  tight  due to improper lubrication))
  (assert (Improperly balanced wheels))
  (assert (Defective or damaged wheels))
  (assert (Defective or damaged tires))
  (assert (Internal engine wear or damage)))
""")

r28=clips.Build("""
(defrule StiffSteering
  (Stiff Steering)
  =>
  (assert (Low front tire air pressure))
  (assert (Bent  or  damaged  steering  stem  or frame at
steering  neck))
  (assert (Loose or worn steering head bearings))
  (assert (Steering stem nut too tight)))
""")

r29=clips.Build("""
(defrule StifforHeavyForkOperation
  (Stiff or Heavy Fork Operation)
  =>
  (assert (Incorrect fork springs))
  (assert (Incorrect fork oil viscosity))
  (assert (Excessive amount of fork oil))
  (assert (Bent fork rubes)))
""")

r30=clips.Build("""
(defrule PoorShockAbsorber
  (Poor Rear Shock Absorber Operation)
  =>
  (assert (Weak or worn spring))
  (assert (Damper unit leaking))
  (assert (Shock shaft worn or bent))
  (assert (Incorrect rear shock spring))
  (assert (Rear shock adjusted incorrectly))
  (assert (Heavy rear  end  loading   from  non-standard equipment))
  (assert (Incorrect loading)))
""")

r31=clips.Build("""
(defrule StiffSteering
  (Stiff Steering)
  =>
  (assert (Low front tire air pressure))
  (assert (Bent  or  damaged  steering  stem  or frame at
steering  neck))
  (assert (Loose or worn steering head bearings))
  (assert (Steering stem nut too tight)))
""")

r32=clips.Build("""
(defrule DiscBrakeFluidLeakage
  (Disc brake fluid leakage)
  =>
  (assert (Loose or damaged line fittings))
  (assert (Worn caliper piston seels))
  (assert (Scored caliper piston andlor bore))
  (assert (Loose banjo bolts))
  (assert (Damaged all line washers))
  (assert (Leaking master cylinder diaphragm))
  (assert (Leaking master cylinder secondary seal))
  (assert (Cracked master cylinder housing))
  (assert (Too high brake fluid level))
  (assert (Loose master cylinder cover)))
""")

r33=clips.Build("""
(defrule BrakeOverheatlng
  (Brake overheatlng)
  =>
  (assert (Warped brake disc))
  (assert (Incorrect brake fluid))
  (assert (Caliper piston andlor brake pads hanging up))
  (assert (Riding brakes during riding)))
""")

r34=clips.Build("""
(defrule BrakeChatter
  (Brake chatter)
  =>
  (assert (Warped brake disc))
  (assert (Loose brake disc))
  (assert (Incorrect caliper alignment))
  (assert (Loose caliper mounting bolts))
  (assert (Loose front axle nut and/or clamps))
  (assert (Worn wheel bearings))
  (assert (Damaged front hub))
  (assert (Restricted brake hydraulic lineb))
  (assert (Contaminated brake pads)))
""")

r35=clips.Build("""
(defrule BrakeLocking
  (Brake locking)
  =>
  (assert (Incorrect brake fluid))
  (assert (Plugged passages In master cylinder))
  (assert (Incorrect front brake adjustment))
  (assert (Caliper piston andlor brake pads hanging up))
  (assert (Warped brake disc)))
""")

r36=clips.Build("""
(defrule InsufficientBrakes
  (Insufficient brakes)
  =>
  (assert (Air In brake lines))
  (assert (Worn brake pads))
  (assert (Low brake fluid level))
  (assert (Incorrect brake fluid))
  (assert (Worn brake disc))
  (assert (Worn caliper piston seals))
  (assert (Glazed brake pads))
  (assert (Leaking primary cup seal In master cylinder))
  (assert (Contaminated brake pads and/or disc)))
""")

r37=clips.Build("""
(defrule BrakeSqueal
  (Brake squeal)
  =>
  (assert (Contaminated brake pads andlor disc))
  (assert (Dust or dirt collected behind brake padsg))
  (assert (Loose parts)))
""")

r38=clips.Build("""
(defrule BrakesDoNotHold
  (Brakes do not hold)
  =>
  (assert (Worn  brake linings))
  (assert (Glazed brake linings))
  (assert (Worn brake drum))
  (assert (Glazed brake drum))
  (assert (Incorrect brake adjustment))
  (assert (Worn or damaged brake cable))
  (assert (Worn or defective brake return springs)))
""")

r39=clips.Build("""
(defrule BrakesGrab
  (Brakes grab)
  =>
  (assert (Worn or damaged brake return springs))
  (assert (Incorrect brake adjustment))
  (assert (Brake drum out-ct-rcund))
  (assert (Warped brake lining web))
  (assert (Loose or worn wheel bearings)))
""")

r40=clips.Build("""
(defrule BrakesSquealOrScrape
  (Brakes  squeal  or  scrape)
  =>
  (assert (Worn brake linings))
  (assert (Brake drum out-of-round))
  (assert (Contaminated brake linings andlor drum))
  (assert (Broken, loose or damaged brake component))
  (assert (Loose or worn wheel bearing))
  (assert (Loose brake drum-ta-wheel mounting bolta)))
""")

r41=clips.Build("""
(defrule BrakesChatter
  (Brakes chatter)
  =>
  (assert (Brake drum out-of-round))
  (assert (Brake linings worn unevenly))
  (assert (Warped brake lining web))
  (assert (Incorrect brake adjustment))
  (assert (Loose or worn wheel bearing))
  (assert (Worn or damaged brake return springs)))
""")

r42=clips.Build("""
(defrule RichMixture
  (Brakes chatter)
  (Rough Idle)
  (Black exhauat smoke)
  (Hard starting)
  (Gas-fouled spark plugs)
  (Black  deposits in exhaust pipe)
  (Engine  performance worse as it worms up)
  =>
  (assert (Rich mixture)))
""")

r43=clips.Build("""
(defrule LeanMixture
(Backfiring)
(Rough Idle)
(Overheating)
(Hesitation upon acceleration)
(Engine  speed  varies at fixed throttle)
(Loss of power)
(White color on spark plug insulator)
(Poor acceleration)
=> 
(assert (Lean mixture)))
""")

name="ime"
rule="ADD"
things="add possible malfunction\nadd certain malfunction"

#name = input("name? ")
#rule = input("LHS? ")
#things = input("RHS? ")

def build(name,rule,things):
	split_rule = rule.splitlines()
	# data = self.text_area.get(0.0, END)
	split_things = things.splitlines()
	stringRHSL = '(assert ('
	stringRHSR = '))'
	stringLHSL = '('
	stringLHSR = ')'
	RHSString = ''
	LHSString = ''
	for i in range(len(split_rule)):
		    LHSString = LHSString + stringLHSL + split_rule[i].encode("utf-8") + stringLHSR + "\n"
	for j,i in enumerate(range(len(split_things))):
		if(j<len(split_things)-1):
			RHSString = RHSString + stringRHSL + split_things[i].encode("utf-8") + stringRHSR + "\n"
		else:
			RHSString = RHSString + stringRHSL + split_things[i].encode("utf-8") + stringRHSR + ")"
	stringBuild = "(defrule "+name+"\n"+LHSString+"=>\n"+RHSString
	print(stringBuild)
	clips.Build(stringBuild)

build(name,rule,things)
# clips.BuildRule("user-rule", "(test (eq (python-call py_getvar",RHSString, "the user rule")
#print(name)
#print(LHSString)
#print(RHSString)
#clips.BuildRule(name, LHSString, RHSString)

#r44=clips.BuildRule("jebotezivot", "(add sypmtom)(add sypmtom)(add sypmtom)", "(assert (add possible malfunction))(assert (add possible malfunction))(assert (add possible malfunction))")
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

clips.SendCommand("(assert (Engine fails to start))")
clips.SendCommand("(assert (Spark is good))")
#clips.SendCommand("(ppdefrule "+"EngineStart"+")")
#clips.Run()
#clips.PrintFacts()
#sys.stdout = open("/dev/stdout", "w")

clips.PrintRules()
