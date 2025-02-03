pixels = [16711680, 31488, 255, 8060928, 123, 8092416, 0, 8092539]

pixels.pop(0)
print(pixels)
exit()
for pixel in pixels:
    bit_string = ("{:0{width}b}".format(pixel, width=24))
    rgb_pixel = (int(bit_string[16:24], 2), int(bit_string[8:16], 2), int(bit_string[:8], 2))

    # print(rgb_pixel)