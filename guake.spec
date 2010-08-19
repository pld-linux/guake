# TODO
# - package autostart script: /etc/xdg/autostart/guake.desktop
Summary:	guake - a drop-down terminal
Summary(pl.UTF-8):	guake - wyskakujący terminal
Name:		guake
Version:	0.4.1
Release:	4
License:	GPL v2+
Group:		X11/Applications
Source0:	http://guake.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	c3bd763f0a7c91cb453c32d8045fa6ca
Patch0:		%{name}-desktop.patch
URL:		http://guake-terminal.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.35
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel
BuildRequires:	python-vte
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	dbus(org.freedesktop.Notifications)
Requires:	python-gnome-gconf
Requires:	python-pygtk-glade
Requires:	python-pynotify
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guake is a drop-down terminal for Gnome Desktop Environment, so you
just need to press a key to invoke him, and press again to hide.

%description -l pl.UTF-8
Guake to wyskakujący terminal dla Gnome, a więc wystarczy nacisnąć
przycisk aby go wywołać i nacisnąć ponownie by schować.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/guake/*.la

mv $RPM_BUILD_ROOT%{_datadir}/locale/{no,nb}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%gconf_schema_install guake.schemas

%preun
%gconf_schema_uninstall guake.schemas

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/guake
%attr(755,root,root) %{_libdir}/guake/*.so
%{_libdir}/guake/*.py
%{_datadir}/guake
%{_pixmapsdir}/guake
%{_desktopdir}/*.desktop
%{_datadir}/dbus-1/services/org.gnome.Guake.service
%{_sysconfdir}/gconf/schemas/guake.schemas
%{_mandir}/man1/guake.1*
