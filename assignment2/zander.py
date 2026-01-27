def check_zander_size(length):
    if length < 42:
        difference = 42 - length
        print("The zander does not meet the size limit.")
        print(f"Release the fish back into the lake. It is {difference:.1f} cm below the size limit.")
    else:
        print("The zander meets the size limit. You may keep it.")

length = float(input("Enter the length of the zander in centimeters: "))
check_zander_size(length)