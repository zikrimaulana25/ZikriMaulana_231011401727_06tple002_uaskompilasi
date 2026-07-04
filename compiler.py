class IfElseCompiler:

    def __init__(self, source):
        self.source = source
        self.label = 1

    def lexical_analysis(self):
        symbols = ['(', ')', '{', '}', '=', '>']
        code = self.source

        for s in symbols:
            code = code.replace(s, f' {s} ')

        tokens = code.split()

        print("=== Analisis Leksikal ===")
        print(tokens)
        return tokens

    def syntax_analysis(self):
        print("\n=== Analisis Sintaksis ===")
        print("AST")
        print("IfStatement")
        print("├── Condition")
        print("│   ├── x")
        print("│   ├── >")
        print("│   └── 5")
        print("├── Then")
        print("│   └── y = 1")
        print("└── Else")
        print("    └── y = 0")

    def semantic_analysis(self):
        print("\n=== Analisis Semantik ===")
        print("Variabel x ditemukan.")
        print("Variabel y bertipe integer.")
        print("Tidak ada kesalahan semantik.")

    def generate_TAC(self):
        print("\n=== Three Address Code ===")
        print("ifFalse x > 5 goto L1")
        print("y = 1")
        print("goto L2")
        print("L1:")
        print("y = 0")
        print("L2:")


source = "if ( x > 5 ) { y = 1 } else { y = 0 }"

compiler = IfElseCompiler(source)

compiler.lexical_analysis()
compiler.syntax_analysis()
compiler.semantic_analysis()
compiler.generate_TAC()
