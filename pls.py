#try:
import sys
argv = sys.argv
import os
from colorama import init, Fore, Back, Style
init()

def read_n_to_last_line(filename, n = 1):
    """Returns the nth before last line of a file (n=1 gives last line)"""
    num_newlines = 0
    with open(filename, 'rb') as f:
        try:
            f.seek(-2, os.SEEK_END)    
            while num_newlines < n:
                f.seek(-2, os.SEEK_CUR)
                if f.read(1) == b'\n':
                    num_newlines += 1
        except OSError:
            f.seek(0)
        last_line = f.readline().decode()
    return last_line

list; memstack = []

fname = argv[1]
retfile = argv[2]

with open(fname, "r") as file:
    
    iteration = 0

    file_read = file.read()

    lines = file_read.split("\n")
    lastline = read_n_to_last_line(fname)
    if(lines[0] == "void main<Main> {" and file_read.endswith("\n}")):
        
        memstack.append("Function::Void::main")
# Array Syntax: <FUNCTION>::<RETURN_TYPE>::<NAME> or <DATA>
# <DATA>: any string or integer etc. mostly coming after a function or keyword as argument or plain data
# <FUNCTION>: Print, Return, Function (for the "main" function)
# <RETURN_TYPE>: Void, CharacterArray, Character, Any, SystemInteger32BitSigned, SystemInteger32BitUnsigned, Array, FloatingPointNumber32Bit, SystemLong64BitSigned, SystemLong64BitUnsigned
# <NAME>: any name, "ANY", or "main"
# [CLASS_TYPE]: type of arrays, like {INFORMATION} for <DATA> and {DECLARE} for <FUNCTION>::<RETURN_TYPE>::<NAME>
        for line in lines:
            
            file_line = lines[iteration]
            def doshit():
                arrlenga = str(memstack).replace("\"", "")
                arrlena = arrlenga.replace("\"", "")

                print(Fore.GREEN + f"""
-------------MEMSK-------------
Memory stack: {memstack}
Memory size: {len(memstack)}
Ram: {len(memstack)}/32678 spaces used
Disk: {len(arrlena)} B used
Disk data: {arrlena}
Return file: {retfile}

 -------------DEBUG-------------
Code file: \n\n{Fore.YELLOW}{file_read} {Fore.GREEN}\n
Code name: {fname}
Code size: {len(file_read)} B
"""
+ Fore.RESET)

            if file_line.startswith("    Std::Print *, "):
                
                memstack.append("Print::CharacterArray::ANY")

                file_line_str_print = file_line[13:]

                memstack.append(file_line_str_print)
                if len(memstack) >= 32768:
                    exit()
            if file_line.startswith("    PrintV *, "):
                
                memstack.append("PrintVariable::Any::ANY")

                file_line_str_printa = file_line[14:]

                memstack.append(file_line_str_printa)
                if len(memstack) >= 32768:
                    exit()
            if file_line.startswith("    Let "):
                
                kccc = file_line.split(" :: ")
                kccc.pop(0)
                a = f"DeclareVariable::Any::{kccc[0]}"
                memstack.append(a)

                file_line_str_prinbt = kccc[1]

                memstack.append(file_line_str_prinbt)
                if len(memstack) >= 32768:
                    exit()
            elif file_line.startswith("void main<Main> {"):
                pass
            elif file_line.startswith("}"):
                pass
            elif file_line.startswith("\n"):
                pass
            elif file_line.startswith("    Return "):
                
                memstack.append("Return::SystemInt32Bit::ANY")

                file_line_int_return = file_line[11:]

                memstack.append(file_line_int_return)
                if len(memstack) > 32768:
                    exit()

            elif file_line.startswith("    import "):
                
                 with open(file_line[11:], "r") as read_file_import:
                    memstack.append(read_file_import.read())
            elif file_line.startswith("    %"):
                pass
            
            else:
                print(Fore.RED + f"\nERROR \n at line (startingpoint: 1): {iteration+1}, not an instruction: '{file_line}', \nInstructionError::None\nunexpected [TYPE]\nProceeding\n#########\n" + Fore.RESET)
            
            iteration += 1
        memstack.append("End::FuncMain::Main")

    if len(memstack) > 32768:
        exit()
with open(retfile, "w") as returnfileobj:
    arrleng = str(memstack).replace("\"", "")
    arrlen = arrleng.replace("\"", "")
    returnfileobj.write(arrlen)


doshit()
#except:
#    print(Fore.RED + f"Some error occured! " + Fore.RESET)