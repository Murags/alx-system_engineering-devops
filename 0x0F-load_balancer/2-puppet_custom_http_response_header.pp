# Install Nginx web server and configure nginx
exec { 'Install Nginx':
  command => 'sudo apt -y install nginx',
  path    => ['/usr/bin', '/bin'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'redirect':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'listen 80 default_server;',
  line     => 'add_header X-Served-By $hostname;',
  multiple => true
}

exec { 'Restart':
  require => Exec['Install Nginx'],
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
}
