Summary:	A packrat parser implementation for Ruby
Name:		ruby-treetop
Version:	1.3.0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/treetop-1.3.0.gem
# Source0-md5:	a1fbf9629f8052eeff592d437c8b47a6
Patch0:	%{name}-gems.patch
URL:		http://treetop.rubyforge.org
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Treetop is a Ruby-based DSL for text parsing and interpretation. It
facilitates an extension of the object-oriented paradigm called
syntax-oriented programming. There's a readme that will get you going and some
examples.

%prep
%setup -q -c -n treetop-%{version}
tar xzf data.tar.gz
cp %{_datadir}/setup.rb .
%patch0 -p1

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

rm ri/created.rid ri/String/cdesc-String.yaml
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%attr(755,root,root) %{_bindir}/tt
%{ruby_rubylibdir}/treetop*
%{ruby_ridir}/*
