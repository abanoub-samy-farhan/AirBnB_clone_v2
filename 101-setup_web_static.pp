# Puppet manifest to setup web servers for web_static deployment

file { '/data/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'root',
  group  => 'root',
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;

                root /var/www/html;

                index index.html index.htm index.nginx-debian.html;

                server_name _;

                location /hbnb_static {
                        alias /data/web_static/current/;
                }

                location / {
                        try_files \$uri \$uri/ =404;
                }
        }",
  notify => Service['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => 'true',
  require => File['/etc/nginx/sites-available/default'],
}

