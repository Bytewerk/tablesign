import machine, neopixel, time

def hsv_to_rgb(h, s, v):
    if s == 0.0: return (int(v), int(v), int(v))
    i = int(h*6.)
    f = (h*6.)-i; p,q,t = v*(1.-s), v*(1.-s*f), v*(1.-s*(1.-f)); i%=6
    v = int(255.0*v)
    t = int(255.0*t)
    p = int(255.0*p)
    q = int(255.0*q)
    if i == 0: return (v, t, p)
    if i == 1: return (q, v, p)
    if i == 2: return (p, v, t)
    if i == 3: return (p, q, v)
    if i == 4: return (t, p, v)
    if i == 5: return (v, p, q)

np = neopixel.NeoPixel(machine.Pin(4), 14)

def cycle(t):
    h = 0
    while True:
        h += 0.001
        if h>1:
            h = 0
        rgb = hsv_to_rgb(h, 1, 1)
        np.fill(rgb)
        np.write()
        time.sleep(t)

cycle(0.5)
