# Install Nginx web server and configure nginx
exec { 'Install Nginx':
  command => 'sudo apt -y install nginx',
  path    => ['/usr/bin', '/bin'],
}

file_line { 'add_header':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  line     => '        add_header X-Served-By $hostname;',
  match    => '^(\s*)server_name\s+_;$',
  after    => 'server_name _;',
}

exec { 'Restart':
  require => Exec['Install Nginx'],
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
}
