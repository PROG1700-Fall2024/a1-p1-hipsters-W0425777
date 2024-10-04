#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.
#Student: Katherine Tucker

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #welcome message
    print("Welcome to the delivery calculator :)")

    #input name
    name = input("Please enter the customer's name: ")

    #input distnace
    km = input("How many Kilometers is the delivery? ")

    #input recipt
    purch = input("What how much is the purchase? ")

    #math
    delTotal = (float(km) * 15)

    tax = (float(purch) * 0.14)

    purTotal = (float(tax) + float(purch))

    total = (delTotal + purTotal)

    #print delivery, purchase, total
    print("\nPurchase Summary for {0}\n".format(name))
    print("Delivery Cost: ${0:.2f}".format(delTotal))
    print("Purchase Cost: ${0:.2f}".format(purTotal))
    print("Total Cost: ${0:.2f}".format(total))

    # YOUR CODE ENDS HERE

main()