#!/usr/bin/env python3

from ciscoconfparse import CiscoConfParse
import re

class LINA:
    def generate_header_h1(self,text):
        header_list = []
        header_list.append('\n\n')
        header_list.append('############################################################')
        header_list.append('# {}'.format(text))
        header_list.append('############################################################')
        return header_list

    def generate_header_h2(self,text):
        header_list = []
        header_list.append('\n\n')
        header_list.append('!------------------------------------------------------------!')
        header_list.append('! {}'.format(text))
        header_list.append('!------------------------------------------------------------!\n')
        return header_list

    def print_list (self,input_list):
        for line in input_list:
            print(line)
        return

    def build_show_cmds_dict(self,config):
        show_cmds_dict = {}
        show_cmd = None
        confparse = CiscoConfParse(config)
        for line in confparse.find_lines('.'):
          if re.search(r'#\s+show|#\s+more',line):
            show_cmd = line.split("#")[1]
            show_cmd = show_cmd.strip()
            show_cmds_dict[show_cmd] = []
          if show_cmd is not None:
            show_cmds_dict[show_cmd].append(line)
        return show_cmds_dict


    def get_output(self,cmd_regex,show_cmds_dict):
        cmd_output = None
        for show_cmd in show_cmds_dict.keys():
            if re.search(cmd_regex,show_cmd):
               cmd_output = show_cmds_dict[show_cmd]
               print(show_cmd)
        if cmd_output is not None:
            return cmd_output
        else:
            return ['No output found for \"{}\" command'.format(re.sub('\
                ?','',cmd_regex))]

    def get_show_version(self,config):
        cmd_regex = r'sho?w? vers?i?o?n?'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_run(self,config):
        cmd_regex = r'sho?w? runn?i?n?g?-?c?o?n?f?i?g?|more system:running-config'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_access_list(self,config):
        cmd_regex = r'sho?w? access-li?s?t?'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_xlate(self,config):
        cmd_regex = r'sho?w? xla?t?e?'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_connections(self,config):
        cmd_regex = r'sho?w? conn'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_ip_address(self,config):
        cmd_regex = r'sho?w? ip addr?e?s?s?'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_arp(self,config):
        cmd_regex = r'sho?w? arp'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_interfaces(self,config):
        cmd_regex = r'sho?w? int?e?r?f?a?c?e?s?'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_failover(self,config):
        cmd_regex = r'sho?w? failover'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_route(self,config):
        cmd_regex = r'sho?w? route'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_eigrp_neighbor(self,config):
        cmd_regex = r'sho?w? eig?r?p? nei?g?h?b?o?r?'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_eigrp_topology(self,config):
        cmd_regex = r'sho?w? eig?r?p? topo?l?o?g?y?'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_ospf_neighbor(self,config):
        cmd_regex = r'sho?w? ospf? neig?h?b?o?r?'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_ospf_database(self,config):
        cmd_regex = r'sho?w? ospf? dat?a?b?a?s?e?'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_ospf_interface(self,config):
        cmd_regex = r'sho?w? ospf? int?e?r?f?a?c?e?'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_vpn_sessiondb_summary(self,config):
        cmd_regex = r'sho?w? vpn-s?e?s?s?i?o?n?d?b? sum?m?a?r?y?'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_vpn_sessiondb(self,config):
        cmd_regex = r'sho?w? vpn-s?e?s?s?i?o?n?d?b?$'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_crypto_ipsec_sa(self,config):
        cmd_regex = r'sho?w? cry?p?t?o? ips?e?c? sa'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_crypto_isakmp_sa(self,config):
        cmd_regex = r'sho?w? cry?p?t?o? isa?k?m?p? sa'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_crypto_ikev1_sa_detail(self,config):
        cmd_regex = r'sho?w? cry?p?t?o? ikev1 sa deta?i?l?'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_crypto_ikev2_sa_detail(self,config):
        cmd_regex = r'sho?w? cry?p?t?o? ikev2 sa deta?i?l?'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_crypto_ca_trustpoints(self,config):
        cmd_regex = r'sho?w? cry?p?t?o? ca trust?p?o?i?n?t?s?'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)

    def get_show_crypto_ca_certificates(self,config):
        cmd_regex = r'sho?w? cry?p?t?o? ca cert?i?f?i?c?a?t?e?s?'
        show_cmds_dict = self.build_show_cmds_dict(config)
        return self.get_output(cmd_regex,show_cmds_dict)


    def group_acls_objects(self,config,acl_name='',hitcnt=False):
        output_list = []
        previous_acl_name = ""
        print_headers = False
        if acl_name == '':
            print_headers = True
        confparse = CiscoConfParse(config)
        for acl in confparse.find_lines('^access-list {}'.format(acl_name.strip())):
            # Clean new-line characters from ASA output
            acl = re.sub('\n+','',acl)
            if hitcnt is True:
                if 'hitcnt' in acl:
                    continue
            else:
                if 'hitcnt' in acl:
                    break
            if 'name hash' in acl:
                break
            # Split the ACL into a list
            acl_split = acl.split()
            acl_name = re.sub(';','',acl_split[1])

            if acl_name != previous_acl_name:
                acl_name = re.sub('name hash:.*','',acl_name)
                acl_name = re.sub('access-list ','',acl_name)
                if print_headers == True:
                    output_list += self.generate_header_h2(acl_name)
                previous_acl_name = acl_name
            else:
                if 'object' in acl:
                    output_list.append("!")
            for position, item in enumerate(acl_split):
                if item == 'object' or item == 'object-group':
                    object_name_position = position + 1
                    object_name = acl_split[object_name_position]
                    object_children = confparse.find_all_children(r'^object.*{}(\s|$)'.format(object_name))
                    for child in object_children:
                        if ('object object' in child) or ('group-object' in child):
                            net_object_name = child.split()[-1]
                            net_object_config = confparse.find_all_children(r'^object.*{}(\s|$)'.format(net_object_name))
                            for line in net_object_config:
                                output_list.append(line)
                    for child in object_children:
                        output_list.append(child)    
                    output_list.append('!')
            # output_list.append('!')
            # Add access-list to the acl+object output.
            output_list.append("{}".format(acl))
        return output_list

    def build_crypto_map_dict(self,config, crypto_map_name=None, crypto_map_seq=None):
        confparse = CiscoConfParse(config)
        crypto_map_dict = {}
        previous_map_seq = ''
        previous_map_name = ''
        pfs = False
        if (crypto_map_name is None) and (crypto_map_seq is not None):
            print('Error: crypto map sequence is defined without crypto map name')
            return
        crypto_map_filter = '{} {}'.format(crypto_map_name,crypto_map_seq).strip
        crypto_map_lines = confparse.find_lines('^crypto map {}'.format(crypto_map_filter))
        for line in crypto_map_lines:
            crypto_map_name = line.split(' ')[2]
            crypto_map_seq = line.split(' ')[3]

            if previous_map_name != crypto_map_name:
                crypto_map_dict[crypto_map_name] = {}
                previous_map_name = crypto_map_name

            if previous_map_seq != crypto_map_seq:
                previous_map_seq = crypto_map_seq
                if crypto_map_seq == 'interface':
                    crypto_map_dict[crypto_map_name]['interface'] = line.split(' ')[-1]
                else:
                    crypto_map_dict[crypto_map_name][crypto_map_seq] = {}

            if 'match address' in line:
                crypto_map_dict[crypto_map_name][crypto_map_seq]['acl'] = line.split(' ')[-1]

            if 'set peer' in line:
                map_peer_list = line.split(' ')[6:]
                crypto_map_dict[crypto_map_name][crypto_map_seq]['peer'] = map_peer_list

            if 'set ikev1' in line:
                crypto_map_dict[crypto_map_name][crypto_map_seq]['ikev1'] = {}
                if 'transform-set' in line:
                    ikev1_transform_list = line.split(' ')[7:]
                    crypto_map_dict[crypto_map_name][crypto_map_seq]['ikev1']['transform-set'] = ikev1_transform_list

            if 'set pfs' in line:
                pfs = line.split(' ')[5]
                crypto_map_dict[crypto_map_name][crypto_map_seq]['pfs'] = True
        # print(crypto_map_dict)
        return crypto_map_dict


    def get_group_policy(self,config,name):
        confparse = CiscoConfParse(config)
        configs = confparse.find_all_children('^group-policy {} '.format(name))
        return configs

    def get_tunnel_group(self,config,name):
        confparse = CiscoConfParse(config)
        configs = confparse.find_all_children('^tunnel-group {} '.format(name))
        return configs

    def get_object_network(self,config,name):
        confparse = CiscoConfParse(config)
        configs = confparse.find_all_children('^object.* network {}$'.format(name))
        return configs

    def get_ip_local_pool(self,config,name):
        confparse = CiscoConfParse(config)
        configs = confparse.find_all_children('^ip local pool {}'.format(name))
        return configs

    def group_group_policy(self,config,name):
        grouped_configs = []
        confparse = CiscoConfParse(config)
        configs = confparse.find_all_children('^group-policy {} '.format(name))
        for line in configs:
            if ' split-tunnel-network-list value' in line:
                access_list = line.split(' ')[3]
                grouped_configs += self.group_acls_objects(config,access_list)
                grouped_configs.append('!')
            if ' address-pools value ' in line:
                pool_name = line.split(' ')[3]
                grouped_configs += self.get_ip_local_pool(config,pool_name)
                grouped_configs.append('!')
        grouped_configs += configs
        return grouped_configs

    def group_aaa_server_group(self,config,name):
        grouped_configs = []
        confparse = CiscoConfParse(config)
        configs = confparse.find_all_children('^aaa-server {} '.format(name))
        for line in configs:
            if ' ldap-attribute-map ' in line:
                ldap_attribute_map = line.split(' ')[2]
                grouped_configs += self.get_ldap_attribute_map(config,ldap_attribute_map)
                grouped_configs.append('!')
        grouped_configs += configs
        return grouped_configs

    def get_ldap_attribute_map(self,config,name):
        confparse = CiscoConfParse(config)
        configs = confparse.find_all_children('^ldap attribute-map {}'.format(name))
        return configs

    def get_anyconnect_profile(self,config,name):
        confparse = CiscoConfParse(config)
        configs = confparse.find_children_w_parents('^webvpn','^anyconnect profiles {}'.format(name))
        return configs


    def group_crypto_map_config(self,config, crypto_map_name='', crypto_map_seq=''):
        confparse = CiscoConfParse(config)
        grouped_configs = []
        tunnel_group_configs = []
        previous_map_seq = ''
        if (crypto_map_name == '') and (crypto_map_seq != ''):
            print('Error: crypto map sequence is defined without crypto map name')
            return
        if (crypto_map_name != '') and (crypto_map_seq != ''):
            crypto_map_filter = '{} {}'.format(crypto_map_name,crypto_map_seq)
        elif crypto_map_name != '':
            crypto_map_filter = '{}'.format(crypto_map_name)
        else:
            crypto_map_filter = ''
        crypto_map_lines = confparse.find_lines('^crypto map {}'.format(crypto_map_filter.strip()))
        for line in crypto_map_lines:
            crypto_map_name = line.split(' ')[2]
            crypto_map_seq = line.split(' ')[3]
            if previous_map_seq != crypto_map_seq:
                if tunnel_group_configs != []:
                    grouped_configs += tunnel_group_configs
                tunnel_group_configs = []
                if previous_map_seq != '':     
                    grouped_configs.append("\n\n!----\n\n")
                previous_map_seq = crypto_map_seq
            if 'match address' in line:
                acl_name = line.split(' ')[-1]
                acl_and_objects = self.group_acls_objects(config,acl_name)
                grouped_configs += acl_and_objects
                grouped_configs.append('!')
            if 'set peer' in line:
                map_peer_list = line.split(' ')[6:]
                tunnel_group_configs.append('!')
                for peer in map_peer_list:
                    #print('peer:{}'.format(peer))
                    tunnel_group_configs += self.get_tunnel_group(config,peer)
                    # if len(map_peer_list) > 1:
                    #     tunnel_group_configs.append('!')
                #print(tunnel_group_configs)
            grouped_configs.append(line)
        grouped_configs += tunnel_group_configs
        # print(grouped_configs)
        return grouped_configs

    def group_static_nat_config(self,config):
        grouped_configs = []
        previous_nat_object = ''
        confparse = CiscoConfParse(config)
        nat_config_lines = confparse.find_lines('^nat ')
        for line in nat_config_lines:
            # Get Object configurations source original position
            if line.split(' ')[4] != 'any':
                nat_object = line.split(' ')[4]
                for obj_line in self.get_object_network(config,nat_object):
                    grouped_configs.append(obj_line)
                grouped_configs.append('!')
                previous_nat_object = nat_object
            # Get Object configurations source translate position
            if (line.split(' ')[5] != 'any') and (line.split(' ')[5] != previous_nat_object):
                nat_object = line.split(' ')[5]
                for obj_line in self.get_object_network(config,nat_object):
                    grouped_configs.append(obj_line)
                grouped_configs.append('!')
                previous_nat_object = nat_object
            if (len(line.split(' ')) > 6) and ((line.split(' ')[6] == 'destination') and (line.split(' ')[7] == 'static')):
                # Get Object configurations destination original position
                if (line.split(' ')[8] != 'any') and (line.split(' ')[8] != previous_nat_object):
                    nat_object = line.split(' ')[8]
                    for obj_line in self.get_object_network(config,nat_object):
                        grouped_configs.append(obj_line)
                    grouped_configs.append('!')
                    previous_nat_object = nat_object
                # Get Object configurations destination translate position
                if (line.split(' ')[9] != 'any') and (line.split(' ')[9] != previous_nat_object):
                    nat_object = line.split(' ')[9]
                    for obj_line in self.get_object_network(config,nat_object):
                        grouped_configs.append(obj_line)
                    grouped_configs.append('!')
                    previous_nat_object = nat_object
            nat_split = line.split()
            for position, item in enumerate(nat_split):
                if item == 'service':
                    service_obj1_position = position + 1
                    service_obj1_name = nat_split[service_obj1_position]
                    service_obj1_children = confparse.find_all_children(r'^object.*{}(\s|$)'.format(service_obj1_name))
                    for child in service_obj1_children:
                        if ('object object' in child) or ('group-object' in child):
                            net_object_name = child.split()[-1]
                            net_object_config = confparse.find_all_children(r'^object.*{}(\s|$)'.format(net_object_name))
                            for line in net_object_config:
                                grouped_configs.append(line)
                    for child in service_obj1_children:
                        grouped_configs.append(child)
                    grouped_configs.append('!')
                    service_obj2_position = position + 2
                    service_obj2_name = nat_split[service_obj2_position]
                    service_obj2_children = confparse.find_all_children(r'^object.*{}(\s|$)'.format(service_obj2_name))
                    for child in service_obj2_children:
                        if ('object object' in child) or ('group-object' in child):
                            net_object_name = child.split()[-1]
                            net_object_config = confparse.find_all_children(r'^object.*{}(\s|$)'.format(net_object_name))
                            for line in net_object_config:
                                grouped_configs.append(line)
                    for child in service_obj2_children:
                        grouped_configs.append(child)
                    grouped_configs.append('!')
            grouped_configs.append('!')
            grouped_configs.append(line)
            grouped_configs.append('\n\n!---\n\n')
        return grouped_configs

    def group_auto_nat_config(self,config):
        grouped_configs = []
        confparse = CiscoConfParse(config)
        config_lines = confparse.find_blocks('^ nat ')
        for line in config_lines:
            if 'object network' in line:
                grouped_configs.append(line)
                grouped_configs += confparse.find_children_w_parents('^{}$'.format(line),'.')
                grouped_configs.append('\n\n!---\n\n')
        return grouped_configs

    def group_anyconnect_config(self,config):
        grouped_configs = []
        confparse = CiscoConfParse(config)
        config_lines = confparse.find_all_children('^tunnel-group .* type remote-access')
        for line in config_lines:
            tg_configs = []
            profile_name = line.split(' ')[1]
            for cfg_line in confparse.find_all_children('^tunnel-group {} '.format(profile_name)):
                if ' address-pool' in cfg_line:
                    pool_name = cfg_line.split(' ')[2]
                    grouped_configs += self.get_ip_local_pool(config,pool_name)
                    grouped_configs.append('!')
                if ' default-group-policy' in cfg_line:
                    # gp_name = cfg_line.split(' ')[2]
                    gp_name = re.sub(' default-group-policy ','',cfg_line)
                    gp_config = self.group_group_policy(config,gp_name)
                    grouped_configs += gp_config
                    grouped_configs.append('!')
                if ' authentication-server-group ' in cfg_line:
                    server_group = cfg_line.split(' ')[2]
                    server_group_config = self.group_aaa_server_group(config,server_group)
                    grouped_configs += server_group_config
                    grouped_configs.append('!')
                if '  anyconnect profiles value' in cfg_line:
                    grouped_configs += self.get_anyconnect_profile(config,profile_name)
                    grouped_configs.append('!')
                tg_configs.append(cfg_line)
            grouped_configs += tg_configs
            grouped_configs.append('\n\n!---\n\n')
        return grouped_configs
