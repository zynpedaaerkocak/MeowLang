import sys

class MeowError:
    
    @staticmethod
    def hairball_error(line, details=""):
        # Handles syntax and dynamic token errors
        print(f"🤮 [HAIRBALL ERROR ON LINE {line}]: Cat choked on syntax {details}")
        sys.exit(1)

    @staticmethod
    def lost_toy_error(line, name):
        # When an undeclared variable is accessed
        print(f"🔍 [LOST TOY ERROR ON LINE {line}]: Kitten lost the variable '{name}' under the sofa/scope")
        sys.exit(1)

    @staticmethod
    def scratch_error(line, details=""):
        # Handles invalid runtime or math logical structures
        print(f"😾 [SCRATCH ERROR ON LINE {line}]: Angry cat scratched the system {details}")
        sys.exit(1)

    @staticmethod
    def empty_bowl_error(line):
        # Prevents divisions or modulos by zero
        print(f"🥣 [EMPTY BOWL ERROR ON LINE {line}]: Empty bowl, You cannot divide treats by zero portions!")
        sys.exit(1)