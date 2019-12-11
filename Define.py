
# 一 Define
norw = 13           # Number of reserved words
txmax = 100         # Symbol table length
nmax = 14           # Maximum number of digits
al = 10             # Maximum length id
amax = 2047         # Maximum address length
levmax = 3          # Block maximum depth
cxmax = 2048        # Maximum size of code array

# 一 Definition of some types
class Instruction:
    def __init__(self, f, l , a):
        self.f = f
        self.l = l
        self.a = a
        self.source = ''
        return

error_message = (
    "",
    "Found ':=' when expecting '='.",
    "There must be a number to follow '='.",
    "There must be an '=' to follow the identifier.",
    "There must be an identifier to follow 'const', 'var', or 'procedure'.",
    "Missing ',' or ';'.",
    "Incorrect procedure name.",
    "Statement expected.",
    "Follow the statement is an incorrect symbol.",
    "'.' expected.",
    "';' expected.",
    "Undeclared identifier.",
    "Illegal assignment.",
    "':=' expected.",
    "There must be an identifier to follow the 'call'.",
    "A constant or variable can not be called.",
    "'then' expected.",
    "';' or 'end' expected.",
    "'do' expected.",
    "Incorrect symbol.",
    "Relative operators expected.",
    "Procedure identifier can not be in an expression.",
    "Missing ')'.",
    "The symbol can not be followed by a factor.",
    "The symbol can not be as the beginning of an expression.",
    "",
    "",
    "",
    "",
    "",
    "",
    "The number is too great.",
    "There are too many levels.",
    "There should be a right paren.",
    "There should be a left paren."
)

# Symbol table object
class Table:
    def __init__(self):
        self.name = ''  # name
        self.kind = 0   # kind
        self.value = 0  # value
        self.level = 0  # level
        self.address = 0# adress，var and procedure use
        return

objectType = {'constant': 0, 'variable': 1, 'procedure': 2}
pCode = {'LIT': 0, 'OPR': 1, 'LOD': 2, 'STO': 3, 'CAL': 4, 'INT': 5, 'JMP': 6, 'JPC': 7}
pCodeRev = {0: 'LIT', 1: 'OPR', 2: 'LOD', 3: 'STO', 4: 'CAL', 5: 'INT', 6: 'JMP', 7: 'JPC'}



#一Control parameters
show_control_detail = True   #

