import subprocess
import sys
import os

def run_command(command, wait=True, detach=False):
    if detach:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    else:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if wait:
        output, error = process.communicate()

        if process.returncode == 0:
            print(output.decode("utf-8"))
        else:
            print(error.decode("utf-8"))
            sys.exit(-1)

# LIST ALL DVD TITLES
titlesCmd= "makemkvcon -r info disc:0 | grep MSG:3028 | awk -F ',' 'BEGIN {printf \"%-9s %-50s\n\", \"Title ID\", \"Information\"} {printf \"%-9d %-50s\n\", NR-1, $4 \" \" $5}'"
print("Getting titles from DVD\n")
run_command(titlesCmd)


# USER INPUT TO GET SPECIFIC TITLES
titles = input("Enter titles to rip:\n").lower()
path = input("Enter filepath to save output to:\n")
ripCmd = "makemkvcon -r mkv disc:0 {} {} > /dev/null"
convertCmd = "HandBrakeCLI -Z \"Fast 1080p30\" -i {} -o output/{}"

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
    os.makedirs("output", exist_ok=True)
    for title in titles:
        print(f"Title {title} being ripped\n")
        run_command(ripCmd.format(title, path))
        files = os.listdir()
        files = [file for file in files if file != ".DS_Store"]
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        run_command(convertCmd.format(files[0], files[0]), False, True)
        print(f"Title {title} being compressed\n")

run_command("drutil eject", False)