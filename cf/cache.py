import CloudFlare

# Set to false if you wanna avoid Debug Information
DEBUG=True

def purge_individual_files_by_url(a_zone_name, urls):
    purge_cache(a_zone_name, {"files": urls})

def purge_everything(a_zone_name):
    purge_cache(a_zone_name,{"purge_everything": True})

def purge_by_tags(a_zone_name, tags):
    purge_cache(a_zone_name,{"tags": tags})

def purge_cache(a_zone_name, purge_data):
    cf = CloudFlare.CloudFlare(debug=DEBUG)
    zones = cf.zones.get(params={'name': a_zone_name})
    # check que pasa si la zona no existe.
    if len(zones) == 1:
        zone_id = zones[0]['id']
        cf.zones.purge_cache.delete(zone_id, data=purge_data)
        #todo check statuses         
    exit(0)
