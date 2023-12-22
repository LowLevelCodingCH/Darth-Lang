sblrunfile = "Output\\Generated\\BYTECODE\\SBLC\\BYTECODE.sblc"
import random, string

def randomword(length:int=5):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def run_sblc_code(bytecode):
    instructionpointer = 0
    for instruction in bytecode:
        if instruction == 'Function::Int::main':
            pass

        elif instruction == 'Print::CharacterArray::ANY':
            exec(f'print("{bytecode[instructionpointer+1]}")')

        elif instruction == 'Return::SystemInt32Bit::ANY':
            randchararrfive = randomword(5)
            exec(f'def {randchararrfive}(): return {bytecode[instructionpointer+1]}\n{randchararrfive}()')

        elif instruction == 'End::FuncMain::Main':
            pass

        elif instruction == 'DeclareVariable::Int::Next':
            exec(f'int; {bytecode[instructionpointer+1]} = {bytecode[instructionpointer+2]}')

        elif instruction == 'PrintVariable::Int::Next':
            exec(f'print({bytecode[instructionpointer+1]})')

        instructionpointer += 1


with open(sblrunfile) as filea:
    k = filea.read()
    exec(f'run_sblc_code({k})')