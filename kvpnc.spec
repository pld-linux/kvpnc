%define		_beta	rm+zomb.1
Summary:	GUI for VPN Client for Cisco EasyVPN
Summary(pl):	GUI dla klienta vpn dla Cisco EasyVPN
Name:		kvpnc
Version:	0.4.1.2
Release:	0.3
License:	GPL
Group:		Networking/Daemons
Source0:	http://download.gna.org/kvpnc/%{name}-%{version}.tar.gz
# Source0-md5:	005a412ddd0fc6f1f8d753fd73e6fb1b
URL:		http://home.gna.org/kvpnc/
BuildRequires:	kdelibs-devel
Requires:	vpnc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUI for cvpn.

%description -l pl
GUI dla Klienta cvpn.

%prep
%setup -q

%build
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/config,%{_desktopdir}}

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

install src/%{name}ui.rc $RPM_BUILD_ROOT%{_datadir}/config
install src/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/*/*/*/%{name}*
%{_datadir}/apps/*
%{_datadir}/config/*
%{_desktopdir}/%{name}.desktop
