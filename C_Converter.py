cconvfile = "Output\\Generated\\BYTECODE\\SBLC\\BYTECODE.sblc"

def generate_c_code(bytecode):
    c_code = "#include <stdio.h>\n\n"
    instructionpointer = 0
    for instruction in bytecode:
        if instruction == 'Function::Int::main':
            c_code += "int main() {\n"
        elif instruction == 'Print::CharacterArray::ANY':
            c_code += f'    printf("{bytecode[instructionpointer+1]}");\n'
        elif instruction == 'Return::SystemInt32Bit::ANY':
            c_code += f'    return {bytecode[instructionpointer+1]};\n'
        elif instruction == 'End::FuncMain::Main':
            c_code += '} // Generated by SBLC parser and SBL interpreter (sblinterpreter, sblcconverter, sblcompiler, BYTECODE.sblc, CCODE.c)'
        elif instruction == 'DeclareVariable::Int::Next':
            c_code += f'    int {bytecode[instructionpointer+1]} = {bytecode[instructionpointer+2]};\n'
        elif instruction == 'PrintVariable::Int::Next':
            c_code += f'    printf("%d", {bytecode[instructionpointer+1]});\n'
        instructionpointer += 1
    return c_code

# Example bytecode sequence
with open(cconvfile, "r") as file:
    bytecode_sequence = file.read()

# Generate and print C code based on the bytecode sequence
exec(f"c_code_generated = generate_c_code({bytecode_sequence})")

