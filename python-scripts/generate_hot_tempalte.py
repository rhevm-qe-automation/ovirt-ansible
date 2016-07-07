#!/bin/python2

import argparse
import sys
import os.path
import yaml
import datetime

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Parser for orchestration with openstack heat and ansible'
                    '.\n This script is preparing environment for running '
                    'multiple instances of engine over openstack HOT. Run '
                    'this script multiple times on the same time to add more '
                    'instances withdifferent prefix, system version, or remove'
                    ' old ones.'
    )
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        '--engine36', '-3', help='Machine for engine 3.6', action='store_true'
    )
    group.add_argument(
        '--engine40', '-4', help='Machine for engine 4.0 (default)',
        action='store_true'
    )
    parser.add_argument_group(group)
    parser.add_argument(
        '--dwh', '-d', action='store', default='local', dest='dwh',
        help='Choose dwh from "none", "local", "remote", to either disable '
             'dwh, install it locally or to remote machine'
    )
    parser.add_argument(
        '--remote-db', action='store_true',
        default=False, help='New instance for remote db'
    )
    parser.add_argument(
        '--remote-dwh-db', action='store_true',
        default=False, help='New instance for remote dwh db'
    )
    parser.add_argument(
        '--file', '-f', default='/tmp/hot.yaml',
        help='Specify path and file name to hot template'
    )
    parser.add_argument(
        '--hot-help',  action='store_true',
        help='Help for openstack Heat Orchestration Template'
    )
    parser.add_argument(
        '--prefix', '-p', help='Prefix for name for the instance',
        default='engine'
    )
    parser.add_argument(
        '--delete', '-D', help='Remove this machine from template',
        action='store_true', default=False
    )
    args = parser.parse_args()

    # Check conflicting arguements
    if args.hot_help:
        print 'For HOT usage it is necessary to set up credentials file to ' \
              'openstack. \nParameters file should contain at least these ' \
              'arguments:'
        print '\tpublic_net: \t\tNetwork interface to connect within the stack'
        print '\tkey_name: \t\tSsh key added to open stack instance'
        print '\tflavor: \t\tFlavor of instance specified within open stack.'
        print '\timage_engine36: \timage name for engine36'
        print '\timage_engine40: \timage name for engine40'
        sys.exit(0)
    if args.dwh not in ["local", "remote", "none"]:
        sys.stderr.write(
            'Incorrect value for argument --dwh/-d: ' + args.dwh + '\n'
        )
        sys.exit(1)
    if args.dwh not in ["local", "remote"] and args.remote_dwh_db:
        sys.stderr.write(
            'Conflicting arguements "--dwh/-d: none" and "--remote-dwh-db\n'
        )
        sys.exit(1)
    if args.dwh not in ["local", "remote"] and args.engine40:
        sys.stderr.write(
            'Conflicting arguements "--dwh/-d: none" and "--engine40/-4\n'
            'Datawarehouse is mandatory in engine 4.0 version\n'
        )
        sys.exit(1)

    if not os.path.isfile(args.file):
        hot = dict()

        # add description
        hot['description'] = 'HOT template for ovirt jobs'

        # add template version
        hot['heat_template_version'] = datetime.date.today()

        # add parameters
        params = dict()
        hot['parameters'] = params

        param_flavor = dict()
        params['flavor'] = param_flavor
        param_flavor['description'] = 'Flavor to use for servers'
        param_flavor['type'] = 'string'

        param_img36 = dict()
        params['image_36'] = param_img36
        param_img36['description'] = 'Name of image to use for engine-36'
        param_img36['type'] = 'string'

        param_img40 = dict()
        params['image_40'] = param_img40
        param_img40['description'] = 'Name of image to use for ovirt-40'
        param_img40['type'] = 'string'

        param_key_name = dict()
        params['key_name'] = param_key_name
        param_key_name['description'] = 'Name of keypair to assign to servers'
        param_key_name['type'] = 'string'

        param_public_net = dict()
        params['public_name'] = param_public_net
        param_public_net['description'] = 'ID or name of public network for ' \
                                          'which floating addresses will be ' \
                                          'allocated'
        param_public_net['type'] = 'string'

        # add resources
        resources = dict()
        hot['resources'] = resources

        disable_requiretty = dict()
        resources['disable_requiretty'] = disable_requiretty

        dis_properties = dict()
        disable_requiretty['properties'] = dis_properties
        disable_requiretty['type'] = 'OS::Heat::SoftwareConfig'

        dis_properties['config'] = "#!/bin/sh\nsed -i -e 's/^Defaults\\s\\+" \
                                   "requiretty/# \\0/' /etc/sudoers\n"
        dis_properties['group'] = 'ungrouped'

        # add outputs
        hot['outputs'] = dict()
        if not args.delete:
            with open(args.file, 'w') as f:
                f.write(yaml.dump(hot, default_flow_style=False))

    hot_template = dict()
    with open(args.file, 'r') as f:
        hot_template = yaml.load(f)

    instances = list()
    instances.append(args.prefix)
    machines_count = 1
    if args.remote_db:
        instances.append(args.prefix + "_remote_db")

    if args.dwh == "remote":
        instances.append(args.prefix + "_dwh")

    if args.remote_dwh_db:
        instances.append(args.prefix + "_remote_dwh_db")

    # remove old template instances with same prefix
    suffix = "_36" if args.engine36 else "_40"
    for i in [
        args.prefix + suffix,
        args.prefix + "_dwh" + suffix,
        args.prefix + "_remote_db" + suffix,
        args.prefix + "_remote_dwh_db" + suffix
    ]:
        if i in hot_template['resources']:
            hot_template['resources'].pop(i)
            hot_template['outputs'].pop(i+'_public_ip')
    if args.delete:
        with open(args.file, 'w') as f:
            yaml.dump(hot_template, f, default_flow_style=False)
        exit(1)
    for i, s in enumerate(instances):
        instances[i] = s+suffix

    for name in instances:
        # add spawned instance
        vm = dict()
        hot_template['resources'][name] = vm

        vm['type'] = 'OS::Nova::Server'
        vm_properties = dict()
        vm['properties'] = vm_properties

        vm_flavor = dict()
        vm_properties['flavor'] = vm_flavor
        vm_flavor['get_param'] = 'flavor'

        vm_image = dict()
        vm_properties['image'] = vm_image
        vm_image['get_param'] = 'image_36' if args.engine36 else 'image_40'

        vm_keyname = dict()
        vm_properties['key_name'] = vm_keyname
        vm_keyname['get_param'] = 'key_name'

        vm_properties['name'] = name

        vm_networks = list()
        vm_properties['networks'] = vm_networks
        vm_network = dict()
        vm_networks.append(vm_network)
        vm_network_param = dict()
        vm_network['network'] = vm_network_param
        vm_network_param['get_param'] = 'public_net'

        vm_user_data = dict()
        vm_properties['user_data'] = vm_user_data
        vm_user_data['get_resource'] = 'disable_requiretty'

        vm_properties['user_data_format'] = 'SOFTWARE_CONFIG'

        # add outputs
        outputs = hot_template['outputs']
        # add ip address as output
        output = dict()
        outputs[name + '_public_ip'] = output
        output['description'] = 'Floating IP address of instance ' + name
        output['value'] = {'get_attr': [name, 'first_address']}
    with open(args.file, 'w') as f:
        yaml.dump(hot_template, f, default_flow_style=False)
