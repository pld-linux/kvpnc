%define		_beta	rm+zomb.1
Summary:	GUI for VPN Client for Cisco EasyVPN
Summary(pl):	GUI dla klienta vpn dla Cisco EasyVPN
Name:		kvpnc
Version:	0.5.1
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://download.gna.org/kvpnc/%{name}-%{version}.tar.bz2
# Source0-md5:	989c0d3857380f9a01272550e4dc524a
URL:		http://home.gna.org/kvpnc/
BuildRequires:	kdelibs-devel >= 3.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
Requires:	vpnc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUI for vpnc.

%description -l pl
GUI dla klienta vpnc.

%prep
%setup -q

%build
%{__sed} -i 's,<UI version="3.1",<UI version="3.2",' src/*.ui
%{__make} -f admin/Makefile.common
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/config,%{_desktopdir},%{_sbindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}
	
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Internet/%{name}.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
mv -f $RPM_BUILD_ROOT%{_bindir}/%{name} \
	$RPM_BUILD_ROOT%{_sbindir}/%{name}

echo "Categories=Qt;KDE;System;X-Administration;" >> \
	$RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
echo "Comment[pl]=Klient vpnc dla KDE" >> \
	$RPM_BUILD_ROOT%{_datadir}/apps/kvpnc/eventsrc

install src/%{name}ui.rc $RPM_BUILD_ROOT%{_datadir}/config

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/apps/kvpnc
%{_datadir}/config/*
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/*/*
