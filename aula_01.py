import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from numpy import bitwise_and, bitwise_or, bitwise_xor, bitwise_not


def show_image(img, nome_janela="imagem"):
    imagem = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.title(nome_janela)
    plt.imshow(imagem)
    plt.show()


# TODO: ADICIONAR FUNÇÃO PARA EXIBIÇÃO EM GRADE: 1x2, 1x3, 2x2...


def get_color(img, x, y):
    return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)


def set_color(img, x, y, b, g, r):
    img.itemset((y, x, 0), b)
    img.itemset((y, x, 1), g)
    img.itemset((y, x, 2), r)
    return img


def save_image(nome: str, source):
    status = cv.imwrite(nome+'.jpg', source)
    print(f"Imagem salva: {status}")


def show_part(source, y_inicial, x_inicial, tam):
    return source[y_inicial:y_inicial + tam, x_inicial:x_inicial + tam]


def soma_imagens(img1, img2):
    img = cv.add(img1, img2)
    return img


def sub_imagens(img1, img2):
    img = cv.subtract(img1, img2)
    return img


def multiply_imagens(img1, img2):
    img = cv.multiply(img1, img2)
    return img


def divide_imagens(img1, img2):
    img = cv.divide(img1, img2)
    return img


def bitwise_operation(img1, op,  img2=[]):
    if op == 'and':
        res = bitwise_and(img1, img2)
        return res
    elif op == 'or':
        res = bitwise_or(img1, img2)
        return res
    elif op == 'xor':
        res = bitwise_xor(img1, img2)
        return res
    elif op == 'not':
        res = bitwise_not(img1)
        return res
    else:
        print('Operação inválida')
        return


def main():
    image1 = cv.imread('dogb.jpg')
    image2 = cv.imread('doga.jpg')

    # altura, largura, qtd_canais = image.shape
    # print(f'Altura: {altura}\nLargura: {largura}\nQuantidade de canais: {qtd_canais}')
    #
    # for y in range(0, altura):
    #     for x in range(0, largura):
    #         # Busca a informação de cor do pixel
    #         # o último argumento representa o canal (BGR)
    #         blue, green, red = get_color(image, x, y)
    #
    #         # exibindo apenas um canal
    #         # no exemplo eu deixo apenas o azul
    #         # image = set_color(image, x, y, 0, 0, red)
    #
    #
    # # showImage(image)
    # # save_image("nova_imagem.png", image)
    # recorte = show_part(image, 98, 190, 15)
    # showImage(recorte)

    # Realizando soma
    # resultado = soma_imagens(image1, image2)
    # showImage(resultado)

    # Realizando subtração de imagens
    # resultado = sub_imagens(image1, image2)
    # showImage(resultado)

    # Realizando multiplicação de imagens
    # resultado = multiply_imagens(image1, image2)
    # showImage(resultado)

    # Realizando divisão de imagens
    # resultado = divide_imagens(image1, image2)
    # show_image(resultado, nome_janela="imagem dividida")

    # OPERAÇÕES COM BITWISE
    bit_not = bitwise_operation(img1=image1, img2=image2, op='not')
    bit_and = bitwise_operation(img1=image1, img2=image2, op='and')
    bit_or = bitwise_operation(img1=image1, img2=image2, op='or')
    bit_xor = bitwise_operation(img1=image1, img2=image2, op='xor')
    # show_image(bit_not, nome_janela="Bitwise NOT")
    # show_image(bit_and, nome_janela="Bitwise AND")
    # show_image(bit_or, nome_janela="Bitwise OR")
    # show_image(bit_xor, nome_janela="Bitwise XOR")

    # GRID de imagens
    # fake = np.zeros((image1.shape[0], image1.shape[1], 3), np.uint8)
    # hori = np.concatenate((bit_not, bit_and), axis=1)
    # hori2 = np.concatenate((bit_or, bit_xor), axis=1)
    # vert = np.concatenate((hori, hori2), axis=0)
    # cv.imshow('Horizontal', vert)
    # cv.waitKey(0)
    # cv.destroyAllWindows()




if __name__ == "__main__":
    main()
