import ocr


import mss
import mss.tools


with mss.mss() as sct:
    # Get information of monitor 2
    monitor_number = 1
    mon = sct.monitors[monitor_number]

    # The screen part to capture
    monitor = {
        "top": mon["top"] + 270,  # 100px from the top
        "left": 0 - 630,  # 100px from the left
        "width": 284,
        "height": 307,
        "mon": monitor_number,
    }
    output = "image.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)
    print(ocr.ocr_core('image.png'))

# import ocr

# print('Image contains...')
# print(ocr.ocr_core('image.png'))
