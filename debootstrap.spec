# TODO:
# - optional package with dev files / links to dev
# - still problems on amd64 :/
Summary:	Bootstrap a basic Debian system
Summary(pl):	Zainstaluj Debiana
Name:		debootstrap
Version:	0.2.45
Release:	0.1
License:	Freeware
Group:		Applications/File
Source0:	http://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.gz
# Source0-md5:	faac4b6cb7f278f64a68e4d45a26ae53
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
%setup -q

%build
%{__make} pkgdetails
sed -i -e "s@/usr/lib/@%{_libdir}/@g" %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}
install -D %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8

install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts
install slink potato woody sarge sid woody.buildd sarge.buildd sid.buildd \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/scripts
install pkgdetails functions $RPM_BUILD_ROOT%{_libdir}/%{name}
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
