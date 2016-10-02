import os
import getpass
import time
import shutil
#Coded by 0xyg3n
#Trying to make your life easier with this.
def banner():
        os.system('clear')
        print """
___  ____ ____ ____    _  _ ____ ____    ____ ___  _ ___ ____ ____
|__] |___ |___ |___ __  \/  [__  [__  __ |___ |  \ |  |  |  | |__/
|__] |___ |___ |       _/\_ ___] ___]    |___ |__/ |  |  |__| |  \ ver 1.0

Coded By 0xyg3n

"""


def config():
    banner()
    ipathbeef=raw_input(' Please Specify Beef-Xss Path (Default /usr/share/beef-xss/): ')
    print ''
    fhost=raw_input(" [i]Host: ")
    print ''
    fport=raw_input(" [i]Port: ")
    print ''
    hookname=raw_input(" [i]Hook.js Rename: ")
    print ''
    ui=raw_input(" [i]Panel: ")
    print ''
    buser=raw_input(" [i]Beef Username: ")
    print ''
    bpasswd=getpass.getpass(" [i]Beef Password: ")

    os.system('clear')
    banner()
    print '''
+==============================================+
[i]Host: '''+fhost+'''\n
[i]Port: '''+fport+'''\n
[i]HookJS: '''+hookname+'''\n
[i]Panel: '''+ui+'''\n
[i]Beef Username: '''+buser+'''\n
[i]Beef PassWord: ******
+==============================================+

'''
    time.sleep(4)


    data='''
#
# Copyright (c) 2006-2016 Wade Alcorn - wade@bindshell.net
# Browser Exploitation Framework (BeEF) - http://beefproject.com
# See the file 'doc/COPYING' for copying permission
#
# BeEF Configuration file

beef:
    version: '0.4.7.0-alpha'
    # More verbose messages (server-side)
    debug: false
    # More verbose messages (client-side)
    client_debug: false
    # Used for generating secure tokens
    crypto_default_value_length: 80

    # Interface / IP restrictions
    restrictions:
        # subnet of IP addresses that can hook to the framework
        permitted_hooking_subnet: "0.0.0.0/0"
        # subnet of IP addresses that can connect to the admin UI
        #permitted_ui_subnet: "127.0.0.1/32"
        permitted_ui_subnet: "0.0.0.0/0"

    # HTTP server
    http:
        debug: false #Thin::Logging.debug, very verbose. Prints also full exception stack trace.
        host: "'''+fhost+'''"
        port: "'''+fport+'''"

        # Decrease this setting to 1,000 (ms) if you want more responsiveness
        #  when sending modules and retrieving results.
        # NOTE: A poll timeout of less than 5,000 (ms) might impact performance
        #  when hooking lots of browsers (50+).
        # Enabling WebSockets is generally better (beef.websocket.enable)
        xhr_poll_timeout: 1000

        # Reverse Proxy / NAT
        # If BeEF is running behind a reverse proxy or NAT
     	#  set the public hostname and port here
        #public: ""      # public hostname/IP address
        #public_port: "" # experimental

        # DNS
        dns_host: "localhost"
        dns_port: 53

        # Web Admin user interface URI
        web_ui_basepath: "/'''+ui+'''"

        # Hook
        hook_file: "/'''+hookname+'''.js"
        hook_session_name: "BEEFHOOK"
        session_cookie_name: "BEEFSESSION"

        # Allow one or multiple origins to access the RESTful API using CORS
        # For multiple origins use: "http://browserhacker.com, http://domain2.com"
  	restful_api:
            allow_cors: false
            cors_allowed_domains: "http://browserhacker.com"

        # Prefer WebSockets over XHR-polling when possible.
        websocket:
            enable: false
            port: 61985 # WS: good success rate through proxies
            # Use encrypted 'WebSocketSecure'
            # NOTE: works only on HTTPS domains and with HTTPS support enabled in BeEF
            secure: true
            secure_port: 61986 # WSSecure
            ws_poll_timeout: 1000 # poll BeEF every second
            ws_connect_timeout: 500 # useful to help fingerprinting finish before establishing the WS channel

        # Imitate a specified web server (default root page, 404 default error page, 'Server' HTTP response header)
        web_server_imitation:
	    enable: true
            type: "apache" # Supported: apache, iis, nginx
            hook_404: false # inject BeEF hook in HTTP 404 responses
            hook_root: false # inject BeEF hook in the server home page
        # Experimental HTTPS support for the hook / admin / all other Thin managed web services
        https:
            enable: false
            # In production environments, be sure to use a valid certificate signed for the value
            # used in beef.http.dns_host (the domain name of the server where you run BeEF)
            key: "beef_key.pem"
            cert: "beef_cert.pem"

      database:
        # For information on using other databases please read the
        # README.databases file

        # supported DBs: sqlite, mysql, postgres
        # NOTE: you must change the Gemfile adding a gem require line like:
        #   gem "dm-postgres-adapter"
        # or
        #   gem "dm-mysql-adapter"
        # if you want to switch drivers from sqlite to postgres (or mysql).
        # Finally, run a 'bundle install' command and start BeEF.
        driver: "sqlite"

        # db_file is only used for sqlite
        db_file: "beef.db"

        # db connection information is only used for mysql/postgres
        db_host: "localhost"
        db_port: 3306
        db_name: "beef"
        db_user: "beef"
        db_passwd: "beef"
        db_encoding: "UTF-8"

    # Credentials to authenticate in BeEF.
    # Used by both the RESTful API and the Admin_UI extension
    credentials:
        user:   "'''+buser+'''"
        passwd: "'''+bpasswd+'''"

    # Autorun Rule Engine
    autorun:
        # this is used when rule chain_mode type is nested-forward, needed as command results are checked via setInterval
        # to ensure that we can wait for async command results. The timeout is needed to prevent infinite loops or eventually
        # continue execution regardless of results.
        # If you're chaining multiple async modules, and you expect them to complete in more than 5 seconds, increase the timeout.
        result_poll_interval: 300
        result_poll_timeout: 5000

        # If the modules doesn't return status/results and timeout exceeded, continue anyway with the chain.
        # This is useful to call modules (nested-forward chain mode) that are not returning their status/results.
        continue_after_timeout: true
    # Enables DNS lookups on zombie IP addresses
    dns_hostname_lookup: false

    # IP Geolocation
    # NOTE: requires MaxMind database:
    #   curl -O http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
    #   gunzip GeoLiteCity.dat.gz && mkdir /opt/GeoIP && mv GeoLiteCity.dat /opt/GeoIP
    geoip:
        enable: false
        database: '/opt/GeoIP/GeoLiteCity.dat'

    # Integration with PhishingFrenzy
    # If enabled BeEF will try to get the UID parameter value from the hooked URI, as this is used by PhishingFrenzy
    # to uniquely identify the victims. In this way you can easily associate phishing emails with hooked browser.
    integration:
        phishing_frenzy:
            enable: false
    # You may override default extension configuration parameters here
    extension:
        requester:
            enable: true
        proxy:
            enable: true
            key: "beef_key.pem"
            cert: "beef_cert.pem"
        metasploit:
            enable: false
        social_engineering:
            enable: true
        evasion:
            enable: false
        ipec:
            enable: true
     # this is still experimental..
        dns:
    	    enable: false
     # this is still experimental..
        dns_rebinding:
            enable: false
'''
    print ''
    print '[*]Writing Out Current Settings Into config.yaml..\n'
    conf = open('config.yaml', "w")
    conf.write(data)
    conf.close()
    time.sleep(3)
    print '[*]Moving To Beef Directory..\n'
    wfilew='config.yaml'
    os.system ("mv"+ " " + wfilew + " " + ipathbeef)
    time.sleep(3)
    print '[*]Done.\n'
    exit()

config()
