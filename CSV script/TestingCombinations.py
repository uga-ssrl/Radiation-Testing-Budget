#
# Generates CSVs containing all of the possible combinations of the specified components, tests, and beams
#

#list of beams, first value after the beam type is beam fluence, rest are [flux,energy]
''' #original placeholder values
beams = [["Electron","1E6",["1E4","10"]],
         ["Proton","1E6",["1E4","1"],["1E3","10"],["1E2","100"],["1E2","50"]],
         ["Neutron","1E6",["1E1","1E-1"],["1E0","1E0"],["1E-2","1E2"],["1E-1","1E1"]],
         ["Photon","1E6",["1E-4","1E2"],["1E-6","1E3"],["1E-2","1E1"],["1E1","1E0"]]]
'''
#all parameters are determined using LEO data and are subject to change
#heavy ion fluence values are placeholders
beams = [["Proton","1E6",["1E4","1"],["1E3","10"],["1E2","100"],["1E2","50"]],
         ["Heavy ion","1E6",["1E-4","1E2"],["1E-6","1E3"],["1E-2","1E1"],["1E1","1E0"]]]


#components with the tests being run on them
components = [["LPDDR4-CPU",["CPU memcheck"]],["LPDDR4-GPU",["CUDA MEMCHECK","Badblocks"]],["GPU",["PTX script","CUDA samples"]],["Flash",["Vector Add/AND"]]]

header = "component,software_test,beam_energy(MeV),beam_flux(cm-2s-1),beam_fluence(cm-2),estimated_time_to_event(s)"

for beam in beams:
    
    filename = beam[0] + ".csv"
    file = open(filename,"w")
    file.write(header)
    file.write("\n")
    
    for component in components:
        for test in component[1]:
            for beamParameters in beam[2:]:
                file.write(component[0])
                file.write(",")
                file.write(test)
                file.write(",")
                file.write(beamParameters[1])
                file.write(",")
                file.write(beamParameters[0])
                file.write(",")
                file.write(beam[1])
                file.write(",")
                time = float(beam[1])/float(beamParameters[0])
                file.write(str(time))
                file.write("\n")

file.close()