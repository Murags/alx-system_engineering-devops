# Install Nginx web server and configure nginx
exec { 'Install Nginx':
  command => 'sudo apt -y install nginx',
  path    => ['/usr/bin', '/bin'],
}

exec { 'config':
  command  => 'sudo sed -i \'/listen 80 default_server;/ a \\t add_header X-Served-By $hostname;\' /etc/nginx/sites-available/default',
  provider => 'shell',
}

exec { 'Restart':
  require => Exec['Install Nginx'],
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
}
