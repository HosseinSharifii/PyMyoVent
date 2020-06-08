## PyMyoVent

PyMyoVent simulates a single ventricle pumping blood around a closed circulation.

+ Installation
  + Python
  + Required libraries
    + Numpy
    + SciPy
    + pandas
    + matplotlib
    + json
    + nested_lookup
    + multiprocessing

+ Structure
  + Modules
    + Single_circulation
    + System_control (Baroreceptor)
    + Perturbation
    + MyoSim
    + Growth

+ Instruction file
  + Json file:
    + output_parameters:

    + baroreflex:
      + fixed_heart_rate
      + simple_baroreceptor

    + perturbations:
      + volume
      + valve
      + compliance
      + resistance
      + myosim

    + circulation:

    + half_sarcomere:
      + myofilaments
      + membranes

    + growth:
      + stress_driven
      + ATPase_driven

    + profiling

    + dumping_data:

    + multi_threads:

+ demo files

  + demo_1 (Using a simple action potential model, Compatible with running on Windows os)

  + demo_2 (Using a sophisticated action potential model (Ten Tusscher et al.), Compatible with running on Windows os)

  + demo_3 (Using a simple action potential model, Compatible with running on Linux/mac os)

  + demo_4 (Using a sophisticated action potential model (Ten Tusscher et al.), Compatible with running on Linux/mac os)
