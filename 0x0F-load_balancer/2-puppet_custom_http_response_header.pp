# install nginx and add custom header

exec { 'update':
  command  => 'sudo apt -y update',
  provider => 'shell',
  before   => Exec['install_nginx'],
}

exec { 'install_nginx':
  command  => 'sudo apt -y install nginx',
  provider => 'shell',
  before   => Exec['configuration'],
}

exec { 'configuration':
  command  => 'sudo sed -i "/listen 80 default_server;/ a     add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell',
  before   => Exec['restart'],
}

exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}
