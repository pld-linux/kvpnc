Summary:	GUI for VPN Client for various servers
Summary(pl.UTF-8):	GUI dla klienta dla różnych serwerów VPN
Name:		kvpnc
Version:	0.9.6a
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.gna.org/kvpnc/%{name}-%{version}-kde4.tar.bz2
# Source0-md5:	bf8b7224284f5d3f8ad5235c599fe9e7
Patch0:		sleep.patch
URL:		http://home.gna.org/kvpnc/en/index.html
BuildRequires:	automoc4
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
Requires:	bash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KVpnc is a KDE frontend for various VPN clients. It supports Cisco VPN
(vpnc) and IPSec (FreeS/WAN, racoon). vpnc is a replacement for the
Cisco VPN client, and is used as client for the cisco3000 VPN
Concentrator. FreeS/WAN (OpenS/WAN) is a IPSec client for Linux 2.4.x,
and raccoon is a IPSec client for Linux 2.6.x and *BSD. It also
supports PPTP (pptpclient) and OpenVPN.

%description -l pl.UTF-8
KVpnc to nakładka na klienta vpnc działajaca w środowisku KDE. Wspiera
Cisco VPN, IPSec (FreeS/WAN, racoon). vpnc jest zamiennikiem dla
klienta VPN Cisco, i jest używany jako klient dla koncentratorów VPN
cisco3000. FreeS/WAN (OpenS/WAN) jest klientem ipsecowym dla Linux
2.4.x oraz racoon w wersji 2.6.x oraz *BSD. Wspiera również protokół
PPTP (pptpclient) oraz OpenVPN.

%prep
%setup -q -n %{name}-%{version}-kde4
%patch0 -p1

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install/fast \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} -f $RPM_BUILD_ROOT%{_desktopdir}/{kde4,}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kvpnc
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/*/*
