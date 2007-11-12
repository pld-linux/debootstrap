# TODO:
# - optional package with dev files / links to dev
# - still problems on amd64:/
Summary:	Bootstrap a basic Debian system
Summary(pl.UTF-8):	Zainstaluj Debiana
Name:		debootstrap
Version:	1.0.6
Release:	1
License:	Freeware
Group:		Applications/File
Source0:	http://archive.ubuntulinux.org/ubuntu/pool/main/d/debootstrap/%{name}_%{version}.tar.gz
# Source0-md5:	e0baaef6140b6a1c87d2181ecbfb2b42
Source1:	devices.tar.gz
BuildRequires:	sed >= 4.0
Requires:	binutils
Requires:	wget
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

%build
%{__make} pkgdetails
sed -i -e "s@/usr/lib/@%{_libdir}/@g" %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}
install -D %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8

install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts
install scripts/debian/* $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts
install scripts/ubuntu/* $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts
ln -sf sid $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts/etch
ln -sf sid $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts/lenny
ln -sf gutsy $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts/hardy

install pkgdetails functions $RPM_BUILD_ROOT%{_libdir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/%{name}/
echo %{_arch} >$RPM_BUILD_ROOT%{_libdir}/%{name}/arch

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc debian/README.Debian debian/copyright
%attr(755,root,root) %{_sbindir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/pkgdetails
%{_mandir}/man?/%{name}.*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/scripts
%{_libdir}/%{name}/functions
%{_libdir}/%{name}/arch
%{_libdir}/%{name}/devices.tar.gz
