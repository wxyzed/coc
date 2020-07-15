print("""
.--.              .       .   .---.
|   : o        o _|_      |   |                           o
|   | .  .-..  .  |  .-.  |   |--- .-. .--..-. .--. .--.  .  .-..--.
|   ; | (   |  |  | (   ) |   |   (   )|  (.-' |  | `--.  | (   `--.
'--'-' `-`-`|-' `-`-'`-'`-`-  '    `-' '   `--''  `-`--'-' `-`-'`--'
         ._.'
""")

print("Choose an option: ")
print("1 - Chain of Custody: ")
print("2 - Check Report Integrity: ")

choice = int(input("Choose: "))

if choice == 1:
    import coc
    coc.create_ev_file()
elif choice == 2:
    import integrity
    check_integrity()
else:
    print("That was not an option")
