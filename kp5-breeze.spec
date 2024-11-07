#
# Conditional build:
%bcond_with	tests	# test suite

%define		kdeplasmaver	5.27.11
%define		qt_ver		5.15.2
%define		kf_ver		5.102.0
%define		kpname		breeze
Summary:	Artwork, styles and assets for the Breeze visual style for the Plasma Desktop
Summary(pl.UTF-8):	Grafika, style i zasoby dla stylu Breeze środowiska Plasma Desktop
Name:		kp5-%{kpname}
Version:	5.27.11
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	cd682d5c0cea4f1d12671c534655b3fc
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5DBus-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5X11Extras-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-tools
BuildRequires:	hardlink >= 1.0-3
BuildRequires:	kf5-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf5-frameworkintegration-devel >= %{kf_ver}
BuildRequires:	kf5-kcmutils-devel >= %{kf_ver}
BuildRequires:	kf5-kconfig-devel >= %{kf_ver}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kf_ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kguiaddons-devel >= %{kf_ver}
BuildRequires:	kf5-ki18n-devel >= %{kf_ver}
BuildRequires:	kf5-kiconthemes-devel >= %{kf_ver}
BuildRequires:	kf5-kirigami2-devel >= %{kf_ver}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kwindowsystem-devel >= %{kf_ver}
BuildRequires:	kp5-kdecoration-devel
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	qt5-qmake >= %{qt_ver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{kpname}-cursor-theme >= %{version}-%{release}
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5DBus >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Quick >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	Qt5X11Extras >= %{qt_ver}
Requires:	kf5-breeze-icons
Requires:	kf5-frameworkintegration >= %{kf_ver}
Requires:	kf5-kcmutils >= %{kf_ver}
Requires:	kf5-kconfig >= %{kf_ver}
Requires:	kf5-kconfigwidgets >= %{kf_ver}
Requires:	kf5-kcoreaddons >= %{kf_ver}
Requires:	kf5-kguiaddons >= %{kf_ver}
Requires:	kf5-ki18n >= %{kf_ver}
Requires:	kf5-kiconthemes >= %{kf_ver}
Requires:	kf5-kirigami2 >= %{kf_ver}
Requires:	kf5-kwidgetsaddons >= %{kf_ver}
Requires:	kf5-kwindowsystem >= %{kf_ver}
Requires:	kp5-breeze-data = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Artwork, styles and assets for the Breeze visual style for the Plasma
Desktop.

%description -l pl.UTF-8
Grafika, style i zasoby dla stylu Breeze środowiska Plasma Desktop.

%package data
Summary:	Data files for %{kpname}
Summary(pl.UTF-8):	Dane dla %{kpname}
Group:		X11/Applications
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildArch:	noarch

%description data
Data for %{kpname}.

%description data -l pl.UTF-8
Dane dla %{kpname}.

%package -n %{kpname}-cursor-theme
Summary:	Breeze cursor theme
Summary(pl.UTF-8):	Motyw kursora Breeze
Group:		Themes
Conflicts:	breeze-icon-theme < 5.4.0-7
Conflicts:	kp5-breeze < 5.4.0-5
BuildArch:	noarch

%description -n %{kpname}-cursor-theme
Breeze cursor theme.

%description -n %{kpname}-cursor-theme -l pl.UTF-8
Motyw kursora Breeze.

%package devel
Summary:	Breeze development files
Summary(pl.UTF-8):	Pliki programistyczne stylu Breeze
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for Breeze style data.

%description devel -l pl.UTF-8
Pliki programistyczne danych stylu Breeze.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/{breeze-dark,breeze}

%ninja_install -C build

# breeze_kwin_deco, breeze_style_config domains
%find_lang %{kpname} --all-name

hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/icons/breeze_cursors
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/icons/Breeze_Snow

%clean
rm -rf $RPM_BUILD_ROOT

%post	data
%update_icon_cache hicolor

%postun	data
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/breeze-settings5
%attr(755,root,root) %{_libdir}/libbreezecommon5.so.*.*.*
%ghost %{_libdir}/libbreezecommon5.so.5
%attr(755,root,root) %{_libdir}/kconf_update_bin/breezetobreezelight
%attr(755,root,root) %{_libdir}/kconf_update_bin/breezehighcontrasttobreezedark
%attr(755,root,root) %{_libdir}/kconf_update_bin/breezetobreezeclassic
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kdecoration2/breezedecoration.so
%dir %{_libdir}/qt5/plugins/plasma/kcms/breeze
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/breeze/kcm_breezedecoration.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/breezestyleconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/styles/breeze.so

%files data -f %{kpname}.lang
%defattr(644,root,root,755)
%dir %{_datadir}/QtCurve
%{_datadir}/QtCurve/Breeze.qtcurve
%dir %{_datadir}/color-schemes
%{_datadir}/color-schemes/BreezeClassic.colors
%{_datadir}/color-schemes/BreezeDark.colors
%{_datadir}/color-schemes/BreezeLight.colors
%{_datadir}/kconf_update/breezehighcontrasttobreezedark.upd
%{_datadir}/kconf_update/breezetobreezeclassic.upd
%{_datadir}/kconf_update/breezetobreezelight.upd
%{_datadir}/kstyle/themes/breeze.themerc
%{_datadir}/wallpapers/Next
%{_desktopdir}/breezestyleconfig.desktop
%{_desktopdir}/kcm_breezedecoration.desktop
%{_iconsdir}/hicolor/scalable/apps/breeze-settings.svgz

%files -n %{kpname}-cursor-theme
%defattr(644,root,root,755)
%{_iconsdir}/Breeze_Snow
%{_iconsdir}/breeze_cursors

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/Breeze
