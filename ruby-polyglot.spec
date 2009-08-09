Summary:	A file-type handler for Ruby code
Name:		ruby-polyglot
Version:	0.2.6
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/polyglot-%{version}.gem
# Source0-md5:	f5be7fc78a711af7e9a4454d28972a2b
URL:		http://polyglot.rubyforge.org
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polyglot provides support for fully-custom DSLs by providing a registry of
file types that can be loaded by its improved version of ‘require’,
using a custom loader for each file type.

%prep
%setup -q -c -n polyglot-%{version}
tar xzf data.tar.gz
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

rm ri/created.rid
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/polyglot*
%{ruby_ridir}/*
