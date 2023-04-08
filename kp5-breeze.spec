#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.4
%define		qtver		5.15.2
%define		kpname		breeze
Summary:	Artwork, styles and assets for the Breeze visual style for the Plasma Desktop
Name:		kp5-%{kpname}
Version:	5.27.4
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	63260b77048292c05c453b0f3a1f7d6e
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	fftw3-devel
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
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-qmake
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{kpname}-cursor-theme = %{version}-%{release}
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	kf5-breeze-icons
Requires:	kp5-breeze-data = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Artwork, styles and assets for the Breeze visual style for the Plasma
Desktop.

%package data
Summary:	Data files for %{kpname}
Summary(pl.UTF-8):	Dane dla %{kpname}
Group:		X11/Applications
BuildArch:	noarch

%description data
Data for %{kpname}.

%description data -l pl.UTF-8
Dane dla %{kpname}.

%package devel
Summary:	Breeze devel
Summary(pl.UTF-8):	Breeze devel
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description devel
Artwork, styles and assets for the Breeze visual style for the Plasma
Desktop. Devel files

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%package -n %{kpname}-cursor-theme
Summary:	Breeze cursor theme
Group:		Themes
Conflicts:	breeze-icon-theme < 5.4.0-7
Conflicts:	kp5-breeze < 5.4.0-5
BuildArch:	noarch

%description -n %{kpname}-cursor-theme
Breeze cursor theme.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/{breeze-dark,breeze}
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/icons/breeze_cursors
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/icons/Breeze_Snow

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/breeze-settings5
%{_libdir}/qt5/plugins/org.kde.kdecoration2/breezedecoration.so
%{_libdir}/qt5/plugins/styles/breeze.so
%ghost %{_libdir}/libbreezecommon5.so.5
%attr(755,root,root) %{_libdir}/libbreezecommon5.so.5.*.*
%attr(755,root,root) %{_libdir}/kconf_update_bin/breezetobreezelight
%attr(755,root,root) %{_libdir}/kconf_update_bin/breezehighcontrasttobreezedark
%attr(755,root,root) %{_libdir}/kconf_update_bin/breezetobreezeclassic
%dir %{_libdir}/qt5/plugins/plasma/kcms/breeze
%{_libdir}/qt5/plugins/plasma/kcms/breeze/kcm_breezedecoration.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/breezestyleconfig.so

%files data -f %{kpname}.lang
%defattr(644,root,root,755)
%{_iconsdir}/hicolor/scalable/apps/breeze-settings.svgz
%dir %{_datadir}/QtCurve
%{_datadir}/QtCurve/Breeze.qtcurve
%dir %{_datadir}/color-schemes
%{_datadir}/color-schemes/BreezeDark.colors
%{_datadir}/kstyle/themes/breeze.themerc
%{_datadir}/wallpapers/Next
%{_datadir}/color-schemes/BreezeLight.colors
%{_datadir}/kconf_update/breezetobreezelight.upd
%{_datadir}/color-schemes/BreezeClassic.colors
%{_datadir}/kconf_update/breezehighcontrasttobreezedark.upd
%{_datadir}/kconf_update/breezetobreezeclassic.upd
%{_desktopdir}/breezestyleconfig.desktop
%{_desktopdir}/kcm_breezedecoration.desktop

%files -n %{kpname}-cursor-theme
%defattr(644,root,root,755)
%{_iconsdir}/Breeze_Snow
%{_iconsdir}/breeze_cursors

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/Breeze
