Gem::Specification.new do |s|
  s.name        = 'basic-ruby'
  s.version     = '0.0.1'
  s.licenses    = ['MIT']
  s.summary     = "Belajar membuat Gem paket ruby"
  s.description = "Gem ini berisi source ruby dari basic sampai oop"
  s.authors     = ["Mukharomdev"]
  s.email       = 'mukharomdev@gmail.com'
  s.files       = ["lib/main.rb"]
  s.homepage    = 'https://rubygems.org/gems/basic-ruby'
  s.metadata    = { "source_code_uri" => "https://github.com/mukharomdev/mukharomdev.git" }
  s.extra_rdoc_files = ['README.md', 'docs/Makefile']
  s.required_ruby_version = '>= 2.7.0'
  # or without Rake...
  s.files = Dir['lib/**/*.rb'] + Dir['bin/*']
  s.files += Dir['[A-Z]*']
  s.files.reject! { |fn| fn.include? "git" }
  # platform
  s.platform = Gem::Platform.local
  s.bindir = 'bin'
  # s.executables << 'rake'
  s.post_install_message = "Terima kasih sudah Menginstall!"
end 