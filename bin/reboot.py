import recovery
recovery.acquire_device().ctrl_transfer(0x40, 0, 0, 0, "reboot" + '\x00', 30000)
