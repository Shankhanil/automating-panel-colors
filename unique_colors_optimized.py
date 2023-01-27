import multiprocessing as mp
import numpy as np
import cv2

def generate_slices(img, i, j):
    subimg = img[
        int(i*N/N_patches) : int( (i+1)*N/N_patches ),
        int(j*N/N_patches) : int( (j+1)*N/N_patches ),
    ]
    panel_colors = np.unique(subimg.reshape(-1, subimg.shape[2]), axis=0)

    print(panel_colors.tolist())
    return panel_colors.tolist()


if __name__ == "__main__":

    img = cv2.imread('T-Shirt_UVMaps_Naming convention.png')   #[0:1024, 0:1024, :]

    w, h, _ = img.shape
    assert w == h
    N = w
    N_patches = 16


    print(w, h)

    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(mp.cpu_count())

    # Step 2: `pool.apply` the `howmany_within_range()`
    results = [pool.apply(generate_slices, args=(img, i, j)) for i in range(0,N_patches) for j in range(0,N_patches)]

    # Step 3: Don't forget to close
    pool.close()

    # print(results)

    assert len(results) == N_patches**2

    res = []
    # res = zip( iterables=results )

    for panels in results:
        res.extend(panels)
    
    # print(set(res))
    setres = []

    for item in res:
        if item not in setres:
            setres.append(item)

    print("setres")
    print(setres)