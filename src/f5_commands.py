f5_knowledge_base = {
    'VIP_DOWN': {
        'root_cause': 'The Virtual IP (VIP) is not reachable.',
        'troubleshooting_steps': [
            'Check if the pool members are online.',
            'Verify network connectivity to the VIP.',
            'Check if any firewalls are blocking access.'
        ],
        'commands': [
            'show pool',
            'show running-config',
            'ping <VIP>'
        ],
        'fixes': [
            'Remove unhealthy pool members.',
            'Adjust firewall rules if applicable.',
            'Restart relevant services if needed.'
        ]
    },
    'SSL_ISSUE': {
        'root_cause': 'SSL certificate problems.',
        'troubleshooting_steps': [
            'Check certificate validity.',
            'Verify SSL profile settings.',
            'Inspect logs for SSL errors.'
        ],
        'commands': [
            'show ssl certificates',
            'show ssl profiles',
            'tail -f /var/log/ssl.log'
        ],
        'fixes': [
            'Renew/replace expired certificates.',
            'Adjust SSL profile settings.',
            'Restart the HTTPS service.'
        ]
    },
    'TIMEOUT': {
        'root_cause': 'Connection timeout issues.',
        'troubleshooting_steps': [
            'Check for high latency on the network.',
            'Review server logs for timeout errors.',
            'Verify configuration settings for timeouts.'
        ],
        'commands': [
            'show performance',
            'show connections',
            'show running-config'
        ],
        'fixes': [
            'Optimize network paths.',
            'Increase timeout settings as necessary.',
            'Review and optimize application performance.'
        ]
    }
}