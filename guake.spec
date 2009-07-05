Summary:	guake - a drop-down terminal
Summary(pl.UTF-8):	guake - wyskakujący terminal
Name:		guake
Version:	0.3.1
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://guake-terminal.org/releases/0.3.1/%{name}-%{version}.tar.gz
# Source0-md5:	ed7af9e0309ba0df08a521b1ef4423ef
URL:		http://guake-terminal.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	python-pygtk-devel
BuildRequires:	python-vte
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

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

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
