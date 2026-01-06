def volume(legth,breadth,height):
    print(legth, breadth, height)
    vol = legth*breadth*height
    return vol

if __name__ == '__main__':
    v = volume(10,5,3)
    print(v)