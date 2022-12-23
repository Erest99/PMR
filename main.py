# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def run(fstring):
    """
    pomocná funkce pro volání HTK programů
    """
    cmd = subprocess.run(fstring, capture_output=True)
    return cmd.stdout.decode("utf-8")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    import subprocess
    fpath = 'results.txt'

    with open(fpath, mode="w", encoding="utf-8") as file:

        for p in range(20,35,3):
            for s in range (10,16,5):
                print(str(p) + " ; "+str(s))
                debug=run("HVite -H 16hmm6/hmmdefs -S test.scp -i recout.mlf -w wordnet -p "+str(p)+" -s "+str(s)+" dict models0")
                print(debug)
                record = run("HResults -e ??? SENT-START -e ??? SENT-END -t -I testref.mlf models0 recout.mlf")
                idx = record.find("WORD: %Corr")
                record = record[idx:idx+66]
                file.write("p: "+ str(p)+" s: "+ str(s)+ record +"\n\n")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
