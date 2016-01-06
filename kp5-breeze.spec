%define		kdeplasmaver	5.4.0
%define		qtver		5.3.2
%define		kpname		breeze
Summary:	Artwork, styles and assets for the Breeze visual style for the Plasma Desktop
Name:		kp5-%{kpname}
Version:	5.4.0
Release:	4
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	ddaa82ee94af4bdf4271132191635968
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
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
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Artwork, styles and assets for the Breeze visual style for the Plasma
Desktop.

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
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang breeze --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f breeze.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/breeze-settings5
%attr(755,root,root) %{_libdir}/kconf_update_bin/gtkbreeze
%attr(755,root,root) %{_libdir}/kconf_update_bin/kde4breeze
%attr(755,root,root) %{_libdir}/qt5/plugins/kstyle_breeze_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kdecoration2/breezedecoration.so
%attr(755,root,root) %{_libdir}/qt5/plugins/styles/breeze.so
%{_libdir}/qt5/qml/QtQuick/Controls/Styles/Breeze
%dir %{_datadir}/QtCurve
%{_datadir}/QtCurve/Breeze.qtcurve
%{_datadir}/color-schemes/Breeze.colors
%{_datadir}/color-schemes/BreezeDark.colors
%{_datadir}/color-schemes/BreezeHighContrast.colors
%{_iconsdir}/Breeze_Snow
%{_iconsdir}/breeze-dark
%{_iconsdir}/breeze
%{_iconsdir}/breeze_cursors
%{_iconsdir}/hicolor/scalable/apps/breeze-settings.svgz
%{_datadir}/kconf_update/gtkbreeze.upd
%{_datadir}/kconf_update/kde4breeze.upd
%{_datadir}/kservices5/breezedecorationconfig.desktop
%{_datadir}/kservices5/breezestyleconfig.desktop
%{_datadir}/kstyle/themes/breeze.themerc
%{_datadir}/wallpapers/Next
