# TODO:
# - optional package with dev files / links to dev
# - still problems on amd64:/
Summary:	Bootstrap a basic Debian system
Summary(pl):	Zainstaluj Debiana
Name:		debootstrap
Version:	0.3.3
Release:	0.2
License:	Freeware
Group:		Applications/File
Source0:	http://ftp.debian.org/debian/pool/main/d/debootstrap/%{name}_%{version}.tar.gz
# Source0-md5:	22fcb8cc4218e582ad701b44e2549dce
Source1:	devices.tar.gz
Source2:	%{name}-etch
Source3:	%{name}-dapper
Source4:	%{name}-edgy
BuildRequires:	sed >= 4.0
Requires:	binutils
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Debootstrap is used to create a Debian base system from scratch,
without requiring the availability of dpkg or apt. It does this by
downloading .deb files from a mirror site, and carefully unpacking
them into a directory which can eventually be chrooted into.

%description -l pl
Debootstrap jest wykorzystywany do tworzenia podstawowego systemu
Debiana od podstaw, bez potrzeby dostêpno¶ci dpkg lub apt. ¦ci±ga
pliki .deb z serwera i ostro¿nie rozpakowuje je do katalogu, dok±d
mo¿esz siê nastêpnie chrootowaæ.

%prep
%setup -q -n %{version}

%build
%{__make} pkgdetails
sed -i -e "s@/usr/lib/@%{_libdir}/@g" %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}
install -D %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8

install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts
install breezy hoary warty potato woody sarge sid woody.buildd sarge.buildd hoary.buildd warty.buildd sarge.fakechroot \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/scripts
install pkgdetails functions $RPM_BUILD_ROOT%{_libdir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/%{name}/
install %{SOURCE2} $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts/etch
install %{SOURCE3} $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts/dapper
install %{SOURCE4} $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts/edgy
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
