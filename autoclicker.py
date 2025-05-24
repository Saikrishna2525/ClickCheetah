    import ctypes
    import threading
    import time
    import keyboard

    # Constants for mouse clicks
    MOUSEEVENTF_LEFTDOWN = 0x0002
    MOUSEEVENTF_LEFTUP = 0x0004

    SendInput = ctypes.windll.user32.mouse_event

    clicking = False
    was_pressed = False
    cps = 1000

    def click():
        SendInput(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        SendInput(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def click_loop():
        global clicking
        while True:
            if clicking:
                click()
                delay = 1 / cps if cps > 0 else 0
                time.sleep(delay)
            else:
                time.sleep(0.01)

    def monitor_toggle():
        global clicking, was_pressed
        while True:
            now_pressed = keyboard.is_pressed('f6')
            if now_pressed and not was_pressed:
                clicking = not clicking
                print("[F6] AutoClicker", "ON ✅" if clicking else "OFF ❌")
            was_pressed = now_pressed
            time.sleep(0.01)

    def input_loop():
        global cps
        while True:
            try:
                val = input("Enter CPS (clicks per second, 1–1000): ")
                cps = max(1, min(1000, int(val)))
                print(f"CPS set to {cps}")
            except ValueError:
                print("Invalid number. Try again.")

    # Start threads
    threading.Thread(target=click_loop, daemon=True).start()
    threading.Thread(target=monitor_toggle, daemon=True).start()

    print("Fastest AutoClicker ⚡ [Terminal Version]")
    print("Press F6 to toggle clicking ON/OFF.")
    print("Enter a new CPS value any time.\n")

    input_loop()
