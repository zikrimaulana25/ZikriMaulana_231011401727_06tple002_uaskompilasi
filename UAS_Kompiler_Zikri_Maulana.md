# Tugas Proyek Akhir
## Representasi Tahapan Kompilasi

### Nama : Zikri Maulana
### NIM : 231011401727

---

# 1. Konstruksi yang Dipilih

Percabangan (If-Else)

Contoh:

if (x > 5) {
    y = 1;
} else {
    y = 0;
}

---

# 2. Pattern (BNF)

<if_stmt> ::= "if" "(" <condition> ")" "{" <statement> "}" "else" "{" <statement> "}"

<condition> ::= <identifier> <operator> <number>

<statement> ::= <identifier> "=" <number>

---

# 3. Analisis Leksikal

Token yang dihasilkan:

IF
(
IDENTIFIER(x)
>
NUMBER(5)
)
{
IDENTIFIER(y)
=
NUMBER(1)
}
ELSE
{
IDENTIFIER(y)
=
NUMBER(0)
}

---

# 4. Analisis Sintaksis

Abstract Syntax Tree (AST)

IfStatement
├── Condition
│   ├── Identifier : x
│   ├── Operator : >
│   └── Number : 5
├── Then
│   └── y = 1
└── Else
    └── y = 0

---

# 5. Analisis Semantik

- Variabel x digunakan sebagai kondisi.
- Variabel y bertipe integer.
- Nilai yang diberikan valid.
- Tidak ditemukan kesalahan semantik.

---

# 6. Three Address Code (TAC)

ifFalse x > 5 goto L1
y = 1
goto L2
L1:
y = 0
L2:

---

# 7. Kesimpulan

Program berhasil mensimulasikan tahapan kompilasi mulai dari analisis leksikal, sintaksis, semantik hingga menghasilkan Three Address Code (TAC). Setiap tahapan berjalan sesuai aturan grammar yang telah dibuat
