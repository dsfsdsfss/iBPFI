import recovery
import os
import checkm8
import readline
import usb
class ibpfi:
	def shell(self):
		while(1):
			cmd = raw_input("iShell: ")
			cm = str(cmd.split(" ")[0])
			if cm != "bgcolor" and cm != "kernelcache" and cm != "setenv" and cm != "saveenv" and cm != "bootx" and cm != "devicetree" and cm != "ramdisk" and cm != "setpicture" and cm != "reset" and cm != "reboot" and cm != "exit":
				print("invalid command")
			else:
				if cm == "exit":
					exit()
				recovery.acquire_device().ctrl_transfer(0x40, 0, 0, 0, str(cmd) + '\x00', 30000)
	def ibshell(self):
		while (1):
			cmd = raw_input("iBPFI: ")
			if cmd == "shell":
				pwn = 0
				cont = 1
				dev = usb.core.find(idVendor=0x5AC, idProduct=0x1281) # fill in your own device, of course
				if dev != None:
					print("found device in recovery mode")
					cont = 1
				if cont != 0:
					while(1):
						cmd = raw_input("iShell: ")
						cm = str(cmd.split(" ")[0])
						if cm != "bgcolor" and cm != "kernelcache" and cm != "setenv" and cm != "saveenv" and cm != "bootx" and cm != "devicetree" and cm != "ramdisk" and cm != "setpicture" and cm != "reset" and cm != "reboot" and cm != "exit" and cmd != "send" and cm != "go":
							print("invalid command")
						else:
							if cm == "exit":
								exit()
							elif cm == "reset" or cm == "reboot":
								if usb.core.find(idVendor=0x5AC, idProduct=0x1281) != None:
									os.system("cd ./bin/; python ./reboot.py 2>/dev/null; cd ../")
									exit()
								exit()
							elif cmd == "send":
								device = recovery.acquire_device()
								recovery.send_data(device, open(raw_input("File to send: "),"r").read())
								recovery.release_device(device)
							else:
								recovery.acquire_device().ctrl_transfer(0x40, 0, 0, 0, str(cmd) + '\x00', 30000)

			if cmd == "checkm8":
				checkm8.exploit()
			if cmd == "exit":
				return
			if cmd == "sig":
				os.system("python ./bin/rmsigchks.py")
			if cmd == "help":
				print("""checkm8 | puts device into pwned dfu mode using checkm8 exploit
sig | patch signiture checks on s5l8960x and t8011 devices
prec | sends ibss and ibec to device in pwned dfu mode
shell | opens recovery shell (like irecovery) for use with device in pwed recovery or regular recovery mode
rainbow | cycles through some colors with bgcolor. must have used prec on device before use
rainbowloop | does the same thing as rainbow but in a infinite loop
checkra1n | jailbreaks device with checkra1n jailbreak""")
			if cmd == "rainbow":
				r = 0 
				g = 0
				b = 0
				while r != 255:
					recovery.acquire_device().ctrl_transfer(0x40, 0, 0, 0, "bgcolor " +str(r) + " " + str(g) + " " + str(b) + '\x00', 30000)
					r = r +1
				while g != 255:
					recovery.acquire_device().ctrl_transfer(0x40, 0, 0, 0, "bgcolor " +str(r) + " " + str(g) + " " + str(b) + '\x00', 30000)
					g = g +1
				while b != 255:
					recovery.acquire_device().ctrl_transfer(0x40, 0, 0, 0, "bgcolor " +str(r) + " " + str(g) + " " + str(b) + '\x00', 30000)
					b = b +1
				r = 0
				g = 0
				b = 0
				while r != 255:
					recovery.acquire_device().ctrl_transfer(0x40, 0, 0, 0, "bgcolor " +str(r) + " " + str(g) + " " + str(b) + '\x00', 30000)
					r = r +1
				r = 0
				while g != 255:
					recovery.acquire_device().ctrl_transfer(0x40, 0, 0, 0, "bgcolor " +str(r) + " " + str(g) + " " + str(b) + '\x00', 30000)
					g = g +1
				g = 0
				while b != 255:
					recovery.acquire_device().ctrl_transfer(0x40, 0, 0, 0, "bgcolor " +str(r) + " " + str(g) + " " + str(b) + '\x00', 30000)
					b = b +1
				b = 0
			if cmd == "rainbowloop":
				while 1:
					r = 0 
					g = 0
					b = 0
					while r != 255:
						recovery.acquire_device().ctrl_transfer(0x40, 0, 0, 0, "bgcolor " +str(r) + " " + str(g) + " " + str(b) + '\x00', 30000)
						r = r +1
					while g != 255:
						recovery.acquire_device().ctrl_transfer(0x40, 0, 0, 0, "bgcolor " +str(r) + " " + str(g) + " " + str(b) + '\x00', 30000)
						g = g +1
					while b != 255:
						recovery.acquire_device().ctrl_transfer(0x40, 0, 0, 0, "bgcolor " +str(r) + " " + str(g) + " " + str(b) + '\x00', 30000)
						b = b +1
					r = 0
					g = 0
					b = 0
					while r != 255:
						recovery.acquire_device().ctrl_transfer(0x40, 0, 0, 0, "bgcolor " +str(r) + " " + str(g) + " " + str(b) + '\x00', 30000)
						r = r +1
					r = 0
					while g != 255:
						recovery.acquire_device().ctrl_transfer(0x40, 0, 0, 0, "bgcolor " +str(r) + " " + str(g) + " " + str(b) + '\x00', 30000)
						g = g +1
					g = 0
					while b != 255:
						recovery.acquire_device().ctrl_transfer(0x40, 0, 0, 0, "bgcolor " +str(r) + " " + str(g) + " " + str(b) + '\x00', 30000)
						b = b +1
					b = 0
			if cmd == "dfusend":
				os.system("./bin/bin/irecovery -f " + str(raw_input("File Path: ")))
			if cmd == "prec":
				os.system("./bin/bin/irecovery -f " + str(raw_input("iBSS Path: ")))
				os.system("./bin/bin/irecovery -f " + str(raw_input("iBEC Path: ")))
			if cmd == "checkra1n":
				os.system("cd ./bin/check; ./checkra1n_gui -")

