# TODO:
# - optional package with dev files / links to dev
Summary:	Bootstrap a basic Debian system
Summary(pl.UTF-8):	Instalator podstawowego systemu opartego o pakiety deb
Name:		debootstrap
Version:	1.0.57
Release:	1
License:	MIT-like
Group:		Applications/File
Source0:	http://ftp.debian.org/debian/pool/main/d/debootstrap/%{name}_%{version}.tar.xz
# Source0-md5:	464c3d461ea396246c7966e6c6ebeb2c
Source1:	devices.tar.gz
# Source1-md5:	8c12b8d845b32080c6c769afb3376ada
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	binutils
Requires:	wget
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Debootstrap is used to create a Debian base system from scratch,
without requiring the availability of dpkg or apt. It does this by
downloading .deb files from a mirror site, and carefully unpacking
them into a directory which can eventually be chrooted into.

%description -l pl.UTF-8
Debootstrap jest wykorzystywany do tworzenia podstawowego systemu
Debiana od podstaw, bez potrzeby dostępności dpkg lub apt. Ściąga
pliki .deb z serwera i ostrożnie rozpakowuje je do katalogu, dokąd
możesz się następnie chrootować.

%prep
%setup -q
sed -i -e "s|@VERSION@|%{version}|g" %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_datadir}/%{name}}

install %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}
install %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8

cp -a scripts $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts

install functions $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO debian/copyright debian/changelog
%attr(755,root,root) %{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/functions
%{_datadir}/%{name}/devices.tar.gz
