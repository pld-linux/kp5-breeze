%define		kdeplasmaver	%{version}
%define		qtver		5.3.2
%define		kpname		breeze
Summary:	Artwork, styles and assets for the Breeze visual style for the Plasma Desktop
Name:		kp5-%{kpname}
Version:	5.5.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	84a0914f9b1934331ea76919aa93f0b1
URL:		https://projects.kde.org/projects/kde/workspace/breeze
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	hardlink
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
BuildRequires:	kf5-kpackage-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	kp5-kdecoration-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-qmake
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{kpname}-cursor-theme = %{version}-%{release}
Requires:	%{kpname}-icon-theme >= %{version}
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Artwork, styles and assets for the Breeze visual style for the Plasma
Desktop.

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
%{__make} -C build install/fast \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/icons/breeze_cursors
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/icons/Breeze_Snow

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/breeze-settings5
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
%{_datadir}/kconf_update/kde4breeze.upd
%{_datadir}/kservices5/breezedecorationconfig.desktop
%{_datadir}/kservices5/breezestyleconfig.desktop
%{_datadir}/kservices5/plasma-lookandfeel-org.kde.breezedark.desktop.desktop
%{_datadir}/kstyle/themes/breeze.themerc
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/defaults
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/previews/preview.png
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/metadata.desktop
%{_datadir}/wallpapers/Next

%files -n %{kpname}-cursor-theme
%defattr(644,root,root,755)
%{_iconsdir}/Breeze_Snow
%{_iconsdir}/breeze_cursors
