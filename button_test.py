arduino = serial.Serial('COM6', 9600, timeout=1)

if arduino.in_waiting > 0:
    line = arduino.readline().decode('utf-8').strip()
    if "accelerations are" in line:
        coords = line.split(":")[-1].strip().split()
        x, y, z = map(int, coords)
        mapped_x = (x - 400) / 220 * 980
        mapped_y = (y - 390) / 220 * 640
        player.move((mapped_x, mapped_y))
