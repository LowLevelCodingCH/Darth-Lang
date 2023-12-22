import Interpreter
import C_Converter

with open(f"Output\\Generated\\C\\CCODE.c", "w") as filea:
    filea.write(str(C_Converter.c_code_generated))
