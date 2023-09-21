Summary:	guake - a drop-down terminal
Summary(pl.UTF-8):	guake - wyskakujący terminal
Name:		guake
Version:	3.10
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://github.com/Guake/guake/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d06eb4b40645f6d71552418102ccc04e
Patch0:		set_scripts_path.patch
Patch1:		dont_try_compile_schemas.patch
Patch2:		dont_use_pip_to_build.patch
Patch3:		fix_manpage_name.patch
URL:		http://guake.org/
BuildRequires:	glib2
BuildRequires:	gettext-tools
BuildRequires:	intltool >= 0.35
BuildRequires:	pkgconfig
BuildRequires:	python3-pygobject3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pbr
BuildRequires:	python3-pip
BuildRequires:	python3-reno
BuildRequires:	python3-sphinxcontrib-programoutput
BuildRequires:	python3-wheel
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
Requires(post,postun):	desktop-file-utils
Requires:	dbus(org.freedesktop.Notifications)
Requires:	python3-pygobject3
Requires:	python3-notify2
Requires:	python3-pbr
BuildArch:	noarch
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
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make}
%{__make} -C docs man

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/glib-2.0/schemas,%{_mandir}/man1}

PBR_VERSION=%{version} \
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} \
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

cp -p docs/_build/man/guake.1 $RPM_BUILD_ROOT%{_mandir}/man1
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{py3_sitescriptdir}/guake
%{py3_sitescriptdir}/guake-%{version}-py*.egg-info
%{_datadir}/guake
%{_pixmapsdir}/guake.png
%{_desktopdir}/*.desktop
%{_datadir}/glib-2.0/schemas/org.guake.gschema.xml
%{_mandir}/man1/guake.1*
%{_metainfodir}/guake.desktop.metainfo.xml
