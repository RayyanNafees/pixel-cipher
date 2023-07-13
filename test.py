from compressor import pixelize, unpixelize
import time

inp = 'Latex.pdf'
out = 'Latex.png'

start = time.time()

pixelize(inp, out)

print("Time: ",time.time()-start)