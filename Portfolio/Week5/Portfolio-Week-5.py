import sys
import shutil

#1.Using command-line arguments involves the sys module. Review the docs for this module and using the information in there write a short program that when run from the command-line reports what operating system platform is being used
print("The OS platform being used is:", sys.platform)
print()

# 2. Write a program that, when run from the command line, reports how many arguments were provided.
print("The number of arguments are:", len(sys.argv))
print()

# 3. Write a program that takes a bunch of command-line arguments and then prints out the shortest.
arg = min(sys.argv[1:], key=len, default=None)
print("The shortest argument is", arg)
print()

# 4. Last week you wrote a program that processed a collection of temperature readings entered by the user
temperatures = [float(arg) for arg in sys.argv[1:]]
if not temperatures:
    print("No temperature provided")
    sys.exit(1)

max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = sum(temperatures) / len(temperatures)
print(f'Maximum temperature: {max_temp:.2f}')
print(f'Minimum temperature: {min_temp:.2f}')
print(f'Mean temperature: {mean_temp:.2f}')
print()

# 5. Write a program that takes the name of a file as a command-line argument and creates a backup copy of that file.
filename = sys.argv[1]
shutil.copy(filename, filename + '.bak')
print(f'Backup copy of {filename} created as {filename}.bak')
print()
