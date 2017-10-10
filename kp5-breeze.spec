%define		kdeplasmaver	5.11.0
%define		qtver		5.3.2
%define		kpname		breeze
Summary:	Artwork, styles and assets for the Breeze visual style for the Plasma Desktop
Name:		kp5-%{kpname}
Version:	5.11.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	074959777749a3cb305b0fa29f721f45
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	hardlink >= 1.0-3
BuildRequires:	kf5-attica-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-frameworkintegration-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kcodecs-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kguiaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kp5-kdecoration-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-qmake
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{kpname}-cursor-theme = %{version}-%{release}
Requires:	%{kpname}-icon-theme = %{version}-%{release}
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Artwork, styles and assets for the Breeze visual style for the Plasma
Desktop.

%package devel
Summary:	Breeze devel
Summary(pl.UTF-8):	Breeze devel
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description devel
Artwork, styles and assets for the Breeze visual style for the Plasma
Desktop. Devel files

%package -n %{kpname}-icon-theme
Summary:	Breeze icon theme
Summary(pl.UTF-8):	Breeze Motyw ikon
Group:		Themes
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Conflicts:	kp5-breeze < 5.4.0-5
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n %{kpname}-icon-theme
Breeze is an icon theme.

%description -n %{kpname}-icon-theme -l pl.UTF-8
Breeze to motyw ikon.

%package -n %{kpname}-cursor-theme
Summary:	Breeze cursor theme
Group:		Themes
Conflicts:	breeze-icon-theme < 5.4.0-7
Conflicts:	kp5-breeze < 5.4.0-5
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n %{kpname}-cursor-theme
Breeze cursor theme.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/{breeze-dark,breeze}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

touch $RPM_BUILD_ROOT%{_iconsdir}/breeze-dark/icon-theme.cache
touch $RPM_BUILD_ROOT%{_iconsdir}/breeze/icon-theme.cache

hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/icons/breeze_cursors
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/icons/Breeze_Snow

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%post -n %{kpname}-icon-theme
%update_icon_cache breeze
%update_icon_cache breeze-dark

%postun -n %{kpname}-icon-theme
%update_icon_cache breeze
%update_icon_cache breeze-dark

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/breeze-settings5
#%%attr(755,root,root) %{_libdir}/kconf_update_bin/gtkbreeze
%attr(755,root,root) %{_libdir}/kconf_update_bin/kde4breeze
%attr(755,root,root) %{_libdir}/qt5/plugins/kstyle_breeze_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kdecoration2/breezedecoration.so
%attr(755,root,root) %{_libdir}/qt5/plugins/styles/breeze.so
%{_iconsdir}/hicolor/scalable/apps/breeze-settings.svgz
%{_libdir}/qt5/qml/QtQuick/Controls/Styles/Breeze
%dir %{_datadir}/QtCurve
%{_datadir}/QtCurve/Breeze.qtcurve
%{_datadir}/color-schemes/Breeze.colors
%{_datadir}/color-schemes/BreezeDark.colors
%{_datadir}/color-schemes/BreezeHighContrast.colors
#%%{_datadir}/kconf_update/gtkbreeze.upd
%{_datadir}/kconf_update/kde4breeze.upd
%{_datadir}/kservices5/breezedecorationconfig.desktop
%{_datadir}/kservices5/breezestyleconfig.desktop
#%%{_datadir}/kservices5/plasma-lookandfeel-org.kde.breezedark.desktop.desktop
%{_datadir}/kstyle/themes/breeze.themerc
%{_datadir}/wallpapers/Next

%dir %{_datadir}/plasma/look-and-feel
%dir %{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop
%dir %{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents
%dir %{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/previews
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/defaults
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/previews/preview.png
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/metadata.desktop
/usr/share/metainfo/org.kde.breezedark.desktop.appdata.xml
/usr/share/plasma/look-and-feel/org.kde.breezedark.desktop/metadata.json


%files -n %{kpname}-icon-theme
%defattr(644,root,root,755)
%dir %{_iconsdir}/breeze-dark
%ghost %{_iconsdir}/breeze-dark/icon-theme.cache

%dir %{_iconsdir}/breeze
%ghost %{_iconsdir}/breeze/icon-theme.cache

%files -n %{kpname}-cursor-theme
%defattr(644,root,root,755)
%{_iconsdir}/Breeze_Snow
%{_iconsdir}/breeze_cursors

%files devel
%defattr(644,root,root,755)
/usr/lib64/cmake/Breeze
