import tqdm
from tqdm import tqdm, trange
import time

pbar = tqdm(total=25)

for i in range(25):
    time.sleep(0.3)
    pbar.update(1)

pbar.close()