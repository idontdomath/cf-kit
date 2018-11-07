import click
import cf.cache
import cf.firewall

@click.group(help='cf-kit: simple command line client for usual tasks on cloudflare.')
def cfkit_cli():
	pass

@click.command(help='purge everything from the cache of a cloudflare zone. with great power comes great responsibility.')
@click.option('--zone','-z', required=True, help='cloudflare zone name')
def purge_everything(zone):
	cf.cache.purge_everything(zone)

@click.command(help='purge and url from the cache of a cloudflare zone')
@click.option('--zone','-z', required=True, help='cloudflare zone name')
@click.option('--url','-u', required=True, help='url to purge')
def purge_by_url(zone, url):
	# FIXME: validation
	# TODO: list of urls
	cf.cache.purge_individual_files_by_url(zone, [url])

@click.command(help='purge tags from the cache of a cloudflare zone')
@click.option('--zone','-z', required=True, help='cloudflare zone name')
@click.option('--tag','-t', required=True, help='tag to purge')
def purge_by_tags(zone, tag):
	# FIXME: validation
	# TODO: list of multiple tags
	cf.cache.purge_by_tags(zone,[tag])

@click.command(help='block an ip on the cloudflare ip firewall')
@click.option('--zone','-z', required=True, help='cloudflare zone name')
@click.option('--ip','-i', required=True, help='ip to block from the zone')
def ip_block(zone, ip):
	# FIXME: ip validation
	cf.firewall.firewall_block_ip(zone, ip)

@click.command(help='whitelist an ip on the cloudflare ip firewall')
@click.option('--zone','-z', required=True, help='cloudflare zone name')
@click.option('--ip','-i', required=True, help='ip to block from the zone')
def ip_whitelist(zone, ip):
	# FIXME: ip validation
	cf.firewall.firewall_whitelist_ip(zone, ip)

cfkit_cli.add_command(purge_everything)
cfkit_cli.add_command(ip_block)
cfkit_cli.add_command(ip_whitelist)
cfkit_cli.add_command(purge_by_url)
cfkit_cli.add_command(purge_by_tags)