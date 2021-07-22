import portscanner


try:
    targets_ip = input("[+] * Enter Target To Scan : ")
    port_num = int(input("[+] * Enter Amount Of Port: "))
    vuln_list = input("[+] * Enter File Path List Of Vulnerability File: ")

    target = portscanner.PortScan(targets_ip, port_num)
    target.scan()

    # print("\n")
    #
    # with open(vuln_list, "r") as file:
    #     count = 0
    #     for banner in target.banners:
    #         file.seek(0)
    #         for line in file.readlines():
    #             if line.strip() in banner:



except KeyboardInterrupt:
    print("\n")
    exit("Program CLosed")


#
# with open(vuln_list, "r") as file:
#     count = 0
#     for banner in