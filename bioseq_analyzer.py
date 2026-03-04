# ==============================
# 🧬 BioSeq Analyzer
# ==============================

def validate_dna(seq):
    seq = seq.upper()
    return set(seq).issubset({"A", "T", "G", "C"})


def nucleotide_count(seq):
    return {
        "A": seq.count("A"),
        "T": seq.count("T"),
        "G": seq.count("G"),
        "C": seq.count("C")
    }


def gc_content(seq):
    return round(((seq.count("G") + seq.count("C")) / len(seq)) * 100, 2)


def complement(seq):
    mapping = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join(mapping[n] for n in seq)


def reverse_complement(seq):
    return complement(seq)[::-1]


def transcription(seq):
    return seq.replace("T", "U")


codon_table = {
    "ATG": "M",
    "TTT": "F", "TTC": "F",
    "TAA": "_", "TAG": "_", "TGA": "_"
}


def translation(seq):
    protein = ""
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        protein += codon_table.get(codon, "X")
    return protein


def mutation_detection(seq1, seq2):
    mutations = []
    for i in range(min(len(seq1), len(seq2))):
        if seq1[i] != seq2[i]:
            mutations.append((i + 1, seq1[i], seq2[i]))
    return mutations


def main():
    print("🧬 Welcome to BioSeq Analyzer 🧬\n")

    seq = input("Enter DNA sequence: ").upper()

    if not validate_dna(seq):
        print("Invalid DNA sequence.")
        return

    print("\nValid DNA Sequence\n")
    print("Length:", len(seq))
    print("Nucleotide Count:", nucleotide_count(seq))
    print("GC Content:", gc_content(seq), "%")
    print("Complement:", complement(seq))
    print("Reverse Complement:", reverse_complement(seq))
    print("RNA:", transcription(seq))
    print("Protein:", translation(seq))

    choice = input("\nCompare with another sequence? (yes/no): ")

    if choice.lower() == "yes":
        seq2 = input("Enter second DNA sequence: ").upper()

        if validate_dna(seq2):
            mutations = mutation_detection(seq, seq2)

            if mutations:
                print("\nMutations Found:")
                for m in mutations:
                    print(f"Position {m[0]}: {m[1]} -> {m[2]}")
            else:
                print("No mutations found.")
        else:
            print("Second sequence invalid.")

    save = input("\nSave report? (yes/no): ")

    if save.lower() == "yes":
        with open("report.txt", "w") as f:
            f.write("BioSeq Analyzer Report\n")
            f.write("=====================\n")
            f.write(f"Sequence: {seq}\n")
            f.write(f"Length: {len(seq)}\n")
            f.write(f"GC Content: {gc_content(seq)}%\n")
        print("Report saved as report.txt")


if __name__ == "__main__":
    main()
