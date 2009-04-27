# TODO:
# - optional package with dev files / links to dev
Summary:	Bootstrap a basic Debian system
Summary(pl.UTF-8):	Instalator podstawowego systemu opartego o pakiety deb
Name:		debootstrap
Version:	1.0.13
Release:	1
License:	Freeware
Group:		Applications/File
Source0:	http://ftp.debian.org/debian/pool/main/d/debootstrap/%{name}_%{version}.tar.gz
# Source0-md5:	38fe16f65419816e5cc8c72ef9feb66a
Source1:	devices.tar.gz
BuildRequires:	sed >= 4.0
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
%setup -q -n %{name}
sed -i -e "s|@VERSION@|%{version}|g" %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_datadir}/%{name}/scripts}

install %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}
install %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8

install scripts/debian/* $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts
install scripts/ubuntu/* $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts

ln -sf sid $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/etch
ln -sf sid $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/etch-m68k
ln -sf sid $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/lenny
ln -sf sid $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/squeezy
ln -sf gutsy $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/hardy
ln -sf gutsy $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/intrepid
ln -sf gutsy $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/jaunty

install functions $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc debian/README.Debian debian/copyright debian/changelog
%attr(755,root,root) %{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/functions
%{_datadir}/%{name}/devices.tar.gz
