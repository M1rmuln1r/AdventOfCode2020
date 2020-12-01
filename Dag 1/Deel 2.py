file = open('input.txt', 'r')
text = file.readlines()
file.close()


for eerstegetal in text:
    for tweedegetal in text:
        for derdegetal in text:
            eerstegetal = int(eerstegetal)
            tweedegetal = int(tweedegetal)
            derdegetal = int(derdegetal)
            resulaat=(eerstegetal+tweedegetal+derdegetal)
            if resulaat == 2020:
                print(eerstegetal)
                print(tweedegetal)
                print(derdegetal)
                print(eerstegetal*tweedegetal*derdegetal)
                exit(0)
