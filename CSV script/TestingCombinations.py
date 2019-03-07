#
# Generates a CSV containing all of the possible combinations of the specified components, tests, and beams
# Unintelligently assumes every component has every test running with every beam type.
#
# TODO: specify which components are running which tests
#

#placeholder beam compositions, energies, and fluxes
beamParameters = [["proton","energy1","flux1"],["neutron","energy2","flux2"],["electron","energy3","flux3"],["photon","energy4","flux4"]]

#placeholder tests
tests = ["test1","test2","test3"]

#placeholder components
components = ["component1","component2","component3"]

header = "component,software_test,beam_type,beam_energy,beam_flux\n"

file = open('TestCombinations.csv','w')

file.write(header)

for component in components:
    for test in tests:
        for parameters in beamParameters:
            file.write(component)
            file.write(",")
            file.write(test)
            file.write(",")
            file.write(parameters[0])
            file.write(",")
            file.write(parameters[1])
            file.write(",")
            file.write(parameters[2])
            file.write("\n")