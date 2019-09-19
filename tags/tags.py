import os
from random import randrange


class Tags(object):


    def __init__(self):
        self.tags = []
        list_rand = self.shake()
        #print(list_rand)
        for r in range(4):
            self.tags.append([])
            for c in range(4):
                self.tags[r].append(list_rand.pop(0))


        #for r in range(4):
        #    print(self.tags[r])

        self.printer()


    def shake(self):
        list = []
        list_rand = []
        for i in range(16):
            list.append(i)

        while len(list) > 0:
            list_rand.append(list.pop(randrange(len(list))))

        #print(list_rand)
        return(list_rand)


        def testShake(self, list_rand):
            k = 0
            while len(list_rand) > 0:
                for i in list_rand:
                    if (list_rand[0] > list_rand[i] and
                        list_rand[0] != 0 and list_rand[i] != 0):
                        k += 1

                i = 0

            while list_rand[i] != 0:
                i += 1
            k += i // 4

            if  (k % 2) == 1:
                return False
            else:
                return True


    def printer(self):
        os.system('cls')
        print()
        print()
        for r in range(4):
            for c in range(4):
                print(self.tags[r][c], ' '*(c + 5), end = '')
            print()
            print()


    def search(self, c1):
        print('c: ', c1)
        rc = -1
        cc = -1
        r0 = -1
        c0 = -1
        for r in range(4):
            for c in range(4):
                #print('self: ', self.tags[r][c])
                if self.tags[r][c] == int(c1):
                    rc = r
                    cc = c
                    #print('YES: ', self.tags[r][c])
                elif self.tags[r][c] == 0:
                    r0 = r
                    c0 = c

        print('rc:', rc, ' cc: ', cc)
        print('r0: ', r0, ' c0: ', c0)

        if rc != -1 and cc != -1 and r0 != -1 and c0 != -1:
            #print("вернул ответ")
            return [rc, cc, r0, c0]
        else:
            #print("вернул 0")
            return 0



    def move(self, c1):
        search = self.search(c1)
        print("search: ", search)
        rc = -1
        cc = -1
        r0 = -1
        c0 = -1
        if search != 0:
            rc, cc, r0, c0 = search
            #rc = int(search[0])
            #cc = int(search[1])
            #r0 = int(search[2])
            #c0 = int(search[3])
            print("Нашел")

            if (rc - r0 == 1 or r0 - rc == 1) and (cc == c0):
                self.tags[r0][c0] = self.tags[rc][cc]
                self.tags[rc][cc] = 0
            elif (cc - c0 == 1 or c0 - cc == 1) and (rc == r0):
                self.tags[r0][c0] = self.tags[rc][cc]
                self.tags[rc][cc] = 0
            else:
                print("не смог найти куда двигать")



tag = Tags()

while True:
    try:
        i = int(input('#>'))
        if i in range(1,15):
            tag.move(i)
            print()
            print()
            tag.printer()
        else:
            tag.printer()
    except Exception as e:
        tag.printer()
        pass
    #tag.move(input('#>'))
