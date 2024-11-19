match input("1. latlong to sl\n2.sl to latlong\n: "):
    case "1":
        print(32*float(input("N+W+E-S- latlong: "))/45 + 64)
    case "2":
        print(45*(float(input("sl: "))-64)/32)