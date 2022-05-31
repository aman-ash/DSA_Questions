def classPhotos(redShirtHeights, blueShirtHeights):
    if len(redShirtHeights) < 1:
        return

    redShirtHeights.sort()
    blueShirtHeights.sort()
    Idx = 1

    if redShirtHeights[0] > blueShirtHeights[0]:
        while Idx < len(redShirtHeights) and redShirtHeights[Idx] > blueShirtHeights[Idx]:
            Idx += 1
    else:
        while Idx < len(redShirtHeights) and blueShirtHeights[Idx] > redShirtHeights[Idx]:
            Idx += 1

    return Idx == len(redShirtHeights)


if __name__ == "__main__":
    redShirtHeights = [5, 8, 1, 3, 4]
    blueShirtHeights = [6, 9, 2, 4, 5]
    print(classPhotos(redShirtHeights, blueShirtHeights))
