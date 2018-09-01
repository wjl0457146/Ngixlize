import xlrd

book = xlrd.open_workbook('2018.xlsx')
sheet = book.sheet_by_index(3)
nrows = sheet.nrows

#n = 21

def Ngixlize():
    print("stream {")
    print("     upstream app-%s {") %virtul_port
    print("         server %s:%s     max_fails=3 fail_timeout=30s;") %(upstream_ip1, upstream_port1)
    print("         server %s:%s     backup") %(upstream_ip2, upstream_port2)
    print("     }")
    print("     server {")
    print("         listen *:%s;") %virtul_port
    print("         proxy_timeout 20s;")
    print("         proxy_pass app-%s;") %virtul_port
    print("     }")
    print("}")

for n in range(1,nrows,2):
    value1 = sheet.row_values(n,1,7)
    value2 = sheet.row_values(n+1,1,7)
    virtul_ip = value1[0]
    virtul_port = int(value1[1])
    upstream_ip1 = value1[3]
    upstream_port1 = int(value1[4])
    masterorbackup1 = value1[5]
    upstream_ip2 = value2[3]
    upstream_port2 = int(value2[4])
    masterorbackup2 = value2[5]
    Ngixlize()


