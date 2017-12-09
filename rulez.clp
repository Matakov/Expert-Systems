(defrule MAIN::Enginefailure1
   (Engine fails to start)
   (Spark is good)
   =>
   (assert (Obstructed fuel line))
   (assert (Obstructed fuel filter))
   (assert (Leaking head gasket))
   (assert (Low compression)))

(defrule MAIN::Enginefailure2
   (Engine fails to start)
   (Spark is not good)
   =>
   (assert (Loose electrical connections))
   (assert (Dirty electrical connections))
   (assert (Loose or broken ignition coil ground wire))
   (assert (Broken or shorted high tension lead to the spark plug))
   (assert (Discharged battery))
   (assert (Disconnected or damaged battery connection))
   (assert (Neutral,starter lockout or side stand switch trouble)))

(defrule MAIN::EngineStart
   (Engine is difficult to start)
   =>
   (assert (Fouled spark plugs))
   (assert (Improperly adjusted choke))
   (assert (Intake manifold air leak))
   (assert (Contaminated fuel system))
   (assert (Improperly adjusted carburetor))
   (assert (Weak ignition unit))
   (assert (Weak ignition coils))
   (assert (Poor compression))
   (assert (Engine and transmission oil too beavy)))

(defrule MAIN::EngineKrank
   (Engine Will Not Crank)
   =>
   (assert (Blown fuse))
   (assert (Discharged battery))
   (assert (Defective starter motor))
   (assert (Seized piston-s))
   (assert (Seized crankshaft bearings))
   (assert (Broken connecting rod)))

(defrule MAIN::EngineIdle
   (Engine Will Not Idle)
   =>
   (assert (Carburetor incorrectly adjusted))
   (assert (Fouled or improperly gapped spark pIug-s))
   (assert (Leaking bead gasket))
   (assert (Obstructed fuel line or fuel shutoff valve))
   (assert (Obstructed fuel filter))
   (assert (Ignition timing incorrect due to defective ignition component))
   (assert (Valve clearance incorrect)))

(defrule MAIN::EngineMisses
   (Engine Misses at High Speed)
   =>
   (assert (Fouled or improperly gapped spark plugs))
   (assert (Improper carburetor main jet selection))
   (assert (Ignition timing incorrect due to defective ignition component-s))
   (assert (Weak ignition coil-s))
   (assert (Obstructed fuel line or fuel shutoff valve))
   (assert (Obstructed fuel filler))
   (assert (Clogged carburetor jets)))

(defrule MAIN::EngineOverheating
   (Engine Overheating)
   =>
   (assert (Incorrect carburetor adjustment or jet selection))
   (assert (Ignition timing incorrect due to improper adjustment or defective ignition components))
   (assert (Improper spark plug beat range))
   (assert (Damaged or blocked cooling fins))
   (assert (Oil level low))
   (assert (Valves leaking))
   (assert (Oil not circulating properly))
   (assert (Heavy engine carbon deposits)))

(defrule MAIN::EngineOverheatingCooling
   (Engine Overheating Water-cooling problems)
   =>
   (assert (Clogged radiator))
   (assert (Damaged thermostat))
   (assert (Worn or damaged radiator cap))
   (assert (Water pump worn or damaged))
   (assert (Fan relay damaged))
   (assert (Thermostatic fan switch damaged))
   (assert (Damaged fan blade-s)))

(defrule MAIN::EngineExhaustSmoke
   (Excessive Exhaust Smoke and Engine Runs Roughly)
   =>
   (assert (Clogged air filter element))
   (assert (Carburetor adjustment incorrect-mixture too rich))
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
   (assert (Intake manifold or air cleaner air leak)))

(defrule MAIN::EnginePowerLoss
   (Engine Loses Power at Normal Riding Speed)
   =>
   (assert (Carburetor incorrectly adjusted))
   (assert (Engine overheating))
   (assert (Ignition timing incorrect due to defective ignition component-s))
   (assert (Incorrectly gapped spark plugs))
   (assert (Obstructed muffler))
   (assert (Dragging brakes-s)))

(defrule MAIN::EngineLacksAcceleration
   (Engine Lacks Acceleration)
   =>
   (assert (Carburetor mixture too lean))
   (assert (Clogged fuel line))
   (assert (Ignition timing incorrect due to defecrive ignition component))
   (assert (Dragging brakes-s)))

(defrule MAIN::EngineOilConsumption
   (Engine Oil Consumption High)
   =>
   (assert (Worn valve guides))
   (assert (Worn or damaged piston rings)))

(defrule MAIN::EngineSmokes
   (Engine Smokes Excessively)
   =>
   (assert (Worn valve guides))
   (assert (Worn or damaged piston rings)))

(defrule MAIN::EngineOilLeaks
   (Excessive Engine Oil Leaks)
   =>
   (assert (Clogged air cleaner breather hose))
   (assert (Loose engine parts))
   (assert (Damaged gasket sealing surfaces)))

(defrule MAIN::ClutchSlipping
   (Clutch slipping)
   =>
   (assert (Weak clutch springs))
   (assert (Worn clutch plates))
   (assert (Damaged pressure plate))
   (assert (Clutch release mechanism damage)))

(defrule MAIN::ClutchDragging
   (Clutch dragging)
   =>
   (assert (Incorrect clutch adjustment))
   (assert (Clutch spring tension uneven))
   (assert (Warped clutch plates))
   (assert (Excessive clutch lever play))
   (assert (Clutch housing damage)))

(defrule MAIN::ClutchNoise
   (Excessive clutch noise)
   =>
   (assert (Damaged clutch gear teeth))
   (assert (Worn or warped clutch plates)))

