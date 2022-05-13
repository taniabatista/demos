def sort_list_of_csv_products(csv, expected):
    """
    csv list of products: [title, popularity, price]
    sort by popularity (desc), price (asc)
    return name
    """
    products = [p.split(',') for p in csv]
    ranked = sorted(products, key=lambda p: (-int(p[1]), int(p[2])))
    return [r[0] for r in ranked] == expected


csv = ["Selfie Stick,98,29", "iPhone Case,90,15", "Fire TV Stick,48,49", "Wyze Cam,48,25", "Water Filter,56,49", "Blue Light Blocking Glasses,90,16", "Ice Maker,47,119", "Video Doorbell,47,199", "AA Batteries,64,12", "Disinfecting Wipes,37,12", "Baseball Cards,73,16", "Winter Gloves,32,112", "Microphone,44,22", "Pet Kennel,5,24", "Jenga Classic Game,100,7", "Ink Cartridges,88,45", "Instant Pot,98,59", "Hoze Nozzle,74,26", "Gift Card,45,25", "Keyboard,82,19"]

expected = ["Jenga Classic Game", "Selfie Stick", "Instant Pot", "iPhone Case", "Blue Light Blocking Glasses", "Ink Cartridges", "Keyboard", "Hoze Nozzle", "Baseball Cards", "AA Batteries", "Water Filter", "Wyze Cam", "Fire TV Stick", "Ice Maker", "Video Doorbell", "Gift Card", "Microphone", "Disinfecting Wipes", "Winter Gloves", "Pet Kennel"]

print(sort_list_of_csv_products(csv, expected))
