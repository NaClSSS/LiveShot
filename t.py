import random
from PIL import Image
from numpy import *
a, b = input().split()
print(a, b)
exit()

def get_thum(image, size=(64, 64), greyscale=False):
    # 利用image对图像大小重新设置, Image.ANTIALIAS为高质量的
    # image = image.resize(size, Image.ANTIALIAS)
    if greyscale:
        # 将图片转换为L模式，其为灰度图，其每个像素用8个bit表示
        image = image.convert('L')
    return image


def image_similarity_vectors_via_numpy(image1, image2):
    image1 = get_thum(image1)
    image2 = get_thum(image2)
    images = [image1, image2]
    vectors = []
    norms = []
    for image in images:
        vector = []
        for pixel_tuple in image.getdata():
            vector.append(average(pixel_tuple))
        vectors.append(vector)
        # linalg=linear（线性）+algebra（代数），norm则表示范数
        # 求图片的范数？？
        norms.append(linalg.norm(vector, 2))
    a, b = vectors
    a_norm, b_norm = norms
    # dot返回的是点积，对二维数组（矩阵）进行计算
    res = dot(a / a_norm, b / b_norm)
    return res


with open('a.txt', 'w') as f:
    t = 10
    f.write(str(t)+'\n')
    # for i in range(t):
    #     t = 5
    #     f.write(str(t) + '\n')
    #     a = [[0, 0], [0, 2], [2, 0], [1, 1], [2, 2]]
    #     random.shuffle(a)
    #     for x in a:
    #         f.write('%d %d\n' % (x[0], x[1]))
    for i in range(t):
        n = random.randint(10, 11)
        f.writelines(str(n)+'\n')
        for j in range(n):
            f.writelines('%d %d\n' % (random.randint(0, 100), random.randint(0, 100)))