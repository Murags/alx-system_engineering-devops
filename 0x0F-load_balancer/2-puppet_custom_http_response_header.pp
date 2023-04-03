# install nginx and add custom header

exec { 'update':
  command  => 'sudo apt -y update',
  provider => 'shell',
}

exec { 'nginx':
  command  => 'sudo apt -y install nginx',
  provider => 'shell',
}

exec { 'config':
  command  => 'sudo sed -i "/listen 80 default_server;/ a     add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell',
}

exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}
