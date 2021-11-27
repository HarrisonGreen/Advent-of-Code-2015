def read_input():
    file = open("Data/day19.txt", "r")
    replacements = []
    
    for line in file:
        line = line.strip("\n").split(" => ")
        replacements.append(tuple(line))
        
    return replacements

def count_molecules(replacements, medicine):
    molecules = set()
    m = len(medicine)
    
    for replacement in replacements:
        r = len(replacement[0])
        
        for i in range(m-r+1):
            if medicine[i:i+r] == replacement[0]:
                molecules.add(medicine[:i] + replacement[1] + medicine[i+r:])
                
    print(f"Part one: {len(molecules)}")

def make_medicine(replacements, medicine):
    steps = 0
    
    while medicine != "e":
        for replacement in replacements:
            steps += medicine.count(replacement[1])
            medicine = medicine.replace(replacement[1], replacement[0])
            
    print(f"Part two: {steps}")
    
if __name__ == "__main__":
    replacements = read_input()
    medicine = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"
    count_molecules(replacements, medicine)
    make_medicine(replacements, medicine)
