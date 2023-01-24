import shutil
import subprocess,sched, time,random, os, sys

def job():
    procs = []
    gcount = random.randint(1, 5)
    for i in range(gcount):
        procs.append(subprocess.Popen("desktopgoose.app/Contents/MacOS/Desktop\ Goose", shell=True))
        time.sleep(10)
    time.sleep(120)
    [p.kill() for p in procs]


s = sched.scheduler(time.time, time.sleep)


def daemonize():
    pid = os.fork()
    if pid > 0:
        sys.exit(0)
    print(pid)
    print(pid, "passed")

def buildup():
    if not os.path.exists(os.path.expanduser("~/Library/Containers/net.namedfork.DesktopGoose/Data/Library/Preferences/net.namedfork.DesktopGoose.plist")):
        if (os.path.exists("desktopgoose.app/Contents/Resources/Memes")):
            shutil.rmtree("desktopgoose.app/Contents/Resources/Memes")
        if (os.path.exists("desktopgoose.app/Contents/Resources/Notes")):
            shutil.rmtree("desktopgoose.app/Contents/Resources/Notes")
        shutil.copytree("Memes","desktopgoose.app/Contents/Resources/Memes")
        shutil.copytree("Notes", "desktopgoose.app/Contents/Resources/Notes")
        # running the app for the first time to create parameters of chaos
        try:
            shutil.rmtree(os.path.expanduser("~/Library/Containers/net.namedfork.DesktopGoose"))
        except:
            pass
        p = subprocess.Popen("desktopgoose.app/Contents/MacOS/Desktop\ Goose", shell=True)
        time.sleep(2)
        p.kill()
        shutil.copy("net.namedfork.DesktopGoose.plist", os.path.expanduser("~/Library/Containers/net.namedfork.DesktopGoose/Data/Library/Preferences"))

    while True:
        interval = 1 * random.randint(1, 5) # in seconds
        s.enter(interval, 1, job, ())
        s.run()


def main():
    pid_file = 'pid'
    if os.path.exists(pid_file):
        with open(pid_file, 'r') as f:
            pid = int(f.read())
            try:
                os.kill(pid, 0)
                sys.exit()
            except OSError:
                    pass
    daemonize()
    with open(pid_file, 'w') as f:
        f.write(str(os.getpid()))
    script_path = os.path.abspath(__file__)
    command = f"python3 {script_path}"
    rc_file = os.path.expanduser("~/.zshrc") if os.path.exists(os.path.expanduser("~/.zshrc")) else os.path.expanduser(
        "~/.bashrc")
    if os.path.exists(rc_file):
        found = False
        with open(rc_file, 'r') as rc:
            rc_lines = rc.readlines()
            for ln in rc_lines:
                if command in ln:
                    found = True
                    break

        if not found:
            f = open(rc_file, "a")
            f.write(command)
            f.close()
    buildup()

if __name__ == "__main__":
    main()
