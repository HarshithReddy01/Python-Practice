def volume(legth=1,breadth=1,height=1):
    print(legth, breadth, height)
    vol = legth*breadth*height
    return vol

if __name__ == '__main__':
    v = volume(10)
    print(v)