import CloudFlare

# Set to false if you wanna avoid Debug Information
DEBUG=True

def firewall_create_rule(a_zone_name, firewall_data):
    cf = CloudFlare.CloudFlare(debug=DEBUG)
    zones = cf.zones.get(params={'name': a_zone_name})
    # check que pasa si la zona no existe.
    if len(zones) == 1:
        zone_id = zones[0]['id']
        cf.zones.firewall.access_rules.rules.post(zone_id, data=firewall_data)
        #todo check statuses         
    exit(0)

def firewall_whitelist_ip(a_zone_name, ip):
    firewall_create_rule(a_zone_name,{"mode":"whitelist","configuration":{"target":"ip","value":ip}})

def firewall_block_ip(a_zone_name, ip):
    firewall_create_rule(a_zone_name,{"mode":"block","configuration":{"target":"ip","value":ip}})
