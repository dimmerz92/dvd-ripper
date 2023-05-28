import subprocess
import sys

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if process.returncode == 0:
        print(output.decode("utf-8"))
    else:
        print(error.decode)
        sys.exit(-1)


# LIST ALL DVD TITLES
titlesCmd= "makemkvcon -r info disc:0 | grep MSG:3028 | awk -F ',' '{print $4, $5}'"
print("Getting titles from DVD\n")
run_command(titlesCmd)


# USER INPUT TO GET SPECIFIC TITLES
titles = input("Enter titles to rip:\n").lower()
path = input("Enter filepath to save output to:\n")
ripCmd = "makemkvcon -r mkv disc:0 {} {}"

if titles == "all":
    # rip all
    ripCmd = ripCmd.format("all", path)
elif "," in titles:
    # process list into list of ints
    try:
        titles = [int(title) for title in titles.split(",")]
    except ValueError as e:
        print(e)
        sys.exit(-1)
elif "-" in titles:
    #process range into list of ints
    try:
        interval = titles.split("-")
        titles = [title for title in range(int(interval[0]), int(interval[1]) + 1)]
    except ValueError as e:
        print(e)
        sys.exit(-1)

if titles == "all":
    run_command(ripCmd)
else:
    for title in titles:
        run_command(ripCmd.format(title, path))