

import meraki 
 
API_KEY = 'your API key'
dashboard = meraki.DashboardAPI(API_KEY)
old_switch = input("Enter OLD switch serial#: ")
new_switch = input("Enter NEW switch serial#: ")
 


                
# Port 1 through 48 (48 LAN, 4 uplinks, 2 stacking, +1 for range ending index)
for port_id in range(1, 48+4+2+1):
    config = dashboard.switch.getDeviceSwitchPort(old_switch, port_id)
    
    # Clone corresponding new switch


    # Access type port
    if config['type'] == 'access':
        dashboard.switch.updateDeviceSwitchPort(new_switch, port_id,
            name=config['name'], porttype=config['type'], vlan=config['vlan'], voicevlan=config['voiceVlan'],
            poe=config['poeEnabled'], isolation=config['isolationEnabled'], rstp=config['rstpEnabled'],
            stpguard=config['stpGuard'])

    # Trunk type port
    elif config['type'] == 'trunk':
        dashboard.switch.updateDeviceSwitchPort(new_switch, port_id,
            name=config['name'], porttype=config['type'], vlan=config['vlan'], allowedvlans=config['allowedVlans'],
            poe=config['poeEnabled'], isolation=config['isolationEnabled'], rstp=config['rstpEnabled'],
            stpguard=config['stpGuard'])
                