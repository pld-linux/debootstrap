# TODO:
# - optional package with dev files / links to dev
# - still problems on amd64:/
Summary:	Bootstrap a basic Debian system
Summary(pl.UTF-8):	Zainstaluj Debiana
Name:		debootstrap
Version:	0.3.3.3
Release:	0.3
License:	Freeware
Group:		Applications/File
Source0:	http://ftp.debian.org/debian/pool/main/d/debootstrap/%{name}_%{version}.tar.gz
# Source0-md5:	d7bbf38b336b6491e0ae6db847b4cfd0
Source1:	devices.tar.gz
Source2:	%{name}-etch
Source3:	%{name}-dapper
Source4:	%{name}-edgy
Source5:	%{name}-feisty
Source6:	%{name}-feisty.fakechroot
Source7:	%{name}-gutsy
Source8:	%{name}-gutsy.fakechroot
BuildRequires:	dpkg
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
%setup -q

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
install %{SOURCE5} $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts/feisty
install %{SOURCE6} $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts/feisty.fakechroot
install %{SOURCE7} $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts/gutsy
install %{SOURCE8} $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts/gutsy.fakechroot
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
