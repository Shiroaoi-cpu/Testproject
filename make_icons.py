import struct, zlib, math

def lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i]-a[i])*t)) for i in range(3))

def pixel(x, y, size):
    bg = (20, 17, 14)
    ring_dark = (110, 66, 36)
    ring_light = (196, 150, 96)
    bark = (92, 58, 32)
    green = (92, 194, 122)
    cx = cy = size/2.0
    dx, dy = x - cx, y - cy
    d = math.sqrt(dx*dx + dy*dy)
    R = size * 0.34
    if d <= R:
        t = d / R
        if t > 0.86:
            return bark
        rings = (math.sin(t * math.pi * 7) + 1) / 2.0
        return lerp(ring_light, ring_dark, rings * 0.7)
    ang = math.atan2(dy, dx)
    leaf = size * 0.40 + math.sin(ang * 6) * size * 0.035
    if d <= leaf:
        return green
    return bg

def write_png(path, size):
    raw = bytearray()
    for y in range(size):
        raw.append(0)
        for x in range(size):
            raw += bytes(pixel(x, y, size))
    comp = zlib.compress(bytes(raw), 9)
    def chunk(tag, data):
        c = struct.pack('>I', len(data)) + tag + data
        return c + struct.pack('>I', zlib.crc32(tag + data) & 0xffffffff)
    ihdr = struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0)
    png = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', ihdr) + chunk(b'IDAT', comp) + chunk(b'IEND', b'')
    with open(path, 'wb') as f:
        f.write(png)
    print('wrote', path, size)

base = r'C:\Users\atsuj\Desktop\Testfolder'
write_png(base + r'\icon-192.png', 192)
write_png(base + r'\icon-512.png', 512)
write_png(base + r'\icon-512-maskable.png', 512)
