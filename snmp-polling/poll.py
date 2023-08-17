from easysnmp import Session

def fetch_snmp_data(host, community, oid):
    session = Session(hostname=host, community=community, version=2)
    result = session.get(oid)
    return result.value

# Test the function
host = '10.21.10.250'
community = 'public'  # use the appropriate community string
oid = 'your-oid-here'

data = fetch_snmp_data(host, community, oid)
print(data)
